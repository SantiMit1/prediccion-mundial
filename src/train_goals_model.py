"""Train a multi-output goals model from the enriched results dataset.

The script reads ``data/results_enriched.csv``, builds a time-ordered train/test
split, trains a ``MultiOutputRegressor(XGBRegressor(...))`` model to predict
home and away goals, evaluates the holdout set, and persists the artifacts
needed for inference.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.multioutput import MultiOutputRegressor
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor


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

EXCLUDED_COLUMNS = {
    "date",
    "city",
    "country",
    "home_team",
    "away_team",
    "home_score",
    "away_score",
}

TARGET_COLUMNS = ["home_score", "away_score"]
TOURNAMENT_COLUMN = "tournament"
NEUTRAL_COLUMN = "neutral"
DRAW_MARGIN = 0.25


def load_dataset(input_path: Path) -> pd.DataFrame:
    """Load and validate the enriched dataset."""

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        raise ValueError(f"results_enriched.csv is missing required columns: {missing_columns}")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    if df["date"].isna().any():
        invalid_rows = df.index[df["date"].isna()].tolist()[:5]
        raise ValueError(f"Invalid dates found in results_enriched.csv at rows: {invalid_rows}")

    df = df.sort_values("date", ascending=True).reset_index(drop=True)
    return df


def split_temporally(df: pd.DataFrame, train_ratio: float = 0.8) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split the dataset using the oldest rows for training and the newest for testing."""

    if not 0 < train_ratio < 1:
        raise ValueError("train_ratio must be between 0 and 1")

    split_index = int(len(df) * train_ratio)
    if split_index <= 0 or split_index >= len(df):
        raise ValueError("Dataset is too small to create a temporal train/test split")

    train_df = df.iloc[:split_index].copy()
    test_df = df.iloc[split_index:].copy()
    return train_df, test_df


def preprocess_features(df: pd.DataFrame) -> pd.DataFrame:
    """Transform raw enriched rows into the feature matrix used for training.

    The transformation matches the requirements: ``neutral`` becomes an integer
    and ``tournament`` is one-hot encoded with ``pd.get_dummies``.
    """

    features = df.copy()

    if NEUTRAL_COLUMN in features.columns:
        features[NEUTRAL_COLUMN] = features[NEUTRAL_COLUMN].astype(int)

    if TOURNAMENT_COLUMN in features.columns:
        tournament_dummies = pd.get_dummies(features[TOURNAMENT_COLUMN], prefix=TOURNAMENT_COLUMN, dtype=int)
        features = pd.concat([features.drop(columns=[TOURNAMENT_COLUMN]), tournament_dummies], axis=1)

    feature_columns = [column for column in features.columns if column not in EXCLUDED_COLUMNS]
    return features[feature_columns]


def align_feature_columns(features: pd.DataFrame, feature_columns: Sequence[str]) -> pd.DataFrame:
    """Align a feature matrix to the exact training column order."""

    aligned = features.reindex(columns=list(feature_columns), fill_value=0)
    return aligned


def build_model() -> MultiOutputRegressor:
    """Create the requested multi-output XGBoost regressor."""

    base_regressor = XGBRegressor(
        objective="reg:squarederror",
        random_state=42,
        n_estimators=650,
        max_depth=5,
        learning_rate=0.0146,
        subsample=0.7088,
        colsample_bytree=0.9511,
        min_child_weight=10,
        reg_alpha=9.8625,
        reg_lambda=2.5621,
        gamma=2.8974,
    )
    return MultiOutputRegressor(base_regressor)


def classify_result(home_goals: float, away_goals: float, draw_margin: float = 0.0) -> str:
    """Convert a pair of goal expectations into a 1X2 result label."""

    if abs(home_goals - away_goals) <= draw_margin:
        return "Draw"
    if home_goals > away_goals:
        return "Home Win"
    return "Away Win"


def evaluate_1x2(predictions: pd.DataFrame, truth: pd.DataFrame) -> float:
    """Compute 1X2 accuracy from goal predictions."""

    predicted_results = [
        classify_result(home, away, draw_margin=DRAW_MARGIN)
        for home, away in zip(predictions["pred_home_score"], predictions["pred_away_score"])
    ]
    actual_results = [classify_result(home, away) for home, away in zip(truth["home_score"], truth["away_score"])]
    correct_predictions = sum(predicted == actual for predicted, actual in zip(predicted_results, actual_results))
    return correct_predictions / len(actual_results)


def save_predictions(test_df: pd.DataFrame, predictions: pd.DataFrame, output_path: Path) -> None:
    """Persist the test predictions in the required CSV format."""

    test_df = test_df.reset_index(drop=True)
    predictions = predictions.reset_index(drop=True)

    prediction_frame = pd.DataFrame(
        {
            "date": test_df["date"].dt.strftime("%Y-%m-%d").to_numpy(),
            "home_team": test_df["home_team"].to_numpy(),
            "away_team": test_df["away_team"].to_numpy(),
            "home_score": test_df["home_score"].to_numpy(),
            "away_score": test_df["away_score"].to_numpy(),
            "pred_home_score": predictions["pred_home_score"].to_numpy(),
            "pred_away_score": predictions["pred_away_score"].to_numpy(),
        }
    )

    prediction_frame["real_result"] = [
        classify_result(home, away) for home, away in zip(test_df["home_score"], test_df["away_score"])
    ]
    prediction_frame["predicted_result"] = [
        classify_result(home, away, draw_margin=DRAW_MARGIN)
        for home, away in zip(predictions["pred_home_score"], predictions["pred_away_score"])
    ]
    prediction_frame.to_csv(output_path, index=False)


def train_and_evaluate() -> None:
    """Train the model, evaluate it, and persist all artifacts."""

    project_root = Path(__file__).resolve().parents[1]
    input_path = project_root / "data" / "results_enriched.csv"
    models_dir = project_root / "models"
    models_dir.mkdir(parents=True, exist_ok=True)
    model_path = models_dir / "goals_model.pkl"
    feature_columns_path = models_dir / "feature_columns.pkl"
    metrics_path = models_dir / "metrics.json"
    predictions_path = models_dir / "test_predictions.csv"

    print(f"Loading enriched dataset from {input_path}")
    df = load_dataset(input_path)
    print(f"Loaded {len(df):,} matches")

    train_df, test_df = split_temporally(df)
    print(f"Train rows: {len(train_df):,}")
    print(f"Test rows: {len(test_df):,}")

    X_train_raw = preprocess_features(train_df)
    X_test_raw = preprocess_features(test_df)
    feature_columns = list(X_train_raw.columns)
    X_train = align_feature_columns(X_train_raw, feature_columns)
    X_test = align_feature_columns(X_test_raw, feature_columns)

    y_train = train_df[TARGET_COLUMNS]
    y_test = test_df[TARGET_COLUMNS]

    model = build_model()
    print("Training model...")
    model.fit(X_train, y_train)
    print("Training complete")

    print("Generating predictions on the test split...")
    raw_predictions = model.predict(X_test)
    predictions = pd.DataFrame(raw_predictions, columns=["pred_home_score", "pred_away_score"])

    mae_home = mean_absolute_error(y_test["home_score"], predictions["pred_home_score"])
    mae_away = mean_absolute_error(y_test["away_score"], predictions["pred_away_score"])
    rmse_home = math.sqrt(mean_squared_error(y_test["home_score"], predictions["pred_home_score"]))
    rmse_away = math.sqrt(mean_squared_error(y_test["away_score"], predictions["pred_away_score"]))
    mae_general = (mae_home + mae_away) / 2
    rmse_general = (rmse_home + rmse_away) / 2
    accuracy_1x2 = evaluate_1x2(predictions, y_test)

    metrics = {
        "mae_home": float(mae_home),
        "mae_away": float(mae_away),
        "rmse_home": float(rmse_home),
        "rmse_away": float(rmse_away),
        "mae_general": float(mae_general),
        "rmse_general": float(rmse_general),
        "accuracy_1x2": float(accuracy_1x2),
    }

    print("Evaluation metrics:")
    print(f"MAE home: {metrics['mae_home']:.4f}")
    print(f"MAE away: {metrics['mae_away']:.4f}")
    print(f"MAE general: {metrics['mae_general']:.4f}")
    print(f"RMSE home: {metrics['rmse_home']:.4f}")
    print(f"RMSE away: {metrics['rmse_away']:.4f}")
    print(f"RMSE general: {metrics['rmse_general']:.4f}") 
    print(f"1X2 accuracy: {metrics['accuracy_1x2']:.4f}")

    joblib.dump(model, model_path)
    joblib.dump(feature_columns, feature_columns_path)
    with metrics_path.open("w", encoding="utf-8") as handle:
        json.dump(metrics, handle, indent=4, ensure_ascii=False)
        handle.write("\n")

    save_predictions(test_df, predictions, predictions_path)

    print(f"Saved model to {model_path}")
    print(f"Saved feature columns to {feature_columns_path}")
    print(f"Saved metrics to {metrics_path}")
    print(f"Saved test predictions to {predictions_path}")


if __name__ == "__main__":
    train_and_evaluate()