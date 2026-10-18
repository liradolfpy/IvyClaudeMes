# u_mes_mast_skillCertification

| Property | Value |
|---|---|
| Module | MasterDataManagement (mast) |
| Purpose | Skills-matrix entries: user x skill, level, valid-from/to, assessor; used for operator lock-out |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 35 (26 required, 9 may be null) |
| Estimated volume per year | 5,000-20,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per skill certification, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1034000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"CERT-10231-ASY-OP"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | userId | String | - | Yes | Reference to u_mes_mast_user._id | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 7 | userName | String | - | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 8 | skillId | String | - | Yes | Reference to u_mes_mast_skill._id | `"1031000000000006"` | Reference: u_mes_mast_skill._id |
| 9 | skillName | String | - | Yes | Display value of skillId, copied from u_mes_mast_skill.name | `"Piston and seal assembly"` |  |
| 10 | level | Int32 | - | Yes | Level number on the scale of the parent record | `NumberInt(3)` |  |
| 11 | awardedAt | Date | Datetime | Yes | Date and time when the record was awarded. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 12 | validFrom | Date | Date | Yes | Valid from. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 13 | validTo | Date | Date | No (null allowed) | Valid to. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2027-03-31T00:00:00.000+0000")` |  |
| 14 | assessorUserId | String | - | Yes | Reference to u_mes_mast_user._id: assessor user | `"1029000000000005"` | Reference: u_mes_mast_user._id |
| 15 | assessorUserName | String | - | Yes | Display value of assessorUserId, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 16 | assessmentScore | Decimal128 | - | Yes | Assessment score | `86.0` |  |
| 17 | assessmentMethod | String | - | Yes | Assessment method | `"Practical Test"` | Practical Test; Written Test; Observation; On the Job |
| 18 | trainingHours | Decimal128 | - | Yes | Training hours | `16.0` |  |
| 19 | evidenceControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: evidence controlled document | `"1246000000000001"` | Reference: u_mes_syst_controlledDocument._id |
| 20 | evidenceControlledDocumentName | String | - | No (null allowed) | Display value of evidenceControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"Drawing 5110-20-0105 revision B, Caliper Body Casting LH"` |  |
| 21 | restrictions | String | - | No (null allowed) | Restrictions of the skill certification | `"Not certified for master leak verification"` |  |
| 22 | revokedAt | Date | Datetime | No (null allowed) | Date and time when the record was revoked. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 23 | revokedReason | String | - | No (null allowed) | Revoked reason | `null` |  |
| 24 | nextReviewAt | Date | Date | No (null allowed) | Next review at. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-10-06T00:00:00.000+0000")` |  |
| 25 | trainedDocumentRevision | String | - | No (null allowed) | Revision of the training document the operator was trained on | `"1"` |  |
| 26 | requalificationRequired | Boolean | - | Yes | True when a new document revision requires the operator to be trained again | `false` |  |
| 27 | revocationSource | String | - | No (null allowed) | Why the certification was revoked or suspended; null while valid | `null` | Expiry; Document Revision; Manual; Assessment Failure |
| 28 | status | String | - | Yes | Primary lifecycle state of the document | `"Valid"` | Valid; Expiring Soon; Expired; Revoked |
| 29 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 30 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 31 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 32 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 33 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 34 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 35 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Valid, Expiring Soon, Expired, Revoked. Initial state: Valid. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ userId: 1 }` | No | Look-up of documents by user |
| 4 | `{ skillId: 1 }` | No | Look-up of documents by skill |
| 5 | `{ assessorUserId: 1 }` | No | Look-up of documents by assessor user |
| 6 | `{ evidenceControlledDocumentId: 1 }` | No | Look-up of documents by evidence controlled document |
| 7 | `{ siteId: 1, awardedAt: -1 }` | No | Time-ordered lists and reports by awarded at |
| 8 | `{ userId: 1, skillId: 1, validTo: -1 }` | No | Operator lock-out check at station login |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_skillCertification.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_skillCertification.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_skillCertification.js
