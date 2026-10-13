# Traceability (trac) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_trac_serialNumber | Entity | transaction | 44 | 20 | 3 | 9 |
| 2 | u_mes_trac_genealogyLink | Entity | transaction | 44 | 27 | 4 | 8 |
| 3 | u_mes_trac_componentLotLink | Entity | transaction | 33 | 29 | 3 | 8 |
| 4 | u_mes_trac_asBuiltRecord | Entity | transaction | 54 | 29 | 3 | 8 |
| 5 | u_mes_trac_asBuiltRecordComponent | Child | transaction | 23 | 19 | 1 | 4 |
| 6 | u_mes_trac_asBuiltRecordOperation | Child | transaction | 29 | 20 | 2 | 4 |
| 7 | u_mes_trac_asBuiltRecordInspectionResult | Relationship | transaction | 17 | 17 | 1 | 2 |
| 8 | u_mes_trac_traceInvestigation | Entity | transaction | 33 | 24 | 4 | 8 |
| 9 | u_mes_trac_traceInvestigationResult | Child | transaction | 29 | 23 | 2 | 4 |
