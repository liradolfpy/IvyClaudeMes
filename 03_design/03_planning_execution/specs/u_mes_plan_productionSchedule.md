# u_mes_plan_productionSchedule

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Finite schedule per line and shift with sequenced orders, planned start/end |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 27 (24 required, 3 may be null) |
| Estimated volume per year | ~10,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per production schedule, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with productionScheduleId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_plan_productionScheduleSlot | Child | slot |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1086000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SCH-2026-000257"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productionDate | Date | Date | Yes | Production date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 6 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000006"` | Reference: u_mes_mast_line._id |
| 7 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Front Caliper Assembly Line 1"` |  |
| 8 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 9 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 10 | workCalendarId | String | - | Yes | Reference to u_mes_mast_workCalendar._id | `"1018000000000001"` | Reference: u_mes_mast_workCalendar._id |
| 11 | workCalendarName | String | - | Yes | Display value of workCalendarId, copied from u_mes_mast_workCalendar.name | `"Chakan Plant Calendar 2026"` |  |
| 12 | scheduleVersion | Int32 | - | Yes | Schedule version | `NumberInt(2)` |  |
| 13 | plannedOutput | Int32 | - | Yes | Planned output | `NumberInt(800)` |  |
| 14 | actualOutput | Int32 | - | Yes | Actual output | `NumberInt(762)` |  |
| 15 | attainmentPct | Decimal128 | - | Yes | Attainment (percent) | `NumberDecimal("95.3")` |  |
| 16 | frozen | Boolean | - | Yes | True when: frozen | `false` |  |
| 17 | publishedAt | Date | Datetime | No (null allowed) | Date and time when the record was published. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 18 | publishedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'published' | `null` | Reference: u_mes_mast_user._id |
| 19 | publishedBy | String | - | No (null allowed) | Display name of the user in publishedById, copied from u_mes_mast_user.fullName | `null` |  |
| 20 | status | String | - | Yes | Primary lifecycle state of the document | `"Planned"` | Planned; Published; In Progress; Completed |
| 21 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 22 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 23 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 24 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 25 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 26 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 27 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Planned, Published, In Progress, Completed. Initial state: Planned. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 4 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 5 | `{ workCalendarId: 1 }` | No | Look-up of documents by work calendar |
| 6 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

u_mes_plan_productionScheduleSlot.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_productionSchedule.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_productionSchedule.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_productionSchedule.js
