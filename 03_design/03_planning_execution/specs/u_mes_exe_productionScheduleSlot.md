# u_mes_exe_productionScheduleSlot

| Property | Value |
|---|---|
| Module | Planning and execution (exe) |
| Purpose | One document per slot of a production schedule |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_exe_productionSchedule |
| _id pattern | <productionScheduleId>-S<nnn> |
| Display value used by references | recordNo |
| Keys | 23 (21 required, 2 may be null) |

## Structure

Child collection. The parent production schedule can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. productionScheduleId and productionScheduleName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <productionScheduleId>-S<nnn> | `"SCH-20260929-ASY-01-A-S001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-ASY-01-A-S001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productionScheduleId | String | Yes | Reference to u_mes_exe_productionSchedule._id: the parent document this one belongs to | `"SCH-20260929-ASY-01-A"` | Reference: u_mes_exe_productionSchedule._id |
| 6 | productionScheduleName | String | Yes | Display value of productionScheduleId, copied from u_mes_exe_productionSchedule.recordNo | `"20260929-ASY-01-A"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | productionOrderId | String | Yes | Reference to u_mes_exe_productionOrder._id | `"PO-1000412"` | Reference: u_mes_exe_productionOrder._id |
| 9 | productionOrderName | String | Yes | Display value of productionOrderId, copied from u_mes_exe_productionOrder.recordNo | `"1000412"` |  |
| 10 | itemId | String | No (null allowed) | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 11 | itemName | String | No (null allowed) | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 12 | plannedQuantity | Int32 | Yes | Planned quantity | `NumberInt(480)` |  |
| 13 | plannedStartAt | Date | Yes | Planned start date and time | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 14 | plannedEndAt | Date | Yes | Planned end date and time | `ISODate("2026-09-29T08:30:00.000+0000")` |  |
| 15 | changeoverMinutes | Int32 | Yes | Changeover (minutes) | `NumberInt(0)` |  |
| 16 | actualQuantity | Int32 | Yes | Actual quantity | `NumberInt(474)` |  |
| 17 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 18 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 19 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 20 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 21 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T08:30:00.000+0000")` |  |
| 22 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 23 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ productionScheduleId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ productionOrderId: 1 }` | No | Look-up of lines by production order |
| 3 | `{ itemId: 1 }` | No | Look-up of lines by item |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_exe_productionScheduleSlot.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_exe_productionScheduleSlot.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_exe_productionScheduleSlot.js
