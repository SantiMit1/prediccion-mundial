# Predicción Mundial 2026 🏆⚽

Simulador probabilístico del Mundial FIFA 2026 basado en modelos estadísticos de goles y simulación Monte Carlo. El sistema estima las probabilidades de cada selección para avanzar por cada ronda del torneo, desde la fase de grupos hasta la final.

---

## Cómo funciona

El proyecto combina dos componentes principales: un **modelo de predicción de goles** y un **simulador Monte Carlo** que corre el torneo completo miles de veces.

### Modelo de predicción de goles

Para cada partido, el modelo predice cuántos goles va a hacer cada equipo de forma independiente. Los goles se modelan con una **distribución de Poisson**: el modelo estima un parámetro λ (la media esperada de goles) para cada equipo, y luego samplea el resultado real desde esa distribución.

El modelo fue entrenado con datos históricos de partidos internacionales y tiene en cuenta el estado actual de cada equipo al momento del partido — no solo estadísticas globales, sino métricas calculadas sobre los últimos 5 partidos jugados.

### Simulador Monte Carlo

Con el modelo de goles entrenado, el simulador corre el Mundial completo `N` veces (por defecto 1000 simulaciones). En cada corrida:

1. Se simulan todos los partidos de la fase de grupos.
2. Se calculan las posiciones finales de cada grupo.
3. Los equipos que pasan de terceros mejores se seleccionan según puntos, diferencia de goles y goles a favor.
4. Se simula el bracket eliminatorio completo (R32 → R16 → QF → SF → Final y tercer puesto), con tiempo extra y penales cuando hay empate.

Al final de las N simulaciones, se calcula la probabilidad de cada selección de llegar a cada ronda.

---

## Datos utilizados

### Fuente histórica — `data/results_enriched.csv`

Es el dataset principal de entrenamiento. Contiene resultados de partidos internacionales históricos con las siguientes columnas clave:

| Columna | Descripción |
|---|---|
| `date` | Fecha del partido |
| `home_team` / `away_team` | Equipos local y visitante |
| `home_score` / `away_score` | Resultado final |
| `tournament` | Competencia (Copa del Mundo, amistoso, eliminatorias, etc.) |
| `neutral` | Si el partido se jugó en cancha neutral |
| `city` / `country` | Sede del partido |

Además de estas columnas base, el dataset contiene **features derivadas** que se calculan en `src/build_dataset.py` y se usan directamente como inputs del modelo:

| Feature | Descripción |
|---|---|
| `home_elo_before` / `away_elo_before` | Rating Elo de cada equipo antes del partido |
| `elo_diff` | Diferencia de Elo entre local y visitante |
| `home_elo_change_last_5` / `away_elo_change_last_5` | Variación de Elo en los últimos 5 partidos |
| `home_wins_last_5` / `away_wins_last_5` | Victorias en los últimos 5 partidos |
| `home_goals_for_last_5` / `away_goals_for_last_5` | Goles anotados en los últimos 5 partidos |
| `home_goals_against_last_5` / `away_goals_against_last_5` | Goles recibidos en los últimos 5 partidos |

### Fixture del torneo — `data/mundial_2026.csv`

Contiene todos los partidos del Mundial 2026, tanto de fase de grupos como de la fase eliminatoria. Los partidos eliminatorios usan placeholders (ej. `1A`, `2B`, `W_R32_1`) que se resuelven dinámicamente en cada simulación según quién clasifica.

| Columna | Descripción |
|---|---|
| `date` | Fecha programada del partido |
| `home_team` / `away_team` | Equipo o placeholder |
| `stage` | Etapa: `GROUP`, `R32`, `R16`, `QF`, `SF`, `3RD`, `FINAL` |
| `group` | Grupo (solo fase de grupos, A–L) |
| `city` / `country` / `neutral` | Información de la sede |

---

## Cómo se organiza el proyecto

```
prediccion-mundial/
│
├── data/
│   ├── results_enriched.csv      # Historial de partidos con features calculadas
│   └── mundial_2026.csv          # Fixture completo del Mundial 2026
│
├── src/
│   ├── build_dataset.py          # Lógica de Elo y features rodantes (ventana de 5 partidos)
│   └── predict_match.py          # Interfaz del modelo para predecir goles de un partido
│
├── models/
│   ├── goals_model.pkl           # Modelo entrenado (serializado con joblib)
│   └── feature_columns.pkl       # Orden exacto de columnas usado en el entrenamiento
│
├── results/
│   ├── world_cup_probabilities.csv   # Probabilidades por equipo y ronda
│   ├── simulation_summary.json       # Resumen con el top 10 de campeones más probables
│   └── wcsims.json                   # Detalle de la primera simulación
│
├── monte_carlo_world_cup.py      # Script principal: reconstruye el estado, corre las simulaciones
└── requirements.txt
```

### Flujo de ejecución

```
results_enriched.csv
        │
        ▼
  reconstruct_state()          ← Reconstruye el Elo y el historial de cada selección
        │
        ▼
  GoalPredictor (goals_model)  ← Predice λ_home y λ_away para cada partido
        │
        ▼
  simulate_world_cup() × N     ← Corre el torneo N veces con sampleo de Poisson
        │
        ▼
  Probabilidades por ronda     → world_cup_probabilities.csv
```

---

## Outputs

Al correr el simulador se generan tres archivos en `results/`:

**`world_cup_probabilities.csv`** — Probabilidad de cada selección de llegar a cada ronda:

| team | r32_probability | r16_probability | quarterfinal_probability | semifinal_probability | final_probability | champion_probability |
|---|---|---|---|---|---|---|
| Argentina | 1.0 | 0.82 | 0.61 | 0.44 | 0.28 | 0.14 |
| ... | ... | ... | ... | ... | ... | ... |

**`simulation_summary.json`** — Top 10 de campeones más probables con sus probabilidades.

**`wcsims.json`** — Resultado detallado de la primera simulación: posiciones de grupos, resultados del bracket y campeón.

---


