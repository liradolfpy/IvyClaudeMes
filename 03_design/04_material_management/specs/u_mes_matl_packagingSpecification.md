# u_mes_matl_packagingSpecification

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Pack instruction: container type, quantity per bin, layers, dunnage, label template |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 28 (23 required, 5 may be null) |
| Estimated volume per year | 100-500 |
| Storage | standard |

## Structure

Flat entity collection: one document per packaging specification, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with packagingSpecificationId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_matl_packagingSpecificationLevel | Child | level |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1122000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PKS-5110-10-0100-SML-01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 6 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 7 | customerId | String | - | Yes | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 8 | customerName | String | - | Yes | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 9 | version | Int32 | - | Yes | Version of the packaging specification | `NumberInt(1)` |  |
| 10 | containerTypeId | String | - | Yes | Reference to u_mes_plan_containerType._id | `"1278000000000001"` | Reference: u_mes_plan_containerType._id |
| 11 | containerTypeName | String | - | Yes | Display value of containerTypeId, copied from u_mes_plan_containerType.name | `"Returnable Bin 600 x 400"` |  |
| 12 | quantityPerContainer | Int32 | - | Yes | Quantity per container | `NumberInt(24)` |  |
| 13 | dunnage | String | - | No (null allowed) | Dunnage of the packaging specification | `"Moulded tray, 8 pockets per layer"` |  |
| 14 | vciRequired | Boolean | - | Yes | True when: vci required | `false` |  |
| 15 | layersPerContainer | Int32 | - | Yes | Layers per container | `NumberInt(3)` |  |
| 16 | unitsPerLayer | Int32 | - | Yes | Units per layer | `NumberInt(8)` |  |
| 17 | containersPerPallet | Int32 | - | Yes | Containers per pallet | `NumberInt(12)` |  |
| 18 | maxGrossWeightKg | Decimal128 | - | Yes | Maximum gross weight (kg) | `NumberDecimal("95.0")` |  |
| 19 | unitLabelTemplateId | String | - | Yes | Reference to u_mes_matl_labelTemplate._id: unit label template | `"1124000000000001"` | Reference: u_mes_matl_labelTemplate._id |
| 20 | unitLabelTemplateName | String | - | Yes | Display value of unitLabelTemplateId, copied from u_mes_matl_labelTemplate.name | `"Sahyadri Motors bin label A5"` |  |
| 21 | containerLabelTemplateId | String | - | No (null allowed) | Reference to u_mes_matl_labelTemplate._id: container label template | `"1124000000000001"` | Reference: u_mes_matl_labelTemplate._id |
| 22 | containerLabelTemplateName | String | - | No (null allowed) | Display value of containerLabelTemplateId, copied from u_mes_matl_labelTemplate.name | `"Sahyadri Motors bin label A5"` |  |
| 23 | instructionControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: instruction controlled document | `"1246000000000010"` | Reference: u_mes_syst_controlledDocument._id |
| 24 | instructionControlledDocumentName | String | - | No (null allowed) | Display value of instructionControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"Drawing 5110-10-0100 revision D, Front Brake Caliper Assembly LH"` |  |
| 25 | approvedByCustomer | Boolean | - | Yes | True when: approved by customer | `true` |  |
| 26 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 27 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 28 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ customerId: 1 }` | No | Look-up of documents by customer |
| 5 | `{ containerTypeId: 1 }` | No | Look-up of documents by container type |
| 6 | `{ unitLabelTemplateId: 1 }` | No | Look-up of documents by unit label template |
| 7 | `{ containerLabelTemplateId: 1 }` | No | Look-up of documents by container label template |

## Referenced by

u_mes_plan_container, u_mes_matl_packagingSpecificationLevel, u_mes_mmr_masterManufacturingRecord.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_packagingSpecification.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_packagingSpecification.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_packagingSpecification.js
