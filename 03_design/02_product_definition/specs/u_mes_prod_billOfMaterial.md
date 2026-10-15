# u_mes_prod_billOfMaterial

| Property | Value |
|---|---|
| Module | ProductDefinition (prod) |
| Purpose | Multi-level bills of material per item revision with effectivity |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 23 (17 required, 6 may be null) |
| Estimated volume per year | 500-3,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per bill of material, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with billOfMaterialId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_prod_billOfMaterialComponent | Child | component |
| u_mes_prod_billOfMaterialComponentProductVariant | Relationship | (below u_mes_prod_billOfMaterialComponent) product variant |
| u_mes_prod_billOfMaterialComponentAlternateItem | Relationship | (below u_mes_prod_billOfMaterialComponent) alternate item |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1047000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"BOM-5110-10-0100-01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 7 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 8 | itemRevision | String | - | Yes | Item revision | `"D"` |  |
| 9 | bomVersion | Int32 | - | Yes | BOM version | `NumberInt(1)` |  |
| 10 | bomType | String | - | Yes | BOM type | `"Production"` | Production; Engineering; Rework |
| 11 | baseQuantity | Decimal128 | - | Yes | Base quantity | `NumberDecimal("1")` |  |
| 12 | baseUnitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id: base unit of measure | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 13 | baseUnitOfMeasureName | String | - | Yes | Display value of baseUnitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 14 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 15 | effectiveTo | Date | Date | No (null allowed) | Effective to. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2027-03-31T00:00:00.000+0000")` |  |
| 16 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `"1076000000000010"` | Reference: u_mes_prod_engineeringChange._id |
| 17 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `"Work instruction pictures updated for RH variant"` |  |
| 18 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `null` | Reference: u_mes_mast_user._id |
| 19 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 20 | approvedAt | Date | Datetime | No (null allowed) | Date and time when the record was approved. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 21 | erpBomNo | String | - | Yes | ERP BOM number | `"00051101-01"` |  |
| 22 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 23 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ baseUnitOfMeasureId: 1 }` | No | Look-up of documents by base unit of measure |
| 5 | `{ engineeringChangeId: 1 }` | No | Look-up of documents by engineering change |

## Referenced by

u_mes_prod_billOfMaterialComponent, u_mes_prod_billOfProcess, u_mes_plan_productionOrder, u_mes_matl_materialConsumption, u_mes_mmr_masterManufacturingRecord.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_billOfMaterial.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_billOfMaterial.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_billOfMaterial.js
