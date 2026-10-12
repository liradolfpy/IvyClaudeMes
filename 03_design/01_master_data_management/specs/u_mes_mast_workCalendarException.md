# u_mes_mast_workCalendarException

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | One document per exception of a work calendar |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mast_workCalendar |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 12 (12 required, 0 may be null) |

## Structure

Child collection. The parent work calendar can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. workCalendarId and workCalendarName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1022000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PN1-2026-E01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workCalendarId | String | - | Yes | Reference to u_mes_mast_workCalendar._id: the parent document this one belongs to | `"1018000000000001"` | Reference: u_mes_mast_workCalendar._id |
| 6 | workCalendarName | String | - | Yes | Display value of workCalendarId, copied from u_mes_mast_workCalendar.name | `"Chakan Plant Calendar 2026"` |  |
| 7 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | exceptionDate | Date | Date | Yes | Exception date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-05-01T00:00:00.000+0000")` |  |
| 9 | exceptionType | String | - | Yes | Exception type | `"Public Holiday"` | Public Holiday; Plant Shutdown; Extra Working Day; Reduced Shift |
| 10 | description | String | - | Yes | Description of the work calendar exception | `"Maharashtra Day"` |  |
| 11 | isWorking | Boolean | - | Yes | True when the record is working | `false` |  |
| 12 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ workCalendarId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

u_mes_mast_workCalendarExceptionShift.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_workCalendarException.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_workCalendarException.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_workCalendarException.js
