# u_mes_mast_workCalendarWeeklyOffDay

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | One document per weekly off day value of a work calendar |
| Kind | Value list |
| Data class | Master |
| Parent collection | u_mes_mast_workCalendar |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Value-list collection. A work calendar can have several values of this kind, and DATA-001 does not allow an array, so each value is its own document. workCalendarId and workCalendarName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1021000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PN1-2026-WOD01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | workCalendarId | String | - | Yes | Reference to u_mes_mast_workCalendar._id: the parent document this one belongs to | `"1018000000000001"` | Reference: u_mes_mast_workCalendar._id |
| 7 | workCalendarName | String | - | Yes | Display value of workCalendarId, copied from u_mes_mast_workCalendar.name | `"Chakan Plant Calendar 2026"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | weeklyOffDay | String | - | Yes | Weekly off day | `"Saturday"` | Monday; Tuesday; Wednesday; Thursday; Friday; Saturday; Sunday |
| 10 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ workCalendarId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_workCalendarWeeklyOffDay.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_workCalendarWeeklyOffDay.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_workCalendarWeeklyOffDay.js
