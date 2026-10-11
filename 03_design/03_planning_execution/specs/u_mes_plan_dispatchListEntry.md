# u_mes_plan_dispatchListEntry

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | One document per entry of a dispatch list |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_plan_dispatchList |
| _id pattern | <dispatchListId>-E<nnn> |
| Display value used by references | recordNo |
| Keys | 28 (24 required, 4 may be null) |

## Structure

Child collection. The parent dispatch list can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. dispatchListId and dispatchListName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <dispatchListId>-E<nnn> | `"DSP-20260929-TRQ-01-A-E001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-TRQ-01-A-E001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | dispatchListId | String | Yes | Reference to u_mes_plan_dispatchList._id: the parent document this one belongs to | `"DSP-20260929-TRQ-01-A"` | Reference: u_mes_plan_dispatchList._id |
| 6 | dispatchListName | String | Yes | Display value of dispatchListId, copied from u_mes_plan_dispatchList.recordNo | `"20260929-TRQ-01-A"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | rank | Int32 | Yes | Position in the work queue (1 = next) | `NumberInt(1)` |  |
| 9 | productionOrderId | String | Yes | Reference to u_mes_plan_productionOrder._id | `"PO-1000412"` | Reference: u_mes_plan_productionOrder._id |
| 10 | productionOrderName | String | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"1000412"` |  |
| 11 | lotId | String | No (null allowed) | Reference to u_mes_plan_lot._id | `"LOT-L260928-GDC-014"` | Reference: u_mes_plan_lot._id |
| 12 | lotName | String | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260928-GDC-014"` |  |
| 13 | itemId | String | No (null allowed) | Reference to u_mes_prod_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prod_item._id |
| 14 | itemName | String | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 15 | quantity | Int32 | Yes | Quantity of the dispatch list entry | `NumberInt(1)` |  |
| 16 | dueAt | Date | Yes | Due date and time | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 17 | queueSince | Date | Yes | Queue since (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 18 | priority | String | Yes | Priority of the dispatch list entry | `"Normal"` | Low; Normal; High; Urgent |
| 19 | materialAvailable | Boolean | Yes | True when: material available | `true` |  |
| 20 | toolAvailable | Boolean | Yes | True when: tool available | `true` |  |
| 21 | status | String | Yes | Primary lifecycle state of the document | `"Completed"` | Queued; Started; Completed; Skipped |
| 22 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 23 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 24 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 25 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 26 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 27 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 28 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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
- Sample document: 03_design/03_planning_execution/samples/u_mes_plan_dispatchListEntry.js
