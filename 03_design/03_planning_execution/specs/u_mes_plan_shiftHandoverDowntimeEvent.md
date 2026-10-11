# u_mes_plan_shiftHandoverDowntimeEvent

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Links one shift handover to one downtime event; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_plan_shiftHandover |
| _id pattern | <shiftHandoverId>-DE<nnn> |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A shift handover can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. shiftHandoverId and shiftHandoverName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <shiftHandoverId>-DE<nnn> | `"SHO-20260929-ASY-01-A-DE001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-ASY-01-A-DE001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | shiftHandoverId | String | Yes | Reference to u_mes_plan_shiftHandover._id: the parent document this one belongs to | `"SHO-20260929-ASY-01-A"` | Reference: u_mes_plan_shiftHandover._id |
| 6 | shiftHandoverName | String | Yes | Display value of shiftHandoverId, copied from u_mes_plan_shiftHandover.recordNo | `"20260929-ASY-01-A"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | downtimeEventId | String | Yes | Reference to u_mes_perf_downtimeEvent._id | `"DT-20260929-0009"` | Reference: u_mes_perf_downtimeEvent._id |
| 9 | downtimeEventName | String | Yes | Display value of downtimeEventId, copied from u_mes_perf_downtimeEvent.recordNo | `"20260929-0009"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 11 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 12 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 13 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 14 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 15 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 16 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ shiftHandoverId: 1, downtimeEventId: 1 }` | Yes | One link per pair |
| 2 | `{ downtimeEventId: 1, shiftHandoverId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_shiftHandoverDowntimeEvent.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_shiftHandoverDowntimeEvent.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_plan_shiftHandoverDowntimeEvent.js
