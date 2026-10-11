# Field list - Planning and Execution (plan)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/03_planning_execution/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_plan_customerSchedule

Kind: entity | Data class: transaction | Parent: - | _id pattern: CSR-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | customerId | String | u_mes_mast_customer._id |
| 6 | customerName | String |  |
| 7 | shipToCode | String |  |
| 8 | scheduleType | String |  |
| 9 | customerOrderNo | String |  |
| 10 | receivedAt | Date |  |
| 11 | horizonFrom | Date |  |
| 12 | horizonTo | Date |  |
| 13 | supersedesCustomerScheduleId | String | u_mes_plan_customerSchedule._id |
| 14 | supersedesCustomerScheduleName | String |  |
| 15 | erpSalesOrderNo | String |  |
| 16 | status | String |  |
| 17 | schemaVersion | Int32 |  |
| 18 | createdAt | Date |  |
| 19 | createdById | String | u_mes_mast_user._id |
| 20 | createdBy | String |  |
| 21 | updatedAt | Date |  |
| 22 | updatedById | String | u_mes_mast_user._id |
| 23 | updatedBy | String |  |

## u_mes_plan_customerScheduleLine

Kind: child | Data class: transaction | Parent: u_mes_plan_customerSchedule | _id pattern: <customerScheduleId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | customerScheduleId | String | u_mes_plan_customerSchedule._id |
| 6 | customerScheduleName | String |  |
| 7 | lineNo | Int32 |  |
| 8 | itemId | String | u_mes_prod_item._id |
| 9 | itemName | String |  |
| 10 | customerPartNo | String |  |
| 11 | dueDate | Date |  |
| 12 | quantity | Int32 |  |
| 13 | cumulativeRequired | Int32 |  |
| 14 | cumulativeShipped | Int32 |  |
| 15 | firmness | String |  |
| 16 | shippedQuantity | Int32 |  |
| 17 | schemaVersion | Int32 |  |
| 18 | createdAt | Date |  |
| 19 | createdById | String | u_mes_mast_user._id |
| 20 | createdBy | String |  |
| 21 | updatedAt | Date |  |
| 22 | updatedById | String | u_mes_mast_user._id |
| 23 | updatedBy | String |  |

## u_mes_plan_productionOrder

Kind: entity | Data class: transaction | Parent: - | _id pattern: PO-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | erpOrderNo | String |  |
| 6 | itemId | String | u_mes_prod_item._id |
| 7 | itemName | String |  |
| 8 | itemRevision | String |  |
| 9 | productVariantId | String | u_mes_prod_productVariant._id |
| 10 | productVariantName | String |  |
| 11 | billOfMaterialId | String | u_mes_prod_billOfMaterial._id |
| 12 | billOfMaterialName | String |  |
| 13 | routingId | String | u_mes_prod_routing._id |
| 14 | routingName | String |  |
| 15 | lineId | String | u_mes_mast_line._id |
| 16 | lineName | String |  |
| 17 | customerScheduleId | String | u_mes_plan_customerSchedule._id |
| 18 | customerScheduleName | String |  |
| 19 | orderType | String |  |
| 20 | priority | String |  |
| 21 | plannedQuantity | Int32 |  |
| 22 | releasedQuantity | Int32 |  |
| 23 | startedQuantity | Int32 |  |
| 24 | goodQuantity | Int32 |  |
| 25 | scrapQuantity | Int32 |  |
| 26 | reworkQuantity | Int32 |  |
| 27 | unitOfMeasureId | String | u_mes_mast_unitOfMeasure._id |
| 28 | unitOfMeasureName | String |  |
| 29 | plannedStartAt | Date |  |
| 30 | plannedEndAt | Date |  |
| 31 | actualStartAt | Date |  |
| 32 | actualEndAt | Date |  |
| 33 | dueDate | Date |  |
| 34 | erpMessageId | String | u_mes_syst_erpMessage._id |
| 35 | erpMessageName | String |  |
| 36 | closedAt | Date |  |
| 37 | closedById | String | u_mes_mast_user._id |
| 38 | closedBy | String |  |
| 39 | remarks | String |  |
| 40 | status | String |  |
| 41 | schemaVersion | Int32 |  |
| 42 | createdAt | Date |  |
| 43 | createdById | String | u_mes_mast_user._id |
| 44 | createdBy | String |  |
| 45 | updatedAt | Date |  |
| 46 | updatedById | String | u_mes_mast_user._id |
| 47 | updatedBy | String |  |

## u_mes_plan_productionOrderRelease

Kind: child | Data class: transaction | Parent: u_mes_plan_productionOrder | _id pattern: <productionOrderId>-R<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | productionOrderId | String | u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String |  |
| 7 | releaseNo | Int32 |  |
| 8 | quantity | Int32 |  |
| 9 | releasedAt | Date |  |
| 10 | releasedById | String | u_mes_mast_user._id |
| 11 | releasedBy | String |  |
| 12 | schemaVersion | Int32 |  |
| 13 | createdAt | Date |  |
| 14 | createdById | String | u_mes_mast_user._id |
| 15 | createdBy | String |  |
| 16 | updatedAt | Date |  |
| 17 | updatedById | String | u_mes_mast_user._id |
| 18 | updatedBy | String |  |

## u_mes_plan_productionOrderLot

Kind: relationship | Data class: transaction | Parent: u_mes_plan_productionOrder | _id pattern: <productionOrderId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | productionOrderId | String | u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | lotId | String | u_mes_plan_lot._id |
| 9 | lotName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mast_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mast_user._id |
| 16 | updatedBy | String |  |

## u_mes_plan_productionSchedule

Kind: entity | Data class: transaction | Parent: - | _id pattern: SCH-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | productionDate | Date |  |
| 6 | lineId | String | u_mes_mast_line._id |
| 7 | lineName | String |  |
| 8 | shiftId | String | u_mes_mast_shift._id |
| 9 | shiftName | String |  |
| 10 | workCalendarId | String | u_mes_mast_workCalendar._id |
| 11 | workCalendarName | String |  |
| 12 | scheduleVersion | Int32 |  |
| 13 | plannedOutput | Int32 |  |
| 14 | actualOutput | Int32 |  |
| 15 | attainmentPct | Decimal128 |  |
| 16 | frozen | Boolean |  |
| 17 | publishedAt | Date |  |
| 18 | publishedById | String | u_mes_mast_user._id |
| 19 | publishedBy | String |  |
| 20 | status | String |  |
| 21 | schemaVersion | Int32 |  |
| 22 | createdAt | Date |  |
| 23 | createdById | String | u_mes_mast_user._id |
| 24 | createdBy | String |  |
| 25 | updatedAt | Date |  |
| 26 | updatedById | String | u_mes_mast_user._id |
| 27 | updatedBy | String |  |

## u_mes_plan_productionScheduleSlot

Kind: child | Data class: transaction | Parent: u_mes_plan_productionSchedule | _id pattern: <productionScheduleId>-S<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | productionScheduleId | String | u_mes_plan_productionSchedule._id |
| 6 | productionScheduleName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | productionOrderId | String | u_mes_plan_productionOrder._id |
| 9 | productionOrderName | String |  |
| 10 | itemId | String | u_mes_prod_item._id |
| 11 | itemName | String |  |
| 12 | plannedQuantity | Int32 |  |
| 13 | plannedStartAt | Date |  |
| 14 | plannedEndAt | Date |  |
| 15 | changeoverMinutes | Int32 |  |
| 16 | actualQuantity | Int32 |  |
| 17 | schemaVersion | Int32 |  |
| 18 | createdAt | Date |  |
| 19 | createdById | String | u_mes_mast_user._id |
| 20 | createdBy | String |  |
| 21 | updatedAt | Date |  |
| 22 | updatedById | String | u_mes_mast_user._id |
| 23 | updatedBy | String |  |

## u_mes_plan_dispatchList

Kind: entity | Data class: transaction | Parent: - | _id pattern: DSP-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | workCenterId | String | u_mes_mast_workCenter._id |
| 6 | workCenterName | String |  |
| 7 | shiftId | String | u_mes_mast_shift._id |
| 8 | shiftName | String |  |
| 9 | productionDate | Date |  |
| 10 | generatedAt | Date |  |
| 11 | rule | String |  |
| 12 | acknowledgedById | String | u_mes_mast_user._id |
| 13 | acknowledgedBy | String |  |
| 14 | acknowledgedAt | Date |  |
| 15 | status | String |  |
| 16 | schemaVersion | Int32 |  |
| 17 | createdAt | Date |  |
| 18 | createdById | String | u_mes_mast_user._id |
| 19 | createdBy | String |  |
| 20 | updatedAt | Date |  |
| 21 | updatedById | String | u_mes_mast_user._id |
| 22 | updatedBy | String |  |

## u_mes_plan_dispatchListEntry

Kind: child | Data class: transaction | Parent: u_mes_plan_dispatchList | _id pattern: <dispatchListId>-E<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | dispatchListId | String | u_mes_plan_dispatchList._id |
| 6 | dispatchListName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | rank | Int32 |  |
| 9 | productionOrderId | String | u_mes_plan_productionOrder._id |
| 10 | productionOrderName | String |  |
| 11 | lotId | String | u_mes_plan_lot._id |
| 12 | lotName | String |  |
| 13 | itemId | String | u_mes_prod_item._id |
| 14 | itemName | String |  |
| 15 | quantity | Int32 |  |
| 16 | dueAt | Date |  |
| 17 | queueSince | Date |  |
| 18 | priority | String |  |
| 19 | materialAvailable | Boolean |  |
| 20 | toolAvailable | Boolean |  |
| 21 | status | String |  |
| 22 | schemaVersion | Int32 |  |
| 23 | createdAt | Date |  |
| 24 | createdById | String | u_mes_mast_user._id |
| 25 | createdBy | String |  |
| 26 | updatedAt | Date |  |
| 27 | updatedById | String | u_mes_mast_user._id |
| 28 | updatedBy | String |  |

## u_mes_plan_operationExecution

Kind: entity | Data class: transaction | Parent: - | _id pattern: OPX-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | productionOrderId | String | u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String |  |
| 7 | wipUnitId | String | u_mes_plan_wipUnit._id |
| 8 | wipUnitName | String |  |
| 9 | lotId | String | u_mes_plan_lot._id |
| 10 | lotName | String |  |
| 11 | itemId | String | u_mes_prod_item._id |
| 12 | itemName | String |  |
| 13 | routingId | String | u_mes_prod_routing._id |
| 14 | routingName | String |  |
| 15 | stepNo | Int32 |  |
| 16 | operationId | String | u_mes_prod_operation._id |
| 17 | operationName | String |  |
| 18 | workCenterId | String | u_mes_mast_workCenter._id |
| 19 | workCenterName | String |  |
| 20 | equipmentId | String | u_mes_mast_equipment._id |
| 21 | equipmentName | String |  |
| 22 | recipeId | String | u_mes_prod_recipe._id |
| 23 | recipeName | String |  |
| 24 | shiftId | String | u_mes_mast_shift._id |
| 25 | shiftName | String |  |
| 26 | operatorUserId | String | u_mes_mast_user._id |
| 27 | operatorUserName | String |  |
| 28 | executionType | String |  |
| 29 | attemptNo | Int32 |  |
| 30 | startedAt | Date |  |
| 31 | completedAt | Date |  |
| 32 | cycleTimeSec | Decimal128 |  |
| 33 | standardCycleTimeSec | Decimal128 |  |
| 34 | quantityIn | Int32 |  |
| 35 | quantityGood | Int32 |  |
| 36 | quantityReject | Int32 |  |
| 37 | quantityRework | Int32 |  |
| 38 | result | String |  |
| 39 | checksSkillVerified | Boolean |  |
| 40 | checksRecipeVerified | Boolean |  |
| 41 | checksToolLifeOk | Boolean |  |
| 42 | checksGaugeCalibrationOk | Boolean |  |
| 43 | checksPreviousStepComplete | Boolean |  |
| 44 | nextStepNo | Int32 |  |
| 45 | remarks | String |  |
| 46 | status | String |  |
| 47 | schemaVersion | Int32 |  |
| 48 | createdAt | Date |  |
| 49 | createdById | String | u_mes_mast_user._id |
| 50 | createdBy | String |  |
| 51 | updatedAt | Date |  |
| 52 | updatedById | String | u_mes_mast_user._id |
| 53 | updatedBy | String |  |

## u_mes_plan_operationExecutionDefectCode

Kind: relationship | Data class: transaction | Parent: u_mes_plan_operationExecution | _id pattern: <operationExecutionId>-DC<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | operationExecutionId | String | u_mes_plan_operationExecution._id |
| 6 | operationExecutionName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | defectCodeId | String | u_mes_qual_defectCode._id |
| 9 | defectCodeName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mast_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mast_user._id |
| 16 | updatedBy | String |  |

## u_mes_plan_operationExecutionTool

Kind: relationship | Data class: transaction | Parent: u_mes_plan_operationExecution | _id pattern: <operationExecutionId>-T<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | operationExecutionId | String | u_mes_plan_operationExecution._id |
| 6 | operationExecutionName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | toolId | String | u_mes_maint_tool._id |
| 9 | toolName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mast_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mast_user._id |
| 16 | updatedBy | String |  |

## u_mes_plan_stepCompletion

Kind: entity | Data class: transaction | Parent: - | _id pattern: STC-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | operationExecutionId | String | u_mes_plan_operationExecution._id |
| 6 | operationExecutionName | String |  |
| 7 | workInstructionId | String | u_mes_prod_workInstruction._id |
| 8 | workInstructionName | String |  |
| 9 | workInstructionVersion | Int32 |  |
| 10 | stepNo | Int32 |  |
| 11 | wipUnitId | String | u_mes_plan_wipUnit._id |
| 12 | wipUnitName | String |  |
| 13 | workCenterId | String | u_mes_mast_workCenter._id |
| 14 | workCenterName | String |  |
| 15 | userId | String | u_mes_mast_user._id |
| 16 | userName | String |  |
| 17 | startedAt | Date |  |
| 18 | completedAt | Date |  |
| 19 | durationSec | Int32 |  |
| 20 | inputType | String |  |
| 21 | enteredText | String |  |
| 22 | enteredNumber | Decimal128 |  |
| 23 | enteredFlag | Boolean |  |
| 24 | scannedCode | String |  |
| 25 | withinLimits | Boolean |  |
| 26 | deviceSource | String |  |
| 27 | overridden | Boolean |  |
| 28 | overrideById | String | u_mes_mast_user._id |
| 29 | overrideBy | String |  |
| 30 | overrideReason | String |  |
| 31 | photoControlledDocumentId | String | u_mes_syst_controlledDocument._id |
| 32 | photoControlledDocumentName | String |  |
| 33 | status | String |  |
| 34 | schemaVersion | Int32 |  |
| 35 | createdAt | Date |  |
| 36 | createdById | String | u_mes_mast_user._id |
| 37 | createdBy | String |  |
| 38 | updatedAt | Date |  |
| 39 | updatedById | String | u_mes_mast_user._id |
| 40 | updatedBy | String |  |

## u_mes_plan_wipUnit

Kind: entity | Data class: transaction | Parent: - | _id pattern: WU-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | productionOrderId | String | u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String |  |
| 7 | itemId | String | u_mes_prod_item._id |
| 8 | itemName | String |  |
| 9 | itemRevision | String |  |
| 10 | productVariantId | String | u_mes_prod_productVariant._id |
| 11 | productVariantName | String |  |
| 12 | serialNumberId | String | u_mes_trac_serialNumber._id |
| 13 | serialNumberName | String |  |
| 14 | bodyLotId | String | u_mes_plan_lot._id |
| 15 | bodyLotName | String |  |
| 16 | routingId | String | u_mes_prod_routing._id |
| 17 | routingName | String |  |
| 18 | currentStepNo | Int32 |  |
| 19 | currentOperationId | String | u_mes_prod_operation._id |
| 20 | currentOperationName | String |  |
| 21 | currentWorkCenterId | String | u_mes_mast_workCenter._id |
| 22 | currentWorkCenterName | String |  |
| 23 | qualityStatus | String |  |
| 24 | onHold | Boolean |  |
| 25 | qualityHoldId | String | u_mes_qual_qualityHold._id |
| 26 | qualityHoldName | String |  |
| 27 | reworkCount | Int32 |  |
| 28 | createdAtOperationId | String | u_mes_prod_operation._id |
| 29 | createdAtOperationName | String |  |
| 30 | startedAt | Date |  |
| 31 | completedAt | Date |  |
| 32 | lastOperationExecutionId | String | u_mes_plan_operationExecution._id |
| 33 | lastOperationExecutionName | String |  |
| 34 | containerId | String | u_mes_plan_container._id |
| 35 | containerName | String |  |
| 36 | bodyCavityNo | Int32 |  |
| 37 | castDateCode | String |  |
| 38 | scrappedAt | Date |  |
| 39 | shippedAt | Date |  |
| 40 | status | String |  |
| 41 | schemaVersion | Int32 |  |
| 42 | createdAt | Date |  |
| 43 | createdById | String | u_mes_mast_user._id |
| 44 | createdBy | String |  |
| 45 | updatedAt | Date |  |
| 46 | updatedById | String | u_mes_mast_user._id |
| 47 | updatedBy | String |  |

## u_mes_plan_wipUnitCompletedStep

Kind: valueList | Data class: transaction | Parent: u_mes_plan_wipUnit | _id pattern: <wipUnitId>-CS<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | wipUnitId | String | u_mes_plan_wipUnit._id |
| 6 | wipUnitName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | completedStep | Int32 |  |
| 9 | schemaVersion | Int32 |  |
| 10 | createdAt | Date |  |
| 11 | createdById | String | u_mes_mast_user._id |
| 12 | createdBy | String |  |
| 13 | updatedAt | Date |  |
| 14 | updatedById | String | u_mes_mast_user._id |
| 15 | updatedBy | String |  |

## u_mes_plan_lot

Kind: entity | Data class: transaction | Parent: - | _id pattern: LOT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | itemId | String | u_mes_prod_item._id |
| 6 | itemName | String |  |
| 7 | lotType | String |  |
| 8 | supplierId | String | u_mes_mast_supplier._id |
| 9 | supplierName | String |  |
| 10 | supplierLotNo | String |  |
| 11 | heatNo | String |  |
| 12 | goodsReceiptId | String | u_mes_matl_goodsReceipt._id |
| 13 | goodsReceiptName | String |  |
| 14 | productionOrderId | String | u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String |  |
| 16 | manufacturedAt | Date |  |
| 17 | receivedAt | Date |  |
| 18 | expiryAt | Date |  |
| 19 | initialQuantity | Decimal128 |  |
| 20 | currentQuantity | Decimal128 |  |
| 21 | unitOfMeasureId | String | u_mes_mast_unitOfMeasure._id |
| 22 | unitOfMeasureName | String |  |
| 23 | qualityStatus | String |  |
| 24 | onHold | Boolean |  |
| 25 | qualityHoldId | String | u_mes_qual_qualityHold._id |
| 26 | qualityHoldName | String |  |
| 27 | storageLocationId | String | u_mes_matl_storageLocation._id |
| 28 | storageLocationName | String |  |
| 29 | attributesDieNo | String |  |
| 30 | attributesFurnaceChargeNo | String |  |
| 31 | attributesHardnessHbw | Decimal128 |  |
| 32 | attributesAnodisingLoadNo | String |  |
| 33 | attributesCoatingThicknessUm | Decimal128 |  |
| 34 | attributesCureDate | Date |  |
| 35 | certificateControlledDocumentId | String | u_mes_syst_controlledDocument._id |
| 36 | certificateControlledDocumentName | String |  |
| 37 | currentOperationId | String | u_mes_prod_operation._id |
| 38 | currentOperationName | String |  |
| 39 | closedAt | Date |  |
| 40 | status | String |  |
| 41 | schemaVersion | Int32 |  |
| 42 | createdAt | Date |  |
| 43 | createdById | String | u_mes_mast_user._id |
| 44 | createdBy | String |  |
| 45 | updatedAt | Date |  |
| 46 | updatedById | String | u_mes_mast_user._id |
| 47 | updatedBy | String |  |

## u_mes_plan_lotParentLot

Kind: relationship | Data class: transaction | Parent: u_mes_plan_lot | _id pattern: <lotId>-PL<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | lotId | String | u_mes_plan_lot._id |
| 6 | lotName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | parentLotId | String | u_mes_plan_lot._id |
| 9 | parentLotName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mast_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mast_user._id |
| 16 | updatedBy | String |  |

## u_mes_plan_lotAttributesCavityNo

Kind: valueList | Data class: transaction | Parent: u_mes_plan_lot | _id pattern: <lotId>-ACN<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | lotId | String | u_mes_plan_lot._id |
| 6 | lotName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | attributesCavityNo | String |  |
| 9 | schemaVersion | Int32 |  |
| 10 | createdAt | Date |  |
| 11 | createdById | String | u_mes_mast_user._id |
| 12 | createdBy | String |  |
| 13 | updatedAt | Date |  |
| 14 | updatedById | String | u_mes_mast_user._id |
| 15 | updatedBy | String |  |

## u_mes_plan_container

Kind: entity | Data class: transaction | Parent: - | _id pattern: CNT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | containerTypeId | String | u_mes_plan_containerType._id |
| 6 | containerTypeName | String |  |
| 7 | packagingSpecificationId | String | u_mes_matl_packagingSpecification._id |
| 8 | packagingSpecificationName | String |  |
| 9 | isReturnable | Boolean |  |
| 10 | ownerCustomerId | String | u_mes_mast_customer._id |
| 11 | ownerCustomerName | String |  |
| 12 | itemId | String | u_mes_prod_item._id |
| 13 | itemName | String |  |
| 14 | quantity | Int32 |  |
| 15 | capacity | Int32 |  |
| 16 | storageLocationId | String | u_mes_matl_storageLocation._id |
| 17 | storageLocationName | String |  |
| 18 | parentContainerId | String | u_mes_plan_container._id |
| 19 | parentContainerName | String |  |
| 20 | tareWeightKg | Decimal128 |  |
| 21 | grossWeightKg | Decimal128 |  |
| 22 | onHold | Boolean |  |
| 23 | packedAt | Date |  |
| 24 | packedById | String | u_mes_mast_user._id |
| 25 | packedBy | String |  |
| 26 | labelId | String | u_mes_matl_label._id |
| 27 | labelName | String |  |
| 28 | shipmentId | String | u_mes_matl_shipment._id |
| 29 | shipmentName | String |  |
| 30 | lastCleanedAt | Date |  |
| 31 | cycleCount | Int32 |  |
| 32 | status | String |  |
| 33 | schemaVersion | Int32 |  |
| 34 | createdAt | Date |  |
| 35 | createdById | String | u_mes_mast_user._id |
| 36 | createdBy | String |  |
| 37 | updatedAt | Date |  |
| 38 | updatedById | String | u_mes_mast_user._id |
| 39 | updatedBy | String |  |

## u_mes_plan_containerLot

Kind: relationship | Data class: transaction | Parent: u_mes_plan_container | _id pattern: <containerId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | containerId | String | u_mes_plan_container._id |
| 6 | containerName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | lotId | String | u_mes_plan_lot._id |
| 9 | lotName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mast_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mast_user._id |
| 16 | updatedBy | String |  |

## u_mes_plan_labourBooking

Kind: entity | Data class: transaction | Parent: - | _id pattern: LAB-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | userId | String | u_mes_mast_user._id |
| 6 | userName | String |  |
| 7 | shiftId | String | u_mes_mast_shift._id |
| 8 | shiftName | String |  |
| 9 | productionDate | Date |  |
| 10 | bookingType | String |  |
| 11 | productionOrderId | String | u_mes_plan_productionOrder._id |
| 12 | productionOrderName | String |  |
| 13 | operationId | String | u_mes_prod_operation._id |
| 14 | operationName | String |  |
| 15 | workCenterId | String | u_mes_mast_workCenter._id |
| 16 | workCenterName | String |  |
| 17 | indirectActivityId | String | u_mes_plan_indirectActivity._id |
| 18 | indirectActivityName | String |  |
| 19 | clockOnAt | Date |  |
| 20 | clockOffAt | Date |  |
| 21 | durationMinutes | Int32 |  |
| 22 | overtimeMinutes | Int32 |  |
| 23 | quantityGood | Int32 |  |
| 24 | approvedById | String | u_mes_mast_user._id |
| 25 | approvedBy | String |  |
| 26 | approvedAt | Date |  |
| 27 | erpConfirmationNo | String |  |
| 28 | source | String |  |
| 29 | status | String |  |
| 30 | schemaVersion | Int32 |  |
| 31 | createdAt | Date |  |
| 32 | createdById | String | u_mes_mast_user._id |
| 33 | createdBy | String |  |
| 34 | updatedAt | Date |  |
| 35 | updatedById | String | u_mes_mast_user._id |
| 36 | updatedBy | String |  |

## u_mes_plan_changeover

Kind: entity | Data class: transaction | Parent: - | _id pattern: CHG-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | lineId | String | u_mes_mast_line._id |
| 6 | lineName | String |  |
| 7 | workCenterId | String | u_mes_mast_workCenter._id |
| 8 | workCenterName | String |  |
| 9 | equipmentId | String | u_mes_mast_equipment._id |
| 10 | equipmentName | String |  |
| 11 | fromProductionOrderId | String | u_mes_plan_productionOrder._id |
| 12 | fromProductionOrderName | String |  |
| 13 | toProductionOrderId | String | u_mes_plan_productionOrder._id |
| 14 | toProductionOrderName | String |  |
| 15 | fromItemId | String | u_mes_prod_item._id |
| 16 | fromItemName | String |  |
| 17 | toItemId | String | u_mes_prod_item._id |
| 18 | toItemName | String |  |
| 19 | changeoverType | String |  |
| 20 | plannedStartAt | Date |  |
| 21 | startedAt | Date |  |
| 22 | completedAt | Date |  |
| 23 | plannedMinutes | Int32 |  |
| 24 | actualMinutes | Int32 |  |
| 25 | recipeId | String | u_mes_prod_recipe._id |
| 26 | recipeName | String |  |
| 27 | firstOffCheckSheetResultId | String | u_mes_qual_checkSheetResult._id |
| 28 | firstOffCheckSheetResultName | String |  |
| 29 | firstOffApprovedById | String | u_mes_mast_user._id |
| 30 | firstOffApprovedBy | String |  |
| 31 | firstOffApprovedAt | Date |  |
| 32 | lossReason | String |  |
| 33 | status | String |  |
| 34 | schemaVersion | Int32 |  |
| 35 | createdAt | Date |  |
| 36 | createdById | String | u_mes_mast_user._id |
| 37 | createdBy | String |  |
| 38 | updatedAt | Date |  |
| 39 | updatedById | String | u_mes_mast_user._id |
| 40 | updatedBy | String |  |

## u_mes_plan_changeoverStep

Kind: child | Data class: transaction | Parent: u_mes_plan_changeover | _id pattern: <changeoverId>-S<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | changeoverId | String | u_mes_plan_changeover._id |
| 6 | changeoverName | String |  |
| 7 | stepNo | Int32 |  |
| 8 | description | String |  |
| 9 | internalExternal | String |  |
| 10 | completedAt | Date |  |
| 11 | completedById | String | u_mes_mast_user._id |
| 12 | completedBy | String |  |
| 13 | schemaVersion | Int32 |  |
| 14 | createdAt | Date |  |
| 15 | createdById | String | u_mes_mast_user._id |
| 16 | createdBy | String |  |
| 17 | updatedAt | Date |  |
| 18 | updatedById | String | u_mes_mast_user._id |
| 19 | updatedBy | String |  |

## u_mes_plan_changeoverRemovedTool

Kind: relationship | Data class: transaction | Parent: u_mes_plan_changeover | _id pattern: <changeoverId>-RT<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | changeoverId | String | u_mes_plan_changeover._id |
| 6 | changeoverName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | removedToolId | String | u_mes_maint_tool._id |
| 9 | removedToolName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mast_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mast_user._id |
| 16 | updatedBy | String |  |

## u_mes_plan_changeoverInstalledTool

Kind: relationship | Data class: transaction | Parent: u_mes_plan_changeover | _id pattern: <changeoverId>-IT<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | changeoverId | String | u_mes_plan_changeover._id |
| 6 | changeoverName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | installedToolId | String | u_mes_maint_tool._id |
| 9 | installedToolName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mast_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mast_user._id |
| 16 | updatedBy | String |  |

## u_mes_plan_changeoverPerformedByUser

Kind: relationship | Data class: transaction | Parent: u_mes_plan_changeover | _id pattern: <changeoverId>-PBU<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | changeoverId | String | u_mes_plan_changeover._id |
| 6 | changeoverName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | performedByUserId | String | u_mes_mast_user._id |
| 9 | performedByUserName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mast_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mast_user._id |
| 16 | updatedBy | String |  |

## u_mes_plan_shiftHandover

Kind: entity | Data class: transaction | Parent: - | _id pattern: SHO-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | productionDate | Date |  |
| 6 | shiftId | String | u_mes_mast_shift._id |
| 7 | shiftName | String |  |
| 8 | lineId | String | u_mes_mast_line._id |
| 9 | lineName | String |  |
| 10 | outgoingSupervisorUserId | String | u_mes_mast_user._id |
| 11 | outgoingSupervisorUserName | String |  |
| 12 | incomingSupervisorUserId | String | u_mes_mast_user._id |
| 13 | incomingSupervisorUserName | String |  |
| 14 | outputPlanned | Int32 |  |
| 15 | outputActual | Int32 |  |
| 16 | outputScrap | Int32 |  |
| 17 | outputRework | Int32 |  |
| 18 | oeePct | Decimal128 |  |
| 19 | safetyNotes | String |  |
| 20 | qualityNotes | String |  |
| 21 | maintenanceNotes | String |  |
| 22 | materialNotes | String |  |
| 23 | handedOverAt | Date |  |
| 24 | acknowledgedAt | Date |  |
| 25 | status | String |  |
| 26 | schemaVersion | Int32 |  |
| 27 | createdAt | Date |  |
| 28 | createdById | String | u_mes_mast_user._id |
| 29 | createdBy | String |  |
| 30 | updatedAt | Date |  |
| 31 | updatedById | String | u_mes_mast_user._id |
| 32 | updatedBy | String |  |

## u_mes_plan_shiftHandoverProductionOrder

Kind: relationship | Data class: transaction | Parent: u_mes_plan_shiftHandover | _id pattern: <shiftHandoverId>-PO<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | shiftHandoverId | String | u_mes_plan_shiftHandover._id |
| 6 | shiftHandoverName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | productionOrderId | String | u_mes_plan_productionOrder._id |
| 9 | productionOrderName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mast_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mast_user._id |
| 16 | updatedBy | String |  |

## u_mes_plan_shiftHandoverDowntimeEvent

Kind: relationship | Data class: transaction | Parent: u_mes_plan_shiftHandover | _id pattern: <shiftHandoverId>-DE<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | shiftHandoverId | String | u_mes_plan_shiftHandover._id |
| 6 | shiftHandoverName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | downtimeEventId | String | u_mes_perf_downtimeEvent._id |
| 9 | downtimeEventName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mast_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mast_user._id |
| 16 | updatedBy | String |  |

## u_mes_plan_shiftHandoverNonconformance

Kind: relationship | Data class: transaction | Parent: u_mes_plan_shiftHandover | _id pattern: <shiftHandoverId>-N<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | shiftHandoverId | String | u_mes_plan_shiftHandover._id |
| 6 | shiftHandoverName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | nonconformanceId | String | u_mes_qual_nonconformance._id |
| 9 | nonconformanceName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mast_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mast_user._id |
| 16 | updatedBy | String |  |

## u_mes_plan_shiftHandoverOpenItem

Kind: child | Data class: transaction | Parent: u_mes_plan_shiftHandover | _id pattern: <shiftHandoverId>-OI<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | shiftHandoverId | String | u_mes_plan_shiftHandover._id |
| 6 | shiftHandoverName | String |  |
| 7 | itemNo | Int32 |  |
| 8 | description | String |  |
| 9 | ownerUserId | String | u_mes_mast_user._id |
| 10 | ownerUserName | String |  |
| 11 | dueAt | Date |  |
| 12 | closed | Boolean |  |
| 13 | schemaVersion | Int32 |  |
| 14 | createdAt | Date |  |
| 15 | createdById | String | u_mes_mast_user._id |
| 16 | createdBy | String |  |
| 17 | updatedAt | Date |  |
| 18 | updatedById | String | u_mes_mast_user._id |
| 19 | updatedBy | String |  |

## u_mes_plan_andonEvent

Kind: entity | Data class: transaction | Parent: - | _id pattern: AND-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | workCenterId | String | u_mes_mast_workCenter._id |
| 6 | workCenterName | String |  |
| 7 | lineId | String | u_mes_mast_line._id |
| 8 | lineName | String |  |
| 9 | shiftId | String | u_mes_mast_shift._id |
| 10 | shiftName | String |  |
| 11 | andonTypeId | String | u_mes_plan_andonType._id |
| 12 | andonTypeName | String |  |
| 13 | reasonCodeId | String | u_mes_perf_reasonCode._id |
| 14 | reasonCodeName | String |  |
| 15 | raisedById | String | u_mes_mast_user._id |
| 16 | raisedBy | String |  |
| 17 | raisedAt | Date |  |
| 18 | acknowledgedById | String | u_mes_mast_user._id |
| 19 | acknowledgedBy | String |  |
| 20 | acknowledgedAt | Date |  |
| 21 | resolvedById | String | u_mes_mast_user._id |
| 22 | resolvedBy | String |  |
| 23 | resolvedAt | Date |  |
| 24 | responseSec | Int32 |  |
| 25 | resolutionSec | Int32 |  |
| 26 | lineStopped | Boolean |  |
| 27 | downtimeEventId | String | u_mes_perf_downtimeEvent._id |
| 28 | downtimeEventName | String |  |
| 29 | description | String |  |
| 30 | resolutionText | String |  |
| 31 | status | String |  |
| 32 | schemaVersion | Int32 |  |
| 33 | createdAt | Date |  |
| 34 | createdById | String | u_mes_mast_user._id |
| 35 | createdBy | String |  |
| 36 | updatedAt | Date |  |
| 37 | updatedById | String | u_mes_mast_user._id |
| 38 | updatedBy | String |  |

## u_mes_plan_andonEventEscalation

Kind: child | Data class: transaction | Parent: u_mes_plan_andonEvent | _id pattern: <andonEventId>-E<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | andonEventId | String | u_mes_plan_andonEvent._id |
| 6 | andonEventName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | level | Int32 |  |
| 9 | escalatedAt | Date |  |
| 10 | toUserId | String | u_mes_mast_user._id |
| 11 | toUserName | String |  |
| 12 | channel | String |  |
| 13 | schemaVersion | Int32 |  |
| 14 | createdAt | Date |  |
| 15 | createdById | String | u_mes_mast_user._id |
| 16 | createdBy | String |  |
| 17 | updatedAt | Date |  |
| 18 | updatedById | String | u_mes_mast_user._id |
| 19 | updatedBy | String |  |

## u_mes_plan_indirectActivity

Kind: entity | Data class: master | Parent: - | _id pattern: IND-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | description | String |  |
| 7 | isPaid | Boolean |  |
| 8 | costCenterId | String | u_mes_mast_costCenter._id |
| 9 | costCenterName | String |  |
| 10 | sequenceNo | Int32 |  |
| 11 | status | String |  |
| 12 | schemaVersion | Int32 |  |

## u_mes_plan_containerType

Kind: entity | Data class: master | Parent: - | _id pattern: CTT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | description | String |  |
| 7 | lengthMm | Decimal128 |  |
| 8 | widthMm | Decimal128 |  |
| 9 | heightMm | Decimal128 |  |
| 10 | tareWeightKg | Decimal128 |  |
| 11 | isReturnable | Boolean |  |
| 12 | sequenceNo | Int32 |  |
| 13 | status | String |  |
| 14 | schemaVersion | Int32 |  |

## u_mes_plan_andonType

Kind: entity | Data class: master | Parent: - | _id pattern: ANT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | description | String |  |
| 7 | colourCode | String |  |
| 8 | responsibleDepartmentId | String | u_mes_mast_department._id |
| 9 | responsibleDepartmentName | String |  |
| 10 | targetResponseSec | Int32 |  |
| 11 | sequenceNo | Int32 |  |
| 12 | status | String |  |
| 13 | schemaVersion | Int32 |  |
