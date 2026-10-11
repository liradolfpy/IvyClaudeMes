# Maintenance and tooling (mnt) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_mnt_maintenancePlan | Entity | master | 24 | 18 | 5 | 5 |
| 2 | u_mes_mnt_maintenancePlanTask | Child | master | 12 | 11 | 0 | 1 |
| 3 | u_mes_mnt_maintenancePlanRequiredSkill | Relationship | master | 10 | 10 | 0 | 2 |
| 4 | u_mes_mnt_maintenancePlanRequiredSparePart | Child | master | 11 | 11 | 0 | 2 |
| 5 | u_mes_mnt_maintenanceWorkOrder | Entity | transaction | 43 | 29 | 3 | 8 |
| 6 | u_mes_mnt_maintenanceWorkOrderAssignedToUser | Relationship | transaction | 16 | 16 | 0 | 2 |
| 7 | u_mes_mnt_maintenanceWorkOrderLabour | Child | transaction | 17 | 17 | 0 | 2 |
| 8 | u_mes_mnt_maintenanceWorkOrderUsedSparePart | Child | transaction | 18 | 18 | 0 | 2 |
| 9 | u_mes_mnt_sparePart | Entity | master | 26 | 20 | 3 | 6 |
| 10 | u_mes_mnt_sparePartUsedOnEquipment | Relationship | master | 10 | 10 | 0 | 2 |
| 11 | u_mes_mnt_tool | Entity | master | 33 | 25 | 3 | 7 |
| 12 | u_mes_mnt_toolItem | Relationship | master | 10 | 10 | 0 | 2 |
| 13 | u_mes_mnt_toolLifeRecord | Entity | transaction | 33 | 22 | 2 | 7 |
| 14 | u_mes_mnt_toolType | Entity | master | 10 | 10 | 2 | 2 |
