# u_mes_matl_kit

| Property | Value |
|---|---|
| Module | MaterialManagement (matl) |
| Purpose | Kits of components picked for an order / line-side delivery |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 29 (24 required, 5 may be null) |
| Estimated volume per year | ~25,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per kit, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with kitId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_matl_kitLine | Child | line |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1118000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"KIT-2026-000397"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 8 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 10 | kitType | String | - | Yes | Kit type | `"Order Kit"` | Order Kit; Shift Kit; Rework Kit |
| 11 | requiredAt | Date | Datetime | Yes | Date and time when the record was required. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:00:40.000+0000")` |  |
| 12 | toLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id: to location | `"1112000000000006"` | Reference: u_mes_matl_storageLocation._id |
| 13 | toLocationName | String | - | Yes | Display value of toLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side supermarket, assembly 1"` |  |
| 14 | pickedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'picked' | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 15 | pickedBy | String | - | Yes | Display name of the user in pickedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 16 | pickStartedAt | Date | Datetime | No (null allowed) | Pick started date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 17 | pickCompletedAt | Date | Datetime | No (null allowed) | Pick completed date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 18 | deliveredAt | Date | Datetime | No (null allowed) | Date and time when the record was delivered. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 19 | receivedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'received' | `null` | Reference: u_mes_mast_user._id |
| 20 | receivedBy | String | - | No (null allowed) | Display name of the user in receivedById, copied from u_mes_mast_user.fullName | `null` |  |
| 21 | isComplete | Boolean | - | Yes | True when the record is complete | `true` |  |
| 22 | status | String | - | Yes | Primary lifecycle state of the document | `"Requested"` | Requested; Picking; Picked; Delivered; Short |
| 23 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 24 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:40.000+0000")` |  |
| 25 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 26 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 27 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:00:40.000+0000")` |  |
| 28 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 29 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Status values

Requested, Picking, Picked, Delivered, Short. Initial state: Requested. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ toLocationId: 1 }` | No | Look-up of documents by to location |
| 6 | `{ siteId: 1, requiredAt: -1 }` | No | Time-ordered lists and reports by required at |

## Referenced by

u_mes_matl_materialMovement, u_mes_matl_kitLine.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_kit.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_kit.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_kit.js
