# u_mes_syst_enumerationValue

| Property | Value |
|---|---|
| Module | SystemAndIntegration (syst) |
| Purpose | Allowed values of fixed enumeration keys, one document per collection, key and value |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | valueName |
| Keys | 14 (14 required, 0 may be null) |

## Structure

Flat entity collection: one document per enumeration value, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1298000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"operationExecution.result.OK"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | collectionName | String | - | Yes | Collection name | `"u_mes_plan_operationExecution"` |  |
| 7 | fieldName | String | - | Yes | Field name | `"result"` |  |
| 8 | valueCode | String | - | Yes | Stable code of the enumeration value | `"OK"` |  |
| 9 | valueName | String | - | Yes | Display text of the enumeration value | `"OK"` |  |
| 10 | description | String | - | Yes | Description of the enumeration value | `"Operation finished within all limits"` |  |
| 11 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 12 | isDefault | Boolean | - | Yes | True when the record is default | `true` |  |
| 13 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 14 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_enumerationValue.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_enumerationValue.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_enumerationValue.js
