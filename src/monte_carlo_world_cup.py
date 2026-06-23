from __future__ import annotations

import json
import math
import sys
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import DefaultDict, Deque, Iterable, Iterator, Sequence

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.build_dataset import (  # noqa: E402
    WINDOW_SIZE,
    actual_scores,
    expected_score,
    get_k_value,
    normalize_bool,
)
from src.model_features import (  # noqa: E402
    TeamState,
    align_feature_columns,
    load_artifacts,
    make_team_state,
    preprocess_features,
    reconstruct_state,
    team_state_to_feature_row,
    update_team_histories,
)


try:
    from importlib import import_module

    tqdm = import_module("tqdm").tqdm
except Exception:
    def tqdm(iterable: Iterable, **_: object) -> Iterable:
        return iterable


RANDOM_SEED = 42
N_SIMULATIONS = 1000
GROUP_ORDER = list("ABCDEFGHIJKL")

HISTORICAL_PATH = PROJECT_ROOT / "data" / "results_enriched.csv"
FIXTURE_PATH = PROJECT_ROOT / "data" / "mundial_2026.csv"
RESULTS_DIR = PROJECT_ROOT / "results"
WCSIMS_PATH = RESULTS_DIR / "wcsims.json"
PROBABILITIES_CSV_PATH = RESULTS_DIR / "world_cup_probabilities.csv"
SUMMARY_JSON_PATH = RESULTS_DIR / "simulation_summary.json"

GROUP_STAGE_POINTS_WIN = 3
GROUP_STAGE_POINTS_DRAW = 1


@dataclass(frozen=True)
class MatchPrediction:
    home_team: str
    away_team: str
    lambda_home: float
    lambda_away: float
    home_goals: int
    away_goals: int
    extra_time_home_goals: int = 0
    extra_time_away_goals: int = 0
    decided_by_penalties: bool = False
    winner: str | None = None


def load_csv(path: Path) -> pd.DataFrame:

    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return pd.read_csv(path)


def normalize_group_value(value: object) -> str | None:
    if pd.isna(value):
        return None
    text = str(value).strip()
    return text if text else None


def parse_bool(value: object) -> bool:
    return normalize_bool(value)


_HOME_AWAY_RENAME = {
    "home_team": "away_team", "away_team": "home_team",
    "home_elo_before": "away_elo_before", "away_elo_before": "home_elo_before",
    "home_elo_change_last_5": "away_elo_change_last_5", "away_elo_change_last_5": "home_elo_change_last_5",
    "home_wins_last_5": "away_wins_last_5", "away_wins_last_5": "home_wins_last_5",
    "home_goals_for_last_5": "away_goals_for_last_5", "away_goals_for_last_5": "home_goals_for_last_5",
    "home_goals_against_last_5": "away_goals_against_last_5", "away_goals_against_last_5": "home_goals_against_last_5",
    "home_attack_strength": "away_attack_strength", "away_attack_strength": "home_attack_strength",
    "home_defense_strength": "away_defense_strength", "away_defense_strength": "home_defense_strength",
}


class GoalPredictor:

    def __init__(self) -> None:
        self.model, self.feature_columns = load_artifacts()

    def predict(self, feature_df: pd.DataFrame, neutral: bool = False) -> tuple[float, float]:

        if not neutral:
            return self._predict_single(feature_df)

        lambda_home, lambda_away = self._predict_single(feature_df)

        swapped = feature_df.copy()
        swapped = swapped.rename(columns=_HOME_AWAY_RENAME)
        if "elo_diff" in swapped.columns:
            swapped["elo_diff"] = -swapped["elo_diff"]

        lambda_swapped_home, lambda_swapped_away = self._predict_single(swapped)

        return (
            (lambda_home + lambda_swapped_away) / 2,
            (lambda_away + lambda_swapped_home) / 2,
        )

    def _predict_single(self, feature_df: pd.DataFrame) -> tuple[float, float]:
        prepared = preprocess_features(feature_df)
        aligned = align_feature_columns(prepared, self.feature_columns)
        predictions = self.model.predict(aligned)
        return float(predictions[0, 0]), float(predictions[0, 1])


def simulate_group_match(
    row: pd.Series,
    states: dict[str, TeamState],
    predictor: GoalPredictor,
    rng: np.random.Generator,
) -> tuple[int, int, float, float]:

    neutral = parse_bool(row.get("neutral", True))
    feature_df = team_state_to_feature_row(
        str(row["home_team"]),
        str(row["away_team"]),
        row["tournament"],
        neutral,
        states,
        date=row.get("date", ""),
        city=row.get("city", ""),
        country=row.get("country", ""),
    )
    lambda_home, lambda_away = predictor.predict(feature_df, neutral=neutral)

    known_home = row.get("home_score")
    known_away = row.get("away_score")
    if pd.notna(known_home) and pd.notna(known_away):
        home_goals = int(known_home)
        away_goals = int(known_away)
    else:
        home_goals = int(rng.poisson(lambda_home))
        away_goals = int(rng.poisson(lambda_away))

    update_team_state_after_match(
        home_team=str(row["home_team"]),
        away_team=str(row["away_team"]),
        neutral=neutral,
        tournament=row.get("tournament", "FIFA World Cup"),
        states=states,
        home_goals=home_goals,
        away_goals=away_goals,
    )
    return home_goals, away_goals, lambda_home, lambda_away


def update_team_state_after_match(
    home_team: str,
    away_team: str,
    neutral: bool,
    tournament: object,
    states: dict[str, TeamState],
    home_goals: int,
    away_goals: int,
) -> None:

    home_team = str(home_team)
    away_team = str(away_team)

    home_state = states.setdefault(home_team, make_team_state())
    away_state = states.setdefault(away_team, make_team_state())

    home_elo_before = float(home_state.elo)
    away_elo_before = float(away_state.elo)

    expected_home = expected_score(home_elo_before, away_elo_before, neutral)
    expected_away = 1.0 - expected_home
    actual_home, actual_away = actual_scores(home_goals, away_goals)
    k_factor = get_k_value(tournament)

    home_state.elo = home_elo_before + k_factor * (actual_home - expected_home)
    away_state.elo = away_elo_before + k_factor * (actual_away - expected_away)

    update_team_histories(home_state, True, home_goals, away_goals, home_elo_before)
    update_team_histories(away_state, False, home_goals, away_goals, away_elo_before)


def simulate_knockout_match(
    home_team: str,
    away_team: str,
    date_value: object,
    tournament: str,
    city: str,
    country: str,
    neutral: bool,
    states: dict[str, TeamState],
    predictor: GoalPredictor,
    rng: np.random.Generator,
) -> tuple[str, str, dict[str, object]]:

    feature_df = team_state_to_feature_row(
        home_team,
        away_team,
        tournament,
        neutral,
        states,
        date=date_value,
        city=city,
        country=country,
    )
    lambda_home, lambda_away = predictor.predict(feature_df, neutral=neutral)

    home_goals = int(rng.poisson(lambda_home))
    away_goals = int(rng.poisson(lambda_away))

    extra_home_goals = 0
    extra_away_goals = 0
    decided_by_penalties = False

    if home_goals == away_goals:
        extra_home_goals = int(rng.poisson(lambda_home / 3.0))
        extra_away_goals = int(rng.poisson(lambda_away / 3.0))
        home_goals += extra_home_goals
        away_goals += extra_away_goals

        if home_goals == away_goals:
            decided_by_penalties = True
            winner = str(rng.choice([home_team, away_team]))
        else:
            winner = home_team if home_goals > away_goals else away_team
    else:
        winner = home_team if home_goals > away_goals else away_team

    update_team_state_after_match(
        home_team=home_team,
        away_team=away_team,
        neutral=neutral,
        tournament=tournament,
        states=states,
        home_goals=home_goals,
        away_goals=away_goals,
    )

    result = {
        "home_team": home_team,
        "away_team": away_team,
        "lambda_home": lambda_home,
        "lambda_away": lambda_away,
        "home_goals": home_goals,
        "away_goals": away_goals,
        "extra_time_home_goals": extra_home_goals,
        "extra_time_away_goals": extra_away_goals,
        "decided_by_penalties": decided_by_penalties,
        "winner": winner,
    }
    loser = away_team if winner == home_team else home_team
    return winner, loser, result


def resolve_group_stage(
    fixtures: pd.DataFrame,
    states: dict[str, TeamState],
    predictor: GoalPredictor,
    rng: np.random.Generator,
) -> tuple[dict[str, dict[str, object]], list[dict[str, object]]]:

    group_matches = fixtures[fixtures["stage"].fillna("") == "GROUP"].copy()

    standings: dict[str, dict[str, object]] = {}
    match_logs: list[dict[str, object]] = []

    for _, row in group_matches.iterrows():
        home_team = str(row["home_team"])
        away_team = str(row["away_team"])
        home_goals, away_goals, lambda_home, lambda_away = simulate_group_match(
            row=row,
            states=states,
            predictor=predictor,
            rng=rng,
        )

        match_logs.append(
            {
                "stage": "GROUP",
                "group": row.get("group"),
                "home_team": home_team,
                "away_team": away_team,
                "home_goals": home_goals,
                "away_goals": away_goals,
                "lambda_home": lambda_home,
                "lambda_away": lambda_away,
            }
        )

        for team, goals_for, goals_against in (
            (home_team, home_goals, away_goals),
            (away_team, away_goals, home_goals),
        ):
            team_row = standings.setdefault(
                team,
                {
                    "team": team,
                    "group": str(row.get("group")) if not pd.isna(row.get("group")) else None,
                    "points": 0,
                    "goals_for": 0,
                    "goals_against": 0,
                    "goal_difference": 0,
                    "matches": 0,
                },
            )
            team_row["goals_for"] += goals_for
            team_row["goals_against"] += goals_against
            team_row["goal_difference"] = team_row["goals_for"] - team_row["goals_against"]
            team_row["matches"] += 1

        if home_goals > away_goals:
            standings[home_team]["points"] += GROUP_STAGE_POINTS_WIN
        elif home_goals < away_goals:
            standings[away_team]["points"] += GROUP_STAGE_POINTS_WIN
        else:
            standings[home_team]["points"] += GROUP_STAGE_POINTS_DRAW
            standings[away_team]["points"] += GROUP_STAGE_POINTS_DRAW

    return standings, match_logs


def _team_elo(record: dict[str, object], states: dict[str, TeamState]) -> float:

    state = states.get(str(record["team"]))
    return float(state.elo) if state is not None else 0.0


def _shuffle_equal_blocks(
    ordered: list[dict[str, object]],
    key_func,
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    """Randomly permute teams that remain perfectly equal under ``key_func``."""

    index = 0
    while index < len(ordered):
        tie_end = index + 1
        while tie_end < len(ordered) and key_func(ordered[tie_end]) == key_func(ordered[index]):
            tie_end += 1
        if tie_end - index > 1:
            block = ordered[index:tie_end]
            order = list(range(len(block)))
            rng.shuffle(order)
            ordered[index:tie_end] = [block[i] for i in order]
        index = tie_end
    return ordered


def _resolve_overall_then_random(
    block: list[dict[str, object]],
    states: dict[str, TeamState],
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    """Tiebreakers 4-7: overall goal difference, overall goals for, Elo, then random."""

    def overall_key(record: dict[str, object]) -> tuple[int, int, float]:
        return (
            int(record["goal_difference"]),
            int(record["goals_for"]),
            _team_elo(record, states),
        )

    ordered = sorted(block, key=overall_key, reverse=True)
    return _shuffle_equal_blocks(ordered, overall_key, rng)


def _rank_tied_teams(
    tied: list[dict[str, object]],
    group_matches: list[dict[str, object]],
    states: dict[str, TeamState],
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    """Order teams that are level on overall points using FIFA tiebreakers 1-7."""

    if len(tied) == 1:
        return list(tied)

    tied_names = {str(record["team"]) for record in tied}
    head_to_head: dict[str, dict[str, int]] = {
        name: {"points": 0, "goals_for": 0, "goals_against": 0} for name in tied_names
    }

    for match in group_matches:
        home_team = str(match["home_team"])
        away_team = str(match["away_team"])
        if home_team not in tied_names or away_team not in tied_names:
            continue
        home_goals = int(match["home_goals"])
        away_goals = int(match["away_goals"])

        head_to_head[home_team]["goals_for"] += home_goals
        head_to_head[home_team]["goals_against"] += away_goals
        head_to_head[away_team]["goals_for"] += away_goals
        head_to_head[away_team]["goals_against"] += home_goals

        if home_goals > away_goals:
            head_to_head[home_team]["points"] += GROUP_STAGE_POINTS_WIN
        elif home_goals < away_goals:
            head_to_head[away_team]["points"] += GROUP_STAGE_POINTS_WIN
        else:
            head_to_head[home_team]["points"] += GROUP_STAGE_POINTS_DRAW
            head_to_head[away_team]["points"] += GROUP_STAGE_POINTS_DRAW

    def h2h_key(record: dict[str, object]) -> tuple[int, int, int]:
        stats = head_to_head[str(record["team"])]
        return (stats["points"], stats["goals_for"] - stats["goals_against"], stats["goals_for"])

    ordered = sorted(tied, key=h2h_key, reverse=True)

    result: list[dict[str, object]] = []
    index = 0
    while index < len(ordered):
        tie_end = index + 1
        while tie_end < len(ordered) and h2h_key(ordered[tie_end]) == h2h_key(ordered[index]):
            tie_end += 1
        block = ordered[index:tie_end]
        if len(block) == 1:
            result.extend(block)
        elif len(block) == len(tied):
            # Head-to-head separated nobody: fall through to overall criteria.
            result.extend(_resolve_overall_then_random(block, states, rng))
        else:
            # A smaller subset is still level: recompute head-to-head among them.
            result.extend(_rank_tied_teams(block, group_matches, states, rng))
        index = tie_end
    return result


def _order_group(
    teams: list[dict[str, object]],
    group_matches: list[dict[str, object]],
    states: dict[str, TeamState],
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    """Rank the four teams of a group: overall points first, then tiebreakers 1-7."""

    by_points = sorted(teams, key=lambda record: int(record["points"]), reverse=True)

    result: list[dict[str, object]] = []
    index = 0
    while index < len(by_points):
        tie_end = index + 1
        while tie_end < len(by_points) and int(by_points[tie_end]["points"]) == int(by_points[index]["points"]):
            tie_end += 1
        block = by_points[index:tie_end]
        if len(block) == 1:
            result.extend(block)
        else:
            result.extend(_rank_tied_teams(block, group_matches, states, rng))
        index = tie_end
    return result


def rank_group_teams(
    standings: dict[str, dict[str, object]],
    group_matches: list[dict[str, object]],
    states: dict[str, TeamState],
    rng: np.random.Generator,
) -> tuple[dict[str, list[str]], list[str]]:

    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for record in standings.values():
        group = str(record.get("group"))
        groups[group].append(record)

    matches_by_group: dict[str, list[dict[str, object]]] = defaultdict(list)
    for match in group_matches:
        matches_by_group[str(match.get("group"))].append(match)

    qualifiers: dict[str, list[str]] = {}
    third_place_candidates: list[dict[str, object]] = []

    for group_name in GROUP_ORDER:
        teams = groups.get(group_name, [])
        if len(teams) != 4:
            raise ValueError(f"Group {group_name} does not contain 4 teams in the simulation")

        ordered = _order_group(teams, matches_by_group.get(group_name, []), states, rng)

        qualifiers[group_name] = [str(ordered[0]["team"]), str(ordered[1]["team"])]
        third_place_candidates.append(ordered[2])

    # Best third-placed teams: rank by points, then by current Elo (random as last resort).
    def third_place_key(record: dict[str, object]) -> tuple[int, float]:
        return (int(record["points"]), _team_elo(record, states))

    third_place_candidates = sorted(third_place_candidates, key=third_place_key, reverse=True)
    third_place_candidates = _shuffle_equal_blocks(third_place_candidates, third_place_key, rng)

    third_place_order = [str(item["team"]) for item in third_place_candidates[:8]]
    return qualifiers, third_place_order


def resolve_placeholders(qualifiers: dict[str, list[str]], third_places: list[str]) -> dict[str, str]:

    mapping: dict[str, str] = {}
    for group_name in GROUP_ORDER:
        mapping[f"1{group_name}"] = qualifiers[group_name][0]
        mapping[f"2{group_name}"] = qualifiers[group_name][1]

    for index, team in enumerate(third_places, start=1):
        mapping[f"3rd_{index}"] = team

    return mapping


def materialize_fixture_value(value: object, mapping: dict[str, str]) -> str:

    if pd.isna(value):
        return ""
    text = str(value).strip()
    return mapping.get(text, text)


def resolve_knockout_fixtures(fixtures: pd.DataFrame, mapping: dict[str, str]) -> pd.DataFrame:

    resolved = fixtures.copy()
    for column in ["home_team", "away_team"]:
        resolved[column] = resolved[column].map(lambda value: materialize_fixture_value(value, mapping))
    return resolved


def build_bracket_maps() -> dict[str, list[str]]:

    return {
        "R32": [
            "W_R32_1",
            "W_R32_2",
            "W_R32_3",
            "W_R32_4",
            "W_R32_5",
            "W_R32_6",
            "W_R32_7",
            "W_R32_8",
            "W_R32_9",
            "W_R32_10",
            "W_R32_11",
            "W_R32_12",
            "W_R32_13",
            "W_R32_14",
            "W_R32_15",
            "W_R32_16",
        ],
        "R16": [
            "W_R16_1",
            "W_R16_2",
            "W_R16_3",
            "W_R16_4",
            "W_R16_5",
            "W_R16_6",
            "W_R16_7",
            "W_R16_8",
        ],
        "QF": ["W_QF1", "W_QF2", "W_QF3", "W_QF4"],
        "SF": ["W_SF1", "W_SF2"],
        "3RD": ["L_SF1", "L_SF2"],
        "FINAL": ["W_FINAL"],
    }


def run_knockout_round(
    fixtures: pd.DataFrame,
    states: dict[str, TeamState],
    predictor: GoalPredictor,
    rng: np.random.Generator,
    stage_name: str,
) -> tuple[pd.DataFrame, dict[str, str], list[dict[str, object]]]:

    results: list[dict[str, object]] = []
    winner_mapping: dict[str, str] = {}
    losers: list[str] = []

    stage_matches = fixtures[fixtures["stage"].fillna("") == stage_name].copy()
    stage_matches = stage_matches.reset_index(drop=True)

    for index, row in stage_matches.iterrows():
        home_team = str(row["home_team"])
        away_team = str(row["away_team"])
        fixture_date = row["date"]
        city = str(row.get("city", ""))
        country = str(row.get("country", ""))
        neutral = parse_bool(row.get("neutral", True))

        winner, loser, match_result = simulate_knockout_match(
            home_team=home_team,
            away_team=away_team,
            date_value=fixture_date,
            tournament=str(row.get("tournament", "FIFA World Cup")),
            city=city,
            country=country,
            neutral=neutral,
            states=states,
            predictor=predictor,
            rng=rng,
        )

        results.append(
            {
                "stage": stage_name,
                "group": row.get("group"),
                "home_team": home_team,
                "away_team": away_team,
                "resolved_home_team": home_team,
                "resolved_away_team": away_team,
                "winner": winner,
                "loser": loser,
                "home_goals": match_result["home_goals"],
                "away_goals": match_result["away_goals"],
                "lambda_home": match_result["lambda_home"],
                "lambda_away": match_result["lambda_away"],
                "decided_by_penalties": match_result["decided_by_penalties"],
            }
        )
        winner_mapping[f"{stage_name}_{index + 1}"] = winner
        losers.append(loser)

    result_frame = pd.DataFrame(results)
    return result_frame, winner_mapping, results


def resolve_knockout_bracket(
    fixtures: pd.DataFrame,
    states: dict[str, TeamState],
    predictor: GoalPredictor,
    rng: np.random.Generator,
    placeholder_map: dict[str, str],
) -> tuple[list[dict[str, object]], dict[str, str], dict[str, str]]:

    all_results: list[dict[str, object]] = []
    winner_placeholders: dict[str, str] = {}
    loser_placeholders: dict[str, str] = {}

    knockout_order = ["R32", "R16", "QF", "SF", "3RD", "FINAL"]
    bracket_map = build_bracket_maps()

    current_map = dict(placeholder_map)

    for stage_name in knockout_order:
        stage_fixtures = fixtures[fixtures["stage"].fillna("") == stage_name].copy().reset_index(drop=True)
        if stage_fixtures.empty:
            continue

        for index, row in stage_fixtures.iterrows():
            resolved_home = materialize_fixture_value(row["home_team"], current_map)
            resolved_away = materialize_fixture_value(row["away_team"], current_map)
            if not resolved_home or not resolved_away:
                raise ValueError(
                    f"Could not resolve knockout fixture {stage_name} #{index + 1}: "
                    f"{row['home_team']} vs {row['away_team']}"
                )

            fixture_date = row["date"]
            city = str(row.get("city", ""))
            country = str(row.get("country", ""))
            neutral = parse_bool(row.get("neutral", True))

            winner, loser, match_result = simulate_knockout_match(
                home_team=resolved_home,
                away_team=resolved_away,
                date_value=fixture_date,
                tournament=str(row.get("tournament", "FIFA World Cup")),
                city=city,
                country=country,
                neutral=neutral,
                states=states,
                predictor=predictor,
                rng=rng,
            )

            all_results.append(
                {
                    "stage": stage_name,
                    "group": row.get("group"),
                    "home_team": resolved_home,
                    "away_team": resolved_away,
                    "winner": winner,
                    "loser": loser,
                    "home_goals": match_result["home_goals"],
                    "away_goals": match_result["away_goals"],
                    "lambda_home": match_result["lambda_home"],
                    "lambda_away": match_result["lambda_away"],
                    "decided_by_penalties": match_result["decided_by_penalties"],
                }
            )

            if stage_name in {"R32", "R16", "QF", "SF"}:
                winner_key = bracket_map[stage_name][index]
                current_map[winner_key] = winner
                winner_placeholders[winner_key] = winner

            if stage_name == "SF":
                loser_key = f"L_SF{index + 1}"
                current_map[loser_key] = loser
                loser_placeholders[loser_key] = loser

            if stage_name == "3RD":
                # No placeholders are created by the third-place match itself.
                pass

    return all_results, winner_placeholders, loser_placeholders


def update_stage_output_columns(fixtures: pd.DataFrame, placeholder_map: dict[str, str]) -> pd.DataFrame:

    output = fixtures.copy()
    output["resolved_home_team"] = output["home_team"].map(lambda value: materialize_fixture_value(value, placeholder_map))
    output["resolved_away_team"] = output["away_team"].map(lambda value: materialize_fixture_value(value, placeholder_map))
    return output


def make_final_rankings(
    group_standings: dict[str, dict[str, object]],
    qualifiers: dict[str, list[str]],
    third_place_order: list[str],
    champion: str,
    runner_up: str,
) -> dict[str, list[dict[str, object]]]:

    group_tables = []
    for team, record in group_standings.items():
        group_tables.append(
            {
                "team": team,
                "group": record["group"],
                "points": record["points"],
                "goal_difference": record["goal_difference"],
                "goals_for": record["goals_for"],
            }
        )

    return {
        "groups": group_tables,
        "qualifiers": [
            {"group": group_name, "first": teams[0], "second": teams[1]}
            for group_name, teams in qualifiers.items()
        ],
        "third_places": [{"rank": index + 1, "team": team} for index, team in enumerate(third_place_order)],
        "champion": [{"team": champion}, {"team": runner_up}],
    }


def simulate_world_cup(
    fixtures: pd.DataFrame,
    predictor: GoalPredictor,
    base_states: dict[str, TeamState],
    rng: np.random.Generator,
) -> dict[str, object]:

    states = {
        team: TeamState(
            elo=team_state.elo,
            elo_history=deque(team_state.elo_history, maxlen=WINDOW_SIZE),
            win_history=deque(team_state.win_history, maxlen=WINDOW_SIZE),
            goals_for_history=deque(team_state.goals_for_history, maxlen=WINDOW_SIZE),
            goals_against_history=deque(team_state.goals_against_history, maxlen=WINDOW_SIZE),
        )
        for team, team_state in base_states.items()
    }

    group_fixtures = fixtures[fixtures["stage"].fillna("") == "GROUP"].copy()
    group_standings, group_logs = resolve_group_stage(group_fixtures, states, predictor, rng)
    qualifiers, third_place_order = rank_group_teams(group_standings, group_logs, states, rng)
    placeholder_map = resolve_placeholders(qualifiers, third_place_order)

    knockout_fixtures = fixtures[fixtures["stage"].fillna("") != "GROUP"].copy()
    knockout_results, winner_placeholders, loser_placeholders = resolve_knockout_bracket(
        knockout_fixtures,
        states,
        predictor,
        rng,
        placeholder_map,
    )

    placeholder_map.update(winner_placeholders)
    placeholder_map.update(loser_placeholders)

    final_match = next(result for result in knockout_results if result["stage"] == "FINAL")
    champion = str(final_match["winner"])
    runner_up = str(final_match["loser"])

    return {
        "groups": group_standings,
        "group_logs": group_logs,
        "knockout_results": knockout_results,
        "placeholder_map": placeholder_map,
        "champion": champion,
        "runner_up": runner_up,
        "third_place_order": third_place_order,
    }


def run_monte_carlo(n_simulations: int = N_SIMULATIONS, random_seed: int = RANDOM_SEED) -> dict[str, object]:

    if n_simulations <= 0:
        raise ValueError("n_simulations must be positive")

    rng = np.random.default_rng(random_seed)
    history = load_csv(HISTORICAL_PATH)
    fixtures = load_csv(FIXTURE_PATH)
    base_states = reconstruct_state(history)
    predictor = GoalPredictor()

    group_participants = fixtures[fixtures["stage"].fillna("") == "GROUP"]
    teams = sorted(
        set(group_participants["home_team"].astype(str)).union(set(group_participants["away_team"].astype(str)))
    )

    statistics = {
        team: {
            "r32": 0,
            "r16": 0,
            "quarterfinal": 0,
            "semifinal": 0,
            "final": 0,
            "champion": 0,
        }
        for team in teams
    }
    champion_counts: dict[str, int] = defaultdict(int)
    simulation_samples: list[dict[str, object]] = []

    for simulation_index in tqdm(range(n_simulations), desc="Simulating World Cup", unit="sim"):
        outcome = simulate_world_cup(fixtures, predictor, base_states, rng)

        group_standings = outcome["groups"]
        qualifiers = outcome["placeholder_map"]
        champion = str(outcome["champion"])
        runner_up = str(outcome["runner_up"])
        third_places = outcome["third_place_order"]

        qualified_r32 = set()
        qualified_r16 = set()
        qualified_qf = set()
        qualified_sf = set()
        qualified_final = {champion, runner_up}

        for group_name in GROUP_ORDER:
            qualified_r32.update([qualifiers[f"1{group_name}"], qualifiers[f"2{group_name}"]])

        qualified_r32.update(third_places[:8])

        for result in outcome["knockout_results"]:
            if result["stage"] == "R32":
                qualified_r16.add(result["winner"])
            elif result["stage"] == "R16":
                qualified_qf.add(result["winner"])
            elif result["stage"] == "QF":
                qualified_sf.add(result["winner"])

        for team in teams:
            if team in qualified_r32:
                statistics[team]["r32"] += 1
            if team in qualified_r16:
                statistics[team]["r16"] += 1
            if team in qualified_qf:
                statistics[team]["quarterfinal"] += 1
            if team in qualified_sf:
                statistics[team]["semifinal"] += 1
            if team in qualified_final:
                statistics[team]["final"] += 1
            if team == champion:
                statistics[team]["champion"] += 1

        champion_counts[champion] += 1

        if simulation_index == 0:
            simulation_samples.append(
                {
                    "groups": group_standings,
                    "champion": champion,
                    "runner_up": runner_up,
                    "knockout_results": outcome["knockout_results"],
                }
            )

    probability_rows = []
    for team in sorted(statistics):
        probability_rows.append(
            {
                "team": team,
                "r32_probability": statistics[team]["r32"] / n_simulations,
                "r16_probability": statistics[team]["r16"] / n_simulations,
                "quarterfinal_probability": statistics[team]["quarterfinal"] / n_simulations,
                "semifinal_probability": statistics[team]["semifinal"] / n_simulations,
                "final_probability": statistics[team]["final"] / n_simulations,
                "champion_probability": statistics[team]["champion"] / n_simulations,
            }
        )

    probability_frame = pd.DataFrame(probability_rows)
    probability_frame = probability_frame.sort_values(
        ["champion_probability", "final_probability", "semifinal_probability"],
        ascending=[False, False, False],
    ).reset_index(drop=True)

    top_10_champions = probability_frame.sort_values("champion_probability", ascending=False).head(10)
    summary = {
        "n_simulations": n_simulations,
        "top_10_champions": [
            {
                "team": str(row.team),
                "champion_probability": float(row.champion_probability),
            }
            for row in top_10_champions.itertuples(index=False)
        ],
    }

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    probability_frame.to_csv(PROBABILITIES_CSV_PATH, index=False)
    with SUMMARY_JSON_PATH.open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=4, ensure_ascii=False)
        handle.write("\n")

    wcsims_payload = {
        "n_simulations": n_simulations,
        "random_seed": random_seed,
        "results_csv": str(PROBABILITIES_CSV_PATH),
        "summary_json": str(SUMMARY_JSON_PATH),
        "sample_run": simulation_samples,
        "top_10_champions": summary["top_10_champions"],
    }
    with WCSIMS_PATH.open("w", encoding="utf-8") as handle:
        json.dump(wcsims_payload, handle, indent=4, ensure_ascii=False)
        handle.write("\n")

    return {
        "probabilities": probability_frame,
        "summary": summary,
        "wcsims": wcsims_payload,
    }


def main() -> None:

    results = run_monte_carlo()
    print(f"Saved probability table to {PROBABILITIES_CSV_PATH}")
    print(f"Saved summary to {SUMMARY_JSON_PATH}")
    print(f"Saved full JSON payload to {WCSIMS_PATH}")
    top_champion = results["summary"]["top_10_champions"][0]
    print(f"Most likely champion: {top_champion['team']} ({top_champion['champion_probability']:.4f})")
    # mostrar todo el csv
    print("\nFull probability table:")
    pd.set_option("display.max_rows", None)
    print(results["probabilities"])

if __name__ == "__main__":
    main()