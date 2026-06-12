"""Inference helpers for the trained football goals model."""

from __future__ import annotations

from pathlib import Path
from typing import Sequence, Tuple

import joblib
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = PROJECT_ROOT / "models"
MODEL_PATH = MODELS_DIR / "goals_model.pkl"
FEATURE_COLUMNS_PATH = MODELS_DIR / "feature_columns.pkl"
EXCLUDED_COLUMNS = {
    "date",
    "city",
    "country",
    "home_team",
    "away_team",
    "home_score",
    "away_score",
}


def load_artifacts(model_path: Path = MODEL_PATH, feature_columns_path: Path = FEATURE_COLUMNS_PATH) -> tuple[object, list[str]]:
    """Load the persisted model and feature column order."""

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
    """Apply the same preprocessing used during model training."""

    prepared = features.copy()

    if "neutral" in prepared.columns:
        prepared["neutral"] = prepared["neutral"].astype(int)

    if "tournament" in prepared.columns:
        tournament_dummies = pd.get_dummies(prepared["tournament"], prefix="tournament", dtype=int)
        prepared = pd.concat([prepared.drop(columns=["tournament"]), tournament_dummies], axis=1)

    feature_columns = [column for column in prepared.columns if column not in EXCLUDED_COLUMNS]
    return prepared[feature_columns]


def align_feature_columns(features: pd.DataFrame, feature_columns: Sequence[str]) -> pd.DataFrame:
    """Align the incoming features to the exact column order used in training."""

    return features.reindex(columns=list(feature_columns), fill_value=0)


def predict_goals(features: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Predict expected goals for the home and away teams.

    Parameters
    ----------
    features:
        DataFrame with the same raw enriched features used for training.

    Returns
    -------
    tuple[pd.Series, pd.Series]
        Predicted goal intensities for the home and away teams.
    """

    model, feature_columns = load_artifacts()
    prepared_features = preprocess_features(features)
    aligned_features = align_feature_columns(prepared_features, feature_columns)

    predictions = model.predict(aligned_features)
    lambda_home = pd.Series(predictions[:, 0], index=features.index, name="lambda_home")
    lambda_away = pd.Series(predictions[:, 1], index=features.index, name="lambda_away")
    return lambda_home, lambda_away


if __name__ == "__main__":
    raise SystemExit(
        "This module exposes predict_goals(features: pd.DataFrame). Import it instead of running it directly."
    )