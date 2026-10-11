# u_mes_sys_statusTransition

| Property | Value |
|---|---|
| Module | Integration and system (sys) |
| Purpose | Status values and allowed transitions per collection (status mapping) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | STT-<recordNo> |
| Display value used by references | transitionName |
| Keys | 15 (15 required, 0 may be null) |

## Structure

Flat entity collection: one document per status transition, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: STT-<recordNo> | `"STT-productionOrder.RELEASED-IN_PROGRESS"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"productionOrder.RELEASED-IN_PROGRESS"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | collectionName | String | Yes | Collection name | `"u_mes_exe_productionOrder"` |  |
| 6 | fromStatusDefinitionId | String | Yes | Reference to u_mes_sys_statusDefinition._id: from status definition | `"STD-productionOrder.RELEASED"` | Reference: u_mes_sys_statusDefinition._id |
| 7 | fromStatusDefinitionName | String | Yes | Display value of fromStatusDefinitionId, copied from u_mes_sys_statusDefinition.statusName | `"Released"` |  |
| 8 | toStatusDefinitionId | String | Yes | Reference to u_mes_sys_statusDefinition._id: to status definition | `"STD-productionOrder.IN_PROGRESS"` | Reference: u_mes_sys_statusDefinition._id |
| 9 | toStatusDefinitionName | String | Yes | Display value of toStatusDefinitionId, copied from u_mes_sys_statusDefinition.statusName | `"In Progress"` |  |
| 10 | transitionName | String | Yes | Transition name | `"Start production"` |  |
| 11 | requiresSignature | Boolean | Yes | True when signature is required | `true` |  |
| 12 | requiresReason | Boolean | Yes | True when reason is required | `false` |  |
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
| 3 | `{ fromStatusDefinitionId: 1 }` | No | Look-up of documents by from status definition |
| 4 | `{ toStatusDefinitionId: 1 }` | No | Look-up of documents by to status definition |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_integration_system/validators/u_mes_sys_statusTransition.json
- Indexes: 03_design/09_integration_system/indexes/u_mes_sys_statusTransition.js
- Sample document: 03_design/09_integration_system/samples/u_mes_sys_statusTransition.js
