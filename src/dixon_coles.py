from __future__ import annotations

from typing import Dict, List, Sequence, Tuple

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import poisson


StrengthMap = Dict[str, Tuple[float, float]]

DEFAULT_HOME_ADVANTAGE_INIT = 0.1
DEFAULT_MAX_ITER = 200
DEFAULT_FTOL = 1e-6
NEUTRAL_STRENGTH = (0.0, 0.0)


def fit_dixon_coles(
    matches: pd.DataFrame,
    teams: Sequence[str],
    home_advantage_init: float = DEFAULT_HOME_ADVANTAGE_INIT,
    max_iter: int = DEFAULT_MAX_ITER,
) -> StrengthMap:
    if matches.empty:
        return {team: NEUTRAL_STRENGTH for team in teams}

    n_teams = len(teams)
    team_index = {team: i for i, team in enumerate(teams)}

    valid_mask = matches["home_team"].isin(team_index) & matches["away_team"].isin(team_index)
    matches = matches.loc[valid_mask]

    if matches.empty:
        return {team: NEUTRAL_STRENGTH for team in teams}

    home_idx = matches["home_team"].map(team_index).to_numpy()
    away_idx = matches["away_team"].map(team_index).to_numpy()
    home_goals = matches["home_score"].to_numpy(dtype=float)
    away_goals = matches["away_score"].to_numpy(dtype=float)

    if "neutral" in matches.columns:
        is_neutral = matches["neutral"].to_numpy(dtype=bool)
    else:
        is_neutral = np.zeros(len(matches), dtype=bool)
    home_advantage_mask = (~is_neutral).astype(float)

    def neg_log_likelihood(params: np.ndarray) -> float:
        attack = params[:n_teams]
        defense = params[n_teams:2 * n_teams]
        home_advantage = params[-1]

        log_lambda_home = attack[home_idx] + defense[away_idx] + home_advantage * home_advantage_mask
        log_lambda_away = attack[away_idx] + defense[home_idx]

        log_lambda_home = np.clip(log_lambda_home, -10, 10)
        log_lambda_away = np.clip(log_lambda_away, -10, 10)

        lambda_home = np.exp(log_lambda_home)
        lambda_away = np.exp(log_lambda_away)

        log_likelihood = (
            poisson.logpmf(home_goals, lambda_home).sum()
            + poisson.logpmf(away_goals, lambda_away).sum()
        )
        return -log_likelihood

    initial_params = np.zeros(2 * n_teams + 1)
    initial_params[-1] = home_advantage_init

    constraints = [
        {"type": "eq", "fun": lambda p: np.mean(p[:n_teams])},
        {"type": "eq", "fun": lambda p: np.mean(p[n_teams:2 * n_teams])},
    ]

    result = minimize(
        neg_log_likelihood,
        initial_params,
        method="SLSQP",
        constraints=constraints,
        options={"maxiter": max_iter, "ftol": DEFAULT_FTOL},
    )

    if not result.success:
        print(f"Warning: Dixon-Coles optimization did not fully converge: {result.message}")

    attack = result.x[:n_teams]
    defense = result.x[n_teams:2 * n_teams]

    return {team: (float(attack[i]), float(defense[i])) for team, i in team_index.items()}


def get_team_strength(strengths: StrengthMap, team: str) -> Tuple[float, float]:
    return strengths.get(team, NEUTRAL_STRENGTH)


def get_all_teams(matches: pd.DataFrame) -> List[str]:
    return sorted(pd.unique(pd.concat([matches["home_team"], matches["away_team"]])))