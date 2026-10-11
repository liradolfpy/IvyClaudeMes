# u_mes_qlt_spcChartControlLimit

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | One document per control limit of a SPC chart |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_qlt_spcChart |
| _id pattern | <spcChartId>-CL<nnn> |
| Display value used by references | recordNo |
| Keys | 16 (13 required, 3 may be null) |

## Structure

Child collection. The parent SPC chart can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. spcChartId and spcChartName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <spcChartId>-CL<nnn> | `"SPC-C012-CNC-01-CL001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"C012-CNC-01-CL001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | spcChartId | String | Yes | Reference to u_mes_qlt_spcChart._id: the parent document this one belongs to | `"SPC-C012-CNC-01"` | Reference: u_mes_qlt_spcChart._id |
| 6 | spcChartName | String | Yes | Display value of spcChartId, copied from u_mes_qlt_spcChart.name | `"Piston bore diameter, X-bar R, CNC-01"` |  |
| 7 | revisionNo | Int32 | Yes | Revision number | `NumberInt(2)` |  |
| 8 | effectiveFrom | Date | Yes | Effective from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 9 | ucl | Decimal128 | Yes | Upper control limit | `NumberDecimal("54.031")` |  |
| 10 | centerLine | Decimal128 | Yes | Center line | `NumberDecimal("54.021")` |  |
| 11 | lcl | Decimal128 | Yes | Lower control limit | `NumberDecimal("54.011")` |  |
| 12 | uclRange | Decimal128 | No (null allowed) | UCL range | `NumberDecimal("0.036")` |  |
| 13 | centerLineRange | Decimal128 | No (null allowed) | Center line range | `NumberDecimal("0.017")` |  |
| 14 | lclRange | Decimal128 | No (null allowed) | LCL range | `NumberDecimal("0.000")` |  |
| 15 | basedOnSubgroups | Int32 | Yes | Based on subgroups | `NumberInt(25)` |  |
| 16 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ spcChartId: 1, revisionNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_spcChartControlLimit.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_spcChartControlLimit.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_spcChartControlLimit.js
