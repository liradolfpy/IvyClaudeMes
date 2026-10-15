# u_mes_plan_dispatchListEntry

| Property | Value |
|---|---|
| Module | PlanningAndExecution (plan) |
| Purpose | One document per entry of a dispatch list |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_plan_dispatchList |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 29 (25 required, 4 may be null) |

## Structure

Child collection. The parent dispatch list can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. dispatchListId and dispatchListName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1089000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"DSP-2026-000121-E01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | dispatchListId | String | - | Yes | Reference to u_mes_plan_dispatchList._id: the parent document this one belongs to | `"1088000000000001"` | Reference: u_mes_plan_dispatchList._id |
| 7 | dispatchListName | String | - | Yes | Display value of dispatchListId, copied from u_mes_plan_dispatchList.recordNo | `"DSP-2026-000121"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | rank | Int32 | - | Yes | Position in the work queue (1 = next) | `NumberInt(1)` |  |
| 10 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 11 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 12 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `"1096000000000001"` | Reference: u_mes_plan_lot._id |
| 13 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260915-GDC-014"` |  |
| 14 | itemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 15 | itemName | String | - | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 16 | quantity | Int32 | - | Yes | Quantity of the dispatch list entry | `NumberInt(1)` |  |
| 17 | dueAt | Date | Datetime | Yes | Due date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-19T06:51:40.000+0000")` |  |
| 18 | queueSince | Date | Datetime | Yes | Queue since. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 19 | priority | String | - | Yes | Priority of the dispatch list entry | `"Normal"` | Low; Normal; High; Urgent |
| 20 | materialAvailable | Boolean | - | Yes | True when: material available | `true` |  |
| 21 | toolAvailable | Boolean | - | Yes | True when: tool available | `true` |  |
| 22 | status | String | - | Yes | Primary lifecycle state of the document | `"Queued"` | Queued; Started; Completed; Skipped |
| 23 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 24 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 25 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 26 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 27 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-19T06:51:40.000+0000")` |  |
| 28 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 29 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Queued, Started, Completed, Skipped. Initial state: Queued. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ dispatchListId: 1, rank: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ productionOrderId: 1 }` | No | Look-up of lines by production order |
| 3 | `{ lotId: 1 }` | No | Look-up of lines by lot |
| 4 | `{ itemId: 1 }` | No | Look-up of lines by item |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_dispatchListEntry.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_dispatchListEntry.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_dispatchListEntry.js
