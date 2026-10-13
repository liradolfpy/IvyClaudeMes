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
| Keys | 36 (21 required, 15 may be null) |
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
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"BRR-PO-1000412"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 7 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 8 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 9 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `null` | Reference: u_mes_plan_lot._id |
| 10 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `null` |  |
| 11 | reviewScope | String | - | Yes | Review method | `"Review By Exception"` | Review By Exception; Full Review |
| 12 | operationsCount | Int32 | - | Yes | Operation executions in the record | `NumberInt(2385)` |  |
| 13 | exceptionCount | Int32 | - | Yes | Exceptions found | `NumberInt(2)` |  |
| 14 | openExceptionCount | Int32 | - | Yes | Exceptions not yet assessed | `NumberInt(0)` |  |
| 15 | genealogyComplete | Boolean | - | Yes | Component genealogy of the order is complete | `true` |  |
| 16 | yieldReconciliationId | String | - | No (null allowed) | Reference to u_mes_bmr_yieldReconciliation._id | `"1353000000000001"` | Reference: u_mes_bmr_yieldReconciliation._id |
| 17 | yieldReconciliationName | String | - | No (null allowed) | Display value of yieldReconciliationId, copied from u_mes_bmr_yieldReconciliation.recordNo | `"YRC-PO-1000412-01"` |  |
| 18 | auditTrailReviewId | String | - | No (null allowed) | Reference to u_mes_syst_auditTrailReview._id | `"1347000000000001"` | Reference: u_mes_syst_auditTrailReview._id |
| 19 | auditTrailReviewName | String | - | No (null allowed) | Display value of auditTrailReviewId, copied from u_mes_syst_auditTrailReview.recordNo | `"ATR-20260916-001"` |  |
| 20 | productionReviewedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'production reviewed' | `"1029000000000005"` | Reference: u_mes_mast_user._id |
| 21 | productionReviewedBy | String | - | No (null allowed) | Display name of the user in productionReviewedById, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 22 | productionReviewedAt | Date | Datetime | No (null allowed) | Time of the production review | `ISODate("2026-09-15T15:10:00.000+0000")` |  |
| 23 | qaReviewedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'qa reviewed' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 24 | qaReviewedBy | String | - | No (null allowed) | Display name of the user in qaReviewedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 25 | qaReviewedAt | Date | Datetime | No (null allowed) | Time of the quality review | `ISODate("2026-09-16T10:20:00.000+0000")` |  |
| 26 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `null` | Reference: u_mes_syst_electronicSignature._id |
| 27 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 28 | returnReasonText | String | - | No (null allowed) | Why the record was returned for correction | `null` |  |
| 29 | status | String | - | Yes | Primary lifecycle state of the document | `"Approved"` | Open; Under Review; Returned For Correction; Approved; Rejected |
| 30 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 31 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T15:10:00.000+0000")` |  |
| 32 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 33 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 34 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T10:20:00.000+0000")` |  |
| 35 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 36 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

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
