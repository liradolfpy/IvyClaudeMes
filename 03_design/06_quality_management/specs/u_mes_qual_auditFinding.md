# u_mes_qual_auditFinding

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One document per finding of a audit |
| Kind | Child |
| Data class | Transaction |
| Parent collection | u_mes_qual_audit |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 24 (20 required, 4 may be null) |

## Structure

Child collection. The parent audit can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. auditId and auditName point to the parent.
Data class (transaction) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1197000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"AUD-2026-0931-F01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | auditId | String | - | Yes | Reference to u_mes_qual_audit._id: the parent document this one belongs to | `"1195000000000001"` | Reference: u_mes_qual_audit._id |
| 7 | auditName | String | - | Yes | Display value of auditId, copied from u_mes_qual_audit.title | `"Layered process audit, foundry, week 38"` |  |
| 8 | findingNo | Int32 | - | Yes | Finding number | `NumberInt(1)` |  |
| 9 | clause | String | - | No (null allowed) | Clause of the audit finding | `"8.5.1.1"` |  |
| 10 | description | String | - | Yes | Description of the audit finding | `"Record for 'Is the die coating intact on both die halves' not signed on one shift"` |  |
| 11 | grade | String | - | Yes | Grade of the audit finding | `"Minor"` | Major; Minor; Observation; Opportunity For Improvement |
| 12 | ownerUserId | String | - | Yes | Reference to u_mes_mast_user._id: owner user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 13 | ownerUserName | String | - | Yes | Display value of ownerUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 14 | dueAt | Date | Datetime | Yes | Due date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:03:00.000+0000")` |  |
| 15 | closedAt | Date | Datetime | No (null allowed) | Date and time when the record was closed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:30.000+0000")` |  |
| 16 | capaId | String | - | No (null allowed) | Reference to u_mes_qual_capa._id | `"1176000000000001"` | Reference: u_mes_qual_capa._id |
| 17 | capaName | String | - | No (null allowed) | Display value of capaId, copied from u_mes_qual_capa.title | `"8D - Shrinkage porosity in bridge section"` |  |
| 18 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 19 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:03:00.000+0000")` |  |
| 20 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 21 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 22 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:03:00.000+0000")` |  |
| 23 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 24 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ auditId: 1, findingNo: 1 }` | Yes | Lines of one parent in order; one line per number |
| 2 | `{ ownerUserId: 1 }` | No | Look-up of lines by owner user |
| 3 | `{ capaId: 1 }` | No | Look-up of lines by CAPA |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_auditFinding.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_auditFinding.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_auditFinding.js
