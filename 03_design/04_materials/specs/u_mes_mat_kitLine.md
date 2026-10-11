# u_mes_mat_kitLine

| Property | Value |
|---|---|
| Module | Materials (mat) |
| Purpose | One document per line of a kit |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_mat_kit |
| _id pattern | <kitId>-L<nnn> |
| Display value used by references | recordNo |
| Keys | 23 (19 required, 4 may be null) |

## Structure

Child collection. The parent kit can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. kitId and kitName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <kitId>-L<nnn> | `"KIT-20260929-0007-L001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-0007-L001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | kitId | String | Yes | Reference to u_mes_mat_kit._id: the parent document this one belongs to | `"KIT-20260929-0007"` | Reference: u_mes_mat_kit._id |
| 6 | kitName | String | Yes | Display value of kitId, copied from u_mes_mat_kit.recordNo | `"20260929-0007"` |  |
| 7 | lineNo | Int32 | Yes | Line number within the parent record | `NumberInt(10)` |  |
| 8 | itemId | String | Yes | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 9 | itemName | String | Yes | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 10 | lotId | String | No (null allowed) | Reference to u_mes_exe_lot._id | `"LOT-L260928-GDC-014"` | Reference: u_mes_exe_lot._id |
| 11 | lotName | String | No (null allowed) | Display value of lotId, copied from u_mes_exe_lot.recordNo | `"L260928-GDC-014"` |  |
| 12 | requiredQuantity | Decimal128 | Yes | Required quantity | `NumberDecimal("480")` |  |
| 13 | pickedQuantity | Decimal128 | Yes | Picked quantity | `NumberDecimal("480")` |  |
| 14 | fromLocationId | String | No (null allowed) | Reference to u_mes_mat_storageLocation._id: from location | `"LOC-WH-A-R02-B14"` | Reference: u_mes_mat_storageLocation._id |
| 15 | fromLocationName | String | No (null allowed) | Display value of fromLocationId, copied from u_mes_mat_storageLocation.name | `"Warehouse A, rack 02, bin 14"` |  |
| 16 | shortQuantity | Decimal128 | Yes | Short quantity | `NumberDecimal("0")` |  |
| 17 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 18 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 19 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10150"` | Reference: u_mes_mdm_user._id |
| 20 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Vikram Pawar"` |  |
| 21 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 22 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10150"` | Reference: u_mes_mdm_user._id |
| 23 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Vikram Pawar"` |  |

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

- Validator: 03_design/04_materials/validators/u_mes_mat_kitLine.json
- Indexes: 03_design/04_materials/indexes/u_mes_mat_kitLine.js
- Sample document: 03_design/04_materials/samples/u_mes_mat_kitLine.js
