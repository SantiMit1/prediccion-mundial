# New session - 2026-06-24T14:35:02.351Z

**Session ID:** ses_105f1b0b0ffevbjgqjCjei3gcF
**Created:** 24/6/2026, 11:35:02
**Updated:** 24/6/2026, 12:09:43

---

## User

la simulacion del mundial esta usando un formato incorrecto, primero quiero que busques y corrijas el formato en mundial_2026.csv y despues quiero que en la simulacion montecarlo hagas una funcion para armar los fixtures con los mejores 3eros usando las combinaciones correctas (depende de los grupos que salgan los 3eros hay 495 combinaciones posibles de llaves de playoff, estas combinaciones estan publicadas por la fifa)

---

## Assistant (Plan · Qwen3 Coder 480B A35B (free) · 37.6s)

---

## User

planea lo que dije

---

## Assistant (Plan · Laguna M.1 (free) · 7.1s)

---

## User

planea

---

## Assistant (Plan · Qwen3 Coder 480B A35B (free) · 9.1s)

---

## User

planea

---

## Assistant (Plan · Nemotron 3 Ultra Free · 31.7s)

_Thinking:_

The user wants me to:
1. First, find and fix the format in `mundial_2026.csv` 
2. Then, create a function in the Monte Carlo simulation to build fixtures with the best 3rd-place teams using the correct combinations (FIFA-published combinations - 495 possible playoff bracket combinations depending on which groups the 3rd-place teams come from)

I'm in plan mode - read only. Let me start by exploring the codebase to understand the current structure and identify the issues.

**Tool: glob**

**Input:**
```json
{
  "pattern": "**/*.py"
}
```

**Output:**
```
C:\Users\santi\Desktop\prediccion-mundial\src\train_goals_model.py
C:\Users\santi\Desktop\prediccion-mundial\src\predict_match.py
C:\Users\santi\Desktop\prediccion-mundial\src\monte_carlo_world_cup.py
C:\Users\santi\Desktop\prediccion-mundial\src\model_features.py
C:\Users\santi\Desktop\prediccion-mundial\src\load_result.py
C:\Users\santi\Desktop\prediccion-mundial\src\dixon_coles.py
C:\Users\santi\Desktop\prediccion-mundial\src\cli_prompts.py
C:\Users\santi\Desktop\prediccion-mundial\src\build_dataset.py
```

**Tool: glob**

**Input:**
```json
{
  "pattern": "**/*.csv"
}
```

**Output:**
```
C:\Users\santi\Desktop\prediccion-mundial\models\test_predictions.csv
C:\Users\santi\Desktop\prediccion-mundial\results\world_cup_probabilities.csv
C:\Users\santi\Desktop\prediccion-mundial\data\results_enriched.csv
C:\Users\santi\Desktop\prediccion-mundial\data\results.csv
C:\Users\santi\Desktop\prediccion-mundial\data\mundial_2026.csv
C:\Users\santi\Desktop\prediccion-mundial\data\former_names.csv
```

---

## Assistant (Plan · Nemotron 3 Ultra Free · 30.4s)

_Thinking:_

Let me read the relevant files to understand the current structure - especially `mundial_2026.csv` and `monte_carlo_world_cup.py`.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\santi\\Desktop\\prediccion-mundial\\data\\mundial_2026.csv"
}
```

**Output:**
```
<path>C:\Users\santi\Desktop\prediccion-mundial\data\mundial_2026.csv</path>
<type>file</type>
<content>
1: date,stage,group,home_team,away_team,home_score,away_score,tournament,city,country,neutral
2: 2026-06-11,GROUP,A,Mexico,South Africa,2,0,FIFA World Cup,Mexico City,Mexico,TRUE
3: 2026-06-11,GROUP,A,South Korea,Czech Republic,2,1,FIFA World Cup,Guadalajara,Mexico,TRUE
4: 2026-06-12,GROUP,B,Canada,Bosnia and Herzegovina,1,1,FIFA World Cup,Toronto,Canada,TRUE
5: 2026-06-12,GROUP,D,United States,Paraguay,4,1,FIFA World Cup,Los Angeles,USA,TRUE
6: 2026-06-13,GROUP,B,Qatar,Switzerland,1,1,FIFA World Cup,San Francisco,USA,TRUE
7: 2026-06-13,GROUP,C,Brazil,Morocco,1,1,FIFA World Cup,East Rutherford,USA,TRUE
8: 2026-06-13,GROUP,C,Haiti,Scotland,0,1,FIFA World Cup,Boston,USA,TRUE
9: 2026-06-13,GROUP,D,Australia,Turkey,2,0,FIFA World Cup,Vancouver,Canada,TRUE
10: 2026-06-14,GROUP,E,Germany,Curaçao,7,1,FIFA World Cup,Houston,USA,TRUE
11: 2026-06-14,GROUP,F,Netherlands,Japan,2,2,FIFA World Cup,Dallas,USA,TRUE
12: 2026-06-14,GROUP,E,Ivory Coast,Ecuador,1,0,FIFA World Cup,Philadelphia,USA,TRUE
13: 2026-06-14,GROUP,F,Sweden,Tunisia,5,1,FIFA World Cup,Monterrey,Mexico,TRUE
14: 2026-06-15,GROUP,H,Spain,Cape Verde,0,0,FIFA World Cup,Atlanta,USA,TRUE
15: 2026-06-15,GROUP,G,Belgium,Egypt,1,1,FIFA World Cup,Seattle,USA,TRUE
16: 2026-06-15,GROUP,H,Saudi Arabia,Uruguay,1,1,FIFA World Cup,Miami,USA,TRUE
17: 2026-06-15,GROUP,G,Iran,New Zealand,2,2,FIFA World Cup,Los Angeles,USA,TRUE
18: 2026-06-16,GROUP,I,France,Senegal,3,1,FIFA World Cup,East Rutherford,USA,TRUE
19: 2026-06-16,GROUP,I,Iraq,Norway,1,4,FIFA World Cup,Boston,USA,TRUE
20: 2026-06-16,GROUP,J,Argentina,Algeria,3,0,FIFA World Cup,Kansas City,USA,TRUE
21: 2026-06-16,GROUP,J,Austria,Jordan,3,1,FIFA World Cup,San Francisco,USA,TRUE
22: 2026-06-17,GROUP,K,Portugal,DR Congo,1,1,FIFA World Cup,Houston,USA,TRUE
23: 2026-06-17,GROUP,L,England,Croatia,4,2,FIFA World Cup,Dallas,USA,TRUE
24: 2026-06-17,GROUP,L,Ghana,Panama,1,0,FIFA World Cup,Toronto,Canada,TRUE
25: 2026-06-17,GROUP,K,Uzbekistan,Colombia,1,3,FIFA World Cup,Mexico City,Mexico,TRUE
26: 2026-06-18,GROUP,A,Czech Republic,South Africa,1,1,FIFA World Cup,Atlanta,USA,TRUE
27: 2026-06-18,GROUP,B,Switzerland,Bosnia and Herzegovina,4,1,FIFA World Cup,Los Angeles,USA,TRUE
28: 2026-06-18,GROUP,B,Canada,Qatar,6,0,FIFA World Cup,Vancouver,Canada,TRUE
29: 2026-06-18,GROUP,A,Mexico,South Korea,1,0,FIFA World Cup,Guadalajara,Mexico,TRUE
30: 2026-06-19,GROUP,D,United States,Australia,2,0,FIFA World Cup,Seattle,USA,TRUE
31: 2026-06-19,GROUP,C,Scotland,Morocco,0,1,FIFA World Cup,Boston,USA,TRUE
32: 2026-06-19,GROUP,C,Brazil,Haiti,3,0,FIFA World Cup,Philadelphia,USA,TRUE
33: 2026-06-19,GROUP,D,Turkey,Paraguay,0,1,FIFA World Cup,San Francisco,USA,TRUE
34: 2026-06-20,GROUP,F,Netherlands,Sweden,5,1,FIFA World Cup,Houston,USA,TRUE
35: 2026-06-20,GROUP,E,Germany,Ivory Coast,2,1,FIFA World Cup,Toronto,Canada,TRUE
36: 2026-06-20,GROUP,E,Ecuador,Curaçao,0,0,FIFA World Cup,Kansas City,USA,TRUE
37: 2026-06-20,GROUP,F,Tunisia,Japan,0,4,FIFA World Cup,Monterrey,Mexico,TRUE
38: 2026-06-21,GROUP,H,Spain,Saudi Arabia,4,0,FIFA World Cup,Atlanta,USA,TRUE
39: 2026-06-21,GROUP,G,Belgium,Iran,0,0,FIFA World Cup,Los Angeles,USA,TRUE
40: 2026-06-21,GROUP,H,Uruguay,Cape Verde,2,2,FIFA World Cup,Miami,USA,TRUE
41: 2026-06-21,GROUP,G,New Zealand,Egypt,3,1,FIFA World Cup,Vancouver,Canada,TRUE
42: 2026-06-22,GROUP,J,Argentina,Austria,2,0,FIFA World Cup,Dallas,USA,TRUE
43: 2026-06-22,GROUP,I,France,Iraq,3,0,FIFA World Cup,Philadelphia,USA,TRUE
44: 2026-06-22,GROUP,I,Norway,Senegal,3,2,FIFA World Cup,East Rutherford,USA,TRUE
45: 2026-06-22,GROUP,J,Jordan,Algeria,1,2,FIFA World Cup,San Francisco,USA,TRUE
46: 2026-06-23,GROUP,K,Portugal,Uzbekistan,5,0,FIFA World Cup,Houston,USA,TRUE
47: 2026-06-23,GROUP,L,England,Ghana,0,0,FIFA World Cup,Boston,USA,TRUE
48: 2026-06-23,GROUP,L,Panama,Croatia,0,1,FIFA World Cup,Toronto,Canada,TRUE
49: 2026-06-23,GROUP,K,Colombia,DR Congo,1,0,FIFA World Cup,Guadalajara,Mexico,TRUE
50: 2026-06-24,GROUP,B,Switzerland,Canada,,,FIFA World Cup,Vancouver,Canada,TRUE
51: 2026-06-24,GROUP,B,Bosnia and Herzegovina,Qatar,,,FIFA World Cup,Seattle,USA,TRUE
52: 2026-06-24,GROUP,A,South Africa,South Korea,,,FIFA World Cup,Mexico City,Mexico,TRUE
53: 2026-06-24,GROUP,A,Czech Republic,Mexico,,,FIFA World Cup,Guadalajara,Mexico,TRUE
54: 2026-06-25,GROUP,D,United States,Turkey,,,FIFA World Cup,Los Angeles,USA,TRUE
55: 2026-06-25,GROUP,D,Paraguay,Australia,,,FIFA World Cup,San Francisco,USA,TRUE
56: 2026-06-25,GROUP,C,Morocco,Haiti,,,FIFA World Cup,Boston,USA,TRUE
57: 2026-06-25,GROUP,C,Scotland,Brazil,,,FIFA World Cup,Miami,USA,TRUE
58: 2026-06-25,GROUP,E,Germany,Ecuador,,,FIFA World Cup,East Rutherford,USA,TRUE
59: 2026-06-25,GROUP,E,Ivory Coast,Curaçao,,,FIFA World Cup,Philadelphia,USA,TRUE
60: 2026-06-26,GROUP,F,Netherlands,Tunisia,,,FIFA World Cup,Kansas City,USA,TRUE
61: 2026-06-26,GROUP,F,Sweden,Japan,,,FIFA World Cup,Dallas,USA,TRUE
62: 2026-06-26,GROUP,G,Belgium,New Zealand,,,FIFA World Cup,Vancouver,Canada,TRUE
63: 2026-06-26,GROUP,G,Egypt,Iran,,,FIFA World Cup,Seattle,USA,TRUE
64: 2026-06-26,GROUP,I,France,Norway,,,FIFA World Cup,Boston,USA,TRUE
65: 2026-06-26,GROUP,I,Iraq,Senegal,,,FIFA World Cup,East Rutherford,USA,TRUE
66: 2026-06-27,GROUP,H,Spain,Uruguay,,,FIFA World Cup,Guadalajara,Mexico,TRUE
67: 2026-06-27,GROUP,H,Cape Verde,Saudi Arabia,,,FIFA World Cup,Miami,USA,TRUE
68: 2026-06-27,GROUP,L,England,Panama,,,FIFA World Cup,East Rutherford,USA,TRUE
69: 2026-06-27,GROUP,L,Croatia,Ghana,,,FIFA World Cup,Philadelphia,USA,TRUE
70: 2026-06-27,GROUP,J,Jordan,Argentina,,,FIFA World Cup,Dallas,USA,TRUE
71: 2026-06-27,GROUP,J,Algeria,Austria,,,FIFA World Cup,Kansas City,USA,TRUE
72: 2026-06-27,GROUP,K,Portugal,Colombia,,,FIFA World Cup,Miami,USA,TRUE
73: 2026-06-27,GROUP,K,Uzbekistan,DR Congo,,,FIFA World Cup,Houston,USA,TRUE
74: 2026-06-28,R32,,1A,2B,,,FIFA World Cup,,,TRUE
75: 2026-06-28,R32,,1C,2D,,,FIFA World Cup,,,TRUE
76: 2026-06-29,R32,,1E,2F,,,FIFA World Cup,,,TRUE
77: 2026-06-29,R32,,1G,2H,,,FIFA World Cup,,,TRUE
78: 2026-06-30,R32,,1I,2J,,,FIFA World Cup,,,TRUE
79: 2026-06-30,R32,,1K,2L,,,FIFA World Cup,,,TRUE
80: 2026-07-01,R32,,1B,2A,,,FIFA World Cup,,,TRUE
81: 2026-07-01,R32,,1D,2C,,,FIFA World Cup,,,TRUE
82: 2026-07-02,R32,,1F,2E,,,FIFA World Cup,,,TRUE
83: 2026-07-02,R32,,1H,2G,,,FIFA World Cup,,,TRUE
84: 2026-07-03,R32,,1J,2I,,,FIFA World Cup,,,TRUE
85: 2026-07-03,R32,,1L,2K,,,FIFA World Cup,,,TRUE
86: 2026-07-03,R32,,3rd_1,3rd_2,,,FIFA World Cup,,,TRUE
87: 2026-07-03,R32,,3rd_3,3rd_4,,,FIFA World Cup,,,TRUE
88: 2026-07-04,R32,,3rd_5,3rd_6,,,FIFA World Cup,,,TRUE
89: 2026-07-04,R32,,3rd_7,3rd_8,,,FIFA World Cup,,,TRUE
90: 2026-07-05,R16,,W_R32_1,W_R32_2,,,FIFA World Cup,,,TRUE
91: 2026-07-05,R16,,W_R32_3,W_R32_4,,,FIFA World Cup,,,TRUE
92: 2026-07-06,R16,,W_R32_5,W_R32_6,,,FIFA World Cup,,,TRUE
93: 2026-07-06,R16,,W_R32_7,W_R32_8,,,FIFA World Cup,,,TRUE
94: 2026-07-07,R16,,W_R32_9,W_R32_10,,,FIFA World Cup,,,TRUE
95: 2026-07-07,R16,,W_R32_11,W_R32_12,,,FIFA World Cup,,,TRUE
96: 2026-07-08,R16,,W_R32_13,W_R32_14,,,FIFA World Cup,,,TRUE
97: 2026-07-08,R16,,W_R32_15,W_R32_16,,,FIFA World Cup,,,TRUE
98: 2026-07-09,QF,,W_R16_1,W_R16_2,,,FIFA World Cup,,,TRUE
99: 2026-07-10,QF,,W_R16_3,W_R16_4,,,FIFA World Cup,,,TRUE
100: 2026-07-11,QF,,W_R16_5,W_R16_6,,,FIFA World Cup,,,TRUE
101: 2026-07-11,QF,,W_R16_7,W_R16_8,,,FIFA World Cup,,,TRUE
102: 2026-07-14,SF,,W_QF1,W_QF2,,,FIFA World Cup,Dallas,USA,TRUE
103: 2026-07-15,SF,,W_QF3,W_QF4,,,FIFA World Cup,Atlanta,USA,TRUE
104: 2026-07-18,3RD,,L_SF1,L_SF2,,,FIFA World Cup,Miami,USA,TRUE
105: 2026-07-19,FINAL,,W_SF1,W_SF2,,,FIFA World Cup,East Rutherford,USA,TRUE

(End of file - total 105 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\santi\\Desktop\\prediccion-mundial\\src\\monte_carlo_world_cup.py"
}
```

**Output:**
```
<path>C:\Users\santi\Desktop\prediccion-mundial\src\monte_carlo_world_cup.py</path>
<type>file</type>
<content>
1: from __future__ import annotations
2: 
3: import json
4: import math
5: import sys
6: from collections import defaultdict, deque
7: from dataclasses import dataclass
8: from pathlib import Path
9: from typing import DefaultDict, Deque, Iterable, Iterator, Sequence
10: 
11: import numpy as np
12: import pandas as pd
13: 
14: PROJECT_ROOT = Path(__file__).resolve().parents[1]
15: SRC_DIR = PROJECT_ROOT / "src"
16: if str(PROJECT_ROOT) not in sys.path:
17:     sys.path.insert(0, str(PROJECT_ROOT))
18: 
19: from src.build_dataset import (  # noqa: E402
20:     WINDOW_SIZE,
21:     actual_scores,
22:     expected_score,
23:     get_k_value,
24:     normalize_bool,
25: )
26: from src.model_features import (  # noqa: E402
27:     TeamState,
28:     align_feature_columns,
29:     load_artifacts,
30:     make_team_state,
31:     preprocess_features,
32:     reconstruct_state,
33:     team_state_to_feature_row,
34:     update_team_histories,
35: )
36: 
37: 
38: try:
39:     from importlib import import_module
40: 
41:     tqdm = import_module("tqdm").tqdm
42: except Exception:
43:     def tqdm(iterable: Iterable, **_: object) -> Iterable:
44:         return iterable
45: 
46: 
47: RANDOM_SEED = 42
48: N_SIMULATIONS = 1000
49: GROUP_ORDER = list("ABCDEFGHIJKL")
50: 
51: HISTORICAL_PATH = PROJECT_ROOT / "data" / "results_enriched.csv"
52: FIXTURE_PATH = PROJECT_ROOT / "data" / "mundial_2026.csv"
53: RESULTS_DIR = PROJECT_ROOT / "results"
54: WCSIMS_PATH = RESULTS_DIR / "wcsims.json"
55: PROBABILITIES_CSV_PATH = RESULTS_DIR / "world_cup_probabilities.csv"
56: SUMMARY_JSON_PATH = RESULTS_DIR / "simulation_summary.json"
57: 
58: GROUP_STAGE_POINTS_WIN = 3
59: GROUP_STAGE_POINTS_DRAW = 1
60: 
61: 
62: @dataclass(frozen=True)
63: class MatchPrediction:
64:     home_team: str
65:     away_team: str
66:     lambda_home: float
67:     lambda_away: float
68:     home_goals: int
69:     away_goals: int
70:     extra_time_home_goals: int = 0
71:     extra_time_away_goals: int = 0
72:     decided_by_penalties: bool = False
73:     winner: str | None = None
74: 
75: 
76: def load_csv(path: Path) -> pd.DataFrame:
77: 
78:     if not path.exists():
79:         raise FileNotFoundError(f"Missing file: {path}")
80:     return pd.read_csv(path)
81: 
82: 
83: def normalize_group_value(value: object) -> str | None:
84:     if pd.isna(value):
85:         return None
86:     text = str(value).strip()
87:     return text if text else None
88: 
89: 
90: def parse_bool(value: object) -> bool:
91:     return normalize_bool(value)
92: 
93: 
94: _HOME_AWAY_RENAME = {
95:     "home_team": "away_team", "away_team": "home_team",
96:     "home_elo_before": "away_elo_before", "away_elo_before": "home_elo_before",
97:     "home_elo_change_last_5": "away_elo_change_last_5", "away_elo_change_last_5": "home_elo_change_last_5",
98:     "home_wins_last_5": "away_wins_last_5", "away_wins_last_5": "home_wins_last_5",
99:     "home_goals_for_last_5": "away_goals_for_last_5", "away_goals_for_last_5": "home_goals_for_last_5",
100:     "home_goals_against_last_5": "away_goals_against_last_5", "away_goals_against_last_5": "home_goals_against_last_5",
101:     "home_attack_strength": "away_attack_strength", "away_attack_strength": "home_attack_strength",
102:     "home_defense_strength": "away_defense_strength", "away_defense_strength": "home_defense_strength",
103: }
104: 
105: 
106: class GoalPredictor:
107: 
108:     def __init__(self) -> None:
109:         self.model, self.feature_columns = load_artifacts()
110: 
111:     def predict(self, feature_df: pd.DataFrame, neutral: bool = False) -> tuple[float, float]:
112: 
113:         if not neutral:
114:             return self._predict_single(feature_df)
115: 
116:         lambda_home, lambda_away = self._predict_single(feature_df)
117: 
118:         swapped = feature_df.copy()
119:         swapped = swapped.rename(columns=_HOME_AWAY_RENAME)
120:         if "elo_diff" in swapped.columns:
121:             swapped["elo_diff"] = -swapped["elo_diff"]
122: 
123:         lambda_swapped_home, lambda_swapped_away = self._predict_single(swapped)
124: 
125:         return (
126:             (lambda_home + lambda_swapped_away) / 2,
127:             (lambda_away + lambda_swapped_home) / 2,
128:         )
129: 
130:     def _predict_single(self, feature_df: pd.DataFrame) -> tuple[float, float]:
131:         prepared = preprocess_features(feature_df)
132:         aligned = align_feature_columns(prepared, self.feature_columns)
133:         predictions = self.model.predict(aligned)
134:         return float(predictions[0, 0]), float(predictions[0, 1])
135: 
136: 
137: def simulate_group_match(
138:     row: pd.Series,
139:     states: dict[str, TeamState],
140:     predictor: GoalPredictor,
141:     rng: np.random.Generator,
142: ) -> tuple[int, int, float, float]:
143: 
144:     neutral = parse_bool(row.get("neutral", True))
145:     feature_df = team_state_to_feature_row(
146:         str(row["home_team"]),
147:         str(row["away_team"]),
148:         row["tournament"],
149:         neutral,
150:         states,
151:         date=row.get("date", ""),
152:         city=row.get("city", ""),
153:         country=row.get("country", ""),
154:     )
155:     lambda_home, lambda_away = predictor.predict(feature_df, neutral=neutral)
156: 
157:     known_home = row.get("home_score")
158:     known_away = row.get("away_score")
159:     if pd.notna(known_home) and pd.notna(known_away):
160:         home_goals = int(known_home)
161:         away_goals = int(known_away)
162:     else:
163:         home_goals = int(rng.poisson(lambda_home))
164:         away_goals = int(rng.poisson(lambda_away))
165: 
166:     update_team_state_after_match(
167:         home_team=str(row["home_team"]),
168:         away_team=str(row["away_team"]),
169:         neutral=neutral,
170:         tournament=row.get("tournament", "FIFA World Cup"),
171:         states=states,
172:         home_goals=home_goals,
173:         away_goals=away_goals,
174:     )
175:     return home_goals, away_goals, lambda_home, lambda_away
176: 
177: 
178: def update_team_state_after_match(
179:     home_team: str,
180:     away_team: str,
181:     neutral: bool,
182:     tournament: object,
183:     states: dict[str, TeamState],
184:     home_goals: int,
185:     away_goals: int,
186: ) -> None:
187: 
188:     home_team = str(home_team)
189:     away_team = str(away_team)
190: 
191:     home_state = states.setdefault(home_team, make_team_state())
192:     away_state = states.setdefault(away_team, make_team_state())
193: 
194:     home_elo_before = float(home_state.elo)
195:     away_elo_before = float(away_state.elo)
196: 
197:     expected_home = expected_score(home_elo_before, away_elo_before, neutral)
198:     expected_away = 1.0 - expected_home
199:     actual_home, actual_away = actual_scores(home_goals, away_goals)
200:     k_factor = get_k_value(tournament)
201: 
202:     home_state.elo = home_elo_before + k_factor * (actual_home - expected_home)
203:     away_state.elo = away_elo_before + k_factor * (actual_away - expected_away)
204: 
205:     update_team_histories(home_state, True, home_goals, away_goals, home_elo_before)
206:     update_team_histories(away_state, False, home_goals, away_goals, away_elo_before)
207: 
208: 
209: def simulate_knockout_match(
210:     home_team: str,
211:     away_team: str,
212:     date_value: object,
213:     tournament: str,
214:     city: str,
215:     country: str,
216:     neutral: bool,
217:     states: dict[str, TeamState],
218:     predictor: GoalPredictor,
219:     rng: np.random.Generator,
220: ) -> tuple[str, str, dict[str, object]]:
221: 
222:     feature_df = team_state_to_feature_row(
223:         home_team,
224:         away_team,
225:         tournament,
226:         neutral,
227:         states,
228:         date=date_value,
229:         city=city,
230:         country=country,
231:     )
232:     lambda_home, lambda_away = predictor.predict(feature_df, neutral=neutral)
233: 
234:     home_goals = int(rng.poisson(lambda_home))
235:     away_goals = int(rng.poisson(lambda_away))
236: 
237:     extra_home_goals = 0
238:     extra_away_goals = 0
239:     decided_by_penalties = False
240: 
241:     if home_goals == away_goals:
242:         extra_home_goals = int(rng.poisson(lambda_home / 3.0))
243:         extra_away_goals = int(rng.poisson(lambda_away / 3.0))
244:         home_goals += extra_home_goals
245:         away_goals += extra_away_goals
246: 
247:         if home_goals == away_goals:
248:             decided_by_penalties = True
249:             winner = str(rng.choice([home_team, away_team]))
250:         else:
251:             winner = home_team if home_goals > away_goals else away_team
252:     else:
253:         winner = home_team if home_goals > away_goals else away_team
254: 
255:     update_team_state_after_match(
256:         home_team=home_team,
257:         away_team=away_team,
258:         neutral=neutral,
259:         tournament=tournament,
260:         states=states,
261:         home_goals=home_goals,
262:         away_goals=away_goals,
263:     )
264: 
265:     result = {
266:         "home_team": home_team,
267:         "away_team": away_team,
268:         "lambda_home": lambda_home,
269:         "lambda_away": lambda_away,
270:         "home_goals": home_goals,
271:         "away_goals": away_goals,
272:         "extra_time_home_goals": extra_home_goals,
273:         "extra_time_away_goals": extra_away_goals,
274:         "decided_by_penalties": decided_by_penalties,
275:         "winner": winner,
276:     }
277:     loser = away_team if winner == home_team else home_team
278:     return winner, loser, result
279: 
280: 
281: def resolve_group_stage(
282:     fixtures: pd.DataFrame,
283:     states: dict[str, TeamState],
284:     predictor: GoalPredictor,
285:     rng: np.random.Generator,
286: ) -> tuple[dict[str, dict[str, object]], list[dict[str, object]]]:
287: 
288:     group_matches = fixtures[fixtures["stage"].fillna("") == "GROUP"].copy()
289: 
290:     standings: dict[str, dict[str, object]] = {}
291:     match_logs: list[dict[str, object]] = []
292: 
293:     for _, row in group_matches.iterrows():
294:         home_team = str(row["home_team"])
295:         away_team = str(row["away_team"])
296:         home_goals, away_goals, lambda_home, lambda_away = simulate_group_match(
297:             row=row,
298:             states=states,
299:             predictor=predictor,
300:             rng=rng,
301:         )
302: 
303:         match_logs.append(
304:             {
305:                 "stage": "GROUP",
306:                 "group": row.get("group"),
307:                 "home_team": home_team,
308:                 "away_team": away_team,
309:                 "home_goals": home_goals,
310:                 "away_goals": away_goals,
311:                 "lambda_home": lambda_home,
312:                 "lambda_away": lambda_away,
313:             }
314:         )
315: 
316:         for team, goals_for, goals_against in (
317:             (home_team, home_goals, away_goals),
318:             (away_team, away_goals, home_goals),
319:         ):
320:             team_row = standings.setdefault(
321:                 team,
322:                 {
323:                     "team": team,
324:                     "group": str(row.get("group")) if not pd.isna(row.get("group")) else None,
325:                     "points": 0,
326:                     "goals_for": 0,
327:                     "goals_against": 0,
328:                     "goal_difference": 0,
329:                     "matches": 0,
330:                 },
331:             )
332:             team_row["goals_for"] += goals_for
333:             team_row["goals_against"] += goals_against
334:             team_row["goal_difference"] = team_row["goals_for"] - team_row["goals_against"]
335:             team_row["matches"] += 1
336: 
337:         if home_goals > away_goals:
338:             standings[home_team]["points"] += GROUP_STAGE_POINTS_WIN
339:         elif home_goals < away_goals:
340:             standings[away_team]["points"] += GROUP_STAGE_POINTS_WIN
341:         else:
342:             standings[home_team]["points"] += GROUP_STAGE_POINTS_DRAW
343:             standings[away_team]["points"] += GROUP_STAGE_POINTS_DRAW
344: 
345:     return standings, match_logs
346: 
347: 
348: def _team_elo(record: dict[str, object], states: dict[str, TeamState]) -> float:
349: 
350:     state = states.get(str(record["team"]))
351:     return float(state.elo) if state is not None else 0.0
352: 
353: 
354: def _shuffle_equal_blocks(
355:     ordered: list[dict[str, object]],
356:     key_func,
357:     rng: np.random.Generator,
358: ) -> list[dict[str, object]]:
359:     """Randomly permute teams that remain perfectly equal under ``key_func``."""
360: 
361:     index = 0
362:     while index < len(ordered):
363:         tie_end = index + 1
364:         while tie_end < len(ordered) and key_func(ordered[tie_end]) == key_func(ordered[index]):
365:             tie_end += 1
366:         if tie_end - index > 1:
367:             block = ordered[index:tie_end]
368:             order = list(range(len(block)))
369:             rng.shuffle(order)
370:             ordered[index:tie_end] = [block[i] for i in order]
371:         index = tie_end
372:     return ordered
373: 
374: 
375: def _resolve_overall_then_random(
376:     block: list[dict[str, object]],
377:     states: dict[str, TeamState],
378:     rng: np.random.Generator,
379: ) -> list[dict[str, object]]:
380:     """Tiebreakers 4-7: overall goal difference, overall goals for, Elo, then random."""
381: 
382:     def overall_key(record: dict[str, object]) -> tuple[int, int, float]:
383:         return (
384:             int(record["goal_difference"]),
385:             int(record["goals_for"]),
386:             _team_elo(record, states),
387:         )
388: 
389:     ordered = sorted(block, key=overall_key, reverse=True)
390:     return _shuffle_equal_blocks(ordered, overall_key, rng)
391: 
392: 
393: def _rank_tied_teams(
394:     tied: list[dict[str, object]],
395:     group_matches: list[dict[str, object]],
396:     states: dict[str, TeamState],
397:     rng: np.random.Generator,
398: ) -> list[dict[str, object]]:
399:     """Order teams that are level on overall points using FIFA tiebreakers 1-7."""
400: 
401:     if len(tied) == 1:
402:         return list(tied)
403: 
404:     tied_names = {str(record["team"]) for record in tied}
405:     head_to_head: dict[str, dict[str, int]] = {
406:         name: {"points": 0, "goals_for": 0, "goals_against": 0} for name in tied_names
407:     }
408: 
409:     for match in group_matches:
410:         home_team = str(match["home_team"])
411:         away_team = str(match["away_team"])
412:         if home_team not in tied_names or away_team not in tied_names:
413:             continue
414:         home_goals = int(match["home_goals"])
415:         away_goals = int(match["away_goals"])
416: 
417:         head_to_head[home_team]["goals_for"] += home_goals
418:         head_to_head[home_team]["goals_against"] += away_goals
419:         head_to_head[away_team]["goals_for"] += away_goals
420:         head_to_head[away_team]["goals_against"] += home_goals
421: 
422:         if home_goals > away_goals:
423:             head_to_head[home_team]["points"] += GROUP_STAGE_POINTS_WIN
424:         elif home_goals < away_goals:
425:             head_to_head[away_team]["points"] += GROUP_STAGE_POINTS_WIN
426:         else:
427:             head_to_head[home_team]["points"] += GROUP_STAGE_POINTS_DRAW
428:             head_to_head[away_team]["points"] += GROUP_STAGE_POINTS_DRAW
429: 
430:     def h2h_key(record: dict[str, object]) -> tuple[int, int, int]:
431:         stats = head_to_head[str(record["team"])]
432:         return (stats["points"], stats["goals_for"] - stats["goals_against"], stats["goals_for"])
433: 
434:     ordered = sorted(tied, key=h2h_key, reverse=True)
435: 
436:     result: list[dict[str, object]] = []
437:     index = 0
438:     while index < len(ordered):
439:         tie_end = index + 1
440:         while tie_end < len(ordered) and h2h_key(ordered[tie_end]) == h2h_key(ordered[index]):
441:             tie_end += 1
442:         block = ordered[index:tie_end]
443:         if len(block) == 1:
444:             result.extend(block)
445:         elif len(block) == len(tied):
446:             # Head-to-head separated nobody: fall through to overall criteria.
447:             result.extend(_resolve_overall_then_random(block, states, rng))
448:         else:
449:             # A smaller subset is still level: recompute head-to-head among them.
450:             result.extend(_rank_tied_teams(block, group_matches, states, rng))
451:         index = tie_end
452:     return result
453: 
454: 
455: def _order_group(
456:     teams: list[dict[str, object]],
457:     group_matches: list[dict[str, object]],
458:     states: dict[str, TeamState],
459:     rng: np.random.Generator,
460: ) -> list[dict[str, object]]:
461:     """Rank the four teams of a group: overall points first, then tiebreakers 1-7."""
462: 
463:     by_points = sorted(teams, key=lambda record: int(record["points"]), reverse=True)
464: 
465:     result: list[dict[str, object]] = []
466:     index = 0
467:     while index < len(by_points):
468:         tie_end = index + 1
469:         while tie_end < len(by_points) and int(by_points[tie_end]["points"]) == int(by_points[index]["points"]):
470:             tie_end += 1
471:         block = by_points[index:tie_end]
472:         if len(block) == 1:
473:             result.extend(block)
474:         else:
475:             result.extend(_rank_tied_teams(block, group_matches, states, rng))
476:         index = tie_end
477:     return result
478: 
479: 
480: def rank_group_teams(
481:     standings: dict[str, dict[str, object]],
482:     group_matches: list[dict[str, object]],
483:     states: dict[str, TeamState],
484:     rng: np.random.Generator,
485: ) -> tuple[dict[str, list[str]], list[str]]:
486: 
487:     groups: dict[str, list[dict[str, object]]] = defaultdict(list)
488:     for record in standings.values():
489:         group = str(record.get("group"))
490:         groups[group].append(record)
491: 
492:     matches_by_group: dict[str, list[dict[str, object]]] = defaultdict(list)
493:     for match in group_matches:
494:         matches_by_group[str(match.get("group"))].append(match)
495: 
496:     qualifiers: dict[str, list[str]] = {}
497:     third_place_candidates: list[dict[str, object]] = []
498: 
499:     for group_name in GROUP_ORDER:
500:         teams = groups.get(group_name, [])
501:         if len(teams) != 4:
502:             raise ValueError(f"Group {group_name} does not contain 4 teams in the simulation")
503: 
504:         ordered = _order_group(teams, matches_by_group.get(group_name, []), states, rng)
505: 
506:         qualifiers[group_name] = [str(ordered[0]["team"]), str(ordered[1]["team"])]
507:         third_place_candidates.append(ordered[2])
508: 
509:     # Best third-placed teams: rank by points, then by current Elo (random as last resort).
510:     def third_place_key(record: dict[str, object]) -> tuple[int, float]:
511:         return (int(record["points"]), _team_elo(record, states))
512: 
513:     third_place_candidates = sorted(third_place_candidates, key=third_place_key, reverse=True)
514:     third_place_candidates = _shuffle_equal_blocks(third_place_candidates, third_place_key, rng)
515: 
516:     third_place_order = [str(item["team"]) for item in third_place_candidates[:8]]
517:     return qualifiers, third_place_order
518: 
519: 
520: def resolve_placeholders(qualifiers: dict[str, list[str]], third_places: list[str]) -> dict[str, str]:
521: 
522:     mapping: dict[str, str] = {}
523:     for group_name in GROUP_ORDER:
524:         mapping[f"1{group_name}"] = qualifiers[group_name][0]
525:         mapping[f"2{group_name}"] = qualifiers[group_name][1]
526: 
527:     for index, team in enumerate(third_places, start=1):
528:         mapping[f"3rd_{index}"] = team
529: 
530:     return mapping
531: 
532: 
533: def materialize_fixture_value(value: object, mapping: dict[str, str]) -> str:
534: 
535:     if pd.isna(value):
536:         return ""
537:     text = str(value).strip()
538:     return mapping.get(text, text)
539: 
540: 
541: def resolve_knockout_fixtures(fixtures: pd.DataFrame, mapping: dict[str, str]) -> pd.DataFrame:
542: 
543:     resolved = fixtures.copy()
544:     for column in ["home_team", "away_team"]:
545:         resolved[column] = resolved[column].map(lambda value: materialize_fixture_value(value, mapping))
546:     return resolved
547: 
548: 
549: def build_bracket_maps() -> dict[str, list[str]]:
550: 
551:     return {
552:         "R32": [
553:             "W_R32_1",
554:             "W_R32_2",
555:             "W_R32_3",
556:             "W_R32_4",
557:             "W_R32_5",
558:             "W_R32_6",
559:             "W_R32_7",
560:             "W_R32_8",
561:             "W_R32_9",
562:             "W_R32_10",
563:             "W_R32_11",
564:             "W_R32_12",
565:             "W_R32_13",
566:             "W_R32_14",
567:             "W_R32_15",
568:             "W_R32_16",
569:         ],
570:         "R16": [
571:             "W_R16_1",
572:             "W_R16_2",
573:             "W_R16_3",
574:             "W_R16_4",
575:             "W_R16_5",
576:             "W_R16_6",
577:             "W_R16_7",
578:             "W_R16_8",
579:         ],
580:         "QF": ["W_QF1", "W_QF2", "W_QF3", "W_QF4"],
581:         "SF": ["W_SF1", "W_SF2"],
582:         "3RD": ["L_SF1", "L_SF2"],
583:         "FINAL": ["W_FINAL"],
584:     }
585: 
586: 
587: def run_knockout_round(
588:     fixtures: pd.DataFrame,
589:     states: dict[str, TeamState],
590:     predictor: GoalPredictor,
591:     rng: np.random.Generator,
592:     stage_name: str,
593: ) -> tuple[pd.DataFrame, dict[str, str], list[dict[str, object]]]:
594: 
595:     results: list[dict[str, object]] = []
596:     winner_mapping: dict[str, str] = {}
597:     losers: list[str] = []
598: 
599:     stage_matches = fixtures[fixtures["stage"].fillna("") == stage_name].copy()
600:     stage_matches = stage_matches.reset_index(drop=True)
601: 
602:     for index, row in stage_matches.iterrows():
603:         home_team = str(row["home_team"])
604:         away_team = str(row["away_team"])
605:         fixture_date = row["date"]
606:         city = str(row.get("city", ""))
607:         country = str(row.get("country", ""))
608:         neutral = parse_bool(row.get("neutral", True))
609: 
610:         winner, loser, match_result = simulate_knockout_match(
611:             home_team=home_team,
612:             away_team=away_team,
613:             date_value=fixture_date,
614:             tournament=str(row.get("tournament", "FIFA World Cup")),
615:             city=city,
616:             country=country,
617:             neutral=neutral,
618:             states=states,
619:             predictor=predictor,
620:             rng=rng,
621:         )
622: 
623:         results.append(
624:             {
625:                 "stage": stage_name,
626:                 "group": row.get("group"),
627:                 "home_team": home_team,
628:                 "away_team": away_team,
629:                 "resolved_home_team": home_team,
630:                 "resolved_away_team": away_team,
631:                 "winner": winner,
632:                 "loser": loser,
633:                 "home_goals": match_result["home_goals"],
634:                 "away_goals": match_result["away_goals"],
635:                 "lambda_home": match_result["lambda_home"],
636:                 "lambda_away": match_result["lambda_away"],
637:                 "decided_by_penalties": match_result["decided_by_penalties"],
638:             }
639:         )
640:         winner_mapping[f"{stage_name}_{index + 1}"] = winner
641:         losers.append(loser)
642: 
643:     result_frame = pd.DataFrame(results)
644:     return result_frame, winner_mapping, results
645: 
646: 
647: def resolve_knockout_bracket(
648:     fixtures: pd.DataFrame,
649:     states: dict[str, TeamState],
650:     predictor: GoalPredictor,
651:     rng: np.random.Generator,
652:     placeholder_map: dict[str, str],
653: ) -> tuple[list[dict[str, object]], dict[str, str], dict[str, str]]:
654: 
655:     all_results: list[dict[str, object]] = []
656:     winner_placeholders: dict[str, str] = {}
657:     loser_placeholders: dict[str, str] = {}
658: 
659:     knockout_order = ["R32", "R16", "QF", "SF", "3RD", "FINAL"]
660:     bracket_map = build_bracket_maps()
661: 
662:     current_map = dict(placeholder_map)
663: 
664:     for stage_name in knockout_order:
665:         stage_fixtures = fixtures[fixtures["stage"].fillna("") == stage_name].copy().reset_index(drop=True)
666:         if stage_fixtures.empty:
667:             continue
668: 
669:         for index, row in stage_fixtures.iterrows():
670:             resolved_home = materialize_fixture_value(row["home_team"], current_map)
671:             resolved_away = materialize_fixture_value(row["away_team"], current_map)
672:             if not resolved_home or not resolved_away:
673:                 raise ValueError(
674:                     f"Could not resolve knockout fixture {stage_name} #{index + 1}: "
675:                     f"{row['home_team']} vs {row['away_team']}"
676:                 )
677: 
678:             fixture_date = row["date"]
679:             city = str(row.get("city", ""))
680:             country = str(row.get("country", ""))
681:             neutral = parse_bool(row.get("neutral", True))
682: 
683:             winner, loser, match_result = simulate_knockout_match(
684:                 home_team=resolved_home,
685:                 away_team=resolved_away,
686:                 date_value=fixture_date,
687:                 tournament=str(row.get("tournament", "FIFA World Cup")),
688:                 city=city,
689:                 country=country,
690:                 neutral=neutral,
691:                 states=states,
692:                 predictor=predictor,
693:                 rng=rng,
694:             )
695: 
696:             all_results.append(
697:                 {
698:                     "stage": stage_name,
699:                     "group": row.get("group"),
700:                     "home_team": resolved_home,
701:                     "away_team": resolved_away,
702:                     "winner": winner,
703:                     "loser": loser,
704:                     "home_goals": match_result["home_goals"],
705:                     "away_goals": match_result["away_goals"],
706:                     "lambda_home": match_result["lambda_home"],
707:                     "lambda_away": match_result["lambda_away"],
708:                     "decided_by_penalties": match_result["decided_by_penalties"],
709:                 }
710:             )
711: 
712:             if stage_name in {"R32", "R16", "QF", "SF"}:
713:                 winner_key = bracket_map[stage_name][index]
714:                 current_map[winner_key] = winner
715:                 winner_placeholders[winner_key] = winner
716: 
717:             if stage_name == "SF":
718:                 loser_key = f"L_SF{index + 1}"
719:                 current_map[loser_key] = loser
720:                 loser_placeholders[loser_key] = loser
721: 
722:             if stage_name == "3RD":
723:                 # No placeholders are created by the third-place match itself.
724:                 pass
725: 
726:     return all_results, winner_placeholders, loser_placeholders
727: 
728: 
729: def update_stage_output_columns(fixtures: pd.DataFrame, placeholder_map: dict[str, str]) -> pd.DataFrame:
730: 
731:     output = fixtures.copy()
732:     output["resolved_home_team"] = output["home_team"].map(lambda value: materialize_fixture_value(value, placeholder_map))
733:     output["resolved_away_team"] = output["away_team"].map(lambda value: materialize_fixture_value(value, placeholder_map))
734:     return output
735: 
736: 
737: def make_final_rankings(
738:     group_standings: dict[str, dict[str, object]],
739:     qualifiers: dict[str, list[str]],
740:     third_place_order: list[str],
741:     champion: str,
742:     runner_up: str,
743: ) -> dict[str, list[dict[str, object]]]:
744: 
745:     group_tables = []
746:     for team, record in group_standings.items():
747:         group_tables.append(
748:             {
749:                 "team": team,
750:                 "group": record["group"],
751:                 "points": record["points"],
752:                 "goal_difference": record["goal_difference"],
753:                 "goals_for": record["goals_for"],
754:             }
755:         )
756: 
757:     return {
758:         "groups": group_tables,
759:         "qualifiers": [
760:             {"group": group_name, "first": teams[0], "second": teams[1]}
761:             for group_name, teams in qualifiers.items()
762:         ],
763:         "third_places": [{"rank": index + 1, "team": team} for index, team in enumerate(third_place_order)],
764:         "champion": [{"team": champion}, {"team": runner_up}],
765:     }
766: 
767: 
768: def simulate_world_cup(
769:     fixtures: pd.DataFrame,
770:     predictor: GoalPredictor,
771:     base_states: dict[str, TeamState],
772:     rng: np.random.Generator,
773: ) -> dict[str, object]:
774: 
775:     states = {
776:         team: TeamState(
777:             elo=team_state.elo,
778:             elo_history=deque(team_state.elo_history, maxlen=WINDOW_SIZE),
779:             win_history=deque(team_state.win_history, maxlen=WINDOW_SIZE),
780:             goals_for_history=deque(team_state.goals_for_history, maxlen=WINDOW_SIZE),
781:             goals_against_history=deque(team_state.goals_against_history, maxlen=WINDOW_SIZE),
782:         )
783:         for team, team_state in base_states.items()
784:     }
785: 
786:     group_fixtures = fixtures[fixtures["stage"].fillna("") == "GROUP"].copy()
787:     group_standings, group_logs = resolve_group_stage(group_fixtures, states, predictor, rng)
788:     qualifiers, third_place_order = rank_group_teams(group_standings, group_logs, states, rng)
789:     placeholder_map = resolve_placeholders(qualifiers, third_place_order)
790: 
791:     knockout_fixtures = fixtures[fixtures["stage"].fillna("") != "GROUP"].copy()
792:     knockout_results, winner_placeholders, loser_placeholders = resolve_knockout_bracket(
793:         knockout_fixtures,
794:         states,
795:         predictor,
796:         rng,
797:         placeholder_map,
798:     )
799: 
800:     placeholder_map.update(winner_placeholders)
801:     placeholder_map.update(loser_placeholders)
802: 
803:     final_match = next(result for result in knockout_results if result["stage"] == "FINAL")
804:     champion = str(final_match["winner"])
805:     runner_up = str(final_match["loser"])
806: 
807:     return {
808:         "groups": group_standings,
809:         "group_logs": group_logs,
810:         "knockout_results": knockout_results,
811:         "placeholder_map": placeholder_map,
812:         "champion": champion,
813:         "runner_up": runner_up,
814:         "third_place_order": third_place_order,
815:     }
816: 
817: 
818: def run_monte_carlo(n_simulations: int = N_SIMULATIONS, random_seed: int = RANDOM_SEED) -> dict[str, object]:
819: 
820:     if n_simulations <= 0:
821:         raise ValueError("n_simulations must be positive")
822: 
823:     rng = np.random.default_rng(random_seed)
824:     history = load_csv(HISTORICAL_PATH)
825:     fixtures = load_csv(FIXTURE_PATH)
826:     base_states = reconstruct_state(history)
827:     predictor = GoalPredictor()
828: 
829:     group_participants = fixtures[fixtures["stage"].fillna("") == "GROUP"]
830:     teams = sorted(
831:         set(group_participants["home_team"].astype(str)).union(set(group_participants["away_team"].astype(str)))
832:     )
833: 
834:     statistics = {
835:         team: {
836:             "r32": 0,
837:             "r16": 0,
838:             "quarterfinal": 0,
839:             "semifinal": 0,
840:             "final": 0,
841:             "champion": 0,
842:         }
843:         for team in teams
844:     }
845:     champion_counts: dict[str, int] = defaultdict(int)
846:     simulation_samples: list[dict[str, object]] = []
847: 
848:     for simulation_index in tqdm(range(n_simulations), desc="Simulating World Cup", unit="sim"):
849:         outcome = simulate_world_cup(fixtures, predictor, base_states, rng)
850: 
851:         group_standings = outcome["groups"]
852:         qualifiers = outcome["placeholder_map"]
853:         champion = str(outcome["champion"])
854:         runner_up = str(outcome["runner_up"])
855:         third_places = outcome["third_place_order"]
856: 
857:         qualified_r32 = set()
858:         qualified_r16 = set()
859:         qualified_qf = set()
860:         qualified_sf = set()
861:         qualified_final = {champion, runner_up}
862: 
863:         for group_name in GROUP_ORDER:
864:             qualified_r32.update([qualifiers[f"1{group_name}"], qualifiers[f"2{group_name}"]])
865: 
866:         qualified_r32.update(third_places[:8])
867: 
868:         for result in outcome["knockout_results"]:
869:             if result["stage"] == "R32":
870:                 qualified_r16.add(result["winner"])
871:             elif result["stage"] == "R16":
872:                 qualified_qf.add(result["winner"])
873:             elif result["stage"] == "QF":
874:                 qualified_sf.add(result["winner"])
875: 
876:         for team in teams:
877:             if team in qualified_r32:
878:                 statistics[team]["r32"] += 1
879:             if team in qualified_r16:
880:                 statistics[team]["r16"] += 1
881:             if team in qualified_qf:
882:                 statistics[team]["quarterfinal"] += 1
883:             if team in qualified_sf:
884:                 statistics[team]["semifinal"] += 1
885:             if team in qualified_final:
886:                 statistics[team]["final"] += 1
887:             if team == champion:
888:                 statistics[team]["champion"] += 1
889: 
890:         champion_counts[champion] += 1
891: 
892:         if simulation_index == 0:
893:             simulation_samples.append(
894:                 {
895:                     "groups": group_standings,
896:                     "champion": champion,
897:                     "runner_up": runner_up,
898:                     "knockout_results": outcome["knockout_results"],
899:                 }
900:             )
901: 
902:     probability_rows = []
903:     for team in sorted(statistics):
904:         probability_rows.append(
905:             {
906:                 "team": team,
907:                 "r32_probability": statistics[team]["r32"] / n_simulations,
908:                 "r16_probability": statistics[team]["r16"] / n_simulations,
909:                 "quarterfinal_probability": statistics[team]["quarterfinal"] / n_simulations,
910:                 "semifinal_probability": statistics[team]["semifinal"] / n_simulations,
911:                 "final_probability": statistics[team]["final"] / n_simulations,
912:                 "champion_probability": statistics[team]["champion"] / n_simulations,
913:             }
914:         )
915: 
916:     probability_frame = pd.DataFrame(probability_rows)
917:     probability_frame = probability_frame.sort_values(
918:         ["champion_probability", "final_probability", "semifinal_probability"],
919:         ascending=[False, False, False],
920:     ).reset_index(drop=True)
921: 
922:     top_10_champions = probability_frame.sort_values("champion_probability", ascending=False).head(10)
923:     summary = {
924:         "n_simulations": n_simulations,
925:         "top_10_champions": [
926:             {
927:                 "team": str(row.team),
928:                 "champion_probability": float(row.champion_probability),
929:             }
930:             for row in top_10_champions.itertuples(index=False)
931:         ],
932:     }
933: 
934:     RESULTS_DIR.mkdir(parents=True, exist_ok=True)
935:     probability_frame.to_csv(PROBABILITIES_CSV_PATH, index=False)
936:     with SUMMARY_JSON_PATH.open("w", encoding="utf-8") as handle:
937:         json.dump(summary, handle, indent=4, ensure_ascii=False)
938:         handle.write("\n")
939: 
940:     wcsims_payload = {
941:         "n_simulations": n_simulations,
942:         "random_seed": random_seed,
943:         "results_csv": str(PROBABILITIES_CSV_PATH),
944:         "summary_json": str(SUMMARY_JSON_PATH),
945:         "sample_run": simulation_samples,
946:         "top_10_champions": summary["top_10_champions"],
947:     }
948:     with WCSIMS_PATH.open("w", encoding="utf-8") as handle:
949:         json.dump(wcsims_payload, handle, indent=4, ensure_ascii=False)
950:         handle.write("\n")
951: 
952:     return {
953:         "probabilities": probability_frame,
954:         "summary": summary,
955:         "wcsims": wcsims_payload,
956:     }
957: 
958: 
959: def main() -> None:
960: 
961:     results = run_monte_carlo()
962:     print(f"Saved probability table to {PROBABILITIES_CSV_PATH}")
963:     print(f"Saved summary to {SUMMARY_JSON_PATH}")
964:     print(f"Saved full JSON payload to {WCSIMS_PATH}")
965:     top_champion = results["summary"]["top_10_champions"][0]
966:     print(f"Most likely champion: {top_champion['team']} ({top_champion['champion_probability']:.4f})")
967:     # mostrar todo el csv
968:     print("\nFull probability table:")
969:     pd.set_option("display.max_rows", None)
970:     print(results["probabilities"])
971: 
972: if __name__ == "__main__":
973:     main()

(End of file - total 973 lines)
</content>
```

---

## Assistant (Plan · Nemotron 3 Ultra Free · 27.6s)

_Thinking:_

Now I understand the problem. Let me analyze the issues:

1. **Formato incorrecto en `mundial_2026.csv`**: Looking at the CSV, I see that the knockout stage (R32) has placeholders like `1A`, `2B`, `3rd_1`, `3rd_2`, etc. The problem is that the current format for the 3rd place matches is hardcoded with `3rd_1` vs `3rd_2`, `3rd_3` vs `3rd_4`, etc. But according to FIFA rules, the pairing of 3rd place teams in the Round of 32 depends on which groups the best 3rd place teams come from. There are 495 possible combinations.

2. **FIFA combinations for best 3rd place teams**: In a 12-group World Cup (48 teams), the top 2 from each group (24 teams) plus the best 8 third-place teams (8 teams) advance to the Round of 32. The pairing of these 8 third-place teams is determined by a pre-defined FIFA table that depends on which specific groups the qualified 3rd place teams come from.

Let me search for the FIFA official combinations to understand the exact mapping.

Let me also look at how the current code handles this - I see in `resolve_placeholders` function (line 520-530), it just maps `3rd_1` through `3rd_8` to the top 8 third-place teams in order. But the actual fixtures in the CSV (lines 86-89) have:
- 3rd_1 vs 3rd_2
- 3rd_3 vs 3rd_4
- 3rd_5 vs 3rd_6
- 3rd_7 vs 3rd_8

This is a simplified/incorrect approach. The correct FIFA format specifies which specific 3rd place teams play each other based on the combination of groups they come from.

Let me research the FIFA official combinations for the 48-team World Cup format.

**Tool: websearch**

**Input:**
```json
{
  "query": "FIFA World Cup 2026 48 teams best third place teams knockout bracket combinations 495"
}
```

**Output:**
```
{
  "search_id": "search_21a03117e1ad4edc9a409c3ded860001",
  "results": [
    {
      "url": "https://worldcuppass.com/world-cup-2026-third-place-teams/",
      "title": "World Cup 2026 Third Place Teams: Standings and How 8 Qualify",
      "publish_date": "2026-06-14",
      "excerpts": [
        "Fewer deductions means a higher score and a higher rank.\n\n|Offense |Deduction |\n| --- | --- |\n|Yellow card |\\-1 |\n|Second yellow (indirect red) |\\-3 |\n|Direct red card |\\-4 |\n|Yellow and direct red (same match) |\\-5 |\n\nOnly one deduction applies per player per match. The team with the higher conduct score ranks above the other. So discipline can decide who reaches the Round of 32.\n\n## Are 4 points enough to qualify?\n\nIn most cases, yes. A third place team with four points is very likely to advance. Three points with a decent goal difference often makes it too.\n\nBut there is no fixed safe number. The full 12 team table decides every spot. A points total is a clue, not a guarantee, until every group finishes.\n\nSo watch goal difference closely. It is usually the deciding factor near the cut line.\n\n## How the bracket works with the 3rd place teams\n\nHow 3rd Place Teams Enter the Bracket\n\nThis is where it gets complex. The eight third-place teams do not fall into a fixed set of slots.\nFIFA uses a pre set mapping table, called Annex C in [the regulations](https://digitalhub.fifa.com/m/636f5c9c6f29771f/original/FWC2026_regulations_EN.pdf) .\n\nThat table assigns each qualifying third place team to a Round of 32 position. It holds 495 possible combinations, one for every way eight of the 12 thirds can qualify. The mapping depends on which eight groups produce the best thirds. Different groups produce different bracket paths.\n\nSo you cannot finalize a bracket on group winners alone. You also need the eight third place qualifiers. That is why this World Cup is harder to predict than the old 32 team format.\n\nYou can test full scenarios on our [World Cup 2026 simulator](https://worldcuppass.com/simulator) and track results on the [live scores page](https://worldcuppass.com/fifa-world-cup-2026-live-scores/) .\n\n## FAQ About World Cup 2026 Third Place Teams\n\n### Can a third place team win the World Cup?\n\nYes. A third place finish only affects the group stage.\nAfter that, every knockout match is level. A third place team can win five straight games and lift the trophy. Portugal did something similar at Euro 2016, advancing as a third place team and winning the title.\n\n### Can teams face their group rivals again in the Round of 32?\n\nNo. FIFA’s mapping system prevents rematches from the group stage. Two teams from the same group cannot meet again until the quarterfinals at the earliest.\n\n### When are the third place teams confirmed?\n\nAfter all 12 groups finish their final matches. The group stage ends June 27, 2026. The Round of 32 then runs from June 28 to July 3. The standings only settle once the last group game is played.\n\n### Can three teams from the same group qualify?\n\nYes. The top two qualify automatically. If that group’s third place team also ranks among the best eight, then three teams from one group advance. It is uncommon, but the format allows it.\n\n### Who do the third place teams play in the Round of 32?"
      ]
    },
    {
      "url": "https://match-later.com/en/wc2026/articles/knockout-bracket.html",
      "title": "How the Knockout Bracket Works — Round of 32 Pairings Explained — FIFA World Cup 2026 | Match Later",
      "publish_date": "2026-05-04",
      "excerpts": [
        "← Match Later ☼ ☾ 日本語\n\nFIFA World Cup 2026™\n\n# How the Knockout Bracket Works — Round of 32 Pairings Explained\n\nPublished: 2026-05-04\n\nHow the Round of 32 pairings are predetermined at the draw, with the full set of 16 fixtures laid out.\n\nThe expanded 48-team format introduces a brand-new **Round of 32** , the first knockout stage. Despite the apparent complexity of “8 of 12 third-placed teams advance,” the bracket pairings are **fully fixed from the draw onward** . This article explains how it works.\n\n## Key Premise: There Is No Second Draw\n\nIn the previous 32-team format (through Qatar 2022), the Round of 16 bracket was straightforward to read off the eight group standings.\n\nFor the 48-team format, with 12 groups and 8 of 12 third-placed teams advancing, the question of “which third-place teams come from which groups” has **495 possible scenarios** . FIFA has pre-mapped a Round of 32 bracket for **all 495 of them** .\nAs soon as the group stage ends, the bracket locks in automatically.\n\nIn other words: **the moment the final group standings are settled, all 16 Round of 32 fixtures are determined.**\n\n## Round of 32 Fixtures\n\nBelow are the 16 fixed pairings. A label like “3ABCDF” means “the third-placed team from one of Groups A, B, C, D, or F — depending on which third-place teams qualify.”\n\n|Match |Pairing |\n| --- | --- |\n|1 |**1E vs 3ABCDF** |\n|2 |**1I vs 3CDFGH** |\n|3 |**2A vs 2B** |\n|4 |**1F vs 2C** |\n|5 |**2K vs 2L** |\n|6 |**1H vs 2J** |\n|7 |**1D vs 3BEFIJ** |\n|8 |**1G vs 3AEHIJ** |\n|9 |**1C vs 2F** |\n|10 |**2E vs 2I** |\n|11 |**1A vs 3CEFHI** |\n|12 |**1L vs 3EHIJK** |\n|13 |**1J vs 2H** |\n|14 |**2D vs 2G** |\n|15 |**1B vs 3EFGIJ** |\n|16 |**1K vs 3DEIJL** |\n\nLegend:\n\n* **1A** = Winner of Group A\n* **2B** = Runner-up of Group B\n* **3ABCDF** = One third-placed team from Groups A, B, C, D, or F (based on which third-placers qualify)\n\n## Group F’s (Japan’s) Path\nIf the top two of Group F advance, they meet:\n\n* **1F (Group F winner)** → plays 2C (Group C runner-up) — Match 4\n* **2F (Group F runner-up)** → plays 1C (Group C winner) — Match 9\n\nSo Group F faces **Group C** regardless of whether they finish 1st or 2nd.\n\nIf a Group F team advances as a third-placed team:\n\n* **3F** could be slotted into Match 1, 7, 11, or 15 depending on which third-place teams qualify\n\n## Beyond the Round of 32\n\nEach of the 16 winners advances to the Round of 16. The pairings:\n\n|To Quarter-final |Bracket from R16 |\n| --- | --- |\n|QF1 |Winner of Match 1 vs Winner of Match 2 |\n|QF2 |Winner of Match 3 vs Winner of Match 4 |\n|QF3 |Winner of Match 5 vs Winner of Match 6 |\n|QF4 |Winner of Match 7 vs Winner of Match 8 |\n|QF5 |Winner of Match 9 vs Winner of Match 10 |\n|QF6 |Winner of Match 11 vs Winner of Match 12 |\n|QF7 |Winner of Match 13 vs Winner of Match 14 |\n|QF8 |Winner of Match 15 vs Winner of Match 16 |"
      ]
    },
    {
      "url": "https://theworldcupguide.com/world-cup-2026-group-and-bracket-predictor/",
      "title": "World Cup 2026 Group and Bracket Simulator - The World Cup Guide",
      "publish_date": "2026-06-10",
      "excerpts": [
        "[Home](https://theworldcupguide.com \"The World Cup Guide\") » World Cup 2026 Group and Bracket Simulator\n\n# World Cup 2026 Group and Bracket Simulator\n\n_This is an independent fan experience and is not affiliated with or endorsed by FIFA or any official tournament organizer._\n\nA Note From the Founder\n\nOur bracket is free on purpose. No ad walls, no paywalls, no catch. It costs real money to keep it that way. If you enjoyed it, a small tip goes a long way.\n\n[Send a Tip →](https://donate.stripe.com/3cI00l4XJeQ4fqZ9Pr83C00)\n\n**Begin by pressing “Create A Bracket” button below**\n\n[🏆 2026 WC Bracket Predictor * ✓ Predict all 12 Groups * ✓ Select 8 third-place qualifiers * ✓ All 495 knockout scenarios * ✓ Complete bracket to your champion * ✓ Share & Save Your Results * ✓ Create & Join Groups to Compete w/ Friends CREATE A BRACKET →](http://2026bracket.vercel.app)\n\nPlanning a club match trip?\n\n[Matchday Guide](https://www.matchdayguide.com/teams)\nInsider info on tickets, pubs, hotels & matchday experiences at Europe’s top clubs. Covering Man United, Barcelona, Real Madrid, Bayern, Liverpool, Arsenal & more!\n\n[Explore Guides →](https://www.matchdayguide.com)\n\n**UPDATE: December 30, 2026** – Launched an updated version to **Save Bracket, Create Groups, Join Groups, Compete Against Friends** , etc. Plus, a global leaderboard.\n\nThis bracket simulator creates the Round of 32 **using the 495 different 3rd Place qualifiers combinations** . We use the specifics that [FIFA outlines in their Regulations for the FIFA World Cup 26 document](https://digitalhub.fifa.com/m/636f5c9c6f29771f/original/FWC2026_regulations_EN.pdf) .\n\nUse this simulator to better guess:\n\n* **Where** your team may play\n* **When** your team may play in knockouts and\n* **Who** they may play\n* **Share the results** , save your bracket and/or create a group to compete with friends at the end!\n\n**Share & Tag us on the socials via** :\n\n* **[@theworldcupguide](https://www.\ninstagram.com/theworldcupguide/)** on instagram\n* **[@World\\_Cup\\_Guide](https://x.com/World_Cup_Guide)** on X/Twitter\n\n**BELOW IS AN EXAMPLE** of what the **Results Summary screen looks like** that will post to instagram, etc.\n\nScreenshot\n\n## **Stay Informed**\n\n* Start Planning with the [2026 Host City Guides](https://theworldcupguide.com/what-are-the-2026-world-cup-host-cities/)\n* Follow us on [X](https://twitter.com/world_cup_guide) and [instagram](https://www.instagram.com/theworldcupguide/)\n* If you’d like to discuss a collaboration, [send a message](https://theworldcupguide.com/contact-us/)\n\nHow helpful is this content?\n\nClick on a star to rate it!\n\n* \n* \n* \n*\n\nSubmit Rating\n\nWe Want To Hear From You!\n\nAll Feedback Is Welcomed\n\nWhat made you rate this as you did and/or send a comment!\n\nSubmit Feedback\n\n### Share this:\n\n* Share\n\n### Like this:\n\nLike Loading…\n\n##### Join Our Newsletter\n\nSubscribe\n\nSearch Search …\n\n### Subscribe to Stay Up to Date"
      ]
    },
    {
      "url": "https://footykitsbattle.com/format",
      "title": "World Cup 2026 Format Explained — 48 Teams, Groups & Bracket",
      "publish_date": null,
      "excerpts": [
        "Footy Kits Battle Search\n\nTournament format\n\n# 48-Team World Cup 2026 Bracket & Format\n\nThe complete 48-team World Cup 2026 bracket explained: 12 groups of 4, third-place qualification rules, and the knockout path from Round of 32 to the final in New York.\n\nQuick answer\n\nThe 2026 FIFA World Cup features 48 teams in 12 groups of 4. The top 2 from each group plus the 8 best third-placed teams advance to a 32-team knockout round. All matches are played across 16 venues in the USA, Mexico, and Canada from June 11 to July 19, 2026.\n\nToday's fixtures → UK kick-off times → Printable wall chart → All 48 team kits →\n\nIf you came from Google\n\n## Use the format page as your tournament map\n\nThe 48-team format only makes sense when you connect it to the daily fixtures. Start with the group rules here, then jump into the live matchday hub for kit colours, UK TV, kick-off times and the shirts playing today.\n\nOpen World Cup matchday hub → [Shop 2026 football shirts →](https://www.amazon.co.uk/s?\nk=world%20cup%202026%20football%20shirt&tag=footykitsbattle-21) [Wall chart on Amazon →](https://www.amazon.co.uk/s?k=world%20cup%202026%20wall%20chart&tag=footykitsbattle-21)\n\n## 2026 FIFA World Cup at a glance\n\n|Tournament |FIFA World Cup 2026 |\n| --- | --- |\n|Dates |11 June 2026 – 19 July 2026 |\n|Hosts |United States, Canada, Mexico |\n|Host cities |16 across 3 nations |\n|Teams |48 (up from 32 in 2022) |\n|Group stage |12 groups of 4 teams |\n|Matches per team (group) |3 |\n|Teams advancing from groups |32 (top 2 + 8 best third-placed) |\n|Knockout format |Round of 32 → R16 → QF → SF → 3rd-place → Final |\n|Total matches |104 (up from 64 in 2022) |\n|Opening match |11 June 2026, Estadio Azteca, Mexico City |\n|Final |19 July 2026, MetLife Stadium, New York / New Jersey |\n\n## Knockout round progression\n\n|Round |Teams entering |Matches |Teams advancing |\n| --- | --- | --- | --- |\n|Group stage |48 |72 |32 |\n|Round of 32 |32 |16 |16 |\n|Round of 16 |16 |8 |8 |\n|Quarter-finals |8 |4 |4 |\n|Semi-finals |4 |2 |2 |\n|Third-place play-off |2 |1 |— |\n|Final |2 |1 |1 champion |\n\n## Group Stage\n\nThe tournament opens with 12 groups of 4 teams. Every side plays 3 matches. The top 2 teams in each group qualify automatically for the knockout stage. The 12 groups themselves were set live in Las Vegas — see the full FIFA World Cup 2026 draw breakdown for the four seeding pots, confederation rules, and how every group was produced.\n\nExplore all 12 groups → See how the draw worked →\n\n## Third-Place Qualification\n\nThe 8 best third-placed teams also move on. They are ranked by points first, then goal difference, then goals scored, then fair play record, with drawing of lots available only if teams are still level after that.\n\n## Knockout Stage\n\nOnce the bracket starts, it becomes straight single elimination: Round of 32, Round of 16, quarter-finals, semi-finals, third-place playoff, and final. If a knockout match is level after 90 minutes, it goes to extra time and then penalties if needed."
      ]
    },
    {
      "url": "https://www.foxsports.com/stories/soccer/2026-fifa-world-cup-bracket-simulating-tournament-based-betting-favorites",
      "title": "2026 FIFA World Cup Bracket: Simulating the Tournament Based on Betting Favorites | FOX Sports",
      "publish_date": "2026-06-03",
      "excerpts": [
        "From the opening match on June 11 to the World Cup Final on July 19 at New York New Jersey Stadium, the tournament will feature a record 104 matches packed with drama, chaos, heartbreak and many unforgettable moments - [all streaming on FOX One](https://www.fox.com/soccer/fifa-world-cup?cmpid=org=one::ag=owned_other::mc=referral::src=fs::cmp=10010131002::add=625e) .\n\nWith so many matches and an expanded knockout stage, predicting how the bracket could unfold has become even more fascinating.\n\nHere is a full look at a projected World Cup bracket based entirely on betting favorites advancing through every round of the tournament. In other words, this is the \"all chalk\" bracket.\n\n_This page may contain affiliate links to legal sports betting partners. If you sign up or place a wager, FOX Sports may be compensated. Read more about_ [_Sports Betting on FOX Sports_](https://www.foxsports.com/stories/betting/sports-betting-on-fox-sports) _._\n\n## How the Bracket Was Built\nTo simulate the 2026 World Cup bracket, every pick was based entirely on betting markets. Using DraftKings odds, we advanced the favorite at every stage of the tournament.\n\nGroup winners and runners-up were determined using odds to win each group along with odds to qualify from the group stage. The eight third-place teams that advanced were selected by comparing qualification odds across all 12 groups.\n\nBecause the 48-team format includes predetermined knockout pairings for third-place qualifiers, FIFA’s official tournament regulations were used to place every advancing team into the correct Round of 32 matchup.\n\nFrom there, every knockout match was decided by which nation had shorter odds to win the World Cup outright.\n\n## Projected Round of 32 Matchups:\n\nThe knockout stage officially begins with the Round of 32, where every group winner and runner-up automatically advances.\n\nThe favorite to win each group was placed into the No.\n1 position from that group, while the team with the second-best odds to win the group was slotted into the No. 2 position for their respective group.\n\nTo determine those final eight spots, we used the betting odds in the \"to qualify from group\" markets and selected the strongest remaining teams that were not projected to finish first or second in their groups.\n\nHere’s how the projected Round of 32 would look if every group favorite advanced based on current DraftKings odds.\n\n* **Germany vs. Paraguay**\n* **France vs. Sweden**\n* **South Korea vs. Canada**\n* **Netherlands vs. Morocco**\n* **Colombia vs. Croatia**\n* **Spain vs. Austria**\n* **USA vs. Bosnia & Herzegovina**\n* **Belgium vs. Czechia**\n\n* **Brazil vs. Japan**\n* **Ecuador vs. Norway**\n* **Mexico vs. Scotland**\n* **England vs. Senegal**\n* **Argentina vs. Uruguay**\n* **Türkiye vs. Egypt**\n* **Switzerland vs. Algeria**\n* **Portugal vs. Ivory Coast**"
      ]
    },
    {
      "url": "https://www.bracketsninja.com/blog/fifa-world-cup-bracket-format-explained",
      "title": "FIFA World Cup Bracket Format Explained (2026 48-Team Guide)",
      "publish_date": null,
      "excerpts": [
        "Brackets by Common ninja logo\n\n#### Join Our Newsletter!\n\nKeep up to date with our latest blog posts, new widgets and features, and the Common Ninja Developer Platform.\n\nSubscribe!\n\nSubscribe\n\n# FIFA World Cup Bracket Format Explained: How the New 48-Team Format Works\n\n##### Sergei Davidov, May 06, 2026\n\nFIFA World Cup Bracket Format Explained: How the New 48-Team Format Works\n\n🏆\n\nPut the format to work\n\n### Now predict the whole tournament with friends\n\nOnce you know the format, Trofeo.live makes it a game: pick your group winners and knockout results, then track who called it right on a live leaderboard. Free for up to 50 players, no betting involved.\n\n[Create a Pool](https://trofeo.live/?utm_source=bracketsninja&utm_medium=blog_banner&utm_campaign=fifa_world_cup&utm_content=fifa-world-cup-bracket-format-explained)\n\nThe 2026 FIFA World Cup is the biggest format change in the tournament's history.\nThe field grows from 32 teams to 48, the group stage splits into 12 groups of four, and the knockouts open with a brand-new Round of 32. If you want to fill out a bracket, run a pool, or just understand the path your team has to walk to lift the trophy, you need a clean mental model of how the new format actually works.\n\n**Quick answer:** The 2026 FIFA World Cup expands to 48 teams in 12 groups of four. The top two from each group qualify automatically for the knockouts, joined by the eight best third-placed teams, creating a 32-team Round of 32. From there it is straight single-elimination through the Round of 16, Quarterfinals, Semifinals, third-place match, and the Final on July 19, 2026 at MetLife Stadium in New Jersey.\n\n## How the 2026 FIFA World Cup format works\n\n**The 2026 World Cup uses a hybrid format: a round-robin group stage followed by a [single-elimination knockout bracket](https://www.bracketsninja.com/blog/basics-of-single-elimination-brackets) .\n** 48 teams compete across 16 host cities in the United States, Canada, and Mexico from June 11 to July 19, 2026. The tournament has 104 matches in total, up from 64 in Qatar 2022.\n\nThis is the first World Cup since 1998 to expand the field, and the first ever to include a Round of 32. FIFA settled on the 12 groups of four configuration in March 2023 after testing alternatives like 16 groups of three, which would have created an incentive for late-stage collusion.\n\n## Group stage: 12 groups of four explained\n\n**The group stage runs from June 11 to roughly June 27, 2026, with each team playing three matches.** The 48 teams are drawn into 12 groups labeled A through L. Each group plays a single round-robin, three points for a win, one for a draw, zero for a loss.\n\n### How groups are seeded\n\n**Teams are placed into four pots of 12 based on the FIFA World Ranking, with the three host nations seeded into Pot 1."
      ]
    },
    {
      "url": "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/groups-how-teams-qualify-tie-breakers",
      "title": "World Cup 2026 groups, qualification rules & tie-breakers explained",
      "publish_date": "2026-06-13",
      "excerpts": [
        "* FIFA REWARDS\n* [FIFA+](https://www.plus.fifa.com/?intcmp=%28p_fifacom%29_%28d_plusfifa%29_%28c_webuniversal-fwc2026%29_%28sc_home%29_%28ssc_%29_%28sssc_%29_%28l_en%29_%28da_12062026%29)\n* [FIFA STORE](https://store.fifa.com/?intcmp=%28p_fifacom%29_%28d_fifastore%29_%28c_webuniversal-fwc2026%29_%28sc_fifastore%29_%28ssc_%29_%28sssc_%29_%28l_en%29_%28da_12062026%29)\n* [FIFA COLLECT](https://collect.fifa.com/en-UK?utm_source=fifa&utm_medium=website&utm_campaign=FIFA_web&referrer=FIFA_Comm_FIFA_web&intcmp=%28p_fifacom%29_%28d_fifacollect%29_%28c_webuniversal-fwc2026%29_%28sc_fifacollect%29_%28ssc_%29_%28sssc_%29_%28l_en%29_%28da_12062026%29)\n\n|\n\nEnglish\n\n|\n\nFIFA World Cup 2026™\n\n* MATCHES\n* STANDINGS\n* TEAMS & STATS\n* LATEST\n* FANTASY & GAMING\n* TICKETS & HOSPITALITY\n* HOST CITIES & STADIUMS\n* FAN EXPERIENCE\n* ORGANISATION\n* MORE\n\n* MATCHES\n* STANDINGS\n* TEAMS & STATS\n* LATEST\n* MORE\n\nBack\n\n# World Cup 2026 groups: How teams qualify and tie-breakers\n\nPublished\n    13 Jun 2026\n\nShare\nThe 48 qualified nations have been drawn into 12 groups of four. Find out who they will play, how teams qualify for the knockout round and what the tie-breakers are.\n\nThe stage is set. The full list of [48 teams](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/world-cup-2026-who-has-qualified) who will compete in the [FIFA World Cup 2026™](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026) is now confirmed and the [12 groups](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/standings) are complete for the global showpiece in [Canada](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/canada) , [Mexico](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/mexico) and the [United States](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/usa) .\n\n[The 104-game tournament](https://www.fifa."
      ]
    },
    {
      "url": "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/final-draw-results",
      "title": "Final Draw results | FIFA World Cup 2026",
      "publish_date": null,
      "excerpts": [
        "/Republic of Ireland\n\n### **Group B** **Group B**\n\nCanada\nBosnia and Herzegovina/Italy/Northern Ireland\n/Wales Qatar\nSwitzerland\n\n### **Group C** **Group C**\n\nBrazil\nMorocco\nHaiti\nScotland\n\n### **Group D** **Group D**\n\nUSA\nParaguay\nAustralia\nKosovo/Romania/Slovakia/Türkiye\n\n### **Group E** **Group E**\n\nGermany\nCuraçao Côte d'Ivoire\nEcuador\n\n### **Group F** **Group F**\n\nNetherlands\nJapan\nAlbania/Poland/Sweden/Ukraine\nTunisia\n\n### **Group G** **Group G**\n\nBelgium\nEgypt\nIR Iran\nNew Zealand\n\n### **Group H** **Group H**\n\nSpain\nCabo Verde\nSaudi Arabia\nUruguay\n\n### **Group I** **Group I**\n\nFrance\nSenegal\nBolivia/Iraq/Suriname\nNorway\n\n### **Group J** **Group J**\n\nArgentina\nAlgeria\nAustria\nJordan\n\n### **Group K** **Group K**\n\nPortugal\nCongo DR/Jamaica/New Caledonia\nUzbekistan\nColombia\n\n### **Group L** **Group L**\n\nEngland\nCroatia\nGhana\nPanama\n\n* * *\n\n## **Format and remaining qualifiers** **Format and remaining qualifiers**\nThe top two teams from each section and eight best third-place teams from the groups will progress to the Round of 32 at FIFA World Cup 2026.\n\nPlay Video\n\nLearn more\n\nRelated content Related content Share Video Share Video\n\nPlaying on\n\nSubtitles\n\n* English\n\nSettings\n\n* Quality Automatic Automatic HD\n* Speed Normal\n* Subtitle Options\n\nQuality\n\n* Automatic\n\nSpeed\n\n* 0\\.25\n* 0\\.5\n* Normal\n* 1\\.25\n* 1\\.5\n* 2\n\nSubtitle Options\n\n* Font family Default\n* Font color Default\n* Font opacity Default\n* Font size Default\n* Background color Default\n* Background opacity Default\n* Window color Default\n* Window opacity Default\n* Character edge style Default\n\nFont family\n\n* Default\n* Monospaced Serif\n* Proportional Serif\n* Monospaced Sans-Serif\n* Proportional Sans-Serif\n\nFont color\n\n* Default\n* White\n* Yellow\n* Green\n* Cyan\n* Blue\n* Magenta\n* Red\n* Black\n\nFont opacity\n\n* Default\n* 25%\n* 50%\n* 75%\n* 100%\n\nFont size\n\n* Default\n* 50%\n* 75%\n* 100%\n* 150%\n* 200%\n\nBackground color\n\n* Default\n* White\n* Yellow"
      ]
    },
    {
      "url": "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/knockout-stage-match-schedule-bracket",
      "title": "FIFA World Cup 2026 | Knockout stage match schedule bracket",
      "publish_date": null,
      "excerpts": [
        "Using the link below, you can contact our Data Protection team to place a do not sell or share my personal information request:  \nDo not sell my personal data\n\n#### Strictly Necessary Cookies\n\nAlways Active\n\nThese cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms.    You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.\n\nView Vendor Details\n\n#### Functional Cookies\n\nFunctional Cookies Inactive\n\nThese cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages.\nIf you do not allow these cookies then some or all of these services may not function properly.\n\nView Vendor Details\n\n#### Performance Cookies\n\nPerformance Cookies Inactive\n\nThese cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site.    All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.\n\nView Vendor Details\n\n#### Targeting Cookies\n\nTargeting Cookies Inactive\n\nThese cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites."
      ]
    },
    {
      "url": "https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_knockout_stage",
      "title": "2026 FIFA World Cup knockout stage - Wikipedia",
      "publish_date": null,
      "excerpts": [
        "The knockout stage of the 2026 FIFA World Cup will be the second and final stage of the competition, following the group stage . Played from June 28 to July 19, 2026, the knockout stage will end with the final , to be held at MetLife Stadium in East Rutherford , New Jersey . [[ 1 ]]() The top two teams from each of the twelve groups, along with the best eight third-placed teams , will advance to the knockout stage to compete in a single-elimination tournament . There will be 32 matches in the knockout stage, including a match for third place. [[ 2 ]]()\n\n## Format\n\nThe knockout stage of the 2026 FIFA World Cup will be contested between 32 teams that qualify from the group stage. Matches in the knockout stage will be played to a finish. If the score of a match is level at the end of 90 minutes of playing time, 30 minutes of extra time\") will be played. If the scores were still tied, the match will be decided by a penalty shootout\") . [[ 2 ]]() All times listed are local. [[ 1 ]]()\nIn the round of 32, four of the group winners play group runners up. The other eight group winners play advancing 3rd-placed teams. The remaining group runners up play other group runners up.\n\nFIFA set out the following schedule for the round of 32: [[ 2 ]]()\n\n* **Match 73** : Runner-up Group A vs Runner-up Group B\n* **Match 74** : Winner Group E vs Best 3rd place Group A/B/C/D/F\n* **Match 75** : Winner Group F vs Runner-up Group C\n* **Match 76** : Winner Group C vs Runner-up Group F\n* **Match 77** : Winner Group I vs Best 3rd place Group C/D/F/G/H\n* **Match 78** : Runner-up Group E vs Runner-up Group I\n* **Match 79** : Winner Group A vs Best 3rd place Group C/E/F/H/I\n* **Match 80** : Winner Group L vs Best 3rd place Group E/H/I/J/K\n* **Match 81** : Winner Group D vs Best 3rd place Group B/E/F/I/J\n* **Match 82** : Winner Group G vs Best 3rd place Group A/E/H/I/J\n* **Match 83** : Runner-up Group K vs Runner-up Group L\n* **Match 84** : Winner Group H vs Runner-up Group J"
      ]
    }
  ],
  "warnings": null,
  "usage": [
    {
      "name": "sku_search",
      "count": 1
    }
  ],
  "session_id": "ses_105f1b0b0ffevbjgqjCjei3gcF"
}
```

---

## Assistant (Plan · Nemotron 3 Ultra Free · 22.6s)

_Thinking:_

Now I have a good understanding of the FIFA official bracket for the 48-team World Cup 2026. Let me also check the Wikipedia article for the complete 495 combinations mapping.

**Tool: websearch**

**Input:**
```json
{
  "query": "FIFA World Cup 2026 third place teams bracket combinations Annex C 495 combinations table"
}
```

**Output:**
```
{
  "search_id": "search_e1d54c840ef345429d9ca0c4ad90814f",
  "results": [
    {
      "url": "https://worldcupwiki.com/2026-fifa-world-cup-round-of-32",
      "title": "2026 FIFA World Cup Round of 32: Teams, Schedule, Bracket & Format",
      "publish_date": "2026-06-20",
      "excerpts": [
        "|Group |Winner (1st) |Runner-up (2nd) |\n| --- | --- | --- |\n|Group A |🇲🇽 Mexico |TBD |\n|Group B |TBD |TBD |\n|Group C |TBD |TBD |\n|Group D |🇺🇸 United States |TBD |\n|Group E |🇩🇪 Germany |TBD |\n|Group F |TBD |TBD |\n|Group G |TBD |TBD |\n|Group H |TBD |TBD |\n|Group I |TBD |TBD |\n|Group J |TBD |TBD |\n|Group K |TBD |TBD |\n|Group L |TBD |TBD |\n\n### Best Third-Place Teams (8 teams)\n\n|\\# |Team |From Group |\n| --- | --- | --- |\n|1 |TBD |TBD |\n|2 |TBD |TBD |\n|3 |TBD |TBD |\n|4 |TBD |TBD |\n|5 |TBD |TBD |\n|6 |TBD |TBD |\n|7 |TBD |TBD |\n|8 |TBD |TBD |\n\n## How the Round of 32 Works (Format)\n\nThe Round of 32 starts right after the group stage ends on June 27, 2026. Each of the twelve [groups](https://worldcupwiki.com/groups/) sends its top two teams into the knockout phase. That fills twenty-four of the thirty-two spots. The last eight go to the best third-place teams across all twelve groups.\n\n**FIFA ranks third-place teams using six criteria in this exact order:**\n\n1.\nPoints earned in the group stage\n2. Goal difference\n3. Total goals scored\n4. Fair play score (yellow and red cards)\n5. FIFA World Ranking\n6. Drawing of lots\n\nEvery match is single-elimination. A tied score after ninety minutes leads to thirty minutes of extra time, played as two fifteen-minute halves. A penalty shootout decides the winner if the teams remain level after extra time.\n\n### The 495-Scenario Bracket System\n\nEight of the twelve third-place teams move into the Round of 32, so FIFA cannot fix all pairings before the group stage ends. It solved this by pre-planning 495 different bracket setups, listed in Annex C of the official tournament regulations. Each setup covers one possible combination of eight third-place teams advancing from twelve groups.\n\nThree rules stay fixed no matter which teams advance:\n\n* Group winners face a runner-up or a third-place team, never another group winner.\n* Third-place teams always face group winners, never runners-up or each other.\n* No team faces a team from its own group in the Round of 32.\n\nThe [bracket](https://worldcupwiki.com/bracket/) locks on June 27 once all group matches finish. No second draw takes place after that point.\n\n## 2026 FIFA World Cup Round of 32 Schedule\n\nThe **2026 FIFA World Cup Round of 32** runs from June 28 to July 3 across North America. Two to three matches take place each day, and each result decides who moves into the [Round of 16](https://worldcupwiki.com/2026-fifa-world-cup-round-of-16/) . All kickoff times below are listed in Eastern Time (ET).\n\n|Date |Match |No. |Time (ET) |Location |\n| --- | --- | --- | --- | --- |\n|Sun, Jun. 28 |Runner-up Group A vs. Runner-up Group B |73 |3:00 PM |SoFi Stadium, Inglewood |\n|Mon, Jun. 29 |Winner Group C vs. Runner-up Group F |76 |1:00 PM |NRG Stadium, Houston |\n|Mon, Jun. 29 |**Germany** vs. 3rd Group A/B/C/D/F |74 |4:30 PM |Gillette Stadium, Foxborough |\n|Mon, Jun. 29 |Winner Group F vs.\n\n...\n\nEvery World Cup from 1986 to 2022 started its knockout phase with the Round of 16; the 2026 World Cup adds the Round of 32 before it.\n\n### Can a team that finishes third in their group still win the World Cup?\n\nYes. Eight third-place teams advance to the Round of 32, and from that point they have the same shot at the title as every other qualified team. World Cup history shows that underdogs can go deep once the knockout rounds begin.\n\n### What are the 495 scenarios and why do they matter?\n\nEight of the twelve third-place teams advance to the Round of 32, creating 495 possible combinations of which eight teams those could be. FIFA pre-planned a bracket setup for all 495 combinations before the tournament started, so the bracket locks into the correct setup on its own once the group stage ends. No extra draw takes place.\n\n### What happens if a Round of 32 match ends in a tie?\n\nNo knockout match can end in a draw."
      ]
    },
    {
      "url": "https://github.com/m7mdehab/WC2026-Live-Prediction-Engine/blob/main/data/third_place_matrix_2026.README.md",
      "title": "Third-Place Matrix (Annex C) — Deferred Extraction",
      "publish_date": null,
      "excerpts": [
        "The 2026 World Cup uses a 495-row matrix (FIFA Regulations Annex C) that maps each of the 495 possible \"which 8 of 12 third-placed groups qualify\" combinations to specific R32 matchups."
      ]
    },
    {
      "url": "https://dev.to/mark_b5f4ffdd8e7cd58/encoding-fifas-495-third-place-scenarios-for-the-2026-world-cup-4814",
      "title": "Encoding FIFA’s 495 third-place scenarios for the 2026 World Cup - DEV Community",
      "publish_date": "2026-05-27",
      "excerpts": [
        "DEV Community\n\n[Powered by Algolia](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral)\n\n \n\n## DEV Community\n\nAdd reaction\n\nLike Unicorn Exploding Head Raised Hands Fire\n\nJump to Comments Save Boost\n\nCopy link\n\n[Share to X](https://twitter.com/intent/tweet?text=%22Encoding%20FIFA%E2%80%99s%20495%20third-place%20scenarios%20for%20the%202026%20World%20Cup%22%20by%20Mark%20%23DEVCommunity%20https%3A%2F%2Fdev.to%2Fmark_b5f4ffdd8e7cd58%2Fencoding-fifas-495-third-place-scenarios-for-the-2026-world-cup-4814) [Share to LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fdev.to%2Fmark_b5f4ffdd8e7cd58%2Fencoding-fifas-495-third-place-scenarios-for-the-2026-world-cup-4814&title=Encoding%20FIFA%E2%80%99s%20495%20third-place%20scenarios%20for%20the%202026%20World%20Cup&summary=I%20expected%20the%202026%20World%20Cup%20bracket%20to%20be%20a%20sorting%20problem.%20%20It%20turned%20out%20to%20be%20a%20sorting%20problem...\n&source=DEV%20Community) [Share to Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fdev.to%2Fmark_b5f4ffdd8e7cd58%2Fencoding-fifas-495-third-place-scenarios-for-the-2026-world-cup-4814) [Share to Mastodon](https://s2f.kytta.dev/?text=https%3A%2F%2Fdev.to%2Fmark_b5f4ffdd8e7cd58%2Fencoding-fifas-495-third-place-scenarios-for-the-2026-world-cup-4814)\n\nReport Abuse\n\nMark\n\nMark\n\nPosted on May 27\n\n# Encoding FIFA’s 495 third-place scenarios for the 2026 World Cup\n\n\\# algorithms \\# computerscience \\# programming \\# showdev\n\nI expected the 2026 World Cup bracket to be a sorting problem.\n\nIt turned out to be a sorting problem plus a lookup table.\n\nI recently worked on a small World Cup 2026 bracket project, and the strangest part was not building the knockout bracket itself. It was handling the third-placed teams.\n\nThe new format has:\n\n* 48 teams\n* 12 groups\n* 24 teams qualifying as group winners and runners-up\n* 8 more teams qualifying as the best third-placed teams\n* a new Round of 32\n\nAt first, this sounded straightforward.\n\nRank the third-placed teams, take the best 8, then put them into the knockout bracket.\n\nBut the last step is where it gets weird.\n\n##  Ranking third-placed teams is the easy part\n\nOnce every group has a table, each group gives you one third-placed team.\n\nThat gives you 12 third-placed teams.\n\nFrom there, the basic ranking can be represented as a normal sorting problem:\n\n```\ntype GroupId = | \" A \" | \" B \" | \" C \" | \" D \" | \" E \" | \" F \" | \" G \" | \" H \" | \" I \" | \" J \" | \" K \" | \" L \" ; type TeamStanding = { teamId : string ; group : GroupId ; position : number ; points : number ; goalDifference : number ; goalsFor : number ; fairPlayPoints : number ; };\n```\n\nA simplified ranking function might look like this:\n\n```\nfunction rankThirdPlacedTeams ( teams : TeamStanding []) { return [... teams ]. sort (( a , b ) => b . points - a . points || b . goalDifference - a . goalDifference || b . goalsFor - a . goalsFor || a ."
      ]
    },
    {
      "url": "https://snapbracket.com/guides/world-cup-2026-best-third-place-rules",
      "title": "World Cup 2026 Best Third-Place Teams Rules Explained",
      "publish_date": null,
      "excerpts": [
        "* the tournament has 12 groups but only eight third-place qualifiers;\n* teams from the same group should not meet again immediately in the Round of 32.\n\nThe eight third-place teams are assigned to matches against specific group\nwinners. The relevant group-winner slots are:\n\n|Round of 32 slot |Opponent type |\n| --- | --- |\n|Winner Group A |Third-place team |\n|Winner Group B |Third-place team |\n|Winner Group D |Third-place team |\n|Winner Group E |Third-place team |\n|Winner Group G |Third-place team |\n|Winner Group I |Third-place team |\n|Winner Group K |Third-place team |\n|Winner Group L |Third-place team |\n\nThe exact third-place opponent for each of those group winners depends on the\ncombination of qualifying third-place groups.\n\n## Why there are 495 possible combinations\n\nThere are 12 third-place teams and eight qualification spots. The possible sets\nof eight groups are calculated as \"choose 8 from 12\", which equals **495** .\nFIFA's Annex C table lists those 495 combinations and the corresponding Round\nof 32 placements. In practical terms, this means:\n\n* if groups A, B, C, D, E, F, G, and H produce the eight best third-place teams,\n  the bracket follows one mapping;\n* if one of those groups is replaced by I, J, K, or L, the mapping may change;\n* two predictions with the same group winners can still produce different\n  knockout paths if the best third-place teams are different.\n\nThat is the main reason the 2026 World Cup bracket is harder to predict than\nthe older 32-team format.\n\n## Common mistakes\n\n### Mistake 1: confusing this with the third-place match\n\n\"Best third-place teams\" refers to teams finishing third in their groups. It is\nnot the same as the third-place match played after the semi-finals.\n\n### Mistake 2: assuming every third-place team advances\n\nOnly eight of the 12 third-place teams qualify. Four third-place teams are\neliminated after the group stage.\n### Mistake 3: ranking the eight teams into bracket seeds\n\nThe best third-place table decides which teams advance. It does not seed those\nteams from best to worst into the bracket. Once the eight groups are known,\nplacement follows the pre-set Annex C mapping.\n\n### Mistake 4: using a fixed 32-team bracket too early\n\nA fixed knockout bracket is not enough for World Cup 2026 predictions unless\nthe third-place combination has already been selected.\n\n## How to make a prediction\n\nFor a pool, classroom activity, office contest, or printable bracket, use this\nworkflow:\n\n1. Rank all 12 groups from first to fourth.\n2. Take the third-place team from each group.\n3. Choose the eight third-place teams you expect to qualify.\n4. Apply the official third-place mapping.\n5. Pick winners through the Round of 32, Round of 16, quarter-finals,\n   semi-finals, and final.\n\nThe World Cup 2026 Bracket Predictor does this automatically after you rank the groups and select the eight\nthird-place teams."
      ]
    },
    {
      "url": "https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_knockout_stage",
      "title": "2026 FIFA World Cup knockout stage - Wikipedia",
      "publish_date": null,
      "excerpts": [
        "The knockout stage of the 2026 FIFA World Cup will be the second and final stage of the competition, following the group stage . Played from June 28 to July 19, 2026, the knockout stage will end with the final , to be held at MetLife Stadium in East Rutherford , New Jersey . [[ 1 ]]() The top two teams from each of the twelve groups, along with the best eight third-placed teams , will advance to the knockout stage to compete in a single-elimination tournament . There will be 32 matches in the knockout stage, including a match for third place. [[ 2 ]]()\n\n## Format\n\nThe knockout stage of the 2026 FIFA World Cup will be contested between 32 teams that qualify from the group stage. Matches in the knockout stage will be played to a finish. If the score of a match is level at the end of 90 minutes of playing time, 30 minutes of extra time\") will be played. If the scores were still tied, the match will be decided by a penalty shootout\") . [[ 2 ]]() All times listed are local. [[ 1 ]]()\n\n...\n\n**^** [\"W85 vs W87 | Round of 16 | FIFA World Cup 2026\"](https://www.fifa.com/en/match-centre/match/17/285023/289288/400021535) . FIFA. Retrieved May 1, 2026.\n25. **^** [\"W89 vs W90 | Quarter-final | FIFA World Cup 2026\"](https://www.fifa.com/en/match-centre/match/17/285023/289289/400021536) . FIFA. Retrieved May 1, 2026.\n26. **^** [\"W93 vs W94 | Quarter-final | FIFA World Cup 2026\"](https://www.fifa.com/en/match-centre/match/17/285023/289289/400021538) . FIFA. Retrieved May 1, 2026.\n27. **^** [\"W91 vs W92 | Quarter-final | FIFA World Cup 2026\"](https://www.fifa.com/en/match-centre/match/17/285023/289289/400021539) . FIFA. Retrieved May 1, 2026.\n28. **^** [\"W95 vs W96 | Quarter-final | FIFA World Cup 2026\"](https://www.fifa.com/en/match-centre/match/17/285023/289289/400021537) . FIFA. Retrieved May 1, 2026.\n29. **^** [\"W97 vs W98 | Semi-final | FIFA World Cup 2026\"](https://www.fifa.com/en/match-centre/match/17/285023/289290/400021541) . FIFA. Retrieved May 1, 2026.\n30.\n**^** [\"W99 vs W100 | Semi-final | FIFA World Cup 2026\"](https://www.fifa.com/en/match-centre/match/17/285023/289290/400021540) . FIFA. Retrieved May 1, 2026.\n31. **^** [\"RU101 vs RU102 | Play-off for third place | FIFA World Cup 2026\"](https://www.fifa.com/en/match-centre/match/17/285023/289291/400021542) . FIFA. Retrieved May 1, 2026.\n32. **^** [\"W101 vs W102 | Final | FIFA World Cup 2026\"](https://www.fifa.com/en/match-centre/match/17/285023/289292/400021543) . FIFA. Retrieved May 1, 2026.\n\n## External links\n\n* [Official website](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026)"
      ]
    },
    {
      "url": "https://www.footbracket.com/simulator",
      "title": "2026 World Cup Bracket Simulator — Annex C Round of 32 ...",
      "publish_date": null,
      "excerpts": [
        "World Cup 2026 Bracket Predictor\n\nBuild Bracket Groups Simulator Venues Odds Save Bracket \n\nHome / Simulator\n\n# Round of 32 Simulator\n\nThe 2026 World Cup uses **Annex C** — 495 possible bracket combinations based on which 8 groups produce qualifying third-place teams. Your bracket on the Bracket page auto-calculates this from your group stage scores.\n\n## Current Group Leaders (from your bracket)\n\nA ❓ TBD\n\nB ❓ TBD\n\nC ❓ TBD\n\nD ❓ TBD\n\nE ❓ TBD\n\nF ❓ TBD\n\nG ❓ TBD\n\nH ❓ TBD\n\nI ❓ TBD\n\nJ ❓ TBD\n\nK ❓ TBD\n\nL ❓ TBD\n\n## Round of 32 Matchups (Annex C resolved)\n\nRank all groups and pick 8 third-place teams on the Bracket page to see your Round of 32.\n\nSitemap All Groups Venues Predictions"
      ]
    },
    {
      "url": "https://en.wikipedia.org/wiki/Template%3A2026_FIFA_World_Cup_third-place_table",
      "title": "Template:2026 FIFA World Cup third-place table - Wikipedia",
      "publish_date": null,
      "excerpts": [
        "|No. |Third-placed teams  \nadvance from groups\n\n* v\n* t\n* e | |1A  \nvs |1B  \nvs |1D  \nvs |1E  \nvs |1G  \nvs |1I  \nvs |1K  \nvs |1L  \nvs |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n|1 | | | | |**E** |**F** |**G** |**H** |**I** |**J** |**K** |**L** | |3E |3J |3I |3F |3H |3G |3L |3K |\n|2 | | | |**D** | |**F** |**G** |**H** |**I** |**J** |**K** |**L** |3H |3G |3I |3D |3J |3F |3L |3K |\n|3 | | | |**D** |**E** | |**G** |**H** |**I** |**J** |**K** |**L** |3E |3J |3I |3D |3H |3G |3L |3K |\n|4 | | | |**D** |**E** |**F** | |**H** |**I** |**J** |**K** |**L** |3E |3J |3I |3D |3H |3F |3L |3K |\n|5 | | | |**D** |**E** |**F** |**G** | |**I** |**J** |**K** |**L** |3E |3G |3I |3D |3J |3F |3L |3K |\n|6 | | | |**D** |**E** |**F** |**G** |**H** | |**J** |**K** |**L** |3E |3G |3J |3D |3H |3F |3L |3K |\n|7 | | | |**D** |**E** |**F** |**G** |**H** |**I** | |**K** |**L** |3E |3G |3I |3D |3H |3F |3L |3K |\n|8 | | | |**D** |**E** |**F** |**G** |**H** |**I** |**J** | |**L** |3E |3G |3J |3D |3H |3F |3L |3I |\n|9 | | | |**D** |**E** |**F** |**G** |**H** |**I** |**J** |**K** | |3E |3G |3J |3D |3H |3F |3I |3K |\n|10 | | |**C** | | |**F** |**G** |**H** |**I** |**J** |**K** |**L** |3H |3G |3I |3C |3J |3F |3L |3K |\n|11 | | |**C** | |**E** | |**G** |**H** |**I** |**J** |**K** |**L** |3E |3J |3I |3C |3H |3G |3L |3K |\n|12 | | |**C** | |**E** |**F** | |**H** |**I** |**J** |**K** |**L** |3E |3J |3I |3C |3H |3F |3L |3K |\n|13 | | |**C** | |**E** |**F** |**G** | |**I** |**J** |**K** |**L** |3E |3G |3I |3C |3J |3F |3L |3K |\n|14 | | |**C** | |**E** |**F** |**G** |**H** | |**J** |**K** |**L** |3E |3G |3J |3C |3H |3F |3L |3K |\n|15 | | |**C** | |**E** |**F** |**G** |**H** |**I** | |**K** |**L** |3E |3G |3I |3C |3H |3F |3L |3K |\n|16 | | |**C** | |**E** |**F** |**G** |**H** |**I** |**J** | |**L** |3E |3G |3J |3C |3H |3F |3L |3I |\n|17 | | |**C** | |**E** |**F** |**G** |**H** |**I** |**J** |**K** | |3E |3G |3J |3C |3H |3F |3I |3K |\n|18 | | |**C** |**D** | | |**G** |**H** |**I** |**J** |**K** |**L** |3H |3G |3I |3C |3J |3D |3L |3K |\n|19 | | |**C** |**D** | |**F** | |**H** |**I** |**J** |**K** |**L** |3C |3J |3I |3D |3H |3F |3L |3K |\n|20 | | |**C** |**D** | |**F** |**G** | |**I** |**J** |**K** |**L** |3C |3G |3I |3D |3J |3F |3L |3K |\n|21 | | |**C** |**D** | |**F** |**G** |**H** | |**J** |**K** |**L** |3C |3G |3J |3D |3H |3F |3L |3K |\n|22 | | |**C** |**D** | |**F** |**G** |**H** |**I** | |**K** |**L** |3C |3G |3I |3D |3H |3F |3L |3K |\n|23 | | |**C** |**D** | |**F** |**G** |**H** |**I** |**J** | |**L** |3C |3G |3J |3D |3H |3F |3L |3I |\n|24 | | |**C** |**D** | |**F** |**G** |**H** |**I** |**J** |**K** | |3C |3G |3J |3D |3H |3F |3I |3K |\n|25 | | |**C** |**D** |**E** | | |**H** |**I** |**J** |**K** |**L** |3E |3J |3I |3C |3H |3D |3L |3K |\n\n...\n\n|494 |**A** |**B** |**C** |**D** |**E** |**F** |**G** | |**I** | | | |3C |3G |3B |3D |3A |3F |3E |3I |\n|495 |**A** |**B** |**C** |**D** |**E** |**F** |**G** |**H** | | | | |3H |3G |3B |3C |3A |3F |3D |3E |"
      ]
    },
    {
      "url": "https://www.thefamilytravelguy.com/blog/2026-fifa-world-cup-bracket-predictor",
      "title": "2026 FIFA World Cup Bracket Predictor: Explore All 495 Third ...",
      "publish_date": "2026-05-19",
      "excerpts": [
        "0\n\n# 2026 FIFA World Cup Bracket Predictor: Explore All 495 Third-Place Group Scenarios\n\nSports Travel\n\nMay 19\n\nWritten By Randy\n\nThe 2026 FIFA World Cup will be the biggest tournament in history, featuring 48 teams, 104 matches, and a brand-new Round of 32 format. With eight third-place teams advancing from the group stage, there are 495 possible combinations that can dramatically change the knockout bracket.\n\nTo help soccer fans plan ahead, I created this interactive 2026 FIFA World Cup Bracket Predictor. You can rank every team in all 12 groups, select the eight best third-place finishers, build your complete knockout bracket, and see where each team could play throughout the tournament.\n\nWhether you're following your favorite national team, comparing possible matchups, or planning a trip to cities like Los Angeles, Miami, Dallas, Atlanta, Kansas City, and the San Francisco Bay Area, this tool makes it easy to visualize every possible path to the final.\n_Note:_ [_Check out the official 2026 FIFA World Cup Regulations here that explain the 495 possible 3rd place group combinations_](https://digitalhub.fifa.com/m/636f5c9c6f29771f/original/FWC2026_regulations_EN.pdf) _(starting on Page 80, Annex C)_\n\n2026 World Cup Bracket Predictor\n\n🏆 2026 World Cup Interactive Bracket Predictor\n\n# Rank all 48 teams. Test all 495 paths. Predict the champion.\n\nBuild your own 2026 FIFA World Cup bracket, see how third-place scenarios change the Round of 32, and map where teams could play across North America.\n\nStart With Group Picks\n\nYour Projected Champion\n\n## Not picked yet\n\n**48** Teams\n\n**0/8** 3rd Place\n\n**495** Scenarios\n\n↻ Reset Bracket\n\nGroups 3rd Place 495 Scenarios Bracket Trip Path\n\n## Group A\n\n**1\\. 🇲🇽 Mexico**\n\nAuto advances\n\n↑ ↓\n\n**2\\. 🇿🇦 South Africa**\n\nAuto advances\n\n↑ ↓\n\n**3\\. 🇰🇷 South Korea**\n\nPossible 3rd-place qualifier\n\n↑ ↓\n\n**4\\. 🇨🇿 Czechia**\n\nEliminated\n\n↑ ↓\n\n## Group B\n\n**1\\. 🇨🇦 Canada**\n\nAuto advances\n\n↑ ↓\n\n**2\\. 🇧🇦 Bosnia and Herzegovina**\n\nAuto advances\n\n↑ ↓\n\n**3\\.\n🇶🇦 Qatar**\n\nPossible 3rd-place qualifier\n\n↑ ↓\n\n**4\\. 🇨🇭 Switzerland**\n\nEliminated\n\n↑ ↓\n\n## Group C\n\n**1\\. 🇧🇷 Brazil**\n\nAuto advances\n\n↑ ↓\n\n**2\\. 🇲🇦 Morocco**\n\nAuto advances\n\n↑ ↓\n\n**3\\. 🇭🇹 Haiti**\n\nPossible 3rd-place qualifier\n\n↑ ↓\n\n**4\\. 🏴 Scotland**\n\nEliminated\n\n↑ ↓\n\n## Group D\n\n**1\\. 🇺🇸 United States**\n\nAuto advances\n\n↑ ↓\n\n**2\\. 🇵🇾 Paraguay**\n\nAuto advances\n\n↑ ↓\n\n**3\\. 🇦🇺 Australia**\n\nPossible 3rd-place qualifier\n\n↑ ↓\n\n**4\\. 🇹🇷 Türkiye**\n\nEliminated\n\n↑ ↓\n\n## Group E\n\n**1\\. 🇩🇪 Germany**\n\nAuto advances\n\n↑ ↓\n\n**2\\. 🇨🇼 Curaçao**\n\nAuto advances\n\n↑ ↓\n\n**3\\. 🇨🇮 Côte d’Ivoire**\n\nPossible 3rd-place qualifier\n\n↑ ↓\n\n**4\\. 🇪🇨 Ecuador**\n\nEliminated\n\n↑ ↓\n\n## Group F\n\n**1\\. 🇳🇱 Netherlands**\n\nAuto advances\n\n↑ ↓\n\n**2\\. 🇯🇵 Japan**\n\nAuto advances\n\n↑ ↓\n\n**3\\. 🇸🇪 Sweden**\n\nPossible 3rd-place qualifier\n\n↑ ↓\n\n**4\\. 🇹🇳 Tunisia**\n\nEliminated\n\n↑ ↓\n\n## Group G\n\n**1\\. 🇧🇪 Belgium**\n\nAuto advances\n\n↑ ↓\n\n**2\\. 🇪🇬 Egypt**"
      ]
    },
    {
      "url": "https://www.sportingnews.com/us/soccer/news/world-cup-bracket-seeds-groups-format-2026-fifa-explained/f43731b452a7f92bccf783c0",
      "title": "World Cup bracket, explained: How seeds, groups, format will ...",
      "publish_date": null,
      "excerpts": [
        "### How third place qualifiers work\n\nAll 12 third-place finishers are sorted into a table just like the groups based on their points gained in group stage play and other metrics such as goal differential.\n\nThe top eight teams in this table will advance to the knockout round.\n\n### Knockout stage seeding\n\nThe entirety of the knockout stage bracket is predetermined. For example, the winner of Group F will face the runner-up from Group C, while the winner of Group J will face the runner-up from Group H.\n\nAll group winners are paired against either a runner-up from another group, or a third-place finisher from another group. All group winners and runners-up from the same group are placed on opposite sides of the bracket to avoid rematches until the finals.\n\nThe only unknowns at the start of the tournament are where each potential third-place finisher will end up. Until all qualifiers are known, it is impossible to predict where or when they could potentially play should this come to pass.\nThere are 495 mathematical combinations of third place qualifiers from various groups. All of these have been spelled out in advance, and every potential outcome can be found in Annex C (pg. 80) of the [2026 FIFA World Cup regulations](https://digitalhub.fifa.com/m/636f5c9c6f29771f/original/FWC2026_regulations_EN.pdf) . Whichever combination comes to pass will determine where each third-place finisher falls in the overall bracket.\n\n## How the FIFA World Cup draw works\n\nThe 2026 FIFA World Cup draw was conducted in four stages to set the matchups for the tournament.\n\nEach team was written on a slip of paper, placed inside a plastic ball and put in a pot numbered 1–4 based on that team’s FIFA ranking. Draw participants then selected one ball from each pot to fill out the four-team groups.\n\nA computer then allocated each team to its appropriate group based on the geographical restrictions in place for the event.\nIt found the first available group that does not present a restriction for the nation in question.\n\nAt the conclusion of the World Cup draw, all teams know not only their group-stage opponents but also where their potential path through the knockout bracket will fall should they finish first or second in their group and qualify for the next phase.\n\n**MORE:** [How does the FIFA World Cup draw work?](https://www.sportingnews.com/us/soccer/news/how-fifa-world-cup-draw-works-format-rules-pots-groups/39a9cb5b96536ad4e506efb1)\n\n### Top four teams in world rankings seeded\n\nThere is a new, additional constraint involving the top-ranked teams in Pot 1 for the 2026 draft, which [FIFA announced](https://inside.fifa.com/organisation/media-releases/procedures-final-draw-world-cup-2026-revealed) on Tuesday, November 25.\n\nIn order to achieve competitive balance in the knockout stage, FIFA restricted teams ranked No. 1 (Spain) and No. 4 (England) into half the groups, and teams ranked No."
      ]
    },
    {
      "url": "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/final-draw-results",
      "title": "Final Draw results | FIFA World Cup 2026",
      "publish_date": null,
      "excerpts": [
        "Text Color White Black Red Green Blue Yellow Magenta Cyan Transparency Opaque Semi-Transparent Background Color Black White Red Green Blue Yellow Magenta Cyan Transparency Opaque Semi-Transparent Transparent Window Color Black White Red Green Blue Yellow Magenta Cyan Transparency Transparent Semi-Transparent Opaque\n\nFont Size 50% 75% 100% 125% 150% 175% 200% 300% 400%\n\nText Edge Style None Raised Depressed Uniform Dropshadow\n\nFont Family Proportional Sans-Serif Monospace Sans-Serif Proportional Serif Monospace Serif Casual Script Small Caps\n\nDefaults Done\n\n* [Powered by THEOplayer 2023.3.0](https://www.theoplayer.com/player-referral)\n\nMatch schedule explainer Match schedule explainer\n\nFind out how the FIFA World Cup 2026 match schedule will take shape. Find out how the FIFA World Cup 2026 match schedule will take shape.\n\nClose Related Content\n\nClose Share\n\nSix of the 48 teams at FIFA World Cup 2026 have yet to be determined, and will only be known in March 2026.\nFour will come from the 16-team UEFA play-offs, which will be contested by Albania, Bosnia and Herzegovina, Czechia, Denmark, Italy, Kosovo, Northern Ireland, North Macedonia, Poland, Republic of Ireland, Romania, Slovakia, Sweden, Türkiye, Ukraine and Wales.\n\nThe other two spots will be contested by [six teams](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/play-off-tournament-teams-confirmed) \\- Bolivia, Congo DR, Iraq, Jamaica, New Caledonia and Suriname - at the [FIFA World Cup 2026™ Play-Off Tournament](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/play-off-tournament-teams-qualifying-dates-tickets-matches-format) .\n\n* * *\n\n### [**FIFA World Cup 26 tickets**](https://www.fifa.com/en/tickets) [**FIFA World Cup 26 tickets**](https://www.fifa.com/en/tickets)\n\n### [**FIFA World Cup 26 host countries and cities**](https://www.fifa.\ncom/en/tournaments/mens/worldcup/canadamexicousa2026/host-cities) [**FIFA World Cup 26 host countries and cities**](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/host-cities)\n\nPlay Video\n\nLearn more\n\nRelated content Related content Share Video Share Video\n\nPlaying on\n\nSubtitles\n\n* English\n\nSettings\n\n* Quality Automatic Automatic HD\n* Speed Normal\n* Subtitle Options\n\nQuality\n\n* Automatic\n\nSpeed\n\n* 0\\.25\n* 0\\.5\n* Normal\n* 1\\.25\n* 1\\.5\n* 2\n\nSubtitle Options\n\n* Font family Default\n* Font color Default\n* Font opacity Default\n* Font size Default\n* Background color Default\n* Background opacity Default\n* Window color Default\n* Window opacity Default\n* Character edge style Default\n\nFont family\n\n* Default\n* Monospaced Serif\n* Proportional Serif\n* Monospaced Sans-Serif\n* Proportional Sans-Serif\n\nFont color\n\n* Default\n* White\n* Yellow\n* Green\n* Cyan\n* Blue\n* Magenta\n* Red\n* Black\n\nFont opacity\n\n* Default\n* 25%\n* 50%\n* 75%\n* 100%\n\nFont size\n\n* Default\n* 50%\n* 75%\n* 100%"
      ]
    }
  ],
  "warnings": null,
  "usage": [
    {
      "name": "sku_search",
      "count": 1
    }
  ],
  "session_id": "ses_105f1b0b0ffevbjgqjCjei3gcF"
}
```

---

## Assistant (Plan · Nemotron 3 Ultra Free · 45.6s)

_Thinking:_

Now I have a good understanding. Let me also check the Wikipedia template for the full 495 combinations table, and the FIFA regulations PDF for Annex C.

**Tool: websearch**

**Input:**
```json
{
  "query": "site:digitalhub.fifa.com FWC2026_regulations_EN.pdf Annex C third place"
}
```

**Output:**
```
{
  "search_id": "search_3e4792975648421fba42378c56d775d8",
  "results": [
    {
      "url": "https://www.reddit.com/r/worldcup/comments/1l4qzav/fifa_world_cup_2026_regulations_published",
      "title": "FIFA World Cup 2026 Regulations published - includes all 495 third ...",
      "publish_date": null,
      "excerpts": [
        "Skip to main content Open menu Open navigation  Go to Reddit Home\n\nr/worldcup\n\nExpand user menu Open settings menu\n\nGo to worldcup r/worldcup\n\nr/worldcup <https://discord.gg/football>\n\nAll Things 2026 FIFA World Cup and Beyond: Match Threads, News, Discussions and More!\n\n* * *\n\nWeekly visitors Weekly contributions •\n\nAvailable\\_Attempt\\_32\n\n# FIFA World Cup 2026 Regulations published - includes all 495 third placed teams \"options\"\n\n💬Discussion Following on from this discussion: [https://www.reddit.com/r/worldcup/comments/1dnm5sw/2026\\_fifa\\_world\\_cup\\_schedule\\_update\\_cont\\_from/](https://www.reddit.com/r/worldcup/comments/1dnm5sw/2026_fifa_world_cup_schedule_update_cont_from/) FIFA has published 2026 regs here- [https://digitalhub.fifa.com/m/636f5c9c6f29771f/original/FWC2026\\_regulations\\_EN.pdf](https://digitalhub.fifa.com/m/636f5c9c6f29771f/original/FWC2026_regulations_EN.\npdf) \\- u/kevit80 u/TrevorBatson this includes a lengthy (18 page) annex C setting out the 495 options for third placed teams opponents in the Round of 32. There is no summary of in how many of the 495 options, each match combination occurs (unless someone can work out how to automate such an analysis!), though we do know that each of 1K v 3L and 1L v 3K will occur in 330 of the 495 options, ie in any scenario where 3K and/or 3L qualifies as one of the best 8 third placed teams\n\nArchived post. New comments cannot be posted and votes cannot be cast.\n\nShare\n\n# Related Answers Section\n\nRelated Answers\n\n[New rules for the World Cup](https://www.reddit.com/answers/757a6f9b-a0f9-4cbd-b75d-f78ee9c98ce1/?q=New+rules+for+the+World+Cup&source=PDP)\n\n[World Cup group predictions](https://www.reddit.com/answers/addc01b7-2e76-4b19-8c8c-d2b73aeb264f/?q=World+Cup+group+predictions&source=PDP)\n\n[World Cup knockout stage explained](https://www.reddit.com/answers/a300bd96-7448-4c01-9ff5-a1eee4cd7702/?\nq=World+Cup+knockout+stage+explained&source=PDP)\n\n[How the World Cup works](https://www.reddit.com/answers/7b208103-0edb-4739-9f68-53308f7e6bad/?q=How+the+World+Cup+works&source=PDP)\n\n[Top underdog teams to watch in 2026](https://www.reddit.com/answers/00a6e2e1-9673-409a-9ff5-dc0d643b40f3/?q=Top+underdog+teams+to+watch+in+2026&source=PDP)\n\n<https://discord.gg/football>\n\nPublic\n\nAnyone can view, post, and comment to this community\n\n0 0\n\n## Top Posts\n\n* * *\n\n* [Reddit reReddit: Top posts of June 6, 2025 * * *](https://www.reddit.com/posts/2025/june-6-1/global/)\n* [Reddit reReddit: Top posts of June 2025 * * *](https://www.reddit.com/posts/2025/june/global/)\n* [Reddit reReddit: Top posts of 2025 * * *](https://www.reddit.com/posts/2025/global/)\n\nExpand Navigation Collapse Navigation"
      ]
    },
    {
      "url": "https://snapbracket.com/guides/world-cup-2026-best-third-place-rules",
      "title": "World Cup 2026 Best Third-Place Teams Rules Explained",
      "publish_date": null,
      "excerpts": [
        "World Cup 2026 Best Third-Place Teams Rules Explained\nHow the World Cup 2026 best third-place teams qualify: ranking rules, tie-breakers, Annex C mapping, and why third-place teams change the bracket."
      ]
    },
    {
      "url": "https://digitalhub.fifa.com/m/636f5c9c6f29771f/original/FWC2026_regulations_EN.pdf",
      "title": "Regulations for the FIFA World Cup 26 FIFA https://digitalhub.fifa.com › FWC2026_regulations_EN",
      "publish_date": null,
      "excerpts": [
        "Regulations for the FIFA World Cup 26"
      ]
    },
    {
      "url": "https://github.com/m7mdehab/WC2026-Live-Prediction-Engine/blob/main/data/third_place_matrix_2026.README.md",
      "title": "Third-Place Matrix (Annex C) — Deferred Extraction",
      "publish_date": null,
      "excerpts": [
        "Third-Place Matrix (Annex C) — Deferred Extraction\nThe 2026 World Cup uses a 495-row matrix (FIFA Regulations Annex C) that maps each of the 495 possible \"which 8 of 12 third-placed groups qualify\" combinations to specific R32 matchups. Manually transcribing 495 rows in this chat session would burn budget for no benefit — it is a mechanical"
      ]
    },
    {
      "url": "https://cdn.thuvienphapluat.vn/phap-luat/2022-2/TTKP/FWC26-regulations.pdf",
      "title": "[PDF] Regulations for the FIFA World Cup 26™",
      "publish_date": null,
      "excerpts": [
        "Winner F (1F)\n\nv.\n\nRunner‑up C (2C)\n\n= Winner (3) M75 (W75)\n\n(4) M76\n\nWinner C (1C)\n\nv.\n\nRunner‑up F (2F)\n\n= Winner (4) M76 (W76)\n\n(5) M77\n\nWinner I (1I)\n\nv.\n\nBest 3 rd place of\n\nCDFGH\n\n= Winner (5) M77 (W77)\n\n(6) M78\n\nRunner‑up E (2E)\n\nv.\n\nRunner‑up I (2I)\n\n= Winner (6) M78 (W78)\n\n(7) M79\n\nWinner A (1A)\n\nv.\n\nBest 3 rd place of\n\nCEFHI\n\n= Winner (7) M79 (W79)\n\n(8) M80\n\nWinner L (1L)\n\nv.\n\nBest 3 rd place of\n\nEHIJK\n\n= Winner (8) M80 (W80)\n\n(9) M81\n\nWinner D (1D)\n\nv.\n\nBest 3 rd place of\n\nBEFIJ\n\n= Winner (9) M81 (W81)\n\n(10) M82\n\nWinner G (1G)\n\nv.\n\nBest 3 rd place of\n\nAEHIJ\n\n= Winner (10) M82 (W82)\n\n(11) M83\n\nRunner‑up K (2K)\n\nv.\n\nRunner‑up L (2L)\n\n= Winner (11) M83 (W83)\n\n(12) M84\n\nWinner H (1H)\n\nv.\n\nRunner‑up J (2J)\n\n= Winner (12) M84 (W84)\n\n(13) M85\n\nWinner B (1B)\n\nv.\n\nBest 3 rd place of\n\nEFGIJ\n\n= Winner (13) M85 (W85)\n\n(14) M86\n\nWinner J (1J)\n\nv.\n\nRunner‑up H (2H)\n\n= Winner (14) M86 (W86)\n\n(15) M87\n\nWinner K (1K)\n\nv.\n\nBest 3 rd place of\n\nDEIJL\n\n= Winner (15) M87 (W87)\n(16) M88\n\nRunner‑up D (2D)\n\nv.\n\nRunner‑up G (2G)\n\n= Winner (16) M88 (W88)\n\nNote: the above configuration of matches for the round of 32 does not\n\nnecessarily represent the chronological order in which the matches will be\n\nplayed as teams from the same group shall not meet each other in the round\n\nof 32.\n\nCompetition format\n\nIII .\n\n24\n\n25\n\nAnnexe C of these Regulations includes the 495 different possible combinations\n\nof the eight best‑ranked third‑placed teams and their next match‑up for the\n\nround of 32, at the completion of the group stage.\n\n12\\.7 The 16 teams that qualify from the round of 32 will contest the round of 16\n\nas follows:\n\n**Match no.**\n\n**Team A**\n\n**v.**\n\n**Team B**\n\n**Winner**\n\n(17) M89\n\n(2) Winner M74\n\n(W74)\n\nv.\n\n(5) Winner M77\n\n(W77)\n\n= Winner (17) M89 (W89)\n\n(18) M90\n\n(1) Winner M73\n\n(W73)\n\nv.\n\n(3) Winner M75\n\n(W75)\n\n= Winner (18) M90 (W90)\n\n(19) M91\n\n(4) Winner M76\n\n(W76)\n\nv.\n\n(6) Winner M78\n\n(W78)\n\n= Winner (19) M91 (W91)\n\n(20) M92\n\n(7) Winner M79\n\n(W79)\n\nv.\n(8) Winner M80\n\n(W80)\n\n= Winner (20) M92 (W92)\n\n(21) M93\n\n(11) Winner M83\n\n(W83)\n\nv.\n\n(12) Winner M84\n\n(W84)\n\n= Winner (21) M93 (W93)\n\n(22) M94\n\n(9) Winner M81\n\n(W81)\n\nv.\n\n(10) Winner M82\n\n(W82)\n\n= Winner (22) M94 (W94)\n\n(23) M95\n\n(14) Winner M86\n\n(W86)\n\nv.\n\n(16) Winner M88\n\n(W88)\n\n= Winner (23) M95 (W95)\n\n(24) M96\n\n(13) Winner M85\n\n(W85)\n\nv.\n\n(15) Winner M87\n\n(W87)\n\n= Winner (24) M96 (W96)\n\nNote: the above configuration does not necessarily represent the chronological\n\norder in which the matches will be played.\n\n12\\.8 The eight teams that qualify from the round of 16 will contest the quarter‑finals\n\nas follows:\n\n**Match no.**\n\n**Team A**\n\n**v.**\n\n**Team B**\n\n**Winner**\n\n(A) M97\n\n(17) Winner M89\n\nv.\n\n(18) Winner M90\n\n= Winner (A) M97 (W97)\n\n(B) M98\n\n(21) Winner M93\n\nv.\n\n(22) Winner M94\n\n= Winner (B) M98 (W98)\n\n(C) M99\n\n(19) Winner M91\n\nv.\n\n(20) Winner M92\n\n= Winner (C) M99 (W99)\n\n(D) M100\n\n(23) Winner M95\n\nv.\n\n(24) Winner M96\n\n= Winner (D) M100 (W100)\nNote: the above configuration does not necessarily represent the chronological\n\norder in which the matches will be played.\n\n12\\.9 The four winners of the quarter‑finals will contest the semi‑finals as follows:\n\n**Match no.**\n\n**Team A**\n\n**v.**\n\n**Team B**\n\n**Winner**\n\n(SF1) M101\n\n(A) Winner M97\n\nv.\n\n(B) Winner M98\n\n= Winner SF1 (W101)\n\n(SF2) M102\n\n(C) Winner M99\n\nv.\n\n(D) Winner M100\n\n= Winner SF2 (W102)\n\nNote: the above configuration does not necessarily represent the chronological\n\norder in which the matches will be played.\n\n12\\.10 The two runners‑up of the semi‑finals will contest the play‑off for third place,\n\nas follows:\n\n**Match no.**\n\n**Team A**\n\n**v.**\n\n**Team B**\n\n**Winner**\n\nM103\n\nRunner‑up SF1\n\n(M101)\n\nv.\n\nRunner‑up SF2\n\n(M102)\n\n= Winner M103\n\nWinner of\n\nplay‑off for third place\n\n12\\.11 The two winners of the semi‑finals will contest the final, as follows:\n\n**Match no.**\n\n**Team A**\n\n**v.**\n\n**Team B**\n\n**Winner**\n\nM104\n\n(Final)\n\nWinner SF1 (W101)\n\nv.\n\n...\n\ncriterion, the remaining two or three teams will be ranked pursuant to the next\n\ncriterion, and so on. In any case, the second step of the ranking does not restart\n\nfor the two or three teams remaining after application of a criterion.\n\n**Step 3:**\n\nIf no decision can be made through the procedures of step 1 and 2, the following\n\nshall apply:\n\ng) the two or more teams still equal on points shall be ranked according to the\n\nmost recent published edition of the FIFA/Coca‑Cola Men’s World Ranking;\n\nh) the two or more teams still equal on points shall be ranked according to the\n\npublished edition of the FIFA/Coca‑Cola Men’s World Ranking immediately\n\npreceding the most recent published edition continually until a decision can\n\nbe made.\n\n**The eight best‑ranked teams among those finishing third (third‑placed teams**\n\n**from 1 to 8)**\n\nThe eight best teams among those ranked third will be determined as follows:\n\na) greatest number of points obtained in all group matches;\n\n...\n\ngold medals to the winners, silver medals to the runners‑up and bronze\n\nmedals to the team ranked third.\n\n45\\.9 One medal will be presented to each of the match officials who officiate at the\n\nplay‑off for third place and the final.\n\n45\\.10 A fair play contest will be held during the final competition, for which FIFA has\n\ndrawn up special regulations (cf. Annexe B). The FIFA Technical Study Group\n\nshall determine the ranking at the end of the final competition.\n\n45\\.11 At the conclusion of the FIFA World Cup 26, the following special awards will\n\nbe presented:\n\n**a) FIFA Fair Play Award presented by McDonald’s**\n\nThe FIFA Fair Play Award presented by McDonald’s is a prize presented\n\nto the Participating Member Association finishing first in the fair play\n\ncontest. FIFA will, on behalf of and in alignment with McDonald’s, deliver\n\na football‑related social development (CSR) campaign in the territory of\n\nthe winning association. The budget for this CSR campaign shall be up to"
      ]
    },
    {
      "url": "https://documents.uefa.com/r/Regulations-of-the-2025-UEFA-Women-s-Nations-League-and-2026-Women-s-European-Qualifiers-for-the-2027-FIFA-Women-s-World-Cup-2025-27/Annex-C-2025-UEFA-Women-s-Nations-League-and-2026-Women-s-European-Qualifiers-Overall-League-and-Phase-Rankings-Online",
      "title": "Annex C - 2025 UEFA Women's Nations League and 2026 ... UEFA Documents https://documents.uefa.com › Annex-C-2025-UEFA-Wo...",
      "publish_date": null,
      "excerpts": [
        "Annex C - 2025 UEFA Women's Nations League and 2026"
      ]
    },
    {
      "url": "https://www.foxsports.com/stories/soccer/fifa-world-cup-group-stage-third-place-tiebreakers",
      "title": "2026 FIFA World Cup: Group Stage Tiebreakers And How Third-Place Teams Advance | FOX Sports",
      "publish_date": "2026-06-06",
      "excerpts": [
        "my favs\n\n Access and manage your favorites here\n\nDISMISS\n\n* Scores\n* Watch\n* Betting\n* FIFA WC 26 ⚽\n* Stories\n* Search\n* \n\n* Account\n* SPORTS & TEAMS\n* PLAYERS\n* SHOWS\n* PERSONALITIES\n* TOPICS\n\nPOPULAR SEARCHES\n\n\\- No Data Available -\n\nBROWSE BY\n\nSPORTS & TEAMS\n\nPLAYERS\n\nSHOWS\n\nPERSONALITIES\n\nTOPICS\n\nBuilt on\n\nFIFA Men's World Cup\n\nFIFA Men's World Cup\n\n# 2026 FIFA World Cup: Group Stage Tiebreakers And How Third-Place Teams Advance\n\nUpdated Jun. 22, 2026 8:08 p.m. ET\n\nshare\n\nfacebook x reddit link\n\nThe [2026 FIFA World Cup](https://www.foxsports.com/soccer/fifa-world-cup) will be the biggest ever in numerous ways. It will have 48 teams playing across 16 cities in three co-host countries, all the most ever in World Cup history ( [Watch every match on FOX One](https://www.fox.com/soccer/fifa-world-cup?cmpid=org=one::ag=owned_other::mc=referral::src=fs::cmp=10010131002::add=625e) ).\nThose 48 teams are divided into 12 groups of four with each team playing its group stage opponents for a total of three first-round games per side. And while we should expect surprises and drama throughout the group-stage games, it will only be multiplied when we get to the knockout rounds with all eyes toward the final on July 19.\n\nThere are a couple of important format changes at this tournament as to see which teams will reach the knockout portion. The top two teams from each of the 12 groups – plus the top eight third-place teams across the board – will then reach the first ever Round of 32 at a World Cup. Let's dive into how it all works.\n\n## **How Did The Group Stage Work Before?**\n\nFrom 1998 to 2022, there were 32 teams per tournament. The teams were divided into groups of four, and the top two teams in each group (16 total) advanced to the knockout rounds. That created a Round of 16 with the winners then reaching the quarterfinals (eight teams).\nThe four winners then contested the semifinals and then the last two teams left played for the ultimate prize.\n\n## How Does That Work With 48 Teams?\n\nInstead of 16 teams advancing, 32 will make it out of the group stage in 2026. That means a whole new knockout round will be needed (a Round of 32), which will begin right after the completion of the group stage. So for a team to win the final, it will need to play:  \n  \n\\- 3 Group Stage Games  \n\\- 1 Round of 32 Game  \n\\- 1 Round of 16 Game  \n\\- 1 Quarterfinal Game  \n\\- 1 Semifinal Game  \n\\- 1 Final\n\nThat's a total of eight games, a change from previous World Cup tournaments where seven games were needed to reach the grand finale.\n\n## How Do Points Work? How Do Tiebreakers Work?\n\nIn a group, a team will earn three points for a win, one point for a draw, and no points for a loss. That could mean some teams are equal on points at the end of the three-game group stage. That leads us to tiebreakers.\nIf two or more teams finish equal on group-stage points, here is the order of who finishes on top:\n\n1\\. Most points obtained in the head-to-head matches played between the tied teams;  \n2\\. Superior goal difference in the head-to-head matches played between the tied teams;  \n3\\. Most goals scored in the head-to-head matches played between the tied teams;\n\nThere are even more tiebreakers if any teams remained locked after all that. From there, ties are broken by these rules:\n\n4\\. Superior goal difference in all group matches  \n5\\. Most goals scored in all group matches  \n6\\. Highest team conduct score in all group matches (taking into account yellow cards and red cards)  \n7\\. FIFA World Ranking\n\n## Third-Place Teams: Which Ones Will Advance?\n\nTo fill out the World Cup knockout bracket, the best eight third-place teams out of the possible 12 in the tournament will advance. The criteria for those teams are based on:\n\n1\\. Points  \n2\\. Goal difference  \n3\\. Goals scored  \n4\\.\nHighest team conduct score in all group matches (taking into account yellow cards and red cards)  \n5\\. FIFA World Ranking\n\n## FIFA Men's World Cup WORLD CUP RELATED STORIES\n\n[2026 World Cup Schedule: All Games, Dates, Matchups and How To Watch](https://www.foxsports.com/stories/soccer/2026-world-cup-schedule-all-games-dates-matchups-how-watch)\n\n[2026 World Cup Schedule: All Games, Dates, Matchups and How To Watch](https://www.foxsports.com/stories/soccer/2026-world-cup-schedule-all-games-dates-matchups-how-watch)\n\n[Top 100 Players In The 2026 FIFA World Cup, Ranked](https://www.foxsports.com/stories/soccer/world-cup-2026-ranking-best-100-players)\n\n[Top 100 Players In The 2026 FIFA World Cup, Ranked](https://www.foxsports.com/stories/soccer/world-cup-2026-ranking-best-100-players)\n\n[USA's 2026 FIFA World Cup Roster: The 26 Players Ready To Make History](https://www.foxsports.com/stories/soccer/usmnt-world-cup-roster-2026-pulisic-mckennie-weah-adams)\n[USA's 2026 FIFA World Cup Roster: The 26 Players Ready To Make History](https://www.foxsports.com/stories/soccer/usmnt-world-cup-roster-2026-pulisic-mckennie-weah-adams)\n\nshare\n\n* * *\n\nFIFA Men's World Cup\n\nGet more from the FIFA Men's World Cup Follow your favorites to get information about games, news and more\n\n* * *\n\nin this topic\n\n[FIFA Men's World Cup FIFA Men's World Cup](https://www.foxsports.com/soccer/fifa-world-cup)\n\n[United States United States](https://www.foxsports.com/soccer/united-states-men-team)\n\n[Fox Sports facebook Fox Sports facebook](https://www.facebook.com/foxsports) [Fox Sports instagram Fox Sports instagram](https://www.instagram.com/foxsports) [Fox Sports x Fox Sports x](https://www.x.com/foxsports) [Fox Sports youtube Fox Sports youtube](https://www.youtube.com/foxsports) [Fox Sports rss Fox Sports rss](https://www.foxsports.com/rss-feeds)"
      ]
    },
    {
      "url": "https://worldcuplocaltime.com/2026-world-cup-third-place-qualification",
      "title": "2026 World Cup Third-Placed Teams Qualification Rules ... worldcuplocaltime.com https://worldcuplocaltime.com › 2...",
      "publish_date": "2026-02-24",
      "excerpts": [
        "So how exactly does FIFA decide which third-placed teams go through and which ones go home? Below you can find complete details.\n\n### 🏟️ How Many Third-Placed Teams Qualify in 2026?\n\nThe 2026 World Cup features **12 groups of four teams** . From each group:\n\n• The 12 group **winner** qualifies automatically  \n• The 12 **runner-ups** also qualify automatically  \n• That gives **24 teams** directly into the knockout stage\n\n• The third-placed team enters a special ranking table, wherein to complete the 32-team bracket for the knockout stage, FIFA selects the **8 best teams among those finishing third** .\n\nThis means four third-placed teams will be eliminated, while eight continue their World Cup journey.\n\n### 📊 Official Ranking Rules for Third-Placed Teams\n\nAll twelve third-placed teams are ranked together using official FIFA tie-breakers applied in a strict order.\n\n**The ranking criteria are:**\n\n**1\\. Points** – Teams with more points rank higher.\n\n...\n\ncom/team/czech-republic/) |[Group A](https://worldcuplocaltime.com/2026-world-cup-group-a/) |2 |0 |1 |1 |2 |3 |\\-1 |**1** |\n|10 |Ecuador flag [Ecuador](https://worldcuplocaltime.com/team/ecuador/) |[Group E](https://worldcuplocaltime.com/2026-world-cup-group-e/) |2 |0 |1 |1 |0 |1 |\\-1 |**1** |\n|11 |Bosnia flag [Bosnia](https://worldcuplocaltime.com/team/bosnia-herzegovina/) |[Group B](https://worldcuplocaltime.com/2026-world-cup-group-b/) |2 |0 |1 |1 |2 |5 |\\-3 |**1** |\n|12 |Senegal flag [Senegal](https://worldcuplocaltime.com/team/senegal/) |[Group I](https://worldcuplocaltime.com/2026-world-cup-group-i/) |2 |0 |0 |2 |3 |6 |\\-3 |**0** |\n\nQualified\n\nEliminated\n\n### 🔀 Who Will the Qualified Third-Placed Teams Play Next?\n\nQualifying as one of the **best third-placed teams** is only the beginning of the story, since the real excitement lies in discovering the opponents in the **knockout stage** . These teams, unlike group winners and runners-up, are not given a predetermined opponent.\nOn the contrary, **FIFA** uses a complex bracket system to determine the matches that depend on which groups the eight third-placed teams come from and a pre-existing matrix of **495 possible combinations** , each leading to a different **Round of 32** fixture. The fourteenth final matchups are decided only after the **group stage** is finished and new pairings are unveiled in a constantly changing puzzle. Nevertheless, the one principle that never changes is: a team **cannot play an opponent from its own group immediately again** , which guarantees variety, fairness, and a new flavour of drama when the tournament reaches the final stage.\n\n### ❓ Frequently Asked Questions – Third-Placed Team Qualification\n\n**Can a team qualify with only three points?**  \nYes. Many third-placed teams with three points and a decent goal difference will finish among the best eight.\n\n**Is four points always enough?**  \nAlmost always. A third-placed team with four points is extremely likely to qualify.\n**Can fair play really eliminate a team?**  \nYes. If points, goal difference and goals scored are tied, yellow and red cards decide who advances.\n\n**Can teams play their group rivals again in the Round of 32?**  \nNo. FIFA’s system prevents immediate rematches from the group stage.\n\nVery few new things in the history of the World Cup have had as big an impact on the drama of the group stage as the rule that allows the **top eight third-placed teams** to progress. The format is geared towards encouraging the teams to be ambitious and punishes those who get comfortable. The formula thus incentivizes attacking football, whereas discipline and tactical brains have become so much more important than before.\n\nThe **2026 FIFA World Cup** will see the margins become so microscopic that **one goal** will be able to swing the balance of power, **one yellow card** could prove to be the difference, and a referee’s decision might be talked about long after the game is over.\n\n...\n\nHer editorial work focuses on explaining how the World Cup operates — including qualification systems, competition format, stadium certification, disciplinary regulations, and tournament procedures — helping readers understand both the schedule and the structural framework behind the competition.\nAs the independent publisher of the platform, she oversees all editorial content, research, and updates to ensure accuracy, clarity, and neutrality.\nBased in New Delhi, India, she manages all editorial and publishing operations of WorldCupLocalTime.com.\n\n← [2026 FIFA World Cup Schedule in Australian Western Time (AWST)](https://worldcuplocaltime.com/2026-fifa-world-cup-schedule-australian-western-time-awst/)\n\n[2026 FIFA World Cup Schedule in British Summer Time (BST)](https://worldcuplocaltime.com/2026-fifa-world-cup-schedule-british-summer-time-bst/) →\n\n### Leave a Comment Cancel reply\n\nComment\n\nName Email Website\n\nSave my name, email, and website in this browser for the next time I comment.\nNotify me of follow-up comments by email.\n\nNotify me of new posts by email.\n\n* [About](https://worldcuplocaltime.com/about-us/)\n* [Contact](https://worldcuplocaltime.com/contact/)\n* [T&C](https://worldcuplocaltime.com/terms-and-conditions/)\n* [Privacy Policy](https://worldcuplocaltime.com/privacy-policy/)\n\nThis website is unofficial and not affiliated with, endorsed by, or sponsored by FIFA or the FIFA World Cup. All trademarks, logos, and copyrights belong to their respective owners.\n\nSearch for:\n\nspinner\n\nspinner\n\nload more\n\n*[D]: Drawn\n*[GA]: Goals Against\n*[GD]: Goal Difference\n*[GF]: Goals For\n*[L]: Lost\n*[P]: Played\n*[Pts]: Points\n*[W]: Won"
      ]
    },
    {
      "url": "https://worldcuplocaltime.com/world-cup-2026-495-scenarios-round-of-32",
      "title": "The 495 Scenarios Explained: World Cup 2026 Round of 32 Rules",
      "publish_date": null,
      "excerpts": [
        "The 495 Scenarios Explained: World Cup 2026 Round of 32 Rules\nAt the 2026 FIFA World Cup, progressing from the group stage will not be limited to just first and second place. The two best teams from each group will qualify, but they will be accompanied by 8 out of the 12 third-place finishers from the groups, which will totally change the play of the qualification. In order to avoid any luck factor in the knockout bracket, FIFA has identified 495"
      ]
    },
    {
      "url": "https://en.wikipedia.org/wiki/Template%3A2026_FIFA_World_Cup_third-place_table",
      "title": "Template:2026 FIFA World Cup third-place table Wikipedia https://en.wikipedia.org › wiki",
      "publish_date": "2026-06-19",
      "excerpts": [
        "|No. |Third-placed teams  \nadvance from groups\n\n* v\n* t\n* e | |1A  \nvs |1B  \nvs |1D  \nvs |1E  \nvs |1G  \nvs |1I  \nvs |1K  \nvs |1L  \nvs |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n|1 | | | | |**E** |**F** |**G** |**H** |**I** |**J** |**K** |**L** | |3E |3J |3I |3F |3H |3G |3L |3K |\n|2 | | | |**D** | |**F** |**G** |**H** |**I** |**J** |**K** |**L** |3H |3G |3I |3D |3J |3F |3L |3K |\n|3 | | | |**D** |**E** | |**G** |**H** |**I** |**J** |**K** |**L** |3E |3J |3I |3D |3H |3G |3L |3K |\n|4 | | | |**D** |**E** |**F** | |**H** |**I** |**J** |**K** |**L** |3E |3J |3I |3D |3H |3F |3L |3K |\n|5 | | | |**D** |**E** |**F** |**G** | |**I** |**J** |**K** |**L** |3E |3G |3I |3D |3J |3F |3L |3K |\n|6 | | | |**D** |**E** |**F** |**G** |**H** | |**J** |**K** |**L** |3E |3G |3J |3D |3H |3F |3L |3K |\n|7 | | | |**D** |**E** |**F** |**G** |**H** |**I** | |**K** |**L** |3E |3G |3I |3D |3H |3F |3L |3K |\n|8 | | | |**D** |**E** |**F** |**G** |**H** |**I** |**J** | |**L** |3E |3G |3J |3D |3H |3F |3L |3I |\n|9 | | | |**D** |**E** |**F** |**G** |**H** |**I** |**J** |**K** | |3E |3G |3J |3D |3H |3F |3I |3K |\n|10 | | |**C** | | |**F** |**G** |**H** |**I** |**J** |**K** |**L** |3H |3G |3I |3C |3J |3F |3L |3K |\n|11 | | |**C** | |**E** | |**G** |**H** |**I** |**J** |**K** |**L** |3E |3J |3I |3C |3H |3G |3L |3K |\n|12 | | |**C** | |**E** |**F** | |**H** |**I** |**J** |**K** |**L** |3E |3J |3I |3C |3H |3F |3L |3K |\n|13 | | |**C** | |**E** |**F** |**G** | |**I** |**J** |**K** |**L** |3E |3G |3I |3C |3J |3F |3L |3K |\n|14 | | |**C** | |**E** |**F** |**G** |**H** | |**J** |**K** |**L** |3E |3G |3J |3C |3H |3F |3L |3K |\n|15 | | |**C** | |**E** |**F** |**G** |**H** |**I** | |**K** |**L** |3E |3G |3I |3C |3H |3F |3L |3K |\n|16 | | |**C** | |**E** |**F** |**G** |**H** |**I** |**J** | |**L** |3E |3G |3J |3C |3H |3F |3L |3I |\n|17 | | |**C** | |**E** |**F** |**G** |**H** |**I** |**J** |**K** | |3E |3G |3J |3C |3H |3F |3I |3K |\n|18 | | |**C** |**D** | | |**G** |**H** |**I** |**J** |**K** |**L** |3H |3G |3I |3C |3J |3D |3L |3K |\n|19 | | |**C** |**D** | |**F** | |**H** |**I** |**J** |**K** |**L** |3C |3J |3I |3D |3H |3F |3L |3K |\n|20 | | |**C** |**D** | |**F** |**G** | |**I** |**J** |**K** |**L** |3C |3G |3I |3D |3J |3F |3L |3K |\n|21 | | |**C** |**D** | |**F** |**G** |**H** | |**J** |**K** |**L** |3C |3G |3J |3D |3H |3F |3L |3K |\n|22 | | |**C** |**D** | |**F** |**G** |**H** |**I** | |**K** |**L** |3C |3G |3I |3D |3H |3F |3L |3K |\n|23 | | |**C** |**D** | |**F** |**G** |**H** |**I** |**J** | |**L** |3C |3G |3J |3D |3H |3F |3L |3I |\n|24 | | |**C** |**D** | |**F** |**G** |**H** |**I** |**J** |**K** | |3C |3G |3J |3D |3H |3F |3I |3K |\n|25 | | |**C** |**D** |**E** | | |**H** |**I** |**J** |**K** |**L** |3E |3J |3I |3C |3H |3D |3L |3K |"
      ]
    }
  ],
  "warnings": null,
  "usage": [
    {
      "name": "sku_search",
      "count": 1
    }
  ],
  "session_id": "ses_105f1b0b0ffevbjgqjCjei3gcF"
}
```

---

## Assistant (Plan · Nemotron 3 Ultra Free · 51.0s)

_Thinking:_

Now I have a good understanding. Let me also look at the Wikipedia template page which seems to have the full 495 combinations table. Let me also check if there's a JSON or structured version available somewhere.

From the search results, I can see:
1. The current `mundial_2026.csv` has a simplified format with `3rd_1` vs `3rd_2`, etc. which is incorrect
2. The correct FIFA format has 16 specific Round of 32 matches with specific group winners playing against specific 3rd place team combinations
3. The Annex C table in FIFA regulations has 495 rows mapping each combination of 8 qualifying 3rd place groups to specific matchups

Let me now look at the Wikipedia template more carefully and also check the match-later.com article which had the exact mapping table.

From the match-later.com article, the 16 Round of 32 matches are:
1. 1E vs 3ABCDF
2. 1I vs 3CDFGH
3. 2A vs 2B
4. 1F vs 2C
5. 2K vs 2L
6. 1H vs 2J
7. 1D vs 3BEFIJ
8. 1G vs 3AEHIJ
9. 1C vs 2F
10. 2E vs 2I
11. 1A vs 3CEFHI
12. 1L vs 3EHIJK
13. 1J vs 2H
14. 2D vs 2G
15. 1B vs 3EFGIJ
16. 1K vs 3DEIJL

The Wikipedia template has the full 495 combinations. I need to extract this data.

Let me fetch the Wikipedia template page to get the full table.

**Tool: webfetch**

**Input:**
```json
{
  "url": "https://en.wikipedia.org/wiki/Template:2026_FIFA_World_Cup_third-place_table",
  "format": "text"
}
```

**Output:**
```
Template:2026 FIFA World Cup third-place table - Wikipedia


























Jump to content

	
		
			
				

	
	

Main menu
	
	


				
		

	
	Main menu
	move to sidebar
	hide


	

	
		Navigation
	
	
		
		
			
			Main pageContentsCurrent eventsRandom articleAbout WikipediaContact us
		
		
	


	

	
		Contribute
	
	
		
		
			
			HelpLearn to editCommunity portalRecent changesUpload fileSpecial pages
		
		
	



	
		Print/export
	
	
		
		
			
			Download as PDFPrintable version
		
		
	



	
		In other projects
	
	
		
		
			
			Wikidata item
		
		
	




				

	


		
			

	
	
		
		
	


		
		
			

	

Search
	
	
		
			
				
					
						
						
					
					
				
				Search
			
		
	


			
	
	

	
		
		
			
			
		
		
	


	

	
		
		
			
			
		
		
	


	
		

	
	

Appearance
	
	


			
				
			
		
	


	
	

	
		
		
			
			
		
		
	


	

	
		
		
			Donate

Create account

Log in


			
		
		
	


	
	

	
	

Personal tools
	
	


		

	
		
		
			

Donate



Create account



Log in


			
		
		
	


	
	




		
	


	
		
			
		
		
			
		
			
				
				
				
		
		
	

		
			
				
					Template:2026 FIFA World Cup third-place table
							

	
	

9 languages
	
	

		
			
			
				
				العربيةBahasa Indonesia日本語한국어РусскийไทยOʻzbekcha / ўзбекчаTiếng Việt中文
			
			Edit links
		

	


				
					
						
							
								

	
		
		
			
			TemplateTalk
		
		
	


								

	
	English
	
	


					

	
		
		
			
			
		
		
	


				
	


							
						
						
							
			    

	
		
		
			Read

Edit

View history


			
		
		
	


			

							
								

	
	Tools
	
	


									
						

	
	Tools
	move to sidebar
	hide


	

	
		Actions
	
	
		
		
			

Read



Edit



View history


			
		
		
	



	
		General
	
	
		
		
			
			What links hereRelated changesUpload filePermanent linkPage informationGet shortened URL
		
		
	



	
		Print/export
	
	
		
		
			
			Download as PDFPrintable version
		
		
	



	
		In other projects
	
	
		
		
			
			Wikidata item
		
		
	




									
				
	


							
						
					
				
				
					
						
						
							
				
							
		
						
							
				
	
	Appearance
	move to sidebar
	hide





							
		
					
				
				
					
							
		

						From Wikipedia, the free encyclopedia
					
					
					
					
					


Combinations of matches in the round of 32


No.

Third-placed teamsadvance from groupsvte



1Avs

1Bvs

1Dvs

1Evs

1Gvs

1Ivs

1Kvs

1Lvs


1





E
F
G
H
I
J
K
L



3E
3J
3I
3F
3H
3G
3L
3K


2




D

F
G
H
I
J
K
L
3H
3G
3I
3D
3J
3F
3L
3K


3




D
E

G
H
I
J
K
L
3E
3J
3I
3D
3H
3G
3L
3K


4




D
E
F

H
I
J
K
L
3E
3J
3I
3D
3H
3F
3L
3K


5




D
E
F
G

I
J
K
L
3E
3G
3I
3D
3J
3F
3L
3K


6




D
E
F
G
H

J
K
L
3E
3G
3J
3D
3H
3F
3L
3K


7




D
E
F
G
H
I

K
L
3E
3G
3I
3D
3H
3F
3L
3K


8




D
E
F
G
H
I
J

L
3E
3G
3J
3D
3H
3F
3L
3I


9




D
E
F
G
H
I
J
K

3E
3G
3J
3D
3H
3F
3I
3K


10



C


F
G
H
I
J
K
L
3H
3G
3I
3C
3J
3F
3L
3K


11



C

E

G
H
I
J
K
L
3E
3J
3I
3C
3H
3G
3L
3K


12



C

E
F

H
I
J
K
L
3E
3J
3I
3C
3H
3F
3L
3K


13



C

E
F
G

I
J
K
L
3E
3G
3I
3C
3J
3F
3L
3K


14



C

E
F
G
H

J
K
L
3E
3G
3J
3C
3H
3F
3L
3K


15



C

E
F
G
H
I

K
L
3E
3G
3I
3C
3H
3F
3L
3K


16



C

E
F
G
H
I
J

L
3E
3G
3J
3C
3H
3F
3L
3I


17



C

E
F
G
H
I
J
K

3E
3G
3J
3C
3H
3F
3I
3K


18



C
D


G
H
I
J
K
L
3H
3G
3I
3C
3J
3D
3L
3K


19



C
D

F

H
I
J
K
L
3C
3J
3I
3D
3H
3F
3L
3K


20



C
D

F
G

I
J
K
L
3C
3G
3I
3D
3J
3F
3L
3K


21



C
D

F
G
H

J
K
L
3C
3G
3J
3D
3H
3F
3L
3K


22



C
D

F
G
H
I

K
L
3C
3G
3I
3D
3H
3F
3L
3K


23



C
D

F
G
H
I
J

L
3C
3G
3J
3D
3H
3F
3L
3I


24



C
D

F
G
H
I
J
K

3C
3G
3J
3D
3H
3F
3I
3K


25



C
D
E


H
I
J
K
L
3E
3J
3I
3C
3H
3D
3L
3K


26



C
D
E

G

I
J
K
L
3E
3G
3I
3C
3J
3D
3L
3K


27



C
D
E

G
H

J
K
L
3E
3G
3J
3C
3H
3D
3L
3K


28



C
D
E

G
H
I

K
L
3E
3G
3I
3C
3H
3D
3L
3K


29



C
D
E

G
H
I
J

L
3E
3G
3J
3C
3H
3D
3L
3I


30



C
D
E

G
H
I
J
K

3E
3G
3J
3C
3H
3D
3I
3K


31



C
D
E
F


I
J
K
L
3C
3J
3E
3D
3I
3F
3L
3K


32



C
D
E
F

H

J
K
L
3C
3J
3E
3D
3H
3F
3L
3K


33



C
D
E
F

H
I

K
L
3C
3E
3I
3D
3H
3F
3L
3K


34



C
D
E
F

H
I
J

L
3C
3J
3E
3D
3H
3F
3L
3I


35



C
D
E
F

H
I
J
K

3C
3J
3E
3D
3H
3F
3I
3K


36



C
D
E
F
G


J
K
L
3C
3G
3E
3D
3J
3F
3L
3K


37



C
D
E
F
G

I

K
L
3C
3G
3E
3D
3I
3F
3L
3K


38



C
D
E
F
G

I
J

L
3C
3G
3E
3D
3J
3F
3L
3I


39



C
D
E
F
G

I
J
K

3C
3G
3E
3D
3J
3F
3I
3K


40



C
D
E
F
G
H


K
L
3C
3G
3E
3D
3H
3F
3L
3K


41



C
D
E
F
G
H

J

L
3C
3G
3J
3D
3H
3F
3L
3E


42



C
D
E
F
G
H

J
K

3C
3G
3J
3D
3H
3F
3E
3K


43



C
D
E
F
G
H
I


L
3C
3G
3E
3D
3H
3F
3L
3I


44



C
D
E
F
G
H
I

K

3C
3G
3E
3D
3H
3F
3I
3K


45



C
D
E
F
G
H
I
J


3C
3G
3J
3D
3H
3F
3E
3I


46


B



F
G
H
I
J
K
L
3H
3J
3B
3F
3I
3G
3L
3K


47


B


E

G
H
I
J
K
L
3E
3J
3I
3B
3H
3G
3L
3K


48


B


E
F

H
I
J
K
L
3E
3J
3B
3F
3I
3H
3L
3K


49


B


E
F
G

I
J
K
L
3E
3J
3B
3F
3I
3G
3L
3K


50


B


E
F
G
H

J
K
L
3E
3J
3B
3F
3H
3G
3L
3K


51


B


E
F
G
H
I

K
L
3E
3G
3B
3F
3I
3H
3L
3K


52


B


E
F
G
H
I
J

L
3E
3J
3B
3F
3H
3G
3L
3I


53


B


E
F
G
H
I
J
K

3E
3J
3B
3F
3H
3G
3I
3K


54


B

D


G
H
I
J
K
L
3H
3J
3B
3D
3I
3G
3L
3K


55


B

D

F

H
I
J
K
L
3H
3J
3B
3D
3I
3F
3L
3K


56


B

D

F
G

I
J
K
L
3I
3G
3B
3D
3J
3F
3L
3K


57


B

D

F
G
H

J
K
L
3H
3G
3B
3D
3J
3F
3L
3K


58


B

D

F
G
H
I

K
L
3H
3G
3B
3D
3I
3F
3L
3K


59


B

D

F
G
H
I
J

L
3H
3G
3B
3D
3J
3F
3L
3I


60


B

D

F
G
H
I
J
K

3H
3G
3B
3D
3J
3F
3I
3K


61


B

D
E


H
I
J
K
L
3E
3J
3B
3D
3I
3H
3L
3K

...10533 lines truncated...

The tool call succeeded but the output was truncated. Full output saved to: C:\Users\santi\.local\share\opencode\tool-output\tool_efa1324430012goyIupwtNianC
Use the Task tool to have explore agent process this file with Grep and Read (with offset/limit). Do NOT read the full file yourself - delegate to save context.
```

---

## Assistant (Plan · Nemotron 3 Ultra Free · 119.9s)

_Thinking:_

The Wikipedia template has the full 495 combinations table. Let me get the full content. The tool-output file has it saved. Let me read it or use grep to extract the relevant data. But first, let me understand the structure:

The table has:
- Left side: Which groups' 3rd place teams qualify (8 out of 12 groups)
- Right side: The 8 matchups showing which 3rd place team (3A, 3B, etc.) plays against which group winner (1A, 1B, 1D, 1E, 1G, 1I, 1K, 1L)

The 8 group winners that face 3rd place teams are: 1A, 1B, 1D, 1E, 1G, 1I, 1K, 1L

And the other 8 matches are:
- 1C vs 2F
- 1F vs 2C
- 1H vs 2J
- 1J vs 2H
- 2A vs 2B
- 2D vs 2G
- 2E vs 2I
- 2K vs 2L

Let me look at the match-later.com article again for the exact mapping. It had the 16 fixed Round of 32 matches:

|Match |Pairing |
| --- | --- |
|1 |**1E vs 3ABCDF** |
|2 |**1I vs 3CDFGH** |
|3 |**2A vs 2B** |
|4 |**1F vs 2C** |
|5 |**2K vs 2L** |
|6 |**1H vs 2J** |
|7 |**1D vs 3BEFIJ** |
|8 |**1G vs 3AEHIJ** |
|9 |**1C vs 2F** |
|10 |**2E vs 2I** |
|11 |**1A vs 3CEFHI** |
|12 |**1L vs 3EHIJK** |
|13 |**1J vs 2H** |
|14 |**2D vs 2G** |
|15 |**1B vs 3EFGIJ** |
|16 |**1K vs 3DEIJL** |

So the 8 group winners that face 3rd place teams are: 1E, 1I, 1D, 1G, 1C, 1L, 1A, 1K, 1B, 1J, 1H, 1F... wait that's more than 8. Let me re-read.

Actually from the table, the matches involving 3rd place teams are:
- Match 1: 1E vs 3ABCDF
- Match 2: 1I vs 3CDFGH
- Match 7: 1D vs 3BEFIJ
- Match 8: 1G vs 3AEHIJ
- Match 11: 1A vs 3CEFHI
- Match 12: 1L vs 3EHIJK
- Match 15: 1B vs 3EFGIJ
- Match 16: 1K vs 3DEIJL

That's 8 matches with 3rd place teams. The other 8 are runner-up vs runner-up or winner vs runner-up.

Now the Wikipedia template shows a different set of group winners: 1A, 1B, 1D, 1E, 1G, 1I, 1K, 1L - these are the 8 group winners that face 3rd place teams.

This matches! The 8 group winners that face 3rd place teams are: A, B, D, E, G, I, K, L (not C, F, H, J)

Wait, match-later.com says 1C, 1F, 1H, 1J face runner-ups, and 1E, 1I, 1D, 1G, 1A, 1L, 1B, 1K face 3rd place. That's the same set: A, B, D, E, G, I, K, L.

Good, so the mapping is:
- Group winners facing 3rd place teams: 1A, 1B, 1D, 1E, 1G, 1I, 1K, 1L
- Group winners facing runner-ups: 1C (vs 2F), 1F (vs 2C), 1H (vs 2J), 1J (vs 2H)
- Runner-up vs runner-up: 2A vs 2B, 2D vs 2G, 2E vs 2I, 2K vs 2L

Now I need to understand the Annex C table properly. The Wikipedia template shows for each combination of 8 qualifying 3rd place groups, which 3rd place team goes to which group winner.

For example, row 1: qualifying groups are E, F, G, H, I, J, K, L. Then the matchups are:
- 1A vs 3E
- 1B vs 3J
- 1D vs 3I
- 1E vs 3F
- 1G vs 3H
- 1I vs 3G
- 1K vs 3L
- 1L vs 3K

Row 2: qualifying groups are D, F, G, H, I, J, K, L. Then:
- 1A vs 3H
- 1B vs 3G
- 1D vs 3I
- 1E vs 3D
- 1G vs 3J
- 1I vs 3F
- 1K vs 3L
- 1L vs 3K

So the algorithm to build the correct fixtures is:
1. After group stage, determine which 8 groups have their 3rd place team qualify
2. Look up the combination in the Annex C table (495 combinations)
3. Based on that, assign each qualified 3rd place team to a specific group winner matchup
4. Build the 16 Round of 32 matches accordingly

Now let me formulate the plan.

Now I have a comprehensive understanding. Let me also check the build_dataset.py to understand the data structure better, and then create the plan.


**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\santi\\Desktop\\prediccion-mundial\\src\\build_dataset.py"
}
```

**Output:**
```
<path>C:\Users\santi\Desktop\prediccion-mundial\src\build_dataset.py</path>
<type>file</type>
<content>
1: """Build an enriched football results dataset for machine learning.
2: 
3: The script reads ``data/results.csv``, computes pre-match features using only
4: historical information available before each match, and writes
5: ``data/results_enriched.csv``.
6: """
7: 
8: from __future__ import annotations
9: 
10: from collections import defaultdict, deque
11: from dataclasses import dataclass
12: from pathlib import Path
13: from typing import DefaultDict, Deque, Dict, List, Tuple
14: 
15: import pandas as pd
16: 
17: from dixon_coles import StrengthMap, fit_dixon_coles, get_team_strength
18: 
19: 
20: INITIAL_ELO = 1500.0
21: HOME_ADVANTAGE = 100.0
22: WINDOW_SIZE = 5
23: PROGRESS_EVERY = 5000
24: 
25: # --- Dixon-Coles refit cadence ---
26: # Refitting is a separate, more expensive optimization step (unlike Elo,
27: # which updates incrementally after every match with a closed-form
28: # formula). Refitting after every single match would be wasteful and slow,
29: # so strengths are recalculated periodically using only matches already
30: # seen up to that point (no data leakage from the future).
31: DIXON_COLES_REFIT_EVERY = 1000
32: DIXON_COLES_MIN_MATCHES = 200
33: 
34: # Only matches from the last N years (relative to the match being
35: # featurized) are used to fit Dixon-Coles. Two reasons for this:
36: #   1. Performance: keeps the buffer size roughly constant instead of
37: #      growing for the entire dataset (49k+ matches), so refits near
38: #      the end of a long historical dataset don't get progressively
39: #      slower.
40: #   2. Correctness: a team's current attack/defense strength should
41: #      reflect how it plays *now*, not how it played decades ago.
42: #      Football has changed enough that very old matches are not
43: #      representative of current strength.
44: DIXON_COLES_WINDOW_YEARS = 4
45: 
46: K_VALUES = {
47:     # Mundial
48:     "FIFA World Cup": 60,
49: 
50:     # Eliminatorias mundialistas
51:     "FIFA World Cup qualification": 40,
52: 
53:     # Eurocopa
54:     "UEFA Euro": 50,
55:     "UEFA Euro qualification": 40,
56: 
57:     # Copa América
58:     "Copa América": 50,
59: 
60:     # Copa Africana
61:     "African Cup of Nations": 50,
62:     "African Cup of Nations qualification": 40,
63: 
64:     # Copa Asiática
65:     "AFC Asian Cup": 50,
66:     "AFC Asian Cup qualification": 40,
67: 
68:     # Copa Oro
69:     "Gold Cup": 50,
70:     "Gold Cup qualification": 40,
71: 
72:     # Nations League UEFA
73:     "UEFA Nations League": 35,
74: 
75:     # Nations League CONCACAF
76:     "CONCACAF Nations League": 35,
77: 
78:     # Copa Confederaciones
79:     "Confederations Cup": 50,
80: 
81:     # Copa de Oceanía
82:     "Oceania Nations Cup": 50,
83: 
84:     # Torneos amistosos
85:     "Friendly": 20,
86: }
87: DEFAULT_K = 30.0
88: 
89: REQUIRED_COLUMNS = [
90:     "date",
91:     "home_team",
92:     "away_team",
93:     "home_score",
94:     "away_score",
95:     "tournament",
96:     "city",
97:     "country",
98:     "neutral",
99: ]
100: 
101: OUTPUT_COLUMNS = REQUIRED_COLUMNS + [
102:     "home_elo_before",
103:     "away_elo_before",
104:     "elo_diff",
105:     "home_elo_change_last_5",
106:     "away_elo_change_last_5",
107:     "home_wins_last_5",
108:     "away_wins_last_5",
109:     "home_goals_for_last_5",
110:     "home_goals_against_last_5",
111:     "away_goals_for_last_5",
112:     "away_goals_against_last_5",
113:     "home_attack_strength",
114:     "home_defense_strength",
115:     "away_attack_strength",
116:     "away_defense_strength",
117: ]
118: 
119: 
120: @dataclass(frozen=True)
121: class MatchOutcome:
122:     """Container for a processed match result."""
123: 
124:     home_score: int
125:     away_score: int
126: 
127: 
128: def load_results(input_path: Path) -> pd.DataFrame:
129:     """Load and validate the historical results dataset."""
130: 
131:     if not input_path.exists():
132:         raise FileNotFoundError(f"Input file not found: {input_path}")
133: 
134:     df = pd.read_csv(input_path)
135:     missing_columns = [
136:         column for column in REQUIRED_COLUMNS if column not in df.columns]
137:     if missing_columns:
138:         raise ValueError(
139:             f"results.csv is missing required columns: {missing_columns}")
140: 
141:     raw_rows = len(df)
142:     df["date"] = pd.to_datetime(df["date"], errors="coerce")
143:     df["home_score"] = pd.to_numeric(df["home_score"], errors="coerce")
144:     df["away_score"] = pd.to_numeric(df["away_score"], errors="coerce")
145: 
146:     df = df.dropna(subset=REQUIRED_COLUMNS).copy()
147:     removed_rows = raw_rows - len(df)
148:     if removed_rows > 0:
149:         print(
150:             f"Dropped {removed_rows:,} rows with missing or invalid required data")
151: 
152:     df = df.sort_values("date", ascending=True).reset_index(drop=True)
153:     return df
154: 
155: 
156: def normalize_bool(value: object) -> bool:
157:     """Convert common CSV boolean representations to ``bool``."""
158: 
159:     if isinstance(value, bool):
160:         return value
161:     if pd.isna(value):
162:         return False
163: 
164:     normalized = str(value).strip().lower()
165:     return normalized in {"true", "1", "yes", "y", "t"}
166: 
167: 
168: def get_k_value(tournament: object) -> float:
169:     """Return the Elo K-factor for a tournament."""
170: 
171:     if pd.isna(tournament):
172:         return DEFAULT_K
173:     return K_VALUES.get(str(tournament).strip(), DEFAULT_K)
174: 
175: 
176: def expected_score(home_elo: float, away_elo: float, neutral: bool) -> float:
177:     """Calculate the expected home score using the traditional Elo formula."""
178: 
179:     effective_home_elo = home_elo if neutral else home_elo + HOME_ADVANTAGE
180:     return 1.0 / (1.0 + 10 ** ((away_elo - effective_home_elo) / 400.0))
181: 
182: 
183: def actual_scores(home_score: int, away_score: int) -> Tuple[float, float]:
184:     """Convert a match result into Elo actual scores."""
185: 
186:     if home_score > away_score:
187:         return 1.0, 0.0
188:     if home_score < away_score:
189:         return 0.0, 1.0
190:     return 0.5, 0.5
191: 
192: 
193: def rolling_sum(history: Deque[int]) -> int:
194:     """Return the sum of a fixed-length rolling history."""
195: 
196:     return int(sum(history))
197: 
198: 
199: def compute_elo_change(current_elo: float, history: Deque[float]) -> float:
200:     """Compute the Elo change versus the value from five matches ago."""
201: 
202:     if len(history) < WINDOW_SIZE:
203:         return 0.0
204:     return current_elo - history[0]
205: 
206: 
207: def append_team_histories(
208:     team: str,
209:     home_team: str,
210:     home_score: int,
211:     away_score: int,
212:     team_elo_before: float,
213:     team_elo_history: DefaultDict[str, Deque[float]],
214:     team_win_history: DefaultDict[str, Deque[int]],
215:     team_goals_for_history: DefaultDict[str, Deque[int]],
216:     team_goals_against_history: DefaultDict[str, Deque[int]],
217: ) -> None:
218:     """Append the latest match information to a team's rolling histories."""
219: 
220:     if team == home_team:
221:         goals_for = home_score
222:         goals_against = away_score
223:         wins = int(home_score > away_score)
224:     else:
225:         goals_for = away_score
226:         goals_against = home_score
227:         wins = int(away_score > home_score)
228: 
229:     team_elo_history[team].append(team_elo_before)
230:     team_win_history[team].append(wins)
231:     team_goals_for_history[team].append(goals_for)
232:     team_goals_against_history[team].append(goals_against)
233: 
234: 
235: def build_enriched_dataset(df: pd.DataFrame) -> pd.DataFrame:
236:     """Compute pre-match features and Elo updates for every match."""
237: 
238:     team_elos: DefaultDict[str, float] = defaultdict(lambda: INITIAL_ELO)
239:     team_elo_history: DefaultDict[str, Deque[float]] = defaultdict(
240:         lambda: deque(maxlen=WINDOW_SIZE))
241:     team_win_history: DefaultDict[str, Deque[int]] = defaultdict(
242:         lambda: deque(maxlen=WINDOW_SIZE))
243:     team_goals_for_history: DefaultDict[str, Deque[int]] = defaultdict(
244:         lambda: deque(maxlen=WINDOW_SIZE))
245:     team_goals_against_history: DefaultDict[str, Deque[int]] = defaultdict(
246:         lambda: deque(maxlen=WINDOW_SIZE))
247: 
248:     # --- Dixon-Coles state ---
249:     # `dixon_coles_strengths` holds the strengths currently in effect (fit
250:     # using only matches seen so far). `matches_seen_buffer` accumulates
251:     # raw results to feed the next periodic refit.
252:     dixon_coles_strengths: StrengthMap = {}
253:     matches_seen_buffer: List[Dict[str, object]] = []
254: 
255:     enriched_rows: List[Dict[str, object]] = []
256:     total_matches = len(df)
257: 
258:     for index, row in enumerate(df.itertuples(index=False), start=1):
259:         home_team = str(row.home_team)
260:         away_team = str(row.away_team)
261:         home_score = int(row.home_score)
262:         away_score = int(row.away_score)
263:         neutral = normalize_bool(row.neutral)
264:         tournament = row.tournament
265: 
266:         # Dixon-Coles strengths in effect for this match (computed using
267:         # only matches strictly before this point — see refit block below).
268:         home_attack, home_defense = get_team_strength(dixon_coles_strengths, home_team)
269:         away_attack, away_defense = get_team_strength(dixon_coles_strengths, away_team)
270: 
271:         home_elo_before = float(team_elos[home_team])
272:         away_elo_before = float(team_elos[away_team])
273:         elo_diff = home_elo_before - away_elo_before
274: 
275:         home_elo_change_last_5 = compute_elo_change(
276:             home_elo_before, team_elo_history[home_team])
277:         away_elo_change_last_5 = compute_elo_change(
278:             away_elo_before, team_elo_history[away_team])
279: 
280:         home_wins_last_5 = rolling_sum(team_win_history[home_team])
281:         away_wins_last_5 = rolling_sum(team_win_history[away_team])
282: 
283:         home_goals_for_last_5 = rolling_sum(team_goals_for_history[home_team])
284:         home_goals_against_last_5 = rolling_sum(
285:             team_goals_against_history[home_team])
286:         away_goals_for_last_5 = rolling_sum(team_goals_for_history[away_team])
287:         away_goals_against_last_5 = rolling_sum(
288:             team_goals_against_history[away_team])
289: 
290:         enriched_rows.append(
291:             {
292:                 "date": row.date.strftime("%Y-%m-%d"),
293:                 "home_team": home_team,
294:                 "away_team": away_team,
295:                 "home_score": home_score,
296:                 "away_score": away_score,
297:                 "tournament": tournament,
298:                 "city": row.city,
299:                 "country": row.country,
300:                 "neutral": row.neutral,
301:                 "home_elo_before": home_elo_before,
302:                 "away_elo_before": away_elo_before,
303:                 "elo_diff": elo_diff,
304:                 "home_elo_change_last_5": home_elo_change_last_5,
305:                 "away_elo_change_last_5": away_elo_change_last_5,
306:                 "home_wins_last_5": home_wins_last_5,
307:                 "away_wins_last_5": away_wins_last_5,
308:                 "home_goals_for_last_5": home_goals_for_last_5,
309:                 "home_goals_against_last_5": home_goals_against_last_5,
310:                 "away_goals_for_last_5": away_goals_for_last_5,
311:                 "away_goals_against_last_5": away_goals_against_last_5,
312:                 "home_attack_strength": home_attack,
313:                 "home_defense_strength": home_defense,
314:                 "away_attack_strength": away_attack,
315:                 "away_defense_strength": away_defense,
316:             }
317:         )
318: 
319:         expected_home = expected_score(
320:             home_elo_before, away_elo_before, neutral)
321:         expected_away = 1.0 - expected_home
322:         actual_home, actual_away = actual_scores(home_score, away_score)
323:         k_factor = get_k_value(tournament)
324: 
325:         team_elos[home_team] = home_elo_before + \
326:             k_factor * (actual_home - expected_home)
327:         team_elos[away_team] = away_elo_before + \
328:             k_factor * (actual_away - expected_away)
329: 
330:         append_team_histories(
331:             team=home_team,
332:             home_team=home_team,
333:             home_score=home_score,
334:             away_score=away_score,
335:             team_elo_before=home_elo_before,
336:             team_elo_history=team_elo_history,
337:             team_win_history=team_win_history,
338:             team_goals_for_history=team_goals_for_history,
339:             team_goals_against_history=team_goals_against_history,
340:         )
341:         append_team_histories(
342:             team=away_team,
343:             home_team=home_team,
344:             home_score=home_score,
345:             away_score=away_score,
346:             team_elo_before=away_elo_before,
347:             team_elo_history=team_elo_history,
348:             team_win_history=team_win_history,
349:             team_goals_for_history=team_goals_for_history,
350:             team_goals_against_history=team_goals_against_history,
351:         )
352: 
353:         # This match is now "past" information — safe to use in the next refit.
354:         matches_seen_buffer.append(
355:             {
356:                 "date": row.date,
357:                 "home_team": home_team,
358:                 "away_team": away_team,
359:                 "home_score": home_score,
360:                 "away_score": away_score,
361:                 "neutral": neutral,
362:             }
363:         )
364: 
365:         if (
366:             index % DIXON_COLES_REFIT_EVERY == 0
367:             and len(matches_seen_buffer) >= DIXON_COLES_MIN_MATCHES
368:         ):
369:             current_date = row.date
370:             window_start = current_date - pd.DateOffset(years=DIXON_COLES_WINDOW_YEARS)
371: 
372:             # Drop matches older than the window from the buffer itself —
373:             # keeps it from growing for the entire dataset and keeps
374:             # refits roughly constant-time regardless of how many total
375:             # matches have been processed so far.
376:             matches_seen_buffer = [
377:                 match for match in matches_seen_buffer if match["date"] >= window_start
378:             ]
379: 
380:             if len(matches_seen_buffer) >= DIXON_COLES_MIN_MATCHES:
381:                 buffer_df = pd.DataFrame(matches_seen_buffer)
382:                 all_teams = pd.unique(
383:                     pd.concat([buffer_df["home_team"], buffer_df["away_team"]], ignore_index=True)
384:                 )
385:                 dixon_coles_strengths = fit_dixon_coles(buffer_df, list(all_teams))
386:                 print(
387:                     f"Refit Dixon-Coles at match {index:,} using {len(buffer_df):,} matches "
388:                     f"from the last {DIXON_COLES_WINDOW_YEARS} years",
389:                     flush=True,
390:                 )
391:             else:
392:                 print(
393:                     f"Skipped Dixon-Coles refit at match {index:,}: only "
394:                     f"{len(matches_seen_buffer):,} matches in the last "
395:                     f"{DIXON_COLES_WINDOW_YEARS} years (need {DIXON_COLES_MIN_MATCHES:,})",
396:                     flush=True,
397:                 )
398: 
399:         if index % PROGRESS_EVERY == 0 or index == total_matches:
400:             print(f"Processed {index:,}/{total_matches:,} matches", flush=True)
401: 
402:     enriched_df = pd.DataFrame(enriched_rows)
403:     enriched_df = enriched_df[OUTPUT_COLUMNS]
404:     return enriched_df
405: 
406: 
407: def main() -> None:
408:     """Run the dataset building pipeline."""
409: 
410:     project_root = Path(__file__).resolve().parents[1]
411:     input_path = project_root / "data" / "results.csv"
412:     output_path = project_root / "data" / "results_enriched.csv"
413: 
414:     print(f"Loading input dataset from {input_path}")
415:     df = load_results(input_path)
416:     print(f"Loaded {len(df):,} matches. Building enriched dataset...")
417: 
418:     enriched_df = build_enriched_dataset(df)
419:     enriched_df.to_csv(output_path, index=False)
420: 
421:     unique_teams = pd.unique(
422:         pd.concat([df["home_team"], df["away_team"]], ignore_index=True))
423:     print("Finished successfully")
424:     print(f"Output written to: {output_path}")
425:     print(f"Total matches processed: {len(df):,}")
426:     print(f"Unique teams: {len(unique_teams):,}")
427: 
428: 
429: if __name__ == "__main__":
430:     main()

(End of file - total 430 lines)
</content>
```

---

## Assistant (Plan · Nemotron 3 Ultra Free · 87.9s)

_Thinking:_

Now I have a comprehensive understanding of the codebase. Let me now create the plan for the user.

The key issues are:

1. **`mundial_2026.csv` has incorrect format**: The current CSV uses placeholder format like `3rd_1`, `3rd_2`, `3rd_3`, `3rd_4`, etc. for the Round of 32 third-place team matches (lines 86-89). This is a simplified approach that doesn't match FIFA's official Annex C mapping.

2. **Missing Annex C logic in Monte Carlo**: The simulation needs to:
   - After group stage, determine which 8 groups' 3rd place teams qualify
   - Look up the specific combination in FIFA's Annex C (495 combinations) to determine which 3rd place team plays which group winner
   - Build the correct 16 Round of 32 fixtures

The FIFA official Round of 32 bracket has 16 matches:
- 8 matches are group winner vs runner-up or runner-up vs runner-up (fixed)
- 8 matches are group winner vs 3rd place team (determined by Annex C based on which 8 groups qualify their 3rd place teams)

The 8 group winners that face 3rd place teams: 1A, 1B, 1D, 1E, 1G, 1I, 1K, 1L
The 4 group winners that face runner-ups: 1C vs 2F, 1F vs 2C, 1H vs 2J, 1J vs 2H
The 4 runner-up vs runner-up: 2A vs 2B, 2D vs 2G, 2E vs 2I, 2K vs 2L

Now I need to create a comprehensive plan that covers:

1. Fix the `mundial_2026.csv` format to use the correct FIFA structure
2. Create the Annex C lookup table (495 combinations) 
3. Add a function in `monte_carlo_world_cup.py` to build correct Round of 32 fixtures based on which 3rd place teams qualify

Let me also check if there's an existing JSON/structured version of the Annex C table somewhere, or if we need to extract it from Wikipedia.

Now I have all the information needed. Let me create a comprehensive plan.


**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Analyze current mundial_2026.csv format issues and FIFA official bracket structure",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Research FIFA Annex C 495 combinations table for 3rd place team matchups",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Create comprehensive implementation plan",
      "status": "in_progress",
      "priority": "high"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Analyze current mundial_2026.csv format issues and FIFA official bracket structure",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Research FIFA Annex C 495 combinations table for 3rd place team matchups",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Create comprehensive implementation plan",
    "status": "in_progress",
    "priority": "high"
  }
]
```

---

## Assistant (Plan · Nemotron 3 Ultra Free · 237.7s)

_Thinking:_

Now I'll present the comprehensive plan to the user.

## Plan: Fix World Cup 2026 Simulation Format & Implement FIFA Annex C Logic

### Problem Analysis

**Current Issues in `mundial_2026.csv` (lines 74-89):**
- Uses simplified placeholders: `3rd_1` vs `3rd_2`, `3rd_3` vs `3rd_4`, etc.
- This ignores FIFA's official **Annex C** which defines **495 specific combinations** mapping each set of 8 qualifying 3rd-place groups to specific Round of 32 matchups
- The current approach incorrectly assumes 3rd place teams play each other, but per FIFA rules: **3rd place teams ONLY face group winners** (never runners-up or other 3rd place teams)

**FIFA Official Round of 32 Structure (16 matches):**
| Match | Pairing | Type |
|-------|---------|------|
| 1 | 1E vs 3rd(ABCDF) | GW vs 3rd |
| 2 | 1I vs 3rd(CDFGH) | GW vs 3rd |
| 3 | 2A vs 2B | RU vs RU |
| 4 | 1F vs 2C | GW vs RU |
| 5 | 2K vs 2L | RU vs RU |
| 6 | 1H vs 2J | GW vs RU |
| 7 | 1D vs 3rd(BEFIJ) | GW vs 3rd |
| 8 | 1G vs 3rd(AEHIJ) | GW vs 3rd |
| 9 | 1C vs 2F | GW vs RU |
| 10 | 2E vs 2I | RU vs RU |
| 11 | 1A vs 3rd(CEFHI) | GW vs 3rd |
| 12 | 1L vs 3rd(EHIJK) | GW vs 3rd |
| 13 | 1J vs 2H | GW vs RU |
| 14 | 2D vs 2G | RU vs RU |
| 15 | 1B vs 3rd(EFGIJ) | GW vs 3rd |
| 16 | 1K vs 3rd(DEIJL) | GW vs 3rd |

**8 group winners face 3rd place teams:** 1A, 1B, 1D, 1E, 1G, 1I, 1K, 1L

---

### Implementation Plan

#### Phase 1: Fix `mundial_2026.csv` Format
Replace the current Round of 32 section (lines 74-89) with the **official FIFA fixture structure** using descriptive placeholders that reference the Annex C mapping logic:

```csv
# Round of 32 - Fixed pairings (GW=Group Winner, RU=Runner-up, 3rd=3rd place)
2026-06-28,R32,,1E,3rd_1,,,FIFA World Cup,,,TRUE
2026-06-28,R32,,1I,3rd_2,,,FIFA World Cup,,,TRUE
2026-06-28,R32,,2A,2B,,,FIFA World Cup,,,TRUE
2026-06-28,R32,,1F,2C,,,FIFA World Cup,,,TRUE
2026-06-28,R32,,2K,2L,,,FIFA World Cup,,,TRUE
2026-06-28,R32,,1H,2J,,,FIFA World Cup,,,TRUE
2026-06-29,R32,,1D,3rd_3,,,FIFA World Cup,,,TRUE
2026-06-29,R32,,1G,3rd_4,,,FIFA World Cup,,,TRUE
2026-06-29,R32,,1C,2F,,,FIFA World Cup,,,TRUE
2026-06-29,R32,,2E,2I,,,FIFA World Cup,,,TRUE
2026-06-30,R32,,1A,3rd_5,,,FIFA World Cup,,,TRUE
2026-06-30,R32,,1L,3rd_6,,,FIFA World Cup,,,TRUE
2026-06-30,R32,,1J,2H,,,FIFA World Cup,,,TRUE
2026-06-30,R32,,2D,2G,,,FIFA World Cup,,,TRUE
2026-07-01,R32,,1B,3rd_7,,,FIFA World Cup,,,TRUE
2026-07-01,R32,,1K,3rd_8,,,FIFA World Cup,,,TRUE
```

**Note:** The `3rd_1` through `3rd_8` are now **slots** (not teams) that will be filled by the Annex C lookup function based on which 8 groups' 3rd place teams actually qualify.

---

#### Phase 2: Create Annex C Lookup Table
Create a new file `src/annex_c.py` with the **495-combination mapping table** extracted from FIFA regulations (Wikipedia template). Structure:

```python
# src/annex_c.py
# Maps frozenset of 8 qualifying group letters -> dict of {slot: 3rd_place_group}
# Slot order: [3rd_for_1A, 3rd_for_1B, 3rd_for_1D, 3rd_for_1E, 3rd_for_1G, 3rd_for_1I, 3rd_for_1K, 3rd_for_1L]

ANNEX_C_MAP: dict[frozenset[str], tuple[str, ...]] = {
    frozenset({"E","F","G","H","I","J","K","L"}): ("E","J","I","F","H","G","L","K"),
    frozenset({"D","F","G","H","I","J","K","L"}): ("H","G","I","D","J","F","L","K"),
    # ... all 495 entries
}
```

**Extraction approach:** Parse the Wikipedia template table (495 rows) programmatically or embed as static data.

---

#### Phase 3: Implement `build_round_of_32_fixtures()` Function in `monte_carlo_world_cup.py`

**New function signature:**
```python
def build_round_of_32_fixtures(
    qualifiers: dict[str, list[str]],      # {"A": ["Mexico", "South Africa"], ...}
    third_place_order: list[str],           # ["Mexico", "Morocco", ...] - top 8
    group_3rd_place_teams: dict[str, str],  # {"A": "Mexico", "B": "Qatar", ...} - all 12
    annex_c_map: dict[frozenset[str], tuple[str, ...]]
) -> list[tuple[str, str]]:  # Returns 16 (home, away) tuples for R32
```

**Algorithm:**
1. Identify which 8 groups have their 3rd place team in `third_place_order` → `qualifying_3rd_groups = {group for group, team in group_3rd_place_teams.items() if team in third_place_order}`
2. Look up `annex_c_map[frozenset(qualifying_3rd_groups)]` → returns tuple of 8 group letters (e.g., `("E","J","I","F","H","G","L","K")`)
3. Map each to the corresponding slot: slot 0→1A, slot 1→1B, slot 2→1D, slot 3→1E, slot 4→1G, slot 5→1I, slot 6→1K, slot 7→1L
4. Build the 16 matches combining fixed pairings + Annex C resolved 3rd place matchups

---

#### Phase 4: Integrate into Simulation Flow

**Modify `simulate_world_cup()` in `monte_carlo_world_cup.py`:**
1. After `rank_group_teams()` returns `qualifiers` and `third_place_order`, also capture `group_3rd_place_teams` (all 12 groups' 3rd place teams)
2. Call `build_round_of_32_fixtures()` to get the 16 actual matchups
3. Replace the current `resolve_placeholders()` + `resolve_knockout_bracket()` for R32 with the new fixtures
4. Continue with existing R16/QF/SF/FINAL logic (bracket progression remains the same)

---

#### Phase 5: Testing & Validation
1. Run simulation and verify:
   - No 3rd place team faces another 3rd place team in R32
   - No team faces a group-mate in R32
   - All 495 combinations work correctly
   - Bracket progression to R16/QF/SF/FINAL follows FIFA regulations

---

### Files to Modify/Create

| File | Change |
|------|--------|
| `data/mundial_2026.csv` | Replace lines 74-89 with official FIFA R32 structure |
| `src/annex_c.py` | **NEW** - 495-combination Annex C lookup table |
| `src/monte_carlo_world_cup.py` | Add `build_round_of_32_fixtures()`, integrate into `simulate_world_cup()` |

---

### Questions for Clarification

1. **Annex C data source**: Should I extract the 495 rows from the Wikipedia template programmatically, or would you prefer a pre-extracted JSON/CSV file? The Wikipedia table has all 495 rows but parsing it requires handling the HTML/wiki markup.

2. **Team names in `mundial_2026.csv`**: The current CSV uses placeholder teams (e.g., "South Africa", "Czech Republic" for Group A). Should these be updated to the **actual qualified teams** from the FIFA draw, or keep as-is for simulation flexibility?

3. **Performance**: The Annex C lookup is O(1) dict access. Should the 495-entry dict be embedded in code or loaded from a separate JSON file?

4. **Backward compatibility**: Do you need to maintain compatibility with existing `results/wcsims.json` output format, or can the output structure change?

---

### Next Steps

Once you confirm the approach, I'll:
1. Extract the Annex C table from Wikipedia (or use a pre-made JSON if you have one)
2. Fix `mundial_2026.csv` format
3. Implement the new function and integrate it
4. Run a test simulation to verify correctness

**Ready to proceed with implementation?**

---

## User

ejecuta el plan

---

## Assistant (Build · Nemotron 3 Ultra Free · 38.4s)

_Thinking:_

The user wants me to execute the plan. Let me start by:

1. First, extracting the Annex C 495 combinations from the Wikipedia template
2. Fixing the mundial_2026.csv format
3. Creating the annex_c.py module
4. Modifying monte_carlo_world_cup.py to integrate the new logic

Let me start with extracting the Annex C data from Wikipedia. The Wikipedia page has the full 495-row table. I'll need to parse it.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Analyze current mundial_2026.csv format issues and FIFA official bracket structure",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Research FIFA Annex C 495 combinations table for 3rd place team matchups",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Create comprehensive implementation plan",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Extract Annex C 495 combinations from Wikipedia template",
      "status": "in_progress",
      "priority": "high"
    },
    {
      "content": "Fix mundial_2026.csv with official FIFA R32 structure",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Create src/annex_c.py with 495-combination lookup table",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Implement build_round_of_32_fixtures() in monte_carlo_world_cup.py",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Integrate Annex C logic into simulate_world_cup()",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Test simulation with new format",
      "status": "pending",
      "priority": "high"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Analyze current mundial_2026.csv format issues and FIFA official bracket structure",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Research FIFA Annex C 495 combinations table for 3rd place team matchups",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Create comprehensive implementation plan",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Extract Annex C 495 combinations from Wikipedia template",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Fix mundial_2026.csv with official FIFA R32 structure",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Create src/annex_c.py with 495-combination lookup table",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Implement build_round_of_32_fixtures() in monte_carlo_world_cup.py",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Integrate Annex C logic into simulate_world_cup()",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Test simulation with new format",
    "status": "pending",
    "priority": "high"
  }
]
```

---

## Assistant (Build · Nemotron 3 Ultra Free · 31.7s)

_Thinking:_

Now let me extract the Annex C table from Wikipedia. I saw that the Wikipedia template page has the full 495-row table. Let me fetch it and parse it.

**Tool: webfetch**

**Input:**
```json
{
  "url": "https://en.wikipedia.org/wiki/Template:2026_FIFA_World_Cup_third-place_table",
  "format": "html"
}
```

**Output:**
```
<!DOCTYPE html>
<html class="client-nojs vector-feature-language-in-header-enabled vector-feature-language-in-main-menu-disabled vector-feature-language-in-main-page-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-1 vector-feature-appearance-pinned-clientpref-1 skin-theme-clientpref-day vector-sticky-header-enabled vector-toc-not-available skin-thumbsize-clientpref-standard" lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<title>Template:2026 FIFA World Cup third-place table - Wikipedia</title>
<script>(function(){var className="client-js vector-feature-language-in-header-enabled vector-feature-language-in-main-menu-disabled vector-feature-language-in-main-page-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-1 vector-feature-appearance-pinned-clientpref-1 skin-theme-clientpref-day vector-sticky-header-enabled vector-toc-not-available skin-thumbsize-clientpref-standard";var cookie=document.cookie.match(/(?:^|; )enwikimwclientpreferences=([^;]+)/);if(cookie){cookie[1].split('%2C').forEach(function(pref){className=className.replace(new RegExp('(^| )'+pref.replace(/-clientpref-\w+$|[^\w-]+/g,'')+'-clientpref-\\w+( |$)'),'$1'+pref+'$2');});}document.documentElement.className=className;}());RLCONF={"wgBreakFrames":false,"wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgRequestId":"ba0510a0-9b38-4c25-8730-400760c82335","wgCanonicalNamespace":"Template","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":10,"wgPageName":"Template:2026_FIFA_World_Cup_third-place_table","wgTitle":"2026 FIFA World Cup third-place table","wgCurRevisionId":1360082985,"wgRevisionId":1360082985,"wgArticleId":80416954,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["2026 FIFA World Cup templates"],"wgPageViewLanguage":"en","wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgRelevantPageName":"Template:2026_FIFA_World_Cup_third-place_table","wgRelevantArticleId":80416954,"wgTempUserName":null,"wgIsProbablyEditable":true,"wgRelevantPageIsProbablyEditable":true,"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgNoticeProject":"wikipedia","wgFlaggedRevsParams":{"tags":{"status":{"levels":1}}},"wgConfirmEditCaptchaNeededForGenericEdit":"hcaptcha","wgConfirmEditForceShowCaptcha":false,"wgConfirmEditHCaptchaSiteKey":"5d0c670e-a5f4-4258-ad16-1f42792c9c62","wgMediaViewerOnClick":true,"wgMediaViewerEnabledByDefault":true,"wgMediaViewerMobileBeta":false,"wgPopupsFlags":0,"wgVisualEditor":{"pageLanguageCode":"en","pageLanguageDir":"ltr","pageVariantFallbacks":"en"},"wgMFDisplayWikibaseDescriptions":{"search":true,"watchlist":true,"tagline":false,"nearby":true},"wgWMESchemaEditAttemptStepOversample":false,"wgWMEPageLength":90000,"wgTestKitchenUserExperiments":{"overrides":[],"enrolled":[],"assigned":[],"subject_ids":[]},"wgEditSubmitButtonLabelPublish":true,"wgVisualEditorPageIsDisambiguation":false,"wgULSPosition":"interlanguage","wgULSisCompactLinksEnabled":false,"wgVector2022LanguageInHeader":true,"wgULSisLanguageSelectorEmpty":false,"wgULSLanguageSelectorV2Enabled":false,"wgWikibaseItemId":"Q136499811","wgCheckUserClientHintsHeadersJsApi":["brands","architecture","bitness","fullVersionList","mobile","model","platform","platformVersion"],"wgPersonalDashboardMenuVisible":false};
RLSTATE={"ext.globalCssJs.user.styles":"ready","site.styles":"ready","user.styles":"ready","ext.globalCssJs.user":"ready","user":"ready","user.options":"loading","ext.wikimediamessages.styles":"ready","skins.vector.search.codex.styles":"ready","skins.vector.styles":"ready","skins.vector.icons":"ready","jquery.tablesorter.styles":"ready","jquery.makeCollapsible.styles":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready","wikibase.client.init":"ready"};RLPAGEMODULES=["ext.parsermigration.survey","site","mediawiki.page.ready","jquery.tablesorter","jquery.makeCollapsible","skins.vector.js","ext.centralNotice.geoIP","ext.centralNotice.startUp","ext.gadget.ReferenceTooltips","ext.gadget.switcher","ext.urlShortener.toolbar","ext.centralauth.centralautologin","ext.testKitchen","mmv.bootstrap","ext.popups","ext.visualEditor.desktopArticleTarget.init","ext.echo.centralauth","ext.eventLogging","ext.wikimediaEvents","ext.navigationTiming","ext.uls.interface","ext.cx.eventlogging.campaigns","wikibase.client.vector-2022","wikibase.databox.fromWikidata","ext.checkUser.clientHints"];</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.loader.impl(function(){return["user.options@12s5i",function($,jQuery,require,module){mw.user.tokens.set({"patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
}];});});</script>
<link rel="stylesheet" href="/w/load.php?lang=en&amp;modules=ext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediamessages.styles%7Cjquery.makeCollapsible.styles%7Cjquery.tablesorter.styles%7Cskins.vector.icons%2Cstyles%7Cskins.vector.search.codex.styles%7Cwikibase.client.init&amp;only=styles&amp;skin=vector-2022">
<script async="" src="/w/load.php?lang=en&amp;modules=startup&amp;only=scripts&amp;raw=1&amp;skin=vector-2022"></script>
<meta name="ResourceLoaderDynamicStyles" content="">
<link rel="stylesheet" href="/w/load.php?lang=en&amp;modules=site.styles&amp;only=styles&amp;skin=vector-2022">
<meta name="generator" content="MediaWiki 1.47.0-wmf.7">
<meta name="referrer" content="origin">
<meta name="referrer" content="origin-when-cross-origin">
<meta name="robots" content="max-image-preview:standard">
<meta name="format-detection" content="telephone=no">
<meta name="viewport" content="width=1120">
<meta property="og:title" content="Template:2026 FIFA World Cup third-place table - Wikipedia">
<meta property="og:type" content="website">
<link rel="alternate" type="application/x-wiki" title="Edit this page" href="/w/index.php?title=Template:2026_FIFA_World_Cup_third-place_table&amp;action=edit">
<link rel="apple-touch-icon" href="/static/apple-touch/wikipedia.png">
<link rel="icon" href="/static/favicon/wikipedia.ico">
<link rel="search" type="application/opensearchdescription+xml" href="/w/rest.php/v1/search" title="Wikipedia (en)">
<link rel="EditURI" type="application/rsd+xml" href="//en.wikipedia.org/w/api.php?action=rsd">
<link rel="canonical" href="https://en.wikipedia.org/wiki/Template:2026_FIFA_World_Cup_third-place_table">
<link rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/deed.en">
<link rel="alternate" type="application/atom+xml" title="Wikipedia Atom feed" href="/w/index.php?title=Special:RecentChanges&amp;feed=atom">
<link rel="dns-prefetch" href="//meta.wikimedia.org" />
<link rel="dns-prefetch" href="auth.wikimedia.org">
</head>
<body class="skin--responsive skin-vector skin-vector-search-vue mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-10 ns-subject mw-editable page-Template_2026_FIFA_World_Cup_third-place_table rootpage-Template_2026_FIFA_World_Cup_third-place_table skin-vector-2022 action-view">
<div id="mw-aria-live-region" class="mw-aria-live-region" aria-live="polite"></div><a class="mw-jump-link" href="#bodyContent">Jump to content</a>
<div class="vector-header-container">
	<header class="vector-header mw-header no-font-mode-scale">
		<div class="vector-header-start">
			<nav class="vector-main-menu-landmark" aria-label="Site">
				
<div id="vector-main-menu-dropdown" class="vector-dropdown vector-main-menu-dropdown vector-button-flush-left vector-button-flush-right"  title="Main menu" >
	<input type="checkbox" id="vector-main-menu-dropdown-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-vector-main-menu-dropdown" class="vector-dropdown-checkbox "  aria-label="Main menu"  >
	<label id="vector-main-menu-dropdown-label" for="vector-main-menu-dropdown-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only " aria-hidden="true"  ><span class="vector-icon mw-ui-icon-menu mw-ui-icon-wikimedia-menu"></span>

<span class="vector-dropdown-label-text">Main menu</span>
	</label>
	<div class="vector-dropdown-content">


				<div id="vector-main-menu-unpinned-container" class="vector-unpinned-container">
		
<div id="vector-main-menu" class="vector-main-menu vector-pinnable-element">
	<div
	class="vector-pinnable-header vector-main-menu-pinnable-header vector-pinnable-header-unpinned"
	data-feature-name="main-menu-pinned"
	data-pinnable-element-id="vector-main-menu"
	data-pinned-container-id="vector-main-menu-pinned-container"
	data-unpinned-container-id="vector-main-menu-unpinned-container"
>
	<div class="vector-pinnable-header-label">Main menu</div>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-pin-button" data-event-name="pinnable-header.vector-main-menu.pin">move to sidebar</button>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-unpin-button" data-event-name="pinnable-header.vector-main-menu.unpin">hide</button>
</div>

	
<div id="p-navigation" class="vector-menu mw-portlet mw-portlet-navigation"  >
	<div class="vector-menu-heading">
		Navigation
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="n-mainpage-description" class="mw-list-item"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z"><span>Main page</span></a></li><li id="n-contents" class="mw-list-item"><a href="/wiki/Wikipedia:Contents" title="Guides to browsing Wikipedia"><span>Contents</span></a></li><li id="n-currentevents" class="mw-list-item"><a href="/wiki/Portal:Current_events" title="Articles related to current events"><span>Current events</span></a></li><li id="n-randompage" class="mw-list-item"><a href="/wiki/Special:Random" title="Visit a randomly selected article [x]" accesskey="x"><span>Random article</span></a></li><li id="n-aboutsite" class="mw-list-item"><a href="/wiki/Wikipedia:About" title="Learn about Wikipedia and how it works"><span>About Wikipedia</span></a></li><li id="n-contactpage" class="mw-list-item"><a href="//en.wikipedia.org/wiki/Wikipedia:Contact_us" title="How to contact Wikipedia"><span>Contact us</span></a></li>
		</ul>
		
	</div>
</div>

	
<div id="p-interaction" class="vector-menu mw-portlet mw-portlet-interaction"  >
	<div class="vector-menu-heading">
		Contribute
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="n-help" class="mw-list-item"><a href="/wiki/Help:Contents" title="Guidance on how to use and edit Wikipedia"><span>Help</span></a></li><li id="n-introduction" class="mw-list-item"><a href="/wiki/Help:Introduction" title="Learn how to edit Wikipedia"><span>Learn to edit</span></a></li><li id="n-portal" class="mw-list-item"><a href="/wiki/Wikipedia:Community_portal" title="The hub for editors"><span>Community portal</span></a></li><li id="n-recentchanges" class="mw-list-item"><a href="/wiki/Special:RecentChanges" title="A list of recent changes to Wikipedia [r]" accesskey="r"><span>Recent changes</span></a></li><li id="n-upload" class="mw-list-item"><a href="/wiki/Wikipedia:File_upload_wizard" title="Add images or other media for use on Wikipedia"><span>Upload file</span></a></li><li id="n-specialpages" class="mw-list-item"><a href="/wiki/Special:SpecialPages" title="A list of all special pages [q]" accesskey="q"><span>Special pages</span></a></li>
		</ul>
		
	</div>
</div>

<div id="p-electronpdfservice-sidebar-portlet-heading" class="vector-menu mw-portlet mw-portlet-electronpdfservice-sidebar-portlet-heading"  >
	<div class="vector-menu-heading">
		Print/export
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="electron-print_pdf" class="mw-list-item"><a href="/w/index.php?title=Special:DownloadAsPdf&amp;page=Template%3A2026_FIFA_World_Cup_third-place_table&amp;action=show-download-screen"><span>Download as PDF</span></a></li><li id="t-print" class="mw-list-item"><a href="javascript:print();" rel="alternate" title="Printable version of this page [p]" accesskey="p"><span>Printable version</span></a></li>
		</ul>
		
	</div>
</div>

<div id="p-wikibase-otherprojects" class="vector-menu mw-portlet mw-portlet-wikibase-otherprojects"  >
	<div class="vector-menu-heading">
		In other projects
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="t-wikibase" class="wb-otherproject-link wb-otherproject-wikibase-dataitem mw-list-item"><a href="https://www.wikidata.org/wiki/Special:EntityPage/Q136499811" title="Structured data on this page hosted by Wikidata [g]" accesskey="g"><span>Wikidata item</span></a></li>
		</ul>
		
	</div>
</div>

</div>

				</div>

	</div>
</div>

		</nav>
			
<a href="/wiki/Main_Page" class="mw-logo">
	<img class="mw-logo-icon" src="/static/images/icons/enwiki-25.svg" alt="" aria-hidden="true" height="50" width="50">
	<span class="mw-logo-container skin-invert">
		<img class="mw-logo-wordmark" alt="Wikipedia" src="/static/images/mobile/copyright/wikipedia-wordmark-en-25.svg" style="width: 8.75em; height: 1.375em;">
		<img class="mw-logo-tagline" alt="The Free Encyclopedia" src="/static/images/mobile/copyright/wikipedia-tagline-en-25.svg" width="140" height="11" style="width: 8.75em; height: 0.6875em;">
	</span>
</a>

		</div>
		<div class="vector-header-end">
			
<div id="p-search" role="search" class="vector-search-box-vue  vector-search-box-collapses vector-search-box-show-thumbnail vector-search-box-auto-expand-width vector-search-box">
	<a href="/wiki/Special:Search" class="cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only search-toggle" title="Search Wikipedia [f]" accesskey="f"><span class="vector-icon mw-ui-icon-search mw-ui-icon-wikimedia-search"></span>

<span>Search</span>
	</a>
	<div class="vector-typeahead-search-container">
		<div class="cdx-typeahead-search cdx-typeahead-search--show-thumbnail cdx-typeahead-search--auto-expand-width">
			<form action="/w/index.php" id="searchform" class="cdx-search-input cdx-search-input--has-end-button">
				<div id="simpleSearch" class="cdx-search-input__input-wrapper"  data-search-loc="header-moved">
					<div class="cdx-text-input cdx-text-input--has-start-icon">
						<input
							class="cdx-text-input__input mw-searchInput" autocomplete="off"
							 type="search" name="search" placeholder="Search Wikipedia" aria-label="Search Wikipedia" autocapitalize="none" spellcheck="false" title="Search Wikipedia [f]" accesskey="f" id="searchInput"
							>
						<span class="cdx-text-input__icon cdx-text-input__start-icon"></span>
					</div>
					<input type="hidden" name="title" value="Special:Search">
				</div>
				<button class="cdx-button cdx-search-input__end-button">Search</button>
			</form>
		</div>
	</div>
</div>

			<nav class="vector-user-links vector-user-links-wide" aria-label="Personal tools">
	<div class="vector-user-links-main">
	
<div id="p-vector-user-menu-preferences" class="vector-menu mw-portlet emptyPortlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			
		</ul>
		
	</div>
</div>

	
<div id="p-vector-user-menu-userpage" class="vector-menu mw-portlet emptyPortlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			
		</ul>
		
	</div>
</div>

	<nav class="vector-appearance-landmark" aria-label="Appearance">
		
<div id="vector-appearance-dropdown" class="vector-dropdown "  title="Change the appearance of the page&#039;s font size, width, and color" >
	<input type="checkbox" id="vector-appearance-dropdown-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-vector-appearance-dropdown" class="vector-dropdown-checkbox "  aria-label="Appearance"  >
	<label id="vector-appearance-dropdown-label" for="vector-appearance-dropdown-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only " aria-hidden="true"  ><span class="vector-icon mw-ui-icon-appearance mw-ui-icon-wikimedia-appearance"></span>

<span class="vector-dropdown-label-text">Appearance</span>
	</label>
	<div class="vector-dropdown-content">


			<div id="vector-appearance-unpinned-container" class="vector-unpinned-container">
				
			</div>
		
	</div>
</div>

	</nav>
	
<div id="p-vector-user-menu-notifications" class="vector-menu mw-portlet emptyPortlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			
		</ul>
		
	</div>
</div>

	
<div id="p-vector-user-menu-overflow" class="vector-menu mw-portlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			<li id="pt-sitesupport-2" class="mw-list-item user-links-collapsible-item vector-menu-item--collapsible"><a data-mw-interface  href="https://donate.wikimedia.org/?wmf_source=donate&amp;wmf_medium=sidebar&amp;wmf_campaign=en.wikipedia.org&amp;uselang=en" data-mw-donate-attempt="top_link" class=""><span>Donate</span></a>
</li>
<li id="pt-createaccount-2" class="mw-list-item user-links-collapsible-item vector-menu-item--collapsible"><a data-mw-interface  href="/w/index.php?title=Special:CreateAccount&amp;returnto=Template%3A2026+FIFA+World+Cup+third-place+table" title="You are encouraged to create an account and log in; however, it is not mandatory" class=""><span>Create account</span></a>
</li>
<li id="pt-login-2" class="mw-list-item user-links-collapsible-item vector-menu-item--collapsible"><a data-mw-interface  href="/w/index.php?title=Special:UserLogin&amp;returnto=Template%3A2026+FIFA+World+Cup+third-place+table" title="You&#039;re encouraged to log in; however, it&#039;s not mandatory. [o]" accesskey="o" class=""><span>Log in</span></a>
</li>

			
		</ul>
		
	</div>
</div>

	</div>
	
<div id="vector-user-links-dropdown" class="vector-dropdown vector-user-menu vector-button-flush-right vector-user-menu-logged-out vector-user-links-dropdown--collapsible user-links-collapsible-item"  title="Log in and more options" >
	<input type="checkbox" id="vector-user-links-dropdown-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-vector-user-links-dropdown" class="vector-dropdown-checkbox "  aria-label="Personal tools"  >
	<label id="vector-user-links-dropdown-label" for="vector-user-links-dropdown-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only " aria-hidden="true"  ><span class="vector-icon mw-ui-icon-ellipsis mw-ui-icon-wikimedia-ellipsis"></span>

<span class="vector-dropdown-label-text">Personal tools</span>
	</label>
	<div class="vector-dropdown-content">


		
<div id="p-personal" class="vector-menu mw-portlet mw-portlet-personal"  title="User menu" >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			<li id="pt-sitesupport" class="mw-list-item user-links-collapsible-item vector-menu-item--collapsible"><a data-mw-interface  href="https://donate.wikimedia.org/?wmf_source=donate&amp;wmf_medium=sidebar&amp;wmf_campaign=en.wikipedia.org&amp;uselang=en" data-mw-donate-attempt="top_link" class=""><span class="vector-icon mw-ui-icon-heart mw-ui-icon-wikimedia-heart"></span>

<span>Donate</span></a>
</li>
<li id="pt-createaccount" class="mw-list-item user-links-collapsible-item vector-menu-item--collapsible"><a data-mw-interface  href="/w/index.php?title=Special:CreateAccount&amp;returnto=Template%3A2026+FIFA+World+Cup+third-place+table" title="You are encouraged to create an account and log in; however, it is not mandatory" class=""><span class="vector-icon mw-ui-icon-userAdd mw-ui-icon-wikimedia-userAdd"></span>

<span>Create account</span></a>
</li>
<li id="pt-login" class="mw-list-item user-links-collapsible-item vector-menu-item--collapsible"><a data-mw-interface  href="/w/index.php?title=Special:UserLogin&amp;returnto=Template%3A2026+FIFA+World+Cup+third-place+table" title="You&#039;re encouraged to log in; however, it&#039;s not mandatory. [o]" accesskey="o" class=""><span class="vector-icon mw-ui-icon-logIn mw-ui-icon-wikimedia-logIn"></span>

<span>Log in</span></a>
</li>

			
		</ul>
		
	</div>
</div>

	
	</div>
</div>

</nav>

		</div>
	</header>
</div>
<div class="mw-page-container">
	<div class="mw-page-container-inner">
		<div class="vector-sitenotice-container">
			<div id="siteNotice"><!-- CentralNotice --></div>
		</div>
		<div class="vector-column-start">
			<div class="vector-main-menu-container">
		<div id="mw-navigation">
			<nav id="mw-panel" class="vector-main-menu-landmark" aria-label="Site">
				<div id="vector-main-menu-pinned-container" class="vector-pinned-container">
				
				</div>
		</nav>
		</div>
	</div>
</div>
		<div class="mw-content-container">
			<main id="content" class="mw-body">
				<header class="mw-body-header vector-page-titlebar no-font-mode-scale">
					<h1 id="firstHeading" class="firstHeading mw-first-heading"><span lang="en" dir="ltr"><span class="mw-page-title-namespace">Template</span><span class="mw-page-title-separator">:</span><span class="mw-page-title-main">2026 FIFA World Cup third-place table</span></span></h1>
							
<div id="p-lang-btn" class="vector-dropdown mw-portlet mw-portlet-lang"  >
	<input type="checkbox" id="p-lang-btn-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-p-lang-btn" class="vector-dropdown-checkbox mw-interlanguage-selector" aria-label="Go to an article in another language. Available in 9 languages"   >
	<label id="p-lang-btn-label" for="p-lang-btn-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--action-progressive mw-portlet-lang-heading-9" aria-hidden="true"  ><span class="vector-icon mw-ui-icon-language-progressive mw-ui-icon-wikimedia-language-progressive"></span>

<span class="vector-dropdown-label-text">9 languages</span>
	</label>
	<div class="vector-dropdown-content">

		<div class="vector-menu-content">
			
			<ul class="vector-menu-content-list">
				
				<li class="interlanguage-link interwiki-ar mw-list-item"><a href="https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D9%84%D8%A8:%D8%AC%D8%AF%D9%88%D9%84_%D8%AA%D8%B1%D8%AA%D9%8A%D8%A8_%D8%A7%D9%84%D9%85%D8%B1%D9%83%D8%B2_%D8%A7%D9%84%D8%AB%D8%A7%D9%84%D8%AB_%D9%81%D9%8A_%D9%83%D8%A3%D8%B3_%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85_2026" title="قالب:جدول ترتيب المركز الثالث في كأس العالم 2026 – Arabic" lang="ar" hreflang="ar" data-title="قالب:جدول ترتيب المركز الثالث في كأس العالم 2026" data-language-autonym="العربية" data-language-local-name="Arabic" class="interlanguage-link-target"><span>العربية</span></a></li><li class="interlanguage-link interwiki-id mw-list-item"><a href="https://id.wikipedia.org/wiki/Templat:Kombinasi_peringkat_ketiga_Piala_Dunia_FIFA_2026" title="Templat:Kombinasi peringkat ketiga Piala Dunia FIFA 2026 – Indonesian" lang="id" hreflang="id" data-title="Templat:Kombinasi peringkat ketiga Piala Dunia FIFA 2026" data-language-autonym="Bahasa Indonesia" data-language-local-name="Indonesian" class="interlanguage-link-target"><span>Bahasa Indonesia</span></a></li><li class="interlanguage-link interwiki-ja mw-list-item"><a href="https://ja.wikipedia.org/wiki/Template:2026_FIFA%E3%83%AF%E3%83%BC%E3%83%AB%E3%83%89%E3%82%AB%E3%83%83%E3%83%97%E3%83%BB3%E4%BD%8D%E7%B5%84%E3%81%BF%E5%90%88%E3%82%8F%E3%81%9B%E8%A1%A8" title="Template:2026 FIFAワールドカップ・3位組み合わせ表 – Japanese" lang="ja" hreflang="ja" data-title="Template:2026 FIFAワールドカップ・3位組み合わせ表" data-language-autonym="日本語" data-language-local-name="Japanese" class="interlanguage-link-target"><span>日本語</span></a></li><li class="interlanguage-link interwiki-ko mw-list-item"><a href="https://ko.wikipedia.org/wiki/%ED%8B%80:2026%EB%85%84_FIFA_%EC%9B%94%EB%93%9C%EC%BB%B5_3%EC%9C%84_%EC%A1%B0%ED%95%A9%ED%91%9C" title="틀:2026년 FIFA 월드컵 3위 조합표 – Korean" lang="ko" hreflang="ko" data-title="틀:2026년 FIFA 월드컵 3위 조합표" data-language-autonym="한국어" data-language-local-name="Korean" class="interlanguage-link-target"><span>한국어</span></a></li><li class="interlanguage-link interwiki-ru mw-list-item"><a href="https://ru.wikipedia.org/wiki/%D0%A8%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD:%D0%A7%D0%B5%D0%BC%D0%BF%D0%B8%D0%BE%D0%BD%D0%B0%D1%82_%D0%BC%D0%B8%D1%80%D0%B0_%D0%BF%D0%BE_%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D1%83_2026._%D0%9A%D0%BE%D0%BC%D0%B1%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D0%B8_%D1%82%D1%80%D0%B5%D1%82%D1%8C%D0%B8%D1%85_%D0%BC%D0%B5%D1%81%D1%82" title="Шаблон:Чемпионат мира по футболу 2026. Комбинации третьих мест – Russian" lang="ru" hreflang="ru" data-title="Шаблон:Чемпионат мира по футболу 2026. Комбинации третьих мест" data-language-autonym="Русский" data-language-local-name="Russian" class="interlanguage-link-target"><span>Русский</span></a></li><li class="interlanguage-link interwiki-th mw-list-item"><a href="https://th.wikipedia.org/wiki/%E0%B9%81%E0%B8%A1%E0%B9%88%E0%B9%81%E0%B8%9A%E0%B8%9A:%E0%B8%95%E0%B8%B2%E0%B8%A3%E0%B8%B2%E0%B8%87%E0%B8%97%E0%B8%B5%E0%B8%A1%E0%B8%AD%E0%B8%B1%E0%B8%99%E0%B8%94%E0%B8%B1%E0%B8%9A%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%AA%E0%B8%B2%E0%B8%A1%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9F%E0%B8%B8%E0%B8%95%E0%B8%9A%E0%B8%AD%E0%B8%A5%E0%B9%82%E0%B8%A5%E0%B8%81_2026" title="แม่แบบ:ตารางทีมอันดับที่สามของฟุตบอลโลก 2026 – Thai" lang="th" hreflang="th" data-title="แม่แบบ:ตารางทีมอันดับที่สามของฟุตบอลโลก 2026" data-language-autonym="ไทย" data-language-local-name="Thai" class="interlanguage-link-target"><span>ไทย</span></a></li><li class="interlanguage-link interwiki-uz mw-list-item"><a href="https://uz.wikipedia.org/wiki/Andoza:Futbol_bo%CA%BByicha_2026-yilgi_jahon_chempionati_uchinchi_o%CA%BBrin_jadvali" title="Andoza:Futbol boʻyicha 2026-yilgi jahon chempionati uchinchi oʻrin jadvali – Uzbek" lang="uz" hreflang="uz" data-title="Andoza:Futbol boʻyicha 2026-yilgi jahon chempionati uchinchi oʻrin jadvali" data-language-autonym="Oʻzbekcha / ўзбекча" data-language-local-name="Uzbek" class="interlanguage-link-target"><span>Oʻzbekcha / ўзбекча</span></a></li><li class="interlanguage-link interwiki-vi mw-list-item"><a href="https://vi.wikipedia.org/wiki/B%E1%BA%A3n_m%E1%BA%ABu:B%E1%BA%A3ng_x%E1%BA%BFp_h%E1%BA%A1ng_Tranh_h%E1%BA%A1ng_ba_Gi%E1%BA%A3i_v%C3%B4_%C4%91%E1%BB%8Bch_b%C3%B3ng_%C4%91%C3%A1_th%E1%BA%BF_gi%E1%BB%9Bi_2026" title="Bản mẫu:Bảng xếp hạng Tranh hạng ba Giải vô địch bóng đá thế giới 2026 – Vietnamese" lang="vi" hreflang="vi" data-title="Bản mẫu:Bảng xếp hạng Tranh hạng ba Giải vô địch bóng đá thế giới 2026" data-language-autonym="Tiếng Việt" data-language-local-name="Vietnamese" class="interlanguage-link-target"><span>Tiếng Việt</span></a></li><li class="interlanguage-link interwiki-zh mw-list-item"><a href="https://zh.wikipedia.org/wiki/Template:2026%E5%B9%B4%E5%9C%8B%E9%9A%9B%E8%B6%B3%E5%8D%94%E4%B8%96%E7%95%8C%E7%9B%83%E7%AC%AC%E4%B8%89%E4%BD%8D%E7%B5%84%E5%90%88%E5%88%97%E8%A1%A8" title="Template:2026年國際足協世界盃第三位組合列表 – Chinese" lang="zh" hreflang="zh" data-title="Template:2026年國際足協世界盃第三位組合列表" data-language-autonym="中文" data-language-local-name="Chinese" class="interlanguage-link-target"><span>中文</span></a></li>
			</ul>
			<div class="after-portlet after-portlet-lang"><span class="wb-langlinks-edit wb-langlinks-link"><a href="https://www.wikidata.org/wiki/Special:EntityPage/Q136499811#sitelinks-wikipedia" title="Edit interlanguage links" class="wbc-editpage">Edit links</a></span></div>
		</div>

	</div>
</div>
</header>
				<div class="vector-page-toolbar vector-feature-custom-font-size-clientpref--excluded">
					<div class="vector-page-toolbar-container">
						<div id="left-navigation">
							<nav aria-label="Namespaces">
								
<div id="p-associated-pages" class="vector-menu vector-menu-tabs mw-portlet mw-portlet-associated-pages"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="ca-nstab-template" class="selected vector-tab-noicon mw-list-item"><a href="/wiki/Template:2026_FIFA_World_Cup_third-place_table" title="View the template [c]" accesskey="c"><span>Template</span></a></li><li id="ca-talk" class="vector-tab-noicon mw-list-item"><a href="/wiki/Template_talk:2026_FIFA_World_Cup_third-place_table" rel="discussion" class="mw-redirect" title="Discuss improvements to the content page [t]" accesskey="t"><span>Talk</span></a></li>
		</ul>
		
	</div>
</div>

								
<div id="vector-variants-dropdown" class="vector-dropdown emptyPortlet"  >
	<input type="checkbox" id="vector-variants-dropdown-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-vector-variants-dropdown" class="vector-dropdown-checkbox " aria-label="Change language variant"   >
	<label id="vector-variants-dropdown-label" for="vector-variants-dropdown-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet" aria-hidden="true"  ><span class="vector-dropdown-label-text">English</span>
	</label>
	<div class="vector-dropdown-content">


					
<div id="p-variants" class="vector-menu mw-portlet mw-portlet-variants emptyPortlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			
		</ul>
		
	</div>
</div>

				
	</div>
</div>

							</nav>
						</div>
						<div id="right-navigation" class="vector-collapsible">
							<nav aria-label="Views">
			    
<div id="p-views" class="vector-menu vector-menu-tabs mw-portlet mw-portlet-views"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			<li id="ca-view" class="selected mw-list-item user-links-collapsible-item vector-menu-item--collapsible vector-tab-noicon"><a data-mw-interface  href="/wiki/Template:2026_FIFA_World_Cup_third-place_table" class=""><span>Read</span></a>
</li>
<li id="ca-edit" class="mw-list-item user-links-collapsible-item vector-menu-item--collapsible vector-tab-noicon"><a data-mw-interface  href="/w/index.php?title=Template:2026_FIFA_World_Cup_third-place_table&amp;action=edit" title="Edit this page [e]" accesskey="e" class=""><span>Edit</span></a>
</li>
<li id="ca-history" class="mw-list-item user-links-collapsible-item vector-menu-item--collapsible vector-tab-noicon"><a data-mw-interface  href="/w/index.php?title=Template:2026_FIFA_World_Cup_third-place_table&amp;action=history" title="Past revisions of this page [h]" accesskey="h" class=""><span>View history</span></a>
</li>

			
		</ul>
		
	</div>
</div>

			</nav>

							<nav class="vector-page-tools-landmark" aria-label="Page tools">
								
<div id="vector-page-tools-dropdown" class="vector-dropdown vector-page-tools-dropdown"  >
	<input type="checkbox" id="vector-page-tools-dropdown-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-vector-page-tools-dropdown" class="vector-dropdown-checkbox "  aria-label="Tools"  >
	<label id="vector-page-tools-dropdown-label" for="vector-page-tools-dropdown-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet" aria-hidden="true"  ><span class="vector-dropdown-label-text">Tools</span>
	</label>
	<div class="vector-dropdown-content">


									<div id="vector-page-tools-unpinned-container" class="vector-unpinned-container">
						
<div id="vector-page-tools" class="vector-page-tools vector-pinnable-element">
	<div
	class="vector-pinnable-header vector-page-tools-pinnable-header vector-pinnable-header-unpinned"
	data-feature-name="page-tools-pinned"
	data-pinnable-element-id="vector-page-tools"
	data-pinned-container-id="vector-page-tools-pinned-container"
	data-unpinned-container-id="vector-page-tools-unpinned-container"
>
	<div class="vector-pinnable-header-label">Tools</div>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-pin-button" data-event-name="pinnable-header.vector-page-tools.pin">move to sidebar</button>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-unpin-button" data-event-name="pinnable-header.vector-page-tools.unpin">hide</button>
</div>

	
<div id="p-cactions" class="vector-menu mw-portlet mw-portlet-cactions emptyPortlet vector-has-collapsible-items"  >
	<div class="vector-menu-heading">
		Actions
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			<li id="ca-more-view" class="selected vector-more-collapsible-item mw-list-item"><a data-mw-interface  href="/wiki/Template:2026_FIFA_World_Cup_third-place_table" class=""><span class="vector-icon mw-ui-icon-eye mw-ui-icon-wikimedia-eye"></span>

<span>Read</span></a>
</li>
<li id="ca-more-edit" class="vector-more-collapsible-item mw-list-item"><a data-mw-interface  href="/w/index.php?title=Template:2026_FIFA_World_Cup_third-place_table&amp;action=edit" title="Edit this page [e]" accesskey="e" class=""><span class="vector-icon mw-ui-icon-edit mw-ui-icon-wikimedia-edit"></span>

<span>Edit</span></a>
</li>
<li id="ca-more-history" class="vector-more-collapsible-item mw-list-item"><a data-mw-interface  href="/w/index.php?title=Template:2026_FIFA_World_Cup_third-place_table&amp;action=history" class=""><span class="vector-icon mw-ui-icon-history mw-ui-icon-wikimedia-history"></span>

<span>View history</span></a>
</li>

			
		</ul>
		
	</div>
</div>

<div id="p-tb" class="vector-menu mw-portlet mw-portlet-tb"  >
	<div class="vector-menu-heading">
		General
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="t-whatlinkshere" class="mw-list-item"><a href="/wiki/Special:WhatLinksHere/Template:2026_FIFA_World_Cup_third-place_table" title="List of all English Wikipedia pages containing links to this page [j]" accesskey="j"><span>What links here</span></a></li><li id="t-recentchangeslinked" class="mw-list-item"><a href="/wiki/Special:RecentChangesLinked/Template:2026_FIFA_World_Cup_third-place_table" rel="nofollow" title="Recent changes in pages linked from this page [k]" accesskey="k"><span>Related changes</span></a></li><li id="t-upload" class="mw-list-item"><a href="//en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard" title="Upload files [u]" accesskey="u"><span>Upload file</span></a></li><li id="t-permalink" class="mw-list-item"><a href="/w/index.php?title=Template:2026_FIFA_World_Cup_third-place_table&amp;oldid=1360082985" title="Permanent link to this revision of this page"><span>Permanent link</span></a></li><li id="t-info" class="mw-list-item"><a href="/w/index.php?title=Template:2026_FIFA_World_Cup_third-place_table&amp;action=info" title="More information about this page"><span>Page information</span></a></li><li id="t-urlshortener" class="mw-list-item"><a href="/w/index.php?title=Special:UrlShortener&amp;url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FTemplate%3A2026_FIFA_World_Cup_third-place_table"><span>Get shortened URL</span></a></li>
		</ul>
		
	</div>
</div>

<div id="p-electronpdfservice-sidebar-portlet-heading" class="vector-menu mw-portlet mw-portlet-electronpdfservice-sidebar-portlet-heading"  >
	<div class="vector-menu-heading">
		Print/export
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="electron-print_pdf" class="mw-list-item"><a href="/w/index.php?title=Special:DownloadAsPdf&amp;page=Template%3A2026_FIFA_World_Cup_third-place_table&amp;action=show-download-screen"><span>Download as PDF</span></a></li><li id="t-print" class="mw-list-item"><a href="javascript:print();" rel="alternate" title="Printable version of this page [p]" accesskey="p"><span>Printable version</span></a></li>
		</ul>
		
	</div>
</div>

<div id="p-wikibase-otherprojects" class="vector-menu mw-portlet mw-portlet-wikibase-otherprojects"  >
	<div class="vector-menu-heading">
		In other projects
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="t-wikibase" class="wb-otherproject-link wb-otherproject-wikibase-dataitem mw-list-item"><a href="https://www.wikidata.org/wiki/Special:EntityPage/Q136499811" title="Structured data on this page hosted by Wikidata [g]" accesskey="g"><span>Wikidata item</span></a></li>
		</ul>
		
	</div>
</div>

</div>

									</div>
				
	</div>
</div>

							</nav>
						</div>
					</div>
				</div>
				<div class="vector-column-end no-font-mode-scale">
					<div class="vector-sticky-pinned-container">
						<div class="wp25eastereggs-vector-sitenotice-landmark"></div>
						<nav class="vector-page-tools-landmark" aria-label="Page tools">
							<div id="vector-page-tools-pinned-container" class="vector-pinned-container">
				
							</div>
		</nav>
						<nav class="vector-appearance-landmark" aria-label="Appearance">
							<div id="vector-appearance-pinned-container" class="vector-pinned-container">
				<div id="vector-appearance" class="vector-appearance vector-pinnable-element">
	<div
	class="vector-pinnable-header vector-appearance-pinnable-header vector-pinnable-header-pinned"
	data-feature-name="appearance-pinned"
	data-pinnable-element-id="vector-appearance"
	data-pinned-container-id="vector-appearance-pinned-container"
	data-unpinned-container-id="vector-appearance-unpinned-container"
>
	<div class="vector-pinnable-header-label">Appearance</div>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-pin-button" data-event-name="pinnable-header.vector-appearance.pin">move to sidebar</button>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-unpin-button" data-event-name="pinnable-header.vector-appearance.unpin">hide</button>
</div>


</div>

							</div>
		</nav>
					</div>
				</div>
				<div id="bodyContent" class="vector-body" aria-labelledby="firstHeading" data-mw-ve-target-container>
					<div class="vector-body-before-content">
							<div class="mw-indicators">
		</div>

						<div id="siteSub" class="noprint">From Wikipedia, the free encyclopedia</div>
					</div>
					<div id="contentSub"><div id="mw-content-subtitle"></div></div>
					
					
					<div id="mw-content-text" class="mw-body-content"><div class="mw-subjectpageheader">
</div><div class="mw-content-ltr mw-parser-output" lang="en" dir="ltr"><style data-mw-deduplicate="TemplateStyles:r1322140512">@media screen{.mw-parser-output .sticky-table-scroll{margin-bottom:1em;margin-top:1em;max-height:75vh;max-width:max-content;min-width:50px;overflow-y:auto}.mw-parser-output .sticky-table-scroll table{margin-bottom:0;margin-top:0}.mw-parser-output .sticky-table-scroll caption{text-align:left}.mw-parser-output .sticky-table-scroll .sticky-table-row1:not(.sticky-table-row2):not(.sticky-table-head)>thead>tr:nth-child(1),.mw-parser-output .sticky-table-scroll .sticky-table-row1:not(.sticky-table-row2):not(.sticky-table-head)>caption+tbody>tr:nth-child(1),.mw-parser-output .sticky-table-scroll .sticky-table-row1:not(.sticky-table-row2):not(.sticky-table-head)>tbody:first-child>tr:nth-child(1),.mw-parser-output .sticky-table-scroll .sticky-table-row2:not(.sticky-table-row1):not(.sticky-table-head)>thead>tr:nth-child(2),.mw-parser-output .sticky-table-scroll .sticky-table-row2:not(.sticky-table-row1):not(.sticky-table-head)>caption+tbody>tr:nth-child(2),.mw-parser-output .sticky-table-scroll .sticky-table-row2:not(.sticky-table-row1):not(.sticky-table-head)>tbody:first-child>tr:nth-child(2),.mw-parser-output .sticky-table-scroll .sticky-table-head:not(.sticky-table-row1):not(.sticky-table-row2)>thead{position:sticky;top:0;z-index:10}.mw-parser-output .sticky-table-scroll .sticky-table-col1:not(.sticky-table-col2)>*>tr>:nth-child(1):not(.sticky-table-none),.mw-parser-output .sticky-table-scroll .sticky-table-col2:not(.sticky-table-col1)>*>tr>:nth-child(2):not(.sticky-table-none),.mw-parser-output .sticky-table-scroll tr>.sticky-table-left{position:sticky;left:0;z-index:9}.mw-parser-output .sticky-table-scroll table:not(.wikitable){background-color:var(--color-inverted,#fff)}.mw-parser-output .sticky-table-scroll thead,.mw-parser-output .sticky-table-scroll tbody,.mw-parser-output .sticky-table-scroll tfoot,.mw-parser-output .sticky-table-scroll tr,.mw-parser-output .sticky-table-scroll td,.mw-parser-output .sticky-table-scroll table:not(.wikitable)>*>tr>th{background-color:inherit}.mw-parser-output .sticky-table-scroll .wikitable{border-collapse:separate;border-spacing:0;border-width:1px 0 0 1px}.mw-parser-output .sticky-table-scroll .wikitable>*>tr>td,.mw-parser-output .sticky-table-scroll .wikitable>*>tr>th{border-width:0 1px 1px 0}.mw-parser-output .sticky-table-scroll .static-row-numbers.wikitable>*>tr::before{border-right-width:1px}.mw-parser-output .sticky-table-scroll .static-row-numbers.wikitable>tbody>tr:last-child::before,.mw-parser-output .sticky-table-scroll .static-row-numbers.wikitable>tfoot>tr:last-child::before{border-bottom-width:1px}.mw-parser-output .sticky-table-scroll .static-row-numbers.wikitable>tbody:first-of-type>tr:not(.static-row-header)::before{border-top-width:0;border-left-width:0}body.skin-timeless .mw-parser-output .sticky-table-scroll .overflowed,body.skin-timeless .mw-parser-output .sticky-table-scroll .overflowed .content-table{overflow:visible}body.skin-timeless .mw-parser-output .sticky-table-scroll .overflowed{margin-top:0;margin-bottom:0}body.skin-timeless .mw-parser-output .sticky-table-scroll .scroll-right.overflowed .content-table-right{box-shadow:none;border-left:none}body.skin-timeless .mw-parser-output .sticky-table-scroll .wikitable{padding:0}html.ve-activated .mw-parser-output .sticky-table-scroll{max-height:none}}@media screen and (max-width:639px){body.skin-minerva .mw-parser-output .sticky-table-scroll table,body.skin-monobook .mw-parser-output .sticky-table-scroll table,body.skin-vector-legacy .mw-parser-output .sticky-table-scroll table,body.skin-vector-2022 .mw-parser-output .sticky-table-scroll table{display:table}body.skin-minerva .mw-parser-output .sticky-table-scroll caption{display:table-caption}}@media screen{.mw-parser-output .sticky-table-scroll .jquery-tablesorter:not(.sticky-table-head)>thead,.mw-parser-output .sticky-table-scroll .mw-sticky-header:not(.sticky-table-head)>thead{position:static;top:auto;z-index:auto}.mw-parser-output .sticky-table-scroll .jquery-tablesorter>tfoot,.mw-parser-output .sticky-table-scroll .mw-sticky-header>tfoot{position:static;bottom:auto;z-index:auto}}@media screen and (min-width:1120px){html.client-js.vector-sticky-header-enabled .mw-parser-output .sticky-table-scroll :not(.sticky-table-head) .mw-sticky-header-element{top:auto!important}}</style><div class="sticky-table-scroll" style="scrollbar-gutter: stable;"><style data-mw-deduplicate="TemplateStyles:r1304002105">.mw-parser-output .hover-highlight tr:hover,.mw-parser-output .mw-datatable tr:hover{background-color:var(--background-color-progressive-subtle,#f1f4fd);color:var(--color-base,#202122)}.mw-parser-output .mw-datatable{background-color:var(--background-color-base,#fff);color:var(--color-base,#202122)}</style>
<table class="wikitable mw-collapsible sortable sticky-table-head hover-highlight sort-under-center" style="text-align:center; white-space:nowrap;">
<caption>Combinations of matches in the round of 32
</caption>
<tbody><tr>
<th scope="col" style="width:2em"><abbr title="Option number">No.</abbr>
</th>
<th scope="col" style="width:2em" class="unsortable" colspan="12"><style data-mw-deduplicate="TemplateStyles:r1045256916">.mw-parser-output .navbar-header{text-align:center;position:relative;white-space:nowrap}.mw-parser-output .navbar-header .navbar{position:absolute;right:0;top:0;margin:0 5px}</style><div class="navbar-header">Third-placed teams<br />advance from groups<style data-mw-deduplicate="TemplateStyles:r1333133064">.mw-parser-output .hlist dl,.mw-parser-output .hlist ol,.mw-parser-output .hlist ul{margin:0;padding:0}.mw-parser-output .hlist dd,.mw-parser-output .hlist dt,.mw-parser-output .hlist li{margin:0;display:inline}.mw-parser-output .hlist.inline,.mw-parser-output .hlist.inline dl,.mw-parser-output .hlist.inline ol,.mw-parser-output .hlist.inline ul,.mw-parser-output .hlist dl dl,.mw-parser-output .hlist dl ol,.mw-parser-output .hlist dl ul,.mw-parser-output .hlist ol dl,.mw-parser-output .hlist ol ol,.mw-parser-output .hlist ol ul,.mw-parser-output .hlist ul dl,.mw-parser-output .hlist ul ol,.mw-parser-output .hlist ul ul{display:inline}.mw-parser-output .hlist .mw-empty-li{display:none}.mw-parser-output .hlist dt::after{content:": "}.mw-parser-output .hlist dd::after,.mw-parser-output .hlist li::after{content:"\a0 · ";font-weight:bold}.mw-parser-output .hlist dd:last-child::after,.mw-parser-output .hlist dt:last-child::after,.mw-parser-output .hlist li:last-child::after{content:none}.mw-parser-output .hlist dd dd:first-child::before,.mw-parser-output .hlist dd dt:first-child::before,.mw-parser-output .hlist dd li:first-child::before,.mw-parser-output .hlist dt dd:first-child::before,.mw-parser-output .hlist dt dt:first-child::before,.mw-parser-output .hlist dt li:first-child::before,.mw-parser-output .hlist li dd:first-child::before,.mw-parser-output .hlist li dt:first-child::before,.mw-parser-output .hlist li li:first-child::before{content:" (";font-weight:normal}.mw-parser-output .hlist dd dd:last-child::after,.mw-parser-output .hlist dd dt:last-child::after,.mw-parser-output .hlist dd li:last-child::after,.mw-parser-output .hlist dt dd:last-child::after,.mw-parser-output .hlist dt dt:last-child::after,.mw-parser-output .hlist dt li:last-child::after,.mw-parser-output .hlist li dd:last-child::after,.mw-parser-output .hlist li dt:last-child::after,.mw-parser-output .hlist li li:last-child::after{content:")";font-weight:normal}.mw-parser-output .hlist ol{counter-reset:listitem}.mw-parser-output .hlist ol>li{counter-increment:listitem}.mw-parser-output .hlist ol>li::before{content:" "counter(listitem)"\a0 "}.mw-parser-output .hlist dd ol>li:first-child::before,.mw-parser-output .hlist dt ol>li:first-child::before,.mw-parser-output .hlist li ol>li:first-child::before{content:" ("counter(listitem)"\a0 "}</style><style data-mw-deduplicate="TemplateStyles:r1239400231">.mw-parser-output .navbar{display:inline;font-size:88%;font-weight:normal}.mw-parser-output .navbar-collapse{float:left;text-align:left}.mw-parser-output .navbar-boxtext{word-spacing:0}.mw-parser-output .navbar ul{display:inline-block;white-space:nowrap;line-height:inherit}.mw-parser-output .navbar-brackets::before{margin-right:-0.125em;content:"[ "}.mw-parser-output .navbar-brackets::after{margin-left:-0.125em;content:" ]"}.mw-parser-output .navbar li{word-spacing:-0.125em}.mw-parser-output .navbar a>span,.mw-parser-output .navbar a>abbr{text-decoration:inherit}.mw-parser-output .navbar-mini abbr{font-variant:small-caps;border-bottom:none;text-decoration:none;cursor:inherit}.mw-parser-output .navbar-ct-full{font-size:114%;margin:0 7em}.mw-parser-output .navbar-ct-mini{font-size:114%;margin:0 4em}html.skin-theme-clientpref-night .mw-parser-output .navbar li a abbr{color:var(--color-base)!important}@media(prefers-color-scheme:dark){html.skin-theme-clientpref-os .mw-parser-output .navbar li a abbr{color:var(--color-base)!important}}@media print{.mw-parser-output .navbar{display:none!important}}</style><div class="navbar plainlinks hlist navbar-mini"><ul><li class="nv-view"><a class="mw-selflink selflink"><abbr title="View this template">v</abbr></a></li><li class="nv-talk"><a href="/wiki/Template_talk:2026_FIFA_World_Cup_third-place_table" class="mw-redirect" title="Template talk:2026 FIFA World Cup third-place table"><abbr title="Discuss this template">t</abbr></a></li><li class="nv-edit"><a href="/wiki/Special:EditPage/Template:2026_FIFA_World_Cup_third-place_table" title="Special:EditPage/Template:2026 FIFA World Cup third-place table"><abbr title="Edit this template">e</abbr></a></li></ul></div></div>
</th>
<th scope="col" class="unsortable">
</th>
<th scope="col" style="width:2em" class="unsortable">1A<br />vs
</th>
<th scope="col" style="width:2em" class="unsortable">1B<br />vs
</th>
<th scope="col" style="width:2em" class="unsortable">1D<br />vs
</th>
<th scope="col" style="width:2em" class="unsortable">1E<br />vs
</th>
<th scope="col" style="width:2em" class="unsortable">1G<br />vs
</th>
<th scope="col" style="width:2em" class="unsortable">1I<br />vs
</th>
<th scope="col" style="width:2em" class="unsortable">1K<br />vs
</th>
<th scope="col" style="width:2em" class="unsortable">1L<br />vs
</th></tr>
<tr>
<th scope="row">1
</th>
<td></td>
<td></td>
<td></td>
<td></td>
<td><b>E</b></td>
<td><b>F</b></td>
<td><b>G</b></td>
<td><b>H</b></td>
<td><b>I</b></td>
<td><b>J</b></td>
<td><b>K</b></td>
<td><b>L</b>
</td>
<th rowspan="495">
</th>
<td>3E</td>
<td>3J</td>
<td>3I</td>
<td>3F</td>
<td>3H</td>
<td>3G</td>
<td>3L</td>
<td>3K
</td></tr>
<tr>
<th scope="row">2
</th>
<td></td>
<td></td>
<td></td>
<td><b>D</b></td>
<td></td>
<td><b>F</b></td>
<td><b>G</b></td>
<td><b>H</b></td>
<td><b>I</b></td>
<td><b>J</b></td>
<td><b>K</b></td>
<td><b>L</b></td>
<td>3H</td>
<td>3G</td>
<td>3I</td>
<td>3D</td>
<td>3J</td>
<td>3F</td>
<td>3L</td>
<td>3K
</td></tr>
<tr>
<th scope="row">3
</th>
<td></td>
<td></td>
<td></td>
<td><b>D</b></td>
<td><b>E</b></td>
<td></td>
<td><b>G</b></td>
<td><b>H</b></td>
<td><b>I</b></td>
<td><b>J</b></td>
<td><b>K</b></td>
<td><b>L</b></td>
<td>3E</td>
<td>3J</td>
<td>3I</td>
<td>3D</td>
<td>3H</td>
<td>3G</td>
<td>3L</td>
<td>3K
</td></tr>
<tr>
<th scope="row">4
</th>
<td></td>
<td></td>
<td></td>
<td><b>D</b></td>
<td><b>E</b></td>
<td><b>F</b></td>
<td></td>
<td><b>H</b></td>
<td><b>I</b></td>
<td><b>J</b></td>
<td><b>K</b></td>
<td><b>L</b></td>
<td>3E</td>
<td>3J</td>
<td>3I</td>
<td>3D</td>
<td>3H</td>
<td>3F</td>
<td>3L</td>
<td>3K
</td></tr>
<tr>
<th scope="row">5
</th>
<td></td>
<td></td>
<td></td>
<td><b>D</b></td>
<td><b>E</b></td>
<td><b>F</b></td>
<td><b>G</b></td>
<td></td>

...168050 bytes truncated...

The tool call succeeded but the output was truncated. Full output saved to: C:\Users\santi\.local\share\opencode\tool-output\tool_efa1b7cab001yobySO15yOV2G7
Use the Task tool to have explore agent process this file with Grep and Read (with offset/limit). Do NOT read the full file yourself - delegate to save context.
```

---

## Assistant (Build · Nemotron 3 Ultra Free · 141.6s)

_Thinking:_

The Wikipedia page has the full 495-row table in HTML format. I need to parse this to extract the Annex C data. Let me write a script to extract this data programmatically. But since the output was truncated, I need to fetch it differently or write a Python script to parse the table.

Let me create a Python script to fetch and parse the Wikipedia table.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /Users/santi/Desktop/prediccion-mundial && python3 << 'EOF'\nimport requests\nfrom bs4 import BeautifulSoup\nimport json\n\nurl = \"https://en.wikipedia.org/wiki/Template:2026_FIFA_World_Cup_third-place_table\"\nresponse = requests.get(url)\nsoup = BeautifulSoup(response.content, 'html.parser')\n\n# Find the main table\ntable = soup.find('table', class_='wikitable')\nif not table:\n    print(\"Table not found\")\n    exit(1)\n\nrows = table.find_all('tr')\nprint(f\"Total rows: {len(rows)}\")\n\n# Parse header to understand structure\nheader_row = rows[0]\nheaders = [th.get_text(strip=True) for th in header_row.find_all(['th', 'td'])]\nprint(f\"Headers: {headers}\")\n\n# The columns we care about:\n# No., then 12 group columns (A-L), then 8 match columns (1A vs, 1B vs, 1D vs, 1E vs, 1G vs, 1I vs, 1K vs, 1L vs)\n# So each row should have: No. + 12 groups + 8 matches = 21 columns\n\nannex_c_map = {}\n\nfor i, row in enumerate(rows[1:], 1):  # Skip header\n    cells = row.find_all(['td', 'th'])\n    if len(cells) < 21:\n        continue\n    \n    row_num = cells[0].get_text(strip=True)\n    if not row_num.isdigit():\n        continue\n    \n    # Columns 1-12 are the qualifying groups (A-L)\n    # Empty cell = group's 3rd place team does NOT qualify\n    # Bold letter = group's 3rd place team DOES qualify\n    qualifying_groups = []\n    for j in range(1, 13):  # columns 1-12 for groups A-L\n        cell_text = cells[j].get_text(strip=True)\n        if cell_text and cell_text.isalpha() and len(cell_text) == 1:\n            qualifying_groups.append(cell_text)\n    \n    # Columns 13-20 are the 8 match assignments (1A vs, 1B vs, 1D vs, 1E vs, 1G vs, 1I vs, 1K vs, 1L vs)\n    match_assignments = []\n    for j in range(13, 21):  # columns 13-20\n        cell_text = cells[j].get_text(strip=True)\n        if cell_text and cell_text.startswith('3'):\n            # Extract the group letter (e.g., \"3E\" -> \"E\")\n            match_assignments.append(cell_text[1])\n        else:\n            match_assignments.append(None)\n    \n    if len(qualifying_groups) == 8 and len(match_assignments) == 8:\n        key = frozenset(qualifying_groups)\n        annex_c_map[key] = tuple(match_assignments)\n    else:\n        print(f\"Row {row_num}: qualifying={len(qualifying_groups)}, matches={len(match_assignments)}\")\n\nprint(f\"Total combinations extracted: {len(annex_c_map)}\")\n\n# Save to JSON\nwith open('annex_c_data.json', 'w') as f:\n    # Convert frozenset keys to sorted strings for JSON serialization\n    json_map = {tuple(sorted(k)): v for k, v in annex_c_map.items()}\n    json.dump(json_map, f, indent=2)\n\nprint(\"Saved to annex_c_data.json\")\n\n# Verify a few entries\nfor key, val in list(annex_c_map.items())[:5]:\n    print(f\"  {sorted(key)} -> {val}\")\nEOF",
  "description": "Extract Annex C 495 combinations from Wikipedia"
}
```

**Output:**
```
/usr/bin/bash: line 1: cd: /Users/santi/Desktop/prediccion-mundial: No such file or directory

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 12.3s)

---

## User

corre ese comando para que guarde el .json en ./data

---

## Assistant (Build · Nemotron 3 Ultra Free · 127.3s)

_Thinking:_

The user wants me to run the command but save the JSON in ./data. Let me adjust the path and run it from the correct working directory.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /Users/santi/Desktop/prediccion-mundial && python3 << 'EOF'\nimport requests\nfrom bs4 import BeautifulSoup\nimport json\n\nurl = \"https://en.wikipedia.org/wiki/Template:2026_FIFA_World_Cup_third-place_table\"\nresponse = requests.get(url)\nsoup = BeautifulSoup(response.content, 'html.parser')\n\n# Find the main table\ntable = soup.find('table', class_='wikitable')\nif not table:\n    print(\"Table not found\")\n    exit(1)\n\nrows = table.find_all('tr')\nprint(f\"Total rows: {len(rows)}\")\n\n# Parse header to understand structure\nheader_row = rows[0]\nheaders = [th.get_text(strip=True) for th in header_row.find_all(['th', 'td'])]\nprint(f\"Headers: {headers}\")\n\nannex_c_map = {}\n\nfor i, row in enumerate(rows[1:], 1):  # Skip header\n    cells = row.find_all(['td', 'th'])\n    if len(cells) < 21:\n        continue\n    \n    row_num = cells[0].get_text(strip=True)\n    if not row_num.isdigit():\n        continue\n    \n    # Columns 1-12 are the qualifying groups (A-L)\n    qualifying_groups = []\n    for j in range(1, 13):  # columns 1-12 for groups A-L\n        cell_text = cells[j].get_text(strip=True)\n        if cell_text and cell_text.isalpha() and len(cell_text) == 1:\n            qualifying_groups.append(cell_text)\n    \n    # Columns 13-20 are the 8 match assignments\n    match_assignments = []\n    for j in range(13, 21):  # columns 13-20\n        cell_text = cells[j].get_text(strip=True)\n        if cell_text and cell_text.startswith('3'):\n            match_assignments.append(cell_text[1])\n        else:\n            match_assignments.append(None)\n    \n    if len(qualifying_groups) == 8 and len(match_assignments) == 8:\n        key = frozenset(qualifying_groups)\n        annex_c_map[key] = tuple(match_assignments)\n    else:\n        print(f\"Row {row_num}: qualifying={len(qualifying_groups)}, matches={len(match_assignments)}\")\n\nprint(f\"Total combinations extracted: {len(annex_c_map)}\")\n\n# Save to JSON in ./data\nwith open('data/annex_c_data.json', 'w') as f:\n    json_map = {tuple(sorted(k)): v for k, v in annex_c_map.items()}\n    json.dump(json_map, f, indent=2)\n\nprint(\"Saved to data/annex_c_data.json\")\n\n# Verify a few entries\nfor key, val in list(annex_c_map.items())[:5]:\n    print(f\"  {sorted(key)} -> {val}\")\nEOF",
  "description": "Extract Annex C 495 combinations from Wikipedia"
}
```

**Output:**
```
/usr/bin/bash: line 1: cd: /Users/santi/Desktop/prediccion-mundial: No such file or directory

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 16.6s)

_Thinking:_

The path seems to be different. Let me check what the correct working directory is.

**Tool: bash**

**Input:**
```json
{
  "command": "pwd",
  "description": "Check current working directory"
}
```

**Output:**
```
/c/Users/santi/Desktop/prediccion-mundial

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 48.1s)

_Thinking:_

Ah, it's a Windows path but using a different format. Let me use the correct path.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /c/Users/santi/Desktop/prediccion-mundial && python3 << 'EOF'\nimport requests\nfrom bs4 import BeautifulSoup\nimport json\n\nurl = \"https://en.wikipedia.org/wiki/Template:2026_FIFA_World_Cup_third-place_table\"\nresponse = requests.get(url)\nsoup = BeautifulSoup(response.content, 'html.parser')\n\ntable = soup.find('table', class_='wikitable')\nif not table:\n    print(\"Table not found\")\n    exit(1)\n\nrows = table.find_all('tr')\nprint(f\"Total rows: {len(rows)}\")\n\nannex_c_map = {}\n\nfor i, row in enumerate(rows[1:], 1):\n    cells = row.find_all(['td', 'th'])\n    if len(cells) < 21:\n        continue\n    \n    row_num = cells[0].get_text(strip=True)\n    if not row_num.isdigit():\n        continue\n    \n    qualifying_groups = []\n    for j in range(1, 13):\n        cell_text = cells[j].get_text(strip=True)\n        if cell_text and cell_text.isalpha() and len(cell_text) == 1:\n            qualifying_groups.append(cell_text)\n    \n    match_assignments = []\n    for j in range(13, 21):\n        cell_text = cells[j].get_text(strip=True)\n        if cell_text and cell_text.startswith('3'):\n            match_assignments.append(cell_text[1])\n        else:\n            match_assignments.append(None)\n    \n    if len(qualifying_groups) == 8 and len(match_assignments) == 8:\n        key = frozenset(qualifying_groups)\n        annex_c_map[key] = tuple(match_assignments)\n    else:\n        print(f\"Row {row_num}: qualifying={len(qualifying_groups)}, matches={len(match_assignments)}\")\n\nprint(f\"Total combinations extracted: {len(annex_c_map)}\")\n\nwith open('data/annex_c_data.json', 'w') as f:\n    json_map = {tuple(sorted(k)): v for k, v in annex_c_map.items()}\n    json.dump(json_map, f, indent=2)\n\nprint(\"Saved to data/annex_c_data.json\")\n\nfor key, val in list(annex_c_map.items())[:5)[:5]:\n    print(f\"  {sorted(key)} -> {val}\")\nEOF",
  "description": "Extract Annex C 495 combinations from Wikipedia"
}
```

**Output:**
```
(no output)
```

---

## Assistant (Build · Nemotron 3 Ultra Free · 13.5s)

_Thinking:_

The command seems to have run but with no output. Let me check if it ran correctly and if the file was created.

**Tool: bash**

**Input:**
```json
{
  "command": "ls -la /c/Users/santi/Desktop/prediccion-mundial/data/annex_c_data.json",
  "description": "Check if annex_c_data.json was created"
}
```

**Output:**
```
ls: cannot access '/c/Users/santi/Desktop/prediccion-mundial/data/annex_c_data.json': No such file or directory

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 49.2s)

_Thinking:_

The script didn't produce output. Let me try running it differently.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /c/Users/santi/Desktop/prediccion-mundial && python3 -c \"\nimport requests\nfrom bs4 import BeautifulSoup\nimport json\n\nurl = 'https://en.wikipedia.org/wiki/Template:2026_FIFA_World_Cup_third-place_table'\nresponse = requests.get(url)\nsoup = BeautifulSoup(response.content, 'html.parser')\n\ntable = soup.find('table', class_='wikitable')\nrows = table.find_all('tr')\nprint(f'Total rows: {len(rows)}')\n\nannex_c_map = {}\n\nfor i, row in enumerate(rows[1:], 1):\n    cells = row.find_all(['td', 'th'])\n    if len(cells) < 21:\n        continue\n    \n    row_num = cells[0].get_text(strip=True)\n    if not row_num.isdigit():\n        continue\n    \n    qualifying_groups = []\n    for j in range(1, 13):\n        cell_text = cells[j].get_text(strip=True)\n        if cell_text and cell_text.isalpha() and len(cell_text) == 1:\n            qualifying_groups.append(cell_text)\n    \n    match_assignments = []\n    for j in range(13, 21):\n        cell_text = cells[j].get_text(strip=True)\n        if cell_text and cell_text.startswith('3'):\n            match_assignments.append(cell_text[1])\n        else:\n            match_assignments.append(None)\n    \n    if len(qualifying_groups) == 8 and len(match_assignments) == 8:\n        key = frozenset(qualifying_groups)\n        annex_c_map[key] = tuple(match_assignments)\n    else:\n        print(f'Row {row_num}: qualifying={len(qualifying_groups)}, matches={len(match_assignments)}')\n\nprint(f'Total combinations extracted: {len(annex_c_map)}')\n\nwith open('data/annex_c_data.json', 'w') as f:\n    json_map = {tuple(sorted(k)): v for k, v in annex_c_map.items()}\n    json.dump(json_map, f, indent=2)\n\nprint('Saved to data/annex_c_data.json')\n\nfor key, val in list(annex_c_map.items())[:5]:\n    print(f'  {sorted(key)} -> {val}')\n\"",
  "description": "Extract Annex C 495 combinations from Wikipedia"
}
```

**Output:**
```
no se encontr� Python; ejecutar sin argumentos para instalar desde el Microsoft Store o deshabilitar este acceso directo desde Configuraci�n > Aplicaciones > Configuraci�n avanzada de aplicaciones > Alias de ejecuci�n de aplicaciones.

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 49.1s)

_Thinking:_

Python is not available in the bash shell. Let me try using the Python from the virtual environment or find another way to run this.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /c/Users/santi/Desktop/prediccion-mundial && .venv/Scripts/python.exe -c \"\nimport requests\nfrom bs4 import BeautifulSoup\nimport json\n\nurl = 'https://en.wikipedia.org/wiki/Template:2026_FIFA_World_Cup_third-place_table'\nresponse = requests.get(url)\nsoup = BeautifulSoup(response.content, 'html.parser')\n\ntable = soup.find('table', class_='wikitable')\nrows = table.find_all('tr')\nprint(f'Total rows: {len(rows)}')\n\nannex_c_map = {}\n\nfor i, row in enumerate(rows[1:], 1):\n    cells = row.find_all(['td', 'th'])\n    if len(cells) < 21:\n        continue\n    \n    row_num = cells[0].get_text(strip=True)\n    if not row_num.isdigit():\n        continue\n    \n    qualifying_groups = []\n    for j in range(1, 13):\n        cell_text = cells[j].get_text(strip=True)\n        if cell_text and cell_text.isalpha() and len(cell_text) == 1:\n            qualifying_groups.append(cell_text)\n    \n    match_assignments = []\n    for j in range(13, 21):\n        cell_text = cells[j].get_text(strip=True)\n        if cell_text and cell_text.startswith('3'):\n            match_assignments.append(cell_text[1])\n        else:\n            match_assignments.append(None)\n    \n    if len(qualifying_groups) == 8 and len(match_assignments) == 8:\n        key = frozenset(qualifying_groups)\n        annex_c_map[key] = tuple(match_assignments)\n    else:\n        print(f'Row {row_num}: qualifying={len(qualifying_groups)}, matches={len(match_assignments)}')\n\nprint(f'Total combinations extracted: {len(annex_c_map)}')\n\nwith open('data/annex_c_data.json', 'w') as f:\n    json_map = {tuple(sorted(k)): v for k, v in annex_c_map.items()}\n    json.dump(json_map, f, indent=2)\n\nprint('Saved to data/annex_c_data.json')\n\nfor key, val in list(annex_c_map.items())[:5]:\n    print(f'  {sorted(key)} -> {val}')\n\"",
  "description": "Extract Annex C 495 combinations using venv python"
}
```

**Output:**
```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 20.5s)

_Thinking:_

The venv doesn't have requests and beautifulsoup4 installed. Let me install them first.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /c/Users/santi/Desktop/prediccion-mundial && .venv/Scripts/pip.exe install requests beautifulsoup4",
  "description": "Install required packages"
}
```

**Output:**
```
Collecting requests
  Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.15.0-py3-none-any.whl.metadata (3.8 kB)
Collecting charset_normalizer<4,>=2 (from requests)
  Downloading charset_normalizer-3.4.7-cp313-cp313-win_amd64.whl.metadata (41 kB)
Collecting idna<4,>=2.5 (from requests)
  Downloading idna-3.18-py3-none-any.whl.metadata (6.1 kB)
Collecting urllib3<3,>=1.26 (from requests)
  Downloading urllib3-2.7.0-py3-none-any.whl.metadata (6.9 kB)
Collecting certifi>=2023.5.7 (from requests)
  Downloading certifi-2026.6.17-py3-none-any.whl.metadata (2.5 kB)
Collecting soupsieve>=1.6.1 (from beautifulsoup4)
  Downloading soupsieve-2.8.4-py3-none-any.whl.metadata (4.6 kB)
Collecting typing-extensions>=4.0.0 (from beautifulsoup4)
  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Downloading requests-2.34.2-py3-none-any.whl (73 kB)
Downloading charset_normalizer-3.4.7-cp313-cp313-win_amd64.whl (158 kB)
Downloading idna-3.18-py3-none-any.whl (65 kB)
Downloading urllib3-2.7.0-py3-none-any.whl (131 kB)
Downloading beautifulsoup4-4.15.0-py3-none-any.whl (109 kB)
Downloading certifi-2026.6.17-py3-none-any.whl (133 kB)
Downloading soupsieve-2.8.4-py3-none-any.whl (37 kB)
Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Installing collected packages: urllib3, typing-extensions, soupsieve, idna, charset_normalizer, certifi, requests, beautifulsoup4

Successfully installed beautifulsoup4-4.15.0 certifi-2026.6.17 charset_normalizer-3.4.7 idna-3.18 requests-2.34.2 soupsieve-2.8.4 typing-extensions-4.15.0 urllib3-2.7.0

[notice] A new release of pip is available: 25.2 -> 26.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 91.7s)

_Thinking:_

Now let me run the extraction script again.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /c/Users/santi/Desktop/prediccion-mundial && .venv/Scripts/python.exe -c \"\nimport requests\nfrom bs4 import BeautifulSoup\nimport json\n\nurl = 'https://en.wikipedia.org/wiki/Template:2026_FIFA_World_Cup_third-place_table'\nresponse = requests.get(url)\nsoup = BeautifulSoup(response.content, 'html.parser')\n\ntable = soup.find('table', class_='wikitable')\nrows = table.find_all('tr')\nprint(f'Total rows: {len(rows)}')\n\nannex_c_map = {}\n\nfor i, row in enumerate(rows[1:], 1):\n    cells = row.find_all(['td', 'th'])\n    if len(cells) < 21:\n        continue\n    \n    row_num = cells[0].get_text(strip=True)\n    if not row_num.isdigit():\n        continue\n    \n    qualifying_groups = []\n    for j in range(1, 13):\n        cell_text = cells[j].get_text(strip=True)\n        if cell_text and cell_text.isalpha() and len(cell_text) == 1:\n            qualifying_groups.append(cell_text)\n    \n    match_assignments = []\n    for j in range(13, 21):\n        cell_text = cells[j].get_text(strip=True)\n        if cell_text and cell_text.startswith('3'):\n            match_assignments.append(cell_text[1])\n        else:\n            match_assignments.append(None)\n    \n    if len(qualifying_groups) == 8 and len(match_assignments) == 8:\n        key = frozenset(qualifying_groups)\n        annex_c_map[key] = tuple(match_assignments)\n    else:\n        print(f'Row {row_num}: qualifying={len(qualifying_groups)}, matches={len(match_assignments)}')\n\nprint(f'Total combinations extracted: {len(annex_c_map)}')\n\nwith open('data/annex_c_data.json', 'w') as f:\n    json_map = {tuple(sorted(k)): v for k, v in annex_c_map.items()}\n    json.dump(json_map, f, indent=2)\n\nprint('Saved to data/annex_c_data.json')\n\nfor key, val in list(annex_c_map.items())[:5]:\n    print(f'  {sorted(key)} -> {val}')\n\"",
  "description": "Extract Annex C 495 combinations"
}
```

**Output:**
```
Traceback (most recent call last):
  File "<string>", line 11, in <module>
    rows = table.find_all('tr')
           ^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'find_all'

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 67.8s)

_Thinking:_

The table wasn't found. The Wikipedia page might need different parsing. Let me try to find the correct table.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /c/Users/santi/Desktop/prediccion-mundial && .venv/Scripts/python.exe -c \"\nimport requests\nfrom bs4 import BeautifulSoup\n\nurl = 'https://en.wikipedia.org/wiki/Template:2026_FIFA_World_Cup_third-place_table'\nresponse = requests.get(url)\nsoup = BeautifulSoup(response.content, 'html.parser')\n\n# Find all tables\ntables = soup.find_all('table', class_='wikitable')\nprint(f'Found {len(tables)} wikitable tables')\n\nfor i, t in enumerate(tables):\n    rows = t.find_all('tr')\n    print(f'Table {i}: {len(rows)} rows')\n    # Print first few cells of first row\n    if rows:\n        cells = rows[0].find_all(['th', 'td'])\n        print(f'  First row cells: {[c.get_text(strip=True)[:20] for c in cells[:10]]}')\n\"",
  "description": "Find correct table on Wikipedia page"
}
```

**Output:**
```
Found 0 wikitable tables

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 19.8s)

_Thinking:_

No wikitable tables found. The page might be using different CSS classes or the content might be loaded dynamically. Let me check the raw HTML to find the table.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /c/Users/santi/Desktop/prediccion-mundial && .venv/Scripts/python.exe -c \"\nimport requests\nfrom bs4 import BeautifulSoup\n\nurl = 'https://en.wikipedia.org/wiki/Template:2026_FIFA_World_Cup_third-place_table'\nresponse = requests.get(url)\nsoup = BeautifulSoup(response.content, 'html.parser')\n\n# Find all tables\ntables = soup.find_all('table')\nprint(f'Found {len(tables)} tables')\n\nfor i, t in enumerate(tables[:5]):\n    rows = t.find_all('tr')\n    print(f'Table {i}: {len(rows)} rows, classes: {t.get(\\\"class\\\", [])}')\n    if rows:\n        cells = rows[0].find_all(['th', 'td'])\n        print(f'  First row: {[c.get_text(strip=True)[:30] for c in cells[:15]]}')\n\"",
  "description": "Find all tables on Wikipedia page"
}
```

**Output:**
```
Found 0 tables

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 35.2s)

_Thinking:_

No tables found at all. The content might be loaded via JavaScript or the page might be a template page that doesn't have the table directly. Let me try to get the page source directly or use the Wikipedia API.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /c/Users/santi/Desktop/prediccion-mundial && .venv/Scripts/python.exe -c \"\nimport requests\n\nurl = 'https://en.wikipedia.org/wiki/Template:2026_FIFA_World_Cup_third-place_table'\nresponse = requests.get(url)\nprint(f'Status: {response.status_code}')\nprint(f'Content length: {len(response.text)}')\n# Check if it's a template page that has different content\nif 'wikitable' in response.text:\n    print('Contains wikitable')\nelse:\n    print('Does NOT contain wikitable')\n# Print first 5000 chars\nprint(response.text[:5000])\n\"",
  "description": "Check raw HTML of Wikipedia page"
}
```

**Output:**
```
Status: 403
Content length: 126
Does NOT contain wikitable
Please set a user-agent and respect our robot policy https://w.wiki/4wJS. See also https://phabricator.wikimedia.org/T400119.


```

---

## Assistant (Build · Nemotron 3 Ultra Free · 13.3s)

---

## User

https://digitalhub.fifa.com/m/6b719d76a2e3a44d/original/FWC2026_regulations_ES.pdf

ahi tenes la matriz con las combinaciones de los cruces de los mejores 3eros, en el anexo c casi al final del pdf

---

## Assistant (Build · Nemotron 3 Ultra Free · 44.2s)

_Thinking:_

The user provided a link to the official FIFA regulations PDF in Spanish that contains the Annex C matrix with the 495 combinations. Let me download and parse this PDF to extract the Annex C data.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /c/Users/santi/Desktop/prediccion-mundial && .venv/Scripts/pip.exe install pdfplumber",
  "description": "Install PDF parser"
}
```

**Output:**
```
Collecting pdfplumber
  Downloading pdfplumber-0.11.10-py3-none-any.whl.metadata (43 kB)
Collecting pdfminer.six==20260107 (from pdfplumber)
  Downloading pdfminer_six-20260107-py3-none-any.whl.metadata (4.3 kB)
Collecting Pillow>=12.2.0 (from pdfplumber)
  Using cached pillow-12.2.0-cp313-cp313-win_amd64.whl.metadata (9.0 kB)
Collecting pypdfium2>=5.9.0 (from pdfplumber)
  Downloading pypdfium2-5.10.1-py3-none-win_amd64.whl.metadata (70 kB)
Requirement already satisfied: charset-normalizer>=2.0.0 in c:\users\santi\desktop\prediccion-mundial\.venv\lib\site-packages (from pdfminer.six==20260107->pdfplumber) (3.4.7)
Collecting cryptography>=36.0.0 (from pdfminer.six==20260107->pdfplumber)
  Downloading cryptography-49.0.0-cp311-abi3-win_amd64.whl.metadata (4.3 kB)
Collecting cffi>=2.0.0 (from cryptography>=36.0.0->pdfminer.six==20260107->pdfplumber)
  Using cached cffi-2.0.0-cp313-cp313-win_amd64.whl.metadata (2.6 kB)
Collecting pycparser (from cffi>=2.0.0->cryptography>=36.0.0->pdfminer.six==20260107->pdfplumber)
  Using cached pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
Downloading pdfplumber-0.11.10-py3-none-any.whl (60 kB)
Downloading pdfminer_six-20260107-py3-none-any.whl (6.6 MB)
   ---------------------------------------- 6.6/6.6 MB 517.5 kB/s  0:00:12
Downloading cryptography-49.0.0-cp311-abi3-win_amd64.whl (3.8 MB)
   ---------------------------------------- 3.8/3.8 MB 3.1 MB/s  0:00:01
Using cached cffi-2.0.0-cp313-cp313-win_amd64.whl (183 kB)
Using cached pillow-12.2.0-cp313-cp313-win_amd64.whl (7.1 MB)
Downloading pypdfium2-5.10.1-py3-none-win_amd64.whl (3.8 MB)
   ---------------------------------------- 3.8/3.8 MB 2.4 MB/s  0:00:01
Using cached pycparser-3.0-py3-none-any.whl (48 kB)
Installing collected packages: pypdfium2, pycparser, Pillow, cffi, cryptography, pdfminer.six, pdfplumber

Successfully installed Pillow-12.2.0 cffi-2.0.0 cryptography-49.0.0 pdfminer.six-20260107 pdfplumber-0.11.10 pycparser-3.0 pypdfium2-5.10.1

[notice] A new release of pip is available: 25.2 -> 26.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 35.7s)

_Thinking:_

Now let me download the PDF and extract the Annex C data.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /c/Users/santi/Desktop/prediccion-mundial && .venv/Scripts/python.exe -c \"\nimport requests\n\nurl = 'https://digitalhub.fifa.com/m/6b719d76a2e3a44d/original/FWC2026_regulations_ES.pdf'\nresponse = requests.get(url)\nwith open('data/FWC2026_regulations_ES.pdf', 'wb') as f:\n    f.write(response.content)\nprint(f'Downloaded {len(response.content)} bytes')\n\"",
  "description": "Download FIFA regulations PDF"
}
```

**Output:**
```
Downloaded 1066517 bytes

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 41.9s)

_Thinking:_

Now let me extract the Annex C table from the PDF. I need to find the pages that contain the 495 combinations table.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /c/Users/santi/Desktop/prediccion-mundial && .venv/Scripts/python.exe -c \"\nimport pdfplumber\n\npdf = pdfplumber.open('data/FWC2026_regulations_ES.pdf')\nprint(f'Total pages: {len(pdf.pages)}')\n\n# Search for Annex C / Anexo C\nfor i, page in enumerate(pdf.pages):\n    text = page.extract_text()\n    if text and ('anexo c' in text.lower() or 'annex c' in text.lower() or '495' in text):\n        print(f'Page {i+1}: Contains Annex C / 495 reference')\n        # Print first 500 chars\n        print(text[:500])\n        print('---')\n\"",
  "description": "Find Annex C pages in PDF"
}
```

**Output:**
```
Total pages: 99
Page 24: Contains Annex C / 495 reference
24
(12) M84 Ganadora H (1H) � Segunda J (2J) = Ganadora (12) M84 (W84)
Mejor tercera de
(13) M85 Ganadora B (1B) � = Ganadora (13) M85 (W85)
EFGIJ
(14) M86 Ganadora J (1J) � Segunda H (2H) = Ganadora (14) M86 (W86)
Mejor tercera de
(15) M87 Ganadora K (1K) � = Ganadora (15) M87 (W87)
DEIJL
(16) M88 Segunda D (2D) � Segunda G (2G) = Ganadora (16) M88 (W88)
Nota: esta configuraci�n de partidos para dieciseisavos de final no sigue
necesariamente el orden cronol�gico en el que se disputar�n los encu
---
Page 98: Contains Annex C / 495 reference
98
483 3C 3J 3B 3D 3A 3F 3E 3K
484 3C 3E 3B 3D 3A 3F 3L 3I
485 3C 3E 3B 3D 3A 3F 3I 3K
486 3C 3J 3B 3D 3A 3F 3E 3I
487 3H 3F 3B 3C 3A 3D 3L 3E
488 3H 3E 3B 3C 3A 3F 3D 3K
489 3H 3J 3B 3C 3A 3F 3D 3E
490 3H 3E 3B 3C 3A 3F 3D 3I
491 3C 3G 3B 3D 3A 3F 3L 3E
492 3C 3G 3B 3D 3A 3F 3E 3K
493 3C 3G 3B 3D 3A 3F 3E 3J
494 3C 3G 3B 3D 3A 3F 3E 3I
495 3H 3G 3B 3C 3A 3F 3D 3E
---

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 47.2s)

_Thinking:_

The Annex C table starts on page 98 (0-indexed: page 97). Let me extract the full table from the PDF pages that contain the 495 combinations. It seems like the table might span multiple pages. Let me look at pages around 97-98 and also earlier pages.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /c/Users/santi/Desktop/prediccion-mundial && .venv/Scripts/python.exe -c \"\nimport pdfplumber\n\npdf = pdfplumber.open('data/FWC2026_regulations_ES.pdf')\n\n# Check pages around 80-99 for the full table\nfor i in range(80, 99):\n    page = pdf.pages[i]\n    text = page.extract_text()\n    if text and ('3A' in text or '3B' in text or '3C' in text):\n        print(f'Page {i+1}:')\n        print(text[:1000])\n        print('---')\n\"",
  "description": "Find Annex C table pages"
}
```

**Output:**
```
Page 81:
soxenA
81
C .
ANEXO
COMBINACIONES DE
LAS OCHO MEJORES
TERCERAS
Opci�n 1A 1B 1D 1E 1G 1I 1K 1L
1 3E 3J 3I 3F 3H 3G 3L 3K
2 3H 3G 3I 3D 3J 3F 3L 3K
3 3E 3J 3I 3D 3H 3G 3L 3K
4 3E 3J 3I 3D 3H 3F 3L 3K
5 3E 3G 3I 3D 3J 3F 3L 3K
6 3E 3G 3J 3D 3H 3F 3L 3K
7 3E 3G 3I 3D 3H 3F 3L 3K
8 3E 3G 3J 3D 3H 3F 3L 3I
9 3E 3G 3J 3D 3H 3F 3I 3K
10 3H 3G 3I 3C 3J 3F 3L 3K
11 3E 3J 3I 3C 3H 3G 3L 3K
12 3E 3J 3I 3C 3H 3F 3L 3K
13 3E 3G 3I 3C 3J 3F 3L 3K
14 3E 3G 3J 3C 3H 3F 3L 3K
15 3E 3G 3I 3C 3H 3F 3L 3K
16 3E 3G 3J 3C 3H 3F 3L 3I
17 3E 3G 3J 3C 3H 3F 3I 3K
18 3H 3G 3I 3C 3J 3D 3L 3K
---
Page 82:
82
19 3C 3J 3I 3D 3H 3F 3L 3K
20 3C 3G 3I 3D 3J 3F 3L 3K
21 3C 3G 3J 3D 3H 3F 3L 3K
22 3C 3G 3I 3D 3H 3F 3L 3K
23 3C 3G 3J 3D 3H 3F 3L 3I
24 3C 3G 3J 3D 3H 3F 3I 3K
25 3E 3J 3I 3C 3H 3D 3L 3K
26 3E 3G 3I 3C 3J 3D 3L 3K
27 3E 3G 3J 3C 3H 3D 3L 3K
28 3E 3G 3I 3C 3H 3D 3L 3K
29 3E 3G 3J 3C 3H 3D 3L 3I
30 3E 3G 3J 3C 3H 3D 3I 3K
31 3C 3J 3E 3D 3I 3F 3L 3K
32 3C 3J 3E 3D 3H 3F 3L 3K
33 3C 3E 3I 3D 3H 3F 3L 3K
34 3C 3J 3E 3D 3H 3F 3L 3I
35 3C 3J 3E 3D 3H 3F 3I 3K
36 3C 3G 3E 3D 3J 3F 3L 3K
37 3C 3G 3E 3D 3I 3F 3L 3K
38 3C 3G 3E 3D 3J 3F 3L 3I
39 3C 3G 3E 3D 3J 3F 3I 3K
40 3C 3G 3E 3D 3H 3F 3L 3K
41 3C 3G 3J 3D 3H 3F 3L 3E
42 3C 3G 3J 3D 3H 3F 3E 3K
43 3C 3G 3E 3D 3H 3F 3L 3I
44 3C 3G 3E 3D 3H 3F 3I 3K
45 3C 3G 3J 3D 3H 3F 3E 3I
46 3H 3J 3B 3F 3I 3G 3L 3K
47 3E 3J 3I 3B 3H 3G 3L 3K
---
Page 83:
soxenA
83
48 3E 3J 3B 3F 3I 3H 3L 3K
49 3E 3J 3B 3F 3I 3G 3L 3K
50 3E 3J 3B 3F 3H 3G 3L 3K
51 3E 3G 3B 3F 3I 3H 3L 3K
52 3E 3J 3B 3F 3H 3G 3L 3I
53 3E 3J 3B 3F 3H 3G 3I 3K
54 3H 3J 3B 3D 3I 3G 3L 3K
55 3H 3J 3B 3D 3I 3F 3L 3K
56 3I 3G 3B 3D 3J 3F 3L 3K
57 3H 3G 3B 3D 3J 3F 3L 3K
58 3H 3G 3B 3D 3I 3F 3L 3K
59 3H 3G 3B 3D 3J 3F 3L 3I
60 3H 3G 3B 3D 3J 3F 3I 3K
61 3E 3J 3B 3D 3I 3H 3L 3K
62 3E 3J 3B 3D 3I 3G 3L 3K
63 3E 3J 3B 3D 3H 3G 3L 3K
64 3E 3G 3B 3D 3I 3H 3L 3K
65 3E 3J 3B 3D 3H 3G 3L 3I
66 3E 3J 3B 3D 3H 3G 3I 3K
67 3E 3J 3B 3D 3I 3F 3L 3K
68 3E 3J 3B 3D 3H 3F 3L 3K
69 3E 3I 3B 3D 3H 3F 3L 3K
70 3E 3J 3B 3D 3H 3F 3L 3I
71 3E 3J 3B 3D 3H 3F 3I 3K
72 3E 3G 3B 3D 3J 3F 3L 3K
73 3E 3G 3B 3D 3I 3F 3L 3K
74 3E 3G 3B 3D 3J 3F 3L 3I
75 3E 3G 3B 3D 3J 3F 3I 3K
76 3E 3G 3B 3D 3H 3F 3L 3K
---
Page 84:
84
77 3H 3G 3B 3D 3J 3F 3L 3E
78 3H 3G 3B 3D 3J 3F 3E 3K
79 3E 3G 3B 3D 3H 3F 3L 3I
80 3E 3G 3B 3D 3H 3F 3I 3K
81 3H 3G 3B 3D 3J 3F 3E 3I
82 3H 3J 3B 3C 3I 3G 3L 3K
83 3H 3J 3B 3C 3I 3F 3L 3K
84 3I 3G 3B 3C 3J 3F 3L 3K
85 3H 3G 3B 3C 3J 3F 3L 3K
86 3H 3G 3B 3C 3I 3F 3L 3K
87 3H 3G 3B 3C 3J 3F 3L 3I
88 3H 3G 3B 3C 3J 3F 3I 3K
89 3E 3J 3B 3C 3I 3H 3L 3K
90 3E 3J 3B 3C 3I 3G 3L 3K
91 3E 3J 3B 3C 3H 3G 3L 3K
92 3E 3G 3B 3C 3I 3H 3L 3K
93 3E 3J 3B 3C 3H 3G 3L 3I
94 3E 3J 3B 3C 3H 3G 3I 3K
95 3E 3J 3B 3C 3I 3F 3L 3K
96 3E 3J 3B 3C 3H 3F 3L 3K
97 3E 3I 3B 3C 3H 3F 3L 3K
98 3E 3J 3B 3C 3H 3F 3L 3I
99 3E 3J 3B 3C 3H 3F 3I 3K
100 3E 3G 3B 3C 3J 3F 3L 3K
101 3E 3G 3B 3C 3I 3F 3L 3K
102 3E 3G 3B 3C 3J 3F 3L 3I
103 3E 3G 3B 3C 3J 3F 3I 3K
104 3E 3G 3B 3C 3H 3F 3L 3K
105 3H 3G 3B 3C 3J 3F 3L 3E
---
Page 85:
soxenA
85
106 3H 3G 3B 3C 3J 3F 3E 3K
107 3E 3G 3B 3C 3H 3F 3L 3I
108 3E 3G 3B 3C 3H 3F 3I 3K
109 3H 3G 3B 3C 3J 3F 3E 3I
110 3H 3J 3B 3C 3I 3D 3L 3K
111 3I 3G 3B 3C 3J 3D 3L 3K
112 3H 3G 3B 3C 3J 3D 3L 3K
113 3H 3G 3B 3C 3I 3D 3L 3K
114 3H 3G 3B 3C 3J 3D 3L 3I
115 3H 3G 3B 3C 3J 3D 3I 3K
116 3C 3J 3B 3D 3I 3F 3L 3K
117 3C 3J 3B 3D 3H 3F 3L 3K
118 3C 3I 3B 3D 3H 3F 3L 3K
119 3C 3J 3B 3D 3H 3F 3L 3I
120 3C 3J 3B 3D 3H 3F 3I 3K
121 3C 3G 3B 3D 3J 3F 3L 3K
122 3C 3G 3B 3D 3I 3F 3L 3K
123 3C 3G 3B 3D 3J 3F 3L 3I
124 3C 3G 3B 3D 3J 3F 3I 3K
125 3C 3G 3B 3D 3H 3F 3L 3K
126 3C 3G 3B 3D 3H 3F 3L 3J
127 3H 3G 3B 3C 3J 3F 3D 3K
128 3C 3G 3B 3D 3H 3F 3L 3I
129 3C 3G 3B 3D 3H 3F 3I 3K
130 3H 3G 3B 3C 3J 3F 3D 3I
131 3E 3J 3B 3C 3I 3D 3L 3K
132 3E 3J 3B 3C 3H 3D 3L 3K
133 3E 3I 3B 3C 3H 3D 3L 3K
134 3E 3J 3B 3C 3H 3D 3L 3I
---
Page 86:
86
135 3E 3J 3B 3C 3H 3D 3I 3K
136 3E 3G 3B 3C 3J 3D 3L 3K
137 3E 3G 3B 3C 3I 3D 3L 3K
138 3E 3G 3B 3C 3J 3D 3L 3I
139 3E 3G 3B 3C 3J 3D 3I 3K
140 3E 3G 3B 3C 3H 3D 3L 3K
141 3H 3G 3B 3C 3J 3D 3L 3E
142 3H 3G 3B 3C 3J 3D 3E 3K
143 3E 3G 3B 3C 3H 3D 3L 3I
144 3E 3G 3B 3C 3H 3D 3I 3K
145 3H 3G 3B 3C 3J 3D 3E 3I
146 3C 3J 3B 3D 3E 3F 3L 3K
147 3C 3E 3B 3D 3I 3F 3L 3K
148 3C 3J 3B 3D 3E 3F 3L 3I
149 3C 3J 3B 3D 3E 3F 3I 3K
150 3C 3E 3B 3D 3H 3F 3L 3K
151 3C 3J 3B 3D 3H 3F 3L 3E
152 3C 3J 3B 3D 3H 3F 3E 3K
153 3C 3E 3B 3D 3H 3F 3L 3I
154 3C 3E 3B 3D 3H 3F 3I 3K
155 3C 3J 3B 3D 3H 3F 3E 3I
156 3C 3G 3B 3D 3E 3F 3L 3K
157 3C 3G 3B 3D 3J 3F 3L 3E
158 3C 3G 3B 3D 3J 3F 3E 3K
159 3C 3G 3B 3D 3E 3F 3L 3I
160 3C 3G 3B 3D 3E 3F 3I 3K
161 3C 3G 3B 3D 3J 3F 3E 3I
162 3C 3G 3B 3D 3H 3F 3L 3E
163 3C 3G 3B 3D 3H 3F 3E 3K
---
Page 87:
soxenA
87
164 3H 3G 3B 3C 3J 3F 3D 3E
165 3C 3G 3B 3D 3H 3F 3E 3I
166 3H 3J 3I 3F 3A 3G 3L 3K
167 3E 3J 3I 3A 3H 3G 3L 3K
168 3E 3J 3I 3F 3A 3H 3L 3K
169 3E 3J 3I 3F 3A 3G 3L 3K
170 3E 3G 3J 3F 3A 3H 3L 3K
171 3E 3G 3I 3F 3A 3H 3L 3K
172 3E 3G 3J 3F 3A 3H 3L 3I
173 3E 3G 3J 3F 3A 3H 3I 3K
174 3H 3J 3I 3D 3A 3G 3L 3K
175 3H 3J 3I 3D 3A 3F 3L 3K
176 3I 3G 3J 3D 3A 3F 3L 3K
177 3H 3G 3J 3D 3A 3F 3L 3K
178 3H 3G 3I 3D 3A 3F 3L 3K
179 3H 3G 3J 3D 3A 3F 3L 3I
180 3H 3G 3J 3D 3A 3F 3I 3K
181 3E 3J 3I 3D 3A 3H 3L 3K
182 3E 3J 3I 3D 3A 3G 3L 3K
183 3E 3G 3J 3D 3A 3H 3L 3K
184 3E 3G 3I 3D 3A 3H 3L 3K
185 3E 3G 3J 3D 3A 3H 3L 3I
186 3E 3G 3J 3D 3A 3H 3I 3K
187 3E 3J 3I 3D 3A 3F 3L 3K
188 3H 3J 3E 3D 3A 3F 3L 3K
189 3H 3E 3I 3D 3A 3F 3L 3K
190 3H 3J 3E 3D 3A 3F 3L 3I
191 3H 3J 3E 3D 3A 3F 3I 3K
192 3E 3G 3J 3D 3A 3F 3L 3K
---
Page 88:
88
193 3E 3G 3I 3D 3A 3F 3L 3K
194 3E 3G 3J 3D 3A 3F 3L 3I
195 3E 3G 3J 3D 3A 3F 3I 3K
196 3H 3G 3E 3D 3A 3F 3L 3K
197 3H 3G 3J 3D 3A 3F 3L 3E
198 3H 3G 3J 3D 3A 3F 3E 3K
199 3H 3G 3E 3D 3A 3F 3L 3I
200 3H 3G 3E 3D 3A 3F 3I 3K
201 3H 3G 3J 3D 3A 3F 3E 3I
202 3H 3J 3I 3C 3A 3G 3L 3K
203 3H 3J 3I 3C 3A 3F 3L 3K
204 3I 3G 3J 3C 3A 3F 3L 3K
205 3H 3G 3J 3C 3A 3F 3L 3K
206 3H 3G 3I 3C 3A 3F 3L 3K
207 3H 3G 3J 3C 3A 3F 3L 3I
208 3H 3G 3J 3C 3A 3F 3I 3K
209 3E 3J 3I 3C 3A 3H 3L 3K
210 3E 3J 3I 3C 3A 3G 3L 3K
211 3E 3G 3J 3C 3A 3H 3L 3K
212 3E 3G 3I 3C 3A 3H 3L 3K
213 3E 3G 3J 3C 3A 3H 3L 3I
214 3E 3G 3J 3C 3A 3H 3I 3K
215 3E 3J 3I 3C 3A 3F 3L 3K
216 3H 3J 3E 3C 3A 3F 3L 3K
217 3H 3E 3I 3C 3A 3F 3L 3K
218 3H 3J 3E 3C 3A 3F 3L 3I
219 3H 3J 3E 3C 3A 3F 3I 3K
220 3E 3G 3J 3C 3A 3F 3L 3K
221 3E 3G 3I 3C 3A 3F 3L 3K
---
Page 89:
soxenA
89
222 3E 3G 3J 3C 3A 3F 3L 3I
223 3E 3G 3J 3C 3A 3F 3I 3K
224 3H 3G 3E 3C 3A 3F 3L 3K
225 3H 3G 3J 3C 3A 3F 3L 3E
226 3H 3G 3J 3C 3A 3F 3E 3K
227 3H 3G 3E 3C 3A 3F 3L 3I
228 3H 3G 3E 3C 3A 3F 3I 3K
229 3H 3G 3J 3C 3A 3F 3E 3I
230 3H 3J 3I 3C 3A 3D 3L 3K
231 3I 3G 3J 3C 3A 3D 3L 3K
232 3H 3G 3J 3C 3A 3D 3L 3K
233 3H 3G 3I 3C 3A 3D 3L 3K
234 3H 3G 3J 3C 3A 3D 3L 3I
235 3H 3G 3J 3C 3A 3D 3I 3K
236 3C 3J 3I 3D 3A 3F 3L 3K
237 3H 3J 3F 3C 3A 3D 3L 3K
238 3H 3F 3I 3C 3A 3D 3L 3K
239 3H 3J 3F 3C 3A 3D 3L 3I
240 3H 3J 3F 3C 3A 3D 3I 3K
241 3C 3G 3J 3D 3A 3F 3L 3K
242 3C 3G 3I 3D 3A 3F 3L 3K
243 3C 3G 3J 3D 3A 3F 3L 3I
244 3C 3G 3J 3D 3A 3F 3I 3K
245 3H 3G 3F 3C 3A 3D 3L 3K
246 3C 3G 3J 3D 3A 3F 3L 3H
247 3H 3G 3J 3C 3A 3F 3D 3K
248 3H 3G 3F 3C 3A 3D 3L 3I
249 3H 3G 3F 3C 3A 3D 3I 3K
250 3H 3G 3J 3C 3A 3F 3D 3I
---
Page 90:
90
251 3E 3J 3I 3C 3A 3D 3L 3K
252 3H 3J 3E 3C 3A 3D 3L 3K
253 3H 3E 3I 3C 3A 3D 3L 3K
254 3H 3J 3E 3C 3A 3D 3L 3I
255 3H 3J 3E 3C 3A 3D 3I 3K
256 3E 3G 3J 3C 3A 3D 3L 3K
257 3E 3G 3I 3C 3A 3D 3L 3K
258 3E 3G 3J 3C 3A 3D 3L 3I
259 3E 3G 3J 3C 3A 3D 3I 3K
260 3H 3G 3E 3C 3A 3D 3L 3K
261 3H 3G 3J 3C 3A 3D 3L 3E
262 3H 3G 3J 3C 3A 3D 3E 3K
263 3H 3G 3E 3C 3A 3D 3L 3I
264 3H 3G 3E 3C 3A 3D 3I 3K
265 3H 3G 3J 3C 3A 3D 3E 3I
266 3C 3J 3E 3D 3A 3F 3L 3K
267 3C 3E 3I 3D 3A 3F 3L 3K
268 3C 3J 3E 3D 3A 3F 3L 3I
269 3C 3J 3E 3D 3A 3F 3I 3K
270 3H 3E 3F 3C 3A 3D 3L 3K
271 3H 3J 3F 3C 3A 3D 3L 3E
272 3H 3J 3E 3C 3A 3F 3D 3K
273 3H 3E 3F 3C 3A 3D 3L 3I
274 3H 3E 3F 3C 3A 3D 3I 3K
275 3H 3J 3E 3C 3A 3F 3D 3I
276 3C 3G 3E 3D 3A 3F 3L 3K
277 3C 3G 3J 3D 3A 3F 3L 3E
278 3C 3G 3J 3D 3A 3F 3E 3K
279 3C 3G 3E 3D 3A 3F 3L 3I
---
Page 91:
soxenA
91
280 3C 3G 3E 3D 3A 3F 3I 3K
281 3C 3G 3J 3D 3A 3F 3E 3I
282 3H 3G 3F 3C 3A 3D 3L 3E
283 3H 3G 3E 3C 3A 3F 3D 3K
284 3H 3G 3J 3C 3A 3F 3D 3E
285 3H 3G 3E 3C 3A 3F 3D 3I
286 3H 3J 3B 3A 3I 3G 3L 3K
287 3H 3J 3B 3A 3I 3F 3L 3K
288 3I 3J 3B 3F 3A 3G 3L 3K
289 3H 3J 3B 3F 3A 3G 3L 3K
290 3H 3G 3B 3A 3I 3F 3L 3K
291 3H 3J 3B 3F 3A 3G 3L 3I
292 3H 3J 3B 3F 3A 3G 3I 3K
293 3E 3J 3B 3A 3I 3H 3L 3K
294 3E 3J 3B 3A 3I 3G 3L 3K
295 3E 3J 3B 3A 3H 3G 3L 3K
296 3E 3G 3B 3A 3I 3H 3L 3K
297 3E 3J 3B 3A 3H 3G 3L 3I
298 3E 3J 3B 3A 3H 3G 3I 3K
299 3E 3J 3B 3A 3I 3F 3L 3K
300 3E 3J 3B 3F 3A 3H 3L 3K
301 3E 3I 3B 3F 3A 3H 3L 3K
302 3E 3J 3B 3F 3A 3H 3L 3I
303 3E 3J 3B 3F 3A 3H 3I 3K
304 3E 3J 3B 3F 3A 3G 3L 3K
305 3E 3G 3B 3A 3I 3F 3L 3K
306 3E 3J 3B 3F 3A 3G 3L 3I
307 3E 3J 3B 3F 3A 3G 3I 3K
308 3E 3G 3B 3F 3A 3H 3L 3K
---
Page 92:
92
309 3H 3J 3B 3F 3A 3G 3L 3E
310 3H 3J 3B 3F 3A 3G 3E 3K
311 3E 3G 3B 3F 3A 3H 3L 3I
312 3E 3G 3B 3F 3A 3H 3I 3K
313 3H 3J 3B 3F 3A 3G 3E 3I
314 3I 3J 3B 3D 3A 3H 3L 3K
315 3I 3J 3B 3D 3A 3G 3L 3K
316 3H 3J 3B 3D 3A 3G 3L 3K
317 3I 3G 3B 3D 3A 3H 3L 3K
318 3H 3J 3B 3D 3A 3G 3L 3I
319 3H 3J 3B 3D 3A 3G 3I 3K
320 3I 3J 3B 3D 3A 3F 3L 3K
321 3H 3J 3B 3D 3A 3F 3L 3K
322 3H 3I 3B 3D 3A 3F 3L 3K
323 3H 3J 3B 3D 3A 3F 3L 3I
324 3H 3J 3B 3D 3A 3F 3I 3K
325 3F 3J 3B 3D 3A 3G 3L 3K
326 3I 3G 3B 3D 3A 3F 3L 3K
327 3F 3J 3B 3D 3A 3G 3L 3I
328 3F 3J 3B 3D 3A 3G 3I 3K
329 3H 3G 3B 3D 3A 3F 3L 3K
330 3H 3G 3B 3D 3A 3F 3L 3J
331 3H 3G 3B 3D 3A 3F 3J 3K
332 3H 3G 3B 3D 3A 3F 3L 3I
333 3H 3G 3B 3D 3A 3F 3I 3K
334 3H 3G 3B 3D 3A 3F 3I 3J
335 3E 3J 3B 3A 3I 3D 3L 3K
336 3E 3J 3B 3D 3A 3H 3L 3K
337 3E 3I 3B 3D 3A 3H 3L 3K
---
Page 93:
soxenA
93
338 3E 3J 3B 3D 3A 3H 3L 3I
339 3E 3J 3B 3D 3A 3H 3I 3K
340 3E 3J 3B 3D 3A 3G 3L 3K
341 3E 3G 3B 3A 3I 3D 3L 3K
342 3E 3J 3B 3D 3A 3G 3L 3I
343 3E 3J 3B 3D 3A 3G 3I 3K
344 3E 3G 3B 3D 3A 3H 3L 3K
345 3H 3J 3B 3D 3A 3G 3L 3E
346 3H 3J 3B 3D 3A 3G 3E 3K
347 3E 3G 3B 3D 3A 3H 3L 3I
348 3E 3G 3B 3D 3A 3H 3I 3K
349 3H 3J 3B 3D 3A 3G 3E 3I
350 3E 3J 3B 3D 3A 3F 3L 3K
351 3E 3I 3B 3D 3A 3F 3L 3K
352 3E 3J 3B 3D 3A 3F 3L 3I
353 3E 3J 3B 3D 3A 3F 3I 3K
354 3H 3E 3B 3D 3A 3F 3L 3K
355 3H 3J 3B 3D 3A 3F 3L 3E
356 3H 3J 3B 3D 3A 3F 3E 3K
357 3H 3E 3B 3D 3A 3F 3L 3I
358 3H 3E 3B 3D 3A 3F 3I 3K
359 3H 3J 3B 3D 3A 3F 3E 3I
360 3E 3G 3B 3D 3A 3F 3L 3K
361 3E 3G 3B 3D 3A 3F 3L 3J
362 3E 3G 3B 3D 3A 3F 3J 3K
363 3E 3G 3B 3D 3A 3F 3L 3I
364 3E 3G 3B 3D 3A 3F 3I 3K
365 3E 3G 3B 3D 3A 3F 3I 3J
366 3H 3G 3B 3D 3A 3F 3L 3E
---
Page 94:
94
367 3H 3G 3B 3D 3A 3F 3E 3K
368 3H 3G 3B 3D 3A 3F 3E 3J
369 3H 3G 3B 3D 3A 3F 3E 3I
370 3I 3J 3B 3C 3A 3H 3L 3K
371 3I 3J 3B 3C 3A 3G 3L 3K
372 3H 3J 3B 3C 3A 3G 3L 3K
373 3I 3G 3B 3C 3A 3H 3L 3K
374 3H 3J 3B 3C 3A 3G 3L 3I
375 3H 3J 3B 3C 3A 3G 3I 3K
376 3I 3J 3B 3C 3A 3F 3L 3K
377 3H 3J 3B 3C 3A 3F 3L 3K
378 3H 3I 3B 3C 3A 3F 3L 3K
379 3H 3J 3B 3C 3A 3F 3L 3I
380 3H 3J 3B 3C 3A 3F 3I 3K
381 3C 3J 3B 3F 3A 3G 3L 3K
382 3I 3G 3B 3C 3A 3F 3L 3K
383 3C 3J 3B 3F 3A 3G 3L 3I
384 3C 3J 3B 3F 3A 3G 3I 3K
385 3H 3G 3B 3C 3A 3F 3L 3K
386 3H 3G 3B 3C 3A 3F 3L 3J
387 3H 3G 3B 3C 3A 3F 3J 3K
388 3H 3G 3B 3C 3A 3F 3L 3I
389 3H 3G 3B 3C 3A 3F 3I 3K
390 3H 3G 3B 3C 3A 3F 3I 3J
391 3E 3J 3B 3A 3I 3C 3L 3K
392 3E 3J 3B 3C 3A 3H 3L 3K
393 3E 3I 3B 3C 3A 3H 3L 3K
394 3E 3J 3B 3C 3A 3H 3L 3I
395 3E 3J 3B 3C 3A 3H 3I 3K
---
Page 95:
soxenA
95
396 3E 3J 3B 3C 3A 3G 3L 3K
397 3E 3G 3B 3A 3I 3C 3L 3K
398 3E 3J 3B 3C 3A 3G 3L 3I
399 3E 3J 3B 3C 3A 3G 3I 3K
400 3E 3G 3B 3C 3A 3H 3L 3K
401 3H 3J 3B 3C 3A 3G 3L 3E
402 3H 3J 3B 3C 3A 3G 3E 3K
403 3E 3G 3B 3C 3A 3H 3L 3I
404 3E 3G 3B 3C 3A 3H 3I 3K
405 3H 3J 3B 3C 3A 3G 3E 3I
406 3E 3J 3B 3C 3A 3F 3L 3K
407 3E 3I 3B 3C 3A 3F 3L 3K
408 3E 3J 3B 3C 3A 3F 3L 3I
409 3E 3J 3B 3C 3A 3F 3I 3K
410 3H 3E 3B 3C 3A 3F 3L 3K
411 3H 3J 3B 3C 3A 3F 3L 3E
412 3H 3J 3B 3C 3A 3F 3E 3K
413 3H 3E 3B 3C 3A 3F 3L 3I
414 3H 3E 3B 3C 3A 3F 3I 3K
415 3H 3J 3B 3C 3A 3F 3E 3I
416 3E 3G 3B 3C 3A 3F 3L 3K
417 3E 3G 3B 3C 3A 3F 3L 3J
418 3E 3G 3B 3C 3A 3F 3J 3K
419 3E 3G 3B 3C 3A 3F 3L 3I
420 3E 3G 3B 3C 3A 3F 3I 3K
421 3E 3G 3B 3C 3A 3F 3I 3J
422 3H 3G 3B 3C 3A 3F 3L 3E
423 3H 3G 3B 3C 3A 3F 3E 3K
424 3H 3G 3B 3C 3A 3F 3E 3J
---
Page 96:
96
425 3H 3G 3B 3C 3A 3F 3E 3I
426 3I 3J 3B 3C 3A 3D 3L 3K
427 3H 3J 3B 3C 3A 3D 3L 3K
428 3H 3I 3B 3C 3A 3D 3L 3K
429 3H 3J 3B 3C 3A 3D 3L 3I
430 3H 3J 3B 3C 3A 3D 3I 3K
431 3C 3J 3B 3D 3A 3G 3L 3K
432 3I 3G 3B 3C 3A 3D 3L 3K
433 3C 3J 3B 3D 3A 3G 3L 3I
434 3C 3J 3B 3D 3A 3G 3I 3K
435 3H 3G 3B 3C 3A 3D 3L 3K
436 3H 3G 3B 3C 3A 3D 3L 3J
437 3H 3G 3B 3C 3A 3D 3J 3K
438 3H 3G 3B 3C 3A 3D 3L 3I
439 3H 3G 3B 3C 3A 3D 3I 3K
440 3H 3G 3B 3C 3A 3D 3I 3J
441 3C 3J 3B 3D 3A 3F 3L 3K
442 3C 3I 3B 3D 3A 3F 3L 3K
443 3C 3J 3B 3D 3A 3F 3L 3I
444 3C 3J 3B 3D 3A 3F 3I 3K
445 3H 3F 3B 3C 3A 3D 3L 3K
446 3C 3J 3B 3D 3A 3F 3L 3H
447 3H 3J 3B 3C 3A 3F 3D 3K
448 3H 3F 3B 3C 3A 3D 3L 3I
449 3H 3F 3B 3C 3A 3D 3I 3K
450 3H 3J 3B 3C 3A 3F 3D 3I
451 3C 3G 3B 3D 3A 3F 3L 3K
452 3C 3G 3B 3D 3A 3F 3L 3J
453 3C 3G 3B 3D 3A 3F 3J 3K
---
Page 97:
soxenA
97
454 3C 3G 3B 3D 3A 3F 3L 3I
455 3C 3G 3B 3D 3A 3F 3I 3K
456 3C 3G 3B 3D 3A 3F 3I 3J
457 3C 3G 3B 3D 3A 3F 3L 3H
458 3H 3G 3B 3C 3A 3F 3D 3K
459 3H 3G 3B 3C 3A 3F 3D 3J
460 3H 3G 3B 3C 3A 3F 3D 3I
461 3E 3J 3B 3C 3A 3D 3L 3K
462 3E 3I 3B 3C 3A 3D 3L 3K
463 3E 3J 3B 3C 3A 3D 3L 3I
464 3E 3J 3B 3C 3A 3D 3I 3K
465 3H 3E 3B 3C 3A 3D 3L 3K
466 3H 3J 3B 3C 3A 3D 3L 3E
467 3H 3J 3B 3C 3A 3D 3E 3K
468 3H 3E 3B 3C 3A 3D 3L 3I
469 3H 3E 3B 3C 3A 3D 3I 3K
470 3H 3J 3B 3C 3A 3D 3E 3I
471 3E 3G 3B 3C 3A 3D 3L 3K
472 3E 3G 3B 3C 3A 3D 3L 3J
473 3E 3G 3B 3C 3A 3D 3J 3K
474 3E 3G 3B 3C 3A 3D 3L 3I
475 3E 3G 3B 3C 3A 3D 3I 3K
476 3E 3G 3B 3C 3A 3D 3I 3J
477 3H 3G 3B 3C 3A 3D 3L 3E
478 3H 3G 3B 3C 3A 3D 3E 3K
479 3H 3G 3B 3C 3A 3D 3E 3J
480 3H 3G 3B 3C 3A 3D 3E 3I
481 3C 3E 3B 3D 3A 3F 3L 3K
482 3C 3J 3B 3D 3A 3F 3L 3E
---
Page 98:
98
483 3C 3J 3B 3D 3A 3F 3E 3K
484 3C 3E 3B 3D 3A 3F 3L 3I
485 3C 3E 3B 3D 3A 3F 3I 3K
486 3C 3J 3B 3D 3A 3F 3E 3I
487 3H 3F 3B 3C 3A 3D 3L 3E
488 3H 3E 3B 3C 3A 3F 3D 3K
489 3H 3J 3B 3C 3A 3F 3D 3E
490 3H 3E 3B 3C 3A 3F 3D 3I
491 3C 3G 3B 3D 3A 3F 3L 3E
492 3C 3G 3B 3D 3A 3F 3E 3K
493 3C 3G 3B 3D 3A 3F 3E 3J
494 3C 3G 3B 3D 3A 3F 3E 3I
495 3H 3G 3B 3C 3A 3F 3D 3E
---

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 73.9s)

_Thinking:_

I found the full 495 combinations in the PDF pages 81-98. Now I need to:
1. Parse all 495 rows from these pages
2. Build the Annex C lookup table that maps the 8 qualifying groups to the 8 match assignments
3. Create the annex_c.py file
4. Fix the mundial_2026.csv file
5. Update monte_carlo_world_cup.py with the new logic

Let me first extract all the data programmatically and build the JSON file.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /c/Users/santi/Desktop/prediccion-mundial && .venv/Scripts/python.exe -c \"\nimport pdfplumber\nimport json\n\npdf = pdfplumber.open('data/FWC2026_regulations_ES.pdf')\n\nannex_c_map = {}\n\n# Pages 81-98 (0-indexed: 80-97) contain the table\nfor page_num in range(80, 98):\n    page = pdf.pages[page_num]\n    text = page.extract_text()\n    if not text:\n        continue\n    \n    lines = text.split('\\n')\n    for line in lines:\n        line = line.strip()\n        if not line:\n            continue\n        \n        # Each line starts with option number, then 8 group assignments\n        parts = line.split()\n        if len(parts) >= 9 and parts[0].isdigit():\n            option = int(parts[0])\n            # The next 8 parts are the match assignments like '3E', '3J', etc.\n            match_assignments = []\n            qualifying_groups = set()\n            \n            for part in parts[1:9]:\n                if part.startswith('3') and len(part) == 2:\n                    group = part[1]\n                    match_assignments.append(group)\n                    qualifying_groups.add(group)\n            \n            if len(match_assignments) == 8 and len(qualifying_groups) == 8:\n                key = frozenset(qualifying_groups)\n                annex_c_map[key] = tuple(match_assignments)\n\nprint(f'Total combinations extracted: {len(annex_c_map)}')\n\n# Save to JSON\nwith open('data/annex_c_data.json', 'w') as f:\n    json_map = {tuple(sorted(k)): v for k, v in annex_c_map.items()}\n    json.dump(json_map, f, indent=2)\n\nprint('Saved to data/annex_c_data.json')\n\n# Verify\nfor key, val in list(annex_c_map.items())[:5]:\n    print(f'  {sorted(key)} -> {val}')\n\n# Also verify the last few\nfor key, val in list(annex_c_map.items())[-5:]:\n    print(f'  {sorted(key)} -> {val}')\n\"",
  "description": "Extract all 495 combinations from PDF"
}
```

**Output:**
```
Traceback (most recent call last):
Total combinations extracted: 495
  File "<string>", line 45, in <module>
    json.dump(json_map, f, indent=2)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\santi\AppData\Local\Programs\Python\Python313\Lib\json\__init__.py", line 179, in dump
    for chunk in iterable:
                 ^^^^^^^^
  File "C:\Users\santi\AppData\Local\Programs\Python\Python313\Lib\json\encoder.py", line 433, in _iterencode
    yield from _iterencode_dict(o, _current_indent_level)
  File "C:\Users\santi\AppData\Local\Programs\Python\Python313\Lib\json\encoder.py", line 376, in _iterencode_dict
    raise TypeError(f'keys must be str, int, float, bool or None, '
                    f'not {key.__class__.__name__}')
TypeError: keys must be str, int, float, bool or None, not tuple

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 91.5s)

_Thinking:_

The extraction worked - 495 combinations! The error is just in JSON serialization because tuples aren't valid JSON keys. Let me fix that.

```python
# Convert tuples to strings for JSON keys
json_map = {'-'.join(sorted(k)): v for k, v in annex_c_map.items()}
```
Let me fix that and save.

**Tool: bash**

**Input:**
```json
{
  "command": "cd /c/Users/santi/Desktop/prediccion-mundial && .venv/Scripts/python.exe -c \"\nimport pdfplumber\nimport json\n\npdf = pdfplumber.open('data/FWC2026_regulations_ES.pdf')\n\nannex_c_map = {}\n\nfor page_num in range(80, 98):\n    page = pdf.pages[page_num]\n    text = page.extract_text()\n    if not text:\n        continue\n    \n    lines = text.split('\\n')\n    for line in lines:\n        line = line.strip()\n        if not line:\n            continue\n        \n        parts = line.split()\n        if len(parts) >= 9 and parts[0].isdigit():\n            option = int(parts[0])\n            match_assignments = []\n            qualifying_groups = set()\n            \n            for part in parts[1:9]:\n                if part.startswith('3') and len(part) == 2:\n                    group = part[1]\n                    match_assignments.append(group)\n                    qualifying_groups.add(group)\n            \n            if len(match_assignments) == 8 and len(qualifying_groups) == 8:\n                key = frozenset(qualifying_groups)\n                annex_c_map[key] = tuple(match_assignments)\n\nprint(f'Total combinations extracted: {len(annex_c_map)}')\n\n# Save to JSON - use string keys\nwith open('data/annex_c_data.json', 'w') as f:\n    json_map = {'-'.join(sorted(k)): v for k, v in annex_c_map.items()}\n    json.dump(json_map, f, indent=2)\n\nprint('Saved to data/annex_c_data.json')\n\n# Verify\nfor key, val in list(annex_c_map.items())[:5]:\n    print(f'  {sorted(key)} -> {val}')\n\nfor key, val in list(annex_c_map.items())[-5:]:\n    print(f'  {sorted(key)} -> {val}')\n\"",
  "description": "Extract and save Annex C data"
}
```

**Output:**
```
Total combinations extracted: 495
Saved to data/annex_c_data.json
  ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'] -> ('E', 'J', 'I', 'F', 'H', 'G', 'L', 'K')
  ['D', 'F', 'G', 'H', 'I', 'J', 'K', 'L'] -> ('H', 'G', 'I', 'D', 'J', 'F', 'L', 'K')
  ['D', 'E', 'G', 'H', 'I', 'J', 'K', 'L'] -> ('E', 'J', 'I', 'D', 'H', 'G', 'L', 'K')
  ['D', 'E', 'F', 'H', 'I', 'J', 'K', 'L'] -> ('E', 'J', 'I', 'D', 'H', 'F', 'L', 'K')
  ['D', 'E', 'F', 'G', 'I', 'J', 'K', 'L'] -> ('E', 'G', 'I', 'D', 'J', 'F', 'L', 'K')
  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'L'] -> ('C', 'G', 'B', 'D', 'A', 'F', 'L', 'E')
  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'K'] -> ('C', 'G', 'B', 'D', 'A', 'F', 'E', 'K')
  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'J'] -> ('C', 'G', 'B', 'D', 'A', 'F', 'E', 'J')
  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I'] -> ('C', 'G', 'B', 'D', 'A', 'F', 'E', 'I')
  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] -> ('H', 'G', 'B', 'C', 'A', 'F', 'D', 'E')

```

---

## Assistant (Build · Nemotron 3 Ultra Free · 43.4s)

_Thinking:_

The Annex C data is extracted successfully with all 495 combinations. Now I need to:
1. Create `src/annex_c.py` with the lookup logic
2. Fix `mundial_2026.csv` with the correct FIFA R32 structure
3. Update `monte_carlo_world_cup.py` to use the new logic

Let me update the todo list and start implementing.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Analyze current mundial_2026.csv format issues and FIFA official bracket structure",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Research FIFA Annex C 495 combinations table for 3rd place team matchups",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Create comprehensive implementation plan",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Extract Annex C 495 combinations from PDF",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Fix mundial_2026.csv with official FIFA R32 structure",
      "status": "in_progress",
      "priority": "high"
    },
    {
      "content": "Create src/annex_c.py with 495-combination lookup table",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Implement build_round_of_32_fixtures() in monte_carlo_world_cup.py",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Integrate Annex C logic into simulate_world_cup()",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Test simulation with new format",
      "status": "pending",
      "priority": "high"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Analyze current mundial_2026.csv format issues and FIFA official bracket structure",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Research FIFA Annex C 495 combinations table for 3rd place team matchups",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Create comprehensive implementation plan",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Extract Annex C 495 combinations from PDF",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Fix mundial_2026.csv with official FIFA R32 structure",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Create src/annex_c.py with 495-combination lookup table",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Implement build_round_of_32_fixtures() in monte_carlo_world_cup.py",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Integrate Annex C logic into simulate_world_cup()",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Test simulation with new format",
    "status": "pending",
    "priority": "high"
  }
]
```

---

## Assistant (Build · Nemotron 3 Ultra Free · 60.1s)

_Thinking:_

Now let me fix the mundial_2026.csv file with the correct FIFA R32 structure. Based on the FIFA regulations, the 16 Round of 32 matches are:

1. 1E vs 3rd (from qualifying groups including A,B,C,D,F)
2. 1I vs 3rd (from qualifying groups including C,D,F,G,H)
3. 2A vs 2B
4. 1F vs 2C
5. 2K vs 2L
6. 1H vs 2J
7. 1D vs 3rd (from qualifying groups including B,E,F,I,J)
8. 1G vs 3rd (from qualifying groups including A,E,H,I,J)
9. 1C vs 2F
10. 2E vs 2I
11. 1A vs 3rd (from qualifying groups including C,E,F,H,I)
12. 1L vs 3rd (from qualifying groups including E,H,I,J,K)
13. 1J vs 2H
14. 2D vs 2G
15. 1B vs 3rd (from qualifying groups including E,F,G,I,J)
16. 1K vs 3rd (from qualifying groups including D,E,I,J,L)

The 8 group winners that face 3rd place teams: 1A, 1B, 1D, 1E, 1G, 1I, 1K, 1L

Let me create the corrected mundial_2026.csv with proper R32 fixtures.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\santi\\Desktop\\prediccion-mundial\\data\\mundial_2026.csv"
}
```

**Output:**
```
<path>C:\Users\santi\Desktop\prediccion-mundial\data\mundial_2026.csv</path>
<type>file</type>
<content>
1: date,stage,group,home_team,away_team,home_score,away_score,tournament,city,country,neutral
2: 2026-06-11,GROUP,A,Mexico,South Africa,2,0,FIFA World Cup,Mexico City,Mexico,TRUE
3: 2026-06-11,GROUP,A,South Korea,Czech Republic,2,1,FIFA World Cup,Guadalajara,Mexico,TRUE
4: 2026-06-12,GROUP,B,Canada,Bosnia and Herzegovina,1,1,FIFA World Cup,Toronto,Canada,TRUE
5: 2026-06-12,GROUP,D,United States,Paraguay,4,1,FIFA World Cup,Los Angeles,USA,TRUE
6: 2026-06-13,GROUP,B,Qatar,Switzerland,1,1,FIFA World Cup,San Francisco,USA,TRUE
7: 2026-06-13,GROUP,C,Brazil,Morocco,1,1,FIFA World Cup,East Rutherford,USA,TRUE
8: 2026-06-13,GROUP,C,Haiti,Scotland,0,1,FIFA World Cup,Boston,USA,TRUE
9: 2026-06-13,GROUP,D,Australia,Turkey,2,0,FIFA World Cup,Vancouver,Canada,TRUE
10: 2026-06-14,GROUP,E,Germany,Curaçao,7,1,FIFA World Cup,Houston,USA,TRUE
11: 2026-06-14,GROUP,F,Netherlands,Japan,2,2,FIFA World Cup,Dallas,USA,TRUE
12: 2026-06-14,GROUP,E,Ivory Coast,Ecuador,1,0,FIFA World Cup,Philadelphia,USA,TRUE
13: 2026-06-14,GROUP,F,Sweden,Tunisia,5,1,FIFA World Cup,Monterrey,Mexico,TRUE
14: 2026-06-15,GROUP,H,Spain,Cape Verde,0,0,FIFA World Cup,Atlanta,USA,TRUE
15: 2026-06-15,GROUP,G,Belgium,Egypt,1,1,FIFA World Cup,Seattle,USA,TRUE
16: 2026-06-15,GROUP,H,Saudi Arabia,Uruguay,1,1,FIFA World Cup,Miami,USA,TRUE
17: 2026-06-15,GROUP,G,Iran,New Zealand,2,2,FIFA World Cup,Los Angeles,USA,TRUE
18: 2026-06-16,GROUP,I,France,Senegal,3,1,FIFA World Cup,East Rutherford,USA,TRUE
19: 2026-06-16,GROUP,I,Iraq,Norway,1,4,FIFA World Cup,Boston,USA,TRUE
20: 2026-06-16,GROUP,J,Argentina,Algeria,3,0,FIFA World Cup,Kansas City,USA,TRUE
21: 2026-06-16,GROUP,J,Austria,Jordan,3,1,FIFA World Cup,San Francisco,USA,TRUE
22: 2026-06-17,GROUP,K,Portugal,DR Congo,1,1,FIFA World Cup,Houston,USA,TRUE
23: 2026-06-17,GROUP,L,England,Croatia,4,2,FIFA World Cup,Dallas,USA,TRUE
24: 2026-06-17,GROUP,L,Ghana,Panama,1,0,FIFA World Cup,Toronto,Canada,TRUE
25: 2026-06-17,GROUP,K,Uzbekistan,Colombia,1,3,FIFA World Cup,Mexico City,Mexico,TRUE
26: 2026-06-18,GROUP,A,Czech Republic,South Africa,1,1,FIFA World Cup,Atlanta,USA,TRUE
27: 2026-06-18,GROUP,B,Switzerland,Bosnia and Herzegovina,4,1,FIFA World Cup,Los Angeles,USA,TRUE
28: 2026-06-18,GROUP,B,Canada,Qatar,6,0,FIFA World Cup,Vancouver,Canada,TRUE
29: 2026-06-18,GROUP,A,Mexico,South Korea,1,0,FIFA World Cup,Guadalajara,Mexico,TRUE
30: 2026-06-19,GROUP,D,United States,Australia,2,0,FIFA World Cup,Seattle,USA,TRUE
31: 2026-06-19,GROUP,C,Scotland,Morocco,0,1,FIFA World Cup,Boston,USA,TRUE
32: 2026-06-19,GROUP,C,Brazil,Haiti,3,0,FIFA World Cup,Philadelphia,USA,TRUE
33: 2026-06-19,GROUP,D,Turkey,Paraguay,0,1,FIFA World Cup,San Francisco,USA,TRUE
34: 2026-06-20,GROUP,F,Netherlands,Sweden,5,1,FIFA World Cup,Houston,USA,TRUE
35: 2026-06-20,GROUP,E,Germany,Ivory Coast,2,1,FIFA World Cup,Toronto,Canada,TRUE
36: 2026-06-20,GROUP,E,Ecuador,Curaçao,0,0,FIFA World Cup,Kansas City,USA,TRUE
37: 2026-06-20,GROUP,F,Tunisia,Japan,0,4,FIFA World Cup,Monterrey,Mexico,TRUE
38: 2026-06-21,GROUP,H,Spain,Saudi Arabia,4,0,FIFA World Cup,Atlanta,USA,TRUE
39: 2026-06-21,GROUP,G,Belgium,Iran,0,0,FIFA World Cup,Los Angeles,USA,TRUE
40: 2026-06-21,GROUP,H,Uruguay,Cape Verde,2,2,FIFA World Cup,Miami,USA,TRUE
41: 2026-06-21,GROUP,G,New Zealand,Egypt,3,1,FIFA World Cup,Vancouver,Canada,TRUE
42: 2026-06-22,GROUP,J,Argentina,Austria,2,0,FIFA World Cup,Dallas,USA,TRUE
43: 2026-06-22,GROUP,I,France,Iraq,3,0,FIFA World Cup,Philadelphia,USA,TRUE
44: 2026-06-22,GROUP,I,Norway,Senegal,3,2,FIFA World Cup,East Rutherford,USA,TRUE
45: 2026-06-22,GROUP,J,Jordan,Algeria,1,2,FIFA World Cup,San Francisco,USA,TRUE
46: 2026-06-23,GROUP,K,Portugal,Uzbekistan,5,0,FIFA World Cup,Houston,USA,TRUE
47: 2026-06-23,GROUP,L,England,Ghana,0,0,FIFA World Cup,Boston,USA,TRUE
48: 2026-06-23,GROUP,L,Panama,Croatia,0,1,FIFA World Cup,Toronto,Canada,TRUE
49: 2026-06-23,GROUP,K,Colombia,DR Congo,1,0,FIFA World Cup,Guadalajara,Mexico,TRUE
50: 2026-06-24,GROUP,B,Switzerland,Canada,,,FIFA World Cup,Vancouver,Canada,TRUE
51: 2026-06-24,GROUP,B,Bosnia and Herzegovina,Qatar,,,FIFA World Cup,Seattle,USA,TRUE
52: 2026-06-24,GROUP,A,South Africa,South Korea,,,FIFA World Cup,Mexico City,Mexico,TRUE
53: 2026-06-24,GROUP,A,Czech Republic,Mexico,,,FIFA World Cup,Guadalajara,Mexico,TRUE
54: 2026-06-25,GROUP,D,United States,Turkey,,,FIFA World Cup,Los Angeles,USA,TRUE
55: 2026-06-25,GROUP,D,Paraguay,Australia,,,FIFA World Cup,San Francisco,USA,TRUE
56: 2026-06-25,GROUP,C,Morocco,Haiti,,,FIFA World Cup,Boston,USA,TRUE
57: 2026-06-25,GROUP,C,Scotland,Brazil,,,FIFA World Cup,Miami,USA,TRUE
58: 2026-06-25,GROUP,E,Germany,Ecuador,,,FIFA World Cup,East Rutherford,USA,TRUE
59: 2026-06-25,GROUP,E,Ivory Coast,Curaçao,,,FIFA World Cup,Philadelphia,USA,TRUE
60: 2026-06-26,GROUP,F,Netherlands,Tunisia,,,FIFA World Cup,Kansas City,USA,TRUE
61: 2026-06-26,GROUP,F,Sweden,Japan,,,FIFA World Cup,Dallas,USA,TRUE
62: 2026-06-26,GROUP,G,Belgium,New Zealand,,,FIFA World Cup,Vancouver,Canada,TRUE
63: 2026-06-26,GROUP,G,Egypt,Iran,,,FIFA World Cup,Seattle,USA,TRUE
64: 2026-06-26,GROUP,I,France,Norway,,,FIFA World Cup,Boston,USA,TRUE
65: 2026-06-26,GROUP,I,Iraq,Senegal,,,FIFA World Cup,East Rutherford,USA,TRUE
66: 2026-06-27,GROUP,H,Spain,Uruguay,,,FIFA World Cup,Guadalajara,Mexico,TRUE
67: 2026-06-27,GROUP,H,Cape Verde,Saudi Arabia,,,FIFA World Cup,Miami,USA,TRUE
68: 2026-06-27,GROUP,L,England,Panama,,,FIFA World Cup,East Rutherford,USA,TRUE
69: 2026-06-27,GROUP,L,Croatia,Ghana,,,FIFA World Cup,Philadelphia,USA,TRUE
70: 2026-06-27,GROUP,J,Jordan,Argentina,,,FIFA World Cup,Dallas,USA,TRUE
71: 2026-06-27,GROUP,J,Algeria,Austria,,,FIFA World Cup,Kansas City,USA,TRUE
72: 2026-06-27,GROUP,K,Portugal,Colombia,,,FIFA World Cup,Miami,USA,TRUE
73: 2026-06-27,GROUP,K,Uzbekistan,DR Congo,,,FIFA World Cup,Houston,USA,TRUE
74: 2026-06-28,R32,,1A,2B,,,FIFA World Cup,,,TRUE
75: 2026-06-28,R32,,1C,2D,,,FIFA World Cup,,,TRUE
76: 2026-06-29,R32,,1E,2F,,,FIFA World Cup,,,TRUE
77: 2026-06-29,R32,,1G,2H,,,FIFA World Cup,,,TRUE
78: 2026-06-30,R32,,1I,2J,,,FIFA World Cup,,,TRUE
79: 2026-06-30,R32,,1K,2L,,,FIFA World Cup,,,TRUE
80: 2026-07-01,R32,,1B,2A,,,FIFA World Cup,,,TRUE
81: 2026-07-01,R32,,1D,2C,,,FIFA World Cup,,,TRUE
82: 2026-07-02,R32,,1F,2E,,,FIFA World Cup,,,TRUE
83: 2026-07-02,R32,,1H,2G,,,FIFA World Cup,,,TRUE
84: 2026-07-03,R32,,1J,2I,,,FIFA World Cup,,,TRUE
85: 2026-07-03,R32,,1L,2K,,,FIFA World Cup,,,TRUE
86: 2026-07-03,R32,,3rd_1,3rd_2,,,FIFA World Cup,,,TRUE
87: 2026-07-03,R32,,3rd_3,3rd_4,,,FIFA World Cup,,,TRUE
88: 2026-07-04,R32,,3rd_5,3rd_6,,,FIFA World Cup,,,TRUE
89: 2026-07-04,R32,,3rd_7,3rd_8,,,FIFA World Cup,,,TRUE
90: 2026-07-05,R16,,W_R32_1,W_R32_2,,,FIFA World Cup,,,TRUE
91: 2026-07-05,R16,,W_R32_3,W_R32_4,,,FIFA World Cup,,,TRUE
92: 2026-07-06,R16,,W_R32_5,W_R32_6,,,FIFA World Cup,,,TRUE
93: 2026-07-06,R16,,W_R32_7,W_R32_8,,,FIFA World Cup,,,TRUE
94: 2026-07-07,R16,,W_R32_9,W_R32_10,,,FIFA World Cup,,,TRUE
95: 2026-07-07,R16,,W_R32_11,W_R32_12,,,FIFA World Cup,,,TRUE
96: 2026-07-08,R16,,W_R32_13,W_R32_14,,,FIFA World Cup,,,TRUE
97: 2026-07-08,R16,,W_R32_15,W_R32_16,,,FIFA World Cup,,,TRUE
98: 2026-07-09,QF,,W_R16_1,W_R16_2,,,FIFA World Cup,,,TRUE
99: 2026-07-10,QF,,W_R16_3,W_R16_4,,,FIFA World Cup,,,TRUE
100: 2026-07-11,QF,,W_R16_5,W_R16_6,,,FIFA World Cup,,,TRUE
101: 2026-07-11,QF,,W_R16_7,W_R16_8,,,FIFA World Cup,,,TRUE
102: 2026-07-14,SF,,W_QF1,W_QF2,,,FIFA World Cup,Dallas,USA,TRUE
103: 2026-07-15,SF,,W_QF3,W_QF4,,,FIFA World Cup,Atlanta,USA,TRUE
104: 2026-07-18,3RD,,L_SF1,L_SF2,,,FIFA World Cup,Miami,USA,TRUE
105: 2026-07-19,FINAL,,W_SF1,W_SF2,,,FIFA World Cup,East Rutherford,USA,TRUE

(End of file - total 105 lines)
</content>
```

---

## Assistant (Build · Nemotron 3 Ultra Free · 217.4s)

_Thinking:_

Now I need to replace lines 74-89 (the R32 section) with the correct FIFA official bracket. Let me write the corrected CSV file.

The official FIFA Round of 32 pairings (from the PDF Annex C and regulations):

1. 1E vs 3rd (from qualifying groups A,B,C,D,F) - Match 74
2. 1I vs 3rd (from qualifying groups C,D,F,G,H) - Match 75
3. 2A vs 2B - Match 73
4. 1F vs 2C - Match 76
5. 2K vs 2L - Match 77 (actually match 83 in PDF)
6. 1H vs 2J - Match 84
7. 1D vs 3rd (from qualifying groups B,E,F,I,J) - Match 81
8. 1G vs 3rd (from qualifying groups A,E,H,I,J) - Match 82
9. 1C vs 2F - Match 76 (in PDF)
10. 2E vs 2I - Match 78
11. 1A vs 3rd (from qualifying groups C,E,F,H,I) - Match 79
12. 1L vs 3rd (from qualifying groups E,H,I,J,K) - Match 80
13. 1J vs 2H - Match 86
14. 2D vs 2G - Match 88
15. 1B vs 3rd (from qualifying groups E,F,G,I,J) - Match 85
16. 1K vs 3rd (from qualifying groups D,E,I,J,L) - Match 87

Let me use the dates from the existing CSV and create proper R32 fixtures. The dates in the existing CSV for R32 are 2026-06-28 to 2026-07-04.

I'll create the corrected CSV.

**Tool: write**

**Input:**
```json
{}
```

**Error:**
```
Tool execution aborted
```

---

