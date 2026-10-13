# u_mes_qual_ppapSubmission

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | PPAP package: level, 18 elements with status, PSW, customer decision |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 36 (22 required, 14 may be null) |
| Estimated volume per year | ~100 |
| Storage | standard |

## Structure

Flat entity collection: one document per PPAP submission, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with ppapSubmissionId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_ppapSubmissionElement | Child | element |
| u_mes_qual_ppapSubmissionMsaStudy | Relationship | MSA study |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1186000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PPAP-5110-10-0100-D-01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 7 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 8 | itemRevision | String | - | Yes | Item revision | `"D"` |  |
| 9 | customerId | String | - | Yes | Reference to u_mes_mast_customer._id | `"1035000000000001"` | Reference: u_mes_mast_customer._id |
| 10 | customerName | String | - | Yes | Display value of customerId, copied from u_mes_mast_customer.name | `"Sahyadri Motors Ltd."` |  |
| 11 | engineeringChangeId | String | - | No (null allowed) | Reference to u_mes_prod_engineeringChange._id | `"1076000000000010"` | Reference: u_mes_prod_engineeringChange._id |
| 12 | engineeringChangeName | String | - | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prod_engineeringChange.title | `"Work instruction pictures updated for RH variant"` |  |
| 13 | submissionLevel | Int32 | - | Yes | PPAP submission level 1 to 5 | `NumberInt(3)` |  |
| 14 | submissionReason | String | - | Yes | Submission reason | `"Initial Submission"` | Initial Submission; Engineering Change; Tooling Transfer; Correction Of Discrepancy; Tooling Inactive Over One Year; Sub Supplier Change |
| 15 | controlPlanId | String | - | No (null allowed) | Reference to u_mes_qual_controlPlan._id | `"1139000000000001"` | Reference: u_mes_qual_controlPlan._id |
| 16 | controlPlanName | String | - | No (null allowed) | Display value of controlPlanId, copied from u_mes_qual_controlPlan.recordNo | `"CP-5110-10-0100-PROD"` |  |
| 17 | pfmeaId | String | - | No (null allowed) | Reference to u_mes_qual_pfmea._id | `"1183000000000001"` | Reference: u_mes_qual_pfmea._id |
| 18 | pfmeaName | String | - | No (null allowed) | Display value of pfmeaId, copied from u_mes_qual_pfmea.title | `"Process FMEA, Front caliper LH, full process routing"` |  |
| 19 | sampleQuantity | Int32 | - | Yes | Sample quantity | `NumberInt(6)` |  |
| 20 | significantProductionRunQuantity | Int32 | - | Yes | Significant production run quantity | `NumberInt(300)` |  |
| 21 | pswSignedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'PSW signed' | `null` | Reference: u_mes_mast_user._id |
| 22 | pswSignedBy | String | - | No (null allowed) | Display name of the user in pswSignedById, copied from u_mes_mast_user.fullName | `null` |  |
| 23 | pswSignedAt | Date | Datetime | No (null allowed) | Psw signed date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 24 | submittedAt | Date | Datetime | No (null allowed) | Date and time when the record was submitted. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 25 | customerDecision | String | - | No (null allowed) | Customer decision | `null` | Approved; Interim Approved; Rejected |
| 26 | customerDecisionAt | Date | Datetime | No (null allowed) | Customer decision date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 27 | customerRemarks | String | - | No (null allowed) | Customer remarks | `null` |  |
| 28 | interimApprovalValidTo | Date | Date | No (null allowed) | Interim approval valid to. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `null` |  |
| 29 | status | String | - | Yes | Primary lifecycle state of the document | `"In Preparation"` | In Preparation; Submitted; Approved; Interim Approved; Rejected |
| 30 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 31 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 32 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 33 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 34 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 35 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 36 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

In Preparation, Submitted, Approved, Interim Approved, Rejected. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 4 | `{ customerId: 1 }` | No | Look-up of documents by customer |
| 5 | `{ engineeringChangeId: 1 }` | No | Look-up of documents by engineering change |
| 6 | `{ controlPlanId: 1 }` | No | Look-up of documents by control plan |
| 7 | `{ pfmeaId: 1 }` | No | Look-up of documents by PFMEA |
| 8 | `{ siteId: 1, pswSignedAt: -1 }` | No | Time-ordered lists and reports by PSW signed at |

## Referenced by

u_mes_qual_ppapSubmissionElement, u_mes_qual_ppapSubmissionMsaStudy.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_ppapSubmission.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_ppapSubmission.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_ppapSubmission.js
