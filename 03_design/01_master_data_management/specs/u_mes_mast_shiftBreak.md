# u_mes_mast_shiftBreak

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | One document per break of a shift |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mast_shift |
| _id pattern | <shiftId>-B<nnn> |
| Display value used by references | name |
| Keys | 12 (12 required, 0 may be null) |

## Structure

Child collection. The parent shift can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. shiftId and shiftName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <shiftId>-B<nnn> | `"SH-A-B001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"A-B001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | shiftId | String | Yes | Reference to u_mes_mast_shift._id: the parent document this one belongs to | `"SH-A"` | Reference: u_mes_mast_shift._id |
| 6 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | name | String | Yes | Name of the shift break; used as its display value in other collections | `"Lunch break"` |  |
| 9 | startTimeLocal | String | Yes | Local start time, 24-hour HH:mm | `"06:00"` |  |
| 10 | durationMinutes | Int32 | Yes | Duration (minutes) | `NumberInt(480)` |  |
| 11 | paid | Boolean | Yes | True when: paid | `true` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ shiftId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_shiftBreak.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_shiftBreak.js
- Sample document: 03_design/01_master_data_management/samples/u_mes_mast_shiftBreak.js
