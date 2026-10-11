# u_mes_mast_workCalendar

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Working calendars with holidays and exception days per site / line |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | CAL-<recordNo> |
| Display value used by references | name |
| Keys | 11 (10 required, 1 may be null) |
| Estimated volume per year | 1-20 per site per year |
| Storage | standard |

## Structure

Flat entity collection: one document per work calendar, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with workCalendarId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mast_workCalendarLine | Relationship | line |
| u_mes_mast_workCalendarShift | Relationship | shift |
| u_mes_mast_workCalendarWeeklyOffDay | Value list | weekly off day |
| u_mes_mast_workCalendarException | Child | exception |
| u_mes_mast_workCalendarExceptionShift | Relationship | (below u_mes_mast_workCalendarException) shift |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: CAL-<recordNo> | `"CAL-PN1-2026"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"PN1-2026"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the work calendar; used as its display value in other collections | `"Chakan Plant Calendar 2026"` |  |
| 6 | year | Int32 | Yes | Year of the work calendar | `NumberInt(2026)` |  |
| 7 | workingDaysCount | Int32 | Yes | Working days count | `NumberInt(303)` |  |
| 8 | validFrom | Date | Yes | Valid from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 9 | validTo | Date | No (null allowed) | Valid to (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2027-03-31T18:29:59.000+0000")` |  |
| 10 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 11 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_mast_site, u_mes_mast_line, u_mes_mast_workCalendarLine, u_mes_mast_workCalendarShift, u_mes_mast_workCalendarWeeklyOffDay, u_mes_mast_workCalendarException, u_mes_plan_productionSchedule.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_workCalendar.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_workCalendar.js
- Sample document: 03_design/01_master_data_management/samples/u_mes_mast_workCalendar.js
