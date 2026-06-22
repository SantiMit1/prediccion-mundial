# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Activate the virtual environment (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Monte Carlo simulator (main entry point)
python src/monte_carlo_world_cup.py

# Rebuild the enriched dataset from results.csv (recomputes Elo + rolling features)
python src/build_dataset.py

# Retrain the goals model (XGBoost) on results_enriched.csv
python src/train_goals_model.py

# Interactively predict a single match (shows Poisson distribution plot)
python src/predict_match.py

# Manually append a played match to both CSVs (interactive prompt)
python src/load_result.py
```

All scripts use `PROJECT_ROOT = Path(__file__).resolve().parents[1]` so they must be run from any directory — no `cd` required.

## Architecture

### Pipeline

```
data/results.csv  →  build_dataset.py  →  data/results_enriched.csv
                                                  │
                                         train_goals_model.py
                                                  │
                                          models/goals_model.pkl
                                          models/feature_columns.pkl
                                                  │
                                       monte_carlo_world_cup.py (×1000 sims)
                                                  │
                                          results/world_cup_probabilities.csv
                                          results/simulation_summary.json
                                          results/wcsims.json
```

### Key modules

- **`src/build_dataset.py`** — Reads `data/results.csv`, iterates chronologically to compute Elo ratings (with K-factors per tournament type) and 5-match rolling windows (wins, goals for/against, Elo change). Also periodically refits Dixon-Coles attack/defense strengths (every 1000 matches, min 200, last 4 years of data). Writes `data/results_enriched.csv`.

- **`src/dixon_coles.py`** — Standalone module that fits Dixon-Coles attack/defense strength parameters via `scipy.optimize.minimize` on a Poisson log-likelihood. Returns a `StrengthMap` dict mapping team → `(attack, defense)`.

- **`src/train_goals_model.py`** — Trains an XGBoost `MultiOutputRegressor` (wrapped in a `Pipeline` + `ColumnTransformer`) to predict `(home_goals, away_goals)` as Poisson λ parameters. Serializes to `models/goals_model.pkl` and saves column order to `models/feature_columns.pkl`.

- **`src/predict_match.py`** — Loads trained artifacts, builds feature rows from current team state, calls `predict_goals()`. For neutral-venue matches, averages predictions with home/away roles swapped to remove home bias. Also contains the interactive `predict_match_from_prompt()` CLI with Poisson distribution plotting.

- **`src/monte_carlo_world_cup.py`** — Main simulator. Calls `reconstruct_state()` to replay all historical matches and build current `TeamState` for every team. Then runs `N_SIMULATIONS=1000` full World Cup simulations: group stage → best-third selection → R32 → R16 → QF → SF → Final + 3rd place. Knockout ties go to extra time and penalties. Outputs probabilities CSV and JSON summaries.

- **`src/load_result.py`** — Interactive CLI to append a single played match to `data/results.csv` and `data/results_enriched.csv` in one step (incremental update without full rebuild).

### Data flow for a simulation

1. `reconstruct_state(history)` replays `results_enriched.csv` in chronological order to produce a `dict[str, TeamState]` with current Elo and rolling stats for every team.
2. For each simulated match, `team_state_to_feature_row()` converts two `TeamState` objects into a single-row DataFrame matching the training schema.
3. `predict_goals()` runs the XGBoost model → λ_home, λ_away.
4. Goals are sampled from `np.random.poisson(λ)`. Ties in knockouts trigger extra time (sampled from a lower λ) and then penalty shootout.
5. Group standings use points → goal difference → goals for → head-to-head tiebreakers. The 8 best third-place teams qualify using a fixed comparison table.

### Important constants (`build_dataset.py` / `monte_carlo_world_cup.py`)

| Constant | Value | Purpose |
|---|---|---|
| `INITIAL_ELO` | 1500.0 | Starting Elo for all teams |
| `HOME_ADVANTAGE` | 100.0 | Elo points added to home team |
| `WINDOW_SIZE` | 5 | Rolling window for recent-form features |
| `RANDOM_SEED` | 42 | Seed for all Monte Carlo simulations |
| `N_SIMULATIONS` | 1000 | Number of full World Cup runs |

### Fixture placeholders

`data/mundial_2026.csv` uses string placeholders for knockout slots (e.g. `1A`, `2B`, `W_R32_1`). The simulator resolves these dynamically each run based on who qualified.
