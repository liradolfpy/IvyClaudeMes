# u_mes_qual_samplingPlanSizeRow

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per size row of a sampling plan |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_qual_samplingPlan |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 14 (14 required, 0 may be null) |

## Structure

Child collection. The parent sampling plan can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. samplingPlanId and samplingPlanName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1145000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"AQL-1.0-II-SR01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | samplingPlanId | String | - | Yes | Reference to u_mes_qual_samplingPlan._id: the parent document this one belongs to | `"1144000000000001"` | Reference: u_mes_qual_samplingPlan._id |
| 7 | samplingPlanName | String | - | Yes | Display value of samplingPlanId, copied from u_mes_qual_samplingPlan.name | `"AQL 1.0, general inspection level II"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | lotSizeFrom | Int32 | - | Yes | Lot size from | `NumberInt(2)` |  |
| 10 | lotSizeTo | Int32 | - | Yes | Lot size to | `NumberInt(8)` |  |
| 11 | sampleSize | Int32 | - | Yes | Sample size | `NumberInt(2)` |  |
| 12 | acceptNumber | Int32 | - | Yes | Accept number | `NumberInt(0)` |  |
| 13 | rejectNumber | Int32 | - | Yes | Reject number | `NumberInt(1)` |  |
| 14 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ samplingPlanId: 1, lotSizeFrom: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_samplingPlanSizeRow.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_samplingPlanSizeRow.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_samplingPlanSizeRow.js
