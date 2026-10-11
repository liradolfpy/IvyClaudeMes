# u_mes_matl_inventoryBalance

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Stock on hand per item, lot, location and stock status |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | INV-<recordNo> |
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
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: INV-<recordNo> | `"INV-000482"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"000482"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | itemId | String | Yes | Reference to u_mes_prod_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prod_item._id |
| 6 | itemName | String | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 7 | lotId | String | No (null allowed) | Reference to u_mes_plan_lot._id | `"LOT-L260928-GDC-014"` | Reference: u_mes_plan_lot._id |
| 8 | lotName | String | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260928-GDC-014"` |  |
| 9 | storageLocationId | String | Yes | Reference to u_mes_matl_storageLocation._id | `"LOC-LS-ASY-01"` | Reference: u_mes_matl_storageLocation._id |
| 10 | storageLocationName | String | Yes | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side supermarket, Assembly 1"` |  |
| 11 | containerId | String | No (null allowed) | Reference to u_mes_plan_container._id | `"CNT-BIN-000731"` | Reference: u_mes_plan_container._id |
| 12 | containerName | String | No (null allowed) | Display value of containerId, copied from u_mes_plan_container.recordNo | `"BIN-000731"` |  |
| 13 | stockStatusId | String | Yes | Reference to u_mes_matl_stockStatus._id | `"STS-UNR"` | Reference: u_mes_matl_stockStatus._id |
| 14 | stockStatusName | String | Yes | Display value of stockStatusId, copied from u_mes_matl_stockStatus.name | `"Unrestricted"` |  |
| 15 | quantity | Decimal128 | Yes | Quantity of the inventory balance | `NumberDecimal("1")` |  |
| 16 | reservedQuantity | Decimal128 | Yes | Reserved quantity | `NumberDecimal("0")` |  |
| 17 | unitOfMeasureId | String | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"UOM-EA"` | Reference: u_mes_mast_unitOfMeasure._id |
| 18 | unitOfMeasureName | String | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 19 | valueInr | Decimal128 | Yes | Value (Indian rupees) | `NumberDecimal("52428.00")` |  |
| 20 | firstReceivedAt | Date | Yes | First received date and time | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 21 | lastMovementAt | Date | No (null allowed) | Last movement date and time | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 22 | lastCountedAt | Date | No (null allowed) | Last counted date and time | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 23 | lastCountedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'last counted' | `"USR-10150"` | Reference: u_mes_mast_user._id |
| 24 | lastCountedBy | String | No (null allowed) | Display name of the user in lastCountedById, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 25 | expiryAt | Date | No (null allowed) | Expiry date and time | `ISODate("2027-03-31T18:29:59.000+0000")` |  |
| 26 | status | String | Yes | Primary lifecycle state of the document | `"Closed"` | Active; Closed |
| 27 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 28 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 29 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10150"` | Reference: u_mes_mast_user._id |
| 30 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 31 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 32 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10150"` | Reference: u_mes_mast_user._id |
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
- Sample document: 03_design/04_material_management/samples/u_mes_matl_inventoryBalance.js
