# u_mes_matl_storageLocation

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Warehouses, racks, line-side supermarkets, quarantine cage, dispatch bay |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 24 (16 required, 8 may be null) |
| Estimated volume per year | 500-5,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per storage location, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with storageLocationId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_matl_storageLocationAllowedItem | Relationship | allowed item |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1112000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"WH-RM-01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the storage location; used as its display value in other collections | `"Raw material yard, ingot bay"` |  |
| 6 | locationType | String | - | Yes | Location type | `"Receiving Bay"` | Warehouse Rack; Line Side; Quarantine; Dispatch Bay; Receiving Bay; Tool Crib; Scrap Yard |
| 7 | areaId | String | - | No (null allowed) | Reference to u_mes_mast_area._id | `"1005000000000001"` | Reference: u_mes_mast_area._id |
| 8 | areaName | String | - | No (null allowed) | Display value of areaId, copied from u_mes_mast_area.name | `"Foundry"` |  |
| 9 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 10 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 11 | parentLocationId | String | - | No (null allowed) | Reference to u_mes_matl_storageLocation._id: parent location | `null` | Reference: u_mes_matl_storageLocation._id |
| 12 | parentLocationName | String | - | No (null allowed) | Display value of parentLocationId, copied from u_mes_matl_storageLocation.name | `null` |  |
| 13 | zone | String | - | Yes | Zone of the storage location | `"ASY"` |  |
| 14 | rack | String | - | No (null allowed) | Rack of the storage location | `"R02"` |  |
| 15 | level | Int32 | - | Yes | Level number on the scale of the parent record | `NumberInt(3)` |  |
| 16 | bin | String | - | No (null allowed) | Bin of the storage location | `"B14"` |  |
| 17 | capacityQuantity | Int32 | - | Yes | CAPAcity quantity | `NumberInt(960)` |  |
| 18 | isQuarantine | Boolean | - | Yes | True when the record is quarantine | `false` |  |
| 19 | isLineSide | Boolean | - | Yes | True when the record is line side | `true` |  |
| 20 | mixedLotsAllowed | Boolean | - | Yes | True when: mixed lots allowed | `false` |  |
| 21 | erpStorageLocation | String | - | Yes | ERP storage location | `"LS01"` |  |
| 22 | barcode | String | - | Yes | Barcode of the storage location | `"LOC-LS-ASY-01"` |  |
| 23 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 24 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ areaId: 1 }` | No | Look-up of documents by area |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ parentLocationId: 1 }` | No | Look-up of documents by parent location |

## Referenced by

u_mes_mast_workCenter, u_mes_prod_item, u_mes_plan_lot, u_mes_plan_container, u_mes_matl_storageLocation, u_mes_matl_inventoryBalance, u_mes_matl_materialMovement, u_mes_matl_goodsReceiptLine, u_mes_matl_kit, u_mes_matl_kitLine, u_mes_matl_materialRequest, u_mes_matl_materialConsumption, u_mes_matl_shipment, u_mes_qual_scrapRecord, u_mes_qual_qualityHold, u_mes_qual_gauge, u_mes_maint_sparePart, u_mes_maint_tool, u_mes_matl_exposureTimer, u_mes_matl_replenishmentRule, u_mes_trac_traceInvestigationResult, u_mes_maint_sparePartTransaction, u_mes_matl_storageLocationAllowedItem.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_storageLocation.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_storageLocation.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_storageLocation.js
