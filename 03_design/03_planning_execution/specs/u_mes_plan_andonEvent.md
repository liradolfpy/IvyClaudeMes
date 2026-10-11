# u_mes_plan_andonEvent

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Help calls from stations (quality, material, maintenance, safety) with response and escalation times |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | description |
| Keys | 38 (27 required, 11 may be null) |
| Estimated volume per year | ~40,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per andon event, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with andonEventId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_plan_andonEventEscalation | Child | escalation |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1251000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"AND-2026-000195"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workCenterId | String | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 6 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 7 | lineId | String | Yes | Reference to u_mes_mast_line._id | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 8 | lineName | String | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 9 | shiftId | String | Yes | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 10 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 11 | andonTypeId | String | Yes | Reference to u_mes_plan_andonType._id | `"1292000000000003"` | Reference: u_mes_plan_andonType._id |
| 12 | andonTypeName | String | Yes | Display value of andonTypeId, copied from u_mes_plan_andonType.name | `"Maintenance"` |  |
| 13 | reasonCodeId | String | No (null allowed) | Reference to u_mes_perf_reasonCode._id | `"1203000000000001"` | Reference: u_mes_perf_reasonCode._id |
| 14 | reasonCodeName | String | No (null allowed) | Display value of reasonCodeId, copied from u_mes_perf_reasonCode.name | `"Die ejector pin stuck"` |  |
| 15 | raisedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'raised' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 16 | raisedBy | String | Yes | Display name of the user in raisedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 17 | raisedAt | Date | Yes | Date and time when the record was raised | `ISODate("2026-09-17T01:22:20.000+0000")` |  |
| 18 | acknowledgedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'acknowledged' | `null` | Reference: u_mes_mast_user._id |
| 19 | acknowledgedBy | String | No (null allowed) | Display name of the user in acknowledgedById, copied from u_mes_mast_user.fullName | `null` |  |
| 20 | acknowledgedAt | Date | No (null allowed) | Date and time when the record was acknowledged | `null` |  |
| 21 | resolvedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'resolved' | `null` | Reference: u_mes_mast_user._id |
| 22 | resolvedBy | String | No (null allowed) | Display name of the user in resolvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 23 | resolvedAt | Date | No (null allowed) | Date and time when the record was resolved | `null` |  |
| 24 | responseSec | Int32 | Yes | Response (seconds) | `NumberInt(210)` |  |
| 25 | resolutionSec | Int32 | Yes | Resolution (seconds) | `NumberInt(840)` |  |
| 26 | lineStopped | Boolean | Yes | True when: line stopped | `true` |  |
| 27 | downtimeEventId | String | No (null allowed) | Reference to u_mes_perf_downtimeEvent._id | `"1205000000000001"` | Reference: u_mes_perf_downtimeEvent._id |
| 28 | downtimeEventName | String | No (null allowed) | Display value of downtimeEventId, copied from u_mes_perf_downtimeEvent.recordNo | `"DT-2026-000196"` |  |
| 29 | description | String | Yes | Description of the andon event | `"Castings sticking in die 2, operator needs maintenance"` |  |
| 30 | resolutionText | String | No (null allowed) | Resolution text | `"Ejector pin polished and die coat thickness corrected"` |  |
| 31 | status | String | Yes | Primary lifecycle state of the document | `"Raised"` | Raised; Acknowledged; Resolved; Cancelled |
| 32 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 33 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-17T01:22:20.000+0000")` |  |
| 34 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 35 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 36 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-17T01:22:20.000+0000")` |  |
| 37 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 38 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Raised, Acknowledged, Resolved, Cancelled. Initial state: Raised. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 6 | `{ andonTypeId: 1 }` | No | Look-up of documents by andon type |
| 7 | `{ reasonCodeId: 1 }` | No | Look-up of documents by reason code |
| 8 | `{ siteId: 1, raisedAt: -1 }` | No | Time-ordered lists and reports by raised at |

## Referenced by

u_mes_matl_materialRequest, u_mes_syst_notification, u_mes_plan_andonEventEscalation.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_andonEvent.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_andonEvent.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_andonEvent.js
