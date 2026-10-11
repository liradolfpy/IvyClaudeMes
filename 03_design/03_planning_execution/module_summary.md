# Planning and execution (exe) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_exe_customerSchedule | Entity | transaction | 23 | 20 | 2 | 5 |
| 2 | u_mes_exe_customerScheduleLine | Child | transaction | 23 | 23 | 1 | 2 |
| 3 | u_mes_exe_productionOrder | Entity | transaction | 47 | 35 | 3 | 8 |
| 4 | u_mes_exe_productionOrderRelease | Child | transaction | 18 | 15 | 0 | 1 |
| 5 | u_mes_exe_productionOrderLot | Relationship | transaction | 16 | 16 | 0 | 2 |
| 6 | u_mes_exe_productionSchedule | Entity | transaction | 27 | 24 | 1 | 6 |
| 7 | u_mes_exe_productionScheduleSlot | Child | transaction | 23 | 21 | 0 | 3 |
| 8 | u_mes_exe_dispatchList | Entity | transaction | 22 | 19 | 2 | 5 |
| 9 | u_mes_exe_dispatchListEntry | Child | transaction | 28 | 24 | 2 | 4 |
| 10 | u_mes_exe_operationExecution | Entity | transaction | 53 | 42 | 3 | 10 |
| 11 | u_mes_exe_operationExecutionDefectCode | Relationship | transaction | 16 | 16 | 0 | 2 |
| 12 | u_mes_exe_operationExecutionTool | Relationship | transaction | 16 | 16 | 0 | 2 |
| 13 | u_mes_exe_stepCompletion | Entity | transaction | 40 | 28 | 3 | 8 |
| 14 | u_mes_exe_wipUnit | Entity | transaction | 47 | 30 | 2 | 8 |
| 15 | u_mes_exe_wipUnitCompletedStep | Value list | transaction | 15 | 15 | 0 | 1 |
| 16 | u_mes_exe_lot | Entity | transaction | 47 | 24 | 3 | 8 |
| 17 | u_mes_exe_lotParentLot | Relationship | transaction | 16 | 16 | 0 | 2 |
| 18 | u_mes_exe_lotAttributesCavityNo | Value list | transaction | 15 | 15 | 0 | 1 |
| 19 | u_mes_exe_container | Entity | transaction | 39 | 27 | 1 | 8 |
| 20 | u_mes_exe_containerLot | Relationship | transaction | 16 | 16 | 0 | 2 |
| 21 | u_mes_exe_labourBooking | Entity | transaction | 36 | 23 | 3 | 8 |
| 22 | u_mes_exe_changeover | Entity | transaction | 40 | 27 | 2 | 8 |
| 23 | u_mes_exe_changeoverStep | Child | transaction | 19 | 16 | 1 | 1 |
| 24 | u_mes_exe_changeoverRemovedTool | Relationship | transaction | 16 | 16 | 0 | 2 |
| 25 | u_mes_exe_changeoverInstalledTool | Relationship | transaction | 16 | 16 | 0 | 2 |
| 26 | u_mes_exe_changeoverPerformedByUser | Relationship | transaction | 16 | 16 | 0 | 2 |
| 27 | u_mes_exe_shiftHandover | Entity | transaction | 32 | 26 | 1 | 7 |
| 28 | u_mes_exe_shiftHandoverProductionOrder | Relationship | transaction | 16 | 16 | 0 | 2 |
| 29 | u_mes_exe_shiftHandoverDowntimeEvent | Relationship | transaction | 16 | 16 | 0 | 2 |
| 30 | u_mes_exe_shiftHandoverNonconformance | Relationship | transaction | 16 | 16 | 0 | 2 |
| 31 | u_mes_exe_shiftHandoverOpenItem | Child | transaction | 19 | 19 | 0 | 2 |
| 32 | u_mes_exe_indirectActivity | Entity | master | 12 | 10 | 1 | 3 |
| 33 | u_mes_exe_containerType | Entity | master | 14 | 14 | 1 | 2 |
