# u_mes_matl_shipmentLine

| Property | Value |
|---|---|
| Module | MaterialManagement (matl) |
| Purpose | One document per line of a shipment |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_matl_shipment |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 19 (19 required, 0 may be null) |

## Structure

Child collection. The parent shipment can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. shipmentId and shipmentName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1128000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SHP-2026-000377-L01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | shipmentId | String | - | Yes | Reference to u_mes_matl_shipment._id: the parent document this one belongs to | `"1127000000000001"` | Reference: u_mes_matl_shipment._id |
| 7 | shipmentName | String | - | Yes | Display value of shipmentId, copied from u_mes_matl_shipment.recordNo | `"SHP-2026-000377"` |  |
| 8 | lineNo | Int32 | - | Yes | Line number within the parent record | `NumberInt(10)` |  |
| 9 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 10 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 11 | customerPartNo | String | - | Yes | Customer part number | `"SM-3501-0421-LH"` |  |
| 12 | quantity | Int32 | - | Yes | Quantity of the shipment line | `NumberInt(480)` |  |
| 13 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 14 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:40.000+0000")` |  |
| 15 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 16 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 17 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:40.000+0000")` |  |
| 18 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 19 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

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
