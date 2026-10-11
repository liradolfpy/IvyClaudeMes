# u_mes_matl_kit

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Kits of components picked for an order / line-side delivery |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | KIT-<recordNo> |
| Display value used by references | recordNo |
| Keys | 28 (23 required, 5 may be null) |
| Estimated volume per year | ~25,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per kit, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with kitId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_matl_kitLine | Child | line |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: KIT-<recordNo> | `"KIT-20260929-0007"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-0007"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productionOrderId | String | Yes | Reference to u_mes_plan_productionOrder._id | `"PO-1000412"` | Reference: u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"1000412"` |  |
| 7 | workCenterId | String | Yes | Reference to u_mes_mast_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mast_workCenter._id |
| 8 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 9 | kitType | String | Yes | Kit type | `"Order Kit"` | Order Kit; Shift Kit; Rework Kit |
| 10 | requiredAt | Date | Yes | Date and time when the record was required | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 11 | toLocationId | String | Yes | Reference to u_mes_matl_storageLocation._id: to location | `"LOC-LS-ASY-01"` | Reference: u_mes_matl_storageLocation._id |
| 12 | toLocationName | String | Yes | Display value of toLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side supermarket, Assembly 1"` |  |
| 13 | pickedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'picked' | `"USR-10150"` | Reference: u_mes_mast_user._id |
| 14 | pickedBy | String | Yes | Display name of the user in pickedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 15 | pickStartedAt | Date | No (null allowed) | Pick started date and time | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 16 | pickCompletedAt | Date | No (null allowed) | Pick completed date and time | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 17 | deliveredAt | Date | No (null allowed) | Date and time when the record was delivered | `ISODate("2026-09-29T03:45:00.000+0000")` |  |
| 18 | receivedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'received' | `"USR-10150"` | Reference: u_mes_mast_user._id |
| 19 | receivedBy | String | No (null allowed) | Display name of the user in receivedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 20 | isComplete | Boolean | Yes | True when the record is complete | `true` |  |
| 21 | status | String | Yes | Primary lifecycle state of the document | `"Delivered"` | Requested; Picking; Picked; Delivered; Short |
| 22 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 23 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 24 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10150"` | Reference: u_mes_mast_user._id |
| 25 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 26 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-10-01T00:30:00.000+0000")` |  |
| 27 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10150"` | Reference: u_mes_mast_user._id |
| 28 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

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
- Sample document: 03_design/04_material_management/samples/u_mes_matl_kit.js
