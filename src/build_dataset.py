"""Build an enriched football results dataset for machine learning.

The script reads ``data/results.csv``, computes pre-match features using only
historical information available before each match, and writes
``data/results_enriched.csv``.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import DefaultDict, Deque, Dict, List, Tuple

import pandas as pd


INITIAL_ELO = 1500.0
HOME_ADVANTAGE = 100.0
WINDOW_SIZE = 5
PROGRESS_EVERY = 5000

K_VALUES = {
    # Mundial
    "FIFA World Cup": 60,

    # Eliminatorias mundialistas
    "FIFA World Cup qualification": 40,

    # Eurocopa
    "UEFA Euro": 50,
    "UEFA Euro qualification": 40,

    # Copa América
    "Copa América": 50,

    # Copa Africana
    "African Cup of Nations": 50,
    "African Cup of Nations qualification": 40,

    # Copa Asiática
    "AFC Asian Cup": 50,
    "AFC Asian Cup qualification": 40,

    # Copa Oro
    "Gold Cup": 50,
    "Gold Cup qualification": 40,

    # Nations League UEFA
    "UEFA Nations League": 35,

    # Nations League CONCACAF
    "CONCACAF Nations League": 35,

    # Copa Confederaciones
    "Confederations Cup": 50,

    # Copa de Oceanía
    "Oceania Nations Cup": 50,

    # Torneos amistosos
    "Friendly": 20,
}
DEFAULT_K = 30.0

REQUIRED_COLUMNS = [
    "date",
    "home_team",
    "away_team",
    "home_score",
    "away_score",
    "tournament",
    "city",
    "country",
    "neutral",
]

OUTPUT_COLUMNS = REQUIRED_COLUMNS + [
    "home_elo_before",
    "away_elo_before",
    "elo_diff",
    "home_elo_change_last_5",
    "away_elo_change_last_5",
    "home_wins_last_5",
    "away_wins_last_5",
    "home_goals_for_last_5",
    "home_goals_against_last_5",
    "away_goals_for_last_5",
    "away_goals_against_last_5",
]


@dataclass(frozen=True)
class MatchOutcome:
    """Container for a processed match result."""

    home_score: int
    away_score: int


def load_results(input_path: Path) -> pd.DataFrame:
    """Load and validate the historical results dataset."""

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    missing_columns = [
        column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        raise ValueError(
            f"results.csv is missing required columns: {missing_columns}")

    raw_rows = len(df)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["home_score"] = pd.to_numeric(df["home_score"], errors="coerce")
    df["away_score"] = pd.to_numeric(df["away_score"], errors="coerce")

    df = df.dropna(subset=REQUIRED_COLUMNS).copy()
    removed_rows = raw_rows - len(df)
    if removed_rows > 0:
        print(
            f"Dropped {removed_rows:,} rows with missing or invalid required data")

    df = df.sort_values("date", ascending=True).reset_index(drop=True)
    return df


def normalize_bool(value: object) -> bool:
    """Convert common CSV boolean representations to ``bool``."""

    if isinstance(value, bool):
        return value
    if pd.isna(value):
        return False

    normalized = str(value).strip().lower()
    return normalized in {"true", "1", "yes", "y", "t"}


def get_k_value(tournament: object) -> float:
    """Return the Elo K-factor for a tournament."""

    if pd.isna(tournament):
        return DEFAULT_K
    return K_VALUES.get(str(tournament).strip(), DEFAULT_K)


def expected_score(home_elo: float, away_elo: float, neutral: bool) -> float:
    """Calculate the expected home score using the traditional Elo formula."""

    effective_home_elo = home_elo if neutral else home_elo + HOME_ADVANTAGE
    return 1.0 / (1.0 + 10 ** ((away_elo - effective_home_elo) / 400.0))


def actual_scores(home_score: int, away_score: int) -> Tuple[float, float]:
    """Convert a match result into Elo actual scores."""

    if home_score > away_score:
        return 1.0, 0.0
    if home_score < away_score:
        return 0.0, 1.0
    return 0.5, 0.5


def rolling_sum(history: Deque[int]) -> int:
    """Return the sum of a fixed-length rolling history."""

    return int(sum(history))


def compute_elo_change(current_elo: float, history: Deque[float]) -> float:
    """Compute the Elo change versus the value from five matches ago."""

    if len(history) < WINDOW_SIZE:
        return 0.0
    return current_elo - history[0]


def append_team_histories(
    team: str,
    home_team: str,
    home_score: int,
    away_score: int,
    team_elo_before: float,
    team_elo_history: DefaultDict[str, Deque[float]],
    team_win_history: DefaultDict[str, Deque[int]],
    team_goals_for_history: DefaultDict[str, Deque[int]],
    team_goals_against_history: DefaultDict[str, Deque[int]],
) -> None:
    """Append the latest match information to a team's rolling histories."""

    if team == home_team:
        goals_for = home_score
        goals_against = away_score
        wins = int(home_score > away_score)
    else:
        goals_for = away_score
        goals_against = home_score
        wins = int(away_score > home_score)

    team_elo_history[team].append(team_elo_before)
    team_win_history[team].append(wins)
    team_goals_for_history[team].append(goals_for)
    team_goals_against_history[team].append(goals_against)


def build_enriched_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Compute pre-match features and Elo updates for every match."""

    team_elos: DefaultDict[str, float] = defaultdict(lambda: INITIAL_ELO)
    team_elo_history: DefaultDict[str, Deque[float]] = defaultdict(
        lambda: deque(maxlen=WINDOW_SIZE))
    team_win_history: DefaultDict[str, Deque[int]] = defaultdict(
        lambda: deque(maxlen=WINDOW_SIZE))
    team_goals_for_history: DefaultDict[str, Deque[int]] = defaultdict(
        lambda: deque(maxlen=WINDOW_SIZE))
    team_goals_against_history: DefaultDict[str, Deque[int]] = defaultdict(
        lambda: deque(maxlen=WINDOW_SIZE))

    enriched_rows: List[Dict[str, object]] = []
    total_matches = len(df)

    for index, row in enumerate(df.itertuples(index=False), start=1):
        home_team = str(row.home_team)
        away_team = str(row.away_team)
        home_score = int(row.home_score)
        away_score = int(row.away_score)
        neutral = normalize_bool(row.neutral)
        tournament = row.tournament

        home_elo_before = float(team_elos[home_team])
        away_elo_before = float(team_elos[away_team])
        elo_diff = home_elo_before - away_elo_before

        home_elo_change_last_5 = compute_elo_change(
            home_elo_before, team_elo_history[home_team])
        away_elo_change_last_5 = compute_elo_change(
            away_elo_before, team_elo_history[away_team])

        home_wins_last_5 = rolling_sum(team_win_history[home_team])
        away_wins_last_5 = rolling_sum(team_win_history[away_team])

        home_goals_for_last_5 = rolling_sum(team_goals_for_history[home_team])
        home_goals_against_last_5 = rolling_sum(
            team_goals_against_history[home_team])
        away_goals_for_last_5 = rolling_sum(team_goals_for_history[away_team])
        away_goals_against_last_5 = rolling_sum(
            team_goals_against_history[away_team])

        enriched_rows.append(
            {
                "date": row.date.strftime("%Y-%m-%d"),
                "home_team": home_team,
                "away_team": away_team,
                "home_score": home_score,
                "away_score": away_score,
                "tournament": tournament,
                "city": row.city,
                "country": row.country,
                "neutral": row.neutral,
                "home_elo_before": home_elo_before,
                "away_elo_before": away_elo_before,
                "elo_diff": elo_diff,
                "home_elo_change_last_5": home_elo_change_last_5,
                "away_elo_change_last_5": away_elo_change_last_5,
                "home_wins_last_5": home_wins_last_5,
                "away_wins_last_5": away_wins_last_5,
                "home_goals_for_last_5": home_goals_for_last_5,
                "home_goals_against_last_5": home_goals_against_last_5,
                "away_goals_for_last_5": away_goals_for_last_5,
                "away_goals_against_last_5": away_goals_against_last_5,
            }
        )

        expected_home = expected_score(
            home_elo_before, away_elo_before, neutral)
        expected_away = 1.0 - expected_home
        actual_home, actual_away = actual_scores(home_score, away_score)
        k_factor = get_k_value(tournament)

        team_elos[home_team] = home_elo_before + \
            k_factor * (actual_home - expected_home)
        team_elos[away_team] = away_elo_before + \
            k_factor * (actual_away - expected_away)

        append_team_histories(
            team=home_team,
            home_team=home_team,
            home_score=home_score,
            away_score=away_score,
            team_elo_before=home_elo_before,
            team_elo_history=team_elo_history,
            team_win_history=team_win_history,
            team_goals_for_history=team_goals_for_history,
            team_goals_against_history=team_goals_against_history,
        )
        append_team_histories(
            team=away_team,
            home_team=home_team,
            home_score=home_score,
            away_score=away_score,
            team_elo_before=away_elo_before,
            team_elo_history=team_elo_history,
            team_win_history=team_win_history,
            team_goals_for_history=team_goals_for_history,
            team_goals_against_history=team_goals_against_history,
        )

        if index % PROGRESS_EVERY == 0 or index == total_matches:
            print(f"Processed {index:,}/{total_matches:,} matches", flush=True)

    enriched_df = pd.DataFrame(enriched_rows)
    enriched_df = enriched_df[OUTPUT_COLUMNS]
    return enriched_df


def main() -> None:
    """Run the dataset building pipeline."""

    project_root = Path(__file__).resolve().parents[1]
    input_path = project_root / "data" / "results.csv"
    output_path = project_root / "data" / "results_enriched.csv"

    print(f"Loading input dataset from {input_path}")
    df = load_results(input_path)
    print(f"Loaded {len(df):,} matches. Building enriched dataset...")

    enriched_df = build_enriched_dataset(df)
    enriched_df.to_csv(output_path, index=False)

    unique_teams = pd.unique(
        pd.concat([df["home_team"], df["away_team"]], ignore_index=True))
    print("Finished successfully")
    print(f"Output written to: {output_path}")
    print(f"Total matches processed: {len(df):,}")
    print(f"Unique teams: {len(unique_teams):,}")


if __name__ == "__main__":
    main()
