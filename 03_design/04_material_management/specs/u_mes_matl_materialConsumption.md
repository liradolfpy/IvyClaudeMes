# u_mes_matl_materialConsumption

| Property | Value |
|---|---|
| Module | MaterialManagement (matl) |
| Purpose | Component / lot consumed at an operation on a unit or lot (backflush or scanned) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 44 (31 required, 13 may be null) |
| Estimated volume per year | ~8 million |
| Storage | standard, partitioned by month |

## Structure

Flat entity collection: one document per material consumption, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1121000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CON-2026-000311"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | operationExecutionId | String | - | Yes | Reference to u_mes_plan_operationExecution._id | `"1090000000000002"` | Reference: u_mes_plan_operationExecution._id |
| 7 | operationExecutionName | String | - | Yes | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000379"` |  |
| 8 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 9 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 10 | wipUnitId | String | - | No (null allowed) | Reference to u_mes_plan_wipUnit._id | `"1094000000000001"` | Reference: u_mes_plan_wipUnit._id |
| 11 | wipUnitName | String | - | No (null allowed) | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915A0184"` |  |
| 12 | parentLotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id: parent lot | `null` | Reference: u_mes_plan_lot._id |
| 13 | parentLotName | String | - | No (null allowed) | Display value of parentLotId, copied from u_mes_plan_lot.recordNo | `null` |  |
| 14 | componentItemId | String | - | Yes | Reference to u_mes_prod_item._id: component item | `"1043000000000005"` | Reference: u_mes_prod_item._id |
| 15 | componentItemName | String | - | Yes | Display value of componentItemId, copied from u_mes_prod_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 16 | componentLotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id: component lot | `"1096000000000005"` | Reference: u_mes_plan_lot._id |
| 17 | componentLotName | String | - | No (null allowed) | Display value of componentLotId, copied from u_mes_plan_lot.recordNo | `"L260905-PST-007"` |  |
| 18 | componentSerialNo | String | - | No (null allowed) | Component serial number | `null` |  |
| 19 | quantity | Decimal128 | - | Yes | Quantity of the material consumption | `1` |  |
| 20 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 21 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 22 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 23 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 24 | fromLocationId | String | - | No (null allowed) | Reference to u_mes_matl_storageLocation._id: from location | `"1112000000000001"` | Reference: u_mes_matl_storageLocation._id |
| 25 | fromLocationName | String | - | No (null allowed) | Display value of fromLocationId, copied from u_mes_matl_storageLocation.name | `"Raw material yard, ingot bay"` |  |
| 26 | consumptionType | String | - | Yes | Consumption type | `"Scanned"` | Scanned; Backflush; Manual |
| 27 | scanVerified | Boolean | - | Yes | True when: scan verified | `true` |  |
| 28 | consumedAt | Date | Datetime | Yes | Date and time when the record was consumed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:37.000+0000")` |  |
| 29 | consumedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'consumed' | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 30 | consumedBy | String | - | Yes | Display name of the user in consumedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 31 | billOfMaterialId | String | - | No (null allowed) | Reference to u_mes_prod_billOfMaterial._id | `"1047000000000001"` | Reference: u_mes_prod_billOfMaterial._id |
| 32 | billOfMaterialName | String | - | No (null allowed) | Display value of billOfMaterialId, copied from u_mes_prod_billOfMaterial.recordNo | `"BOM-5110-10-0100-01"` |  |
| 33 | bomLineNo | Int32 | - | Yes | BOM line number | `NumberInt(40)` |  |
| 34 | erpPosted | Boolean | - | Yes | True when: ERP posted | `true` |  |
| 35 | erpMessageId | String | - | No (null allowed) | Reference to u_mes_syst_erpMessage._id | `"1229000000000006"` | Reference: u_mes_syst_erpMessage._id |
| 36 | erpMessageName | String | - | No (null allowed) | Display value of erpMessageId, copied from u_mes_syst_erpMessage.recordNo | `"MSG-2026-000168"` |  |
| 37 | status | String | - | Yes | Primary lifecycle state of the document | `"Posted"` | Posted; Reversed |
| 38 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 39 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:07.000+0000")` |  |
| 40 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 41 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 42 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:02:37.000+0000")` |  |
| 43 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 44 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Status values

Posted, Reversed. Initial state: Posted. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ operationExecutionId: 1 }` | No | Look-up of documents by operation execution |
| 4 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 5 | `{ wipUnitId: 1 }` | No | Look-up of documents by wip unit |
| 6 | `{ parentLotId: 1 }` | No | Look-up of documents by parent lot |
| 7 | `{ componentItemId: 1 }` | No | Look-up of documents by component item |
| 8 | `{ siteId: 1, consumedAt: -1 }` | No | Time-ordered lists and reports by consumed at |

## Referenced by

u_mes_trac_genealogyLink.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_materialConsumption.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_materialConsumption.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_materialConsumption.js
