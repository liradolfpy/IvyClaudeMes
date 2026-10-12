# Traceability (trac) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_trac_serialNumber | Entity | transaction | 43 | 19 | 2 | 9 |
| 2 | u_mes_trac_genealogyLink | Entity | transaction | 43 | 26 | 3 | 8 |
| 3 | u_mes_trac_componentLotLink | Entity | transaction | 32 | 28 | 2 | 8 |
| 4 | u_mes_trac_asBuiltRecord | Entity | transaction | 53 | 36 | 2 | 8 |
| 5 | u_mes_trac_asBuiltRecordComponent | Child | transaction | 22 | 18 | 0 | 4 |
| 6 | u_mes_trac_asBuiltRecordOperation | Child | transaction | 28 | 19 | 1 | 4 |
| 7 | u_mes_trac_asBuiltRecordInspectionResult | Relationship | transaction | 16 | 16 | 0 | 2 |
| 8 | u_mes_trac_traceInvestigation | Entity | transaction | 32 | 23 | 3 | 8 |
| 9 | u_mes_trac_traceInvestigationResult | Child | transaction | 28 | 22 | 1 | 4 |
