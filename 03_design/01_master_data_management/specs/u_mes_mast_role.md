# u_mes_mast_role

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Named sets of permissions (operator, setter, quality engineer ...) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 12 (11 required, 1 may be null) |
| Estimated volume per year | 10-40 |
| Storage | standard |

## Structure

Flat entity collection: one document per role, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with roleId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mast_rolePermission | Relationship | permission |
| u_mes_mast_roleSignatureMeaning | Relationship | signature meaning |
| u_mes_mast_roleRequiredSkill | Relationship | required skill |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1026000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"OPERATOR"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the role; used as its display value in other collections | `"Production Operator"` |  |
| 6 | scope | String | - | Yes | Whether the record applies to the whole enterprise or to one site | `"Enterprise"` | Enterprise; Site |
| 7 | description | String | - | Yes | Description of the role | `"Runs operations at an assigned station and records results"` |  |
| 8 | canSign | Boolean | - | Yes | True when the holder can sign | `true` |  |
| 9 | approvalLimitInr | Decimal128 | - | No (null allowed) | Approval limit (Indian rupees) | `NumberDecimal("0.00")` |  |
| 10 | isSystemRole | Boolean | - | Yes | True when the record is system role | `false` |  |
| 11 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 12 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_mast_rolePermission, u_mes_mast_roleSignatureMeaning, u_mes_mast_userRole, u_mes_syst_electronicSignature, u_mes_syst_notificationRecipient, u_mes_mast_roleRequiredSkill, u_mes_qual_auditSchedule, u_mes_perf_alarmDefinition, u_mes_syst_interlockRule, u_mes_syst_statusTransitionRole, u_mes_syst_escalationRule, u_mes_syst_escalationRuleLevel, u_mes_syst_recordPolicy, u_mes_syst_savedView, u_mes_syst_userAccessReviewLine.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_role.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_role.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_role.js
