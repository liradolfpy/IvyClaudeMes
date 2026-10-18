# Field list - Traceability (trac)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/05_traceability/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = n.nn (plain number, no NumberDecimal()); Double = Double(n); Boolean = true / false.

## u_mes_trac_serialNumber

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
| 8 | itemRevision | String | - |  |
| 9 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 10 | productVariantName | String | - |  |
| 11 | wipUnitId | String | - | u_mes_plan_wipUnit._id |
| 12 | wipUnitName | String | - |  |
| 13 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 14 | productionOrderName | String | - |  |
| 15 | numberRangeId | String | - | u_mes_syst_numberRange._id |
| 16 | numberRangeName | String | - |  |
| 17 | dataMatrixPayload | String | - |  |
| 18 | issuedAt | Date | Datetime |  |
| 19 | markedAt | Date | Datetime |  |
| 20 | markedAtEquipmentId | String | - | u_mes_mast_equipment._id |
| 21 | markedAtEquipmentName | String | - |  |
| 22 | markGrade | String | - |  |
| 23 | markVerifiedAt | Date | Datetime |  |
| 24 | labelId | String | - | u_mes_matl_label._id |
| 25 | labelName | String | - |  |
| 26 | containerId | String | - | u_mes_plan_container._id |
| 27 | containerName | String | - |  |
| 28 | shipmentId | String | - | u_mes_matl_shipment._id |
| 29 | shipmentName | String | - |  |
| 30 | shippedAt | Date | Datetime |  |
| 31 | customerId | String | - | u_mes_mast_customer._id |
| 32 | customerName | String | - |  |
| 33 | voidReason | String | - |  |
| 34 | markingRecipeId | String | - | u_mes_prod_recipe._id |
| 35 | markingRecipeName | String | - |  |
| 36 | markingRecipeVersion | String | - |  |
| 37 | status | String | - |  |
| 38 | schemaVersion | Int32 | - |  |
| 39 | createdAt | Date | Datetime |  |
| 40 | createdById | String | - | u_mes_mast_user._id |
| 41 | createdBy | String | - |  |
| 42 | updatedAt | Date | Datetime |  |
| 43 | updatedById | String | - | u_mes_mast_user._id |
| 44 | updatedBy | String | - |  |

## u_mes_trac_genealogyLink

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | parentWipUnitId | String | - | u_mes_plan_wipUnit._id |
| 7 | parentWipUnitName | String | - |  |
| 8 | parentSerialNumberId | String | - | u_mes_trac_serialNumber._id |
| 9 | parentSerialNumberName | String | - |  |
| 10 | parentItemId | String | - | u_mes_prod_item._id |
| 11 | parentItemName | String | - |  |
| 12 | childType | String | - |  |
| 13 | childItemId | String | - | u_mes_prod_item._id |
| 14 | childItemName | String | - |  |
| 15 | childLotId | String | - | u_mes_plan_lot._id |
| 16 | childLotName | String | - |  |
| 17 | childSerialNo | String | - |  |
| 18 | quantity | Decimal128 | - |  |
| 19 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 20 | unitOfMeasureName | String | - |  |
| 21 | operationId | String | - | u_mes_prod_operation._id |
| 22 | operationName | String | - |  |
| 23 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 24 | operationExecutionName | String | - |  |
| 25 | materialConsumptionId | String | - | u_mes_matl_materialConsumption._id |
| 26 | materialConsumptionName | String | - |  |
| 27 | linkedAt | Date | Datetime |  |
| 28 | linkedById | String | - | u_mes_mast_user._id |
| 29 | linkedBy | String | - |  |
| 30 | linkType | String | - |  |
| 31 | removedAt | Date | Datetime |  |
| 32 | removedReason | String | - |  |
| 33 | childSerialNumberId | String | - | u_mes_trac_serialNumber._id |
| 34 | childSerialNumberName | String | - |  |
| 35 | childWipUnitId | String | - | u_mes_plan_wipUnit._id |
| 36 | childWipUnitName | String | - |  |
| 37 | status | String | - |  |
| 38 | schemaVersion | Int32 | - |  |
| 39 | createdAt | Date | Datetime |  |
| 40 | createdById | String | - | u_mes_mast_user._id |
| 41 | createdBy | String | - |  |
| 42 | updatedAt | Date | Datetime |  |
| 43 | updatedById | String | - | u_mes_mast_user._id |
| 44 | updatedBy | String | - |  |

## u_mes_trac_componentLotLink

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | parentLotId | String | - | u_mes_plan_lot._id |
| 7 | parentLotName | String | - |  |
| 8 | childLotId | String | - | u_mes_plan_lot._id |
| 9 | childLotName | String | - |  |
| 10 | parentItemId | String | - | u_mes_prod_item._id |
| 11 | parentItemName | String | - |  |
| 12 | childItemId | String | - | u_mes_prod_item._id |
| 13 | childItemName | String | - |  |
| 14 | linkType | String | - |  |
| 15 | quantity | Decimal128 | - |  |
| 16 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 17 | unitOfMeasureName | String | - |  |
| 18 | operationId | String | - | u_mes_prod_operation._id |
| 19 | operationName | String | - |  |
| 20 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 21 | operationExecutionName | String | - |  |
| 22 | linkedAt | Date | Datetime |  |
| 23 | linkedById | String | - | u_mes_mast_user._id |
| 24 | linkedBy | String | - |  |
| 25 | yieldPct | Decimal128 | - |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |
| 28 | createdAt | Date | Datetime |  |
| 29 | createdById | String | - | u_mes_mast_user._id |
| 30 | createdBy | String | - |  |
| 31 | updatedAt | Date | Datetime |  |
| 32 | updatedById | String | - | u_mes_mast_user._id |
| 33 | updatedBy | String | - |  |

## u_mes_trac_asBuiltRecord

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
| 8 | serialNumberId | String | - | u_mes_trac_serialNumber._id |
| 9 | serialNumberName | String | - |  |
| 10 | itemId | String | - | u_mes_prod_item._id |
| 11 | itemName | String | - |  |
| 12 | itemRevision | String | - |  |
| 13 | productVariantId | String | - | u_mes_prod_productVariant._id |
| 14 | productVariantName | String | - |  |
| 15 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - |  |
| 17 | customerId | String | - | u_mes_mast_customer._id |
| 18 | customerName | String | - |  |
| 19 | builtAt | Date | Datetime |  |
| 20 | torqueTorqueResultId | String | - | u_mes_perf_torqueResult._id |
| 21 | torqueTorqueResultName | String | - |  |
| 22 | torqueFinalTorqueNm | Decimal128 | - |  |
| 23 | torqueFinalAngleDeg | Decimal128 | - |  |
| 24 | leakTestLeakTestResultId | String | - | u_mes_perf_leakTestResult._id |
| 25 | leakTestLeakTestResultName | String | - |  |
| 26 | leakTestVerdict | String | - |  |
| 27 | leakTestLeakRate | Decimal128 | - |  |
| 28 | bodyLotId | String | - | u_mes_plan_lot._id |
| 29 | bodyLotName | String | - |  |
| 30 | castingLotId | String | - | u_mes_plan_lot._id |
| 31 | castingLotName | String | - |  |
| 32 | heatTreatmentLotId | String | - | u_mes_plan_lot._id |
| 33 | heatTreatmentLotName | String | - |  |
| 34 | reworkCount | Int32 | - |  |
| 35 | deviationPermitId | String | - | u_mes_qual_deviationPermit._id |
| 36 | deviationPermitName | String | - |  |
| 37 | containerId | String | - | u_mes_plan_container._id |
| 38 | containerName | String | - |  |
| 39 | shipmentId | String | - | u_mes_matl_shipment._id |
| 40 | shipmentName | String | - |  |
| 41 | finalReleaseById | String | - | u_mes_mast_user._id |
| 42 | finalReleaseBy | String | - |  |
| 43 | finalReleaseAt | Date | Datetime |  |
| 44 | recordHash | String | - |  |
| 45 | genealogyComplete | Boolean | - |  |
| 46 | missingComponentCount | Int32 | - |  |
| 47 | status | String | - |  |
| 48 | schemaVersion | Int32 | - |  |
| 49 | createdAt | Date | Datetime |  |
| 50 | createdById | String | - | u_mes_mast_user._id |
| 51 | createdBy | String | - |  |
| 52 | updatedAt | Date | Datetime |  |
| 53 | updatedById | String | - | u_mes_mast_user._id |
| 54 | updatedBy | String | - |  |

## u_mes_trac_asBuiltRecordComponent

Kind: child | Data class: transaction | Parent: u_mes_trac_asBuiltRecord | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | asBuiltRecordId | String | - | u_mes_trac_asBuiltRecord._id |
| 7 | asBuiltRecordName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | lotId | String | - | u_mes_plan_lot._id |
| 12 | lotName | String | - |  |
| 13 | serialNo | String | - |  |
| 14 | quantity | Int32 | - |  |
| 15 | genealogyLinkId | String | - | u_mes_trac_genealogyLink._id |
| 16 | genealogyLinkName | String | - |  |
| 17 | schemaVersion | Int32 | - |  |
| 18 | createdAt | Date | Datetime |  |
| 19 | createdById | String | - | u_mes_mast_user._id |
| 20 | createdBy | String | - |  |
| 21 | updatedAt | Date | Datetime |  |
| 22 | updatedById | String | - | u_mes_mast_user._id |
| 23 | updatedBy | String | - |  |

## u_mes_trac_asBuiltRecordOperation

Kind: child | Data class: transaction | Parent: u_mes_trac_asBuiltRecord | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | asBuiltRecordId | String | - | u_mes_trac_asBuiltRecord._id |
| 7 | asBuiltRecordName | String | - |  |
| 8 | stepNo | Int32 | - |  |
| 9 | operationId | String | - | u_mes_prod_operation._id |
| 10 | operationName | String | - |  |
| 11 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 12 | workCenterName | String | - |  |
| 13 | equipmentId | String | - | u_mes_mast_equipment._id |
| 14 | equipmentName | String | - |  |
| 15 | operatorUserId | String | - | u_mes_mast_user._id |
| 16 | operatorUserName | String | - |  |
| 17 | completedAt | Date | Datetime |  |
| 18 | result | String | - |  |
| 19 | recipeId | String | - | u_mes_prod_recipe._id |
| 20 | recipeName | String | - |  |
| 21 | recipeVersion | String | - |  |
| 22 | recipeChecksum | String | - |  |
| 23 | schemaVersion | Int32 | - |  |
| 24 | createdAt | Date | Datetime |  |
| 25 | createdById | String | - | u_mes_mast_user._id |
| 26 | createdBy | String | - |  |
| 27 | updatedAt | Date | Datetime |  |
| 28 | updatedById | String | - | u_mes_mast_user._id |
| 29 | updatedBy | String | - |  |

## u_mes_trac_asBuiltRecordInspectionResult

Kind: relationship | Data class: transaction | Parent: u_mes_trac_asBuiltRecord | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | asBuiltRecordId | String | - | u_mes_trac_asBuiltRecord._id |
| 7 | asBuiltRecordName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | inspectionResultId | String | - | u_mes_qual_inspectionResult._id |
| 10 | inspectionResultName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_trac_traceInvestigation

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | title | String | - |  |
| 7 | direction | String | - |  |
| 8 | relatedCollectionName | String | - |  |
| 9 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 10 | relatedEntityName | String | - |  |
| 11 | depthLimit | Int32 | - |  |
| 12 | resultCount | Int32 | - |  |
| 13 | shippedCount | Int32 | - |  |
| 14 | qualityHoldId | String | - | u_mes_qual_qualityHold._id |
| 15 | qualityHoldName | String | - |  |
| 16 | nonconformanceId | String | - | u_mes_qual_nonconformance._id |
| 17 | nonconformanceName | String | - |  |
| 18 | customerComplaintId | String | - | u_mes_qual_customerComplaint._id |
| 19 | customerComplaintName | String | - |  |
| 20 | requestedById | String | - | u_mes_mast_user._id |
| 21 | requestedBy | String | - |  |
| 22 | requestedAt | Date | Datetime |  |
| 23 | completedAt | Date | Datetime |  |
| 24 | exportControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 25 | exportControlledDocumentName | String | - |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |
| 28 | createdAt | Date | Datetime |  |
| 29 | createdById | String | - | u_mes_mast_user._id |
| 30 | createdBy | String | - |  |
| 31 | updatedAt | Date | Datetime |  |
| 32 | updatedById | String | - | u_mes_mast_user._id |
| 33 | updatedBy | String | - |  |

## u_mes_trac_traceInvestigationResult

Kind: child | Data class: transaction | Parent: u_mes_trac_traceInvestigation | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | traceInvestigationId | String | - | u_mes_trac_traceInvestigation._id |
| 7 | traceInvestigationName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | relatedCollectionName | String | - |  |
| 10 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 11 | relatedEntityName | String | - |  |
| 12 | genealogyDepth | Int32 | - |  |
| 13 | itemId | String | - | u_mes_prod_item._id |
| 14 | itemName | String | - |  |
| 15 | statusAtRun | String | - |  |
| 16 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 17 | storageLocationName | String | - |  |
| 18 | shipmentId | String | - | u_mes_matl_shipment._id |
| 19 | shipmentName | String | - |  |
| 20 | customerId | String | - | u_mes_mast_customer._id |
| 21 | customerName | String | - |  |
| 22 | quantity | Decimal128 | - |  |
| 23 | schemaVersion | Int32 | - |  |
| 24 | createdAt | Date | Datetime |  |
| 25 | createdById | String | - | u_mes_mast_user._id |
| 26 | createdBy | String | - |  |
| 27 | updatedAt | Date | Datetime |  |
| 28 | updatedById | String | - | u_mes_mast_user._id |
| 29 | updatedBy | String | - |  |
