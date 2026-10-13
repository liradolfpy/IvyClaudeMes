# u_mes_prod_itemRevision

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | One document per revision of a item |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prod_item |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 14 (14 required, 0 may be null) |

## Structure

Child collection. The parent item can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. itemId and itemName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1044000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-R01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | itemId | String | - | Yes | Reference to u_mes_prod_item._id: the parent document this one belongs to | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 7 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | revision | String | - | Yes | Revision of the item revision | `"A"` |  |
| 10 | engineeringChangeId | String | - | Yes | Reference to u_mes_prod_engineeringChange._id | `"1076000000000010"` | Reference: u_mes_prod_engineeringChange._id |
| 11 | engineeringChangeName | String | - | Yes | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `"Work instruction pictures updated for RH variant"` |  |
| 12 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 13 | description | String | - | Yes | Description of the item revision | `"Initial release for production"` |  |
| 14 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ itemId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ engineeringChangeId: 1 }` | No | Look-up of lines by engineering change |

## Referenced by

u_mes_mmr_masterManufacturingRecord.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_itemRevision.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_itemRevision.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_itemRevision.js
