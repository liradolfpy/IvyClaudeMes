# Field list - Equipment and performance (eqp)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/07_equipment_performance/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_eqp_reasonCode

Kind: entity | Data class: master | Parent: - | _id pattern: RSN-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | reasonType | String |  |
| 7 | level | Int32 |  |
| 8 | parentReasonCodeId | String | u_mes_eqp_reasonCode._id |
| 9 | parentReasonCodeName | String |  |
| 10 | pathText | String |  |
| 11 | reasonCategoryId | String | u_mes_eqp_reasonCategory._id |
| 12 | reasonCategoryName | String |  |
| 13 | lossCategoryId | String | u_mes_eqp_lossCategory._id |
| 14 | lossCategoryName | String |  |
| 15 | oeeImpact | String |  |
| 16 | isPlanned | Boolean |  |
| 17 | responsibleDepartmentId | String | u_mes_mdm_department._id |
| 18 | responsibleDepartmentName | String |  |
| 19 | requiresComment | Boolean |  |
| 20 | requiresMaintenanceWorkOrder | Boolean |  |
| 21 | sequenceNo | Int32 |  |
| 22 | status | String |  |
| 23 | schemaVersion | Int32 |  |

## u_mes_eqp_equipmentState

Kind: entity | Data class: transaction | Parent: - | _id pattern: EST-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | equipmentId | String | u_mes_mdm_equipment._id |
| 6 | equipmentName | String |  |
| 7 | workCenterId | String | u_mes_mdm_workCenter._id |
| 8 | workCenterName | String |  |
| 9 | stateCode | String |  |
| 10 | subStateCode | String |  |
| 11 | startedAt | Date |  |
| 12 | endedAt | Date |  |
| 13 | durationSec | Int32 |  |
| 14 | productionOrderId | String | u_mes_exe_productionOrder._id |
| 15 | productionOrderName | String |  |
| 16 | shiftId | String | u_mes_mdm_shift._id |
| 17 | shiftName | String |  |
| 18 | productionDate | Date |  |
| 19 | source | String |  |
| 20 | plcStateCode | String |  |
| 21 | downtimeEventId | String | u_mes_eqp_downtimeEvent._id |
| 22 | downtimeEventName | String |  |
| 23 | status | String |  |
| 24 | schemaVersion | Int32 |  |
| 25 | createdAt | Date |  |
| 26 | createdById | String | u_mes_mdm_user._id |
| 27 | createdBy | String |  |
| 28 | updatedAt | Date |  |
| 29 | updatedById | String | u_mes_mdm_user._id |
| 30 | updatedBy | String |  |

## u_mes_eqp_downtimeEvent

Kind: entity | Data class: transaction | Parent: - | _id pattern: DT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | equipmentId | String | u_mes_mdm_equipment._id |
| 6 | equipmentName | String |  |
| 7 | lineId | String | u_mes_mdm_line._id |
| 8 | lineName | String |  |
| 9 | workCenterId | String | u_mes_mdm_workCenter._id |
| 10 | workCenterName | String |  |
| 11 | shiftId | String | u_mes_mdm_shift._id |
| 12 | shiftName | String |  |
| 13 | productionDate | Date |  |
| 14 | productionOrderId | String | u_mes_exe_productionOrder._id |
| 15 | productionOrderName | String |  |
| 16 | startedAt | Date |  |
| 17 | endedAt | Date |  |
| 18 | durationMinutes | Int32 |  |
| 19 | downtimeType | String |  |
| 20 | faultCode | String |  |
| 21 | faultText | String |  |
| 22 | reasonCodeId | String | u_mes_eqp_reasonCode._id |
| 23 | reasonCodeName | String |  |
| 24 | reasonPathText | String |  |
| 25 | actionText | String |  |
| 26 | isPlanned | Boolean |  |
| 27 | isMicroStop | Boolean |  |
| 28 | alarmId | String | u_mes_eqp_alarm._id |
| 29 | alarmName | String |  |
| 30 | maintenanceWorkOrderId | String | u_mes_mnt_maintenanceWorkOrder._id |
| 31 | maintenanceWorkOrderName | String |  |
| 32 | reportedById | String | u_mes_mdm_user._id |
| 33 | reportedBy | String |  |
| 34 | classifiedById | String | u_mes_mdm_user._id |
| 35 | classifiedBy | String |  |
| 36 | classifiedAt | Date |  |
| 37 | responseMinutes | Int32 |  |
| 38 | repairMinutes | Int32 |  |
| 39 | unitsLost | Int32 |  |
| 40 | status | String |  |
| 41 | schemaVersion | Int32 |  |
| 42 | createdAt | Date |  |
| 43 | createdById | String | u_mes_mdm_user._id |
| 44 | createdBy | String |  |
| 45 | updatedAt | Date |  |
| 46 | updatedById | String | u_mes_mdm_user._id |
| 47 | updatedBy | String |  |

## u_mes_eqp_downtimeEventComment

Kind: child | Data class: transaction | Parent: u_mes_eqp_downtimeEvent | _id pattern: <downtimeEventId>-C<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | downtimeEventId | String | u_mes_eqp_downtimeEvent._id |
| 6 | downtimeEventName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | commentedAt | Date |  |
| 9 | authorUserId | String | u_mes_mdm_user._id |
| 10 | authorUserName | String |  |
| 11 | commentText | String |  |
| 12 | schemaVersion | Int32 |  |
| 13 | createdAt | Date |  |
| 14 | createdById | String | u_mes_mdm_user._id |
| 15 | createdBy | String |  |
| 16 | updatedAt | Date |  |
| 17 | updatedById | String | u_mes_mdm_user._id |
| 18 | updatedBy | String |  |

## u_mes_eqp_productionCount

Kind: entity | Data class: transaction | Parent: - | _id pattern: PC-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workCenterId | String | u_mes_mdm_workCenter._id |
| 6 | workCenterName | String |  |
| 7 | lineId | String | u_mes_mdm_line._id |
| 8 | lineName | String |  |
| 9 | shiftId | String | u_mes_mdm_shift._id |
| 10 | shiftName | String |  |
| 11 | productionDate | Date |  |
| 12 | hourStartAt | Date |  |
| 13 | hourEndAt | Date |  |
| 14 | productionOrderId | String | u_mes_exe_productionOrder._id |
| 15 | productionOrderName | String |  |
| 16 | itemId | String | u_mes_prd_item._id |
| 17 | itemName | String |  |
| 18 | targetQuantity | Int32 |  |
| 19 | goodQuantity | Int32 |  |
| 20 | rejectQuantity | Int32 |  |
| 21 | reworkQuantity | Int32 |  |
| 22 | cumulativeTarget | Int32 |  |
| 23 | cumulativeGood | Int32 |  |
| 24 | downtimeMinutes | Int32 |  |
| 25 | source | String |  |
| 26 | gapReason | String |  |
| 27 | status | String |  |
| 28 | schemaVersion | Int32 |  |
| 29 | createdAt | Date |  |
| 30 | createdById | String | u_mes_mdm_user._id |
| 31 | createdBy | String |  |
| 32 | updatedAt | Date |  |
| 33 | updatedById | String | u_mes_mdm_user._id |
| 34 | updatedBy | String |  |

## u_mes_eqp_oeeRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: OEE-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | equipmentId | String | u_mes_mdm_equipment._id |
| 6 | equipmentName | String |  |
| 7 | lineId | String | u_mes_mdm_line._id |
| 8 | lineName | String |  |
| 9 | shiftId | String | u_mes_mdm_shift._id |
| 10 | shiftName | String |  |
| 11 | productionDate | Date |  |
| 12 | itemId | String | u_mes_prd_item._id |
| 13 | itemName | String |  |
| 14 | productionOrderId | String | u_mes_exe_productionOrder._id |
| 15 | productionOrderName | String |  |
| 16 | periodStartAt | Date |  |
| 17 | periodEndAt | Date |  |
| 18 | calendarMinutes | Int32 |  |
| 19 | plannedProductionMinutes | Int32 |  |
| 20 | plannedDowntimeMinutes | Int32 |  |
| 21 | unplannedDowntimeMinutes | Int32 |  |
| 22 | runMinutes | Int32 |  |
| 23 | idealCycleTimeSec | Decimal128 |  |
| 24 | totalCount | Int32 |  |
| 25 | goodCount | Int32 |  |
| 26 | rejectCount | Int32 |  |
| 27 | reworkCount | Int32 |  |
| 28 | availabilityPct | Decimal128 |  |
| 29 | performancePct | Decimal128 |  |
| 30 | qualityPct | Decimal128 |  |
| 31 | oeePct | Decimal128 |  |
| 32 | teepPct | Decimal128 |  |
| 33 | calculatedAt | Date |  |
| 34 | calculationVersion | Int32 |  |
| 35 | status | String |  |
| 36 | schemaVersion | Int32 |  |
| 37 | createdAt | Date |  |
| 38 | createdById | String | u_mes_mdm_user._id |
| 39 | createdBy | String |  |
| 40 | updatedAt | Date |  |
| 41 | updatedById | String | u_mes_mdm_user._id |
| 42 | updatedBy | String |  |

## u_mes_eqp_oeeRecordLoss

Kind: child | Data class: transaction | Parent: u_mes_eqp_oeeRecord | _id pattern: <oeeRecordId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | oeeRecordId | String | u_mes_eqp_oeeRecord._id |
| 6 | oeeRecordName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | lossCategoryId | String | u_mes_eqp_lossCategory._id |
| 9 | lossCategoryName | String |  |
| 10 | reasonCodeId | String | u_mes_eqp_reasonCode._id |
| 11 | reasonCodeName | String |  |
| 12 | lossMinutes | Int32 |  |
| 13 | lossUnits | Int32 |  |
| 14 | schemaVersion | Int32 |  |
| 15 | createdAt | Date |  |
| 16 | createdById | String | u_mes_mdm_user._id |
| 17 | createdBy | String |  |
| 18 | updatedAt | Date |  |
| 19 | updatedById | String | u_mes_mdm_user._id |
| 20 | updatedBy | String |  |

## u_mes_eqp_processTag

Kind: entity | Data class: master | Parent: - | _id pattern: TAG-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | description | String |  |
| 6 | equipmentId | String | u_mes_mdm_equipment._id |
| 7 | equipmentName | String |  |
| 8 | iotDeviceId | String | u_mes_sys_iotDevice._id |
| 9 | iotDeviceName | String |  |
| 10 | sourceAddress | String |  |
| 11 | dataType | String |  |
| 12 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 13 | unitOfMeasureName | String |  |
| 14 | tagClass | String |  |
| 15 | scanRateMs | Int32 |  |
| 16 | deadband | Decimal128 |  |
| 17 | lowLimit | Decimal128 |  |
| 18 | highLimit | Decimal128 |  |
| 19 | lowLowLimit | Decimal128 |  |
| 20 | highHighLimit | Decimal128 |  |
| 21 | engineeringMin | Decimal128 |  |
| 22 | engineeringMax | Decimal128 |  |
| 23 | isCritical | Boolean |  |
| 24 | historise | Boolean |  |
| 25 | retentionDays | Int32 |  |
| 26 | aggregation | String |  |
| 27 | status | String |  |
| 28 | schemaVersion | Int32 |  |

## u_mes_eqp_processReading

Kind: entity | Data class: transaction | Parent: - | _id pattern: PD-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | processTagId | String | u_mes_eqp_processTag._id |
| 6 | processTagName | String |  |
| 7 | equipmentId | String | u_mes_mdm_equipment._id |
| 8 | equipmentName | String |  |
| 9 | timestamp | Date |  |
| 10 | tagValue | Double |  |
| 11 | tagValueText | String |  |
| 12 | signalQuality | String |  |
| 13 | productionOrderId | String | u_mes_exe_productionOrder._id |
| 14 | productionOrderName | String |  |
| 15 | lotId | String | u_mes_exe_lot._id |
| 16 | lotName | String |  |
| 17 | inLimits | Boolean |  |
| 18 | schemaVersion | Int32 |  |
| 19 | createdAt | Date |  |
| 20 | createdById | String | u_mes_mdm_user._id |
| 21 | createdBy | String |  |
| 22 | updatedAt | Date |  |
| 23 | updatedById | String | u_mes_mdm_user._id |
| 24 | updatedBy | String |  |

## u_mes_eqp_alarm

Kind: entity | Data class: transaction | Parent: - | _id pattern: ALM-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | equipmentId | String | u_mes_mdm_equipment._id |
| 6 | equipmentName | String |  |
| 7 | processTagId | String | u_mes_eqp_processTag._id |
| 8 | processTagName | String |  |
| 9 | iotDeviceId | String | u_mes_sys_iotDevice._id |
| 10 | iotDeviceName | String |  |
| 11 | alarmCode | String |  |
| 12 | alarmText | String |  |
| 13 | alarmClass | String |  |
| 14 | severity | Int32 |  |
| 15 | raisedAt | Date |  |
| 16 | acknowledgedAt | Date |  |
| 17 | acknowledgedById | String | u_mes_mdm_user._id |
| 18 | acknowledgedBy | String |  |
| 19 | clearedAt | Date |  |
| 20 | durationSec | Int32 |  |
| 21 | triggerValue | Decimal128 |  |
| 22 | limitValue | Decimal128 |  |
| 23 | productionOrderId | String | u_mes_exe_productionOrder._id |
| 24 | productionOrderName | String |  |
| 25 | causedStop | Boolean |  |
| 26 | downtimeEventId | String | u_mes_eqp_downtimeEvent._id |
| 27 | downtimeEventName | String |  |
| 28 | actionTaken | String |  |
| 29 | status | String |  |
| 30 | schemaVersion | Int32 |  |
| 31 | createdAt | Date |  |
| 32 | createdById | String | u_mes_mdm_user._id |
| 33 | createdBy | String |  |
| 34 | updatedAt | Date |  |
| 35 | updatedById | String | u_mes_mdm_user._id |
| 36 | updatedBy | String |  |

## u_mes_eqp_torqueResult

Kind: entity | Data class: transaction | Parent: - | _id pattern: TRQ-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | wipUnitId | String | u_mes_exe_wipUnit._id |
| 6 | wipUnitName | String |  |
| 7 | operationExecutionId | String | u_mes_exe_operationExecution._id |
| 8 | operationExecutionName | String |  |
| 9 | equipmentId | String | u_mes_mdm_equipment._id |
| 10 | equipmentName | String |  |
| 11 | toolId | String | u_mes_mnt_tool._id |
| 12 | toolName | String |  |
| 13 | recipeId | String | u_mes_prd_recipe._id |
| 14 | recipeName | String |  |
| 15 | controllerIotDeviceId | String | u_mes_sys_iotDevice._id |
| 16 | controllerIotDeviceName | String |  |
| 17 | operatorUserId | String | u_mes_mdm_user._id |
| 18 | operatorUserName | String |  |
| 19 | jointName | String |  |
| 20 | programNo | String |  |
| 21 | tighteningNo | Int32 |  |
| 22 | attemptNo | Int32 |  |
| 23 | targetTorqueNm | Decimal128 |  |
| 24 | minTorqueNm | Decimal128 |  |
| 25 | maxTorqueNm | Decimal128 |  |
| 26 | finalTorqueNm | Decimal128 |  |
| 27 | targetAngleDeg | Decimal128 |  |
| 28 | minAngleDeg | Decimal128 |  |
| 29 | maxAngleDeg | Decimal128 |  |
| 30 | finalAngleDeg | Decimal128 |  |
| 31 | rundownTimeMs | Int32 |  |
| 32 | strategy | String |  |
| 33 | result | String |  |
| 34 | failureReason | String |  |
| 35 | curveControlledDocumentId | String | u_mes_sys_controlledDocument._id |
| 36 | curveControlledDocumentName | String |  |
| 37 | tightenedAt | Date |  |
| 38 | controllerResultNo | String |  |
| 39 | status | String |  |
| 40 | schemaVersion | Int32 |  |
| 41 | createdAt | Date |  |
| 42 | createdById | String | u_mes_mdm_user._id |
| 43 | createdBy | String |  |
| 44 | updatedAt | Date |  |
| 45 | updatedById | String | u_mes_mdm_user._id |
| 46 | updatedBy | String |  |

## u_mes_eqp_leakTestResult

Kind: entity | Data class: transaction | Parent: - | _id pattern: LKT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | wipUnitId | String | u_mes_exe_wipUnit._id |
| 6 | wipUnitName | String |  |
| 7 | operationExecutionId | String | u_mes_exe_operationExecution._id |
| 8 | operationExecutionName | String |  |
| 9 | equipmentId | String | u_mes_mdm_equipment._id |
| 10 | equipmentName | String |  |
| 11 | recipeId | String | u_mes_prd_recipe._id |
| 12 | recipeName | String |  |
| 13 | testerIotDeviceId | String | u_mes_sys_iotDevice._id |
| 14 | testerIotDeviceName | String |  |
| 15 | operatorUserId | String | u_mes_mdm_user._id |
| 16 | operatorUserName | String |  |
| 17 | programNo | String |  |
| 18 | testMedium | String |  |
| 19 | attemptNo | Int32 |  |
| 20 | ambientTemperatureC | Decimal128 |  |
| 21 | partTemperatureC | Decimal128 |  |
| 22 | fixtureToolId | String | u_mes_mnt_tool._id |
| 23 | fixtureToolName | String |  |
| 24 | masterLeakVerifiedAt | Date |  |
| 25 | verdict | String |  |
| 26 | failureReason | String |  |
| 27 | testedAt | Date |  |
| 28 | status | String |  |
| 29 | schemaVersion | Int32 |  |
| 30 | createdAt | Date |  |
| 31 | createdById | String | u_mes_mdm_user._id |
| 32 | createdBy | String |  |
| 33 | updatedAt | Date |  |
| 34 | updatedById | String | u_mes_mdm_user._id |
| 35 | updatedBy | String |  |

## u_mes_eqp_leakTestResultStage

Kind: child | Data class: transaction | Parent: u_mes_eqp_leakTestResult | _id pattern: <leakTestResultId>-S<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | leakTestResultId | String | u_mes_eqp_leakTestResult._id |
| 6 | leakTestResultName | String |  |
| 7 | stageNo | Int32 |  |
| 8 | stageName | String |  |
| 9 | testPressureBar | Decimal128 |  |
| 10 | fillTimeSec | Decimal128 |  |
| 11 | stabiliseTimeSec | Decimal128 |  |
| 12 | testTimeSec | Decimal128 |  |
| 13 | pressureDropPa | Decimal128 |  |
| 14 | leakRateSccm | Decimal128 |  |
| 15 | limitPressureDropPa | Decimal128 |  |
| 16 | limitLeakRateSccm | Decimal128 |  |
| 17 | stageResult | String |  |
| 18 | schemaVersion | Int32 |  |
| 19 | createdAt | Date |  |
| 20 | createdById | String | u_mes_mdm_user._id |
| 21 | createdBy | String |  |
| 22 | updatedAt | Date |  |
| 23 | updatedById | String | u_mes_mdm_user._id |
| 24 | updatedBy | String |  |

## u_mes_eqp_lossCategory

Kind: entity | Data class: master | Parent: - | _id pattern: LSC-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | description | String |  |
| 7 | oeeImpact | String |  |
| 8 | sixBigLossNo | Int32 |  |
| 9 | sequenceNo | Int32 |  |
| 10 | status | String |  |
| 11 | schemaVersion | Int32 |  |

## u_mes_eqp_reasonCategory

Kind: entity | Data class: master | Parent: - | _id pattern: RCT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | description | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | status | String |  |
| 9 | schemaVersion | Int32 |  |
