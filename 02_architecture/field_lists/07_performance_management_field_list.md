# Field list - Performance Management (perf)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/07_performance_management/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_perf_reasonCode

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | reasonType | String | - |  |
| 7 | level | Int32 | - |  |
| 8 | parentReasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 9 | parentReasonCodeName | String | - |  |
| 10 | pathText | String | - |  |
| 11 | reasonCategoryId | String | - | u_mes_perf_reasonCategory._id |
| 12 | reasonCategoryName | String | - |  |
| 13 | lossCategoryId | String | - | u_mes_perf_lossCategory._id |
| 14 | lossCategoryName | String | - |  |
| 15 | oeeImpact | String | - |  |
| 16 | isPlanned | Boolean | - |  |
| 17 | responsibleDepartmentId | String | - | u_mes_mast_department._id |
| 18 | responsibleDepartmentName | String | - |  |
| 19 | requiresComment | Boolean | - |  |
| 20 | requiresMaintenanceWorkOrder | Boolean | - |  |
| 21 | sequenceNo | Int32 | - |  |
| 22 | status | String | - |  |
| 23 | schemaVersion | Int32 | - |  |

## u_mes_perf_equipmentState

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | equipmentId | String | - | u_mes_mast_equipment._id |
| 6 | equipmentName | String | - |  |
| 7 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 8 | workCenterName | String | - |  |
| 9 | stateCode | String | - |  |
| 10 | subStateCode | String | - |  |
| 11 | startedAt | Date | Datetime |  |
| 12 | endedAt | Date | Datetime |  |
| 13 | durationSec | Int32 | - |  |
| 14 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String | - |  |
| 16 | shiftId | String | - | u_mes_mast_shift._id |
| 17 | shiftName | String | - |  |
| 18 | productionDate | Date | Date |  |
| 19 | source | String | - |  |
| 20 | plcStateCode | String | - |  |
| 21 | downtimeEventId | String | - | u_mes_perf_downtimeEvent._id |
| 22 | downtimeEventName | String | - |  |
| 23 | status | String | - |  |
| 24 | schemaVersion | Int32 | - |  |
| 25 | createdAt | Date | Datetime |  |
| 26 | createdById | String | - | u_mes_mast_user._id |
| 27 | createdBy | String | - |  |
| 28 | updatedAt | Date | Datetime |  |
| 29 | updatedById | String | - | u_mes_mast_user._id |
| 30 | updatedBy | String | - |  |

## u_mes_perf_downtimeEvent

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | equipmentId | String | - | u_mes_mast_equipment._id |
| 6 | equipmentName | String | - |  |
| 7 | lineId | String | - | u_mes_mast_line._id |
| 8 | lineName | String | - |  |
| 9 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 10 | workCenterName | String | - |  |
| 11 | shiftId | String | - | u_mes_mast_shift._id |
| 12 | shiftName | String | - |  |
| 13 | productionDate | Date | Date |  |
| 14 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String | - |  |
| 16 | startedAt | Date | Datetime |  |
| 17 | endedAt | Date | Datetime |  |
| 18 | durationMinutes | Int32 | - |  |
| 19 | downtimeType | String | - |  |
| 20 | faultCode | String | - |  |
| 21 | faultText | String | - |  |
| 22 | reasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 23 | reasonCodeName | String | - |  |
| 24 | reasonPathText | String | - |  |
| 25 | actionText | String | - |  |
| 26 | isPlanned | Boolean | - |  |
| 27 | isMicroStop | Boolean | - |  |
| 28 | alarmId | String | - | u_mes_perf_alarm._id |
| 29 | alarmName | String | - |  |
| 30 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 31 | maintenanceWorkOrderName | String | - |  |
| 32 | reportedById | String | - | u_mes_mast_user._id |
| 33 | reportedBy | String | - |  |
| 34 | classifiedById | String | - | u_mes_mast_user._id |
| 35 | classifiedBy | String | - |  |
| 36 | classifiedAt | Date | Datetime |  |
| 37 | responseMinutes | Int32 | - |  |
| 38 | repairMinutes | Int32 | - |  |
| 39 | unitsLost | Int32 | - |  |
| 40 | captureSource | String | - |  |
| 41 | equipmentStateId | String | - | u_mes_perf_equipmentState._id |
| 42 | equipmentStateName | String | - |  |
| 43 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 44 | productVariantName | String | - |  |
| 45 | capaId | String | - | u_mes_qual_capa._id |
| 46 | capaName | String | - |  |
| 47 | status | String | - |  |
| 48 | schemaVersion | Int32 | - |  |
| 49 | createdAt | Date | Datetime |  |
| 50 | createdById | String | - | u_mes_mast_user._id |
| 51 | createdBy | String | - |  |
| 52 | updatedAt | Date | Datetime |  |
| 53 | updatedById | String | - | u_mes_mast_user._id |
| 54 | updatedBy | String | - |  |

## u_mes_perf_downtimeEventComment

Kind: child | Data class: transaction | Parent: u_mes_perf_downtimeEvent | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | downtimeEventId | String | - | u_mes_perf_downtimeEvent._id |
| 6 | downtimeEventName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | commentedAt | Date | Datetime |  |
| 9 | authorUserId | String | - | u_mes_mast_user._id |
| 10 | authorUserName | String | - |  |
| 11 | commentText | String | - |  |
| 12 | schemaVersion | Int32 | - |  |
| 13 | createdAt | Date | Datetime |  |
| 14 | createdById | String | - | u_mes_mast_user._id |
| 15 | createdBy | String | - |  |
| 16 | updatedAt | Date | Datetime |  |
| 17 | updatedById | String | - | u_mes_mast_user._id |
| 18 | updatedBy | String | - |  |

## u_mes_perf_productionCount

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 6 | workCenterName | String | - |  |
| 7 | lineId | String | - | u_mes_mast_line._id |
| 8 | lineName | String | - |  |
| 9 | shiftId | String | - | u_mes_mast_shift._id |
| 10 | shiftName | String | - |  |
| 11 | productionDate | Date | Date |  |
| 12 | hourStartAt | Date | Datetime |  |
| 13 | hourEndAt | Date | Datetime |  |
| 14 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String | - |  |
| 16 | itemId | String | - | u_mes_prod_item._id |
| 17 | itemName | String | - |  |
| 18 | targetQuantity | Int32 | - |  |
| 19 | goodQuantity | Int32 | - |  |
| 20 | rejectQuantity | Int32 | - |  |
| 21 | reworkQuantity | Int32 | - |  |
| 22 | cumulativeTarget | Int32 | - |  |
| 23 | cumulativeGood | Int32 | - |  |
| 24 | downtimeMinutes | Int32 | - |  |
| 25 | source | String | - |  |
| 26 | gapReason | String | - |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |
| 29 | createdAt | Date | Datetime |  |
| 30 | createdById | String | - | u_mes_mast_user._id |
| 31 | createdBy | String | - |  |
| 32 | updatedAt | Date | Datetime |  |
| 33 | updatedById | String | - | u_mes_mast_user._id |
| 34 | updatedBy | String | - |  |

## u_mes_perf_oeeRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | equipmentId | String | - | u_mes_mast_equipment._id |
| 6 | equipmentName | String | - |  |
| 7 | lineId | String | - | u_mes_mast_line._id |
| 8 | lineName | String | - |  |
| 9 | shiftId | String | - | u_mes_mast_shift._id |
| 10 | shiftName | String | - |  |
| 11 | productionDate | Date | Date |  |
| 12 | itemId | String | - | u_mes_prod_item._id |
| 13 | itemName | String | - |  |
| 14 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String | - |  |
| 16 | periodStartAt | Date | Datetime |  |
| 17 | periodEndAt | Date | Datetime |  |
| 18 | calendarMinutes | Int32 | - |  |
| 19 | plannedProductionMinutes | Int32 | - |  |
| 20 | plannedDowntimeMinutes | Int32 | - |  |
| 21 | unplannedDowntimeMinutes | Int32 | - |  |
| 22 | runMinutes | Int32 | - |  |
| 23 | idealCycleTimeSec | Decimal128 | - |  |
| 24 | totalCount | Int32 | - |  |
| 25 | goodCount | Int32 | - |  |
| 26 | rejectCount | Int32 | - |  |
| 27 | reworkCount | Int32 | - |  |
| 28 | availabilityPct | Decimal128 | - |  |
| 29 | performancePct | Decimal128 | - |  |
| 30 | qualityPct | Decimal128 | - |  |
| 31 | oeePct | Decimal128 | - |  |
| 32 | teepPct | Decimal128 | - |  |
| 33 | calculatedAt | Date | Datetime |  |
| 34 | calculationVersion | Int32 | - |  |
| 35 | status | String | - |  |
| 36 | schemaVersion | Int32 | - |  |
| 37 | createdAt | Date | Datetime |  |
| 38 | createdById | String | - | u_mes_mast_user._id |
| 39 | createdBy | String | - |  |
| 40 | updatedAt | Date | Datetime |  |
| 41 | updatedById | String | - | u_mes_mast_user._id |
| 42 | updatedBy | String | - |  |

## u_mes_perf_oeeRecordLoss

Kind: child | Data class: transaction | Parent: u_mes_perf_oeeRecord | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | oeeRecordId | String | - | u_mes_perf_oeeRecord._id |
| 6 | oeeRecordName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | lossCategoryId | String | - | u_mes_perf_lossCategory._id |
| 9 | lossCategoryName | String | - |  |
| 10 | reasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 11 | reasonCodeName | String | - |  |
| 12 | lossMinutes | Int32 | - |  |
| 13 | lossUnits | Int32 | - |  |
| 14 | schemaVersion | Int32 | - |  |
| 15 | createdAt | Date | Datetime |  |
| 16 | createdById | String | - | u_mes_mast_user._id |
| 17 | createdBy | String | - |  |
| 18 | updatedAt | Date | Datetime |  |
| 19 | updatedById | String | - | u_mes_mast_user._id |
| 20 | updatedBy | String | - |  |

## u_mes_perf_processTag

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | description | String | - |  |
| 6 | equipmentId | String | - | u_mes_mast_equipment._id |
| 7 | equipmentName | String | - |  |
| 8 | iotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 9 | iotDeviceName | String | - |  |
| 10 | sourceAddress | String | - |  |
| 11 | dataType | String | - |  |
| 12 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 13 | unitOfMeasureName | String | - |  |
| 14 | tagClass | String | - |  |
| 15 | scanRateMs | Int32 | - |  |
| 16 | deadband | Decimal128 | - |  |
| 17 | lowLimit | Decimal128 | - |  |
| 18 | highLimit | Decimal128 | - |  |
| 19 | lowLowLimit | Decimal128 | - |  |
| 20 | highHighLimit | Decimal128 | - |  |
| 21 | engineeringMin | Decimal128 | - |  |
| 22 | engineeringMax | Decimal128 | - |  |
| 23 | isCritical | Boolean | - |  |
| 24 | historise | Boolean | - |  |
| 25 | retentionDays | Int32 | - |  |
| 26 | aggregation | String | - |  |
| 27 | areaId | String | - | u_mes_mast_area._id |
| 28 | areaName | String | - |  |
| 29 | lineId | String | - | u_mes_mast_line._id |
| 30 | lineName | String | - |  |
| 31 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 32 | workCenterName | String | - |  |
| 33 | status | String | - |  |
| 34 | schemaVersion | Int32 | - |  |

## u_mes_perf_processReading

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | processTagId | String | - | u_mes_perf_processTag._id |
| 6 | processTagName | String | - |  |
| 7 | equipmentId | String | - | u_mes_mast_equipment._id |
| 8 | equipmentName | String | - |  |
| 9 | timestamp | Date | Datetime |  |
| 10 | tagValue | Double | - |  |
| 11 | tagValueText | String | - |  |
| 12 | signalQuality | String | - |  |
| 13 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 14 | productionOrderName | String | - |  |
| 15 | lotId | String | - | u_mes_plan_lot._id |
| 16 | lotName | String | - |  |
| 17 | inLimits | Boolean | - |  |
| 18 | areaId | String | - | u_mes_mast_area._id |
| 19 | areaName | String | - |  |
| 20 | shiftId | String | - | u_mes_mast_shift._id |
| 21 | shiftName | String | - |  |
| 22 | productionDate | Date | Date |  |
| 23 | schemaVersion | Int32 | - |  |
| 24 | createdAt | Date | Datetime |  |
| 25 | createdById | String | - | u_mes_mast_user._id |
| 26 | createdBy | String | - |  |
| 27 | updatedAt | Date | Datetime |  |
| 28 | updatedById | String | - | u_mes_mast_user._id |
| 29 | updatedBy | String | - |  |

## u_mes_perf_alarm

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | equipmentId | String | - | u_mes_mast_equipment._id |
| 6 | equipmentName | String | - |  |
| 7 | processTagId | String | - | u_mes_perf_processTag._id |
| 8 | processTagName | String | - |  |
| 9 | iotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 10 | iotDeviceName | String | - |  |
| 11 | alarmCode | String | - |  |
| 12 | alarmText | String | - |  |
| 13 | alarmClass | String | - |  |
| 14 | severity | Int32 | - |  |
| 15 | raisedAt | Date | Datetime |  |
| 16 | acknowledgedAt | Date | Datetime |  |
| 17 | acknowledgedById | String | - | u_mes_mast_user._id |
| 18 | acknowledgedBy | String | - |  |
| 19 | clearedAt | Date | Datetime |  |
| 20 | durationSec | Int32 | - |  |
| 21 | triggerValue | Decimal128 | - |  |
| 22 | limitValue | Decimal128 | - |  |
| 23 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 24 | productionOrderName | String | - |  |
| 25 | causedStop | Boolean | - |  |
| 26 | downtimeEventId | String | - | u_mes_perf_downtimeEvent._id |
| 27 | downtimeEventName | String | - |  |
| 28 | actionTaken | String | - |  |
| 29 | alarmDefinitionId | String | - | u_mes_perf_alarmDefinition._id |
| 30 | alarmDefinitionName | String | - |  |
| 31 | lineId | String | - | u_mes_mast_line._id |
| 32 | lineName | String | - |  |
| 33 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 34 | workCenterName | String | - |  |
| 35 | shiftId | String | - | u_mes_mast_shift._id |
| 36 | shiftName | String | - |  |
| 37 | productionDate | Date | Date |  |
| 38 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 39 | wipUnitName | String | - |  |
| 40 | blocksRestart | Boolean | - |  |
| 41 | restartAuthorizedById | String | - | u_mes_mast_user._id |
| 42 | restartAuthorizedBy | String | - |  |
| 43 | restartAuthorizedAt | Date | Datetime |  |
| 44 | closureReasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 45 | closureReasonCodeName | String | - |  |
| 46 | escalationLevel | Int32 | - |  |
| 47 | status | String | - |  |
| 48 | schemaVersion | Int32 | - |  |
| 49 | createdAt | Date | Datetime |  |
| 50 | createdById | String | - | u_mes_mast_user._id |
| 51 | createdBy | String | - |  |
| 52 | updatedAt | Date | Datetime |  |
| 53 | updatedById | String | - | u_mes_mast_user._id |
| 54 | updatedBy | String | - |  |

## u_mes_perf_torqueResult

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 6 | wipUnitName | String | - |  |
| 7 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 8 | operationExecutionName | String | - |  |
| 9 | equipmentId | String | - | u_mes_mast_equipment._id |
| 10 | equipmentName | String | - |  |
| 11 | toolId | String | - | u_mes_maint_tool._id |
| 12 | toolName | String | - |  |
| 13 | recipeId | String | - | u_mes_prod_recipe._id |
| 14 | recipeName | String | - |  |
| 15 | controllerIotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 16 | controllerIotDeviceName | String | - |  |
| 17 | operatorUserId | String | - | u_mes_mast_user._id |
| 18 | operatorUserName | String | - |  |
| 19 | jointName | String | - |  |
| 20 | programNo | String | - |  |
| 21 | tighteningNo | Int32 | - |  |
| 22 | attemptNo | Int32 | - |  |
| 23 | targetTorqueNm | Decimal128 | - |  |
| 24 | minTorqueNm | Decimal128 | - |  |
| 25 | maxTorqueNm | Decimal128 | - |  |
| 26 | finalTorqueNm | Decimal128 | - |  |
| 27 | targetAngleDeg | Decimal128 | - |  |
| 28 | minAngleDeg | Decimal128 | - |  |
| 29 | maxAngleDeg | Decimal128 | - |  |
| 30 | finalAngleDeg | Decimal128 | - |  |
| 31 | rundownTimeMs | Int32 | - |  |
| 32 | strategy | String | - |  |
| 33 | result | String | - |  |
| 34 | failureReason | String | - |  |
| 35 | curveControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 36 | curveControlledDocumentName | String | - |  |
| 37 | tightenedAt | Date | Datetime |  |
| 38 | controllerResultNo | String | - |  |
| 39 | curveEnvelopeId | String | - | u_mes_qual_curveEnvelope._id |
| 40 | curveEnvelopeName | String | - |  |
| 41 | measurementCurveId | String | - | u_mes_qual_measurementCurve._id |
| 42 | measurementCurveName | String | - |  |
| 43 | envelopeResult | String | - |  |
| 44 | status | String | - |  |
| 45 | schemaVersion | Int32 | - |  |
| 46 | createdAt | Date | Datetime |  |
| 47 | createdById | String | - | u_mes_mast_user._id |
| 48 | createdBy | String | - |  |
| 49 | updatedAt | Date | Datetime |  |
| 50 | updatedById | String | - | u_mes_mast_user._id |
| 51 | updatedBy | String | - |  |

## u_mes_perf_leakTestResult

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 6 | wipUnitName | String | - |  |
| 7 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 8 | operationExecutionName | String | - |  |
| 9 | equipmentId | String | - | u_mes_mast_equipment._id |
| 10 | equipmentName | String | - |  |
| 11 | recipeId | String | - | u_mes_prod_recipe._id |
| 12 | recipeName | String | - |  |
| 13 | testerIotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 14 | testerIotDeviceName | String | - |  |
| 15 | operatorUserId | String | - | u_mes_mast_user._id |
| 16 | operatorUserName | String | - |  |
| 17 | programNo | String | - |  |
| 18 | testMedium | String | - |  |
| 19 | attemptNo | Int32 | - |  |
| 20 | ambientTemperatureC | Decimal128 | - |  |
| 21 | partTemperatureC | Decimal128 | - |  |
| 22 | fixtureToolId | String | - | u_mes_maint_tool._id |
| 23 | fixtureToolName | String | - |  |
| 24 | masterLeakVerifiedAt | Date | Datetime |  |
| 25 | verdict | String | - |  |
| 26 | failureReason | String | - |  |
| 27 | testedAt | Date | Datetime |  |
| 28 | measurementCurveId | String | - | u_mes_qual_measurementCurve._id |
| 29 | measurementCurveName | String | - |  |
| 30 | status | String | - |  |
| 31 | schemaVersion | Int32 | - |  |
| 32 | createdAt | Date | Datetime |  |
| 33 | createdById | String | - | u_mes_mast_user._id |
| 34 | createdBy | String | - |  |
| 35 | updatedAt | Date | Datetime |  |
| 36 | updatedById | String | - | u_mes_mast_user._id |
| 37 | updatedBy | String | - |  |

## u_mes_perf_leakTestResultStage

Kind: child | Data class: transaction | Parent: u_mes_perf_leakTestResult | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | leakTestResultId | String | - | u_mes_perf_leakTestResult._id |
| 6 | leakTestResultName | String | - |  |
| 7 | stageNo | Int32 | - |  |
| 8 | stageName | String | - |  |
| 9 | testPressureBar | Decimal128 | - |  |
| 10 | fillTimeSec | Decimal128 | - |  |
| 11 | stabiliseTimeSec | Decimal128 | - |  |
| 12 | testTimeSec | Decimal128 | - |  |
| 13 | pressureDropPa | Decimal128 | - |  |
| 14 | leakRateSccm | Decimal128 | - |  |
| 15 | limitPressureDropPa | Decimal128 | - |  |
| 16 | limitLeakRateSccm | Decimal128 | - |  |
| 17 | stageResult | String | - |  |
| 18 | schemaVersion | Int32 | - |  |
| 19 | createdAt | Date | Datetime |  |
| 20 | createdById | String | - | u_mes_mast_user._id |
| 21 | createdBy | String | - |  |
| 22 | updatedAt | Date | Datetime |  |
| 23 | updatedById | String | - | u_mes_mast_user._id |
| 24 | updatedBy | String | - |  |

## u_mes_perf_energyReading

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | meterIotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 6 | meterIotDeviceName | String | - |  |
| 7 | equipmentId | String | - | u_mes_mast_equipment._id |
| 8 | equipmentName | String | - |  |
| 9 | lineId | String | - | u_mes_mast_line._id |
| 10 | lineName | String | - |  |
| 11 | shiftId | String | - | u_mes_mast_shift._id |
| 12 | shiftName | String | - |  |
| 13 | energyTypeId | String | - | u_mes_perf_energyType._id |
| 14 | energyTypeName | String | - |  |
| 15 | intervalStartAt | Date | Datetime |  |
| 16 | intervalEndAt | Date | Datetime |  |
| 17 | consumption | Decimal128 | - |  |
| 18 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 19 | unitOfMeasureName | String | - |  |
| 20 | meterReadingStart | Decimal128 | - |  |
| 21 | meterReadingEnd | Decimal128 | - |  |
| 22 | demandKw | Decimal128 | - |  |
| 23 | powerFactor | Double | - |  |
| 24 | costInr | Decimal128 | - |  |
| 25 | unitsProduced | Int32 | - |  |
| 26 | specificConsumption | Decimal128 | - |  |
| 27 | signalQuality | String | - |  |
| 28 | schemaVersion | Int32 | - |  |
| 29 | createdAt | Date | Datetime |  |
| 30 | createdById | String | - | u_mes_mast_user._id |
| 31 | createdBy | String | - |  |
| 32 | updatedAt | Date | Datetime |  |
| 33 | updatedById | String | - | u_mes_mast_user._id |
| 34 | updatedBy | String | - |  |

## u_mes_perf_lossCategory

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | oeeImpact | String | - |  |
| 8 | sixBigLossNo | Int32 | - |  |
| 9 | sequenceNo | Int32 | - |  |
| 10 | status | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_perf_reasonCategory

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | status | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_perf_energyType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 8 | unitOfMeasureName | String | - |  |
| 9 | sequenceNo | Int32 | - |  |
| 10 | status | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_perf_alarmDefinition

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | equipmentTypeId | String | - | u_mes_mast_equipmentType._id |
| 6 | equipmentTypeName | String | - |  |
| 7 | alarmCode | String | - |  |
| 8 | alarmText | String | - |  |
| 9 | alarmClass | String | - |  |
| 10 | severityClass | String | - |  |
| 11 | blocksRestart | Boolean | - |  |
| 12 | authorizingRoleId | String | - | u_mes_mast_role._id |
| 13 | authorizingRoleName | String | - |  |
| 14 | defaultReasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 15 | defaultReasonCodeName | String | - |  |
| 16 | escalationRuleId | String | - | u_mes_syst_escalationRule._id |
| 17 | escalationRuleName | String | - |  |
| 18 | createsDowntime | Boolean | - |  |
| 19 | responseInstruction | String | - |  |
| 20 | status | String | - |  |
| 21 | schemaVersion | Int32 | - |  |

## u_mes_perf_lossSummary

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | lineId | String | - | u_mes_mast_line._id |
| 6 | lineName | String | - |  |
| 7 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 8 | workCenterName | String | - |  |
| 9 | shiftId | String | - | u_mes_mast_shift._id |
| 10 | shiftName | String | - |  |
| 11 | productionDate | Date | Date |  |
| 12 | lossCategoryId | String | - | u_mes_perf_lossCategory._id |
| 13 | lossCategoryName | String | - |  |
| 14 | reasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 15 | reasonCodeName | String | - |  |
| 16 | isPlanned | Boolean | - |  |
| 17 | occurrenceCount | Int32 | - |  |
| 18 | lossMinutes | Int32 | - |  |
| 19 | lossUnits | Int32 | - |  |
| 20 | lossPctOfPlannedTime | Decimal128 | - |  |
| 21 | paretoRank | Int32 | - |  |
| 22 | cumulativePct | Decimal128 | - |  |
| 23 | maintenanceWorkOrderCount | Int32 | - |  |
| 24 | capaCount | Int32 | - |  |
| 25 | calculatedAt | Date | Datetime |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |
| 28 | createdAt | Date | Datetime |  |
| 29 | createdById | String | - | u_mes_mast_user._id |
| 30 | createdBy | String | - |  |
| 31 | updatedAt | Date | Datetime |  |
| 32 | updatedById | String | - | u_mes_mast_user._id |
| 33 | updatedBy | String | - |  |

## u_mes_perf_workCenterPerformance

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 6 | workCenterName | String | - |  |
| 7 | lineId | String | - | u_mes_mast_line._id |
| 8 | lineName | String | - |  |
| 9 | shiftId | String | - | u_mes_mast_shift._id |
| 10 | shiftName | String | - |  |
| 11 | productionDate | Date | Date |  |
| 12 | periodStartAt | Date | Datetime |  |
| 13 | periodEndAt | Date | Datetime |  |
| 14 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 15 | productVariantName | String | - |  |
| 16 | unitsCompleted | Int32 | - |  |
| 17 | throughputPerHour | Decimal128 | - |  |
| 18 | averageCycleTimeSec | Decimal128 | - |  |
| 19 | taktTimeSec | Decimal128 | - |  |
| 20 | taktBreachCount | Int32 | - |  |
| 21 | wipQuantity | Int32 | - |  |
| 22 | blockedMinutes | Decimal128 | - |  |
| 23 | starvedMinutes | Decimal128 | - |  |
| 24 | isConstraint | Boolean | - |  |
| 25 | rankInLine | Int32 | - |  |
| 26 | calculatedAt | Date | Datetime |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |
| 29 | createdAt | Date | Datetime |  |
| 30 | createdById | String | - | u_mes_mast_user._id |
| 31 | createdBy | String | - |  |
| 32 | updatedAt | Date | Datetime |  |
| 33 | updatedById | String | - | u_mes_mast_user._id |
| 34 | updatedBy | String | - |  |

## u_mes_perf_operatorPerformance

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | userId | String | - | u_mes_mast_user._id |
| 6 | userName | String | - |  |
| 7 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 8 | workCenterName | String | - |  |
| 9 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 10 | productVariantName | String | - |  |
| 11 | shiftId | String | - | u_mes_mast_shift._id |
| 12 | shiftName | String | - |  |
| 13 | productionDate | Date | Date |  |
| 14 | attendedMinutes | Decimal128 | - |  |
| 15 | earnedMinutes | Decimal128 | - |  |
| 16 | efficiencyPct | Decimal128 | - |  |
| 17 | goodQuantity | Int32 | - |  |
| 18 | rejectQuantity | Int32 | - |  |
| 19 | errorCount | Int32 | - |  |
| 20 | interlockCount | Int32 | - |  |
| 21 | calculatedAt | Date | Datetime |  |
| 22 | status | String | - |  |
| 23 | schemaVersion | Int32 | - |  |
| 24 | createdAt | Date | Datetime |  |
| 25 | createdById | String | - | u_mes_mast_user._id |
| 26 | createdBy | String | - |  |
| 27 | updatedAt | Date | Datetime |  |
| 28 | updatedById | String | - | u_mes_mast_user._id |
| 29 | updatedBy | String | - |  |
