# u_mes_syst_recordPolicy

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Edit, lock and retention policy per collection. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 18 (13 required, 5 may be null) |
| Estimated volume per year | one row per collection (343) |
| Storage | standard collection |

## Structure

Flat entity collection: one document per record policy, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1340000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"RPO-u_mes_plan_operationExecution"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | collectionName | String | - | Yes | Collection governed | `"u_mes_plan_operationExecution"` |  |
| 6 | editPolicy | String | - | Yes | Edit policy | `"No Edit After Lock"` | Free Edit; Controlled Edit; No Edit After Lock; Append Only |
| 7 | lockOnStatusDefinitionId | String | - | No (null allowed) | Reference to u_mes_syst_statusDefinition._id: lock on status definition | `null` | Reference: u_mes_syst_statusDefinition._id |
| 8 | lockOnStatusDefinitionName | String | - | No (null allowed) | Display value of lockOnStatusDefinitionId, copied from u_mes_syst_statusDefinition.statusName | `null` |  |
| 9 | requiresReasonForEdit | Boolean | - | Yes | Edit needs a reason | `true` |  |
| 10 | requiresSignatureForEdit | Boolean | - | Yes | Edit needs an electronic signature | `true` |  |
| 11 | editRoleId | String | - | No (null allowed) | Reference to u_mes_mast_role._id: edit role | `null` | Reference: u_mes_mast_role._id |
| 12 | editRoleName | String | - | No (null allowed) | Display value of editRoleId, copied from u_mes_mast_role.name | `null` |  |
| 13 | deleteAllowed | Boolean | - | Yes | Physical delete allowed (false for all transaction data) | `false` |  |
| 14 | retentionYears | Int32 | - | Yes | Retention period | `NumberInt(15)` |  |
| 15 | archiveAfterMonths | Int32 | - | No (null allowed) | Move to archive storage after | `NumberInt(24)` |  |
| 16 | gxpRelevant | Boolean | - | Yes | True when the collection holds GMP records (GMP-10) | `true` |  |
| 17 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 18 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ lockOnStatusDefinitionId: 1 }` | No | Look-up of documents by lock on status definition |
| 4 | `{ editRoleId: 1 }` | No | Look-up of documents by edit role |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_recordPolicy.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_recordPolicy.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_recordPolicy.js
