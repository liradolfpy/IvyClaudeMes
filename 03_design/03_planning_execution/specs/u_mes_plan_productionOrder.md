# u_mes_plan_productionOrder

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Shop orders from ERP: item, quantity, routing/BOM version, partial releases, status |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 47 (35 required, 12 may be null) |
| Estimated volume per year | 8,000-15,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per production order, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with productionOrderId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_plan_productionOrderRelease | Child | release |
| u_mes_plan_productionOrderLot | Relationship | lot |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1083000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PO-1000412"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | erpOrderNo | String | - | Yes | ERP order number | `"000100041200"` |  |
| 6 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 7 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 8 | itemRevision | String | - | Yes | Item revision | `"D"` |  |
| 9 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000001"` | Reference: u_mes_prod_productVariant._id |
| 10 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper LH, Standard"` |  |
| 11 | billOfMaterialId | String | - | Yes | Reference to u_mes_prod_billOfMaterial._id | `"1047000000000001"` | Reference: u_mes_prod_billOfMaterial._id |
| 12 | billOfMaterialName | String | - | Yes | Display value of billOfMaterialId, copied from u_mes_prod_billOfMaterial.recordNo | `"BOM-5110-10-0100-01"` |  |
| 13 | routingId | String | - | Yes | Reference to u_mes_prod_routing._id | `"1053000000000001"` | Reference: u_mes_prod_routing._id |
| 14 | routingName | String | - | Yes | Display value of routingId, copied from u_mes_prod_routing.description | `"Front caliper LH, full process routing"` |  |
| 15 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000006"` | Reference: u_mes_mast_line._id |
| 16 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Front Caliper Assembly Line 1"` |  |
| 17 | customerScheduleId | String | - | No (null allowed) | Reference to u_mes_plan_customerSchedule._id | `null` | Reference: u_mes_plan_customerSchedule._id |
| 18 | customerScheduleName | String | - | No (null allowed) | Display value of customerScheduleId, copied from u_mes_plan_customerSchedule.recordNo | `null` |  |
| 19 | orderType | String | - | Yes | Order type | `"Production"` | Production; Rework; Trial; PPAP Run |
| 20 | priority | String | - | Yes | Priority of the production order | `"Normal"` | Low; Normal; High; Urgent |
| 21 | plannedQuantity | Int32 | - | Yes | Planned quantity | `NumberInt(480)` |  |
| 22 | releasedQuantity | Int32 | - | Yes | Released quantity | `NumberInt(480)` |  |
| 23 | startedQuantity | Int32 | - | Yes | Started quantity | `NumberInt(480)` |  |
| 24 | goodQuantity | Int32 | - | Yes | Good quantity | `NumberInt(474)` |  |
| 25 | scrapQuantity | Int32 | - | Yes | Scrap quantity | `NumberInt(2)` |  |
| 26 | reworkQuantity | Int32 | - | Yes | Rework quantity | `NumberInt(4)` |  |
| 27 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 28 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 29 | plannedStartAt | Date | Datetime | Yes | Planned start date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 30 | plannedEndAt | Date | Datetime | Yes | Planned end date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T14:00:00.000+0000")` |  |
| 31 | actualStartAt | Date | Datetime | No (null allowed) | Actual start date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:30.000+0000")` |  |
| 32 | actualEndAt | Date | Datetime | No (null allowed) | Actual end date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T13:40:00.000+0000")` |  |
| 33 | dueDate | Date | Date | Yes | Due date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 34 | erpMessageId | String | - | No (null allowed) | Reference to u_mes_syst_erpMessage._id | `"1229000000000006"` | Reference: u_mes_syst_erpMessage._id |
| 35 | erpMessageName | String | - | No (null allowed) | Display value of erpMessageId, copied from u_mes_syst_erpMessage.recordNo | `"MSG-2026-000168"` |  |
| 36 | closedAt | Date | Datetime | No (null allowed) | Date and time when the record was closed. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 37 | closedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'closed' | `null` | Reference: u_mes_mast_user._id |
| 38 | closedBy | String | - | No (null allowed) | Display name of the user in closedById, copied from u_mes_mast_user.fullName | `null` |  |
| 39 | remarks | String | - | No (null allowed) | Remarks of the production order | `"No abnormality observed"` |  |
| 40 | status | String | - | Yes | Primary lifecycle state of the document | `"Completed"` | Created; Released; In Progress; On Hold; Completed; Closed; Cancelled |
| 41 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 42 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 43 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 44 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 45 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T14:00:00.000+0000")` |  |
| 46 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 47 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Created, Released, In Progress, On Hold, Completed, Closed, Cancelled. Initial state: Created. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ productVariantId: 1 }` | No | Look-up of documents by product variant |
| 5 | `{ billOfMaterialId: 1 }` | No | Look-up of documents by bill of material |
| 6 | `{ routingId: 1 }` | No | Look-up of documents by routing |
| 7 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 8 | `{ siteId: 1, plannedStartAt: -1 }` | No | Time-ordered lists and reports by planned start at |

## Referenced by

u_mes_plan_productionOrderRelease, u_mes_plan_productionOrderLot, u_mes_plan_productionScheduleSlot, u_mes_plan_dispatchListEntry, u_mes_plan_operationExecution, u_mes_plan_wipUnit, u_mes_plan_lot, u_mes_plan_labourBooking, u_mes_plan_changeover, u_mes_plan_shiftHandoverProductionOrder, u_mes_matl_materialMovement, u_mes_matl_kit, u_mes_matl_materialConsumption, u_mes_trac_serialNumber, u_mes_trac_asBuiltRecord, u_mes_qual_checkSheetResult, u_mes_perf_equipmentState, u_mes_perf_downtimeEvent, u_mes_perf_productionCount, u_mes_perf_oeeRecord, u_mes_perf_processReading, u_mes_perf_alarm, u_mes_maint_toolLifeRecord, u_mes_syst_erpMessage, u_mes_syst_businessEvent.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_productionOrder.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_productionOrder.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_productionOrder.js
