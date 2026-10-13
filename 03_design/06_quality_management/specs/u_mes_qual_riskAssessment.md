# u_mes_qual_riskAssessment

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Documented quality risk assessment of a change, system, deviation, equipment or product: method, initial and residual risk, controls and acceptance. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 28 (19 required, 9 may be null) |
| Estimated volume per year | about 200 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per risk assessment, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1361000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"QRA-2026-021"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | - | Yes | Title | `"MES release 2.7.0, validation risk assessment of GMP functions"` |  |
| 6 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_syst_computerisedSystem"` | u_mes_prod_engineeringChange; u_mes_syst_computerisedSystem; u_mes_qual_nonconformance; u_mes_mast_equipment; u_mes_prod_item |
| 7 | relatedEntityId | String | - | Yes | _id of the related document in the collection named by relatedCollectionName | `"1344000000000001"` | Reference: Any collection (see relatedCollectionName) |
| 8 | relatedEntityName | String | - | Yes | Display value of the related document | `"Manufacturing execution system, Chakan plant"` |  |
| 9 | assessmentMethod | String | - | Yes | Risk method | `"Risk Ranking And Filtering"` | FMEA; Risk Ranking And Filtering; Fault Tree Analysis; HACCP; Preliminary Hazard Analysis |
| 10 | scopeText | String | - | Yes | Scope of the assessment | `"New and changed functions of release 2.7.0: signatures, batch record review, release, reconciliation, reports"` |  |
| 11 | initialRiskLevel | String | - | Yes | Risk before controls | `"High"` | Low; Medium; High |
| 12 | residualRiskLevel | String | - | No (null allowed) | Risk after controls; null until assessed | `"Low"` | Low; Medium; High |
| 13 | riskControlsText | String | - | No (null allowed) | Controls decided | `"Scripted testing of signature, release and reconciliation functions; unscripted testing of reports"` |  |
| 14 | pfmeaId | String | - | No (null allowed) | Reference to u_mes_qual_pfmea._id | `null` | Reference: u_mes_qual_pfmea._id |
| 15 | pfmeaName | String | - | No (null allowed) | Display value of pfmeaId, copied from u_mes_qual_pfmea.title | `null` |  |
| 16 | acceptanceDecision | String | - | No (null allowed) | Risk acceptance decision | `"Accepted With Controls"` | Accepted; Accepted With Controls; Not Accepted |
| 17 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 18 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 19 | approvedAt | Date | Datetime | No (null allowed) | Approval time | `ISODate("2026-08-14T10:00:00.000+0000")` |  |
| 20 | nextReviewDate | Date | Date | No (null allowed) | Date of the next review | `ISODate("2027-08-14T00:00:00.000+0000")` |  |
| 21 | status | String | - | Yes | Primary lifecycle state of the document | `"Approved"` | In Preparation; In Review; Approved; Superseded |
| 22 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 23 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-08-14T10:00:00.000+0000")` |  |
| 24 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 25 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 26 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-08-14T10:00:00.000+0000")` |  |
| 27 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 28 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

In Preparation, In Review, Approved, Superseded. Initial state: In Preparation. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ pfmeaId: 1 }` | No | Look-up of documents by PFMEA |
| 4 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 5 | `{ siteId: 1, approvedAt: -1 }` | No | Time-ordered lists and reports by approved at |

## Referenced by

u_mes_prod_engineeringChange, u_mes_qual_nonconformance, u_mes_syst_systemValidation.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_riskAssessment.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_riskAssessment.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_riskAssessment.js
