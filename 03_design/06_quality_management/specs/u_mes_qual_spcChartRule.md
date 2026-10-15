# u_mes_qual_spcChartRule

| Property | Value |
|---|---|
| Module | QualityManagement (qual) |
| Purpose | One document per rule value of a SPC chart |
| Kind | Value list |
| Data class | Master |
| Parent collection | u_mes_qual_spcChart |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Value-list collection. A SPC chart can have several values of this kind, and DATA-001 does not allow an array, so each value is its own document. spcChartId and spcChartName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1153000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SPC-OP010-01-R01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | spcChartId | String | - | Yes | Reference to u_mes_qual_spcChart._id: the parent document this one belongs to | `"1151000000000001"` | Reference: u_mes_qual_spcChart._id |
| 7 | spcChartName | String | - | Yes | Display value of spcChartId, copied from u_mes_qual_spcChart.name | `"Casting wall thickness at bridge, X-bar R chart"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | rule | String | - | Yes | Rule of the SPC chart rule | `"Earliest Due Date"` | Earliest Due Date; First In First Out; Critical Ratio; Priority |
| 10 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ spcChartId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_spcChartRule.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_spcChartRule.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_spcChartRule.js
