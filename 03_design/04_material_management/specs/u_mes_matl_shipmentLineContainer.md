# u_mes_matl_shipmentLineContainer

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Links one shipment line to one container; one document per link |
| Kind | Relationship |
| Data class | Transaction |
| Parent collection | u_mes_matl_shipmentLine |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 16 (16 required, 0 may be null) |

## Structure

Relationship collection. A shipment line can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. shipmentLineId and shipmentLineName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1129000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"SHP-2026-000377-L01-C01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | shipmentLineId | String | Yes | Reference to u_mes_matl_shipmentLine._id: the parent document this one belongs to | `"1128000000000001"` | Reference: u_mes_matl_shipmentLine._id |
| 6 | shipmentLineName | String | Yes | Display value of shipmentLineId, copied from u_mes_matl_shipmentLine.recordNo | `"SHP-2026-000377-L01"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | containerId | String | Yes | Reference to u_mes_plan_container._id | `"1099000000000004"` | Reference: u_mes_plan_container._id |
| 9 | containerName | String | Yes | Display value of containerId, copied from u_mes_plan_container.recordNo | `"BIN-000082"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 11 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:36:40.000+0000")` |  |
| 12 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 13 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |
| 14 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:36:40.000+0000")` |  |
| 15 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000008"` | Reference: u_mes_mast_user._id |
| 16 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Vikram Pawar"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ shipmentLineId: 1, containerId: 1 }` | Yes | One link per pair |
| 2 | `{ containerId: 1, shipmentLineId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_shipmentLineContainer.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_shipmentLineContainer.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_shipmentLineContainer.js
