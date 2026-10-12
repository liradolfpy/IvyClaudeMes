# Field list - Traceability (trac)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/05_traceability/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_trac_serialNumber

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | itemId | String | - | u_mes_prod_item._id |
| 6 | itemName | String | - |  |
| 7 | itemRevision | String | - |  |
| 8 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 9 | productVariantName | String | - |  |
| 10 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 11 | wipUnitName | String | - |  |
| 12 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 13 | productionOrderName | String | - |  |
| 14 | numberRangeId | String | - | u_mes_syst_numberRange._id |
| 15 | numberRangeName | String | - |  |
| 16 | dataMatrixPayload | String | - |  |
| 17 | issuedAt | Date | Datetime |  |
| 18 | markedAt | Date | Datetime |  |
| 19 | markedAtEquipmentId | String | - | u_mes_mast_equipment._id |
| 20 | markedAtEquipmentName | String | - |  |
| 21 | markGrade | String | - |  |
| 22 | markVerifiedAt | Date | Datetime |  |
| 23 | labelId | String | - | u_mes_matl_label._id |
| 24 | labelName | String | - |  |
| 25 | containerId | String | - | u_mes_plan_container._id |
| 26 | containerName | String | - |  |
| 27 | shipmentId | String | - | u_mes_matl_shipment._id |
| 28 | shipmentName | String | - |  |
| 29 | shippedAt | Date | Datetime |  |
| 30 | customerId | String | - | u_mes_mast_customer._id |
| 31 | customerName | String | - |  |
| 32 | voidReason | String | - |  |
| 33 | status | String | - |  |
| 34 | schemaVersion | Int32 | - |  |
| 35 | createdAt | Date | Datetime |  |
| 36 | createdById | String | - | u_mes_mast_user._id |
| 37 | createdBy | String | - |  |
| 38 | updatedAt | Date | Datetime |  |
| 39 | updatedById | String | - | u_mes_mast_user._id |
| 40 | updatedBy | String | - |  |

## u_mes_trac_genealogyLink

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | parentWipUnitId | String | - | u_mes_plan_wipUnit._id |
| 6 | parentWipUnitName | String | - |  |
| 7 | parentSerialNumberId | String | - | u_mes_trac_serialNumber._id |
| 8 | parentSerialNumberName | String | - |  |
| 9 | parentItemId | String | - | u_mes_prod_item._id |
| 10 | parentItemName | String | - |  |
| 11 | childType | String | - |  |
| 12 | childItemId | String | - | u_mes_prod_item._id |
| 13 | childItemName | String | - |  |
| 14 | childLotId | String | - | u_mes_plan_lot._id |
| 15 | childLotName | String | - |  |
| 16 | childSerialNo | String | - |  |
| 17 | quantity | Decimal128 | - |  |
| 18 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 19 | unitOfMeasureName | String | - |  |
| 20 | operationId | String | - | u_mes_prod_operation._id |
| 21 | operationName | String | - |  |
| 22 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 23 | operationExecutionName | String | - |  |
| 24 | materialConsumptionId | String | - | u_mes_matl_materialConsumption._id |
| 25 | materialConsumptionName | String | - |  |
| 26 | linkedAt | Date | Datetime |  |
| 27 | linkedById | String | - | u_mes_mast_user._id |
| 28 | linkedBy | String | - |  |
| 29 | linkType | String | - |  |
| 30 | removedAt | Date | Datetime |  |
| 31 | removedReason | String | - |  |
| 32 | status | String | - |  |
| 33 | schemaVersion | Int32 | - |  |
| 34 | createdAt | Date | Datetime |  |
| 35 | createdById | String | - | u_mes_mast_user._id |
| 36 | createdBy | String | - |  |
| 37 | updatedAt | Date | Datetime |  |
| 38 | updatedById | String | - | u_mes_mast_user._id |
| 39 | updatedBy | String | - |  |

## u_mes_trac_componentLotLink

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | parentLotId | String | - | u_mes_plan_lot._id |
| 6 | parentLotName | String | - |  |
| 7 | childLotId | String | - | u_mes_plan_lot._id |
| 8 | childLotName | String | - |  |
| 9 | parentItemId | String | - | u_mes_prod_item._id |
| 10 | parentItemName | String | - |  |
| 11 | childItemId | String | - | u_mes_prod_item._id |
| 12 | childItemName | String | - |  |
| 13 | linkType | String | - |  |
| 14 | quantity | Decimal128 | - |  |
| 15 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 16 | unitOfMeasureName | String | - |  |
| 17 | operationId | String | - | u_mes_prod_operation._id |
| 18 | operationName | String | - |  |
| 19 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 20 | operationExecutionName | String | - |  |
| 21 | linkedAt | Date | Datetime |  |
| 22 | linkedById | String | - | u_mes_mast_user._id |
| 23 | linkedBy | String | - |  |
| 24 | yieldPct | Decimal128 | - |  |
| 25 | status | String | - |  |
| 26 | schemaVersion | Int32 | - |  |
| 27 | createdAt | Date | Datetime |  |
| 28 | createdById | String | - | u_mes_mast_user._id |
| 29 | createdBy | String | - |  |
| 30 | updatedAt | Date | Datetime |  |
| 31 | updatedById | String | - | u_mes_mast_user._id |
| 32 | updatedBy | String | - |  |

## u_mes_trac_asBuiltRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 6 | wipUnitName | String | - |  |
| 7 | serialNumberId | String | - | u_mes_trac_serialNumber._id |
| 8 | serialNumberName | String | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | itemRevision | String | - |  |
| 12 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 13 | productVariantName | String | - |  |
| 14 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String | - |  |
| 16 | customerId | String | - | u_mes_mast_customer._id |
| 17 | customerName | String | - |  |
| 18 | builtAt | Date | Datetime |  |
| 19 | torqueTorqueResultId | String | - | u_mes_perf_torqueResult._id |
| 20 | torqueTorqueResultName | String | - |  |
| 21 | torqueFinalTorqueNm | Decimal128 | - |  |
| 22 | torqueFinalAngleDeg | Decimal128 | - |  |
| 23 | leakTestLeakTestResultId | String | - | u_mes_perf_leakTestResult._id |
| 24 | leakTestLeakTestResultName | String | - |  |
| 25 | leakTestVerdict | String | - |  |
| 26 | leakTestLeakRate | Decimal128 | - |  |
| 27 | bodyLotId | String | - | u_mes_plan_lot._id |
| 28 | bodyLotName | String | - |  |
| 29 | castingLotId | String | - | u_mes_plan_lot._id |
| 30 | castingLotName | String | - |  |
| 31 | heatTreatmentLotId | String | - | u_mes_plan_lot._id |
| 32 | heatTreatmentLotName | String | - |  |
| 33 | reworkCount | Int32 | - |  |
| 34 | deviationPermitId | String | - | u_mes_qual_deviationPermit._id |
| 35 | deviationPermitName | String | - |  |
| 36 | containerId | String | - | u_mes_plan_container._id |
| 37 | containerName | String | - |  |
| 38 | shipmentId | String | - | u_mes_matl_shipment._id |
| 39 | shipmentName | String | - |  |
| 40 | finalReleaseById | String | - | u_mes_mast_user._id |
| 41 | finalReleaseBy | String | - |  |
| 42 | finalReleaseAt | Date | Datetime |  |
| 43 | recordHash | String | - |  |
| 44 | status | String | - |  |
| 45 | schemaVersion | Int32 | - |  |
| 46 | createdAt | Date | Datetime |  |
| 47 | createdById | String | - | u_mes_mast_user._id |
| 48 | createdBy | String | - |  |
| 49 | updatedAt | Date | Datetime |  |
| 50 | updatedById | String | - | u_mes_mast_user._id |
| 51 | updatedBy | String | - |  |

## u_mes_trac_asBuiltRecordComponent

Kind: child | Data class: transaction | Parent: u_mes_trac_asBuiltRecord | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | asBuiltRecordId | String | - | u_mes_trac_asBuiltRecord._id |
| 6 | asBuiltRecordName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | lotId | String | - | u_mes_plan_lot._id |
| 11 | lotName | String | - |  |
| 12 | serialNo | String | - |  |
| 13 | quantity | Int32 | - |  |
| 14 | genealogyLinkId | String | - | u_mes_trac_genealogyLink._id |
| 15 | genealogyLinkName | String | - |  |
| 16 | schemaVersion | Int32 | - |  |
| 17 | createdAt | Date | Datetime |  |
| 18 | createdById | String | - | u_mes_mast_user._id |
| 19 | createdBy | String | - |  |
| 20 | updatedAt | Date | Datetime |  |
| 21 | updatedById | String | - | u_mes_mast_user._id |
| 22 | updatedBy | String | - |  |

## u_mes_trac_asBuiltRecordOperation

Kind: child | Data class: transaction | Parent: u_mes_trac_asBuiltRecord | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | asBuiltRecordId | String | - | u_mes_trac_asBuiltRecord._id |
| 6 | asBuiltRecordName | String | - |  |
| 7 | stepNo | Int32 | - |  |
| 8 | operationId | String | - | u_mes_prod_operation._id |
| 9 | operationName | String | - |  |
| 10 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - |  |
| 12 | equipmentId | String | - | u_mes_mast_equipment._id |
| 13 | equipmentName | String | - |  |
| 14 | operatorUserId | String | - | u_mes_mast_user._id |
| 15 | operatorUserName | String | - |  |
| 16 | completedAt | Date | Datetime |  |
| 17 | result | String | - |  |
| 18 | schemaVersion | Int32 | - |  |
| 19 | createdAt | Date | Datetime |  |
| 20 | createdById | String | - | u_mes_mast_user._id |
| 21 | createdBy | String | - |  |
| 22 | updatedAt | Date | Datetime |  |
| 23 | updatedById | String | - | u_mes_mast_user._id |
| 24 | updatedBy | String | - |  |

## u_mes_trac_asBuiltRecordInspectionResult

Kind: relationship | Data class: transaction | Parent: u_mes_trac_asBuiltRecord | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | asBuiltRecordId | String | - | u_mes_trac_asBuiltRecord._id |
| 6 | asBuiltRecordName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | inspectionResultId | String | - | u_mes_qual_inspectionResult._id |
| 9 | inspectionResultName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |
