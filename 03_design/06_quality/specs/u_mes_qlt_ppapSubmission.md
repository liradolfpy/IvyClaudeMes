# u_mes_qlt_ppapSubmission

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | PPAP package: level, 18 elements with status, PSW, customer decision |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | PPAP-<recordNo> |
| Display value used by references | recordNo |
| Keys | 35 (21 required, 14 may be null) |
| Estimated volume per year | ~100 |
| Storage | standard |

## Structure

Flat entity collection: one document per PPAP submission, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with ppapSubmissionId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qlt_ppapSubmissionElement | Child | element |
| u_mes_qlt_ppapSubmissionMsaStudy | Relationship | MSA study |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: PPAP-<recordNo> | `"PPAP-5110-10-0100-D-L3"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"5110-10-0100-D-L3"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | itemId | String | Yes | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 6 | itemName | String | Yes | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 7 | itemRevision | String | Yes | Item revision | `"D"` |  |
| 8 | customerId | String | Yes | Reference to u_mes_mdm_customer._id | `"CUS-SML"` | Reference: u_mes_mdm_customer._id |
| 9 | customerName | String | Yes | Display value of customerId, copied from u_mes_mdm_customer.name | `"Sahyadri Motors Ltd."` |  |
| 10 | engineeringChangeId | String | No (null allowed) | Reference to u_mes_prd_engineeringChange._id | `"ECN-2026-0031"` | Reference: u_mes_prd_engineeringChange._id |
| 11 | engineeringChangeName | String | No (null allowed) | Display value of engineeringChangeId, copied from u_mes_prd_engineeringChange.title | `"Bleed screw torque window revised"` |  |
| 12 | submissionLevel | Int32 | Yes | PPAP submission level 1 to 5 | `NumberInt(3)` |  |
| 13 | submissionReason | String | Yes | Submission reason | `"Engineering Change"` | Initial Submission; Engineering Change; Tooling Transfer; Correction Of Discrepancy; Tooling Inactive Over One Year; Sub Supplier Change |
| 14 | controlPlanId | String | No (null allowed) | Reference to u_mes_qlt_controlPlan._id | `"CP-5110-10-0100-PROD"` | Reference: u_mes_qlt_controlPlan._id |
| 15 | controlPlanName | String | No (null allowed) | Display value of controlPlanId, copied from u_mes_qlt_controlPlan.recordNo | `"5110-10-0100-PROD"` |  |
| 16 | pfmeaId | String | No (null allowed) | Reference to u_mes_qlt_pfmea._id | `"FMEA-5110-10-0100-PF"` | Reference: u_mes_qlt_pfmea._id |
| 17 | pfmeaName | String | No (null allowed) | Display value of pfmeaId, copied from u_mes_qlt_pfmea.title | `"Process FMEA, Front Brake Caliper Assembly LH"` |  |
| 18 | sampleQuantity | Int32 | Yes | Sample quantity | `NumberInt(6)` |  |
| 19 | significantProductionRunQuantity | Int32 | Yes | Significant production run quantity | `NumberInt(300)` |  |
| 20 | pswSignedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'PSW signed' | `"USR-10019"` | Reference: u_mes_mdm_user._id |
| 21 | pswSignedBy | String | No (null allowed) | Display name of the user in pswSignedById, copied from u_mes_mdm_user.fullName | `"Meera Deshpande"` |  |
| 22 | pswSignedAt | Date | No (null allowed) | Psw signed date and time | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 23 | submittedAt | Date | No (null allowed) | Date and time when the record was submitted | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 24 | customerDecision | String | No (null allowed) | Customer decision | `"Approved"` | Approved; Interim Approved; Rejected |
| 25 | customerDecisionAt | Date | No (null allowed) | Customer decision date and time | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 26 | customerRemarks | String | No (null allowed) | Customer remarks | `null` |  |
| 27 | interimApprovalValidTo | Date | No (null allowed) | Interim approval valid to (calendar date, stored as the start of that day in IST converted to UTC) | `null` |  |
| 28 | status | String | Yes | Primary lifecycle state of the document | `"Approved"` | In Preparation; Submitted; Approved; Interim Approved; Rejected |
| 29 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 30 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 31 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 32 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 33 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 34 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 35 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |

## Status values

In Preparation, Submitted, Approved, Interim Approved, Rejected. Initial state: In Preparation. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_qlt_ppapSubmissionElement, u_mes_qlt_ppapSubmissionMsaStudy.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_ppapSubmission.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_ppapSubmission.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_ppapSubmission.js
