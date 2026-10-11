# u_mes_eqp_lossCategory

| Property | Value |
|---|---|
| Module | Equipment and performance (eqp) |
| Purpose | OEE loss categories with the OEE factor they reduce |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | LSC-<recordNo> |
| Display value used by references | name |
| Keys | 11 (11 required, 0 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per loss category, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: LSC-<recordNo> | `"LSC-BREAKDOWN"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"BREAKDOWN"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the loss category; used as its display value in other collections | `"Breakdown"` |  |
| 6 | description | String | Yes | Description of the loss category | `"Unplanned equipment failure"` |  |
| 7 | oeeImpact | String | Yes | OEE impact | `"Availability"` | Availability; Performance; Quality; None |
| 8 | sixBigLossNo | Int32 | Yes | Number of the loss in the six big losses of TPM (1 = breakdown) | `NumberInt(1)` |  |
| 9 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 10 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 11 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_eqp_reasonCode, u_mes_eqp_oeeRecordLoss.

## Files

- Validator: 03_design/07_equipment_performance/validators/u_mes_eqp_lossCategory.json
- Indexes: 03_design/07_equipment_performance/indexes/u_mes_eqp_lossCategory.js
- Sample document: 03_design/07_equipment_performance/samples/u_mes_eqp_lossCategory.js
