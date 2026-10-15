# EnvironmentHealthAndSafety (ehs) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_ehs_safetyIncident | Entity | transaction | 45 | 30 | 2 | 8 |
| 2 | u_mes_ehs_safetyIncidentWitnessUser | Relationship | transaction | 17 | 17 | 1 | 2 |
| 3 | u_mes_ehs_safetyIncidentAction | Child | transaction | 20 | 19 | 1 | 2 |
| 4 | u_mes_ehs_incidentType | Entity | master | 12 | 12 | 2 | 2 |
| 5 | u_mes_ehs_bodyPart | Entity | master | 10 | 10 | 2 | 2 |
| 6 | u_mes_ehs_injuryType | Entity | master | 10 | 10 | 2 | 2 |
