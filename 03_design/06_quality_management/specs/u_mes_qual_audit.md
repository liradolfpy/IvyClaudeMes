# u_mes_qual_audit

| Property | Value |
|---|---|
| Module | QualityManagement (qual) |
| Purpose | Layered process, process (VDA 6.3), product and system audits with findings |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 45 (30 required, 15 may be null) |
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

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1195000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"AUD-2026-0931"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | title | String | - | Yes | Title of the audit; used as its display value in other collections | `"Layered process audit, foundry, week 38"` |  |
| 7 | auditType | String | - | Yes | Audit type | `"Layered Process Audit"` | Layered Process Audit; Process Audit; Product Audit; System Audit; Customer Audit; Supplier Audit |
| 8 | standard | String | - | Yes | Standard or specification the record refers to | `"IATF 16949:2016"` |  |
| 9 | scopeText | String | - | Yes | Scope text | `"Assembly line 1, torque and leak test stations"` |  |
| 10 | areaId | String | - | No (null allowed) | Reference to u_mes_mast_area._id | `"1005000000000001"` | Reference: u_mes_mast_area._id |
| 11 | areaName | String | - | No (null allowed) | Display value of areaId, copied from u_mes_mast_area.name | `"Foundry"` |  |
| 12 | lineId | String | - | No (null allowed) | Reference to u_mes_mast_line._id | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 13 | lineName | String | - | No (null allowed) | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 14 | customerId | String | - | No (null allowed) | Reference to u_mes_mast_customer._id | `null` | Reference: u_mes_mast_customer._id |
| 15 | customerName | String | - | No (null allowed) | Display value of customerId, copied from u_mes_mast_customer.name | `null` |  |
| 16 | layer | Int32 | - | Yes | Audit layer (1 = line leader, 2 = supervisor, 3 = manager) | `NumberInt(1)` |  |
| 17 | leadAuditorUserId | String | - | Yes | Reference to u_mes_mast_user._id: lead auditor user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 18 | leadAuditorUserName | String | - | Yes | Display value of leadAuditorUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 19 | auditeeUserId | String | - | Yes | Reference to u_mes_mast_user._id: auditee user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 20 | auditeeUserName | String | - | Yes | Display value of auditeeUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 21 | plannedDate | Date | Date | Yes | Planned date. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 22 | startedAt | Date | Datetime | Yes | Date and time when the record was started. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 23 | completedAt | Date | Datetime | No (null allowed) | Date and time when the record was completed. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 24 | checkSheetId | String | - | No (null allowed) | Reference to u_mes_qual_checkSheet._id | `"1146000000000001"` | Reference: u_mes_qual_checkSheet._id |
| 25 | checkSheetName | String | - | No (null allowed) | Display value of checkSheetId, copied from u_mes_qual_checkSheet.name | `"Start of shift check, Gravity Die Casting Cell 1"` |  |
| 26 | questionsCount | Int32 | - | Yes | Questions count | `NumberInt(20)` |  |
| 27 | conformingCount | Int32 | - | Yes | Conforming count | `NumberInt(19)` |  |
| 28 | scorePct | Decimal128 | - | Yes | Score (percent) | `95.0` |  |
| 29 | overallRating | String | - | No (null allowed) | Overall rating | `null` | A; B; C |
| 30 | reportControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: report controlled document | `"1246000000000001"` | Reference: u_mes_syst_controlledDocument._id |
| 31 | reportControlledDocumentName | String | - | No (null allowed) | Display value of reportControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `"Drawing 5110-20-0105 revision B, Caliper Body Casting LH"` |  |
| 32 | nextAuditDueAt | Date | Date | Yes | Next audit due at. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-10-06T00:00:00.000+0000")` |  |
| 33 | auditScheduleId | String | - | No (null allowed) | Reference to u_mes_qual_auditSchedule._id | `"1322000000000008"` | Reference: u_mes_qual_auditSchedule._id |
| 34 | auditScheduleName | String | - | No (null allowed) | Display value of auditScheduleId, copied from u_mes_qual_auditSchedule.name | `"LPA layer 3, foundry, weekly"` |  |
| 35 | dueDate | Date | Date | No (null allowed) | Date by which the audit had to be done | `ISODate("2026-09-19T00:00:00.000+0000")` |  |
| 36 | isMissed | Boolean | - | Yes | True when the audit was not done by its due date plus tolerance | `true` |  |
| 37 | escalationLevel | Int32 | - | Yes | Escalation level reached (0 = not escalated) | `NumberInt(1)` |  |
| 38 | status | String | - | Yes | Primary lifecycle state of the document | `"Planned"` | Planned; In Progress; Completed; Closed |
| 39 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 40 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 41 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 42 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 43 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 44 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 45 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

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
