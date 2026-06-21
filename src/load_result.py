from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Tuple

import pandas as pd

from build_dataset import (
    K_VALUES,
    OUTPUT_COLUMNS,
    REQUIRED_COLUMNS,
    WINDOW_SIZE,
    actual_scores,
    expected_score,
    get_k_value,
    normalize_bool,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_PATH = PROJECT_ROOT / "data" / "results.csv"
ENRICHED_PATH = PROJECT_ROOT / "data" / "results_enriched.csv"
DEFAULT_LOCATION = "Unknown"

BASE_COLUMNS = [
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

NEUTRAL_STRENGTH = (0.0, 0.0)


@dataclass(frozen=True)
class MatchInput:
	date: str
	home_team: str
	away_team: str
	home_score: int
	away_score: int
	tournament: str
	city: str
	country: str
	neutral: bool


@dataclass(frozen=True)
class TeamState:
	current_elo: float
	elo_5_matches_ago: float | None  # None si tiene menos de 5 partidos jugados
	wins_last_5: int
	goals_for_last_5: int
	goals_against_last_5: int
	attack_strength: float
	defense_strength: float


def prompt_text(message: str, *, default: str | None = None) -> str:
	while True:
		suffix = f" [{default}]" if default is not None else ""
		value = input(f"{message}{suffix}: ").strip()
		if value:
			return value
		if default is not None:
			return default
		print("Este campo es obligatorio.")


def prompt_int(message: str) -> int:
	while True:
		value = input(f"{message}: ").strip()
		try:
			parsed = int(value)
		except ValueError:
			print("Ingresá un número entero válido.")
			continue
		if parsed < 0:
			print("El valor debe ser cero o mayor.")
			continue
		return parsed


def prompt_date(message: str) -> str:
	while True:
		value = input(f"{message} [YYYY-MM-DD]: ").strip()
		try:
			if value == "":
				return datetime.today().strftime("%Y-%m-%d") 
			parsed = datetime.strptime(value, "%Y-%m-%d")
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


def ensure_columns(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
	missing_columns: List[str] = [column for column in columns if column not in df.columns]
	if missing_columns:
		raise ValueError(f"results.csv is missing required columns: {missing_columns}")
	return df


def load_existing_results(path: Path) -> pd.DataFrame:
	if path.exists():
		df = pd.read_csv(path)
		return ensure_columns(df, BASE_COLUMNS)

	return pd.DataFrame(columns=BASE_COLUMNS)


def load_enriched(path: Path) -> pd.DataFrame:
	if path.exists():
		df = pd.read_csv(path)
		df["date"] = pd.to_datetime(df["date"], errors="coerce")
		return df

	return pd.DataFrame(columns=OUTPUT_COLUMNS)


def build_match_row(match: MatchInput) -> dict[str, object]:
	return {
		"date": match.date,
		"home_team": match.home_team,
		"away_team": match.away_team,
		"home_score": match.home_score,
		"away_score": match.away_score,
		"tournament": match.tournament,
		"city": match.city,
		"country": match.country,
		"neutral": match.neutral,
	}


def get_team_matches(enriched_df: pd.DataFrame, team: str) -> pd.DataFrame:
	team_matches = enriched_df[
		(enriched_df["home_team"] == team) | (enriched_df["away_team"] == team)
	]
	return team_matches.sort_values("date", ascending=True)


def reconstruct_team_state(enriched_df: pd.DataFrame, team: str) -> TeamState:
	team_matches = get_team_matches(enriched_df, team)

	if team_matches.empty:
		return TeamState(
			current_elo=1500.0,  # mismo valor que INITIAL_ELO en build_features.py
			elo_5_matches_ago=None,
			wins_last_5=0,
			goals_for_last_5=0,
			goals_against_last_5=0,
			attack_strength=NEUTRAL_STRENGTH[0],
			defense_strength=NEUTRAL_STRENGTH[1],
		)

	last_match = team_matches.iloc[-1]
	is_home = last_match["home_team"] == team

	home_elo_before = float(last_match["home_elo_before"])
	away_elo_before = float(last_match["away_elo_before"])
	home_score = int(last_match["home_score"])
	away_score = int(last_match["away_score"])
	neutral = normalize_bool(last_match["neutral"])
	tournament = last_match["tournament"]

	expected_home = expected_score(home_elo_before, away_elo_before, neutral)
	expected_away = 1.0 - expected_home
	actual_home, actual_away = actual_scores(home_score, away_score)
	k_factor = get_k_value(tournament)

	new_home_elo = home_elo_before + k_factor * (actual_home - expected_home)
	new_away_elo = away_elo_before + k_factor * (actual_away - expected_away)
	current_elo = new_home_elo if is_home else new_away_elo

	last_5 = team_matches.tail(WINDOW_SIZE)
	wins = 0
	goals_for = 0
	goals_against = 0

	for _, row in last_5.iterrows():
		row_is_home = row["home_team"] == team
		if row_is_home:
			team_goals, opponent_goals = int(row["home_score"]), int(row["away_score"])
		else:
			team_goals, opponent_goals = int(row["away_score"]), int(row["home_score"])

		wins += int(team_goals > opponent_goals)
		goals_for += team_goals
		goals_against += opponent_goals

	elo_5_matches_ago = None
	if len(team_matches) >= WINDOW_SIZE:
		reference_match = team_matches.iloc[-WINDOW_SIZE]
		reference_is_home = reference_match["home_team"] == team
		elo_5_matches_ago = float(
			reference_match["home_elo_before"] if reference_is_home
			else reference_match["away_elo_before"]
		)

	attack_strength = float(
		last_match["home_attack_strength"] if is_home else last_match["away_attack_strength"]
	)
	defense_strength = float(
		last_match["home_defense_strength"] if is_home else last_match["away_defense_strength"]
	)

	return TeamState(
		current_elo=current_elo,
		elo_5_matches_ago=elo_5_matches_ago,
		wins_last_5=wins,
		goals_for_last_5=goals_for,
		goals_against_last_5=goals_against,
		attack_strength=attack_strength,
		defense_strength=defense_strength,
	)


def build_enriched_row(match: MatchInput, enriched_df: pd.DataFrame) -> dict[str, object]:
	home_state = reconstruct_team_state(enriched_df, match.home_team)
	away_state = reconstruct_team_state(enriched_df, match.away_team)

	home_elo_change_last_5 = (
		0.0 if home_state.elo_5_matches_ago is None
		else home_state.current_elo - home_state.elo_5_matches_ago
	)
	away_elo_change_last_5 = (
		0.0 if away_state.elo_5_matches_ago is None
		else away_state.current_elo - away_state.elo_5_matches_ago
	)

	return {
		"date": match.date,
		"home_team": match.home_team,
		"away_team": match.away_team,
		"home_score": match.home_score,
		"away_score": match.away_score,
		"tournament": match.tournament,
		"city": match.city,
		"country": match.country,
		"neutral": match.neutral,
		"home_elo_before": home_state.current_elo,
		"away_elo_before": away_state.current_elo,
		"elo_diff": home_state.current_elo - away_state.current_elo,
		"home_elo_change_last_5": home_elo_change_last_5,
		"away_elo_change_last_5": away_elo_change_last_5,
		"home_wins_last_5": home_state.wins_last_5,
		"away_wins_last_5": away_state.wins_last_5,
		"home_goals_for_last_5": home_state.goals_for_last_5,
		"home_goals_against_last_5": home_state.goals_against_last_5,
		"away_goals_for_last_5": away_state.goals_for_last_5,
		"away_goals_against_last_5": away_state.goals_against_last_5,
		# Fuerzas de Dixon-Coles: se mantienen las últimas conocidas para
		# cada equipo. Se recalibran solo cuando se corre el rebuild
		# completo (build_features.py), no acá.
		"home_attack_strength": home_state.attack_strength,
		"home_defense_strength": home_state.defense_strength,
		"away_attack_strength": away_state.attack_strength,
		"away_defense_strength": away_state.defense_strength,
	}


def append_match(match: MatchInput) -> None:
	existing_results = load_existing_results(RESULTS_PATH)
	new_raw_row = pd.DataFrame([build_match_row(match)])
	updated_results = pd.concat([existing_results, new_raw_row], ignore_index=True)

	updated_results["date"] = pd.to_datetime(updated_results["date"], errors="coerce")
	updated_results = updated_results.dropna(subset=BASE_COLUMNS).copy()
	updated_results = updated_results.sort_values("date", ascending=True).reset_index(drop=True)

	results_output = updated_results.copy()
	results_output["date"] = results_output["date"].dt.strftime("%Y-%m-%d")
	results_output = results_output[BASE_COLUMNS]
	results_output.to_csv(RESULTS_PATH, index=False)

	enriched_df = load_enriched(ENRICHED_PATH)
	new_enriched_row = build_enriched_row(match, enriched_df)

	updated_enriched = pd.concat(
		[enriched_df, pd.DataFrame([new_enriched_row])], ignore_index=True
	)
	updated_enriched["date"] = pd.to_datetime(updated_enriched["date"], errors="coerce")
	updated_enriched = updated_enriched.sort_values("date", ascending=True).reset_index(drop=True)

	enriched_output = updated_enriched.copy()
	enriched_output["date"] = enriched_output["date"].dt.strftime("%Y-%m-%d")
	enriched_output = enriched_output[OUTPUT_COLUMNS]
	enriched_output.to_csv(ENRICHED_PATH, index=False)


def collect_match_input() -> MatchInput:
	print("Carga manual de un partido ya jugado")
	print("Dejá ciudad y país en Unknown si no querés completarlos.")

	return MatchInput(
		date=prompt_date("Fecha del partido"),
		home_team=prompt_text("Equipo local"),
		away_team=prompt_text("Equipo visitante"),
		home_score=prompt_int("Goles del equipo local"),
		away_score=prompt_int("Goles del equipo visitante"),
		tournament=prompt_tournament(),
		city=prompt_text("Ciudad", default=DEFAULT_LOCATION),
		country=prompt_text("País", default=DEFAULT_LOCATION),
		neutral=prompt_bool("¿Fue en cancha neutral?"),
	)


def main() -> None:
	match = collect_match_input()
	append_match(match)

	print("Partido agregado correctamente.")
	print(f"Actualizado: {RESULTS_PATH}")
	print(f"Actualizado: {ENRICHED_PATH}")


if __name__ == "__main__":
	main()