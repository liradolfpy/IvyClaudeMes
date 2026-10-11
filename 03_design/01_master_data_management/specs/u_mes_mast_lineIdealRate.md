# u_mes_mast_lineIdealRate

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | One document per ideal rate of a line |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mast_line |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 12 (12 required, 0 may be null) |

## Structure

Child collection. The parent line can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. lineId and lineName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1008000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"GDC-01-IR01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | lineId | String | Yes | Reference to u_mes_mast_line._id: the parent document this one belongs to | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 6 | lineName | String | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | itemId | String | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 10 | idealCycleTimeSec | Decimal128 | Yes | Ideal cycle time (seconds) | `NumberDecimal("95.0")` |  |
| 11 | targetPerHour | Int32 | Yes | Target per hour | `NumberInt(100)` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ lineId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ itemId: 1 }` | No | Look-up of lines by item |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_lineIdealRate.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_lineIdealRate.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_lineIdealRate.js
