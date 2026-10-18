# Field list - ToolingAndMaintenance (maint)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/08_tooling_maintenance/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = n.nn (plain number, no NumberDecimal()); Double = Double(n); Boolean = true / false.

## u_mes_maint_maintenancePlan

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | equipmentId | String | - | u_mes_mast_equipment._id |
| 8 | equipmentName | String | - |  |
| 9 | toolId | String | - | u_mes_maint_tool._id |
| 10 | toolName | String | - |  |
| 11 | planType | String | - |  |
| 12 | strategy | String | - |  |
| 13 | intervalType | String | - |  |
| 14 | intervalValue | Decimal128 | - |  |
| 15 | intervalUom | String | - |  |
| 16 | counterSource | String | - |  |
| 17 | estimatedMinutes | Int32 | - |  |
| 18 | lastDoneAt | Date | Datetime |  |
| 19 | nextDueAt | Date | Date |  |
| 20 | toleranceDays | Int32 | - |  |
| 21 | blockEquipmentWhenOverdue | Boolean | - |  |
| 22 | ownerDepartmentId | String | - | u_mes_mast_department._id |
| 23 | ownerDepartmentName | String | - |  |
| 24 | status | String | - |  |
| 25 | schemaVersion | Int32 | - |  |

## u_mes_maint_maintenancePlanTask

Kind: child | Data class: master | Parent: u_mes_maint_maintenancePlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | maintenancePlanId | String | - | u_mes_maint_maintenancePlan._id |
| 7 | maintenancePlanName | String | - |  |
| 8 | taskNo | Int32 | - |  |
| 9 | description | String | - |  |
| 10 | standardMinutes | Int32 | - |  |
| 11 | requiresShutdown | Boolean | - |  |
| 12 | acceptanceCriteria | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_maint_maintenancePlanRequiredSkill

Kind: relationship | Data class: master | Parent: u_mes_maint_maintenancePlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | maintenancePlanId | String | - | u_mes_maint_maintenancePlan._id |
| 7 | maintenancePlanName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | requiredSkillId | String | - | u_mes_mast_skill._id |
| 10 | requiredSkillName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_maint_maintenancePlanRequiredSparePart

Kind: child | Data class: master | Parent: u_mes_maint_maintenancePlan | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | maintenancePlanId | String | - | u_mes_maint_maintenancePlan._id |
| 7 | maintenancePlanName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | sparePartId | String | - | u_mes_maint_sparePart._id |
| 10 | sparePartName | String | - |  |
| 11 | quantity | Decimal128 | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_maint_maintenanceWorkOrder

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | title | String | - |  |
| 7 | workOrderType | String | - |  |
| 8 | equipmentId | String | - | u_mes_mast_equipment._id |
| 9 | equipmentName | String | - |  |
| 10 | toolId | String | - | u_mes_maint_tool._id |
| 11 | toolName | String | - |  |
| 12 | maintenancePlanId | String | - | u_mes_maint_maintenancePlan._id |
| 13 | maintenancePlanName | String | - |  |
| 14 | downtimeEventId | String | - | u_mes_perf_downtimeEvent._id |
| 15 | downtimeEventName | String | - |  |
| 16 | priority | String | - |  |
| 17 | reportedById | String | - | u_mes_mast_user._id |
| 18 | reportedBy | String | - |  |
| 19 | reportedAt | Date | Datetime |  |
| 20 | problemDescription | String | - |  |
| 21 | reasonCodeId | String | - | u_mes_perf_reasonCode._id |
| 22 | reasonCodeName | String | - |  |
| 23 | failureMode | String | - |  |
| 24 | rootCause | String | - |  |
| 25 | actionTaken | String | - |  |
| 26 | plannedStartAt | Date | Datetime |  |
| 27 | startedAt | Date | Datetime |  |
| 28 | completedAt | Date | Datetime |  |
| 29 | downtimeMinutes | Int32 | - |  |
| 30 | responseMinutes | Int32 | - |  |
| 31 | repairMinutes | Int32 | - |  |
| 32 | totalCostInr | Decimal128 | - |  |
| 33 | equipmentReleasedById | String | - | u_mes_mast_user._id |
| 34 | equipmentReleasedBy | String | - |  |
| 35 | equipmentReleasedAt | Date | Datetime |  |
| 36 | followUpRequired | Boolean | - |  |
| 37 | shiftId | String | - | u_mes_mast_shift._id |
| 38 | shiftName | String | - |  |
| 39 | rootCauseCodeId | String | - | u_mes_perf_reasonCode._id |
| 40 | rootCauseCodeName | String | - |  |
| 41 | closureApprovedById | String | - | u_mes_mast_user._id |
| 42 | closureApprovedBy | String | - |  |
| 43 | closureApprovedAt | Date | Datetime |  |
| 44 | andonEventId | String | - | u_mes_plan_andonEvent._id |
| 45 | andonEventName | String | - |  |
| 46 | priorityScore | Decimal128 | - |  |
| 47 | schedulingSource | String | - |  |
| 48 | slaResponseDueAt | Date | Datetime |  |
| 49 | slaRepairDueAt | Date | Datetime |  |
| 50 | status | String | - |  |
| 51 | schemaVersion | Int32 | - |  |
| 52 | createdAt | Date | Datetime |  |
| 53 | createdById | String | - | u_mes_mast_user._id |
| 54 | createdBy | String | - |  |
| 55 | updatedAt | Date | Datetime |  |
| 56 | updatedById | String | - | u_mes_mast_user._id |
| 57 | updatedBy | String | - |  |

## u_mes_maint_maintenanceWorkOrderAssignedToUser

Kind: relationship | Data class: transaction | Parent: u_mes_maint_maintenanceWorkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 7 | maintenanceWorkOrderName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | assignedToUserId | String | - | u_mes_mast_user._id |
| 10 | assignedToUserName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_maint_maintenanceWorkOrderLabour

Kind: child | Data class: transaction | Parent: u_mes_maint_maintenanceWorkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 7 | maintenanceWorkOrderName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | userId | String | - | u_mes_mast_user._id |
| 10 | userName | String | - |  |
| 11 | labourMinutes | Int32 | - |  |
| 12 | schemaVersion | Int32 | - |  |
| 13 | createdAt | Date | Datetime |  |
| 14 | createdById | String | - | u_mes_mast_user._id |
| 15 | createdBy | String | - |  |
| 16 | updatedAt | Date | Datetime |  |
| 17 | updatedById | String | - | u_mes_mast_user._id |
| 18 | updatedBy | String | - |  |

## u_mes_maint_maintenanceWorkOrderUsedSparePart

Kind: child | Data class: transaction | Parent: u_mes_maint_maintenanceWorkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 7 | maintenanceWorkOrderName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | sparePartId | String | - | u_mes_maint_sparePart._id |
| 10 | sparePartName | String | - |  |
| 11 | quantity | Decimal128 | - |  |
| 12 | costInr | Decimal128 | - |  |
| 13 | schemaVersion | Int32 | - |  |
| 14 | createdAt | Date | Datetime |  |
| 15 | createdById | String | - | u_mes_mast_user._id |
| 16 | createdBy | String | - |  |
| 17 | updatedAt | Date | Datetime |  |
| 18 | updatedById | String | - | u_mes_mast_user._id |
| 19 | updatedBy | String | - |  |

## u_mes_maint_sparePart

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | description | String | - |  |
| 7 | category | String | - |  |
| 8 | manufacturerId | String | - | u_mes_mast_manufacturer._id |
| 9 | manufacturerName | String | - |  |
| 10 | manufacturerPartNo | String | - |  |
| 11 | supplierId | String | - | u_mes_mast_supplier._id |
| 12 | supplierName | String | - |  |
| 13 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 14 | unitOfMeasureName | String | - |  |
| 15 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 16 | storageLocationName | String | - |  |
| 17 | stockQuantity | Decimal128 | - |  |
| 18 | minimumQuantity | Decimal128 | - |  |
| 19 | reorderQuantity | Decimal128 | - |  |
| 20 | leadTimeDays | Int32 | - |  |
| 21 | unitCostInr | Decimal128 | - |  |
| 22 | criticality | String | - |  |
| 23 | lastIssuedAt | Date | Datetime |  |
| 24 | lastReceivedAt | Date | Datetime |  |
| 25 | isInsuranceSpare | Boolean | - |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |

## u_mes_maint_sparePartUsedOnEquipment

Kind: relationship | Data class: master | Parent: u_mes_maint_sparePart | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | sparePartId | String | - | u_mes_maint_sparePart._id |
| 7 | sparePartName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | usedOnEquipmentId | String | - | u_mes_mast_equipment._id |
| 10 | usedOnEquipmentName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_maint_tool

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | toolTypeId | String | - | u_mes_maint_toolType._id |
| 8 | toolTypeName | String | - |  |
| 9 | toolClass | String | - |  |
| 10 | equipmentId | String | - | u_mes_mast_equipment._id |
| 11 | equipmentName | String | - |  |
| 12 | mountedPosition | String | - |  |
| 13 | supplierId | String | - | u_mes_mast_supplier._id |
| 14 | supplierName | String | - |  |
| 15 | drawingNo | String | - |  |
| 16 | serialNo | String | - |  |
| 17 | cavities | Int32 | - |  |
| 18 | lifeUom | String | - |  |
| 19 | lifeLimit | Int64 | - |  |
| 20 | lifeUsed | Int64 | - |  |
| 21 | lifeRemaining | Int64 | - |  |
| 22 | warningThresholdPct | Decimal128 | - |  |
| 23 | regrindCount | Int32 | - |  |
| 24 | maxRegrinds | Int32 | - |  |
| 25 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 26 | storageLocationName | String | - |  |
| 27 | lastMaintainedAt | Date | Datetime |  |
| 28 | nextMaintenanceDueAt | Date | Date |  |
| 29 | purchasedAt | Date | Datetime |  |
| 30 | costInr | Decimal128 | - |  |
| 31 | ownedByCustomerId | String | - | u_mes_mast_customer._id |
| 32 | ownedByCustomerName | String | - |  |
| 33 | blockAtLifeLimit | Boolean | - |  |
| 34 | lastCertifiedAt | Date | Datetime |  |
| 35 | certificationDueDate | Date | Date |  |
| 36 | certificateControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 37 | certificateControlledDocumentName | String | - |  |
| 38 | status | String | - |  |
| 39 | schemaVersion | Int32 | - |  |

## u_mes_maint_toolItem

Kind: relationship | Data class: master | Parent: u_mes_maint_tool | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | toolId | String | - | u_mes_maint_tool._id |
| 7 | toolName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_maint_toolLifeRecord

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | toolId | String | - | u_mes_maint_tool._id |
| 7 | toolName | String | - |  |
| 8 | equipmentId | String | - | u_mes_mast_equipment._id |
| 9 | equipmentName | String | - |  |
| 10 | eventType | String | - |  |
| 11 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 12 | productionOrderName | String | - |  |
| 13 | eventAt | Date | Datetime |  |
| 14 | performedById | String | - | u_mes_mast_user._id |
| 15 | performedBy | String | - |  |
| 16 | cyclesThisEvent | Int64 | - |  |
| 17 | lifeUsedBefore | Int64 | - |  |
| 18 | lifeUsedAfter | Int64 | - |  |
| 19 | lifeRemaining | Int64 | - |  |
| 20 | regrindNo | Int32 | - |  |
| 21 | conditionOnRemoval | String | - |  |
| 22 | removalReason | String | - |  |
| 23 | measuredWearMm | Decimal128 | - |  |
| 24 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 25 | maintenanceWorkOrderName | String | - |  |
| 26 | remarks | String | - |  |
| 27 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 28 | workCenterName | String | - |  |
| 29 | itemId | String | - | u_mes_prod_item._id |
| 30 | itemName | String | - |  |
| 31 | operationExecutionId | String | - | u_mes_plan_operationExecution._id |
| 32 | operationExecutionName | String | - |  |
| 33 | status | String | - |  |
| 34 | schemaVersion | Int32 | - |  |
| 35 | createdAt | Date | Datetime |  |
| 36 | createdById | String | - | u_mes_mast_user._id |
| 37 | createdBy | String | - |  |
| 38 | updatedAt | Date | Datetime |  |
| 39 | updatedById | String | - | u_mes_mast_user._id |
| 40 | updatedBy | String | - |  |

## u_mes_maint_toolType

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
| 8 | lifeUom | String | - |  |
| 9 | sequenceNo | Int32 | - |  |
| 10 | status | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_maint_maintenanceWorkOrderTask

Kind: child | Data class: transaction | Parent: u_mes_maint_maintenanceWorkOrder | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 7 | maintenanceWorkOrderName | String | - |  |
| 8 | taskNo | Int32 | - |  |
| 9 | maintenancePlanTaskId | String | - | u_mes_maint_maintenancePlanTask._id |
| 10 | maintenancePlanTaskName | String | - |  |
| 11 | description | String | - |  |
| 12 | result | String | - |  |
| 13 | measuredValue | Decimal128 | - |  |
| 14 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 15 | unitOfMeasureName | String | - |  |
| 16 | comment | String | - |  |
| 17 | completedById | String | - | u_mes_mast_user._id |
| 18 | completedBy | String | - |  |
| 19 | completedAt | Date | Datetime |  |
| 20 | schemaVersion | Int32 | - |  |
| 21 | createdAt | Date | Datetime |  |
| 22 | createdById | String | - | u_mes_mast_user._id |
| 23 | createdBy | String | - |  |
| 24 | updatedAt | Date | Datetime |  |
| 25 | updatedById | String | - | u_mes_mast_user._id |
| 26 | updatedBy | String | - |  |

## u_mes_maint_sparePartTransaction

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | sparePartId | String | - | u_mes_maint_sparePart._id |
| 7 | sparePartName | String | - |  |
| 8 | transactionType | String | - |  |
| 9 | quantity | Decimal128 | - |  |
| 10 | unitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 11 | unitOfMeasureName | String | - |  |
| 12 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 13 | maintenanceWorkOrderName | String | - |  |
| 14 | equipmentId | String | - | u_mes_mast_equipment._id |
| 15 | equipmentName | String | - |  |
| 16 | storageLocationId | String | - | u_mes_matl_storageLocation._id |
| 17 | storageLocationName | String | - |  |
| 18 | scanVerified | Boolean | - |  |
| 19 | unitCostInr | Decimal128 | - |  |
| 20 | transactedAt | Date | Datetime |  |
| 21 | transactedById | String | - | u_mes_mast_user._id |
| 22 | transactedBy | String | - |  |
| 23 | erpDocumentNo | String | - |  |
| 24 | status | String | - |  |
| 25 | schemaVersion | Int32 | - |  |
| 26 | createdAt | Date | Datetime |  |
| 27 | createdById | String | - | u_mes_mast_user._id |
| 28 | createdBy | String | - |  |
| 29 | updatedAt | Date | Datetime |  |
| 30 | updatedById | String | - | u_mes_mast_user._id |
| 31 | updatedBy | String | - |  |

## u_mes_maint_reliabilitySummary

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
| 12 | periodType | String | - |  |
| 13 | periodStartAt | Date | Datetime |  |
| 14 | periodEndAt | Date | Datetime |  |
| 15 | operatingHours | Decimal128 | - |  |
| 16 | failureCount | Int32 | - |  |
| 17 | repairMinutes | Int32 | - |  |
| 18 | mtbfHours | Decimal128 | - |  |
| 19 | mttrMinutes | Decimal128 | - |  |
| 20 | availabilityPct | Decimal128 | - |  |
| 21 | calculatedAt | Date | Datetime |  |
| 22 | status | String | - |  |
| 23 | schemaVersion | Int32 | - |  |
| 24 | createdAt | Date | Datetime |  |
| 25 | createdById | String | - | u_mes_mast_user._id |
| 26 | createdBy | String | - |  |
| 27 | updatedAt | Date | Datetime |  |
| 28 | updatedById | String | - | u_mes_mast_user._id |
| 29 | updatedBy | String | - |  |

## u_mes_maint_equipmentLifecycleEvent

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
| 8 | eventType | String | - |  |
| 9 | eventAt | Date | Datetime |  |
| 10 | description | String | - |  |
| 11 | costInr | Decimal128 | - |  |
| 12 | healthScore | Decimal128 | - |  |
| 13 | lifetimeCyclesAtEvent | Int64 | - |  |
| 14 | lifetimeRunHoursAtEvent | Decimal128 | - |  |
| 15 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 16 | maintenanceWorkOrderName | String | - |  |
| 17 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 18 | engineeringChangeName | String | - |  |
| 19 | modelPredictionId | String | - | u_mes_syst_modelPrediction._id |
| 20 | modelPredictionName | String | - |  |
| 21 | approvedById | String | - | u_mes_mast_user._id |
| 22 | approvedBy | String | - |  |
| 23 | approvedAt | Date | Datetime |  |
| 24 | status | String | - |  |
| 25 | schemaVersion | Int32 | - |  |
| 26 | createdAt | Date | Datetime |  |
| 27 | createdById | String | - | u_mes_mast_user._id |
| 28 | createdBy | String | - |  |
| 29 | updatedAt | Date | Datetime |  |
| 30 | updatedById | String | - | u_mes_mast_user._id |
| 31 | updatedBy | String | - |  |

## u_mes_maint_logbookEntry

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
| 9 | activityType | String | - |  |
| 10 | productionOrderId | String | - | u_mes_plan_productionOrder._id |
| 11 | productionOrderName | String | - |  |
| 12 | lotId | String | - | u_mes_plan_lot._id |
| 13 | lotName | String | - |  |
| 14 | cleaningRecordId | String | - | u_mes_maint_cleaningRecord._id |
| 15 | cleaningRecordName | String | - |  |
| 16 | maintenanceWorkOrderId | String | - | u_mes_maint_maintenanceWorkOrder._id |
| 17 | maintenanceWorkOrderName | String | - |  |
| 18 | lineClearanceId | String | - | u_mes_plan_lineClearance._id |
| 19 | lineClearanceName | String | - |  |
| 20 | entryText | String | - |  |
| 21 | performedById | String | - | u_mes_mast_user._id |
| 22 | performedBy | String | - |  |
| 23 | startedAt | Date | Datetime |  |
| 24 | completedAt | Date | Datetime |  |
| 25 | reviewedById | String | - | u_mes_mast_user._id |
| 26 | reviewedBy | String | - |  |
| 27 | reviewedAt | Date | Datetime |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |
| 30 | createdAt | Date | Datetime |  |
| 31 | createdById | String | - | u_mes_mast_user._id |
| 32 | createdBy | String | - |  |
| 33 | updatedAt | Date | Datetime |  |
| 34 | updatedById | String | - | u_mes_mast_user._id |
| 35 | updatedBy | String | - |  |

## u_mes_maint_cleaningRecord

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
| 10 | cleaningType | String | - |  |
| 11 | procedureControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 12 | procedureControlledDocumentName | String | - |  |
| 13 | previousProductionOrderId | String | - | u_mes_plan_productionOrder._id |
| 14 | previousProductionOrderName | String | - |  |
| 15 | previousItemId | String | - | u_mes_prod_item._id |
| 16 | previousItemName | String | - |  |
| 17 | dirtyHoldStartAt | Date | Datetime |  |
| 18 | startedAt | Date | Datetime |  |
| 19 | completedAt | Date | Datetime |  |
| 20 | cleanedById | String | - | u_mes_mast_user._id |
| 21 | cleanedBy | String | - |  |
| 22 | verificationMethod | String | - |  |
| 23 | verificationResult | String | - |  |
| 24 | verifiedById | String | - | u_mes_mast_user._id |
| 25 | verifiedBy | String | - |  |
| 26 | verifiedAt | Date | Datetime |  |
| 27 | cleanHoldExpiresAt | Date | Datetime |  |
| 28 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 29 | electronicSignatureName | String | - |  |
| 30 | status | String | - |  |
| 31 | schemaVersion | Int32 | - |  |
| 32 | createdAt | Date | Datetime |  |
| 33 | createdById | String | - | u_mes_mast_user._id |
| 34 | createdBy | String | - |  |
| 35 | updatedAt | Date | Datetime |  |
| 36 | updatedById | String | - | u_mes_mast_user._id |
| 37 | updatedBy | String | - |  |

## u_mes_maint_equipmentQualification

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
| 8 | qualificationPhase | String | - |  |
| 9 | engineeringChangeId | String | - | u_mes_prod_engineeringChange._id |
| 10 | engineeringChangeName | String | - |  |
| 11 | protocolControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 12 | protocolControlledDocumentName | String | - |  |
| 13 | reportControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 14 | reportControlledDocumentName | String | - |  |
| 15 | testCaseCount | Int32 | - |  |
| 16 | testFailedCount | Int32 | - |  |
| 17 | openDeviationCount | Int32 | - |  |
| 18 | executedById | String | - | u_mes_mast_user._id |
| 19 | executedBy | String | - |  |
| 20 | startedAt | Date | Datetime |  |
| 21 | completedAt | Date | Datetime |  |
| 22 | approvedById | String | - | u_mes_mast_user._id |
| 23 | approvedBy | String | - |  |
| 24 | approvedAt | Date | Datetime |  |
| 25 | electronicSignatureId | String | - | u_mes_syst_electronicSignature._id |
| 26 | electronicSignatureName | String | - |  |
| 27 | requalificationDueDate | Date | Date |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |
| 30 | createdAt | Date | Datetime |  |
| 31 | createdById | String | - | u_mes_mast_user._id |
| 32 | createdBy | String | - |  |
| 33 | updatedAt | Date | Datetime |  |
| 34 | updatedById | String | - | u_mes_mast_user._id |
| 35 | updatedBy | String | - |  |
