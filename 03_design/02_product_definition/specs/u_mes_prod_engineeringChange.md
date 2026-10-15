# u_mes_prod_engineeringChange

| Property | Value |
|---|---|
| Module | ProductDefinition (prod) |
| Purpose | Engineering change notices with affected objects, approvals and effectivity (cut-in serial / date) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 37 (27 required, 10 may be null) |
| Estimated volume per year | 200-1,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per engineering change, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with engineeringChangeId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_prod_engineeringChangeAffectedItem | Child | affected item |
| u_mes_prod_engineeringChangeAffectedObject | Child | affected object |
| u_mes_prod_engineeringChangeApproval | Child | approval |
| u_mes_prod_engineeringChangeControlledDocument | Relationship | controlled document |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1076000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ECN-2026-0027"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | title | String | - | Yes | Title of the engineering change; used as its display value in other collections | `"Bleed screw torque window revised to 14 +/- 2 N.m"` |  |
| 7 | description | String | - | Yes | Description of the engineering change | `"Change request: bleed screw torque window revised to 14 +/- 2 n.m. Affected process step: gravity die casting"` |  |
| 8 | changeType | String | - | Yes | Change type | `"Process Change"` | Design Change; Process Change; Material Change; Supplier Change; Tooling Change; Document Change |
| 9 | reasonCodeText | String | - | Yes | Reason code text | `"Customer request after field study of bleed screw seepage"` |  |
| 10 | originator | String | - | Yes | Originator of the engineering change | `"Customer"` | Customer; Internal; Supplier |
| 11 | customerId | String | - | No (null allowed) | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 12 | customerName | String | - | No (null allowed) | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 13 | customerChangeRef | String | - | No (null allowed) | Customer change ref | `"SML-ECR-2026-118"` |  |
| 14 | raisedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'raised' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 15 | raisedBy | String | - | Yes | Display name of the user in raisedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 16 | raisedAt | Date | Datetime | Yes | Date and time when the record was raised. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 17 | effectivityType | String | - | Yes | Effectivity type | `"Date"` | Date; Serial Number; Lot; Stock Run Out |
| 18 | effectiveFrom | Date | Date | Yes | Effective from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 19 | cutInSerialNo | String | - | No (null allowed) | Cut in serial number | `"VB26272A00001"` |  |
| 20 | stockDispositionTypeId | String | - | No (null allowed) | Reference to u_mes_qual_dispositionType._id: stock disposition type | `"1284000000000001"` | Reference: u_mes_qual_dispositionType._id |
| 21 | stockDispositionTypeName | String | - | No (null allowed) | Display value of stockDispositionTypeId, copied from u_mes_qual_dispositionType.name | `"Use As Is"` |  |
| 22 | ppapRequired | Boolean | - | Yes | True when: PPAP required | `false` |  |
| 23 | implementedAt | Date | Datetime | No (null allowed) | Date and time when the record was implemented. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 24 | closedAt | Date | Datetime | No (null allowed) | Date and time when the record was closed. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 25 | gmpImpact | Boolean | - | Yes | True when the change affects GMP-relevant product, process, equipment or systems (GMP-44) | `true` |  |
| 26 | validationRequired | Boolean | - | Yes | True when process, equipment or system validation is required | `true` |  |
| 27 | regulatoryImpact | String | - | Yes | Regulatory or customer approval needed before implementation | `"Customer Notification"` | None; Customer Notification; Prior Approval |
| 28 | riskAssessmentId | String | - | No (null allowed) | Reference to u_mes_qual_riskAssessment._id | `null` | Reference: u_mes_qual_riskAssessment._id |
| 29 | riskAssessmentName | String | - | No (null allowed) | Display value of riskAssessmentId, copied from u_mes_qual_riskAssessment.title | `null` |  |
| 30 | status | String | - | Yes | Primary lifecycle state of the document | `"Raised"` | Raised; Under Evaluation; Approved; Implemented; Closed; Rejected |
| 31 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 32 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 33 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 34 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 35 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 36 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 37 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Raised, Under Evaluation, Approved, Implemented, Closed, Rejected. Initial state: Raised. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ customerId: 1 }` | No | Look-up of documents by customer |
| 4 | `{ stockDispositionTypeId: 1 }` | No | Look-up of documents by stock disposition type |
| 5 | `{ riskAssessmentId: 1 }` | No | Look-up of documents by risk assessment |
| 6 | `{ siteId: 1, raisedAt: -1 }` | No | Time-ordered lists and reports by raised at |

## Referenced by

u_mes_prod_itemRevision, u_mes_prod_billOfMaterial, u_mes_prod_routing, u_mes_prod_workInstruction, u_mes_prod_recipe, u_mes_prod_engineeringChangeAffectedItem, u_mes_prod_engineeringChangeAffectedObject, u_mes_prod_engineeringChangeApproval, u_mes_prod_engineeringChangeControlledDocument, u_mes_qual_controlPlan, u_mes_qual_deviationPermit, u_mes_qual_ppapSubmission, u_mes_maint_equipmentLifecycleEvent, u_mes_syst_systemValidation, u_mes_qual_processValidation, u_mes_maint_equipmentQualification, u_mes_mmr_masterManufacturingRecord.

## Files

- Validator: 03_design/02_product_definition/validators/u_mes_prod_engineeringChange.json
- Indexes: 03_design/02_product_definition/indexes/u_mes_prod_engineeringChange.js
- Sample documents (10): 03_design/02_product_definition/samples/u_mes_prod_engineeringChange.js
