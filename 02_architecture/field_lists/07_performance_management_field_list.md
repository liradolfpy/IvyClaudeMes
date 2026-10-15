# Field list - PerformanceManagement (perf)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/07_performance_management/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_perf_reasonCode

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | reasonType | String | - |  |
| 8 | level | Int32 | - |  |
| 9 | parentReasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 10 | parentReasonCodeName | String | - |  |
| 11 | pathText | String | - |  |
| 12 | reasonCategoryId | String | - | u_mes_perf_reasonCategory._id |
| 13 | reasonCategoryName | String | - |  |
| 14 | lossCategoryId | String | - | u_mes_perf_lossCategory._id |
| 15 | lossCategoryName | String | - |  |
| 16 | oeeImpact | String | - |  |
| 17 | isPlanned | Boolean | - |  |
| 18 | responsibleDepartmentId | String | - | u_mes_mast_department._id |
| 19 | responsibleDepartmentName | String | - |  |
| 20 | requiresComment | Boolean | - |  |
| 21 | requiresMaintenanceWorkOrder | Boolean | - |  |
| 22 | sequenceNo | Int32 | - |  |
| 23 | status | String | - |  |
| 24 | schemaVersion | Int32 | - |  |

## u_mes_perf_equipmentState

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | equipmentId | String | - | u_mes_mast_equipment._id |
| 7 | equipmentName | String | - |  |
| 8 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - |  |
| 10 | stateCode | String | - |  |
| 11 | subStateCode | String | - |  |
| 12 | startedAt | Date | Datetime |  |
| 13 | endedAt | Date | Datetime |  |
| 14 | durationSec | Int32 | - |  |
| 15 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - |  |
| 17 | shiftId | String | - | u_mes_mast_shift._id |
| 18 | shiftName | String | - |  |
| 19 | productionDate | Date | Date |  |
| 20 | source | String | - |  |
| 21 | plcStateCode | String | - |  |
| 22 | downtimeEventId | String | - | u_mes_perf_downtimeEvent._id |
| 23 | downtimeEventName | String | - |  |
| 24 | status | String | - |  |
| 25 | schemaVersion | Int32 | - |  |
| 26 | createdAt | Date | Datetime |  |
| 27 | createdById | String | - | u_mes_mast_user._id |
| 28 | createdBy | String | - |  |
| 29 | updatedAt | Date | Datetime |  |
| 30 | updatedById | String | - | u_mes_mast_user._id |
| 31 | updatedBy | String | - |  |

## u_mes_perf_downtimeEvent

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | equipmentId | String | - | u_mes_mast_equipment._id |
| 7 | equipmentName | String | - |  |
| 8 | lineId | String | - | u_mes_mast_line._id |
| 9 | lineName | String | - |  |
| 10 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - |  |
| 12 | shiftId | String | - | u_mes_mast_shift._id |
| 13 | shiftName | String | - |  |
| 14 | productionDate | Date | Date |  |
| 15 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - |  |
| 17 | startedAt | Date | Datetime |  |
| 18 | endedAt | Date | Datetime |  |
| 19 | durationMinutes | Int32 | - |  |
| 20 | downtimeType | String | - |  |
| 21 | faultCode | String | - |  |
| 22 | faultText | String | - |  |
| 23 | reasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 24 | reasonCodeName | String | - |  |
| 25 | reasonPathText | String | - |  |
| 26 | actionText | String | - |  |
| 27 | isPlanned | Boolean | - |  |
| 28 | isMicroStop | Boolean | - |  |
| 29 | alarmId | String | - | u_mes_perf_alarm._id |
| 30 | alarmName | String | - |  |
| 31 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 32 | maintenanceWorkOrderName | String | - |  |
| 33 | reportedById | String | - | u_mes_mast_user._id |
| 34 | reportedBy | String | - |  |
| 35 | classifiedById | String | - | u_mes_mast_user._id |
| 36 | classifiedBy | String | - |  |
| 37 | classifiedAt | Date | Datetime |  |
| 38 | responseMinutes | Int32 | - |  |
| 39 | repairMinutes | Int32 | - |  |
| 40 | unitsLost | Int32 | - |  |
| 41 | captureSource | String | - |  |
| 42 | equipmentStateId | String | - | u_mes_perf_equipmentState._id |
| 43 | equipmentStateName | String | - |  |
| 44 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 45 | productVariantName | String | - |  |
| 46 | capaId | String | - | u_mes_qual_capa._id |
| 47 | capaName | String | - |  |
| 48 | status | String | - |  |
| 49 | schemaVersion | Int32 | - |  |
| 50 | createdAt | Date | Datetime |  |
| 51 | createdById | String | - | u_mes_mast_user._id |
| 52 | createdBy | String | - |  |
| 53 | updatedAt | Date | Datetime |  |
| 54 | updatedById | String | - | u_mes_mast_user._id |
| 55 | updatedBy | String | - |  |

## u_mes_perf_downtimeEventComment

Kind: child | Data class: transaction | Parent: u_mes_perf_downtimeEvent | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | downtimeEventId | String | - | u_mes_perf_downtimeEvent._id |
| 7 | downtimeEventName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | commentedAt | Date | Datetime |  |
| 10 | authorUserId | String | - | u_mes_mast_user._id |
| 11 | authorUserName | String | - |  |
| 12 | commentText | String | - |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_perf_productionCount

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
| 12 | productionDate | Date | Date |  |
| 13 | hourStartAt | Date | Datetime |  |
| 14 | hourEndAt | Date | Datetime |  |
| 15 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - |  |
| 17 | itemId | String | - | u_mes_prod_item._id |
| 18 | itemName | String | - |  |
| 19 | targetQuantity | Int32 | - |  |
| 20 | goodQuantity | Int32 | - |  |
| 21 | rejectQuantity | Int32 | - |  |
| 22 | reworkQuantity | Int32 | - |  |
| 23 | cumulativeTarget | Int32 | - |  |
| 24 | cumulativeGood | Int32 | - |  |
| 25 | downtimeMinutes | Int32 | - |  |
| 26 | source | String | - |  |
| 27 | gapReason | String | - |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |
| 30 | createdAt | Date | Datetime |  |
| 31 | createdById | String | - | u_mes_mast_user._id |
| 32 | createdBy | String | - |  |
| 33 | updatedAt | Date | Datetime |  |
| 34 | updatedById | String | - | u_mes_mast_user._id |
| 35 | updatedBy | String | - |  |

## u_mes_perf_oeeRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | equipmentId | String | - | u_mes_mast_equipment._id |
| 7 | equipmentName | String | - |  |
| 8 | lineId | String | - | u_mes_mast_line._id |
| 9 | lineName | String | - |  |
| 10 | shiftId | String | - | u_mes_mast_shift._id |
| 11 | shiftName | String | - |  |
| 12 | productionDate | Date | Date |  |
| 13 | itemId | String | - | u_mes_prod_item._id |
| 14 | itemName | String | - |  |
| 15 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - |  |
| 17 | periodStartAt | Date | Datetime |  |
| 18 | periodEndAt | Date | Datetime |  |
| 19 | calendarMinutes | Int32 | - |  |
| 20 | plannedProductionMinutes | Int32 | - |  |
| 21 | plannedDowntimeMinutes | Int32 | - |  |
| 22 | unplannedDowntimeMinutes | Int32 | - |  |
| 23 | runMinutes | Int32 | - |  |
| 24 | idealCycleTimeSec | Decimal128 | - |  |
| 25 | totalCount | Int32 | - |  |
| 26 | goodCount | Int32 | - |  |
| 27 | rejectCount | Int32 | - |  |
| 28 | reworkCount | Int32 | - |  |
| 29 | availabilityPct | Decimal128 | - |  |
| 30 | performancePct | Decimal128 | - |  |
| 31 | qualityPct | Decimal128 | - |  |
| 32 | oeePct | Decimal128 | - |  |
| 33 | teepPct | Decimal128 | - |  |
| 34 | calculatedAt | Date | Datetime |  |
| 35 | calculationVersion | Int32 | - |  |
| 36 | status | String | - |  |
| 37 | schemaVersion | Int32 | - |  |
| 38 | createdAt | Date | Datetime |  |
| 39 | createdById | String | - | u_mes_mast_user._id |
| 40 | createdBy | String | - |  |
| 41 | updatedAt | Date | Datetime |  |
| 42 | updatedById | String | - | u_mes_mast_user._id |
| 43 | updatedBy | String | - |  |

## u_mes_perf_oeeRecordLoss

Kind: child | Data class: transaction | Parent: u_mes_perf_oeeRecord | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | oeeRecordId | String | - | u_mes_perf_oeeRecord._id |
| 7 | oeeRecordName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | lossCategoryId | String | - | u_mes_perf_lossCategory._id |
| 10 | lossCategoryName | String | - |  |
| 11 | reasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 12 | reasonCodeName | String | - |  |
| 13 | lossMinutes | Int32 | - |  |
| 14 | lossUnits | Int32 | - |  |
| 15 | schemaVersion | Int32 | - |  |
| 16 | createdAt | Date | Datetime |  |
| 17 | createdById | String | - | u_mes_mast_user._id |
| 18 | createdBy | String | - |  |
| 19 | updatedAt | Date | Datetime |  |
| 20 | updatedById | String | - | u_mes_mast_user._id |
| 21 | updatedBy | String | - |  |

## u_mes_perf_processTag

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | description | String | - |  |
| 7 | equipmentId | String | - | u_mes_mast_equipment._id |
| 8 | equipmentName | String | - |  |
| 9 | iotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 10 | iotDeviceName | String | - |  |
| 11 | sourceAddress | String | - |  |
| 12 | dataType | String | - |  |
| 13 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 14 | unitOfMeasureName | String | - |  |
| 15 | tagClass | String | - |  |
| 16 | scanRateMs | Int32 | - |  |
| 17 | deadband | Decimal128 | - |  |
| 18 | lowLimit | Decimal128 | - |  |
| 19 | highLimit | Decimal128 | - |  |
| 20 | lowLowLimit | Decimal128 | - |  |
| 21 | highHighLimit | Decimal128 | - |  |
| 22 | engineeringMin | Decimal128 | - |  |
| 23 | engineeringMax | Decimal128 | - |  |
| 24 | isCritical | Boolean | - |  |
| 25 | historise | Boolean | - |  |
| 26 | retentionDays | Int32 | - |  |
| 27 | aggregation | String | - |  |
| 28 | areaId | String | - | u_mes_mast_area._id |
| 29 | areaName | String | - |  |
| 30 | lineId | String | - | u_mes_mast_line._id |
| 31 | lineName | String | - |  |
| 32 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 33 | workCenterName | String | - |  |
| 34 | status | String | - |  |
| 35 | schemaVersion | Int32 | - |  |

## u_mes_perf_processReading

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | processTagId | String | - | u_mes_perf_processTag._id |
| 7 | processTagName | String | - |  |
| 8 | equipmentId | String | - | u_mes_mast_equipment._id |
| 9 | equipmentName | String | - |  |
| 10 | timestamp | Date | Datetime |  |
| 11 | tagValue | Double | - |  |
| 12 | tagValueText | String | - |  |
| 13 | signalQuality | String | - |  |
| 14 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String | - |  |
| 16 | lotId | String | - | u_mes_plan_lot._id |
| 17 | lotName | String | - |  |
| 18 | inLimits | Boolean | - |  |
| 19 | areaId | String | - | u_mes_mast_area._id |
| 20 | areaName | String | - |  |
| 21 | shiftId | String | - | u_mes_mast_shift._id |
| 22 | shiftName | String | - |  |
| 23 | productionDate | Date | Date |  |
| 24 | schemaVersion | Int32 | - |  |
| 25 | createdAt | Date | Datetime |  |
| 26 | createdById | String | - | u_mes_mast_user._id |
| 27 | createdBy | String | - |  |
| 28 | updatedAt | Date | Datetime |  |
| 29 | updatedById | String | - | u_mes_mast_user._id |
| 30 | updatedBy | String | - |  |

## u_mes_perf_alarm

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | equipmentId | String | - | u_mes_mast_equipment._id |
| 7 | equipmentName | String | - |  |
| 8 | processTagId | String | - | u_mes_perf_processTag._id |
| 9 | processTagName | String | - |  |
| 10 | iotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 11 | iotDeviceName | String | - |  |
| 12 | alarmCode | String | - |  |
| 13 | alarmText | String | - |  |
| 14 | alarmClass | String | - |  |
| 15 | severity | Int32 | - |  |
| 16 | raisedAt | Date | Datetime |  |
| 17 | acknowledgedAt | Date | Datetime |  |
| 18 | acknowledgedById | String | - | u_mes_mast_user._id |
| 19 | acknowledgedBy | String | - |  |
| 20 | clearedAt | Date | Datetime |  |
| 21 | durationSec | Int32 | - |  |
| 22 | triggerValue | Decimal128 | - |  |
| 23 | limitValue | Decimal128 | - |  |
| 24 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 25 | productionOrderName | String | - |  |
| 26 | causedStop | Boolean | - |  |
| 27 | downtimeEventId | String | - | u_mes_perf_downtimeEvent._id |
| 28 | downtimeEventName | String | - |  |
| 29 | actionTaken | String | - |  |
| 30 | alarmDefinitionId | String | - | u_mes_perf_alarmDefinition._id |
| 31 | alarmDefinitionName | String | - |  |
| 32 | lineId | String | - | u_mes_mast_line._id |
| 33 | lineName | String | - |  |
| 34 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 35 | workCenterName | String | - |  |
| 36 | shiftId | String | - | u_mes_mast_shift._id |
| 37 | shiftName | String | - |  |
| 38 | productionDate | Date | Date |  |
| 39 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 40 | wipUnitName | String | - |  |
| 41 | blocksRestart | Boolean | - |  |
| 42 | restartAuthorizedById | String | - | u_mes_mast_user._id |
| 43 | restartAuthorizedBy | String | - |  |
| 44 | restartAuthorizedAt | Date | Datetime |  |
| 45 | closureReasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 46 | closureReasonCodeName | String | - |  |
| 47 | escalationLevel | Int32 | - |  |
| 48 | status | String | - |  |
| 49 | schemaVersion | Int32 | - |  |
| 50 | createdAt | Date | Datetime |  |
| 51 | createdById | String | - | u_mes_mast_user._id |
| 52 | createdBy | String | - |  |
| 53 | updatedAt | Date | Datetime |  |
| 54 | updatedById | String | - | u_mes_mast_user._id |
| 55 | updatedBy | String | - |  |

## u_mes_perf_torqueResult

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 7 | wipUnitName | String | - |  |
| 8 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 9 | operationExecutionName | String | - |  |
| 10 | equipmentId | String | - | u_mes_mast_equipment._id |
| 11 | equipmentName | String | - |  |
| 12 | toolId | String | - | u_mes_maint_tool._id |
| 13 | toolName | String | - |  |
| 14 | recipeId | String | - | u_mes_prod_recipe._id |
| 15 | recipeName | String | - |  |
| 16 | controllerIotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 17 | controllerIotDeviceName | String | - |  |
| 18 | operatorUserId | String | - | u_mes_mast_user._id |
| 19 | operatorUserName | String | - |  |
| 20 | jointName | String | - |  |
| 21 | programNo | String | - |  |
| 22 | tighteningNo | Int32 | - |  |
| 23 | attemptNo | Int32 | - |  |
| 24 | targetTorqueNm | Decimal128 | - |  |
| 25 | minTorqueNm | Decimal128 | - |  |
| 26 | maxTorqueNm | Decimal128 | - |  |
| 27 | finalTorqueNm | Decimal128 | - |  |
| 28 | targetAngleDeg | Decimal128 | - |  |
| 29 | minAngleDeg | Decimal128 | - |  |
| 30 | maxAngleDeg | Decimal128 | - |  |
| 31 | finalAngleDeg | Decimal128 | - |  |
| 32 | rundownTimeMs | Int32 | - |  |
| 33 | strategy | String | - |  |
| 34 | result | String | - |  |
| 35 | failureReason | String | - |  |
| 36 | curveControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 37 | curveControlledDocumentName | String | - |  |
| 38 | tightenedAt | Date | Datetime |  |
| 39 | controllerResultNo | String | - |  |
| 40 | curveEnvelopeId | String | - | u_mes_qual_curveEnvelope._id |
| 41 | curveEnvelopeName | String | - |  |
| 42 | measurementCurveId | String | - | u_mes_qual_measurementCurve._id |
| 43 | measurementCurveName | String | - |  |
| 44 | envelopeResult | String | - |  |
| 45 | status | String | - |  |
| 46 | schemaVersion | Int32 | - |  |
| 47 | createdAt | Date | Datetime |  |
| 48 | createdById | String | - | u_mes_mast_user._id |
| 49 | createdBy | String | - |  |
| 50 | updatedAt | Date | Datetime |  |
| 51 | updatedById | String | - | u_mes_mast_user._id |
| 52 | updatedBy | String | - |  |

## u_mes_perf_leakTestResult

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 7 | wipUnitName | String | - |  |
| 8 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 9 | operationExecutionName | String | - |  |
| 10 | equipmentId | String | - | u_mes_mast_equipment._id |
| 11 | equipmentName | String | - |  |
| 12 | recipeId | String | - | u_mes_prod_recipe._id |
| 13 | recipeName | String | - |  |
| 14 | testerIotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 15 | testerIotDeviceName | String | - |  |
| 16 | operatorUserId | String | - | u_mes_mast_user._id |
| 17 | operatorUserName | String | - |  |
| 18 | programNo | String | - |  |
| 19 | testMedium | String | - |  |
| 20 | attemptNo | Int32 | - |  |
| 21 | ambientTemperatureC | Decimal128 | - |  |
| 22 | partTemperatureC | Decimal128 | - |  |
| 23 | fixtureToolId | String | - | u_mes_maint_tool._id |
| 24 | fixtureToolName | String | - |  |
| 25 | masterLeakVerifiedAt | Date | Datetime |  |
| 26 | verdict | String | - |  |
| 27 | failureReason | String | - |  |
| 28 | testedAt | Date | Datetime |  |
| 29 | measurementCurveId | String | - | u_mes_qual_measurementCurve._id |
| 30 | measurementCurveName | String | - |  |
| 31 | status | String | - |  |
| 32 | schemaVersion | Int32 | - |  |
| 33 | createdAt | Date | Datetime |  |
| 34 | createdById | String | - | u_mes_mast_user._id |
| 35 | createdBy | String | - |  |
| 36 | updatedAt | Date | Datetime |  |
| 37 | updatedById | String | - | u_mes_mast_user._id |
| 38 | updatedBy | String | - |  |

## u_mes_perf_leakTestResultStage

Kind: child | Data class: transaction | Parent: u_mes_perf_leakTestResult | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | leakTestResultId | String | - | u_mes_perf_leakTestResult._id |
| 7 | leakTestResultName | String | - |  |
| 8 | stageNo | Int32 | - |  |
| 9 | stageName | String | - |  |
| 10 | testPressureBar | Decimal128 | - |  |
| 11 | fillTimeSec | Decimal128 | - |  |
| 12 | stabiliseTimeSec | Decimal128 | - |  |
| 13 | testTimeSec | Decimal128 | - |  |
| 14 | pressureDropPa | Decimal128 | - |  |
| 15 | leakRateSccm | Decimal128 | - |  |
| 16 | limitPressureDropPa | Decimal128 | - |  |
| 17 | limitLeakRateSccm | Decimal128 | - |  |
| 18 | stageResult | String | - |  |
| 19 | schemaVersion | Int32 | - |  |
| 20 | createdAt | Date | Datetime |  |
| 21 | createdById | String | - | u_mes_mast_user._id |
| 22 | createdBy | String | - |  |
| 23 | updatedAt | Date | Datetime |  |
| 24 | updatedById | String | - | u_mes_mast_user._id |
| 25 | updatedBy | String | - |  |

## u_mes_perf_energyReading

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | meterIotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 7 | meterIotDeviceName | String | - |  |
| 8 | equipmentId | String | - | u_mes_mast_equipment._id |
| 9 | equipmentName | String | - |  |
| 10 | lineId | String | - | u_mes_mast_line._id |
| 11 | lineName | String | - |  |
| 12 | shiftId | String | - | u_mes_mast_shift._id |
| 13 | shiftName | String | - |  |
| 14 | energyTypeId | String | - | u_mes_perf_energyType._id |
| 15 | energyTypeName | String | - |  |
| 16 | intervalStartAt | Date | Datetime |  |
| 17 | intervalEndAt | Date | Datetime |  |
| 18 | consumption | Decimal128 | - |  |
| 19 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 20 | unitOfMeasureName | String | - |  |
| 21 | meterReadingStart | Decimal128 | - |  |
| 22 | meterReadingEnd | Decimal128 | - |  |
| 23 | demandKw | Decimal128 | - |  |
| 24 | powerFactor | Double | - |  |
| 25 | costInr | Decimal128 | - |  |
| 26 | unitsProduced | Int32 | - |  |
| 27 | specificConsumption | Decimal128 | - |  |
| 28 | signalQuality | String | - |  |
| 29 | schemaVersion | Int32 | - |  |
| 30 | createdAt | Date | Datetime |  |
| 31 | createdById | String | - | u_mes_mast_user._id |
| 32 | createdBy | String | - |  |
| 33 | updatedAt | Date | Datetime |  |
| 34 | updatedById | String | - | u_mes_mast_user._id |
| 35 | updatedBy | String | - |  |

## u_mes_perf_lossCategory

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
| 8 | oeeImpact | String | - |  |
| 9 | sixBigLossNo | Int32 | - |  |
| 10 | sequenceNo | Int32 | - |  |
| 11 | status | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_perf_reasonCategory

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
| 8 | sequenceNo | Int32 | - |  |
| 9 | status | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_perf_energyType

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
| 8 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 9 | unitOfMeasureName | String | - |  |
| 10 | sequenceNo | Int32 | - |  |
| 11 | status | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_perf_alarmDefinition

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | equipmentTypeId | String | - | u_mes_mast_equipmentType._id |
| 7 | equipmentTypeName | String | - |  |
| 8 | alarmCode | String | - |  |
| 9 | alarmText | String | - |  |
| 10 | alarmClass | String | - |  |
| 11 | severityClass | String | - |  |
| 12 | blocksRestart | Boolean | - |  |
| 13 | authorizingRoleId | String | - | u_mes_mast_role._id |
| 14 | authorizingRoleName | String | - |  |
| 15 | defaultReasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 16 | defaultReasonCodeName | String | - |  |
| 17 | escalationRuleId | String | - | u_mes_syst_escalationRule._id |
| 18 | escalationRuleName | String | - |  |
| 19 | createsDowntime | Boolean | - |  |
| 20 | responseInstruction | String | - |  |
| 21 | status | String | - |  |
| 22 | schemaVersion | Int32 | - |  |

## u_mes_perf_lossSummary

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
| 10 | shiftId | String | - | u_mes_mast_shift._id |
| 11 | shiftName | String | - |  |
| 12 | productionDate | Date | Date |  |
| 13 | lossCategoryId | String | - | u_mes_perf_lossCategory._id |
| 14 | lossCategoryName | String | - |  |
| 15 | reasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 16 | reasonCodeName | String | - |  |
| 17 | isPlanned | Boolean | - |  |
| 18 | occurrenceCount | Int32 | - |  |
| 19 | lossMinutes | Int32 | - |  |
| 20 | lossUnits | Int32 | - |  |
| 21 | lossPctOfPlannedTime | Decimal128 | - |  |
| 22 | paretoRank | Int32 | - |  |
| 23 | cumulativePct | Decimal128 | - |  |
| 24 | maintenanceWorkOrderCount | Int32 | - |  |
| 25 | capaCount | Int32 | - |  |
| 26 | calculatedAt | Date | Datetime |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |
| 29 | createdAt | Date | Datetime |  |
| 30 | createdById | String | - | u_mes_mast_user._id |
| 31 | createdBy | String | - |  |
| 32 | updatedAt | Date | Datetime |  |
| 33 | updatedById | String | - | u_mes_mast_user._id |
| 34 | updatedBy | String | - |  |

## u_mes_perf_workCenterPerformance

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
| 12 | productionDate | Date | Date |  |
| 13 | periodStartAt | Date | Datetime |  |
| 14 | periodEndAt | Date | Datetime |  |
| 15 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 16 | productVariantName | String | - |  |
| 17 | unitsCompleted | Int32 | - |  |
| 18 | throughputPerHour | Decimal128 | - |  |
| 19 | averageCycleTimeSec | Decimal128 | - |  |
| 20 | taktTimeSec | Decimal128 | - |  |
| 21 | taktBreachCount | Int32 | - |  |
| 22 | wipQuantity | Int32 | - |  |
| 23 | blockedMinutes | Decimal128 | - |  |
| 24 | starvedMinutes | Decimal128 | - |  |
| 25 | isConstraint | Boolean | - |  |
| 26 | rankInLine | Int32 | - |  |
| 27 | calculatedAt | Date | Datetime |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |
| 30 | createdAt | Date | Datetime |  |
| 31 | createdById | String | - | u_mes_mast_user._id |
| 32 | createdBy | String | - |  |
| 33 | updatedAt | Date | Datetime |  |
| 34 | updatedById | String | - | u_mes_mast_user._id |
| 35 | updatedBy | String | - |  |

## u_mes_perf_operatorPerformance

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
| 10 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 11 | productVariantName | String | - |  |
| 12 | shiftId | String | - | u_mes_mast_shift._id |
| 13 | shiftName | String | - |  |
| 14 | productionDate | Date | Date |  |
| 15 | attendedMinutes | Decimal128 | - |  |
| 16 | earnedMinutes | Decimal128 | - |  |
| 17 | efficiencyPct | Decimal128 | - |  |
| 18 | goodQuantity | Int32 | - |  |
| 19 | rejectQuantity | Int32 | - |  |
| 20 | errorCount | Int32 | - |  |
| 21 | interlockCount | Int32 | - |  |
| 22 | calculatedAt | Date | Datetime |  |
| 23 | status | String | - |  |
| 24 | schemaVersion | Int32 | - |  |
| 25 | createdAt | Date | Datetime |  |
| 26 | createdById | String | - | u_mes_mast_user._id |
| 27 | createdBy | String | - |  |
| 28 | updatedAt | Date | Datetime |  |
| 29 | updatedById | String | - | u_mes_mast_user._id |
| 30 | updatedBy | String | - |  |
