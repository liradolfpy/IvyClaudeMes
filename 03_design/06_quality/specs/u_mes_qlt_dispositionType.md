# u_mes_qlt_dispositionType

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | Dispositions for nonconforming material (use as is, rework, scrap, return, sort) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | DSP-T-<recordNo> |
| Display value used by references | name |
| Keys | 12 (12 required, 0 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per disposition type, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: DSP-T-<recordNo> | `"DSP-T-REWORK"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"REWORK"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the disposition type; used as its display value in other collections | `"Rework"` |  |
| 6 | description | String | Yes | Description of the disposition type | `"Bring the part back to specification on the rework routing"` |  |
| 7 | requiresRework | Boolean | Yes | True when rework is required | `true` |  |
| 8 | requiresScrap | Boolean | Yes | True when scrap is required | `true` |  |
| 9 | requiresCustomerApproval | Boolean | Yes | True when customer approval is required | `true` |  |
| 10 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 11 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_prd_engineeringChange, u_mes_qlt_defectCode, u_mes_qlt_nonconformanceAffectedObject.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_dispositionType.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_dispositionType.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_dispositionType.js
