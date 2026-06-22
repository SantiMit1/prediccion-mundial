"""Shared team-state reconstruction and feature/model utilities.

These helpers were previously duplicated across ``predict_match.py``,
``monte_carlo_world_cup.py`` and ``train_goals_model.py``. They turn the
historical results into per-team rolling state, build the model feature
rows from that state, and load the trained artifacts.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Deque, Sequence

import joblib
import pandas as pd

try:
    from src.build_dataset import (
        INITIAL_ELO,
        WINDOW_SIZE,
        actual_scores,
        compute_elo_change,
        expected_score,
        get_k_value,
        normalize_bool,
    )
except ImportError:
    from build_dataset import (
        INITIAL_ELO,
        WINDOW_SIZE,
        actual_scores,
        compute_elo_change,
        expected_score,
        get_k_value,
        normalize_bool,
    )


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "models" / "goals_model.pkl"
FEATURE_COLUMNS_PATH = PROJECT_ROOT / "models" / "feature_columns.pkl"

# Columns that are never used as model inputs (identifiers and targets).
EXCLUDED_COLUMNS = {
    "date",
    "city",
    "country",
    "home_team",
    "away_team",
    "home_score",
    "away_score",
}


@dataclass
class TeamState:
    elo: float = INITIAL_ELO
    elo_history: Deque[float] = None
    win_history: Deque[int] = None
    goals_for_history: Deque[int] = None
    goals_against_history: Deque[int] = None

    def __post_init__(self) -> None:
        if self.elo_history is None:
            self.elo_history = deque(maxlen=WINDOW_SIZE)
        if self.win_history is None:
            self.win_history = deque(maxlen=WINDOW_SIZE)
        if self.goals_for_history is None:
            self.goals_for_history = deque(maxlen=WINDOW_SIZE)
        if self.goals_against_history is None:
            self.goals_against_history = deque(maxlen=WINDOW_SIZE)


def make_team_state() -> TeamState:
    return TeamState()


def update_team_histories(
    state: TeamState,
    team_is_home: bool,
    home_goals: int,
    away_goals: int,
    team_elo_before: float,
) -> None:
    if team_is_home:
        goals_for = home_goals
        goals_against = away_goals
        wins = int(home_goals > away_goals)
    else:
        goals_for = away_goals
        goals_against = home_goals
        wins = int(away_goals > home_goals)

    state.elo_history.append(team_elo_before)
    state.win_history.append(wins)
    state.goals_for_history.append(goals_for)
    state.goals_against_history.append(goals_against)


def reconstruct_state(history: pd.DataFrame) -> dict[str, TeamState]:
    """Replay historical matches chronologically into per-team state."""
    states: dict[str, TeamState] = defaultdict(make_team_state)

    if "date" not in history.columns:
        raise ValueError("results_enriched.csv must contain a date column")

    history = history.copy()
    history["date"] = pd.to_datetime(history["date"], errors="coerce")
    history = history.dropna(subset=["date"]).sort_values("date").reset_index(drop=True)

    for row in history.itertuples(index=False):
        home_team = str(row.home_team)
        away_team = str(row.away_team)
        home_score = int(row.home_score)
        away_score = int(row.away_score)
        neutral = normalize_bool(row.neutral)
        tournament = row.tournament

        home_state = states[home_team]
        away_state = states[away_team]

        home_elo_before = float(home_state.elo)
        away_elo_before = float(away_state.elo)

        expected_home = expected_score(home_elo_before, away_elo_before, neutral)
        expected_away = 1.0 - expected_home
        actual_home, actual_away = actual_scores(home_score, away_score)
        k_factor = get_k_value(tournament)

        home_state.elo = home_elo_before + k_factor * (actual_home - expected_home)
        away_state.elo = away_elo_before + k_factor * (actual_away - expected_away)

        update_team_histories(home_state, True, home_score, away_score, home_elo_before)
        update_team_histories(away_state, False, home_score, away_score, away_elo_before)

    return states


def team_state_to_feature_row(
    home_team: str,
    away_team: str,
    tournament: str,
    neutral: bool,
    states: dict[str, TeamState],
    *,
    date: object = "",
    city: str = "",
    country: str = "",
) -> pd.DataFrame:
    """Build a single-row feature DataFrame from current team state.

    ``date``/``city``/``country`` are carried along for callers that have
    them but are dropped before inference (see ``EXCLUDED_COLUMNS``).
    """
    if home_team not in states:
        states[home_team] = make_team_state()
    if away_team not in states:
        states[away_team] = make_team_state()

    home_state = states[home_team]
    away_state = states[away_team]

    feature_row = {
        "date": date,
        "home_team": home_team,
        "away_team": away_team,
        "tournament": tournament,
        "city": city,
        "country": country,
        "neutral": neutral,
        "home_elo_before": float(home_state.elo),
        "away_elo_before": float(away_state.elo),
        "elo_diff": float(home_state.elo - away_state.elo),
        "home_elo_change_last_5": compute_elo_change(home_state.elo, home_state.elo_history),
        "away_elo_change_last_5": compute_elo_change(away_state.elo, away_state.elo_history),
        "home_wins_last_5": int(sum(home_state.win_history)),
        "away_wins_last_5": int(sum(away_state.win_history)),
        "home_goals_for_last_5": int(sum(home_state.goals_for_history)),
        "home_goals_against_last_5": int(sum(home_state.goals_against_history)),
        "away_goals_for_last_5": int(sum(away_state.goals_for_history)),
        "away_goals_against_last_5": int(sum(away_state.goals_against_history)),
    }
    return pd.DataFrame([feature_row])


def preprocess_features(features: pd.DataFrame) -> pd.DataFrame:
    prepared = features.copy()

    if "neutral" in prepared.columns:
        prepared["neutral"] = prepared["neutral"].astype(int)

    if "tournament" in prepared.columns:
        tournament_dummies = pd.get_dummies(prepared["tournament"], prefix="tournament", dtype=int)
        prepared = pd.concat([prepared.drop(columns=["tournament"]), tournament_dummies], axis=1)

    feature_columns = [column for column in prepared.columns if column not in EXCLUDED_COLUMNS]
    return prepared[feature_columns]


def align_feature_columns(features: pd.DataFrame, feature_columns: Sequence[str]) -> pd.DataFrame:
    return features.reindex(columns=list(feature_columns), fill_value=0)


def load_artifacts(
    model_path: Path = MODEL_PATH,
    feature_columns_path: Path = FEATURE_COLUMNS_PATH,
) -> tuple[object, list[str]]:
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")
    if not feature_columns_path.exists():
        raise FileNotFoundError(f"Feature column file not found: {feature_columns_path}")

    model = joblib.load(model_path)
    feature_columns = joblib.load(feature_columns_path)

    if not isinstance(feature_columns, list) or not all(isinstance(column, str) for column in feature_columns):
        raise ValueError("feature_columns.pkl must contain a list of feature column names")

    return model, feature_columns
