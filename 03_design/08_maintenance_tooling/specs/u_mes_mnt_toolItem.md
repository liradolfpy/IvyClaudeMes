# u_mes_mnt_toolItem

| Property | Value |
|---|---|
| Module | Maintenance and tooling (mnt) |
| Purpose | Links one tool to one item; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_mnt_tool |
| _id pattern | <toolId>-I<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A tool can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. toolId and toolName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <toolId>-I<nnn> | `"TL-SKT-10-0007-I001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"SKT-10-0007-I001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | toolId | String | Yes | Reference to u_mes_mnt_tool._id: the parent document this one belongs to | `"TL-SKT-10-0007"` | Reference: u_mes_mnt_tool._id |
| 6 | toolName | String | Yes | Display value of toolId, copied from u_mes_mnt_tool.name | `"Nutrunner socket 10 mm, torque station 1"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | itemId | String | Yes | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 9 | itemName | String | Yes | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ toolId: 1, itemId: 1 }` | Yes | One link per pair |
| 2 | `{ itemId: 1, toolId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/08_maintenance_tooling/validators/u_mes_mnt_toolItem.json
- Indexes: 03_design/08_maintenance_tooling/indexes/u_mes_mnt_toolItem.js
- Sample document: 03_design/08_maintenance_tooling/samples/u_mes_mnt_toolItem.js
