# u_mes_mdm_permission

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Permissions that can be granted to roles |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | PRM-<recordNo> |
| Display value used by references | name |
| Keys | 11 (11 required, 0 may be null) |
| Estimated volume per year | 100-500 |
| Storage | standard |

## Structure

Flat entity collection: one document per permission, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: PRM-<recordNo> | `"PRM-operationExecution.complete"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"operationExecution.complete"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the permission; used as its display value in other collections | `"Complete an operation"` |  |
| 6 | description | String | Yes | Description of the permission | `"Complete an operation"` |  |
| 7 | resourceName | String | Yes | Object the permission applies to | `"operationExecution"` |  |
| 8 | actionName | String | Yes | Action the permission allows on the resource | `"complete"` |  |
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

u_mes_mdm_rolePermission.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_permission.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_permission.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_permission.js
