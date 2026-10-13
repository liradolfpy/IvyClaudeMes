# u_mes_bmr_batchRecordReview

| Property | Value |
|---|---|
| Module | Batch Manufacturing Record (bmr) |
| Purpose | Review of the electronic production record of an order before release: production review, quality review by exception, exceptions found and their closure. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 37 (22 required, 15 may be null) |
| Estimated volume per year | about 2,500 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per batch record review, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with batchRecordReviewId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_bmr_batchRecordReviewException | Child | exception |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1350000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"BRR-PCM5B26091"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000011"` | Reference: u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PCM5B26091"` |  |
| 8 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000011"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Paracetamol Tablets IP 500 mg, blister 10 x 10"` |  |
| 10 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `null` | Reference: u_mes_plan_lot._id |
| 11 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `null` |  |
| 12 | reviewScope | String | - | Yes | Review method | `"Review By Exception"` | Review By Exception; Full Review |
| 13 | operationsCount | Int32 | - | Yes | Operation executions in the record | `NumberInt(486)` |  |
| 14 | exceptionCount | Int32 | - | Yes | Exceptions found | `NumberInt(2)` |  |
| 15 | openExceptionCount | Int32 | - | Yes | Exceptions not yet assessed | `NumberInt(0)` |  |
| 16 | genealogyComplete | Boolean | - | Yes | Component genealogy of the order is complete | `true` |  |
| 17 | yieldReconciliationId | String | - | No (null allowed) | Reference to u_mes_bmr_yieldReconciliation._id | `"1353000000000001"` | Reference: u_mes_bmr_yieldReconciliation._id |
| 18 | yieldReconciliationName | String | - | No (null allowed) | Display value of yieldReconciliationId, copied from u_mes_bmr_yieldReconciliation.recordNo | `"YRC-PCM5B26091-01"` |  |
| 19 | auditTrailReviewId | String | - | No (null allowed) | Reference to u_mes_syst_auditTrailReview._id | `"1347000000000001"` | Reference: u_mes_syst_auditTrailReview._id |
| 20 | auditTrailReviewName | String | - | No (null allowed) | Display value of auditTrailReviewId, copied from u_mes_syst_auditTrailReview.recordNo | `"ATR-20260916-001"` |  |
| 21 | productionReviewedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'production reviewed' | `"1029000000000015"` | Reference: u_mes_mast_user._id |
| 22 | productionReviewedBy | String | - | No (null allowed) | Display name of the user in productionReviewedById, copied from u_mes_mast_user.fullName | `"Nilesh Sawant"` |  |
| 23 | productionReviewedAt | Date | Datetime | No (null allowed) | Time of the production review | `ISODate("2026-09-15T15:10:00.000+0000")` |  |
| 24 | qaReviewedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'qa reviewed' | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 25 | qaReviewedBy | String | - | No (null allowed) | Display name of the user in qaReviewedById, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 26 | qaReviewedAt | Date | Datetime | No (null allowed) | Time of the quality review | `ISODate("2026-09-16T10:20:00.000+0000")` |  |
| 27 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `null` | Reference: u_mes_syst_electronicSignature._id |
| 28 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 29 | returnReasonText | String | - | No (null allowed) | Why the record was returned for correction | `null` |  |
| 30 | status | String | - | Yes | Primary lifecycle state of the document | `"Approved"` | Open; Under Review; Returned For Correction; Approved; Rejected |
| 31 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 32 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T15:10:00.000+0000")` |  |
| 33 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 34 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 35 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T10:20:00.000+0000")` |  |
| 36 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 37 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |

## Status values

Open, Under Review, Returned For Correction, Approved, Rejected. Initial state: Open. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 4 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 5 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 6 | `{ yieldReconciliationId: 1 }` | No | Look-up of documents by yield reconciliation |
| 7 | `{ auditTrailReviewId: 1 }` | No | Look-up of documents by audit trail review |
| 8 | `{ siteId: 1, productionReviewedAt: -1 }` | No | Time-ordered lists and reports by production reviewed at |

## Referenced by

u_mes_plan_productionOrder, u_mes_bmr_batchRecordReviewException, u_mes_bmr_batchRelease, u_mes_bmr_batchManufacturingRecord.

## Files

- Validator: 03_design/11_batch_manufacturing_record/validators/u_mes_bmr_batchRecordReview.json
- Indexes: 03_design/11_batch_manufacturing_record/indexes/u_mes_bmr_batchRecordReview.js
- Sample documents (10): 03_design/11_batch_manufacturing_record/samples/u_mes_bmr_batchRecordReview.js
