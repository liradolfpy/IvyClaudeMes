# u_mes_mdm_role

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Named sets of permissions (operator, setter, quality engineer ...) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | ROLE-<recordNo> |
| Display value used by references | name |
| Keys | 12 (11 required, 1 may be null) |
| Estimated volume per year | 10-40 |
| Storage | standard |

## Structure

Flat entity collection: one document per role, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with roleId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mdm_rolePermission | Relationship | permission |
| u_mes_mdm_roleSignatureMeaning | Relationship | signature meaning |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: ROLE-<recordNo> | `"ROLE-OPERATOR"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"OPERATOR"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the role; used as its display value in other collections | `"Production Operator"` |  |
| 6 | scope | String | Yes | Whether the record applies to the whole enterprise or to one site | `"Enterprise"` | Enterprise; Site |
| 7 | description | String | Yes | Description of the role | `"Runs operations at an assigned station and records results"` |  |
| 8 | canSign | Boolean | Yes | True when the holder can sign | `true` |  |
| 9 | approvalLimitInr | Decimal128 | No (null allowed) | Approval limit (Indian rupees) | `NumberDecimal("0.00")` |  |
| 10 | isSystemRole | Boolean | Yes | True when the record is system role | `false` |  |
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

u_mes_mdm_rolePermission, u_mes_mdm_roleSignatureMeaning, u_mes_mdm_userRole, u_mes_sys_electronicSignature, u_mes_sys_notificationRecipient.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_role.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_role.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_role.js
