# u_mes_qual_checkSheetResult

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Completed check sheets with answers, failures and reactions |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | CKR-<recordNo> |
| Display value used by references | recordNo |
| Keys | 36 (25 required, 11 may be null) |
| Estimated volume per year | ~150,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per check sheet result, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with checkSheetResultId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_checkSheetResultAnswer | Child | answer |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: CKR-<recordNo> | `"CKR-20260929-A-TRQ-01"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-A-TRQ-01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | checkSheetId | String | Yes | Reference to u_mes_qual_checkSheet._id | `"CKS-TRQ-01-SOS"` | Reference: u_mes_qual_checkSheet._id |
| 6 | checkSheetName | String | Yes | Display value of checkSheetId, copied from u_mes_qual_checkSheet.name | `"Start of shift check, torque station"` |  |
| 7 | checkSheetVersion | Int32 | Yes | Check sheet version | `NumberInt(2)` |  |
| 8 | workCenterId | String | Yes | Reference to u_mes_mast_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mast_workCenter._id |
| 9 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 10 | equipmentId | String | No (null allowed) | Reference to u_mes_mast_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mast_equipment._id |
| 11 | equipmentName | String | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 12 | shiftId | String | Yes | Reference to u_mes_mast_shift._id | `"SH-A"` | Reference: u_mes_mast_shift._id |
| 13 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 14 | productionDate | Date | Yes | Production date (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-09-28T18:30:00.000+0000")` |  |
| 15 | productionOrderId | String | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"PO-1000412"` | Reference: u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"1000412"` |  |
| 17 | performedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'performed' | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 18 | performedBy | String | Yes | Display name of the user in performedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 19 | startedAt | Date | Yes | Date and time when the record was started | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 20 | completedAt | Date | No (null allowed) | Date and time when the record was completed | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 21 | overallResult | String | Yes | Overall result | `"Pass"` | Pass; Fail |
| 22 | failedCount | Int32 | Yes | Failed count | `NumberInt(0)` |  |
| 23 | reactionTaken | String | No (null allowed) | Reaction taken | `null` |  |
| 24 | verifiedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'verified' | `"USR-10019"` | Reference: u_mes_mast_user._id |
| 25 | verifiedBy | String | No (null allowed) | Display name of the user in verifiedById, copied from u_mes_mast_user.fullName | `"Meera Deshpande"` |  |
| 26 | verifiedAt | Date | No (null allowed) | Date and time when the record was verified | `ISODate("2026-09-29T00:30:54.000+0000")` |  |
| 27 | nonconformanceId | String | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `"NCR-2026-000118"` | Reference: u_mes_qual_nonconformance._id |
| 28 | nonconformanceName | String | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `"Leak test failures on caliper LH"` |  |
| 29 | status | String | Yes | Primary lifecycle state of the document | `"Completed"` | In Progress; Completed; Verified |
| 30 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 31 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 32 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 33 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 34 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:54.000+0000")` |  |
| 35 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mast_user._id |
| 36 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

In Progress, Completed, Verified. Initial state: In Progress. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ checkSheetId: 1 }` | No | Look-up of documents by check sheet |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 6 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 7 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 8 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

u_mes_plan_changeover, u_mes_qual_checkSheetResultAnswer.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_checkSheetResult.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_checkSheetResult.js
- Sample document: 03_design/06_quality_management/samples/u_mes_qual_checkSheetResult.js
