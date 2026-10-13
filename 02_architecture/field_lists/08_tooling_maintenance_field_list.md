# Field list - Tooling & Maintenance (maint)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/08_tooling_maintenance/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_maint_maintenancePlan

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | equipmentId | String | - | u_mes_mast_equipment._id |
| 7 | equipmentName | String | - |  |
| 8 | toolId | String | - | u_mes_maint_tool._id |
| 9 | toolName | String | - |  |
| 10 | planType | String | - |  |
| 11 | strategy | String | - |  |
| 12 | intervalType | String | - |  |
| 13 | intervalValue | Decimal128 | - |  |
| 14 | intervalUom | String | - |  |
| 15 | counterSource | String | - |  |
| 16 | estimatedMinutes | Int32 | - |  |
| 17 | lastDoneAt | Date | Datetime |  |
| 18 | nextDueAt | Date | Date |  |
| 19 | toleranceDays | Int32 | - |  |
| 20 | blockEquipmentWhenOverdue | Boolean | - |  |
| 21 | ownerDepartmentId | String | - | u_mes_mast_department._id |
| 22 | ownerDepartmentName | String | - |  |
| 23 | status | String | - |  |
| 24 | schemaVersion | Int32 | - |  |

## u_mes_maint_maintenancePlanTask

Kind: child | Data class: master | Parent: u_mes_maint_maintenancePlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | maintenancePlanId | String | - | u_mes_maint_maintenancePlan._id |
| 6 | maintenancePlanName | String | - |  |
| 7 | taskNo | Int32 | - |  |
| 8 | description | String | - |  |
| 9 | standardMinutes | Int32 | - |  |
| 10 | requiresShutdown | Boolean | - |  |
| 11 | acceptanceCriteria | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_maint_maintenancePlanRequiredSkill

Kind: relationship | Data class: master | Parent: u_mes_maint_maintenancePlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | maintenancePlanId | String | - | u_mes_maint_maintenancePlan._id |
| 6 | maintenancePlanName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | requiredSkillId | String | - | u_mes_mast_skill._id |
| 9 | requiredSkillName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_maint_maintenancePlanRequiredSparePart

Kind: child | Data class: master | Parent: u_mes_maint_maintenancePlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | maintenancePlanId | String | - | u_mes_maint_maintenancePlan._id |
| 6 | maintenancePlanName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | sparePartId | String | - | u_mes_maint_sparePart._id |
| 9 | sparePartName | String | - |  |
| 10 | quantity | Decimal128 | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_maint_maintenanceWorkOrder

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | title | String | - |  |
| 6 | workOrderType | String | - |  |
| 7 | equipmentId | String | - | u_mes_mast_equipment._id |
| 8 | equipmentName | String | - |  |
| 9 | toolId | String | - | u_mes_maint_tool._id |
| 10 | toolName | String | - |  |
| 11 | maintenancePlanId | String | - | u_mes_maint_maintenancePlan._id |
| 12 | maintenancePlanName | String | - |  |
| 13 | downtimeEventId | String | - | u_mes_perf_downtimeEvent._id |
| 14 | downtimeEventName | String | - |  |
| 15 | priority | String | - |  |
| 16 | reportedById | String | - | u_mes_mast_user._id |
| 17 | reportedBy | String | - |  |
| 18 | reportedAt | Date | Datetime |  |
| 19 | problemDescription | String | - |  |
| 20 | reasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 21 | reasonCodeName | String | - |  |
| 22 | failureMode | String | - |  |
| 23 | rootCause | String | - |  |
| 24 | actionTaken | String | - |  |
| 25 | plannedStartAt | Date | Datetime |  |
| 26 | startedAt | Date | Datetime |  |
| 27 | completedAt | Date | Datetime |  |
| 28 | downtimeMinutes | Int32 | - |  |
| 29 | responseMinutes | Int32 | - |  |
| 30 | repairMinutes | Int32 | - |  |
| 31 | totalCostInr | Decimal128 | - |  |
| 32 | equipmentReleasedById | String | - | u_mes_mast_user._id |
| 33 | equipmentReleasedBy | String | - |  |
| 34 | equipmentReleasedAt | Date | Datetime |  |
| 35 | followUpRequired | Boolean | - |  |
| 36 | shiftId | String | - | u_mes_mast_shift._id |
| 37 | shiftName | String | - |  |
| 38 | rootCauseCodeId | String | - | u_mes_perf_reasonCode._id |
| 39 | rootCauseCodeName | String | - |  |
| 40 | closureApprovedById | String | - | u_mes_mast_user._id |
| 41 | closureApprovedBy | String | - |  |
| 42 | closureApprovedAt | Date | Datetime |  |
| 43 | andonEventId | String | - | u_mes_plan_andonEvent._id |
| 44 | andonEventName | String | - |  |
| 45 | priorityScore | Decimal128 | - |  |
| 46 | schedulingSource | String | - |  |
| 47 | slaResponseDueAt | Date | Datetime |  |
| 48 | slaRepairDueAt | Date | Datetime |  |
| 49 | status | String | - |  |
| 50 | schemaVersion | Int32 | - |  |
| 51 | createdAt | Date | Datetime |  |
| 52 | createdById | String | - | u_mes_mast_user._id |
| 53 | createdBy | String | - |  |
| 54 | updatedAt | Date | Datetime |  |
| 55 | updatedById | String | - | u_mes_mast_user._id |
| 56 | updatedBy | String | - |  |

## u_mes_maint_maintenanceWorkOrderAssignedToUser

Kind: relationship | Data class: transaction | Parent: u_mes_maint_maintenanceWorkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 6 | maintenanceWorkOrderName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | assignedToUserId | String | - | u_mes_mast_user._id |
| 9 | assignedToUserName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
| 11 | createdAt | Date | Datetime |  |
| 12 | createdById | String | - | u_mes_mast_user._id |
| 13 | createdBy | String | - |  |
| 14 | updatedAt | Date | Datetime |  |
| 15 | updatedById | String | - | u_mes_mast_user._id |
| 16 | updatedBy | String | - |  |

## u_mes_maint_maintenanceWorkOrderLabour

Kind: child | Data class: transaction | Parent: u_mes_maint_maintenanceWorkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 6 | maintenanceWorkOrderName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | userId | String | - | u_mes_mast_user._id |
| 9 | userName | String | - |  |
| 10 | labourMinutes | Int32 | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_maint_maintenanceWorkOrderUsedSparePart

Kind: child | Data class: transaction | Parent: u_mes_maint_maintenanceWorkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 6 | maintenanceWorkOrderName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | sparePartId | String | - | u_mes_maint_sparePart._id |
| 9 | sparePartName | String | - |  |
| 10 | quantity | Decimal128 | - |  |
| 11 | costInr | Decimal128 | - |  |
| 12 | schemaVersion | Int32 | - |  |
| 13 | createdAt | Date | Datetime |  |
| 14 | createdById | String | - | u_mes_mast_user._id |
| 15 | createdBy | String | - |  |
| 16 | updatedAt | Date | Datetime |  |
| 17 | updatedById | String | - | u_mes_mast_user._id |
| 18 | updatedBy | String | - |  |

## u_mes_maint_sparePart

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | description | String | - |  |
| 6 | category | String | - |  |
| 7 | manufacturerId | String | - | u_mes_mast_manufacturer._id |
| 8 | manufacturerName | String | - |  |
| 9 | manufacturerPartNo | String | - |  |
| 10 | supplierId | String | - | u_mes_mast_supplier._id |
| 11 | supplierName | String | - |  |
| 12 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 13 | unitOfMeasureName | String | - |  |
| 14 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 15 | storageLocationName | String | - |  |
| 16 | stockQuantity | Decimal128 | - |  |
| 17 | minimumQuantity | Decimal128 | - |  |
| 18 | reorderQuantity | Decimal128 | - |  |
| 19 | leadTimeDays | Int32 | - |  |
| 20 | unitCostInr | Decimal128 | - |  |
| 21 | criticality | String | - |  |
| 22 | lastIssuedAt | Date | Datetime |  |
| 23 | lastReceivedAt | Date | Datetime |  |
| 24 | isInsuranceSpare | Boolean | - |  |
| 25 | status | String | - |  |
| 26 | schemaVersion | Int32 | - |  |

## u_mes_maint_sparePartUsedOnEquipment

Kind: relationship | Data class: master | Parent: u_mes_maint_sparePart | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | sparePartId | String | - | u_mes_maint_sparePart._id |
| 6 | sparePartName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | usedOnEquipmentId | String | - | u_mes_mast_equipment._id |
| 9 | usedOnEquipmentName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_maint_tool

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | toolTypeId | String | - | u_mes_maint_toolType._id |
| 7 | toolTypeName | String | - |  |
| 8 | toolClass | String | - |  |
| 9 | equipmentId | String | - | u_mes_mast_equipment._id |
| 10 | equipmentName | String | - |  |
| 11 | mountedPosition | String | - |  |
| 12 | supplierId | String | - | u_mes_mast_supplier._id |
| 13 | supplierName | String | - |  |
| 14 | drawingNo | String | - |  |
| 15 | serialNo | String | - |  |
| 16 | cavities | Int32 | - |  |
| 17 | lifeUom | String | - |  |
| 18 | lifeLimit | Int64 | - |  |
| 19 | lifeUsed | Int64 | - |  |
| 20 | lifeRemaining | Int64 | - |  |
| 21 | warningThresholdPct | Decimal128 | - |  |
| 22 | regrindCount | Int32 | - |  |
| 23 | maxRegrinds | Int32 | - |  |
| 24 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 25 | storageLocationName | String | - |  |
| 26 | lastMaintainedAt | Date | Datetime |  |
| 27 | nextMaintenanceDueAt | Date | Date |  |
| 28 | purchasedAt | Date | Datetime |  |
| 29 | costInr | Decimal128 | - |  |
| 30 | ownedByCustomerId | String | - | u_mes_mast_customer._id |
| 31 | ownedByCustomerName | String | - |  |
| 32 | blockAtLifeLimit | Boolean | - |  |
| 33 | lastCertifiedAt | Date | Datetime |  |
| 34 | certificationDueDate | Date | Date |  |
| 35 | certificateControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 36 | certificateControlledDocumentName | String | - |  |
| 37 | status | String | - |  |
| 38 | schemaVersion | Int32 | - |  |

## u_mes_maint_toolItem

Kind: relationship | Data class: master | Parent: u_mes_maint_tool | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | toolId | String | - | u_mes_maint_tool._id |
| 6 | toolName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_maint_toolLifeRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | toolId | String | - | u_mes_maint_tool._id |
| 6 | toolName | String | - |  |
| 7 | equipmentId | String | - | u_mes_mast_equipment._id |
| 8 | equipmentName | String | - |  |
| 9 | eventType | String | - |  |
| 10 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 11 | productionOrderName | String | - |  |
| 12 | eventAt | Date | Datetime |  |
| 13 | performedById | String | - | u_mes_mast_user._id |
| 14 | performedBy | String | - |  |
| 15 | cyclesThisEvent | Int64 | - |  |
| 16 | lifeUsedBefore | Int64 | - |  |
| 17 | lifeUsedAfter | Int64 | - |  |
| 18 | lifeRemaining | Int64 | - |  |
| 19 | regrindNo | Int32 | - |  |
| 20 | conditionOnRemoval | String | - |  |
| 21 | removalReason | String | - |  |
| 22 | measuredWearMm | Decimal128 | - |  |
| 23 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 24 | maintenanceWorkOrderName | String | - |  |
| 25 | remarks | String | - |  |
| 26 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 27 | workCenterName | String | - |  |
| 28 | itemId | String | - | u_mes_prod_item._id |
| 29 | itemName | String | - |  |
| 30 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 31 | operationExecutionName | String | - |  |
| 32 | status | String | - |  |
| 33 | schemaVersion | Int32 | - |  |
| 34 | createdAt | Date | Datetime |  |
| 35 | createdById | String | - | u_mes_mast_user._id |
| 36 | createdBy | String | - |  |
| 37 | updatedAt | Date | Datetime |  |
| 38 | updatedById | String | - | u_mes_mast_user._id |
| 39 | updatedBy | String | - |  |

## u_mes_maint_toolType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | lifeUom | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | status | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_maint_maintenanceWorkOrderTask

Kind: child | Data class: transaction | Parent: u_mes_maint_maintenanceWorkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 6 | maintenanceWorkOrderName | String | - |  |
| 7 | taskNo | Int32 | - |  |
| 8 | maintenancePlanTaskId | String | - | u_mes_maint_maintenancePlanTask._id |
| 9 | maintenancePlanTaskName | String | - |  |
| 10 | description | String | - |  |
| 11 | result | String | - |  |
| 12 | measuredValue | Decimal128 | - |  |
| 13 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 14 | unitOfMeasureName | String | - |  |
| 15 | comment | String | - |  |
| 16 | completedById | String | - | u_mes_mast_user._id |
| 17 | completedBy | String | - |  |
| 18 | completedAt | Date | Datetime |  |
| 19 | schemaVersion | Int32 | - |  |
| 20 | createdAt | Date | Datetime |  |
| 21 | createdById | String | - | u_mes_mast_user._id |
| 22 | createdBy | String | - |  |
| 23 | updatedAt | Date | Datetime |  |
| 24 | updatedById | String | - | u_mes_mast_user._id |
| 25 | updatedBy | String | - |  |

## u_mes_maint_sparePartTransaction

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | sparePartId | String | - | u_mes_maint_sparePart._id |
| 6 | sparePartName | String | - |  |
| 7 | transactionType | String | - |  |
| 8 | quantity | Decimal128 | - |  |
| 9 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 10 | unitOfMeasureName | String | - |  |
| 11 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 12 | maintenanceWorkOrderName | String | - |  |
| 13 | equipmentId | String | - | u_mes_mast_equipment._id |
| 14 | equipmentName | String | - |  |
| 15 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 16 | storageLocationName | String | - |  |
| 17 | scanVerified | Boolean | - |  |
| 18 | unitCostInr | Decimal128 | - |  |
| 19 | transactedAt | Date | Datetime |  |
| 20 | transactedById | String | - | u_mes_mast_user._id |
| 21 | transactedBy | String | - |  |
| 22 | erpDocumentNo | String | - |  |
| 23 | status | String | - |  |
| 24 | schemaVersion | Int32 | - |  |
| 25 | createdAt | Date | Datetime |  |
| 26 | createdById | String | - | u_mes_mast_user._id |
| 27 | createdBy | String | - |  |
| 28 | updatedAt | Date | Datetime |  |
| 29 | updatedById | String | - | u_mes_mast_user._id |
| 30 | updatedBy | String | - |  |

## u_mes_maint_reliabilitySummary

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
| 11 | periodType | String | - |  |
| 12 | periodStartAt | Date | Datetime |  |
| 13 | periodEndAt | Date | Datetime |  |
| 14 | operatingHours | Decimal128 | - |  |
| 15 | failureCount | Int32 | - |  |
| 16 | repairMinutes | Int32 | - |  |
| 17 | mtbfHours | Decimal128 | - |  |
| 18 | mttrMinutes | Decimal128 | - |  |
| 19 | availabilityPct | Decimal128 | - |  |
| 20 | calculatedAt | Date | Datetime |  |
| 21 | status | String | - |  |
| 22 | schemaVersion | Int32 | - |  |
| 23 | createdAt | Date | Datetime |  |
| 24 | createdById | String | - | u_mes_mast_user._id |
| 25 | createdBy | String | - |  |
| 26 | updatedAt | Date | Datetime |  |
| 27 | updatedById | String | - | u_mes_mast_user._id |
| 28 | updatedBy | String | - |  |

## u_mes_maint_equipmentLifecycleEvent

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | equipmentId | String | - | u_mes_mast_equipment._id |
| 6 | equipmentName | String | - |  |
| 7 | eventType | String | - |  |
| 8 | eventAt | Date | Datetime |  |
| 9 | description | String | - |  |
| 10 | costInr | Decimal128 | - |  |
| 11 | healthScore | Decimal128 | - |  |
| 12 | lifetimeCyclesAtEvent | Int64 | - |  |
| 13 | lifetimeRunHoursAtEvent | Decimal128 | - |  |
| 14 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 15 | maintenanceWorkOrderName | String | - |  |
| 16 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 17 | engineeringChangeName | String | - |  |
| 18 | modelPredictionId | String | - | u_mes_syst_modelPrediction._id |
| 19 | modelPredictionName | String | - |  |
| 20 | approvedById | String | - | u_mes_mast_user._id |
| 21 | approvedBy | String | - |  |
| 22 | approvedAt | Date | Datetime |  |
| 23 | status | String | - |  |
| 24 | schemaVersion | Int32 | - |  |
| 25 | createdAt | Date | Datetime |  |
| 26 | createdById | String | - | u_mes_mast_user._id |
| 27 | createdBy | String | - |  |
| 28 | updatedAt | Date | Datetime |  |
| 29 | updatedById | String | - | u_mes_mast_user._id |
| 30 | updatedBy | String | - |  |

## u_mes_maint_logbookEntry

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | relatedCollectionName | String | - |  |
| 6 | relatedEntityId | String | - | any collection, named in relatedCollectionName |
| 7 | relatedEntityName | String | - |  |
| 8 | activityType | String | - |  |
| 9 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 10 | productionOrderName | String | - |  |
| 11 | lotId | String | - | u_mes_plan_lot._id |
| 12 | lotName | String | - |  |
| 13 | cleaningRecordId | String | - | u_mes_maint_cleaningRecord._id |
| 14 | cleaningRecordName | String | - |  |
| 15 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 16 | maintenanceWorkOrderName | String | - |  |
| 17 | lineClearanceId | String | - | u_mes_plan_lineClearance._id |
| 18 | lineClearanceName | String | - |  |
| 19 | entryText | String | - |  |
| 20 | performedById | String | - | u_mes_mast_user._id |
| 21 | performedBy | String | - |  |
| 22 | startedAt | Date | Datetime |  |
| 23 | completedAt | Date | Datetime |  |
| 24 | reviewedById | String | - | u_mes_mast_user._id |
| 25 | reviewedBy | String | - |  |
| 26 | reviewedAt | Date | Datetime |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |
| 29 | createdAt | Date | Datetime |  |
| 30 | createdById | String | - | u_mes_mast_user._id |
| 31 | createdBy | String | - |  |
| 32 | updatedAt | Date | Datetime |  |
| 33 | updatedById | String | - | u_mes_mast_user._id |
| 34 | updatedBy | String | - |  |

## u_mes_maint_cleaningRecord

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
| 9 | cleaningType | String | - |  |
| 10 | procedureControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 11 | procedureControlledDocumentName | String | - |  |
| 12 | previousProductionOrderId | String | - | u_mes_plan_productionOrder._id |
| 13 | previousProductionOrderName | String | - |  |
| 14 | previousItemId | String | - | u_mes_prod_item._id |
| 15 | previousItemName | String | - |  |
| 16 | dirtyHoldStartAt | Date | Datetime |  |
| 17 | startedAt | Date | Datetime |  |
| 18 | completedAt | Date | Datetime |  |
| 19 | cleanedById | String | - | u_mes_mast_user._id |
| 20 | cleanedBy | String | - |  |
| 21 | verificationMethod | String | - |  |
| 22 | verificationResult | String | - |  |
| 23 | verifiedById | String | - | u_mes_mast_user._id |
| 24 | verifiedBy | String | - |  |
| 25 | verifiedAt | Date | Datetime |  |
| 26 | cleanHoldExpiresAt | Date | Datetime |  |
| 27 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 28 | electronicSignatureName | String | - |  |
| 29 | status | String | - |  |
| 30 | schemaVersion | Int32 | - |  |
| 31 | createdAt | Date | Datetime |  |
| 32 | createdById | String | - | u_mes_mast_user._id |
| 33 | createdBy | String | - |  |
| 34 | updatedAt | Date | Datetime |  |
| 35 | updatedById | String | - | u_mes_mast_user._id |
| 36 | updatedBy | String | - |  |

## u_mes_maint_equipmentQualification

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | equipmentId | String | - | u_mes_mast_equipment._id |
| 6 | equipmentName | String | - |  |
| 7 | qualificationPhase | String | - |  |
| 8 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 9 | engineeringChangeName | String | - |  |
| 10 | protocolControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 11 | protocolControlledDocumentName | String | - |  |
| 12 | reportControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 13 | reportControlledDocumentName | String | - |  |
| 14 | testCaseCount | Int32 | - |  |
| 15 | testFailedCount | Int32 | - |  |
| 16 | openDeviationCount | Int32 | - |  |
| 17 | executedById | String | - | u_mes_mast_user._id |
| 18 | executedBy | String | - |  |
| 19 | startedAt | Date | Datetime |  |
| 20 | completedAt | Date | Datetime |  |
| 21 | approvedById | String | - | u_mes_mast_user._id |
| 22 | approvedBy | String | - |  |
| 23 | approvedAt | Date | Datetime |  |
| 24 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 25 | electronicSignatureName | String | - |  |
| 26 | requalificationDueDate | Date | Date |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |
| 29 | createdAt | Date | Datetime |  |
| 30 | createdById | String | - | u_mes_mast_user._id |
| 31 | createdBy | String | - |  |
| 32 | updatedAt | Date | Datetime |  |
| 33 | updatedById | String | - | u_mes_mast_user._id |
| 34 | updatedBy | String | - |  |
