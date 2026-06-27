"""Non-interactive wrapper for load_result.py — cronjob-friendly.

Usage:
    python src/load_result_batch.py \\
        --date 2026-06-27 \\
        --home "Argentina" \\
        --away "Brazil" \\
        --home-score 2 \\
        --away-score 1 \\
        --tournament "FIFA World Cup" \\
        --city "Miami" \\
        --country "USA" \\
        --neutral True
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Ensure we can import from the project's src directory
SRC_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SRC_DIR))

from load_result import MatchInput, append_match


def main() -> None:
    parser = argparse.ArgumentParser(description="Load a match result non-interactively")
    parser.add_argument("--date", required=True, help="Match date (YYYY-MM-DD)")
    parser.add_argument("--home", "--home-team", dest="home_team", required=True, help="Home team name")
    parser.add_argument("--away", "--away-team", dest="away_team", required=True, help="Away team name")
    parser.add_argument("--home-score", type=int, required=True, help="Home team goals")
    parser.add_argument("--away-score", type=int, required=True, help="Away team goals")
    parser.add_argument("--tournament", required=True, help="Tournament name (e.g. FIFA World Cup)")
    parser.add_argument("--city", default="Unknown", help="City")
    parser.add_argument("--country", default="Unknown", help="Country")
    parser.add_argument("--neutral", type=lambda x: x.lower() in ("true", "1", "yes", "y"), default=False, help="Neutral venue")

    args = parser.parse_args()

    match = MatchInput(
        date=args.date,
        home_team=args.home_team,
        away_team=args.away_team,
        home_score=args.home_score,
        away_score=args.away_score,
        tournament=args.tournament,
        city=args.city,
        country=args.country,
        neutral=args.neutral,
    )

    append_match(match)
    print(f"✓ Added: {args.home_team} {args.home_score}-{args.away_score} {args.away_team} ({args.tournament}, {args.date})")


if __name__ == "__main__":
    main()
