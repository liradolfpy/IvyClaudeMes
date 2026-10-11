# u_mes_mdm_skill

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Skill definitions required by operations (e.g. leak-test operation, CMM programming) |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | SKL-<recordNo> |
| Display value used by references | name |
| Keys | 16 (14 required, 2 may be null) |
| Estimated volume per year | 50-300 |
| Storage | standard |

## Structure

Flat entity collection: one document per skill, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with skillId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mdm_skillOperation | Relationship | operation |
| u_mes_mdm_skillLevelScale | Child | level scale |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: SKL-<recordNo> | `"SKL-LEAK-TEST-OP"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"LEAK-TEST-OP"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the skill; used as its display value in other collections | `"Leak Test Operation"` |  |
| 6 | skillCategoryId | String | Yes | Reference to u_mes_mdm_skillCategory._id | `"SKC-PROCESS"` | Reference: u_mes_mdm_skillCategory._id |
| 7 | skillCategoryName | String | Yes | Display value of skillCategoryId, copied from u_mes_mdm_skillCategory.name | `"Process"` |  |
| 8 | description | String | Yes | Description of the skill | `"Operate the pressure leak tester and react to a failed test"` |  |
| 9 | minimumLevelRequired | Int32 | Yes | Lowest skill level allowed to work unsupervised | `NumberInt(3)` |  |
| 10 | validityMonths | Int32 | Yes | Validity (months) | `NumberInt(12)` |  |
| 11 | trainingControlledDocumentId | String | No (null allowed) | Reference to u_mes_sys_controlledDocument._id: training controlled document | `"DOC-TRN-LEAK-TEST-OP"` | Reference: u_mes_sys_controlledDocument._id |
| 12 | trainingControlledDocumentName | String | No (null allowed) | Display value of trainingControlledDocumentId, copied from u_mes_sys_controlledDocument.title | `"Training module, leak test operation"` |  |
| 13 | assessmentMethod | String | Yes | Assessment method | `"Practical Test"` | Practical Test; Written Test; Observation; On the Job |
| 14 | isSafetyCritical | Boolean | Yes | True when the record is safety critical | `true` |  |
| 15 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 16 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ skillCategoryId: 1 }` | No | Look-up of documents by skill category |
| 4 | `{ trainingControlledDocumentId: 1 }` | No | Look-up of documents by training controlled document |

## Referenced by

u_mes_mdm_workCenterRequiresSkill, u_mes_mdm_skillOperation, u_mes_mdm_skillLevelScale, u_mes_mdm_skillCertification, u_mes_prd_operationRequiredSkill, u_mes_prd_billOfProcessStepRequiredSkill, u_mes_mnt_maintenancePlanRequiredSkill.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_skill.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_skill.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_skill.js
