# u_mes_mast_skillLevelScale

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | One document per level scale of a skill |
| Kind | Child |
| Data class | Master |
| Parent collection | u_mes_mast_skill |
| _id pattern | <skillId>-LS<nnn> |
| Display value used by references | description |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Child collection. The parent skill can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. skillId and skillName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <skillId>-LS<nnn> | `"SKL-LEAK-TEST-OP-LS001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"LEAK-TEST-OP-LS001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | skillId | String | Yes | Reference to u_mes_mast_skill._id: the parent document this one belongs to | `"SKL-LEAK-TEST-OP"` | Reference: u_mes_mast_skill._id |
| 6 | skillName | String | Yes | Display value of skillId, copied from u_mes_mast_skill.name | `"Leak Test Operation"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | level | Int32 | Yes | Level number on the scale of the parent record | `NumberInt(3)` |  |
| 9 | description | String | Yes | Description of the skill level scale | `"Works independently to standard and can react to abnormalities"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ skillId: 1, level: 1 }` | Yes | Lines of one parent in order; one line per number |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_skillLevelScale.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_skillLevelScale.js
- Sample document: 03_design/01_master_data_management/samples/u_mes_mast_skillLevelScale.js
