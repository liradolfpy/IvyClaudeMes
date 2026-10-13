# u_mes_syst_operatorApp

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Composable operator screen definitions (versioned) bound to work centres and operations |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 18 (10 required, 8 may be null) |
| Estimated volume per year | 50-300 |
| Storage | standard |

## Structure

Flat entity collection: one document per operator app, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with operatorAppId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_syst_operatorAppWorkCenter | Relationship | work center |
| u_mes_syst_operatorAppOperation | Relationship | operation |
| u_mes_syst_operatorAppStep | Child | step |
| u_mes_syst_operatorAppStepTrigger | Child | (below u_mes_syst_operatorAppStep) trigger |
| u_mes_syst_operatorAppDeviceBinding | Child | device binding |
| u_mes_syst_operatorAppLanguage | Relationship | language |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1233000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"APP-GDC-01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the operator app; used as its display value in other collections | `"Operator app, Gravity Die Casting Cell 1"` |  |
| 7 | appType | String | - | Yes | App type | `"Operator Station"` | Operator Station; Inspection; Material Handling; Maintenance; Andon Board |
| 8 | version | Int32 | - | Yes | Version of the operator app | `NumberInt(1)` |  |
| 9 | publishedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'published' | `null` | Reference: u_mes_mast_user._id |
| 10 | publishedBy | String | - | No (null allowed) | Display name of the user in publishedById, copied from u_mes_mast_user.fullName | `null` |  |
| 11 | publishedAt | Date | Datetime | No (null allowed) | Date and time when the record was published. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 12 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `null` | Reference: u_mes_mast_user._id |
| 13 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 14 | approvedAt | Date | Datetime | No (null allowed) | Date and time when the record was approved. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 15 | previousVersionOperatorAppId | String | - | No (null allowed) | Reference to u_mes_syst_operatorApp._id: previous version operator app | `null` | Reference: u_mes_syst_operatorApp._id |
| 16 | previousVersionOperatorAppName | String | - | No (null allowed) | Display value of previousVersionOperatorAppId, copied from u_mes_syst_operatorApp.name | `null` |  |
| 17 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 18 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ previousVersionOperatorAppId: 1 }` | No | Look-up of documents by previous version operator app |

## Referenced by

u_mes_syst_operatorApp, u_mes_syst_operatorAppWorkCenter, u_mes_syst_operatorAppOperation, u_mes_syst_operatorAppStep, u_mes_syst_operatorAppDeviceBinding, u_mes_syst_operatorAppLanguage.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_operatorApp.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_operatorApp.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_operatorApp.js
