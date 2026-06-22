"""Reusable interactive CLI prompt helpers.

Shared by the interactive scripts (``predict_match.py`` and
``load_result.py``) so the input-validation loops live in one place.
"""

from __future__ import annotations

from datetime import datetime

try:
    from src.build_dataset import K_VALUES
except ImportError:
    from build_dataset import K_VALUES


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


def prompt_date(message: str, *, default_today: bool = False) -> str:
    """Prompt for a ``YYYY-MM-DD`` date.

    When ``default_today`` is set, an empty input returns today's date.
    """
    while True:
        value = input(f"{message} [YYYY-MM-DD]: ").strip()
        if not value and default_today:
            return datetime.today().strftime("%Y-%m-%d")
        try:
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
