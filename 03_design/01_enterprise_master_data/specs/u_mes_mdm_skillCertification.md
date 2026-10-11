# u_mes_mdm_skillCertification

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Skills-matrix entries: user x skill, level, valid-from/to, assessor; used for operator lock-out |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | CERT-<recordNo> |
| Display value used by references | recordNo |
| Keys | 31 (24 required, 7 may be null) |
| Estimated volume per year | 5,000-20,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per skill certification, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: CERT-<recordNo> | `"CERT-10231-LEAK-TEST-OP"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"10231-LEAK-TEST-OP"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | userId | String | Yes | Reference to u_mes_mdm_user._id | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 6 | userName | String | Yes | Display value of userId, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 7 | skillId | String | Yes | Reference to u_mes_mdm_skill._id | `"SKL-LEAK-TEST-OP"` | Reference: u_mes_mdm_skill._id |
| 8 | skillName | String | Yes | Display value of skillId, copied from u_mes_mdm_skill.name | `"Leak Test Operation"` |  |
| 9 | level | Int32 | Yes | Level number on the scale of the parent record | `NumberInt(3)` |  |
| 10 | awardedAt | Date | Yes | Date and time when the record was awarded | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 11 | validFrom | Date | Yes | Valid from (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 12 | validTo | Date | No (null allowed) | Valid to (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2027-03-31T18:29:59.000+0000")` |  |
| 13 | assessorUserId | String | Yes | Reference to u_mes_mdm_user._id: assessor user | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 14 | assessorUserName | String | Yes | Display value of assessorUserId, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 15 | assessmentScore | Decimal128 | Yes | Assessment score | `NumberDecimal("86.0")` |  |
| 16 | assessmentMethod | String | Yes | Assessment method | `"Practical Test"` | Practical Test; Written Test; Observation; On the Job |
| 17 | trainingHours | Decimal128 | Yes | Training hours | `NumberDecimal("16.0")` |  |
| 18 | evidenceControlledDocumentId | String | No (null allowed) | Reference to u_mes_sys_controlledDocument._id: evidence controlled document | `"DOC-TRN-10231-LEAK"` | Reference: u_mes_sys_controlledDocument._id |
| 19 | evidenceControlledDocumentName | String | No (null allowed) | Display value of evidenceControlledDocumentId, copied from u_mes_sys_controlledDocument.title | `"Assessment sheet, Sunil Jadhav, leak test operation"` |  |
| 20 | restrictions | String | No (null allowed) | Restrictions of the skill certification | `"Not certified for master leak verification"` |  |
| 21 | revokedAt | Date | No (null allowed) | Date and time when the record was revoked | `null` |  |
| 22 | revokedReason | String | No (null allowed) | Revoked reason | `null` |  |
| 23 | nextReviewAt | Date | No (null allowed) | Next review date and time | `ISODate("2026-10-27T18:30:00.000+0000")` |  |
| 24 | status | String | Yes | Primary lifecycle state of the document | `"Valid"` | Valid; Expiring Soon; Expired; Revoked |
| 25 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 26 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 27 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 28 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 29 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 30 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 31 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Valid, Expiring Soon, Expired, Revoked. Initial state: Valid. The values are maintained in u_mes_sys_statusDefinition.

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

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_skillCertification.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_skillCertification.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_skillCertification.js
