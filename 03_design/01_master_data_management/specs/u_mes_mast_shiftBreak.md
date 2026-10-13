# u_mes_mast_shiftBreak

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | One document per break of a shift |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mast_shift |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 13 (13 required, 0 may be null) |

## Structure

Child collection. The parent shift can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. shiftId and shiftName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1016000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"A-B01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id: the parent document this one belongs to | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 7 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | name | String | - | Yes | Name of the shift break | `"Tea break"` |  |
| 10 | startTimeLocal | String | - | Yes | Local start time, 24-hour HH:mm | `"06:00"` |  |
| 11 | durationMinutes | Int32 | - | Yes | Duration (minutes) | `NumberInt(480)` |  |
| 12 | paid | Boolean | - | Yes | True when: paid | `true` |  |
| 13 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ shiftId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_shiftBreak.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_shiftBreak.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_shiftBreak.js
