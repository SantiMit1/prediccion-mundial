# AGENTS.md — Predicción Mundial 2026

## Quick Commands

```bash
# Activate venv (Windows)
.venv\Scripts\activate

# Install deps
pip install -r requirements.txt

# Rebuild enriched dataset from results.csv
python src/build_dataset.py

# Retrain XGBoost goals model
python src/train_goals_model.py

# Run Monte Carlo simulation (1000 sims)
python src/monte_carlo_world_cup.py

# Predict a single match interactively (with Poisson plot)
python src/predict_match.py

# Append a played match to both CSVs
python src/load_result.py
```

## Pipeline Overview

```
data/results.csv → build_dataset.py → data/results_enriched.csv
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

## Key Constants

| Constant | Value | Location |
|----------|-------|----------|
| `INITIAL_ELO` | 1500.0 | `build_dataset.py` |
| `HOME_ADVANTAGE` | 100.0 | `build_dataset.py` |
| `WINDOW_SIZE` | 5 | `build_dataset.py` |
| `RANDOM_SEED` | 42 | `monte_carlo_world_cup.py` |
| `N_SIMULATIONS` | 1000 | `monte_carlo_world_cup.py` |

## Important Files

| Path | Purpose |
|------|---------|
| `data/results.csv` | Raw historical matches (input) |
| `data/results_enriched.csv` | Matches + Elo + rolling features + Dixon-Coles strengths |
| `data/mundial_2026.csv` | 2026 World Cup fixture (uses placeholders like `1A`, `W_R32_1`) |
| `models/goals_model.pkl` | Trained XGBoost MultiOutputRegressor |
| `models/feature_columns.pkl` | Column order for model inference |
| `src/build_dataset.py` | Computes Elo, rolling windows, Dixon-Coles refits every 1000 matches |
| `src/train_goals_model.py` | Temporal 80/20 split, trains XGBoost → predicts (λ_home, λ_away) |
| `src/monte_carlo_world_cup.py` | Main simulator: `reconstruct_state()` → 1000 sims → group/knockout |
| `src/predict_match.py` | Interactive CLI, averages home/away swap for neutral venues |

## Architecture Notes

- **All scripts use `PROJECT_ROOT = Path(__file__).resolve().parents[1]`** — run from any directory, no `cd` needed
- **Model artifacts use Git LFS** — `.gitattributes` tracks `models/*.pkl`
- **Dixon-Coles refit**: every 1000 matches, min 200 matches, last 4 years of data (see `build_dataset.py:DIXON_COLES_*`)
- **Knockout placeholders** resolved dynamically each simulation: `1A`, `2B` → group winners/runners-up; `W_R32_1` etc. → bracket progression
- **Neutral venue handling**: `predict_goals()` averages prediction with home/away swapped to remove home bias
- **Poisson sampling**: goals ~ `Poisson(λ)`; knockout ties → extra time (λ/3) → penalties (random choice)
- **Group tiebreakers**: points → goal diff → goals for → head-to-head → Elo → random

## CI Workflows

- `.github/workflows/run_sim.yml` — manual trigger, runs simulation, commits `results/`
- `.github/workflows/build_enriched_dataset.yml` — manual trigger, rebuilds dataset, commits `data/enriched_dataset.csv` (note: filename differs from local `results_enriched.csv`)