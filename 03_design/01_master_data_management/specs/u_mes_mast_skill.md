# u_mes_mast_skill

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Skill definitions required by operations (e.g. leak-test operation, CMM programming) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 16 (14 required, 2 may be null) |
| Estimated volume per year | 50-300 |
| Storage | standard |

## Structure

Flat entity collection: one document per skill, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with skillId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mast_skillOperation | Relationship | operation |
| u_mes_mast_skillLevelScale | Child | level scale |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1031000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"GDC-OP"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the skill; used as its display value in other collections | `"Gravity die casting operation"` |  |
| 6 | skillCategoryId | String | - | Yes | Reference to u_mes_mast_skillCategory._id | `"1262000000000001"` | Reference: u_mes_mast_skillCategory._id |
| 7 | skillCategoryName | String | - | Yes | Display value of skillCategoryId, copied from u_mes_mast_skillCategory.name | `"Process"` |  |
| 8 | description | String | - | Yes | Description of the skill | `"Can perform 'gravity die casting' to the work instruction and react to abnormalities"` |  |
| 9 | minimumLevelRequired | Int32 | - | Yes | Lowest skill level allowed to work unsupervised | `NumberInt(3)` |  |
| 10 | validityMonths | Int32 | - | Yes | Validity (months) | `NumberInt(12)` |  |
| 11 | trainingControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: training controlled document | `"1246000000000001"` | Reference: u_mes_syst_controlledDocument._id |
| 12 | trainingControlledDocumentName | String | - | No (null allowed) | Display value of trainingControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"Drawing 5110-20-0105 revision B, Caliper Body Casting LH"` |  |
| 13 | assessmentMethod | String | - | Yes | Assessment method | `"Practical Test"` | Practical Test; Written Test; Observation; On the Job |
| 14 | isSafetyCritical | Boolean | - | Yes | True when the record is safety critical | `true` |  |
| 15 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 16 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ skillCategoryId: 1 }` | No | Look-up of documents by skill category |
| 4 | `{ trainingControlledDocumentId: 1 }` | No | Look-up of documents by training controlled document |

## Referenced by

u_mes_mast_workCenterRequiresSkill, u_mes_mast_skillOperation, u_mes_mast_skillLevelScale, u_mes_mast_skillCertification, u_mes_prod_operationRequiredSkill, u_mes_prod_billOfProcessStepRequiredSkill, u_mes_maint_maintenancePlanRequiredSkill, u_mes_mast_roleRequiredSkill, u_mes_syst_escalationRule.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_skill.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_skill.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_skill.js
