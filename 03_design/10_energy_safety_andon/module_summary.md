# Energy, safety and andon (ehs) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_ehs_energyReading | Entity | transaction | 34 | 25 | 1 | 8 |
| 2 | u_mes_ehs_andonEvent | Entity | transaction | 38 | 27 | 1 | 8 |
| 3 | u_mes_ehs_andonEventEscalation | Child | transaction | 19 | 19 | 1 | 2 |
| 4 | u_mes_ehs_safetyIncident | Entity | transaction | 44 | 29 | 1 | 8 |
| 5 | u_mes_ehs_safetyIncidentWitnessUser | Relationship | transaction | 16 | 16 | 0 | 2 |
| 6 | u_mes_ehs_safetyIncidentAction | Child | transaction | 19 | 18 | 0 | 2 |
| 7 | u_mes_ehs_andonType | Entity | master | 13 | 10 | 1 | 3 |
| 8 | u_mes_ehs_incidentType | Entity | master | 11 | 11 | 1 | 2 |
| 9 | u_mes_ehs_energyType | Entity | master | 11 | 9 | 1 | 3 |
| 10 | u_mes_ehs_bodyPart | Entity | master | 9 | 9 | 1 | 2 |
| 11 | u_mes_ehs_injuryType | Entity | master | 9 | 9 | 1 | 2 |
