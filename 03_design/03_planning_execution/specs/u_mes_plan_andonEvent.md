# u_mes_plan_andonEvent

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Help calls from stations (quality, material, maintenance, safety) with response and escalation times |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | AND-<recordNo> |
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
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: AND-<recordNo> | `"AND-20260929-0005"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-0005"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workCenterId | String | Yes | Reference to u_mes_mast_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mast_workCenter._id |
| 6 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 7 | lineId | String | Yes | Reference to u_mes_mast_line._id | `"LN-ASY-01"` | Reference: u_mes_mast_line._id |
| 8 | lineName | String | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Caliper Assembly Line 1"` |  |
| 9 | shiftId | String | Yes | Reference to u_mes_mast_shift._id | `"SH-A"` | Reference: u_mes_mast_shift._id |
| 10 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 11 | andonTypeId | String | Yes | Reference to u_mes_plan_andonType._id | `"ANT-QUALITY"` | Reference: u_mes_plan_andonType._id |
| 12 | andonTypeName | String | Yes | Display value of andonTypeId, copied from u_mes_plan_andonType.name | `"Quality"` |  |
| 13 | reasonCodeId | String | No (null allowed) | Reference to u_mes_perf_reasonCode._id | `"RSN-MECH-NR-02"` | Reference: u_mes_perf_reasonCode._id |
| 14 | reasonCodeName | String | No (null allowed) | Display value of reasonCodeId, copied from u_mes_perf_reasonCode.name | `"Nutrunner socket worn"` |  |
| 15 | raisedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'raised' | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 16 | raisedBy | String | Yes | Display name of the user in raisedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 17 | raisedAt | Date | Yes | Date and time when the record was raised | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 18 | acknowledgedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'acknowledged' | `"USR-10045"` | Reference: u_mes_mast_user._id |
| 19 | acknowledgedBy | String | No (null allowed) | Display name of the user in acknowledgedById, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 20 | acknowledgedAt | Date | No (null allowed) | Date and time when the record was acknowledged | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 21 | resolvedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'resolved' | `"USR-10112"` | Reference: u_mes_mast_user._id |
| 22 | resolvedBy | String | No (null allowed) | Display name of the user in resolvedById, copied from u_mes_mast_user.fullName | `"Imran Shaikh"` |  |
| 23 | resolvedAt | Date | No (null allowed) | Date and time when the record was resolved | `ISODate("2026-09-29T00:30:54.000+0000")` |  |
| 24 | responseSec | Int32 | Yes | Response (seconds) | `NumberInt(210)` |  |
| 25 | resolutionSec | Int32 | Yes | Resolution (seconds) | `NumberInt(840)` |  |
| 26 | lineStopped | Boolean | Yes | True when: line stopped | `false` |  |
| 27 | downtimeEventId | String | No (null allowed) | Reference to u_mes_perf_downtimeEvent._id | `"DT-20260929-0009"` | Reference: u_mes_perf_downtimeEvent._id |
| 28 | downtimeEventName | String | No (null allowed) | Display value of downtimeEventId, copied from u_mes_perf_downtimeEvent.recordNo | `"20260929-0009"` |  |
| 29 | description | String | Yes | Description of the andon event | `"Leak test rejects repeating at station LKT-01"` |  |
| 30 | resolutionText | String | No (null allowed) | Resolution text | `"Seal lot segregated, new lot issued"` |  |
| 31 | status | String | Yes | Primary lifecycle state of the document | `"Resolved"` | Raised; Acknowledged; Resolved; Cancelled |
| 32 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 33 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 34 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 35 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 36 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:54.000+0000")` |  |
| 37 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
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
- Sample document: 03_design/03_planning_execution/samples/u_mes_plan_andonEvent.js
