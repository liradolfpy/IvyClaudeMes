# u_mes_qual_spcChartControlLimit

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per control limit of a SPC chart |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_qual_spcChart |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 16 (13 required, 3 may be null) |

## Structure

Child collection. The parent SPC chart can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. spcChartId and spcChartName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1152000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SPC-OP010-01-CL01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | spcChartId | String | - | Yes | Reference to u_mes_qual_spcChart._id: the parent document this one belongs to | `"1151000000000001"` | Reference: u_mes_qual_spcChart._id |
| 6 | spcChartName | String | - | Yes | Display value of spcChartId, copied from u_mes_qual_spcChart.name | `"Casting wall thickness at bridge, X-bar R chart"` |  |
| 7 | revisionNo | Int32 | - | Yes | Revision number | `NumberInt(1)` |  |
| 8 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 9 | ucl | Decimal128 | - | Yes | Upper control limit | `NumberDecimal("8.20")` |  |
| 10 | centerLine | Decimal128 | - | Yes | Center line | `NumberDecimal("8.02")` |  |
| 11 | lcl | Decimal128 | - | Yes | Lower control limit | `NumberDecimal("7.84")` |  |
| 12 | uclRange | Decimal128 | - | No (null allowed) | UCL range | `NumberDecimal("0.36")` |  |
| 13 | centerLineRange | Decimal128 | - | No (null allowed) | Center line range | `NumberDecimal("0.17")` |  |
| 14 | lclRange | Decimal128 | - | No (null allowed) | LCL range | `NumberDecimal("0.00")` |  |
| 15 | basedOnSubgroups | Int32 | - | Yes | Based on subgroups | `NumberInt(25)` |  |
| 16 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ spcChartId: 1, revisionNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_spcChartControlLimit.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_spcChartControlLimit.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_spcChartControlLimit.js
