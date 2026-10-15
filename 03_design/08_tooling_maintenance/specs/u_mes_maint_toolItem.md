# u_mes_maint_toolItem

| Property | Value |
|---|---|
| Module | Tooling And Maintenance (maint) |
| Purpose | Links one tool to one item; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_maint_tool |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 11 (11 required, 0 may be null) |

## Structure

Relationship collection. A tool can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. toolId and toolName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1227000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"DIE-5110-LH-02-I01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | toolId | String | - | Yes | Reference to u_mes_maint_tool._id: the parent document this one belongs to | `"1226000000000001"` | Reference: u_mes_maint_tool._id |
| 7 | toolName | String | - | Yes | Display value of toolId, copied from u_mes_maint_tool.name | `"Gravity die, caliper body LH, die 2"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 10 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 11 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ toolId: 1, itemId: 1 }` | Yes | One link per pair |
| 2 | `{ itemId: 1, toolId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_tooling_maintenance/validators/u_mes_maint_toolItem.json
- Indexes: 03_design/08_tooling_maintenance/indexes/u_mes_maint_toolItem.js
- Sample documents (10): 03_design/08_tooling_maintenance/samples/u_mes_maint_toolItem.js
