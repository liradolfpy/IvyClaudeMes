# u_mes_matl_inventoryBalance

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Stock on hand per item, lot, location and stock status |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 33 (24 required, 9 may be null) |
| Estimated volume per year | ~20,000 live rows |
| Storage | standard |

## Structure

Flat entity collection: one document per inventory balance, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1113000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"INV-2026-000289"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | itemId | String | Yes | Reference to u_mes_prod_item._id | `"1043000000000005"` | Reference: u_mes_prod_item._id |
| 6 | itemName | String | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 7 | lotId | String | No (null allowed) | Reference to u_mes_plan_lot._id | `"1096000000000005"` | Reference: u_mes_plan_lot._id |
| 8 | lotName | String | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260905-PST-007"` |  |
| 9 | storageLocationId | String | Yes | Reference to u_mes_matl_storageLocation._id | `"1112000000000002"` | Reference: u_mes_matl_storageLocation._id |
| 10 | storageLocationName | String | Yes | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Warehouse A, rack 02, bin 14"` |  |
| 11 | containerId | String | No (null allowed) | Reference to u_mes_plan_container._id | `null` | Reference: u_mes_plan_container._id |
| 12 | containerName | String | No (null allowed) | Display value of containerId, copied from u_mes_plan_container.recordNo | `null` |  |
| 13 | stockStatusId | String | Yes | Reference to u_mes_matl_stockStatus._id | `"1280000000000001"` | Reference: u_mes_matl_stockStatus._id |
| 14 | stockStatusName | String | Yes | Display value of stockStatusId, copied from u_mes_matl_stockStatus.name | `"Unrestricted"` |  |
| 15 | quantity | Decimal128 | Yes | Quantity of the inventory balance | `NumberDecimal("1")` |  |
| 16 | reservedQuantity | Decimal128 | Yes | Reserved quantity | `NumberDecimal("0")` |  |
| 17 | unitOfMeasureId | String | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 18 | unitOfMeasureName | String | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 19 | valueInr | Decimal128 | Yes | Value (Indian rupees) | `NumberDecimal("52428.00")` |  |
| 20 | firstReceivedAt | Date | Yes | First received date and time | `ISODate("2026-04-01T18:30:00.000+0000")` |  |
| 21 | lastMovementAt | Date | No (null allowed) | Last movement date and time | `null` |  |
| 22 | lastCountedAt | Date | No (null allowed) | Last counted date and time | `null` |  |
| 23 | lastCountedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'last counted' | `null` | Reference: u_mes_mast_user._id |
| 24 | lastCountedBy | String | No (null allowed) | Display name of the user in lastCountedById, copied from u_mes_mast_user.fullName | `null` |  |
| 25 | expiryAt | Date | No (null allowed) | Expiry date and time | `ISODate("2027-03-31T18:29:59.000+0000")` |  |
| 26 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Closed |
| 27 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 28 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:31:48.000+0000")` |  |
| 29 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 30 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 31 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:31:48.000+0000")` |  |
| 32 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 33 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Status values

Active, Closed. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 5 | `{ storageLocationId: 1 }` | No | Look-up of documents by storage location |
| 6 | `{ containerId: 1 }` | No | Look-up of documents by container |
| 7 | `{ stockStatusId: 1 }` | No | Look-up of documents by stock status |
| 8 | `{ siteId: 1, firstReceivedAt: -1 }` | No | Time-ordered lists and reports by first received at |
| 9 | `{ itemId: 1, lotId: 1, storageLocationId: 1, stockStatus: 1 }` | Yes | One balance row per item, lot, location and stock status |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_inventoryBalance.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_inventoryBalance.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_inventoryBalance.js
