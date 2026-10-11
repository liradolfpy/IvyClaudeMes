# Field list - Maintenance and tooling (mnt)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/08_maintenance_tooling/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_mnt_maintenancePlan

Kind: entity | Data class: master | Parent: - | _id pattern: MP-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | equipmentId | String | u_mes_mdm_equipment._id |
| 7 | equipmentName | String |  |
| 8 | toolId | String | u_mes_mnt_tool._id |
| 9 | toolName | String |  |
| 10 | planType | String |  |
| 11 | strategy | String |  |
| 12 | intervalType | String |  |
| 13 | intervalValue | Decimal128 |  |
| 14 | intervalUom | String |  |
| 15 | counterSource | String |  |
| 16 | estimatedMinutes | Int32 |  |
| 17 | lastDoneAt | Date |  |
| 18 | nextDueAt | Date |  |
| 19 | toleranceDays | Int32 |  |
| 20 | blockEquipmentWhenOverdue | Boolean |  |
| 21 | ownerDepartment | String |  |
| 22 | status | String |  |
| 23 | schemaVersion | Int32 |  |

## u_mes_mnt_maintenancePlanTask

Kind: child | Data class: master | Parent: u_mes_mnt_maintenancePlan | _id pattern: <maintenancePlanId>-T<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | maintenancePlanId | String | u_mes_mnt_maintenancePlan._id |
| 6 | maintenancePlanName | String |  |
| 7 | taskNo | Int32 |  |
| 8 | description | String |  |
| 9 | standardMinutes | Int32 |  |
| 10 | requiresShutdown | Boolean |  |
| 11 | acceptanceCriteria | String |  |
| 12 | schemaVersion | Int32 |  |

## u_mes_mnt_maintenancePlanRequiredSkill

Kind: relationship | Data class: master | Parent: u_mes_mnt_maintenancePlan | _id pattern: <maintenancePlanId>-RS<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | maintenancePlanId | String | u_mes_mnt_maintenancePlan._id |
| 6 | maintenancePlanName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | requiredSkillId | String | u_mes_mdm_skill._id |
| 9 | requiredSkillName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mnt_maintenancePlanRequiredSparePart

Kind: child | Data class: master | Parent: u_mes_mnt_maintenancePlan | _id pattern: <maintenancePlanId>-RSP<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | maintenancePlanId | String | u_mes_mnt_maintenancePlan._id |
| 6 | maintenancePlanName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | sparePartId | String | u_mes_mnt_sparePart._id |
| 9 | sparePartName | String |  |
| 10 | quantity | Decimal128 |  |
| 11 | schemaVersion | Int32 |  |

## u_mes_mnt_maintenanceWorkOrder

Kind: entity | Data class: transaction | Parent: - | _id pattern: MWO-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | title | String |  |
| 6 | workOrderType | String |  |
| 7 | equipmentId | String | u_mes_mdm_equipment._id |
| 8 | equipmentName | String |  |
| 9 | toolId | String | u_mes_mnt_tool._id |
| 10 | toolName | String |  |
| 11 | maintenancePlanId | String | u_mes_mnt_maintenancePlan._id |
| 12 | maintenancePlanName | String |  |
| 13 | downtimeEventId | String | u_mes_eqp_downtimeEvent._id |
| 14 | downtimeEventName | String |  |
| 15 | priority | String |  |
| 16 | reportedById | String | u_mes_mdm_user._id |
| 17 | reportedBy | String |  |
| 18 | reportedAt | Date |  |
| 19 | problemDescription | String |  |
| 20 | reasonCodeId | String | u_mes_eqp_reasonCode._id |
| 21 | reasonCodeName | String |  |
| 22 | failureMode | String |  |
| 23 | rootCause | String |  |
| 24 | actionTaken | String |  |
| 25 | plannedStartAt | Date |  |
| 26 | startedAt | Date |  |
| 27 | completedAt | Date |  |
| 28 | downtimeMinutes | Int32 |  |
| 29 | responseMinutes | Int32 |  |
| 30 | repairMinutes | Int32 |  |
| 31 | totalCostInr | Decimal128 |  |
| 32 | equipmentReleasedById | String | u_mes_mdm_user._id |
| 33 | equipmentReleasedBy | String |  |
| 34 | equipmentReleasedAt | Date |  |
| 35 | followUpRequired | Boolean |  |
| 36 | status | String |  |
| 37 | schemaVersion | Int32 |  |
| 38 | createdAt | Date |  |
| 39 | createdById | String | u_mes_mdm_user._id |
| 40 | createdBy | String |  |
| 41 | updatedAt | Date |  |
| 42 | updatedById | String | u_mes_mdm_user._id |
| 43 | updatedBy | String |  |

## u_mes_mnt_maintenanceWorkOrderAssignedToUser

Kind: relationship | Data class: transaction | Parent: u_mes_mnt_maintenanceWorkOrder | _id pattern: <maintenanceWorkOrderId>-ATU<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | maintenanceWorkOrderId | String | u_mes_mnt_maintenanceWorkOrder._id |
| 6 | maintenanceWorkOrderName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | assignedToUserId | String | u_mes_mdm_user._id |
| 9 | assignedToUserName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_mnt_maintenanceWorkOrderLabour

Kind: child | Data class: transaction | Parent: u_mes_mnt_maintenanceWorkOrder | _id pattern: <maintenanceWorkOrderId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | maintenanceWorkOrderId | String | u_mes_mnt_maintenanceWorkOrder._id |
| 6 | maintenanceWorkOrderName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | userId | String | u_mes_mdm_user._id |
| 9 | userName | String |  |
| 10 | labourMinutes | Int32 |  |
| 11 | schemaVersion | Int32 |  |
| 12 | createdAt | Date |  |
| 13 | createdById | String | u_mes_mdm_user._id |
| 14 | createdBy | String |  |
| 15 | updatedAt | Date |  |
| 16 | updatedById | String | u_mes_mdm_user._id |
| 17 | updatedBy | String |  |

## u_mes_mnt_maintenanceWorkOrderUsedSparePart

Kind: child | Data class: transaction | Parent: u_mes_mnt_maintenanceWorkOrder | _id pattern: <maintenanceWorkOrderId>-USP<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | maintenanceWorkOrderId | String | u_mes_mnt_maintenanceWorkOrder._id |
| 6 | maintenanceWorkOrderName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | sparePartId | String | u_mes_mnt_sparePart._id |
| 9 | sparePartName | String |  |
| 10 | quantity | Decimal128 |  |
| 11 | costInr | Decimal128 |  |
| 12 | schemaVersion | Int32 |  |
| 13 | createdAt | Date |  |
| 14 | createdById | String | u_mes_mdm_user._id |
| 15 | createdBy | String |  |
| 16 | updatedAt | Date |  |
| 17 | updatedById | String | u_mes_mdm_user._id |
| 18 | updatedBy | String |  |

## u_mes_mnt_sparePart

Kind: entity | Data class: master | Parent: - | _id pattern: SPR-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | description | String |  |
| 6 | category | String |  |
| 7 | manufacturer | String |  |
| 8 | manufacturerPartNo | String |  |
| 9 | supplierId | String | u_mes_mdm_supplier._id |
| 10 | supplierName | String |  |
| 11 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 12 | unitOfMeasureName | String |  |
| 13 | storageLocationId | String | u_mes_mat_storageLocation._id |
| 14 | storageLocationName | String |  |
| 15 | stockQuantity | Decimal128 |  |
| 16 | minimumQuantity | Decimal128 |  |
| 17 | reorderQuantity | Decimal128 |  |
| 18 | leadTimeDays | Int32 |  |
| 19 | unitCostInr | Decimal128 |  |
| 20 | criticality | String |  |
| 21 | lastIssuedAt | Date |  |
| 22 | lastReceivedAt | Date |  |
| 23 | isInsuranceSpare | Boolean |  |
| 24 | status | String |  |
| 25 | schemaVersion | Int32 |  |

## u_mes_mnt_sparePartUsedOnEquipment

Kind: relationship | Data class: master | Parent: u_mes_mnt_sparePart | _id pattern: <sparePartId>-UOE<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | sparePartId | String | u_mes_mnt_sparePart._id |
| 6 | sparePartName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | usedOnEquipmentId | String | u_mes_mdm_equipment._id |
| 9 | usedOnEquipmentName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mnt_tool

Kind: entity | Data class: master | Parent: - | _id pattern: TL-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | toolType | String |  |
| 7 | toolClass | String |  |
| 8 | equipmentId | String | u_mes_mdm_equipment._id |
| 9 | equipmentName | String |  |
| 10 | mountedPosition | String |  |
| 11 | supplierId | String | u_mes_mdm_supplier._id |
| 12 | supplierName | String |  |
| 13 | drawingNo | String |  |
| 14 | serialNo | String |  |
| 15 | cavities | Int32 |  |
| 16 | lifeUom | String |  |
| 17 | lifeLimit | Int64 |  |
| 18 | lifeUsed | Int64 |  |
| 19 | lifeRemaining | Int64 |  |
| 20 | warningThresholdPct | Decimal128 |  |
| 21 | regrindCount | Int32 |  |
| 22 | maxRegrinds | Int32 |  |
| 23 | storageLocationId | String | u_mes_mat_storageLocation._id |
| 24 | storageLocationName | String |  |
| 25 | lastMaintainedAt | Date |  |
| 26 | nextMaintenanceDueAt | Date |  |
| 27 | purchasedAt | Date |  |
| 28 | costInr | Decimal128 |  |
| 29 | ownedByCustomerId | String | u_mes_mdm_customer._id |
| 30 | ownedByCustomerName | String |  |
| 31 | status | String |  |
| 32 | schemaVersion | Int32 |  |

## u_mes_mnt_toolItem

Kind: relationship | Data class: master | Parent: u_mes_mnt_tool | _id pattern: <toolId>-I<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | toolId | String | u_mes_mnt_tool._id |
| 6 | toolName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | itemId | String | u_mes_prd_item._id |
| 9 | itemName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mnt_toolLifeRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: TLR-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | toolId | String | u_mes_mnt_tool._id |
| 6 | toolName | String |  |
| 7 | equipmentId | String | u_mes_mdm_equipment._id |
| 8 | equipmentName | String |  |
| 9 | eventType | String |  |
| 10 | productionOrderId | String | u_mes_exe_productionOrder._id |
| 11 | productionOrderName | String |  |
| 12 | eventAt | Date |  |
| 13 | performedById | String | u_mes_mdm_user._id |
| 14 | performedBy | String |  |
| 15 | cyclesThisEvent | Int64 |  |
| 16 | lifeUsedBefore | Int64 |  |
| 17 | lifeUsedAfter | Int64 |  |
| 18 | lifeRemaining | Int64 |  |
| 19 | regrindNo | Int32 |  |
| 20 | conditionOnRemoval | String |  |
| 21 | removalReason | String |  |
| 22 | measuredWearMm | Decimal128 |  |
| 23 | maintenanceWorkOrderId | String | u_mes_mnt_maintenanceWorkOrder._id |
| 24 | maintenanceWorkOrderName | String |  |
| 25 | remarks | String |  |
| 26 | status | String |  |
| 27 | schemaVersion | Int32 |  |
| 28 | createdAt | Date |  |
| 29 | createdById | String | u_mes_mdm_user._id |
| 30 | createdBy | String |  |
| 31 | updatedAt | Date |  |
| 32 | updatedById | String | u_mes_mdm_user._id |
| 33 | updatedBy | String |  |
