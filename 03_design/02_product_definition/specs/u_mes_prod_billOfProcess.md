# u_mes_prod_billOfProcess

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | Per routing step: required equipment, tools, recipe, work instruction, data collection, consumed components, cycle time |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 19 (13 required, 6 may be null) |
| Estimated volume per year | 500-3,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per bill of process, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with billOfProcessId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_prod_billOfProcessStep | Child | step |
| u_mes_prod_billOfProcessStepEquipment | Relationship | (below u_mes_prod_billOfProcessStep) equipment |
| u_mes_prod_billOfProcessStepTool | Relationship | (below u_mes_prod_billOfProcessStep) tool |
| u_mes_prod_billOfProcessStepRequiredSkill | Relationship | (below u_mes_prod_billOfProcessStep) required skill |
| u_mes_prod_billOfProcessStepConsumedComponent | Child | (below u_mes_prod_billOfProcessStep) consumed component |
| u_mes_prod_billOfProcessStepInterlock | Child | (below u_mes_prod_billOfProcessStep) interlock |
| u_mes_prod_billOfProcessStepProcessParameter | Child | (below u_mes_prod_billOfProcessStep) process parameter |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1057000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"BOP-5110-10-0100-R01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 6 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 7 | itemRevision | String | - | Yes | Item revision | `"D"` |  |
| 8 | routingId | String | - | Yes | Reference to u_mes_prod_routing._id | `"1053000000000001"` | Reference: u_mes_prod_routing._id |
| 9 | routingName | String | - | Yes | Display value of routingId, copied from u_mes_prod_routing.description | `"Front caliper LH, full process routing"` |  |
| 10 | bopVersion | Int32 | - | Yes | BOP version | `NumberInt(1)` |  |
| 11 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 12 | effectiveTo | Date | Date | No (null allowed) | Effective to. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2027-03-31T00:00:00.000+0000")` |  |
| 13 | billOfMaterialId | String | - | No (null allowed) | Reference to u_mes_prod_billOfMaterial._id | `"1047000000000001"` | Reference: u_mes_prod_billOfMaterial._id |
| 14 | billOfMaterialName | String | - | No (null allowed) | Display value of billOfMaterialId, copied from u_mes_prod_billOfMaterial.recordNo | `"BOM-5110-10-0100-01"` |  |
| 15 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `null` | Reference: u_mes_mast_user._id |
| 16 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 17 | approvedAt | Date | Datetime | No (null allowed) | Date and time when the record was approved. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 18 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 19 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ routingId: 1 }` | No | Look-up of documents by routing |
| 5 | `{ billOfMaterialId: 1 }` | No | Look-up of documents by bill of material |

## Referenced by

u_mes_prod_billOfProcessStep.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_billOfProcess.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_billOfProcess.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_billOfProcess.js
