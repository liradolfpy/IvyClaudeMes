# u_mes_sys_enumerationValue

| Property | Value |
|---|---|
| Module | Integration and system (sys) |
| Purpose | Allowed values of fixed enumeration keys, one document per collection, key and value |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | ENV-<recordNo> |
| Display value used by references | valueName |
| Keys | 13 (13 required, 0 may be null) |

## Structure

Flat entity collection: one document per enumeration value, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: ENV-<recordNo> | `"ENV-operationExecution.result.OK"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"operationExecution.result.OK"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | collectionName | String | Yes | Collection name | `"u_mes_exe_operationExecution"` |  |
| 6 | fieldName | String | Yes | Field name | `"result"` |  |
| 7 | valueCode | String | Yes | Stable code of the enumeration value | `"OK"` |  |
| 8 | valueName | String | Yes | Display text of the enumeration value | `"OK"` |  |
| 9 | description | String | Yes | Description of the enumeration value | `"Operation finished within all limits"` |  |
| 10 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 11 | isDefault | Boolean | Yes | True when the record is default | `true` |  |
| 12 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 13 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_integration_system/validators/u_mes_sys_enumerationValue.json
- Indexes: 03_design/09_integration_system/indexes/u_mes_sys_enumerationValue.js
- Sample document: 03_design/09_integration_system/samples/u_mes_sys_enumerationValue.js
