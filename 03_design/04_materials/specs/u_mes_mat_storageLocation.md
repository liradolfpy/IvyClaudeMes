# u_mes_mat_storageLocation

| Property | Value |
|---|---|
| Module | Materials (mat) |
| Purpose | Warehouses, racks, line-side supermarkets, quarantine cage, dispatch bay |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | LOC-<recordNo> |
| Display value used by references | name |
| Keys | 24 (16 required, 8 may be null) |
| Estimated volume per year | 500-5,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per storage location, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: LOC-<recordNo> | `"LOC-LS-ASY-01"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"LS-ASY-01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the storage location; used as its display value in other collections | `"Line-side supermarket, Assembly 1"` |  |
| 6 | locationType | String | Yes | Location type | `"Line Side"` | Warehouse Rack; Line Side; Quarantine; Dispatch Bay; Receiving Bay; Tool Crib; Scrap Yard |
| 7 | areaId | String | No (null allowed) | Reference to u_mes_mdm_area._id | `"AR-ASY"` | Reference: u_mes_mdm_area._id |
| 8 | areaName | String | No (null allowed) | Display value of areaId, copied from u_mes_mdm_area.name | `"Assembly and Test"` |  |
| 9 | workCenterId | String | No (null allowed) | Reference to u_mes_mdm_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 10 | workCenterName | String | No (null allowed) | Display value of workCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 11 | parentLocationId | String | No (null allowed) | Reference to u_mes_mat_storageLocation._id: parent location | `"LOC-WH-A-R02-B14"` | Reference: u_mes_mat_storageLocation._id |
| 12 | parentLocationName | String | No (null allowed) | Display value of parentLocationId, copied from u_mes_mat_storageLocation.name | `"Warehouse A, rack 02, bin 14"` |  |
| 13 | zone | String | Yes | Zone of the storage location | `"ASY"` |  |
| 14 | rack | String | No (null allowed) | Rack of the storage location | `"R02"` |  |
| 15 | level | Int32 | Yes | Level number on the scale of the parent record | `NumberInt(3)` |  |
| 16 | bin | String | No (null allowed) | Bin of the storage location | `"B14"` |  |
| 17 | capacityQuantity | Int32 | Yes | CAPAcity quantity | `NumberInt(960)` |  |
| 18 | isQuarantine | Boolean | Yes | True when the record is quarantine | `false` |  |
| 19 | isLineSide | Boolean | Yes | True when the record is line side | `true` |  |
| 20 | mixedLotsAllowed | Boolean | Yes | True when: mixed lots allowed | `false` |  |
| 21 | erpStorageLocation | String | Yes | ERP storage location | `"LS01"` |  |
| 22 | barcode | String | Yes | Barcode of the storage location | `"LOC-LS-ASY-01"` |  |
| 23 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 24 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ areaId: 1 }` | No | Look-up of documents by area |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ parentLocationId: 1 }` | No | Look-up of documents by parent location |

## Referenced by

u_mes_mdm_workCenter, u_mes_prd_item, u_mes_exe_lot, u_mes_exe_container, u_mes_mat_storageLocation, u_mes_mat_inventoryBalance, u_mes_mat_materialMovement, u_mes_mat_goodsReceiptLine, u_mes_mat_kit, u_mes_mat_kitLine, u_mes_mat_materialRequest, u_mes_mat_materialConsumption, u_mes_mat_shipment, u_mes_qlt_scrapRecord, u_mes_qlt_qualityHold, u_mes_qlt_gauge, u_mes_mnt_sparePart, u_mes_mnt_tool.

## Files

- Validator: 03_design/04_materials/validators/u_mes_mat_storageLocation.json
- Indexes: 03_design/04_materials/indexes/u_mes_mat_storageLocation.js
- Sample document: 03_design/04_materials/samples/u_mes_mat_storageLocation.js
