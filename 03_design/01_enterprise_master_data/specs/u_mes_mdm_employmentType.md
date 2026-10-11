# u_mes_mdm_employmentType

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Types of employment (permanent, contract, trainee, apprentice) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | EMT-<recordNo> |
| Display value used by references | name |
| Keys | 10 (10 required, 0 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per employment type, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: EMT-<recordNo> | `"EMT-PERM"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"PERM"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the employment type; used as its display value in other collections | `"Permanent"` |  |
| 6 | description | String | Yes | Description of the employment type | `"On the company payroll without end date"` |  |
| 7 | isContract | Boolean | Yes | True when the record is contract | `true` |  |
| 8 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_mdm_user.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_employmentType.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_employmentType.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_employmentType.js
