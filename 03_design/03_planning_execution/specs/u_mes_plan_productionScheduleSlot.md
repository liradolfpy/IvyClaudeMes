# u_mes_plan_productionScheduleSlot

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | One document per slot of a production schedule |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_plan_productionSchedule |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 23 (21 required, 2 may be null) |

## Structure

Child collection. The parent production schedule can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. productionScheduleId and productionScheduleName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1087000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SCH-2026-000257-S01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productionScheduleId | String | - | Yes | Reference to u_mes_plan_productionSchedule._id: the parent document this one belongs to | `"1086000000000001"` | Reference: u_mes_plan_productionSchedule._id |
| 6 | productionScheduleName | String | - | Yes | Display value of productionScheduleId, copied from u_mes_plan_productionSchedule.recordNo | `"SCH-2026-000257"` |  |
| 7 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 9 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 10 | itemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 11 | itemName | String | - | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 12 | plannedQuantity | Int32 | - | Yes | Planned quantity | `NumberInt(480)` |  |
| 13 | plannedStartAt | Date | Datetime | Yes | Planned start date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:40.000+0000")` |  |
| 14 | plannedEndAt | Date | Datetime | Yes | Planned end date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T14:00:40.000+0000")` |  |
| 15 | changeoverMinutes | Int32 | - | Yes | Changeover (minutes) | `NumberInt(0)` |  |
| 16 | actualQuantity | Int32 | - | Yes | Actual quantity | `NumberInt(474)` |  |
| 17 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 18 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:40.000+0000")` |  |
| 19 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 20 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 21 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T14:00:40.000+0000")` |  |
| 22 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 23 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ productionScheduleId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ productionOrderId: 1 }` | No | Look-up of lines by production order |
| 3 | `{ itemId: 1 }` | No | Look-up of lines by item |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_productionScheduleSlot.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_productionScheduleSlot.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_productionScheduleSlot.js
