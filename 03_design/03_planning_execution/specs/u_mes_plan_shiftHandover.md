# u_mes_plan_shiftHandover

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Shift logbook: output, open issues, safety and quality notes, acknowledgements |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | SHO-<recordNo> |
| Display value used by references | recordNo |
| Keys | 32 (26 required, 6 may be null) |
| Estimated volume per year | ~10,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per shift handover, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with shiftHandoverId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_plan_shiftHandoverProductionOrder | Relationship | production order |
| u_mes_plan_shiftHandoverDowntimeEvent | Relationship | downtime event |
| u_mes_plan_shiftHandoverNonconformance | Relationship | nonconformance |
| u_mes_plan_shiftHandoverOpenItem | Child | open item |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: SHO-<recordNo> | `"SHO-20260929-ASY-01-A"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-ASY-01-A"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productionDate | Date | Yes | Production date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-09-28T18:30:00.000+0000")` |  |
| 6 | shiftId | String | Yes | Reference to u_mes_mast_shift._id | `"SH-A"` | Reference: u_mes_mast_shift._id |
| 7 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 8 | lineId | String | Yes | Reference to u_mes_mast_line._id | `"LN-ASY-01"` | Reference: u_mes_mast_line._id |
| 9 | lineName | String | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Caliper Assembly Line 1"` |  |
| 10 | outgoingSupervisorUserId | String | Yes | Reference to u_mes_mast_user._id: outgoing supervisor user | `"USR-10045"` | Reference: u_mes_mast_user._id |
| 11 | outgoingSupervisorUserName | String | Yes | Display value of outgoingSupervisorUserId, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 12 | incomingSupervisorUserId | String | Yes | Reference to u_mes_mast_user._id: incoming supervisor user | `"USR-10045"` | Reference: u_mes_mast_user._id |
| 13 | incomingSupervisorUserName | String | Yes | Display value of incomingSupervisorUserId, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 14 | outputPlanned | Int32 | Yes | Output planned | `NumberInt(800)` |  |
| 15 | outputActual | Int32 | Yes | Output actual | `NumberInt(762)` |  |
| 16 | outputScrap | Int32 | Yes | Output scrap | `NumberInt(3)` |  |
| 17 | outputRework | Int32 | Yes | Output rework | `NumberInt(6)` |  |
| 18 | oeePct | Decimal128 | Yes | OEE (percent) | `NumberDecimal("80.7")` |  |
| 19 | safetyNotes | String | No (null allowed) | Safety notes | `"Keep hands clear of the nutrunner socket during rundown"` |  |
| 20 | qualityNotes | String | No (null allowed) | Quality notes | `"Two leak test rejects on unit serials ending 0171 and 0178, NCR raised"` |  |
| 21 | maintenanceNotes | String | No (null allowed) | Maintenance notes | `"Nutrunner socket replaced at 09:40"` |  |
| 22 | materialNotes | String | No (null allowed) | Material notes | `"Piston seal lot changeover at 11:15"` |  |
| 23 | handedOverAt | Date | No (null allowed) | Handed over date and time | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 24 | acknowledgedAt | Date | No (null allowed) | Date and time when the record was acknowledged | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 25 | status | String | Yes | Primary lifecycle state of the document | `"Acknowledged"` | Open; Handed Over; Acknowledged |
| 26 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 27 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 28 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 29 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 30 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 31 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mast_user._id |
| 32 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Open, Handed Over, Acknowledged. Initial state: Open. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ outgoingSupervisorUserId: 1 }` | No | Look-up of documents by outgoing supervisor user |
| 6 | `{ incomingSupervisorUserId: 1 }` | No | Look-up of documents by incoming supervisor user |
| 7 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

u_mes_plan_shiftHandoverProductionOrder, u_mes_plan_shiftHandoverDowntimeEvent, u_mes_plan_shiftHandoverNonconformance, u_mes_plan_shiftHandoverOpenItem.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_shiftHandover.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_shiftHandover.js
- Sample document: 03_design/03_planning_execution/samples/u_mes_plan_shiftHandover.js
