# u_mes_prod_workInstruction

| Property | Value |
|---|---|
| Module | ProductDefinition (prod) |
| Purpose | Versioned visual work instructions with steps, media, cautions, variant applicability, required checks |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 30 (21 required, 9 may be null) |
| Estimated volume per year | 1,000-5,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per work instruction, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with workInstructionId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_prod_workInstructionStep | Child | step |
| u_mes_prod_workInstructionStepMediaControlledDocument | Relationship | (below u_mes_prod_workInstructionStep) media controlled document |
| u_mes_prod_workInstructionStepProductVariant | Relationship | (below u_mes_prod_workInstructionStep) product variant |
| u_mes_prod_workInstructionStepTool | Relationship | (below u_mes_prod_workInstructionStep) tool |
| u_mes_prod_workInstructionStepCharacteristic | Relationship | (below u_mes_prod_workInstructionStep) characteristic |
| u_mes_prod_workInstructionPpeItem | Relationship | ppe item |
| u_mes_prod_workInstructionKeyPoint | Value list | key point |
| u_mes_prod_workInstructionWorkCenter | Relationship | work center |
| u_mes_prod_workInstructionProductVariant | Relationship | product variant |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1065000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"WI-OP010-001"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | title | String | - | Yes | Title of the work instruction; used as its display value in other collections | `"Pouring and die cycle - Caliper body LH"` |  |
| 7 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 8 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 9 | operationId | String | - | Yes | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 10 | operationName | String | - | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 11 | version | Int32 | - | Yes | Version of the work instruction | `NumberInt(1)` |  |
| 12 | languageId | String | - | Yes | Reference to u_mes_mast_language._id | `"1267000000000001"` | Reference: u_mes_mast_language._id |
| 13 | languageName | String | - | Yes | Display value of languageId, copied from u_mes_mast_language.name | `"English"` |  |
| 14 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 15 | effectiveTo | Date | Date | No (null allowed) | Effective to. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2027-03-31T00:00:00.000+0000")` |  |
| 16 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `"1076000000000001"` | Reference: u_mes_prod_engineeringChange._id |
| 17 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `"Bleed screw torque window revised to 14 +/- 2 N.m"` |  |
| 18 | safetyNotes | String | - | No (null allowed) | Safety notes | `"Keep hands clear of the nutrunner socket during rundown"` |  |
| 19 | authorUserId | String | - | Yes | Reference to u_mes_mast_user._id: author user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 20 | authorUserName | String | - | Yes | Display value of authorUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 21 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `null` | Reference: u_mes_mast_user._id |
| 22 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 23 | approvedAt | Date | Datetime | No (null allowed) | Date and time when the record was approved. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 24 | readAcknowledgementRequired | Boolean | - | Yes | True when: read acknowledgement required | `true` |  |
| 25 | reacknowledgeOnRevision | Boolean | - | Yes | True when operators must acknowledge every new revision before the next operation | `false` |  |
| 26 | generationSource | String | - | Yes | How the draft was produced | `"Manual"` | Manual; Generated From Bill Of Process; Generated By Model |
| 27 | sourceBillOfProcessId | String | - | No (null allowed) | Reference to u_mes_prod_billOfProcess._id: source bill of process | `null` | Reference: u_mes_prod_billOfProcess._id |
| 28 | sourceBillOfProcessName | String | - | No (null allowed) | Display value of sourceBillOfProcessId, copied from u_mes_prod_billOfProcess.recordNo | `null` |  |
| 29 | status | String | - | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 30 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

In Preparation, Released, Obsolete. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ operationId: 1 }` | No | Look-up of documents by operation |
| 5 | `{ languageId: 1 }` | No | Look-up of documents by language |
| 6 | `{ engineeringChangeId: 1 }` | No | Look-up of documents by engineering change |
| 7 | `{ authorUserId: 1 }` | No | Look-up of documents by author user |

## Referenced by

u_mes_prod_billOfProcessStep, u_mes_prod_workInstructionStep, u_mes_prod_workInstructionPpeItem, u_mes_prod_workInstructionKeyPoint, u_mes_plan_stepCompletion, u_mes_syst_operatorAppStep, u_mes_prod_workInstructionWorkCenter, u_mes_prod_workInstructionProductVariant.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_workInstruction.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_workInstruction.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_workInstruction.js
