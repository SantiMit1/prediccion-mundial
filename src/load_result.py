from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, List

import pandas as pd

from build_dataset import K_VALUES, build_enriched_dataset


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


def append_match_and_rebuild(match: MatchInput) -> None:
	existing_results = load_existing_results(RESULTS_PATH)
	new_row = pd.DataFrame([build_match_row(match)])

	updated_results = pd.concat([existing_results, new_row], ignore_index=True)
	updated_results["date"] = pd.to_datetime(updated_results["date"], errors="coerce")
	updated_results = updated_results.dropna(subset=BASE_COLUMNS).copy()
	updated_results = updated_results.sort_values("date", ascending=True).reset_index(drop=True)
	enriched_input = updated_results[BASE_COLUMNS].copy()

	results_output = updated_results.copy()
	results_output["date"] = results_output["date"].dt.strftime("%Y-%m-%d")
	results_output = results_output[BASE_COLUMNS]
	results_output.to_csv(RESULTS_PATH, index=False)

	enriched_df = build_enriched_dataset(enriched_input)
	enriched_df.to_csv(ENRICHED_PATH, index=False)


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
	append_match_and_rebuild(match)

	print("Partido agregado correctamente.")
	print(f"Actualizado: {RESULTS_PATH}")
	print(f"Actualizado: {ENRICHED_PATH}")


if __name__ == "__main__":
	main()
