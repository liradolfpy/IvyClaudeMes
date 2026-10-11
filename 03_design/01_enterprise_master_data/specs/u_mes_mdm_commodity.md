# u_mes_mdm_commodity

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Purchasing commodities used to classify suppliers |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | CMD-<recordNo> |
| Display value used by references | name |
| Keys | 9 (9 required, 0 may be null) |
| Estimated volume per year | 10-50 |
| Storage | standard |

## Structure

Flat entity collection: one document per commodity, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: CMD-<recordNo> | `"CMD-MACH-STEEL"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"MACH-STEEL"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the commodity; used as its display value in other collections | `"Machined Steel Parts"` |  |
| 6 | description | String | Yes | Description of the commodity | `"Machined Steel Parts"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 9 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |

## Referenced by

u_mes_mdm_supplier.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_commodity.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_commodity.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_commodity.js
