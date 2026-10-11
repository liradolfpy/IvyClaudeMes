# u_mes_mast_department

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Departments of the site (production, quality, maintenance ...) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
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
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1256000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"PROD"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the department; used as its display value in other collections | `"Production"` |  |
| 6 | description | String | Yes | Description of the department | `"Production (PROD)"` |  |
| 7 | parentDepartmentId | String | No (null allowed) | Reference to u_mes_mast_department._id: parent department | `null` | Reference: u_mes_mast_department._id |
| 8 | parentDepartmentName | String | No (null allowed) | Display value of parentDepartmentId, copied from u_mes_mast_department.name | `null` |  |
| 9 | headUserId | String | Yes | Reference to u_mes_mast_user._id: head user | `"1029000000000005"` | Reference: u_mes_mast_user._id |
| 10 | headUserName | String | Yes | Display value of headUserId, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 11 | costCenterId | String | No (null allowed) | Reference to u_mes_mast_costCenter._id | `"1259000000000005"` | Reference: u_mes_mast_costCenter._id |
| 12 | costCenterName | String | No (null allowed) | Display value of costCenterId, copied from u_mes_mast_costCenter.name | `"Assembly and Test"` |  |
| 13 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 14 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 15 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ parentDepartmentId: 1 }` | No | Look-up of documents by parent department |
| 4 | `{ headUserId: 1 }` | No | Look-up of documents by head user |
| 5 | `{ costCenterId: 1 }` | No | Look-up of documents by cost center |

## Referenced by

u_mes_mast_user, u_mes_perf_reasonCode, u_mes_maint_maintenancePlan, u_mes_mast_department, u_mes_mast_designation, u_mes_plan_andonType.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_department.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_department.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_department.js
