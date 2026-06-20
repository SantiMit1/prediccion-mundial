from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Deque, Sequence

import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import poisson

try:
    from src.build_dataset import (
        INITIAL_ELO,
        WINDOW_SIZE,
        K_VALUES,
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
        K_VALUES,
        actual_scores,
        compute_elo_change,
        expected_score,
        get_k_value,
        normalize_bool,
    )


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = PROJECT_ROOT / "models"
MODEL_PATH = MODELS_DIR / "goals_model.pkl"
FEATURE_COLUMNS_PATH = MODELS_DIR / "feature_columns.pkl"
HISTORICAL_RESULTS_PATH = PROJECT_ROOT / "data" / "results_enriched.csv"
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


def load_artifacts(model_path: Path = MODEL_PATH, feature_columns_path: Path = FEATURE_COLUMNS_PATH) -> tuple[object, list[str]]:
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")
    if not feature_columns_path.exists():
        raise FileNotFoundError(f"Feature column file not found: {feature_columns_path}")

    model = joblib.load(model_path)
    feature_columns = joblib.load(feature_columns_path)

    if not isinstance(feature_columns, list) or not all(isinstance(column, str) for column in feature_columns):
        raise ValueError("feature_columns.pkl must contain a list of feature column names")

    return model, feature_columns


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


def predict_goals(features: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    model, feature_columns = load_artifacts()
    prepared_features = preprocess_features(features)
    aligned_features = align_feature_columns(prepared_features, feature_columns)

    predictions = model.predict(aligned_features)
    lambda_home = pd.Series(predictions[:, 0], index=features.index, name="lambda_home")
    lambda_away = pd.Series(predictions[:, 1], index=features.index, name="lambda_away")
    return lambda_home, lambda_away


def load_historical_results(path: Path = HISTORICAL_RESULTS_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Historical results file not found: {path}")

    history = pd.read_csv(path)
    if "date" not in history.columns:
        raise ValueError("results_enriched.csv must contain a date column")

    history["date"] = pd.to_datetime(history["date"], errors="coerce")
    history = history.dropna(subset=["date"]).sort_values("date").reset_index(drop=True)
    return history


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
    states: dict[str, TeamState] = defaultdict(make_team_state)

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
) -> pd.DataFrame:
    if home_team not in states:
        states[home_team] = make_team_state()
    if away_team not in states:
        states[away_team] = make_team_state()

    home_state = states[home_team]
    away_state = states[away_team]

    feature_row = {
        "home_team": home_team,
        "away_team": away_team,
        "tournament": tournament,
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


def prompt_text(message: str, *, default: str | None = None) -> str:
    while True:
        suffix = f" [{default}]" if default is not None else ""
        value = input(f"{message}{suffix}: ").strip()
        if value:
            return value
        if default is not None:
            return default
        print("Este campo es obligatorio.")


def prompt_date(message: str) -> str:
    while True:
        value = input(f"{message} [YYYY-MM-DD]: ").strip()
        try:
            parsed = pd.to_datetime(value, format="%Y-%m-%d")
        except ValueError:
            print("Usá el formato YYYY-MM-DD.")
            continue
        return parsed.strftime("%Y-%m-%d")


def prompt_bool(message: str) -> bool:
    while True:
        value = input(f"{message} [s/n]: ").strip().lower()
        if value in {"s", "si", "sí", "y", "yes", "true", "1"}:
            return True
        if value in {"n", "no", "false", "0"}:
            return False
        print("Respondé con s o n.")


def prompt_tournament() -> str:
    tournaments = list(K_VALUES.keys())
    print("Torneos disponibles:")
    for index, tournament in enumerate(tournaments, start=1):
        print(f"  {index}. {tournament}")

    while True:
        value = input("Elegí el torneo por número: ").strip()
        try:
            selected = int(value)
        except ValueError:
            print("Ingresá el número de la opción.")
            continue
        if 1 <= selected <= len(tournaments):
            return tournaments[selected - 1]
        print("Opción fuera de rango.")


def classify_result(home_goals: int | float, away_goals: int | float) -> str:
    if home_goals > away_goals:
        return "gana el local"
    if home_goals < away_goals:
        return "gana el visitante"
    return "empate"

def plot_poisson_distribution(
    alpha_home: float,
    alpha_away: float,
    home_team: str,
    away_team: str,
    max_goals: int = 10,
) -> None:
    goals = np.arange(0, max_goals + 1)
    pmf_home = poisson.pmf(goals, alpha_home)
    pmf_away = poisson.pmf(goals, alpha_away)

    prob_matrix = np.outer(pmf_home, pmf_away)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    width = 0.35
    ax1.bar(goals - width / 2, pmf_home, width, label=f"{home_team} (λ={alpha_home:.2f})", color="steelblue", alpha=0.8)
    ax1.bar(goals + width / 2, pmf_away, width, label=f"{away_team} (λ={alpha_away:.2f})", color="tomato", alpha=0.8)

    ax1.set_xlabel("Goles")
    ax1.set_ylabel("Probabilidad")
    ax1.set_title("Distribución de Poisson — Goles esperados")
    ax1.set_xticks(goals)
    ax1.legend()
    ax1.grid(axis="y", linestyle="--", alpha=0.5)

    im = ax2.imshow(prob_matrix, cmap="YlOrRd", origin="upper")

    ax2.set_xlabel(f"Goles {away_team}")
    ax2.set_ylabel(f"Goles {home_team}")
    ax2.set_title("Matriz de probabilidades — Resultado exacto")
    ax2.set_xticks(goals)
    ax2.set_yticks(goals)

    for i in goals:
        for j in goals:
            value = prob_matrix[i, j]
            text_color = "white" if value > prob_matrix.max() * 0.5 else "black"
            ax2.text(j, i, f"{value * 100:.1f}%", ha="center", va="center",
                      color=text_color, fontsize=8)

    cbar = fig.colorbar(im, ax=ax2, fraction=0.046, pad=0.04)
    cbar.set_label("Probabilidad")

    plt.tight_layout()
    plt.show()


def predict_match_from_prompt() -> None:

    print("Predicción interactiva de partido")
    print("Los goles esperados salen del modelo y luego se muestrean con Poisson usando esos lambdas como alpha.")

    home_team = prompt_text("Equipo local")
    away_team = prompt_text("Equipo visitante")
    tournament = prompt_tournament()
    neutral = prompt_bool("¿Es en cancha neutral?")

    history = load_historical_results()
    states = reconstruct_state(history)
    feature_df = team_state_to_feature_row(
        home_team=home_team,
        away_team=away_team,
        tournament=tournament,
        neutral=neutral,
        states=states,
    )

    lambda_home, lambda_away = predict_goals(feature_df)
    alpha_home = max(float(lambda_home.iloc[0]), 0.0)
    alpha_away = max(float(lambda_away.iloc[0]), 0.0)

    plot_poisson_distribution(alpha_home, alpha_away, home_team, away_team)

    expected_winner = classify_result(alpha_home, alpha_away)
    rng = np.random.default_rng()
    sampled_home_goals = int(rng.poisson(alpha_home))
    sampled_away_goals = int(rng.poisson(alpha_away))
    sampled_winner = classify_result(sampled_home_goals, sampled_away_goals)

    print()
    print("Resultado esperado")
    print(f"{home_team} {alpha_home:.2f} - {alpha_away:.2f} {away_team}")
    print(f"Ganador esperado: {expected_winner}")
    print()
    print("Resultado Poisson")
    print(f"{home_team} {sampled_home_goals} - {sampled_away_goals} {away_team}")
    print(f"Ganador Poisson: {sampled_winner}")


if __name__ == "__main__":
    predict_match_from_prompt()