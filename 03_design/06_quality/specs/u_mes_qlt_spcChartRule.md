# u_mes_qlt_spcChartRule

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | One document per rule value of a SPC chart |
| Kind | Value list |
| Data class | Master |
| Parent collection | u_mes_qlt_spcChart |
| _id pattern | <spcChartId>-R<nnn> |
| Display value used by references | recordNo |
| Keys | 9 (9 required, 0 may be null) |

## Structure

Value-list collection. A SPC chart can have several values of this kind, and DATA-001 does not allow an array, so each value is its own document. spcChartId and spcChartName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <spcChartId>-R<nnn> | `"SPC-C012-CNC-01-R001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"C012-CNC-01-R001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | spcChartId | String | Yes | Reference to u_mes_qlt_spcChart._id: the parent document this one belongs to | `"SPC-C012-CNC-01"` | Reference: u_mes_qlt_spcChart._id |
| 6 | spcChartName | String | Yes | Display value of spcChartId, copied from u_mes_qlt_spcChart.name | `"Piston bore diameter, X-bar R, CNC-01"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | rule | String | Yes | Rule of the SPC chart rule | `"Earliest Due Date"` | Earliest Due Date; First In First Out; Critical Ratio; Priority |
| 9 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ spcChartId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_spcChartRule.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_spcChartRule.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_spcChartRule.js
