# u_mes_prod_workInstruction

| Property | Value |
|---|---|
| Module | Product Definition (prod) |
| Purpose | Versioned visual work instructions with steps, media, cautions, variant applicability, required checks |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | WI-<recordNo> |
| Display value used by references | title |
| Keys | 25 (18 required, 7 may be null) |
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

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: WI-<recordNo> | `"WI-WI-OP070-001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"WI-OP070-001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | Yes | Title of the work instruction; used as its display value in other collections | `"Bleed screw tightening - Front caliper LH"` |  |
| 6 | itemId | String | Yes | Reference to u_mes_prod_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prod_item._id |
| 7 | itemName | String | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 8 | operationId | String | Yes | Reference to u_mes_prod_operation._id | `"OPN-OP070"` | Reference: u_mes_prod_operation._id |
| 9 | operationName | String | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Bleed screw torque"` |  |
| 10 | version | Int32 | Yes | Version of the work instruction | `NumberInt(3)` |  |
| 11 | languageId | String | Yes | Reference to u_mes_mast_language._id | `"LNG-en"` | Reference: u_mes_mast_language._id |
| 12 | languageName | String | Yes | Display value of languageId, copied from u_mes_mast_language.name | `"English"` |  |
| 13 | effectiveFrom | Date | Yes | Effective from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 14 | effectiveTo | Date | No (null allowed) | Effective to (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2027-03-31T18:29:59.000+0000")` |  |
| 15 | engineeringChangeId | String | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `"ECN-2026-0031"` | Reference: u_mes_prod_engineeringChange._id |
| 16 | engineeringChangeName | String | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `"Bleed screw torque window revised"` |  |
| 17 | safetyNotes | String | No (null allowed) | Safety notes | `"Keep hands clear of the nutrunner socket during rundown"` |  |
| 18 | authorUserId | String | Yes | Reference to u_mes_mast_user._id: author user | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 19 | authorUserName | String | Yes | Display value of authorUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 20 | approvedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"USR-10019"` | Reference: u_mes_mast_user._id |
| 21 | approvedBy | String | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 22 | approvedAt | Date | No (null allowed) | Date and time when the record was approved | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 23 | readAcknowledgementRequired | Boolean | Yes | True when: read acknowledgement required | `true` |  |
| 24 | status | String | Yes | Primary lifecycle state of the document | `"Released"` | In Preparation; Released; Obsolete |
| 25 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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

u_mes_prod_billOfProcessStep, u_mes_prod_workInstructionStep, u_mes_prod_workInstructionPpeItem, u_mes_prod_workInstructionKeyPoint, u_mes_plan_stepCompletion, u_mes_syst_operatorAppStep.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_workInstruction.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_workInstruction.js
- Sample document: 03_design/02_product_definition/samples/u_mes_prod_workInstruction.js
