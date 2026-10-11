# u_mes_matl_stockStatus

| Property | Value |
|---|---|
| Module | Material Management (matl) |
| Purpose | Stock statuses (unrestricted, quality inspection, blocked, reserved) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | STS-<recordNo> |
| Display value used by references | name |
| Keys | 11 (10 required, 1 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per stock status, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: STS-<recordNo> | `"STS-UNR"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"UNR"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the stock status; used as its display value in other collections | `"Unrestricted"` |  |
| 6 | description | String | Yes | Description of the stock status | `"Free to use"` |  |
| 7 | isUsable | Boolean | Yes | True when the record is usable | `true` |  |
| 8 | erpStockType | String | No (null allowed) | Stock type the status maps to in ERP | `"Unrestricted-use"` |  |
| 9 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 10 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 11 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_matl_inventoryBalance, u_mes_matl_materialMovement.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_stockStatus.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_stockStatus.js
- Sample document: 03_design/04_material_management/samples/u_mes_matl_stockStatus.js
