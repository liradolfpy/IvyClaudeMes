# u_mes_plan_lineClearance

| Property | Value |
|---|---|
| Module | PlanningAndExecution (plan) |
| Purpose | Check that a line or station is free of materials, labels, documents and product of the previous order before the next order starts, with a second-person verification. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 40 (25 required, 15 may be null) |
| Estimated volume per year | about 3,000 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per line clearance, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1354000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"LCL-20260915-001"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000016"` | Reference: u_mes_mast_line._id |
| 7 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Blister Packing Line 1"` |  |
| 8 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `null` | Reference: u_mes_mast_workCenter._id |
| 9 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `null` |  |
| 10 | clearanceType | String | - | Yes | When the clearance is done | `"Before Order Start"` | Before Order Start; Order Changeover; After Order Completion; After Maintenance |
| 11 | previousProductionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id: previous production order | `null` | Reference: u_mes_plan_productionOrder._id |
| 12 | previousProductionOrderName | String | - | No (null allowed) | Display value of previousProductionOrderId, copied from u_mes_plan_productionOrder.recordNo | `null` |  |
| 13 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000011"` | Reference: u_mes_plan_productionOrder._id |
| 14 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PCM5B26091"` |  |
| 15 | changeoverId | String | - | No (null allowed) | Reference to u_mes_plan_changeover._id | `null` | Reference: u_mes_plan_changeover._id |
| 16 | changeoverName | String | - | No (null allowed) | Display value of changeoverId, copied from u_mes_plan_changeover.recordNo | `null` |  |
| 17 | checkSheetResultId | String | - | No (null allowed) | Reference to u_mes_qual_checkSheetResult._id | `"1148000000000016"` | Reference: u_mes_qual_checkSheetResult._id |
| 18 | checkSheetResultName | String | - | No (null allowed) | Display value of checkSheetResultId, copied from u_mes_qual_checkSheetResult.recordNo | `"CKR-2026-000994"` |  |
| 19 | materialsRemoved | Boolean | - | Yes | No components or product of the previous order left | `true` |  |
| 20 | labelsRemoved | Boolean | - | Yes | No labels or printed packaging of the previous order left | `true` |  |
| 21 | documentsRemoved | Boolean | - | Yes | No documents of the previous order left | `true` |  |
| 22 | equipmentClean | Boolean | - | Yes | Equipment in clean status | `true` |  |
| 23 | performedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'performed' | `"1029000000000011"` | Reference: u_mes_mast_user._id |
| 24 | performedBy | String | - | Yes | Display name of the user in performedById, copied from u_mes_mast_user.fullName | `"Amol Shinde"` |  |
| 25 | startedAt | Date | Datetime | Yes | Start of the clearance | `ISODate("2026-09-15T05:40:00.000+0000")` |  |
| 26 | completedAt | Date | Datetime | No (null allowed) | End of the clearance | `ISODate("2026-09-15T05:52:00.000+0000")` |  |
| 27 | verifiedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'verified' | `"1029000000000015"` | Reference: u_mes_mast_user._id |
| 28 | verifiedBy | String | - | No (null allowed) | Display name of the user in verifiedById, copied from u_mes_mast_user.fullName | `"Nilesh Sawant"` |  |
| 29 | verifiedAt | Date | Datetime | No (null allowed) | Time of the verification | `ISODate("2026-09-15T05:55:00.000+0000")` |  |
| 30 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `null` | Reference: u_mes_syst_electronicSignature._id |
| 31 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 32 | failureText | String | - | No (null allowed) | What was found when the clearance failed | `null` |  |
| 33 | status | String | - | Yes | Primary lifecycle state of the document | `"Verified"` | In Progress; Passed; Failed; Verified |
| 34 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 35 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T05:40:00.000+0000")` |  |
| 36 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000011"` | Reference: u_mes_mast_user._id |
| 37 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Amol Shinde"` |  |
| 38 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T05:55:00.000+0000")` |  |
| 39 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000011"` | Reference: u_mes_mast_user._id |
| 40 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Amol Shinde"` |  |

## Status values

In Progress, Passed, Failed, Verified. Initial state: In Progress. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ previousProductionOrderId: 1 }` | No | Look-up of documents by previous production order |
| 6 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 7 | `{ changeoverId: 1 }` | No | Look-up of documents by changeover |
| 8 | `{ siteId: 1, startedAt: -1 }` | No | Time-ordered lists and reports by started at |

## Referenced by

u_mes_plan_productionOrder, u_mes_maint_logbookEntry, u_mes_bmr_batchManufacturingRecord.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_lineClearance.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_lineClearance.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_lineClearance.js
