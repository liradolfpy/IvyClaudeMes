# Tooling & Maintenance (maint) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_maint_maintenancePlan | Entity | master | 24 | 18 | 5 | 5 |
| 2 | u_mes_maint_maintenancePlanTask | Child | master | 12 | 11 | 0 | 1 |
| 3 | u_mes_maint_maintenancePlanRequiredSkill | Relationship | master | 10 | 10 | 0 | 2 |
| 4 | u_mes_maint_maintenancePlanRequiredSparePart | Child | master | 11 | 11 | 0 | 2 |
| 5 | u_mes_maint_maintenanceWorkOrder | Entity | transaction | 56 | 30 | 4 | 8 |
| 6 | u_mes_maint_maintenanceWorkOrderAssignedToUser | Relationship | transaction | 16 | 16 | 0 | 2 |
| 7 | u_mes_maint_maintenanceWorkOrderLabour | Child | transaction | 17 | 17 | 0 | 2 |
| 8 | u_mes_maint_maintenanceWorkOrderUsedSparePart | Child | transaction | 18 | 18 | 0 | 2 |
| 9 | u_mes_maint_sparePart | Entity | master | 26 | 20 | 3 | 6 |
| 10 | u_mes_maint_sparePartUsedOnEquipment | Relationship | master | 10 | 10 | 0 | 2 |
| 11 | u_mes_maint_tool | Entity | master | 38 | 26 | 3 | 7 |
| 12 | u_mes_maint_toolItem | Relationship | master | 10 | 10 | 0 | 2 |
| 13 | u_mes_maint_toolLifeRecord | Entity | transaction | 39 | 22 | 2 | 8 |
| 14 | u_mes_maint_toolType | Entity | master | 10 | 10 | 2 | 2 |
| 15 | u_mes_maint_maintenanceWorkOrderTask | Child | transaction | 25 | 16 | 1 | 3 |
| 16 | u_mes_maint_sparePartTransaction | Entity | transaction | 30 | 25 | 2 | 8 |
| 17 | u_mes_maint_reliabilitySummary | Entity | transaction | 28 | 24 | 2 | 6 |
| 18 | u_mes_maint_equipmentLifecycleEvent | Entity | transaction | 30 | 17 | 2 | 7 |
| 19 | u_mes_maint_logbookEntry | Entity | transaction | 34 | 20 | 3 | 9 |
| 20 | u_mes_maint_cleaningRecord | Entity | transaction | 36 | 23 | 4 | 8 |
| 21 | u_mes_maint_equipmentQualification | Entity | transaction | 34 | 20 | 2 | 8 |
