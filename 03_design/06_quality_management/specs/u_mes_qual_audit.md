# u_mes_qual_audit

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Layered process, process (VDA 6.3), product and system audits with findings |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 39 (27 required, 12 may be null) |
| Estimated volume per year | ~1,500 |
| Storage | standard |

## Structure

Flat entity collection: one document per audit, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with auditId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_auditAuditorUser | Relationship | auditor user |
| u_mes_qual_auditFinding | Child | finding |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1195000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"AUD-2026-0931"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | Yes | Title of the audit; used as its display value in other collections | `"Layered process audit, foundry, week 38"` |  |
| 6 | auditType | String | Yes | Audit type | `"Layered Process Audit"` | Layered Process Audit; Process Audit; Product Audit; System Audit; Customer Audit; Supplier Audit |
| 7 | standard | String | Yes | Standard or specification the record refers to | `"IATF 16949:2016"` |  |
| 8 | scopeText | String | Yes | Scope text | `"Assembly line 1, torque and leak test stations"` |  |
| 9 | areaId | String | No (null allowed) | Reference to u_mes_mast_area._id | `"1005000000000001"` | Reference: u_mes_mast_area._id |
| 10 | areaName | String | No (null allowed) | Display value of areaId, copied from u_mes_mast_area.name | `"Foundry"` |  |
| 11 | lineId | String | No (null allowed) | Reference to u_mes_mast_line._id | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 12 | lineName | String | No (null allowed) | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 13 | customerId | String | No (null allowed) | Reference to u_mes_mast_customer._id | `null` | Reference: u_mes_mast_customer._id |
| 14 | customerName | String | No (null allowed) | Display value of customerId, copied from u_mes_mast_customer.name | `null` |  |
| 15 | layer | Int32 | Yes | Audit layer (1 = line leader, 2 = supervisor, 3 = manager) | `NumberInt(1)` |  |
| 16 | leadAuditorUserId | String | Yes | Reference to u_mes_mast_user._id: lead auditor user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 17 | leadAuditorUserName | String | Yes | Display value of leadAuditorUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 18 | auditeeUserId | String | Yes | Reference to u_mes_mast_user._id: auditee user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 19 | auditeeUserName | String | Yes | Display value of auditeeUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 20 | plannedDate | Date | Yes | Planned date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-04-01T18:30:00.000+0000")` |  |
| 21 | startedAt | Date | Yes | Date and time when the record was started | `ISODate("2026-09-15T00:30:00.000+0000")` |  |
| 22 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `null` |  |
| 23 | checkSheetId | String | No (null allowed) | Reference to u_mes_qual_checkSheet._id | `"1146000000000001"` | Reference: u_mes_qual_checkSheet._id |
| 24 | checkSheetName | String | No (null allowed) | Display value of checkSheetId, copied from u_mes_qual_checkSheet.name | `"Start of shift check, Gravity Die Casting Cell 1"` |  |
| 25 | questionsCount | Int32 | Yes | Questions count | `NumberInt(20)` |  |
| 26 | conformingCount | Int32 | Yes | Conforming count | `NumberInt(19)` |  |
| 27 | scorePct | Decimal128 | Yes | Score (percent) | `NumberDecimal("95.0")` |  |
| 28 | overallRating | String | No (null allowed) | Overall rating | `null` | A; B; C |
| 29 | reportControlledDocumentId | String | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: report controlled document | `"1246000000000001"` | Reference: u_mes_syst_controlledDocument._id |
| 30 | reportControlledDocumentName | String | No (null allowed) | Display value of reportControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"Drawing 5110-20-0105 revision B, Caliper Body Casting LH"` |  |
| 31 | nextAuditDueAt | Date | Yes | Next audit due date and time | `ISODate("2026-10-05T18:30:00.000+0000")` |  |
| 32 | status | String | Yes | Primary lifecycle state of the document | `"Planned"` | Planned; In Progress; Completed; Closed |
| 33 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 34 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:30:00.000+0000")` |  |
| 35 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 36 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 37 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:30:00.000+0000")` |  |
| 38 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 39 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Planned, In Progress, Completed, Closed. Initial state: Planned. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ areaId: 1 }` | No | Look-up of documents by area |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ customerId: 1 }` | No | Look-up of documents by customer |
| 6 | `{ leadAuditorUserId: 1 }` | No | Look-up of documents by lead auditor user |
| 7 | `{ auditeeUserId: 1 }` | No | Look-up of documents by auditee user |
| 8 | `{ siteId: 1, plannedDate: -1 }` | No | Time-ordered lists and reports by planned date |

## Referenced by

u_mes_qual_capa, u_mes_qual_auditAuditorUser, u_mes_qual_auditFinding.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_audit.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_audit.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_audit.js
