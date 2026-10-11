# Equipment and performance (eqp) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_eqp_reasonCode | Entity | master | 23 | 19 | 3 | 6 |
| 2 | u_mes_eqp_equipmentState | Entity | transaction | 30 | 23 | 3 | 9 |
| 3 | u_mes_eqp_downtimeEvent | Entity | transaction | 47 | 31 | 2 | 8 |
| 4 | u_mes_eqp_downtimeEventComment | Child | transaction | 18 | 18 | 0 | 2 |
| 5 | u_mes_eqp_productionCount | Entity | transaction | 34 | 29 | 2 | 8 |
| 6 | u_mes_eqp_oeeRecord | Entity | transaction | 42 | 38 | 1 | 8 |
| 7 | u_mes_eqp_oeeRecordLoss | Child | transaction | 20 | 18 | 0 | 3 |
| 8 | u_mes_eqp_processTag | Entity | master | 28 | 24 | 4 | 5 |
| 9 | u_mes_eqp_processReading | Entity | transaction | 24 | 19 | 1 | 7 |
| 10 | u_mes_eqp_alarm | Entity | transaction | 36 | 23 | 2 | 8 |
| 11 | u_mes_eqp_torqueResult | Entity | transaction | 46 | 41 | 3 | 9 |
| 12 | u_mes_eqp_leakTestResult | Entity | transaction | 35 | 31 | 3 | 9 |
| 13 | u_mes_eqp_leakTestResultStage | Child | transaction | 24 | 24 | 2 | 1 |
| 14 | u_mes_eqp_lossCategory | Entity | master | 11 | 11 | 2 | 2 |
| 15 | u_mes_eqp_reasonCategory | Entity | master | 9 | 9 | 1 | 2 |
