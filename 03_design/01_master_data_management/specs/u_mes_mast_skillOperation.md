# u_mes_mast_skillOperation

| Property | Value |
|---|---|
| Module | MasterDataManagement (mast) |
| Purpose | Links one skill to one operation; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_mast_skill |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 11 (11 required, 0 may be null) |

## Structure

Relationship collection. A skill can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. skillId and skillName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1032000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"GDC-OP-O01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | skillId | String | - | Yes | Reference to u_mes_mast_skill._id: the parent document this one belongs to | `"1031000000000001"` | Reference: u_mes_mast_skill._id |
| 7 | skillName | String | - | Yes | Display value of skillId, copied from u_mes_mast_skill.name | `"Gravity die casting operation"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | operationId | String | - | Yes | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 10 | operationName | String | - | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 11 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ skillId: 1, operationId: 1 }` | Yes | One link per pair |
| 2 | `{ operationId: 1, skillId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_skillOperation.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_skillOperation.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_skillOperation.js
