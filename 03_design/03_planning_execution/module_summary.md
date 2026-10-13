# Planning and Execution (plan) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_plan_customerSchedule | Entity | transaction | 24 | 21 | 3 | 5 |
| 2 | u_mes_plan_customerScheduleLine | Child | transaction | 24 | 24 | 2 | 2 |
| 3 | u_mes_plan_productionOrder | Entity | transaction | 59 | 38 | 4 | 8 |
| 4 | u_mes_plan_productionOrderRelease | Child | transaction | 19 | 16 | 1 | 1 |
| 5 | u_mes_plan_productionOrderLot | Relationship | transaction | 17 | 17 | 1 | 2 |
| 6 | u_mes_plan_productionSchedule | Entity | transaction | 28 | 25 | 2 | 6 |
| 7 | u_mes_plan_productionScheduleSlot | Child | transaction | 24 | 22 | 1 | 3 |
| 8 | u_mes_plan_dispatchList | Entity | transaction | 23 | 20 | 3 | 5 |
| 9 | u_mes_plan_dispatchListEntry | Child | transaction | 29 | 25 | 3 | 4 |
| 10 | u_mes_plan_operationExecution | Entity | transaction | 71 | 52 | 5 | 10 |
| 11 | u_mes_plan_operationExecutionDefectCode | Relationship | transaction | 17 | 17 | 1 | 2 |
| 12 | u_mes_plan_operationExecutionTool | Relationship | transaction | 17 | 17 | 1 | 2 |
| 13 | u_mes_plan_stepCompletion | Entity | transaction | 44 | 29 | 4 | 8 |
| 14 | u_mes_plan_wipUnit | Entity | transaction | 48 | 29 | 3 | 8 |
| 15 | u_mes_plan_wipUnitCompletedStep | Value list | transaction | 16 | 16 | 1 | 1 |
| 16 | u_mes_plan_lot | Entity | transaction | 51 | 25 | 4 | 8 |
| 17 | u_mes_plan_lotParentLot | Relationship | transaction | 17 | 17 | 1 | 2 |
| 18 | u_mes_plan_lotAttributesCavityNo | Value list | transaction | 16 | 16 | 1 | 1 |
| 19 | u_mes_plan_container | Entity | transaction | 40 | 28 | 2 | 8 |
| 20 | u_mes_plan_containerLot | Relationship | transaction | 17 | 17 | 1 | 2 |
| 21 | u_mes_plan_labourBooking | Entity | transaction | 43 | 24 | 4 | 8 |
| 22 | u_mes_plan_changeover | Entity | transaction | 41 | 28 | 3 | 8 |
| 23 | u_mes_plan_changeoverStep | Child | transaction | 20 | 17 | 2 | 1 |
| 24 | u_mes_plan_changeoverRemovedTool | Relationship | transaction | 17 | 17 | 1 | 2 |
| 25 | u_mes_plan_changeoverInstalledTool | Relationship | transaction | 17 | 17 | 1 | 2 |
| 26 | u_mes_plan_changeoverPerformedByUser | Relationship | transaction | 17 | 17 | 1 | 2 |
| 27 | u_mes_plan_shiftHandover | Entity | transaction | 33 | 27 | 2 | 7 |
| 28 | u_mes_plan_shiftHandoverProductionOrder | Relationship | transaction | 17 | 17 | 1 | 2 |
| 29 | u_mes_plan_shiftHandoverDowntimeEvent | Relationship | transaction | 17 | 17 | 1 | 2 |
| 30 | u_mes_plan_shiftHandoverNonconformance | Relationship | transaction | 17 | 17 | 1 | 2 |
| 31 | u_mes_plan_shiftHandoverOpenItem | Child | transaction | 20 | 20 | 1 | 2 |
| 32 | u_mes_plan_andonEvent | Entity | transaction | 46 | 29 | 3 | 8 |
| 33 | u_mes_plan_andonEventEscalation | Child | transaction | 20 | 20 | 2 | 2 |
| 34 | u_mes_plan_indirectActivity | Entity | master | 13 | 11 | 2 | 3 |
| 35 | u_mes_plan_containerType | Entity | master | 15 | 15 | 2 | 2 |
| 36 | u_mes_plan_andonType | Entity | master | 17 | 11 | 2 | 4 |
| 37 | u_mes_plan_operatorSession | Entity | transaction | 33 | 24 | 4 | 8 |
| 38 | u_mes_plan_documentAcknowledgement | Entity | transaction | 34 | 26 | 5 | 9 |
| 39 | u_mes_plan_interlockEvent | Entity | transaction | 51 | 21 | 2 | 9 |
| 40 | u_mes_plan_recipeDownload | Entity | transaction | 34 | 26 | 4 | 8 |
| 41 | u_mes_plan_setupVerification | Entity | transaction | 33 | 25 | 3 | 8 |
| 42 | u_mes_plan_setupVerificationItem | Child | transaction | 26 | 18 | 2 | 2 |
| 43 | u_mes_plan_lineClearance | Entity | transaction | 40 | 25 | 3 | 8 |
