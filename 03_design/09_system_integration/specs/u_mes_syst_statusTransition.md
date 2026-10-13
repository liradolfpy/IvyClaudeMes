# u_mes_syst_statusTransition

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Status values and allowed transitions per collection (status mapping) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | transitionName |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Flat entity collection: one document per status transition, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with statusTransitionId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_syst_statusTransitionRole | Relationship | role |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1299000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"productionOrder.CREATED-RELEASED"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Common"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | collectionName | String | - | Yes | Collection name | `"u_mes_plan_productionOrder"` |  |
| 7 | fromStatusDefinitionId | String | - | Yes | Reference to u_mes_syst_statusDefinition._id: from status definition | `"1297000000000001"` | Reference: u_mes_syst_statusDefinition._id |
| 8 | fromStatusDefinitionName | String | - | Yes | Display value of fromStatusDefinitionId, copied from u_mes_syst_statusDefinition.statusName | `"Created"` |  |
| 9 | toStatusDefinitionId | String | - | Yes | Reference to u_mes_syst_statusDefinition._id: to status definition | `"1297000000000002"` | Reference: u_mes_syst_statusDefinition._id |
| 10 | toStatusDefinitionName | String | - | Yes | Display value of toStatusDefinitionId, copied from u_mes_syst_statusDefinition.statusName | `"Released"` |  |
| 11 | transitionName | String | - | Yes | Transition name | `"Release order"` |  |
| 12 | requiresSignature | Boolean | - | Yes | True when signature is required | `true` |  |
| 13 | requiresReason | Boolean | - | Yes | True when reason is required | `false` |  |
| 14 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 15 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 16 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ fromStatusDefinitionId: 1 }` | No | Look-up of documents by from status definition |
| 4 | `{ toStatusDefinitionId: 1 }` | No | Look-up of documents by to status definition |

## Referenced by

u_mes_syst_statusTransitionRole.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_statusTransition.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_statusTransition.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_statusTransition.js
