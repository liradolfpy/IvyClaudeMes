# u_mes_syst_statusDefinition

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Status values and allowed transitions per collection (status mapping) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | statusName |
| Keys | 16 (15 required, 1 may be null) |

## Structure

Flat entity collection: one document per status definition, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1297000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"productionOrder.CREATED"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Common"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | collectionName | String | - | Yes | Collection name | `"u_mes_plan_productionOrder"` |  |
| 7 | fieldName | String | - | Yes | Field name | `"status"` |  |
| 8 | statusCode | String | - | Yes | Stable code for the status value, upper case with underscores | `"CREATED"` |  |
| 9 | statusName | String | - | Yes | Status name | `"Created"` |  |
| 10 | description | String | - | Yes | Description of the status definition | `"Order received from ERP and not yet released"` |  |
| 11 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 12 | isInitial | Boolean | - | Yes | True when the record is initial | `true` |  |
| 13 | isFinal | Boolean | - | Yes | True when the record is final | `false` |  |
| 14 | colourCode | String | - | No (null allowed) | Colour code | `"#9E9E9E"` |  |
| 15 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 16 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ collectionName: 1, statusCode: 1 }` | Yes | One definition per collection and status code |

## Referenced by

u_mes_syst_statusTransition, u_mes_syst_recordPolicy.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_statusDefinition.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_statusDefinition.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_statusDefinition.js
