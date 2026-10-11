# u_mes_prd_billOfMaterial

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | Multi-level bills of material per item revision with effectivity |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | BOM-<recordNo> |
| Display value used by references | recordNo |
| Keys | 22 (16 required, 6 may be null) |
| Estimated volume per year | 500-3,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per bill of material, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with billOfMaterialId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_prd_billOfMaterialComponent | Child | component |
| u_mes_prd_billOfMaterialComponentProductVariant | Relationship | (below u_mes_prd_billOfMaterialComponent) product variant |
| u_mes_prd_billOfMaterialComponentAlternateItem | Relationship | (below u_mes_prd_billOfMaterialComponent) alternate item |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: BOM-<recordNo> | `"BOM-5110-10-0100-D-01"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-D-01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | itemId | String | Yes | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 6 | itemName | String | Yes | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 7 | itemRevision | String | Yes | Item revision | `"D"` |  |
| 8 | bomVersion | Int32 | Yes | BOM version | `NumberInt(1)` |  |
| 9 | bomType | String | Yes | BOM type | `"Production"` | Production; Engineering; Rework |
| 10 | baseQuantity | Decimal128 | Yes | Base quantity | `NumberDecimal("1")` |  |
| 11 | baseUnitOfMeasureId | String | Yes | Reference to u_mes_mdm_unitOfMeasure._id: base unit of measure | `"UOM-EA"` | Reference: u_mes_mdm_unitOfMeasure._id |
| 12 | baseUnitOfMeasureName | String | Yes | Display value of baseUnitOfMeasureId, copied from u_mes_mdm_unitOfMeasure.name | `"Each"` |  |
| 13 | effectiveFrom | Date | Yes | Effective from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 14 | effectiveTo | Date | No (null allowed) | Effective to (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2027-03-31T18:29:59.000+0000")` |  |
| 15 | engineeringChangeId | String | No (null allowed) | Reference to u_mes_prd_engineeringChange._id | `"ECN-2026-0031"` | Reference: u_mes_prd_engineeringChange._id |
| 16 | engineeringChangeName | String | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prd_engineeringChange.title | `"Bleed screw torque window revised"` |  |
| 17 | approvedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'approved' | `"USR-10019"` | Reference: u_mes_mdm_user._id |
| 18 | approvedBy | String | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mdm_user.fullName | `"Meera Deshpande"` |  |
| 19 | approvedAt | Date | No (null allowed) | Date and time when the record was approved | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 20 | erpBomNo | String | Yes | ERP BOM number | `"00051101-01"` |  |
| 21 | status | String | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 22 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ baseUnitOfMeasureId: 1 }` | No | Look-up of documents by base unit of measure |
| 5 | `{ engineeringChangeId: 1 }` | No | Look-up of documents by engineering change |

## Referenced by

u_mes_prd_billOfMaterialComponent, u_mes_prd_billOfProcess, u_mes_exe_productionOrder, u_mes_mat_materialConsumption.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_billOfMaterial.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_billOfMaterial.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_billOfMaterial.js
