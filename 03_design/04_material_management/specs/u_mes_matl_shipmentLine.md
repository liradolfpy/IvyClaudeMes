# u_mes_matl_shipmentLine

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | One document per line of a shipment |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_matl_shipment |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 18 (18 required, 0 may be null) |

## Structure

Child collection. The parent shipment can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. shipmentId and shipmentName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1128000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"SHP-2026-000377-L01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | shipmentId | String | Yes | Reference to u_mes_matl_shipment._id: the parent document this one belongs to | `"1127000000000001"` | Reference: u_mes_matl_shipment._id |
| 6 | shipmentName | String | Yes | Display value of shipmentId, copied from u_mes_matl_shipment.recordNo | `"SHP-2026-000377"` |  |
| 7 | lineNo | Int32 | Yes | Line number within the parent record | `NumberInt(10)` |  |
| 8 | itemId | String | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 10 | customerPartNo | String | Yes | Customer part number | `"SM-3501-0421-LH"` |  |
| 11 | quantity | Int32 | Yes | Quantity of the shipment line | `NumberInt(480)` |  |
| 12 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 13 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:33:40.000+0000")` |  |
| 14 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 15 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 16 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:33:40.000+0000")` |  |
| 17 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 18 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ shipmentId: 1, lineNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ itemId: 1 }` | No | Look-up of lines by item |

## Referenced by

u_mes_matl_shipmentLineContainer, u_mes_matl_shipmentLineLot.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_shipmentLine.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_shipmentLine.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_shipmentLine.js
