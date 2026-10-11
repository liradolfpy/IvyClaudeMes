# u_mes_mdm_department

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Departments of the site (production, quality, maintenance ...) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | DEPT-<recordNo> |
| Display value used by references | name |
| Keys | 15 (11 required, 4 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per department, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: DEPT-<recordNo> | `"DEPT-PROD"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"PROD"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the department; used as its display value in other collections | `"Production"` |  |
| 6 | description | String | Yes | Description of the department | `"All manufacturing lines from casting to packing"` |  |
| 7 | parentDepartmentId | String | No (null allowed) | Reference to u_mes_mdm_department._id: parent department | `"DEPT-MFG"` | Reference: u_mes_mdm_department._id |
| 8 | parentDepartmentName | String | No (null allowed) | Display value of parentDepartmentId, copied from u_mes_mdm_department.name | `"Manufacturing"` |  |
| 9 | headUserId | String | Yes | Reference to u_mes_mdm_user._id: head user | `"USR-10019"` | Reference: u_mes_mdm_user._id |
| 10 | headUserName | String | Yes | Display value of headUserId, copied from u_mes_mdm_user.fullName | `"Meera Deshpande"` |  |
| 11 | costCenterId | String | No (null allowed) | Reference to u_mes_mdm_costCenter._id | `"CC-5120"` | Reference: u_mes_mdm_costCenter._id |
| 12 | costCenterName | String | No (null allowed) | Display value of costCenterId, copied from u_mes_mdm_costCenter.name | `"Assembly Line 1"` |  |
| 13 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 14 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 15 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ parentDepartmentId: 1 }` | No | Look-up of documents by parent department |
| 4 | `{ headUserId: 1 }` | No | Look-up of documents by head user |
| 5 | `{ costCenterId: 1 }` | No | Look-up of documents by cost center |

## Referenced by

u_mes_mdm_user, u_mes_eqp_reasonCode, u_mes_mnt_maintenancePlan, u_mes_mdm_department, u_mes_mdm_designation, u_mes_ehs_andonType.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_department.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_department.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_department.js
