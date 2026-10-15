# u_mes_matl_storageLocationAllowedItem

| Property | Value |
|---|---|
| Module | MaterialManagement (matl) |
| Purpose | Links one storage location to one allowed item; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_matl_storageLocation |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 13 (9 required, 4 may be null) |

## Structure

Relationship collection. A storage location can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. storageLocationId and storageLocationName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1343000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"LS-ASY-01-AI01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | storageLocationId | String | - | Yes | Reference to u_mes_matl_storageLocation._id: the parent document this one belongs to | `"1112000000000006"` | Reference: u_mes_matl_storageLocation._id |
| 7 | storageLocationName | String | - | Yes | Display value of storageLocationId, copied from u_mes_matl_storageLocation.name | `"Line-side supermarket, assembly 1"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | itemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id | `"1043000000000005"` | Reference: u_mes_prod_item._id |
| 10 | itemName | String | - | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `"Piston, dia 54 mm, steel, chrome plated"` |  |
| 11 | itemGroupId | String | - | No (null allowed) | Reference to u_mes_prod_itemGroup._id | `null` | Reference: u_mes_prod_itemGroup._id |
| 12 | itemGroupName | String | - | No (null allowed) | Display value of itemGroupId, copied from u_mes_prod_itemGroup.name | `null` |  |
| 13 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ storageLocationId: 1, itemId: 1 }` | Yes | One link per pair |
| 2 | `{ itemId: 1, storageLocationId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/04_material_management/validators/u_mes_matl_storageLocationAllowedItem.json
- Indexes: 03_design/04_material_management/indexes/u_mes_matl_storageLocationAllowedItem.js
- Sample documents (10): 03_design/04_material_management/samples/u_mes_matl_storageLocationAllowedItem.js
