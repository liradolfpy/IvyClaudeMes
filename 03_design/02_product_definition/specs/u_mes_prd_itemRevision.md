# u_mes_prd_itemRevision

| Property | Value |
|---|---|
| Module | Product definition (prd) |
| Purpose | One document per revision of a item |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_prd_item |
| _id pattern | <itemId>-R<nnn> |
| Display value used by references | description |
| Keys | 13 (13 required, 0 may be null) |

## Structure

Child collection. The parent item can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. itemId and itemName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <itemId>-R<nnn> | `"ITM-5110-10-0100-R001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-R001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | itemId | String | Yes | Reference to u_mes_prd_item._id: the parent document this one belongs to | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 6 | itemName | String | Yes | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | revision | String | Yes | Revision of the item revision | `"D"` |  |
| 9 | engineeringChangeId | String | Yes | Reference to u_mes_prd_engineeringChange._id | `"ECN-2026-0031"` | Reference: u_mes_prd_engineeringChange._id |
| 10 | engineeringChangeName | String | Yes | Display value of engineeringChangeId, copied from u_mes_prd_engineeringChange.title | `"Bleed screw torque window revised"` |  |
| 11 | effectiveFrom | Date | Yes | Effective from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 12 | description | String | Yes | Description of the item revision | `"Bleed screw torque window revised to 14 +/- 2 N.m"` |  |
| 13 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ itemId: 1, sequenceNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ engineeringChangeId: 1 }` | No | Look-up of lines by engineering change |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prd_itemRevision.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prd_itemRevision.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prd_itemRevision.js
