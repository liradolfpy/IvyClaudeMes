# u_mes_mast_lineDefaultShift

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Links one line to one default shift; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_mast_line |
| _id pattern | <lineId>-DS<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A line can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. lineId and lineName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <lineId>-DS<nnn> | `"LN-ASY-01-DS001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"ASY-01-DS001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | lineId | String | Yes | Reference to u_mes_mast_line._id: the parent document this one belongs to | `"LN-ASY-01"` | Reference: u_mes_mast_line._id |
| 6 | lineName | String | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Caliper Assembly Line 1"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | defaultShiftId | String | Yes | Reference to u_mes_mast_shift._id: default shift | `"SH-A"` | Reference: u_mes_mast_shift._id |
| 9 | defaultShiftName | String | Yes | Display value of defaultShiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ lineId: 1, defaultShiftId: 1 }` | Yes | One link per pair |
| 2 | `{ defaultShiftId: 1, lineId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_lineDefaultShift.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_lineDefaultShift.js
- Sample document: 03_design/01_master_data_management/samples/u_mes_mast_lineDefaultShift.js
