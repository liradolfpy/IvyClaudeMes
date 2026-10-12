# u_mes_matl_replenishmentRule

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Min-max or e-Kanban rule for replenishing an item at a line-side location. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 27 (20 required, 7 may be null) |
| Estimated volume per year | about 300 rows in total |
| Storage | standard collection |

## Structure

Flat entity collection: one document per replenishment rule, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1312000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"RPL-5110-30-0010-LS-ASY-01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000005"` | Reference: u_mes_prod_item._id |
| 6 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 7 | toLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id: to location | `"1112000000000006"` | Reference: u_mes_matl_storageLocation._id |
| 8 | toLocationName | String | - | Yes | Display value of toLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side supermarket, assembly 1"` |  |
| 9 | fromLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id: from location | `"1112000000000002"` | Reference: u_mes_matl_storageLocation._id |
| 10 | fromLocationName | String | - | Yes | Display value of fromLocationId, copied from u_mes_matl_storageLocation.name | `"Warehouse A, rack 02, bin 14"` |  |
| 11 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 12 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 13 | triggerType | String | - | Yes | How replenishment is triggered | `"Kanban Scan"` | Consumption; Kanban Scan; Min-Max; Order Demand |
| 14 | minQuantity | Decimal128 | - | Yes | Minimum quantity | `NumberDecimal("96")` |  |
| 15 | maxQuantity | Decimal128 | - | Yes | Maximum quantity | `NumberDecimal("480")` |  |
| 16 | reorderPointQuantity | Decimal128 | - | Yes | Quantity that triggers a request | `NumberDecimal("192")` |  |
| 17 | kanbanQuantity | Decimal128 | - | No (null allowed) | Quantity per kanban | `NumberDecimal("96")` |  |
| 18 | kanbanCount | Int32 | - | No (null allowed) | Number of kanbans in the loop | `NumberInt(5)` |  |
| 19 | containerTypeId | String | - | No (null allowed) | Reference to u_mes_plan_containerType._id | `"1278000000000002"` | Reference: u_mes_plan_containerType._id |
| 20 | containerTypeName | String | - | No (null allowed) | Display value of containerTypeId, copied from u_mes_plan_containerType.name | `"Returnable Bin 400 x 300"` |  |
| 21 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 22 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 23 | leadTimeMinutes | Int32 | - | Yes | Replenishment lead time | `NumberInt(45)` |  |
| 24 | validFrom | Date | Date | Yes | Valid from (date stored at 00:00:00) | `ISODate("2026-04-01T00:00:00.000+0000")` |  |
| 25 | validTo | Date | Date | No (null allowed) | Valid to | `null` |  |
| 26 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 27 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ toLocationId: 1 }` | No | Look-up of documents by to location |
| 5 | `{ fromLocationId: 1 }` | No | Look-up of documents by from location |
| 6 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 7 | `{ containerTypeId: 1 }` | No | Look-up of documents by container type |

## Referenced by

u_mes_matl_materialRequest.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_replenishmentRule.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_replenishmentRule.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_replenishmentRule.js
