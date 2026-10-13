# Planning and Execution (plan) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_plan_customerSchedule | Entity | transaction | 23 | 20 | 2 | 5 |
| 2 | u_mes_plan_customerScheduleLine | Child | transaction | 23 | 23 | 1 | 2 |
| 3 | u_mes_plan_productionOrder | Entity | transaction | 58 | 37 | 3 | 8 |
| 4 | u_mes_plan_productionOrderRelease | Child | transaction | 18 | 15 | 0 | 1 |
| 5 | u_mes_plan_productionOrderLot | Relationship | transaction | 16 | 16 | 0 | 2 |
| 6 | u_mes_plan_productionSchedule | Entity | transaction | 27 | 24 | 1 | 6 |
| 7 | u_mes_plan_productionScheduleSlot | Child | transaction | 23 | 21 | 0 | 3 |
| 8 | u_mes_plan_dispatchList | Entity | transaction | 22 | 19 | 2 | 5 |
| 9 | u_mes_plan_dispatchListEntry | Child | transaction | 28 | 24 | 2 | 4 |
| 10 | u_mes_plan_operationExecution | Entity | transaction | 70 | 51 | 4 | 10 |
| 11 | u_mes_plan_operationExecutionDefectCode | Relationship | transaction | 16 | 16 | 0 | 2 |
| 12 | u_mes_plan_operationExecutionTool | Relationship | transaction | 16 | 16 | 0 | 2 |
| 13 | u_mes_plan_stepCompletion | Entity | transaction | 43 | 28 | 3 | 8 |
| 14 | u_mes_plan_wipUnit | Entity | transaction | 47 | 30 | 2 | 8 |
| 15 | u_mes_plan_wipUnitCompletedStep | Value list | transaction | 15 | 15 | 0 | 1 |
| 16 | u_mes_plan_lot | Entity | transaction | 50 | 24 | 3 | 8 |
| 17 | u_mes_plan_lotParentLot | Relationship | transaction | 16 | 16 | 0 | 2 |
| 18 | u_mes_plan_lotAttributesCavityNo | Value list | transaction | 15 | 15 | 0 | 1 |
| 19 | u_mes_plan_container | Entity | transaction | 39 | 27 | 1 | 8 |
| 20 | u_mes_plan_containerLot | Relationship | transaction | 16 | 16 | 0 | 2 |
| 21 | u_mes_plan_labourBooking | Entity | transaction | 42 | 23 | 3 | 8 |
| 22 | u_mes_plan_changeover | Entity | transaction | 40 | 27 | 2 | 8 |
| 23 | u_mes_plan_changeoverStep | Child | transaction | 19 | 16 | 1 | 1 |
| 24 | u_mes_plan_changeoverRemovedTool | Relationship | transaction | 16 | 16 | 0 | 2 |
| 25 | u_mes_plan_changeoverInstalledTool | Relationship | transaction | 16 | 16 | 0 | 2 |
| 26 | u_mes_plan_changeoverPerformedByUser | Relationship | transaction | 16 | 16 | 0 | 2 |
| 27 | u_mes_plan_shiftHandover | Entity | transaction | 32 | 26 | 1 | 7 |
| 28 | u_mes_plan_shiftHandoverProductionOrder | Relationship | transaction | 16 | 16 | 0 | 2 |
| 29 | u_mes_plan_shiftHandoverDowntimeEvent | Relationship | transaction | 16 | 16 | 0 | 2 |
| 30 | u_mes_plan_shiftHandoverNonconformance | Relationship | transaction | 16 | 16 | 0 | 2 |
| 31 | u_mes_plan_shiftHandoverOpenItem | Child | transaction | 19 | 19 | 0 | 2 |
| 32 | u_mes_plan_andonEvent | Entity | transaction | 45 | 28 | 2 | 8 |
| 33 | u_mes_plan_andonEventEscalation | Child | transaction | 19 | 19 | 1 | 2 |
| 34 | u_mes_plan_indirectActivity | Entity | master | 12 | 10 | 1 | 3 |
| 35 | u_mes_plan_containerType | Entity | master | 14 | 14 | 1 | 2 |
| 36 | u_mes_plan_andonType | Entity | master | 16 | 10 | 1 | 4 |
| 37 | u_mes_plan_operatorSession | Entity | transaction | 32 | 23 | 3 | 8 |
| 38 | u_mes_plan_documentAcknowledgement | Entity | transaction | 33 | 25 | 4 | 9 |
| 39 | u_mes_plan_interlockEvent | Entity | transaction | 50 | 20 | 1 | 9 |
| 40 | u_mes_plan_recipeDownload | Entity | transaction | 33 | 25 | 3 | 8 |
| 41 | u_mes_plan_setupVerification | Entity | transaction | 32 | 24 | 2 | 8 |
| 42 | u_mes_plan_setupVerificationItem | Child | transaction | 25 | 17 | 1 | 2 |
| 43 | u_mes_plan_lineClearance | Entity | transaction | 39 | 24 | 2 | 8 |
