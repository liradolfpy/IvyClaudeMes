# u_mes_qual_samplingPlanSizeRow

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per size row of a sampling plan |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_qual_samplingPlan |
| _id pattern | <samplingPlanId>-SR<nnn> |
| Display value used by references | recordNo |
| Keys | 13 (13 required, 0 may be null) |

## Structure

Child collection. The parent sampling plan can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. samplingPlanId and samplingPlanName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <samplingPlanId>-SR<nnn> | `"SMP-AQL-1.0-II-SR001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"AQL-1.0-II-SR001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | samplingPlanId | String | Yes | Reference to u_mes_qual_samplingPlan._id: the parent document this one belongs to | `"SMP-AQL-1.0-II"` | Reference: u_mes_qual_samplingPlan._id |
| 6 | samplingPlanName | String | Yes | Display value of samplingPlanId, copied from u_mes_qual_samplingPlan.name | `"AQL 1.0, general inspection level II"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | lotSizeFrom | Int32 | Yes | Lot size from | `NumberInt(281)` |  |
| 9 | lotSizeTo | Int32 | Yes | Lot size to | `NumberInt(500)` |  |
| 10 | sampleSize | Int32 | Yes | Sample size | `NumberInt(5)` |  |
| 11 | acceptNumber | Int32 | Yes | Accept number | `NumberInt(1)` |  |
| 12 | rejectNumber | Int32 | Yes | Reject number | `NumberInt(2)` |  |
| 13 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ samplingPlanId: 1, lotSizeFrom: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_samplingPlanSizeRow.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_samplingPlanSizeRow.js
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_samplingPlanSizeRow.js
