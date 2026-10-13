# u_mes_plan_lineClearance

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | Check that a line or station is free of materials, labels, documents and product of the previous order before the next order starts, with a second-person verification. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 39 (24 required, 15 may be null) |
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
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000006"` | Reference: u_mes_mast_line._id |
| 6 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Front Caliper Assembly Line 1"` |  |
| 7 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `null` | Reference: u_mes_mast_workCenter._id |
| 8 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `null` |  |
| 9 | clearanceType | String | - | Yes | When the clearance is done | `"Before Order Start"` | Before Order Start; Order Changeover; After Order Completion; After Maintenance |
| 10 | previousProductionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id: previous production order | `null` | Reference: u_mes_plan_productionOrder._id |
| 11 | previousProductionOrderName | String | - | No (null allowed) | Display value of previousProductionOrderId, copied from u_mes_plan_productionOrder.recordNo | `null` |  |
| 12 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 13 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 14 | changeoverId | String | - | No (null allowed) | Reference to u_mes_plan_changeover._id | `null` | Reference: u_mes_plan_changeover._id |
| 15 | changeoverName | String | - | No (null allowed) | Display value of changeoverId, copied from u_mes_plan_changeover.recordNo | `null` |  |
| 16 | checkSheetResultId | String | - | No (null allowed) | Reference to u_mes_qual_checkSheetResult._id | `"1148000000000006"` | Reference: u_mes_qual_checkSheetResult._id |
| 17 | checkSheetResultName | String | - | No (null allowed) | Display value of checkSheetResultId, copied from u_mes_qual_checkSheetResult.recordNo | `"CKR-2026-000494"` |  |
| 18 | materialsRemoved | Boolean | - | Yes | No components or product of the previous order left | `true` |  |
| 19 | labelsRemoved | Boolean | - | Yes | No labels or printed packaging of the previous order left | `true` |  |
| 20 | documentsRemoved | Boolean | - | Yes | No documents of the previous order left | `true` |  |
| 21 | equipmentClean | Boolean | - | Yes | Equipment in clean status | `true` |  |
| 22 | performedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'performed' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 23 | performedBy | String | - | Yes | Display name of the user in performedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 24 | startedAt | Date | Datetime | Yes | Start of the clearance | `ISODate("2026-09-15T05:40:00.000+0000")` |  |
| 25 | completedAt | Date | Datetime | No (null allowed) | End of the clearance | `ISODate("2026-09-15T05:52:00.000+0000")` |  |
| 26 | verifiedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'verified' | `"1029000000000005"` | Reference: u_mes_mast_user._id |
| 27 | verifiedBy | String | - | No (null allowed) | Display name of the user in verifiedById, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 28 | verifiedAt | Date | Datetime | No (null allowed) | Time of the verification | `ISODate("2026-09-15T05:55:00.000+0000")` |  |
| 29 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `null` | Reference: u_mes_syst_electronicSignature._id |
| 30 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 31 | failureText | String | - | No (null allowed) | What was found when the clearance failed | `null` |  |
| 32 | status | String | - | Yes | Primary lifecycle state of the document | `"Verified"` | In Progress; Passed; Failed; Verified |
| 33 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 34 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T05:40:00.000+0000")` |  |
| 35 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 36 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 37 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T05:55:00.000+0000")` |  |
| 38 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 39 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

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
