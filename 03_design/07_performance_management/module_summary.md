# Performance Management (perf) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_perf_reasonCode | Entity | master | 24 | 20 | 4 | 6 |
| 2 | u_mes_perf_equipmentState | Entity | transaction | 31 | 24 | 4 | 9 |
| 3 | u_mes_perf_downtimeEvent | Entity | transaction | 55 | 33 | 4 | 8 |
| 4 | u_mes_perf_downtimeEventComment | Child | transaction | 19 | 19 | 1 | 2 |
| 5 | u_mes_perf_productionCount | Entity | transaction | 35 | 30 | 3 | 8 |
| 6 | u_mes_perf_oeeRecord | Entity | transaction | 43 | 39 | 2 | 8 |
| 7 | u_mes_perf_oeeRecordLoss | Child | transaction | 21 | 19 | 1 | 3 |
| 8 | u_mes_perf_processTag | Entity | master | 35 | 25 | 5 | 7 |
| 9 | u_mes_perf_processReading | Entity | transaction | 30 | 20 | 2 | 8 |
| 10 | u_mes_perf_alarm | Entity | transaction | 55 | 26 | 3 | 8 |
| 11 | u_mes_perf_torqueResult | Entity | transaction | 52 | 42 | 5 | 9 |
| 12 | u_mes_perf_leakTestResult | Entity | transaction | 38 | 32 | 4 | 9 |
| 13 | u_mes_perf_leakTestResultStage | Child | transaction | 25 | 25 | 3 | 1 |
| 14 | u_mes_perf_energyReading | Entity | transaction | 35 | 26 | 2 | 8 |
| 15 | u_mes_perf_lossCategory | Entity | master | 12 | 12 | 3 | 2 |
| 16 | u_mes_perf_reasonCategory | Entity | master | 10 | 10 | 2 | 2 |
| 17 | u_mes_perf_energyType | Entity | master | 12 | 10 | 2 | 3 |
| 18 | u_mes_perf_alarmDefinition | Entity | master | 22 | 15 | 4 | 6 |
| 19 | u_mes_perf_lossSummary | Entity | transaction | 34 | 32 | 2 | 8 |
| 20 | u_mes_perf_workCenterPerformance | Entity | transaction | 35 | 33 | 2 | 7 |
| 21 | u_mes_perf_operatorPerformance | Entity | transaction | 30 | 28 | 2 | 7 |
