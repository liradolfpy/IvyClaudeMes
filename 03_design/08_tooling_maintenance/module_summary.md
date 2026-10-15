# ToolingAndMaintenance (maint) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_maint_maintenancePlan | Entity | master | 25 | 19 | 6 | 5 |
| 2 | u_mes_maint_maintenancePlanTask | Child | master | 13 | 12 | 1 | 1 |
| 3 | u_mes_maint_maintenancePlanRequiredSkill | Relationship | master | 11 | 11 | 1 | 2 |
| 4 | u_mes_maint_maintenancePlanRequiredSparePart | Child | master | 12 | 12 | 1 | 2 |
| 5 | u_mes_maint_maintenanceWorkOrder | Entity | transaction | 57 | 31 | 5 | 8 |
| 6 | u_mes_maint_maintenanceWorkOrderAssignedToUser | Relationship | transaction | 17 | 17 | 1 | 2 |
| 7 | u_mes_maint_maintenanceWorkOrderLabour | Child | transaction | 18 | 18 | 1 | 2 |
| 8 | u_mes_maint_maintenanceWorkOrderUsedSparePart | Child | transaction | 19 | 19 | 1 | 2 |
| 9 | u_mes_maint_sparePart | Entity | master | 27 | 21 | 4 | 6 |
| 10 | u_mes_maint_sparePartUsedOnEquipment | Relationship | master | 11 | 11 | 1 | 2 |
| 11 | u_mes_maint_tool | Entity | master | 39 | 27 | 4 | 7 |
| 12 | u_mes_maint_toolItem | Relationship | master | 11 | 11 | 1 | 2 |
| 13 | u_mes_maint_toolLifeRecord | Entity | transaction | 40 | 23 | 3 | 8 |
| 14 | u_mes_maint_toolType | Entity | master | 11 | 11 | 3 | 2 |
| 15 | u_mes_maint_maintenanceWorkOrderTask | Child | transaction | 26 | 17 | 2 | 3 |
| 16 | u_mes_maint_sparePartTransaction | Entity | transaction | 31 | 26 | 3 | 8 |
| 17 | u_mes_maint_reliabilitySummary | Entity | transaction | 29 | 25 | 3 | 6 |
| 18 | u_mes_maint_equipmentLifecycleEvent | Entity | transaction | 31 | 18 | 3 | 7 |
| 19 | u_mes_maint_logbookEntry | Entity | transaction | 35 | 21 | 4 | 9 |
| 20 | u_mes_maint_cleaningRecord | Entity | transaction | 37 | 24 | 5 | 8 |
| 21 | u_mes_maint_equipmentQualification | Entity | transaction | 35 | 21 | 3 | 8 |
