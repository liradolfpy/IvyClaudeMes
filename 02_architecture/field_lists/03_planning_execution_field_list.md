# Field list - PlanningAndExecution (plan)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/03_planning_execution/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = n.nn (plain number, no NumberDecimal()); Double = Double(n); Boolean = true / false.

## u_mes_plan_customerSchedule

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | customerId | String | - | u_mes_mast_customer._id |
| 7 | customerName | String | - |  |
| 8 | shipToCode | String | - |  |
| 9 | scheduleType | String | - |  |
| 10 | customerOrderNo | String | - |  |
| 11 | receivedAt | Date | Datetime |  |
| 12 | horizonFrom | Date | Date |  |
| 13 | horizonTo | Date | Date |  |
| 14 | supersedesCustomerScheduleId | String | - | u_mes_plan_customerSchedule._id |
| 15 | supersedesCustomerScheduleName | String | - |  |
| 16 | erpSalesOrderNo | String | - |  |
| 17 | status | String | - |  |
| 18 | schemaVersion | Int32 | - |  |
| 19 | createdAt | Date | Datetime |  |
| 20 | createdById | String | - | u_mes_mast_user._id |
| 21 | createdBy | String | - |  |
| 22 | updatedAt | Date | Datetime |  |
| 23 | updatedById | String | - | u_mes_mast_user._id |
| 24 | updatedBy | String | - |  |

## u_mes_plan_customerScheduleLine

Kind: child | Data class: transaction | Parent: u_mes_plan_customerSchedule | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | customerScheduleId | String | - | u_mes_plan_customerSchedule._id |
| 7 | customerScheduleName | String | - |  |
| 8 | lineNo | Int32 | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | customerPartNo | String | - |  |
| 12 | dueDate | Date | Date |  |
| 13 | quantity | Int32 | - |  |
| 14 | cumulativeRequired | Int32 | - |  |
| 15 | cumulativeShipped | Int32 | - |  |
| 16 | firmness | String | - |  |
| 17 | shippedQuantity | Int32 | - |  |
| 18 | schemaVersion | Int32 | - |  |
| 19 | createdAt | Date | Datetime |  |
| 20 | createdById | String | - | u_mes_mast_user._id |
| 21 | createdBy | String | - |  |
| 22 | updatedAt | Date | Datetime |  |
| 23 | updatedById | String | - | u_mes_mast_user._id |
| 24 | updatedBy | String | - |  |

## u_mes_plan_productionOrder

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | erpOrderNo | String | - |  |
| 7 | itemId | String | - | u_mes_prod_item._id |
| 8 | itemName | String | - |  |
| 9 | itemRevision | String | - |  |
| 10 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 11 | productVariantName | String | - |  |
| 12 | billOfMaterialId | String | - | u_mes_prod_billOfMaterial._id |
| 13 | billOfMaterialName | String | - |  |
| 14 | routingId | String | - | u_mes_prod_routing._id |
| 15 | routingName | String | - |  |
| 16 | lineId | String | - | u_mes_mast_line._id |
| 17 | lineName | String | - |  |
| 18 | customerScheduleId | String | - | u_mes_plan_customerSchedule._id |
| 19 | customerScheduleName | String | - |  |
| 20 | orderType | String | - |  |
| 21 | priority | String | - |  |
| 22 | plannedQuantity | Int32 | - |  |
| 23 | releasedQuantity | Int32 | - |  |
| 24 | startedQuantity | Int32 | - |  |
| 25 | goodQuantity | Int32 | - |  |
| 26 | scrapQuantity | Int32 | - |  |
| 27 | reworkQuantity | Int32 | - |  |
| 28 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 29 | unitOfMeasureName | String | - |  |
| 30 | plannedStartAt | Date | Datetime |  |
| 31 | plannedEndAt | Date | Datetime |  |
| 32 | actualStartAt | Date | Datetime |  |
| 33 | actualEndAt | Date | Datetime |  |
| 34 | dueDate | Date | Date |  |
| 35 | erpMessageId | String | - | u_mes_syst_erpMessage._id |
| 36 | erpMessageName | String | - |  |
| 37 | closedAt | Date | Datetime |  |
| 38 | closedById | String | - | u_mes_mast_user._id |
| 39 | closedBy | String | - |  |
| 40 | remarks | String | - |  |
| 41 | onHold | Boolean | - |  |
| 42 | qualityHoldId | String | - | u_mes_qual_qualityHold._id |
| 43 | qualityHoldName | String | - |  |
| 44 | holdReasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 45 | holdReasonCodeName | String | - |  |
| 46 | genealogyComplete | Boolean | - |  |
| 47 | batchRecordReviewId | String | - | u_mes_bmr_batchRecordReview._id |
| 48 | batchRecordReviewName | String | - |  |
| 49 | lineClearanceId | String | - | u_mes_plan_lineClearance._id |
| 50 | lineClearanceName | String | - |  |
| 51 | yieldWithinLimits | Boolean | - |  |
| 52 | status | String | - |  |
| 53 | schemaVersion | Int32 | - |  |
| 54 | createdAt | Date | Datetime |  |
| 55 | createdById | String | - | u_mes_mast_user._id |
| 56 | createdBy | String | - |  |
| 57 | updatedAt | Date | Datetime |  |
| 58 | updatedById | String | - | u_mes_mast_user._id |
| 59 | updatedBy | String | - |  |

## u_mes_plan_productionOrderRelease

Kind: child | Data class: transaction | Parent: u_mes_plan_productionOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - |  |
| 8 | releaseNo | Int32 | - |  |
| 9 | quantity | Int32 | - |  |
| 10 | releasedAt | Date | Datetime |  |
| 11 | releasedById | String | - | u_mes_mast_user._id |
| 12 | releasedBy | String | - |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_plan_productionOrderLot

Kind: relationship | Data class: transaction | Parent: u_mes_plan_productionOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | lotId | String | - | u_mes_plan_lot._id |
| 10 | lotName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_plan_productionSchedule

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | productionDate | Date | Date |  |
| 7 | lineId | String | - | u_mes_mast_line._id |
| 8 | lineName | String | - |  |
| 9 | shiftId | String | - | u_mes_mast_shift._id |
| 10 | shiftName | String | - |  |
| 11 | workCalendarId | String | - | u_mes_mast_workCalendar._id |
| 12 | workCalendarName | String | - |  |
| 13 | scheduleVersion | Int32 | - |  |
| 14 | plannedOutput | Int32 | - |  |
| 15 | actualOutput | Int32 | - |  |
| 16 | attainmentPct | Decimal128 | - |  |
| 17 | frozen | Boolean | - |  |
| 18 | publishedAt | Date | Datetime |  |
| 19 | publishedById | String | - | u_mes_mast_user._id |
| 20 | publishedBy | String | - |  |
| 21 | status | String | - |  |
| 22 | schemaVersion | Int32 | - |  |
| 23 | createdAt | Date | Datetime |  |
| 24 | createdById | String | - | u_mes_mast_user._id |
| 25 | createdBy | String | - |  |
| 26 | updatedAt | Date | Datetime |  |
| 27 | updatedById | String | - | u_mes_mast_user._id |
| 28 | updatedBy | String | - |  |

## u_mes_plan_productionScheduleSlot

Kind: child | Data class: transaction | Parent: u_mes_plan_productionSchedule | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | productionScheduleId | String | - | u_mes_plan_productionSchedule._id |
| 7 | productionScheduleName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 10 | productionOrderName | String | - |  |
| 11 | itemId | String | - | u_mes_prod_item._id |
| 12 | itemName | String | - |  |
| 13 | plannedQuantity | Int32 | - |  |
| 14 | plannedStartAt | Date | Datetime |  |
| 15 | plannedEndAt | Date | Datetime |  |
| 16 | changeoverMinutes | Int32 | - |  |
| 17 | actualQuantity | Int32 | - |  |
| 18 | schemaVersion | Int32 | - |  |
| 19 | createdAt | Date | Datetime |  |
| 20 | createdById | String | - | u_mes_mast_user._id |
| 21 | createdBy | String | - |  |
| 22 | updatedAt | Date | Datetime |  |
| 23 | updatedById | String | - | u_mes_mast_user._id |
| 24 | updatedBy | String | - |  |

## u_mes_plan_dispatchList

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 7 | workCenterName | String | - |  |
| 8 | shiftId | String | - | u_mes_mast_shift._id |
| 9 | shiftName | String | - |  |
| 10 | productionDate | Date | Date |  |
| 11 | generatedAt | Date | Datetime |  |
| 12 | rule | String | - |  |
| 13 | acknowledgedById | String | - | u_mes_mast_user._id |
| 14 | acknowledgedBy | String | - |  |
| 15 | acknowledgedAt | Date | Datetime |  |
| 16 | status | String | - |  |
| 17 | schemaVersion | Int32 | - |  |
| 18 | createdAt | Date | Datetime |  |
| 19 | createdById | String | - | u_mes_mast_user._id |
| 20 | createdBy | String | - |  |
| 21 | updatedAt | Date | Datetime |  |
| 22 | updatedById | String | - | u_mes_mast_user._id |
| 23 | updatedBy | String | - |  |

## u_mes_plan_dispatchListEntry

Kind: child | Data class: transaction | Parent: u_mes_plan_dispatchList | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | dispatchListId | String | - | u_mes_plan_dispatchList._id |
| 7 | dispatchListName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | rank | Int32 | - |  |
| 10 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 11 | productionOrderName | String | - |  |
| 12 | lotId | String | - | u_mes_plan_lot._id |
| 13 | lotName | String | - |  |
| 14 | itemId | String | - | u_mes_prod_item._id |
| 15 | itemName | String | - |  |
| 16 | quantity | Int32 | - |  |
| 17 | dueAt | Date | Datetime |  |
| 18 | queueSince | Date | Datetime |  |
| 19 | priority | String | - |  |
| 20 | materialAvailable | Boolean | - |  |
| 21 | toolAvailable | Boolean | - |  |
| 22 | status | String | - |  |
| 23 | schemaVersion | Int32 | - |  |
| 24 | createdAt | Date | Datetime |  |
| 25 | createdById | String | - | u_mes_mast_user._id |
| 26 | createdBy | String | - |  |
| 27 | updatedAt | Date | Datetime |  |
| 28 | updatedById | String | - | u_mes_mast_user._id |
| 29 | updatedBy | String | - |  |

## u_mes_plan_operationExecution

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - |  |
| 8 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 9 | wipUnitName | String | - |  |
| 10 | lotId | String | - | u_mes_plan_lot._id |
| 11 | lotName | String | - |  |
| 12 | itemId | String | - | u_mes_prod_item._id |
| 13 | itemName | String | - |  |
| 14 | routingId | String | - | u_mes_prod_routing._id |
| 15 | routingName | String | - |  |
| 16 | stepNo | Int32 | - |  |
| 17 | operationId | String | - | u_mes_prod_operation._id |
| 18 | operationName | String | - |  |
| 19 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 20 | workCenterName | String | - |  |
| 21 | equipmentId | String | - | u_mes_mast_equipment._id |
| 22 | equipmentName | String | - |  |
| 23 | recipeId | String | - | u_mes_prod_recipe._id |
| 24 | recipeName | String | - |  |
| 25 | shiftId | String | - | u_mes_mast_shift._id |
| 26 | shiftName | String | - |  |
| 27 | operatorUserId | String | - | u_mes_mast_user._id |
| 28 | operatorUserName | String | - |  |
| 29 | executionType | String | - |  |
| 30 | attemptNo | Int32 | - |  |
| 31 | startedAt | Date | Datetime |  |
| 32 | completedAt | Date | Datetime |  |
| 33 | cycleTimeSec | Decimal128 | - |  |
| 34 | standardCycleTimeSec | Decimal128 | - |  |
| 35 | quantityIn | Int32 | - |  |
| 36 | quantityGood | Int32 | - |  |
| 37 | quantityReject | Int32 | - |  |
| 38 | quantityRework | Int32 | - |  |
| 39 | result | String | - |  |
| 40 | checksSkillVerified | Boolean | - |  |
| 41 | checksRecipeVerified | Boolean | - |  |
| 42 | checksToolLifeOk | Boolean | - |  |
| 43 | checksGaugeCalibrationOk | Boolean | - |  |
| 44 | checksPreviousStepComplete | Boolean | - |  |
| 45 | nextStepNo | Int32 | - |  |
| 46 | remarks | String | - |  |
| 47 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 48 | productVariantName | String | - |  |
| 49 | recipeVersion | String | - |  |
| 50 | recipeChecksum | String | - |  |
| 51 | taktTimeSec | Decimal128 | - |  |
| 52 | taktBreached | Boolean | - |  |
| 53 | captureMethod | String | - |  |
| 54 | startScanCode | String | - |  |
| 55 | operatorSessionId | String | - | u_mes_plan_operatorSession._id |
| 56 | operatorSessionName | String | - |  |
| 57 | checksVariantVerified | Boolean | - |  |
| 58 | checksDocumentAcknowledged | Boolean | - |  |
| 59 | checksEquipmentReady | Boolean | - |  |
| 60 | checksMaterialReleased | Boolean | - |  |
| 61 | checksSetupVerified | Boolean | - |  |
| 62 | checksEnvironmentOk | Boolean | - |  |
| 63 | interlockEventCount | Int32 | - |  |
| 64 | status | String | - |  |
| 65 | schemaVersion | Int32 | - |  |
| 66 | createdAt | Date | Datetime |  |
| 67 | createdById | String | - | u_mes_mast_user._id |
| 68 | createdBy | String | - |  |
| 69 | updatedAt | Date | Datetime |  |
| 70 | updatedById | String | - | u_mes_mast_user._id |
| 71 | updatedBy | String | - |  |

## u_mes_plan_operationExecutionDefectCode

Kind: relationship | Data class: transaction | Parent: u_mes_plan_operationExecution | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 7 | operationExecutionName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | defectCodeId | String | - | u_mes_qual_defectCode._id |
| 10 | defectCodeName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_plan_operationExecutionTool

Kind: relationship | Data class: transaction | Parent: u_mes_plan_operationExecution | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 7 | operationExecutionName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | toolId | String | - | u_mes_maint_tool._id |
| 10 | toolName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_plan_stepCompletion

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 7 | operationExecutionName | String | - |  |
| 8 | workInstructionId | String | - | u_mes_prod_workInstruction._id |
| 9 | workInstructionName | String | - |  |
| 10 | workInstructionVersion | Int32 | - |  |
| 11 | stepNo | Int32 | - |  |
| 12 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 13 | wipUnitName | String | - |  |
| 14 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 15 | workCenterName | String | - |  |
| 16 | userId | String | - | u_mes_mast_user._id |
| 17 | userName | String | - |  |
| 18 | startedAt | Date | Datetime |  |
| 19 | completedAt | Date | Datetime |  |
| 20 | durationSec | Int32 | - |  |
| 21 | inputType | String | - |  |
| 22 | enteredText | String | - |  |
| 23 | enteredNumber | Decimal128 | - |  |
| 24 | enteredFlag | Boolean | - |  |
| 25 | scannedCode | String | - |  |
| 26 | withinLimits | Boolean | - |  |
| 27 | deviceSource | String | - |  |
| 28 | overridden | Boolean | - |  |
| 29 | overrideById | String | - | u_mes_mast_user._id |
| 30 | overrideBy | String | - |  |
| 31 | overrideReason | String | - |  |
| 32 | photoControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 33 | photoControlledDocumentName | String | - |  |
| 34 | overrideReasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 35 | overrideReasonCodeName | String | - |  |
| 36 | arSessionRef | String | - |  |
| 37 | status | String | - |  |
| 38 | schemaVersion | Int32 | - |  |
| 39 | createdAt | Date | Datetime |  |
| 40 | createdById | String | - | u_mes_mast_user._id |
| 41 | createdBy | String | - |  |
| 42 | updatedAt | Date | Datetime |  |
| 43 | updatedById | String | - | u_mes_mast_user._id |
| 44 | updatedBy | String | - |  |

## u_mes_plan_wipUnit

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | itemRevision | String | - |  |
| 11 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 12 | productVariantName | String | - |  |
| 13 | serialNumberId | String | - | u_mes_trac_serialNumber._id |
| 14 | serialNumberName | String | - |  |
| 15 | bodyLotId | String | - | u_mes_plan_lot._id |
| 16 | bodyLotName | String | - |  |
| 17 | routingId | String | - | u_mes_prod_routing._id |
| 18 | routingName | String | - |  |
| 19 | currentStepNo | Int32 | - |  |
| 20 | currentOperationId | String | - | u_mes_prod_operation._id |
| 21 | currentOperationName | String | - |  |
| 22 | currentWorkCenterId | String | - | u_mes_mast_workCenter._id |
| 23 | currentWorkCenterName | String | - |  |
| 24 | qualityStatus | String | - |  |
| 25 | onHold | Boolean | - |  |
| 26 | qualityHoldId | String | - | u_mes_qual_qualityHold._id |
| 27 | qualityHoldName | String | - |  |
| 28 | reworkCount | Int32 | - |  |
| 29 | createdAtOperationId | String | - | u_mes_prod_operation._id |
| 30 | createdAtOperationName | String | - |  |
| 31 | startedAt | Date | Datetime |  |
| 32 | completedAt | Date | Datetime |  |
| 33 | lastOperationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 34 | lastOperationExecutionName | String | - |  |
| 35 | containerId | String | - | u_mes_plan_container._id |
| 36 | containerName | String | - |  |
| 37 | bodyCavityNo | Int32 | - |  |
| 38 | castDateCode | String | - |  |
| 39 | scrappedAt | Date | Datetime |  |
| 40 | shippedAt | Date | Datetime |  |
| 41 | status | String | - |  |
| 42 | schemaVersion | Int32 | - |  |
| 43 | createdAt | Date | Datetime |  |
| 44 | createdById | String | - | u_mes_mast_user._id |
| 45 | createdBy | String | - |  |
| 46 | updatedAt | Date | Datetime |  |
| 47 | updatedById | String | - | u_mes_mast_user._id |
| 48 | updatedBy | String | - |  |

## u_mes_plan_wipUnitCompletedStep

Kind: valueList | Data class: transaction | Parent: u_mes_plan_wipUnit | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 7 | wipUnitName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | completedStep | Int32 | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_plan_lot

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | itemId | String | - | u_mes_prod_item._id |
| 7 | itemName | String | - |  |
| 8 | lotType | String | - |  |
| 9 | supplierId | String | - | u_mes_mast_supplier._id |
| 10 | supplierName | String | - |  |
| 11 | supplierLotNo | String | - |  |
| 12 | heatNo | String | - |  |
| 13 | goodsReceiptId | String | - | u_mes_matl_goodsReceipt._id |
| 14 | goodsReceiptName | String | - |  |
| 15 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - |  |
| 17 | manufacturedAt | Date | Datetime |  |
| 18 | receivedAt | Date | Datetime |  |
| 19 | expiryAt | Date | Date |  |
| 20 | initialQuantity | Decimal128 | - |  |
| 21 | currentQuantity | Decimal128 | - |  |
| 22 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 23 | unitOfMeasureName | String | - |  |
| 24 | qualityStatus | String | - |  |
| 25 | onHold | Boolean | - |  |
| 26 | qualityHoldId | String | - | u_mes_qual_qualityHold._id |
| 27 | qualityHoldName | String | - |  |
| 28 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 29 | storageLocationName | String | - |  |
| 30 | attributesDieNo | String | - |  |
| 31 | attributesFurnaceChargeNo | String | - |  |
| 32 | attributesHardnessHbw | Decimal128 | - |  |
| 33 | attributesAnodisingLoadNo | String | - |  |
| 34 | attributesCoatingThicknessUm | Decimal128 | - |  |
| 35 | attributesCureDate | Date | Date |  |
| 36 | certificateControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 37 | certificateControlledDocumentName | String | - |  |
| 38 | currentOperationId | String | - | u_mes_prod_operation._id |
| 39 | currentOperationName | String | - |  |
| 40 | closedAt | Date | Datetime |  |
| 41 | retestDate | Date | Date |  |
| 42 | batchReleaseId | String | - | u_mes_bmr_batchRelease._id |
| 43 | batchReleaseName | String | - |  |
| 44 | status | String | - |  |
| 45 | schemaVersion | Int32 | - |  |
| 46 | createdAt | Date | Datetime |  |
| 47 | createdById | String | - | u_mes_mast_user._id |
| 48 | createdBy | String | - |  |
| 49 | updatedAt | Date | Datetime |  |
| 50 | updatedById | String | - | u_mes_mast_user._id |
| 51 | updatedBy | String | - |  |

## u_mes_plan_lotParentLot

Kind: relationship | Data class: transaction | Parent: u_mes_plan_lot | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | lotId | String | - | u_mes_plan_lot._id |
| 7 | lotName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | parentLotId | String | - | u_mes_plan_lot._id |
| 10 | parentLotName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_plan_lotAttributesCavityNo

Kind: valueList | Data class: transaction | Parent: u_mes_plan_lot | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | lotId | String | - | u_mes_plan_lot._id |
| 7 | lotName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | attributesCavityNo | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_plan_container

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | containerTypeId | String | - | u_mes_plan_containerType._id |
| 7 | containerTypeName | String | - |  |
| 8 | packagingSpecificationId | String | - | u_mes_matl_packagingSpecification._id |
| 9 | packagingSpecificationName | String | - |  |
| 10 | isReturnable | Boolean | - |  |
| 11 | ownerCustomerId | String | - | u_mes_mast_customer._id |
| 12 | ownerCustomerName | String | - |  |
| 13 | itemId | String | - | u_mes_prod_item._id |
| 14 | itemName | String | - |  |
| 15 | quantity | Int32 | - |  |
| 16 | capacity | Int32 | - |  |
| 17 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 18 | storageLocationName | String | - |  |
| 19 | parentContainerId | String | - | u_mes_plan_container._id |
| 20 | parentContainerName | String | - |  |
| 21 | tareWeightKg | Decimal128 | - |  |
| 22 | grossWeightKg | Decimal128 | - |  |
| 23 | onHold | Boolean | - |  |
| 24 | packedAt | Date | Datetime |  |
| 25 | packedById | String | - | u_mes_mast_user._id |
| 26 | packedBy | String | - |  |
| 27 | labelId | String | - | u_mes_matl_label._id |
| 28 | labelName | String | - |  |
| 29 | shipmentId | String | - | u_mes_matl_shipment._id |
| 30 | shipmentName | String | - |  |
| 31 | lastCleanedAt | Date | Datetime |  |
| 32 | cycleCount | Int32 | - |  |
| 33 | status | String | - |  |
| 34 | schemaVersion | Int32 | - |  |
| 35 | createdAt | Date | Datetime |  |
| 36 | createdById | String | - | u_mes_mast_user._id |
| 37 | createdBy | String | - |  |
| 38 | updatedAt | Date | Datetime |  |
| 39 | updatedById | String | - | u_mes_mast_user._id |
| 40 | updatedBy | String | - |  |

## u_mes_plan_containerLot

Kind: relationship | Data class: transaction | Parent: u_mes_plan_container | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | containerId | String | - | u_mes_plan_container._id |
| 7 | containerName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | lotId | String | - | u_mes_plan_lot._id |
| 10 | lotName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_plan_labourBooking

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | userId | String | - | u_mes_mast_user._id |
| 7 | userName | String | - |  |
| 8 | shiftId | String | - | u_mes_mast_shift._id |
| 9 | shiftName | String | - |  |
| 10 | productionDate | Date | Date |  |
| 11 | bookingType | String | - |  |
| 12 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 13 | productionOrderName | String | - |  |
| 14 | operationId | String | - | u_mes_prod_operation._id |
| 15 | operationName | String | - |  |
| 16 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 17 | workCenterName | String | - |  |
| 18 | indirectActivityId | String | - | u_mes_plan_indirectActivity._id |
| 19 | indirectActivityName | String | - |  |
| 20 | clockOnAt | Date | Datetime |  |
| 21 | clockOffAt | Date | Datetime |  |
| 22 | durationMinutes | Int32 | - |  |
| 23 | overtimeMinutes | Int32 | - |  |
| 24 | quantityGood | Int32 | - |  |
| 25 | approvedById | String | - | u_mes_mast_user._id |
| 26 | approvedBy | String | - |  |
| 27 | approvedAt | Date | Datetime |  |
| 28 | erpConfirmationNo | String | - |  |
| 29 | source | String | - |  |
| 30 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 31 | operationExecutionName | String | - |  |
| 32 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 33 | productVariantName | String | - |  |
| 34 | operatorSessionId | String | - | u_mes_plan_operatorSession._id |
| 35 | operatorSessionName | String | - |  |
| 36 | status | String | - |  |
| 37 | schemaVersion | Int32 | - |  |
| 38 | createdAt | Date | Datetime |  |
| 39 | createdById | String | - | u_mes_mast_user._id |
| 40 | createdBy | String | - |  |
| 41 | updatedAt | Date | Datetime |  |
| 42 | updatedById | String | - | u_mes_mast_user._id |
| 43 | updatedBy | String | - |  |

## u_mes_plan_changeover

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | lineId | String | - | u_mes_mast_line._id |
| 7 | lineName | String | - |  |
| 8 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - |  |
| 10 | equipmentId | String | - | u_mes_mast_equipment._id |
| 11 | equipmentName | String | - |  |
| 12 | fromProductionOrderId | String | - | u_mes_plan_productionOrder._id |
| 13 | fromProductionOrderName | String | - |  |
| 14 | toProductionOrderId | String | - | u_mes_plan_productionOrder._id |
| 15 | toProductionOrderName | String | - |  |
| 16 | fromItemId | String | - | u_mes_prod_item._id |
| 17 | fromItemName | String | - |  |
| 18 | toItemId | String | - | u_mes_prod_item._id |
| 19 | toItemName | String | - |  |
| 20 | changeoverType | String | - |  |
| 21 | plannedStartAt | Date | Datetime |  |
| 22 | startedAt | Date | Datetime |  |
| 23 | completedAt | Date | Datetime |  |
| 24 | plannedMinutes | Int32 | - |  |
| 25 | actualMinutes | Int32 | - |  |
| 26 | recipeId | String | - | u_mes_prod_recipe._id |
| 27 | recipeName | String | - |  |
| 28 | firstOffCheckSheetResultId | String | - | u_mes_qual_checkSheetResult._id |
| 29 | firstOffCheckSheetResultName | String | - |  |
| 30 | firstOffApprovedById | String | - | u_mes_mast_user._id |
| 31 | firstOffApprovedBy | String | - |  |
| 32 | firstOffApprovedAt | Date | Datetime |  |
| 33 | lossReason | String | - |  |
| 34 | status | String | - |  |
| 35 | schemaVersion | Int32 | - |  |
| 36 | createdAt | Date | Datetime |  |
| 37 | createdById | String | - | u_mes_mast_user._id |
| 38 | createdBy | String | - |  |
| 39 | updatedAt | Date | Datetime |  |
| 40 | updatedById | String | - | u_mes_mast_user._id |
| 41 | updatedBy | String | - |  |

## u_mes_plan_changeoverStep

Kind: child | Data class: transaction | Parent: u_mes_plan_changeover | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | changeoverId | String | - | u_mes_plan_changeover._id |
| 7 | changeoverName | String | - |  |
| 8 | stepNo | Int32 | - |  |
| 9 | description | String | - |  |
| 10 | internalExternal | String | - |  |
| 11 | completedAt | Date | Datetime |  |
| 12 | completedById | String | - | u_mes_mast_user._id |
| 13 | completedBy | String | - |  |
| 14 | schemaVersion | Int32 | - |  |
| 15 | createdAt | Date | Datetime |  |
| 16 | createdById | String | - | u_mes_mast_user._id |
| 17 | createdBy | String | - |  |
| 18 | updatedAt | Date | Datetime |  |
| 19 | updatedById | String | - | u_mes_mast_user._id |
| 20 | updatedBy | String | - |  |

## u_mes_plan_changeoverRemovedTool

Kind: relationship | Data class: transaction | Parent: u_mes_plan_changeover | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | changeoverId | String | - | u_mes_plan_changeover._id |
| 7 | changeoverName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | removedToolId | String | - | u_mes_maint_tool._id |
| 10 | removedToolName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_plan_changeoverInstalledTool

Kind: relationship | Data class: transaction | Parent: u_mes_plan_changeover | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | changeoverId | String | - | u_mes_plan_changeover._id |
| 7 | changeoverName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | installedToolId | String | - | u_mes_maint_tool._id |
| 10 | installedToolName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_plan_changeoverPerformedByUser

Kind: relationship | Data class: transaction | Parent: u_mes_plan_changeover | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | changeoverId | String | - | u_mes_plan_changeover._id |
| 7 | changeoverName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | performedByUserId | String | - | u_mes_mast_user._id |
| 10 | performedByUserName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_plan_shiftHandover

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | productionDate | Date | Date |  |
| 7 | shiftId | String | - | u_mes_mast_shift._id |
| 8 | shiftName | String | - |  |
| 9 | lineId | String | - | u_mes_mast_line._id |
| 10 | lineName | String | - |  |
| 11 | outgoingSupervisorUserId | String | - | u_mes_mast_user._id |
| 12 | outgoingSupervisorUserName | String | - |  |
| 13 | incomingSupervisorUserId | String | - | u_mes_mast_user._id |
| 14 | incomingSupervisorUserName | String | - |  |
| 15 | outputPlanned | Int32 | - |  |
| 16 | outputActual | Int32 | - |  |
| 17 | outputScrap | Int32 | - |  |
| 18 | outputRework | Int32 | - |  |
| 19 | oeePct | Decimal128 | - |  |
| 20 | safetyNotes | String | - |  |
| 21 | qualityNotes | String | - |  |
| 22 | maintenanceNotes | String | - |  |
| 23 | materialNotes | String | - |  |
| 24 | handedOverAt | Date | Datetime |  |
| 25 | acknowledgedAt | Date | Datetime |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |
| 28 | createdAt | Date | Datetime |  |
| 29 | createdById | String | - | u_mes_mast_user._id |
| 30 | createdBy | String | - |  |
| 31 | updatedAt | Date | Datetime |  |
| 32 | updatedById | String | - | u_mes_mast_user._id |
| 33 | updatedBy | String | - |  |

## u_mes_plan_shiftHandoverProductionOrder

Kind: relationship | Data class: transaction | Parent: u_mes_plan_shiftHandover | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | shiftHandoverId | String | - | u_mes_plan_shiftHandover._id |
| 7 | shiftHandoverName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 10 | productionOrderName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_plan_shiftHandoverDowntimeEvent

Kind: relationship | Data class: transaction | Parent: u_mes_plan_shiftHandover | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | shiftHandoverId | String | - | u_mes_plan_shiftHandover._id |
| 7 | shiftHandoverName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | downtimeEventId | String | - | u_mes_perf_downtimeEvent._id |
| 10 | downtimeEventName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_plan_shiftHandoverNonconformance

Kind: relationship | Data class: transaction | Parent: u_mes_plan_shiftHandover | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | shiftHandoverId | String | - | u_mes_plan_shiftHandover._id |
| 7 | shiftHandoverName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 10 | nonconformanceName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_plan_shiftHandoverOpenItem

Kind: child | Data class: transaction | Parent: u_mes_plan_shiftHandover | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | shiftHandoverId | String | - | u_mes_plan_shiftHandover._id |
| 7 | shiftHandoverName | String | - |  |
| 8 | itemNo | Int32 | - |  |
| 9 | description | String | - |  |
| 10 | ownerUserId | String | - | u_mes_mast_user._id |
| 11 | ownerUserName | String | - |  |
| 12 | dueAt | Date | Datetime |  |
| 13 | closed | Boolean | - |  |
| 14 | schemaVersion | Int32 | - |  |
| 15 | createdAt | Date | Datetime |  |
| 16 | createdById | String | - | u_mes_mast_user._id |
| 17 | createdBy | String | - |  |
| 18 | updatedAt | Date | Datetime |  |
| 19 | updatedById | String | - | u_mes_mast_user._id |
| 20 | updatedBy | String | - |  |

## u_mes_plan_andonEvent

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 7 | workCenterName | String | - |  |
| 8 | lineId | String | - | u_mes_mast_line._id |
| 9 | lineName | String | - |  |
| 10 | shiftId | String | - | u_mes_mast_shift._id |
| 11 | shiftName | String | - |  |
| 12 | andonTypeId | String | - | u_mes_plan_andonType._id |
| 13 | andonTypeName | String | - |  |
| 14 | reasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 15 | reasonCodeName | String | - |  |
| 16 | raisedById | String | - | u_mes_mast_user._id |
| 17 | raisedBy | String | - |  |
| 18 | raisedAt | Date | Datetime |  |
| 19 | acknowledgedById | String | - | u_mes_mast_user._id |
| 20 | acknowledgedBy | String | - |  |
| 21 | acknowledgedAt | Date | Datetime |  |
| 22 | resolvedById | String | - | u_mes_mast_user._id |
| 23 | resolvedBy | String | - |  |
| 24 | resolvedAt | Date | Datetime |  |
| 25 | responseSec | Int32 | - |  |
| 26 | resolutionSec | Int32 | - |  |
| 27 | lineStopped | Boolean | - |  |
| 28 | downtimeEventId | String | - | u_mes_perf_downtimeEvent._id |
| 29 | downtimeEventName | String | - |  |
| 30 | description | String | - |  |
| 31 | resolutionText | String | - |  |
| 32 | equipmentId | String | - | u_mes_mast_equipment._id |
| 33 | equipmentName | String | - |  |
| 34 | severityClass | String | - |  |
| 35 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 36 | maintenanceWorkOrderName | String | - |  |
| 37 | escalationRuleId | String | - | u_mes_syst_escalationRule._id |
| 38 | escalationRuleName | String | - |  |
| 39 | status | String | - |  |
| 40 | schemaVersion | Int32 | - |  |
| 41 | createdAt | Date | Datetime |  |
| 42 | createdById | String | - | u_mes_mast_user._id |
| 43 | createdBy | String | - |  |
| 44 | updatedAt | Date | Datetime |  |
| 45 | updatedById | String | - | u_mes_mast_user._id |
| 46 | updatedBy | String | - |  |

## u_mes_plan_andonEventEscalation

Kind: child | Data class: transaction | Parent: u_mes_plan_andonEvent | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | andonEventId | String | - | u_mes_plan_andonEvent._id |
| 7 | andonEventName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | level | Int32 | - |  |
| 10 | escalatedAt | Date | Datetime |  |
| 11 | toUserId | String | - | u_mes_mast_user._id |
| 12 | toUserName | String | - |  |
| 13 | channel | String | - |  |
| 14 | schemaVersion | Int32 | - |  |
| 15 | createdAt | Date | Datetime |  |
| 16 | createdById | String | - | u_mes_mast_user._id |
| 17 | createdBy | String | - |  |
| 18 | updatedAt | Date | Datetime |  |
| 19 | updatedById | String | - | u_mes_mast_user._id |
| 20 | updatedBy | String | - |  |

## u_mes_plan_indirectActivity

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | isPaid | Boolean | - |  |
| 9 | costCenterId | String | - | u_mes_mast_costCenter._id |
| 10 | costCenterName | String | - |  |
| 11 | sequenceNo | Int32 | - |  |
| 12 | status | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_plan_containerType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | lengthMm | Decimal128 | - |  |
| 9 | widthMm | Decimal128 | - |  |
| 10 | heightMm | Decimal128 | - |  |
| 11 | tareWeightKg | Decimal128 | - |  |
| 12 | isReturnable | Boolean | - |  |
| 13 | sequenceNo | Int32 | - |  |
| 14 | status | String | - |  |
| 15 | schemaVersion | Int32 | - |  |

## u_mes_plan_andonType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | colourCode | String | - |  |
| 9 | responsibleDepartmentId | String | - | u_mes_mast_department._id |
| 10 | responsibleDepartmentName | String | - |  |
| 11 | targetResponseSec | Int32 | - |  |
| 12 | sequenceNo | Int32 | - |  |
| 13 | targetRepairSec | Int32 | - |  |
| 14 | escalationRuleId | String | - | u_mes_syst_escalationRule._id |
| 15 | escalationRuleName | String | - |  |
| 16 | status | String | - |  |
| 17 | schemaVersion | Int32 | - |  |

## u_mes_plan_operatorSession

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | userId | String | - | u_mes_mast_user._id |
| 7 | userName | String | - |  |
| 8 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - |  |
| 10 | equipmentId | String | - | u_mes_mast_equipment._id |
| 11 | equipmentName | String | - |  |
| 12 | shiftId | String | - | u_mes_mast_shift._id |
| 13 | shiftName | String | - |  |
| 14 | productionDate | Date | Date |  |
| 15 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - |  |
| 17 | authenticationMethod | String | - |  |
| 18 | loginAt | Date | Datetime |  |
| 19 | logoutAt | Date | Datetime |  |
| 20 | logoutReason | String | - |  |
| 21 | skillVerified | Boolean | - |  |
| 22 | trainingVerified | Boolean | - |  |
| 23 | interlockEventId | String | - | u_mes_plan_interlockEvent._id |
| 24 | interlockEventName | String | - |  |
| 25 | clientWorkstation | String | - |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |
| 28 | createdAt | Date | Datetime |  |
| 29 | createdById | String | - | u_mes_mast_user._id |
| 30 | createdBy | String | - |  |
| 31 | updatedAt | Date | Datetime |  |
| 32 | updatedById | String | - | u_mes_mast_user._id |
| 33 | updatedBy | String | - |  |

## u_mes_plan_documentAcknowledgement

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | relatedCollectionName | String | - |  |
| 7 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 8 | relatedEntityName | String | - |  |
| 9 | documentVersion | String | - |  |
| 10 | userId | String | - | u_mes_mast_user._id |
| 11 | userName | String | - |  |
| 12 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 13 | workCenterName | String | - |  |
| 14 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 15 | productVariantName | String | - |  |
| 16 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 17 | productionOrderName | String | - |  |
| 18 | shiftId | String | - | u_mes_mast_shift._id |
| 19 | shiftName | String | - |  |
| 20 | operatorSessionId | String | - | u_mes_plan_operatorSession._id |
| 21 | operatorSessionName | String | - |  |
| 22 | acknowledgementType | String | - |  |
| 23 | method | String | - |  |
| 24 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 25 | electronicSignatureName | String | - |  |
| 26 | acknowledgedAt | Date | Datetime |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |
| 29 | createdAt | Date | Datetime |  |
| 30 | createdById | String | - | u_mes_mast_user._id |
| 31 | createdBy | String | - |  |
| 32 | updatedAt | Date | Datetime |  |
| 33 | updatedById | String | - | u_mes_mast_user._id |
| 34 | updatedBy | String | - |  |

## u_mes_plan_interlockEvent

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | interlockRuleId | String | - | u_mes_syst_interlockRule._id |
| 7 | interlockRuleName | String | - |  |
| 8 | ruleType | String | - |  |
| 9 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 10 | workCenterName | String | - |  |
| 11 | equipmentId | String | - | u_mes_mast_equipment._id |
| 12 | equipmentName | String | - |  |
| 13 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 14 | productionOrderName | String | - |  |
| 15 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 16 | wipUnitName | String | - |  |
| 17 | lotId | String | - | u_mes_plan_lot._id |
| 18 | lotName | String | - |  |
| 19 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 20 | operationExecutionName | String | - |  |
| 21 | relatedCollectionName | String | - |  |
| 22 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 23 | relatedEntityName | String | - |  |
| 24 | foundValueText | String | - |  |
| 25 | expectedValueText | String | - |  |
| 26 | messageText | String | - |  |
| 27 | shiftId | String | - | u_mes_mast_shift._id |
| 28 | shiftName | String | - |  |
| 29 | productionDate | Date | Date |  |
| 30 | operatorUserId | String | - | u_mes_mast_user._id |
| 31 | operatorUserName | String | - |  |
| 32 | raisedAt | Date | Datetime |  |
| 33 | overrideReasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 34 | overrideReasonCodeName | String | - |  |
| 35 | overrideComment | String | - |  |
| 36 | overrideById | String | - | u_mes_mast_user._id |
| 37 | overrideBy | String | - |  |
| 38 | overrideAt | Date | Datetime |  |
| 39 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 40 | electronicSignatureName | String | - |  |
| 41 | clearedAt | Date | Datetime |  |
| 42 | notificationId | String | - | u_mes_syst_notification._id |
| 43 | notificationName | String | - |  |
| 44 | status | String | - |  |
| 45 | schemaVersion | Int32 | - |  |
| 46 | createdAt | Date | Datetime |  |
| 47 | createdById | String | - | u_mes_mast_user._id |
| 48 | createdBy | String | - |  |
| 49 | updatedAt | Date | Datetime |  |
| 50 | updatedById | String | - | u_mes_mast_user._id |
| 51 | updatedBy | String | - |  |

## u_mes_plan_recipeDownload

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | recipeId | String | - | u_mes_prod_recipe._id |
| 7 | recipeName | String | - |  |
| 8 | recipeVersion | String | - |  |
| 9 | equipmentId | String | - | u_mes_mast_equipment._id |
| 10 | equipmentName | String | - |  |
| 11 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 12 | workCenterName | String | - |  |
| 13 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 14 | productionOrderName | String | - |  |
| 15 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 16 | productVariantName | String | - |  |
| 17 | trigger | String | - |  |
| 18 | checksumExpected | String | - |  |
| 19 | checksumReported | String | - |  |
| 20 | verificationResult | String | - |  |
| 21 | downloadedAt | Date | Datetime |  |
| 22 | verifiedAt | Date | Datetime |  |
| 23 | requestedById | String | - | u_mes_mast_user._id |
| 24 | requestedBy | String | - |  |
| 25 | interlockEventId | String | - | u_mes_plan_interlockEvent._id |
| 26 | interlockEventName | String | - |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |
| 29 | createdAt | Date | Datetime |  |
| 30 | createdById | String | - | u_mes_mast_user._id |
| 31 | createdBy | String | - |  |
| 32 | updatedAt | Date | Datetime |  |
| 33 | updatedById | String | - | u_mes_mast_user._id |
| 34 | updatedBy | String | - |  |

## u_mes_plan_setupVerification

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 7 | workCenterName | String | - |  |
| 8 | equipmentId | String | - | u_mes_mast_equipment._id |
| 9 | equipmentName | String | - |  |
| 10 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 11 | productionOrderName | String | - |  |
| 12 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 13 | productVariantName | String | - |  |
| 14 | changeoverId | String | - | u_mes_plan_changeover._id |
| 15 | changeoverName | String | - |  |
| 16 | billOfProcessId | String | - | u_mes_prod_billOfProcess._id |
| 17 | billOfProcessName | String | - |  |
| 18 | trigger | String | - |  |
| 19 | itemCount | Int32 | - |  |
| 20 | failedCount | Int32 | - |  |
| 21 | verifiedById | String | - | u_mes_mast_user._id |
| 22 | verifiedBy | String | - |  |
| 23 | verifiedAt | Date | Datetime |  |
| 24 | interlockEventId | String | - | u_mes_plan_interlockEvent._id |
| 25 | interlockEventName | String | - |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |
| 28 | createdAt | Date | Datetime |  |
| 29 | createdById | String | - | u_mes_mast_user._id |
| 30 | createdBy | String | - |  |
| 31 | updatedAt | Date | Datetime |  |
| 32 | updatedById | String | - | u_mes_mast_user._id |
| 33 | updatedBy | String | - |  |

## u_mes_plan_setupVerificationItem

Kind: child | Data class: transaction | Parent: u_mes_plan_setupVerification | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | setupVerificationId | String | - | u_mes_plan_setupVerification._id |
| 7 | setupVerificationName | String | - |  |
| 8 | itemNo | Int32 | - |  |
| 9 | checkType | String | - |  |
| 10 | relatedCollectionName | String | - |  |
| 11 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 12 | relatedEntityName | String | - |  |
| 13 | scannedCode | String | - |  |
| 14 | expectedValue | Decimal128 | - |  |
| 15 | actualValue | Decimal128 | - |  |
| 16 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 17 | unitOfMeasureName | String | - |  |
| 18 | passed | Boolean | - |  |
| 19 | checkedAt | Date | Datetime |  |
| 20 | schemaVersion | Int32 | - |  |
| 21 | createdAt | Date | Datetime |  |
| 22 | createdById | String | - | u_mes_mast_user._id |
| 23 | createdBy | String | - |  |
| 24 | updatedAt | Date | Datetime |  |
| 25 | updatedById | String | - | u_mes_mast_user._id |
| 26 | updatedBy | String | - |  |

## u_mes_plan_lineClearance

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | lineId | String | - | u_mes_mast_line._id |
| 7 | lineName | String | - |  |
| 8 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - |  |
| 10 | clearanceType | String | - |  |
| 11 | previousProductionOrderId | String | - | u_mes_plan_productionOrder._id |
| 12 | previousProductionOrderName | String | - |  |
| 13 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 14 | productionOrderName | String | - |  |
| 15 | changeoverId | String | - | u_mes_plan_changeover._id |
| 16 | changeoverName | String | - |  |
| 17 | checkSheetResultId | String | - | u_mes_qual_checkSheetResult._id |
| 18 | checkSheetResultName | String | - |  |
| 19 | materialsRemoved | Boolean | - |  |
| 20 | labelsRemoved | Boolean | - |  |
| 21 | documentsRemoved | Boolean | - |  |
| 22 | equipmentClean | Boolean | - |  |
| 23 | performedById | String | - | u_mes_mast_user._id |
| 24 | performedBy | String | - |  |
| 25 | startedAt | Date | Datetime |  |
| 26 | completedAt | Date | Datetime |  |
| 27 | verifiedById | String | - | u_mes_mast_user._id |
| 28 | verifiedBy | String | - |  |
| 29 | verifiedAt | Date | Datetime |  |
| 30 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 31 | electronicSignatureName | String | - |  |
| 32 | failureText | String | - |  |
| 33 | status | String | - |  |
| 34 | schemaVersion | Int32 | - |  |
| 35 | createdAt | Date | Datetime |  |
| 36 | createdById | String | - | u_mes_mast_user._id |
| 37 | createdBy | String | - |  |
| 38 | updatedAt | Date | Datetime |  |
| 39 | updatedById | String | - | u_mes_mast_user._id |
| 40 | updatedBy | String | - |  |
