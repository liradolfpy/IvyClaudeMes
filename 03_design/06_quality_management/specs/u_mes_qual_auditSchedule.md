# u_mes_qual_auditSchedule

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Plan for layered process audits (and other recurring audits): layer, area or line, check sheet, frequency and auditor. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 29 (17 required, 12 may be null) |
| Estimated volume per year | about 60 rows in total |
| Storage | standard collection |

## Structure

Flat entity collection: one document per audit schedule, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1322000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"LPA-L1-ASY-01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Schedule name | `"LPA layer 1, piston and seal assembly, every shift"` |  |
| 6 | auditType | String | - | Yes | Audit type | `"Layered Process Audit"` | Layered Process Audit; Product Audit; Process Audit; 5S Audit |
| 7 | layer | Int32 | - | No (null allowed) | LPA layer | `NumberInt(1)` |  |
| 8 | areaId | String | - | No (null allowed) | Reference to u_mes_mast_area._id | `"1005000000000005"` | Reference: u_mes_mast_area._id |
| 9 | areaName | String | - | No (null allowed) | Display value of areaId, copied from u_mes_mast_area.name | `"Assembly and Test"` |  |
| 10 | lineId | String | - | No (null allowed) | Reference to u_mes_mast_line._id | `"1006000000000006"` | Reference: u_mes_mast_line._id |
| 11 | lineName | String | - | No (null allowed) | Display value of lineId, copied from u_mes_mast_line.name | `"Front Caliper Assembly Line 1"` |  |
| 12 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 13 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 14 | checkSheetId | String | - | Yes | Reference to u_mes_qual_checkSheet._id | `"1146000000000006"` | Reference: u_mes_qual_checkSheet._id |
| 15 | checkSheetName | String | - | Yes | Display value of checkSheetId, copied from u_mes_qual_checkSheet.name | `"Start of shift check, Piston and Seal Assembly Station"` |  |
| 16 | frequencyType | String | - | Yes | Frequency | `"Shift"` | Shift; Daily; Weekly; Monthly |
| 17 | frequencyValue | Decimal128 | - | Yes | Every n periods | `NumberDecimal("1")` |  |
| 18 | auditorRoleId | String | - | Yes | Reference to u_mes_mast_role._id: auditor role | `"1026000000000003"` | Reference: u_mes_mast_role._id |
| 19 | auditorRoleName | String | - | Yes | Display value of auditorRoleId, copied from u_mes_mast_role.name | `"Line Leader"` |  |
| 20 | auditorUserId | String | - | No (null allowed) | Reference to u_mes_mast_user._id: auditor user | `null` | Reference: u_mes_mast_user._id |
| 21 | auditorUserName | String | - | No (null allowed) | Display value of auditorUserId, copied from u_mes_mast_user.fullName | `null` |  |
| 22 | toleranceHours | Int32 | - | Yes | Grace period before the audit counts as missed | `NumberInt(4)` |  |
| 23 | escalationRuleId | String | - | No (null allowed) | Reference to u_mes_syst_escalationRule._id | `"1334000000000006"` | Reference: u_mes_syst_escalationRule._id |
| 24 | escalationRuleName | String | - | No (null allowed) | Display value of escalationRuleId, copied from u_mes_syst_escalationRule.name | `"Missed layered process audit"` |  |
| 25 | nextDueDate | Date | Date | Yes | Next due date | `ISODate("2026-09-28T00:00:00.000+0000")` |  |
| 26 | validFrom | Date | Date | Yes | Valid from | `ISODate("2026-04-01T00:00:00.000+0000")` |  |
| 27 | validTo | Date | Date | No (null allowed) | Valid to | `null` |  |
| 28 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 29 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ areaId: 1 }` | No | Look-up of documents by area |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 6 | `{ checkSheetId: 1 }` | No | Look-up of documents by check sheet |
| 7 | `{ auditorRoleId: 1 }` | No | Look-up of documents by auditor role |

## Referenced by

u_mes_qual_audit.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_auditSchedule.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_auditSchedule.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_auditSchedule.js
