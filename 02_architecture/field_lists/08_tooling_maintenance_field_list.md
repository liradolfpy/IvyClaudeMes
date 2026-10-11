# Field list - Tooling & Maintenance (maint)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/08_tooling_maintenance/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_maint_maintenancePlan

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | equipmentId | String | u_mes_mast_equipment._id |
| 7 | equipmentName | String |  |
| 8 | toolId | String | u_mes_maint_tool._id |
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
| 21 | ownerDepartmentId | String | u_mes_mast_department._id |
| 22 | ownerDepartmentName | String |  |
| 23 | status | String |  |
| 24 | schemaVersion | Int32 |  |

## u_mes_maint_maintenancePlanTask

Kind: child | Data class: master | Parent: u_mes_maint_maintenancePlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | maintenancePlanId | String | u_mes_maint_maintenancePlan._id |
| 6 | maintenancePlanName | String |  |
| 7 | taskNo | Int32 |  |
| 8 | description | String |  |
| 9 | standardMinutes | Int32 |  |
| 10 | requiresShutdown | Boolean |  |
| 11 | acceptanceCriteria | String |  |
| 12 | schemaVersion | Int32 |  |

## u_mes_maint_maintenancePlanRequiredSkill

Kind: relationship | Data class: master | Parent: u_mes_maint_maintenancePlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | maintenancePlanId | String | u_mes_maint_maintenancePlan._id |
| 6 | maintenancePlanName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | requiredSkillId | String | u_mes_mast_skill._id |
| 9 | requiredSkillName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_maint_maintenancePlanRequiredSparePart

Kind: child | Data class: master | Parent: u_mes_maint_maintenancePlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | maintenancePlanId | String | u_mes_maint_maintenancePlan._id |
| 6 | maintenancePlanName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | sparePartId | String | u_mes_maint_sparePart._id |
| 9 | sparePartName | String |  |
| 10 | quantity | Decimal128 |  |
| 11 | schemaVersion | Int32 |  |

## u_mes_maint_maintenanceWorkOrder

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | title | String |  |
| 6 | workOrderType | String |  |
| 7 | equipmentId | String | u_mes_mast_equipment._id |
| 8 | equipmentName | String |  |
| 9 | toolId | String | u_mes_maint_tool._id |
| 10 | toolName | String |  |
| 11 | maintenancePlanId | String | u_mes_maint_maintenancePlan._id |
| 12 | maintenancePlanName | String |  |
| 13 | downtimeEventId | String | u_mes_perf_downtimeEvent._id |
| 14 | downtimeEventName | String |  |
| 15 | priority | String |  |
| 16 | reportedById | String | u_mes_mast_user._id |
| 17 | reportedBy | String |  |
| 18 | reportedAt | Date |  |
| 19 | problemDescription | String |  |
| 20 | reasonCodeId | String | u_mes_perf_reasonCode._id |
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
| 32 | equipmentReleasedById | String | u_mes_mast_user._id |
| 33 | equipmentReleasedBy | String |  |
| 34 | equipmentReleasedAt | Date |  |
| 35 | followUpRequired | Boolean |  |
| 36 | status | String |  |
| 37 | schemaVersion | Int32 |  |
| 38 | createdAt | Date |  |
| 39 | createdById | String | u_mes_mast_user._id |
| 40 | createdBy | String |  |
| 41 | updatedAt | Date |  |
| 42 | updatedById | String | u_mes_mast_user._id |
| 43 | updatedBy | String |  |

## u_mes_maint_maintenanceWorkOrderAssignedToUser

Kind: relationship | Data class: transaction | Parent: u_mes_maint_maintenanceWorkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | maintenanceWorkOrderId | String | u_mes_maint_maintenanceWorkOrder._id |
| 6 | maintenanceWorkOrderName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | assignedToUserId | String | u_mes_mast_user._id |
| 9 | assignedToUserName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mast_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mast_user._id |
| 16 | updatedBy | String |  |

## u_mes_maint_maintenanceWorkOrderLabour

Kind: child | Data class: transaction | Parent: u_mes_maint_maintenanceWorkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | maintenanceWorkOrderId | String | u_mes_maint_maintenanceWorkOrder._id |
| 6 | maintenanceWorkOrderName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | userId | String | u_mes_mast_user._id |
| 9 | userName | String |  |
| 10 | labourMinutes | Int32 |  |
| 11 | schemaVersion | Int32 |  |
| 12 | createdAt | Date |  |
| 13 | createdById | String | u_mes_mast_user._id |
| 14 | createdBy | String |  |
| 15 | updatedAt | Date |  |
| 16 | updatedById | String | u_mes_mast_user._id |
| 17 | updatedBy | String |  |

## u_mes_maint_maintenanceWorkOrderUsedSparePart

Kind: child | Data class: transaction | Parent: u_mes_maint_maintenanceWorkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | maintenanceWorkOrderId | String | u_mes_maint_maintenanceWorkOrder._id |
| 6 | maintenanceWorkOrderName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | sparePartId | String | u_mes_maint_sparePart._id |
| 9 | sparePartName | String |  |
| 10 | quantity | Decimal128 |  |
| 11 | costInr | Decimal128 |  |
| 12 | schemaVersion | Int32 |  |
| 13 | createdAt | Date |  |
| 14 | createdById | String | u_mes_mast_user._id |
| 15 | createdBy | String |  |
| 16 | updatedAt | Date |  |
| 17 | updatedById | String | u_mes_mast_user._id |
| 18 | updatedBy | String |  |

## u_mes_maint_sparePart

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | description | String |  |
| 6 | category | String |  |
| 7 | manufacturerId | String | u_mes_mast_manufacturer._id |
| 8 | manufacturerName | String |  |
| 9 | manufacturerPartNo | String |  |
| 10 | supplierId | String | u_mes_mast_supplier._id |
| 11 | supplierName | String |  |
| 12 | unitOfMeasureId | String | u_mes_mast_unitOfMeasure._id |
| 13 | unitOfMeasureName | String |  |
| 14 | storageLocationId | String | u_mes_matl_storageLocation._id |
| 15 | storageLocationName | String |  |
| 16 | stockQuantity | Decimal128 |  |
| 17 | minimumQuantity | Decimal128 |  |
| 18 | reorderQuantity | Decimal128 |  |
| 19 | leadTimeDays | Int32 |  |
| 20 | unitCostInr | Decimal128 |  |
| 21 | criticality | String |  |
| 22 | lastIssuedAt | Date |  |
| 23 | lastReceivedAt | Date |  |
| 24 | isInsuranceSpare | Boolean |  |
| 25 | status | String |  |
| 26 | schemaVersion | Int32 |  |

## u_mes_maint_sparePartUsedOnEquipment

Kind: relationship | Data class: master | Parent: u_mes_maint_sparePart | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | sparePartId | String | u_mes_maint_sparePart._id |
| 6 | sparePartName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | usedOnEquipmentId | String | u_mes_mast_equipment._id |
| 9 | usedOnEquipmentName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_maint_tool

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | toolTypeId | String | u_mes_maint_toolType._id |
| 7 | toolTypeName | String |  |
| 8 | toolClass | String |  |
| 9 | equipmentId | String | u_mes_mast_equipment._id |
| 10 | equipmentName | String |  |
| 11 | mountedPosition | String |  |
| 12 | supplierId | String | u_mes_mast_supplier._id |
| 13 | supplierName | String |  |
| 14 | drawingNo | String |  |
| 15 | serialNo | String |  |
| 16 | cavities | Int32 |  |
| 17 | lifeUom | String |  |
| 18 | lifeLimit | Int64 |  |
| 19 | lifeUsed | Int64 |  |
| 20 | lifeRemaining | Int64 |  |
| 21 | warningThresholdPct | Decimal128 |  |
| 22 | regrindCount | Int32 |  |
| 23 | maxRegrinds | Int32 |  |
| 24 | storageLocationId | String | u_mes_matl_storageLocation._id |
| 25 | storageLocationName | String |  |
| 26 | lastMaintainedAt | Date |  |
| 27 | nextMaintenanceDueAt | Date |  |
| 28 | purchasedAt | Date |  |
| 29 | costInr | Decimal128 |  |
| 30 | ownedByCustomerId | String | u_mes_mast_customer._id |
| 31 | ownedByCustomerName | String |  |
| 32 | status | String |  |
| 33 | schemaVersion | Int32 |  |

## u_mes_maint_toolItem

Kind: relationship | Data class: master | Parent: u_mes_maint_tool | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | toolId | String | u_mes_maint_tool._id |
| 6 | toolName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | itemId | String | u_mes_prod_item._id |
| 9 | itemName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_maint_toolLifeRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | toolId | String | u_mes_maint_tool._id |
| 6 | toolName | String |  |
| 7 | equipmentId | String | u_mes_mast_equipment._id |
| 8 | equipmentName | String |  |
| 9 | eventType | String |  |
| 10 | productionOrderId | String | u_mes_plan_productionOrder._id |
| 11 | productionOrderName | String |  |
| 12 | eventAt | Date |  |
| 13 | performedById | String | u_mes_mast_user._id |
| 14 | performedBy | String |  |
| 15 | cyclesThisEvent | Int64 |  |
| 16 | lifeUsedBefore | Int64 |  |
| 17 | lifeUsedAfter | Int64 |  |
| 18 | lifeRemaining | Int64 |  |
| 19 | regrindNo | Int32 |  |
| 20 | conditionOnRemoval | String |  |
| 21 | removalReason | String |  |
| 22 | measuredWearMm | Decimal128 |  |
| 23 | maintenanceWorkOrderId | String | u_mes_maint_maintenanceWorkOrder._id |
| 24 | maintenanceWorkOrderName | String |  |
| 25 | remarks | String |  |
| 26 | status | String |  |
| 27 | schemaVersion | Int32 |  |
| 28 | createdAt | Date |  |
| 29 | createdById | String | u_mes_mast_user._id |
| 30 | createdBy | String |  |
| 31 | updatedAt | Date |  |
| 32 | updatedById | String | u_mes_mast_user._id |
| 33 | updatedBy | String |  |

## u_mes_maint_toolType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | description | String |  |
| 7 | lifeUom | String |  |
| 8 | sequenceNo | Int32 |  |
| 9 | status | String |  |
| 10 | schemaVersion | Int32 |  |
