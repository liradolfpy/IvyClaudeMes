# u_mes_mast_roleRequiredSkill

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Links one role to one required skill; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_mast_role |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 12 (12 required, 0 may be null) |

## Structure

Relationship collection. A role can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. roleId and roleName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1300000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"OPERATOR-RS01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | roleId | String | - | Yes | Reference to u_mes_mast_role._id: the parent document this one belongs to | `"1026000000000001"` | Reference: u_mes_mast_role._id |
| 7 | roleName | String | - | Yes | Display value of roleId, copied from u_mes_mast_role.name | `"Production Operator"` |  |
| 8 | sequenceNo | Int32 | - | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 9 | requiredSkillId | String | - | Yes | Reference to u_mes_mast_skill._id: required skill | `"1031000000000006"` | Reference: u_mes_mast_skill._id |
| 10 | requiredSkillName | String | - | Yes | Display value of requiredSkillId, copied from u_mes_mast_skill.name | `"Piston and seal assembly"` |  |
| 11 | minimumLevel | Int32 | - | Yes | Minimum skill level required for the role | `NumberInt(2)` |  |
| 12 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ roleId: 1, requiredSkillId: 1 }` | Yes | One link per pair |
| 2 | `{ requiredSkillId: 1, roleId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_roleRequiredSkill.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_roleRequiredSkill.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_roleRequiredSkill.js
