# u_mes_matl_kitLine

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | One document per line of a kit |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_matl_kit |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 23 (19 required, 4 may be null) |

## Structure

Child collection. The parent kit can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. kitId and kitName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1119000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"KIT-2026-000397-L01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | kitId | String | Yes | Reference to u_mes_matl_kit._id: the parent document this one belongs to | `"1118000000000001"` | Reference: u_mes_matl_kit._id |
| 6 | kitName | String | Yes | Display value of kitId, copied from u_mes_matl_kit.recordNo | `"KIT-2026-000397"` |  |
| 7 | lineNo | Int32 | Yes | Line number within the parent record | `NumberInt(10)` |  |
| 8 | itemId | String | Yes | Reference to u_mes_prod_item._id | `"1043000000000005"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 10 | lotId | String | No (null allowed) | Reference to u_mes_plan_lot._id | `"1096000000000005"` | Reference: u_mes_plan_lot._id |
| 11 | lotName | String | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260905-PST-007"` |  |
| 12 | requiredQuantity | Decimal128 | Yes | Required quantity | `NumberDecimal("480")` |  |
| 13 | pickedQuantity | Decimal128 | Yes | Picked quantity | `NumberDecimal("480")` |  |
| 14 | fromLocationId | String | No (null allowed) | Reference to u_mes_matl_storageLocation._id: from location | `"1112000000000001"` | Reference: u_mes_matl_storageLocation._id |
| 15 | fromLocationName | String | No (null allowed) | Display value of fromLocationId, copied from u_mes_matl_storageLocation.name | `"Raw material yard, ingot bay"` |  |
| 16 | shortQuantity | Decimal128 | Yes | Short quantity | `NumberDecimal("0")` |  |
| 17 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 18 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:31:48.000+0000")` |  |
| 19 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 20 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 21 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:31:48.000+0000")` |  |
| 22 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 23 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ kitId: 1, lineNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ itemId: 1 }` | No | Look-up of lines by item |
| 3 | `{ lotId: 1 }` | No | Look-up of lines by lot |
| 4 | `{ fromLocationId: 1 }` | No | Look-up of lines by from location |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_kitLine.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_kitLine.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_kitLine.js
