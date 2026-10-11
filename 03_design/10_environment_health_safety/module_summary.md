# Environment Health and Safety (ehs) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_ehs_safetyIncident | Entity | transaction | 44 | 29 | 1 | 8 |
| 2 | u_mes_ehs_safetyIncidentWitnessUser | Relationship | transaction | 16 | 16 | 0 | 2 |
| 3 | u_mes_ehs_safetyIncidentAction | Child | transaction | 19 | 18 | 0 | 2 |
| 4 | u_mes_ehs_incidentType | Entity | master | 11 | 11 | 1 | 2 |
| 5 | u_mes_ehs_bodyPart | Entity | master | 9 | 9 | 1 | 2 |
| 6 | u_mes_ehs_injuryType | Entity | master | 9 | 9 | 1 | 2 |
