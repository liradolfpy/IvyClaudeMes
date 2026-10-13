# u_mes_bmr_batchRelease

| Property | Value |
|---|---|
| Module | Batch Manufacturing Record (bmr) |
| Purpose | Release decision of the quality unit for a lot after review of its production record: released, conditionally released under a deviation, or rejected. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 36 (20 required, 16 may be null) |
| Estimated volume per year | about 2,500 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per batch release, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1352000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"BRL-PCM5G26091-S2"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `"1096000000000012"` | Reference: u_mes_plan_lot._id |
| 7 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"PCM5G26091-S2"` |  |
| 8 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000014"` | Reference: u_mes_plan_productionOrder._id |
| 9 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PCM5G26091"` |  |
| 10 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000014"` | Reference: u_mes_prod_item._id |
| 11 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Paracetamol 500 mg lubricated granules and core tablets, bulk"` |  |
| 12 | batchRecordReviewId | String | - | No (null allowed) | Reference to u_mes_bmr_batchRecordReview._id | `"1350000000000004"` | Reference: u_mes_bmr_batchRecordReview._id |
| 13 | batchRecordReviewName | String | - | No (null allowed) | Display value of batchRecordReviewId, copied from u_mes_bmr_batchRecordReview.recordNo | `"BRR-PCM5G26091"` |  |
| 14 | releaseQuantity | Int32 | - | Yes | Quantity covered by the decision | `NumberInt(150)` |  |
| 15 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000012"` | Reference: u_mes_mast_unitOfMeasure._id |
| 16 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Kilogram"` |  |
| 17 | deviationPermitId | String | - | No (null allowed) | Reference to u_mes_qual_deviationPermit._id | `"1174000000000012"` | Reference: u_mes_qual_deviationPermit._id |
| 18 | deviationPermitName | String | - | No (null allowed) | Display value of deviationPermitId, copied from u_mes_qual_deviationPermit.title | `"Granulation with binder pump in manual mode for one batch"` |  |
| 19 | qualityHoldId | String | - | No (null allowed) | Reference to u_mes_qual_qualityHold._id | `null` | Reference: u_mes_qual_qualityHold._id |
| 20 | qualityHoldName | String | - | No (null allowed) | Display value of qualityHoldId, copied from u_mes_qual_qualityHold.recordNo | `null` |  |
| 21 | certificateControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: certificate controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 22 | certificateControlledDocumentName | String | - | No (null allowed) | Display value of certificateControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 23 | releasedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'released' | `null` | Reference: u_mes_mast_user._id |
| 24 | releasedBy | String | - | No (null allowed) | Display name of the user in releasedById, copied from u_mes_mast_user.fullName | `null` |  |
| 25 | releasedAt | Date | Datetime | No (null allowed) | Time of the decision | `ISODate("2026-09-18T11:30:00.000+0000")` |  |
| 26 | electronicSignatureId | String | - | No (null allowed) | Reference to u_mes_syst_electronicSignature._id | `null` | Reference: u_mes_syst_electronicSignature._id |
| 27 | electronicSignatureName | String | - | No (null allowed) | Display value of electronicSignatureId, copied from u_mes_syst_electronicSignature.recordNo | `null` |  |
| 28 | decisionText | String | - | No (null allowed) | Justification of the decision | `"Released to blending under deviation DEV-2026-0007 (binder pump in manual mode); loss on drying and particle size within limits"` |  |
| 29 | status | String | - | Yes | Primary lifecycle state of the document | `"Conditionally Released"` | Pending; Released; Conditionally Released; Rejected |
| 30 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 31 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-18T11:30:00.000+0000")` |  |
| 32 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 33 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 34 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-18T11:30:00.000+0000")` |  |
| 35 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 36 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |

## Status values

Pending, Released, Conditionally Released, Rejected. Initial state: Pending. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 4 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 5 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 6 | `{ batchRecordReviewId: 1 }` | No | Look-up of documents by batch record review |
| 7 | `{ unitOfMeasureId: 1 }` | No | Look-up of documents by unit of measure |
| 8 | `{ siteId: 1, releasedAt: -1 }` | No | Time-ordered lists and reports by released at |

## Referenced by

u_mes_plan_lot, u_mes_bmr_batchManufacturingRecord.

## Files

- Validator: 03_design/11_batch_manufacturing_record/validators/u_mes_bmr_batchRelease.json
- Indexes: 03_design/11_batch_manufacturing_record/indexes/u_mes_bmr_batchRelease.js
- Sample documents (10): 03_design/11_batch_manufacturing_record/samples/u_mes_bmr_batchRelease.js
