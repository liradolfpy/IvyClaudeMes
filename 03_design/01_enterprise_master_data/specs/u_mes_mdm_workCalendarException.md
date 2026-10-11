# u_mes_mdm_workCalendarException

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | One document per exception of a work calendar |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mdm_workCalendar |
| _id pattern | <workCalendarId>-E<nnn> |
| Display value used by references | description |
| Keys | 12 (12 required, 0 may be null) |

## Structure

Child collection. The parent work calendar can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. workCalendarId and workCalendarName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <workCalendarId>-E<nnn> | `"CAL-PN1-2026-E001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"PN1-2026-E001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workCalendarId | String | Yes | Reference to u_mes_mdm_workCalendar._id: the parent document this one belongs to | `"CAL-PN1-2026"` | Reference: u_mes_mdm_workCalendar._id |
| 6 | workCalendarName | String | Yes | Display value of workCalendarId, copied from u_mes_mdm_workCalendar.name | `"Chakan Plant Calendar 2026"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | exceptionDate | Date | Yes | Exception date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 9 | exceptionType | String | Yes | Exception type | `"Public Holiday"` | Public Holiday; Plant Shutdown; Extra Working Day; Reduced Shift |
| 10 | description | String | Yes | Description of the work calendar exception | `"Gandhi Jayanti"` |  |
| 11 | isWorking | Boolean | Yes | True when the record is working | `true` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ workCalendarId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

u_mes_mdm_workCalendarExceptionShift.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_workCalendarException.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_workCalendarException.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_workCalendarException.js
