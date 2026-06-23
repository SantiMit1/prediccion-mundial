# Predicción Mundial 2026

Simulación probabilística del Mundial FIFA 2026 basada en un modelo de machine learning que predice la distribución de goles de cada partido, combinado con un simulador Monte Carlo que ejecuta el torneo completo miles de veces para estimar la probabilidad de cada selección de alcanzar cada ronda.

---

## 1. Feature engineering — `build_dataset.py`

El punto de partida es `data/results.csv`, que contiene ~50 000 partidos internacionales desde 1872. Sobre ese dataset crudo se construyen tres familias de features, todas calculadas *antes* de cada partido usando únicamente información histórica disponible hasta ese momento (sin data leakage).

### 1.1 Rating Elo

Cada selección comienza con un Elo base de **1500**. Después de cada partido, el Elo se actualiza con la fórmula:

```
nuevo_elo = elo_anterior + K × (resultado_real - resultado_esperado)
```

- **K** varía según el torneo: 60 para Mundiales, 50 para eliminatorias, 40 para copas continentales, 30 para amistosos.
- **Resultado esperado**: función sigmoide basada en la diferencia de Elo entre los equipos, con una ventaja de localía de **100 puntos Elo** que se anula en partidos neutrales.
- **Resultado real**: 1.0 para victoria, 0.5 para empate, 0.0 para derrota.

### 1.2 Ventana rodante (últimos 5 partidos)

Para cada equipo y antes de cada partido se calculan estadísticas sobre los últimos 5 encuentros:

- `elo_change_last_5`: variación del rating Elo en el período.
- `wins_last_5`: cantidad de victorias.
- `goals_for_last_5` / `goals_against_last_5`: goles anotados y recibidos.

La ventana de 5 partidos se eligió porque captura la forma reciente del equipo sin ser tan corta como para ser ruidosa ni tan larga como para diluir cambios de rendimiento.

### 1.3 Dixon-Coles — fuerzas de ataque y defensa

Además de las features rodantes, se estiman fuerzas de ataque y defensa para cada equipo mediante el modelo **Dixon-Coles** (Dixon & Coles, 1997). Se asume que los goles de cada equipo siguen una distribución de Poisson donde el logaritmo de la tasa esperada se descompone como:

```
log(λ_local)  = ataque_local  + defensa_visitante + ventaja_localía
log(λ_visita) = ataque_visitante + defensa_local
```

Los parámetros se estiman por **máxima verosimilitud** usando `scipy.optimize.minimize` con restricciones de suma cero sobre ataques y defensas (para hacer identificable el modelo).

A diferencia del Elo —que se actualiza tras cada partido con una fórmula cerrada—, Dixon-Coles requiere una optimización numérica costosa. Por eso se recalcula **cada 1000 partidos** usando solo los últimos **4 años de datos** (con un mínimo de 200 partidos). Esto mantiene el costo acotado y evita que partidos de décadas anteriores distorsionen la fuerza actual de un equipo.

---

## 2. Modelo de predicción de goles — `train_goals_model.py`

### 2.1 Arquitectura

Se entrena un **XGBoost** con `MultiOutputRegressor` de scikit-learn para predecir simultáneamente dos variables:

```
[λ_home, λ_away] = modelo(features)
```

Las features de entrada incluyen todas las descritas arriba más **dummies de torneo** (one-hot encoding sobre el tipo de competencia), ya que el factor K del Elo no captura completamente la diferencia de intensidad entre un amistoso y un Mundial.

### 2.2 Split temporal

El dataset enriquecido se ordena cronológicamente y se parte **80/20**: los primeros ~40 000 partidos se usan para entrenar, los ~10 000 más recientes para evaluar. Este split refleja el uso real del modelo — predecir partidos futuros con datos pasados.

### 2.3 Hiperparámetros

Se realizó una búsqueda de hiperparámetros que encontró la configuración óptima:

| Parámetro | Valor |
|---|---|
| `n_estimators` | 650 |
| `max_depth` | 5 |
| `learning_rate` | 0.0146 |
| `subsample` | 0.709 |
| `colsample_bytree` | 0.951 |
| `min_child_weight` | 10 |
| `reg_alpha` | 9.86 |
| `reg_lambda` | 2.56 |
| `gamma` | 2.90 |

### 2.4 Métricas sobre el test set

| Métrica | Valor |
|---|---|
| MAE goles local | 1.022 |
| MAE goles visitante | 0.837 |
| MAE general | 0.930 |
| RMSE general | 1.235 |
| Accuracy 1X2 | 59.3% |

La accuracy 1X2 mide qué porcentaje de las veces el modelo acierta el signo del resultado (local gana, empate, visitante gana) considerando empate cuando la diferencia de goles predichos es menor a 0.25.

---

## 3. Simulación Monte Carlo — `monte_carlo_world_cup.py`

### 3.1 Reconstrucción del estado actual

Antes de simular, `reconstruct_state()` reproduce cronológicamente todos los partidos de `results_enriched.csv` para obtener el Elo, las estadísticas rodantes y las fuerzas Dixon-Coles actuales de cada selección. Este estado es el punto de partida para todas las simulaciones.

### 3.2 Generación de resultados

Para cada partido del fixture `mundial_2026.csv`:

1. Se toman las features actuales de ambos equipos (Elo, ventana rodante, fuerzas Dixon-Coles).
2. El modelo XGBoost predice `λ_home` y `λ_away`.
3. Se sortea el resultado: `home_goals ~ Poisson(λ_home)`, `away_goals ~ Poisson(λ_away)`.

En partidos de sede neutral (todos los del Mundial), la predicción se promedia con la predicción intercambiando local y visitante. Esto elimina el sesgo de localía incorporado en el Elo y en el parámetro de ventaja de Dixon-Coles.

### 3.3 Fase de grupos

Los 48 partidos de grupo se simulan y se calculan las posiciones finales de cada grupo (A–L). El criterio de desempate es:

1. Puntos
2. Diferencia de goles
3. Goles a favor
4. Resultado head-to-head entre los equipos empatados
5. Rating Elo (mayor Elo avanza)
6. Sorteo aleatorio

Los 4 mejores terceros se seleccionan con los mismos criterios.

### 3.4 Fase eliminatoria

El bracket de 32 equipos está definido en `mundial_2026.csv` con placeholders del tipo `1A` (primer lugar del grupo A), `2B` (segundo del grupo B), `W_R32_1` (ganador del partido de R32 #1), etc. Estos placeholders se resuelven dinámicamente en cada simulación según los resultados de la fase de grupos y del bracket anterior.

Cuando un partido eliminatorio termina empatado tras los 90 minutos, se simula **tiempo extra** reduciendo la tasa de goles a `λ/3` (dos períodos de 15 minutos con menor ritmo de juego). Si persiste el empate, el ganador se define por **penales** (selección aleatoria con probabilidad 50/50, ya que es inherentemente impredecible).

### 3.5 Agregación

Con **1000 simulaciones** completadas:

- `world_cup_probabilities.csv`: para cada selección, la fracción de simulaciones en las que alcanzó cada ronda (R32, R16, QF, SF, final, campeón).
- `simulation_summary.json`: top 10 de campeones más probables.
- `wcsims.json`: detalle completo de la primera simulación (posiciones de grupos, resultados del bracket, campeón).

---

## 4. Archivos del proyecto

```
data/
├── results.csv                    # Partidos históricos crudos (~50k)
├── results_enriched.csv           # Partidos + features calculadas
├── mundial_2026.csv               # Fixture del Mundial con placeholders
└── former_names.csv               # Mapeo de nombres históricos a actuales

src/
├── build_dataset.py               # Feature engineering: Elo, ventanas, Dixon-Coles
├── dixon_coles.py                 # Implementación del modelo Dixon-Coles (MLE)
├── model_features.py              # Utilidades compartidas para reconstrucción de estado
├── train_goals_model.py           # Entrenamiento y evaluación del XGBoost
├── monte_carlo_world_cup.py       # Simulador Monte Carlo del mundial
├── predict_match.py               # Predicción interactiva de un partido
├── load_result.py                 # Carga de un resultado real a los datasets
└── cli_prompts.py                 # Helpers de input para scripts interactivos

models/
├── goals_model.pkl                # XGBoost entrenado (joblib)
├── feature_columns.pkl            # Orden de columnas para inferencia
├── metrics.json                   # MAE, RMSE, accuracy 1X2
├── best_params.json               # Hiperparámetros óptimos
└── test_predictions.csv           # Predicciones sobre el test set

results/
├── world_cup_probabilities.csv    # Probabilidades por equipo y ronda (desde la fecha 2)
├── simulation_summary.json        # Top 10 campeones
└── wcsims.json                    # Detalle de la primera simulación
```
