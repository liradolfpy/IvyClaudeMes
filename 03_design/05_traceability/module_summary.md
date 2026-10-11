# Traceability (trc) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_trc_serialNumber | Entity | transaction | 40 | 19 | 2 | 9 |
| 2 | u_mes_trc_genealogyLink | Entity | transaction | 39 | 26 | 3 | 8 |
| 3 | u_mes_trc_componentLotLink | Entity | transaction | 32 | 28 | 2 | 8 |
| 4 | u_mes_trc_asBuiltRecord | Entity | transaction | 51 | 34 | 2 | 8 |
| 5 | u_mes_trc_asBuiltRecordComponent | Child | transaction | 22 | 18 | 0 | 4 |
| 6 | u_mes_trc_asBuiltRecordOperation | Child | transaction | 24 | 19 | 1 | 4 |
| 7 | u_mes_trc_asBuiltRecordInspectionResult | Relationship | transaction | 16 | 16 | 0 | 2 |
