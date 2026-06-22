from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import poisson

try:
    from src.cli_prompts import prompt_bool, prompt_text, prompt_tournament
    from src.model_features import (
        align_feature_columns,
        load_artifacts,
        preprocess_features,
        reconstruct_state,
        team_state_to_feature_row,
    )
except ImportError:
    from cli_prompts import prompt_bool, prompt_text, prompt_tournament
    from model_features import (
        align_feature_columns,
        load_artifacts,
        preprocess_features,
        reconstruct_state,
        team_state_to_feature_row,
    )


PROJECT_ROOT = Path(__file__).resolve().parents[1]
HISTORICAL_RESULTS_PATH = PROJECT_ROOT / "data" / "results_enriched.csv"


def _swap_home_away(features: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of features with home/away roles swapped."""
    swapped = features.copy()
    rename = {
        "home_team": "away_team", "away_team": "home_team",
        "home_elo_before": "away_elo_before", "away_elo_before": "home_elo_before",
        "home_elo_change_last_5": "away_elo_change_last_5", "away_elo_change_last_5": "home_elo_change_last_5",
        "home_wins_last_5": "away_wins_last_5", "away_wins_last_5": "home_wins_last_5",
        "home_goals_for_last_5": "away_goals_for_last_5", "away_goals_for_last_5": "home_goals_for_last_5",
        "home_goals_against_last_5": "away_goals_against_last_5", "away_goals_against_last_5": "home_goals_against_last_5",
        "home_attack_strength": "away_attack_strength", "away_attack_strength": "home_attack_strength",
        "home_defense_strength": "away_defense_strength", "away_defense_strength": "home_defense_strength",
    }
    swapped = swapped.rename(columns=rename)
    if "elo_diff" in swapped.columns:
        swapped["elo_diff"] = -swapped["elo_diff"]
    return swapped


def predict_goals(features: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    model, feature_columns = load_artifacts()

    prepared_features = preprocess_features(features)
    aligned_features = align_feature_columns(prepared_features, feature_columns)
    predictions = model.predict(aligned_features)
    lambda_home = pd.Series(predictions[:, 0], index=features.index, name="lambda_home")
    lambda_away = pd.Series(predictions[:, 1], index=features.index, name="lambda_away")

    # For neutral venues, average with the swapped prediction to remove home/away bias.
    if "neutral" in features.columns and features["neutral"].astype(bool).any():
        neutral_mask = features["neutral"].astype(bool)
        swapped_features = _swap_home_away(features)
        prepared_swapped = preprocess_features(swapped_features)
        aligned_swapped = align_feature_columns(prepared_swapped, feature_columns)
        swapped_preds = model.predict(aligned_swapped)
        lambda_home_swapped = pd.Series(swapped_preds[:, 1], index=features.index)
        lambda_away_swapped = pd.Series(swapped_preds[:, 0], index=features.index)

        lambda_home = lambda_home.where(~neutral_mask, (lambda_home + lambda_home_swapped) / 2)
        lambda_away = lambda_away.where(~neutral_mask, (lambda_away + lambda_away_swapped) / 2)

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
