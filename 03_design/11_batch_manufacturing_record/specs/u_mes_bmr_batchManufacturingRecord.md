# u_mes_bmr_batchManufacturingRecord

| Property | Value |
|---|---|
| Module | Batch Manufacturing Record (bmr) |
| Purpose | Header of the executed batch record of one production order: the master record version frozen at opening, links to line clearance, yield reconciliation, review and release, and the exported true copy of the compiled record with its checksum. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 40 (21 required, 19 may be null) |
| Estimated volume per year | about 2,500 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per batch manufacturing record, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1369000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"BMR-PO-1000412"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 7 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 8 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 9 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `null` | Reference: u_mes_plan_lot._id |
| 10 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `null` |  |
| 11 | masterManufacturingRecordId | String | - | Yes | Reference to u_mes_mmr_masterManufacturingRecord._id | `"1367000000000001"` | Reference: u_mes_mmr_masterManufacturingRecord._id |
| 12 | masterManufacturingRecordName | String | - | Yes | Display value of masterManufacturingRecordId, copied from u_mes_mmr_masterManufacturingRecord.title | `"Front brake caliper assembly LH, master manufacturing record version 3"` |  |
| 13 | masterRecordVersion | Int32 | - | Yes | Version number of the frozen master record | `NumberInt(3)` |  |
| 14 | plannedQuantity | Int32 | - | Yes | Batch size of the order | `NumberInt(480)` |  |
| 15 | lineClearanceId | String | - | No (null allowed) | Reference to u_mes_plan_lineClearance._id | `"1354000000000001"` | Reference: u_mes_plan_lineClearance._id |
| 16 | lineClearanceName | String | - | No (null allowed) | Display value of lineClearanceId, copied from u_mes_plan_lineClearance.recordNo | `"LCL-20260915-001"` |  |
| 17 | yieldReconciliationId | String | - | No (null allowed) | Reference to u_mes_bmr_yieldReconciliation._id | `"1353000000000001"` | Reference: u_mes_bmr_yieldReconciliation._id |
| 18 | yieldReconciliationName | String | - | No (null allowed) | Display value of yieldReconciliationId, copied from u_mes_bmr_yieldReconciliation.recordNo | `"YRC-PO-1000412-01"` |  |
| 19 | batchRecordReviewId | String | - | No (null allowed) | Reference to u_mes_bmr_batchRecordReview._id | `"1350000000000001"` | Reference: u_mes_bmr_batchRecordReview._id |
| 20 | batchRecordReviewName | String | - | No (null allowed) | Display value of batchRecordReviewId, copied from u_mes_bmr_batchRecordReview.recordNo | `"BRR-PO-1000412"` |  |
| 21 | batchReleaseId | String | - | No (null allowed) | Reference to u_mes_bmr_batchRelease._id | `"1352000000000005"` | Reference: u_mes_bmr_batchRelease._id |
| 22 | batchReleaseName | String | - | No (null allowed) | Display value of batchReleaseId, copied from u_mes_bmr_batchRelease.recordNo | `"BRL-PO-1000412"` |  |
| 23 | openedAt | Date | Datetime | Yes | Time the record was opened and the master record frozen | `ISODate("2026-09-15T05:30:00.000+0000")` |  |
| 24 | compiledAt | Date | Datetime | No (null allowed) | Time the record was compiled after the last operation | `ISODate("2026-09-15T13:45:00.000+0000")` |  |
| 25 | exportControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: export controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 26 | exportControlledDocumentName | String | - | No (null allowed) | Display value of exportControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 27 | checksumSha256 | String | - | No (null allowed) | SHA-256 checksum of the exported copy | `"b913f6afb3f5c6349ff803631b07d1934cbcbf5d4568e38e485f5d84f6e35a8e"` |  |
| 28 | pageCount | Int32 | - | No (null allowed) | Pages of the exported copy | `NumberInt(46)` |  |
| 29 | exportedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'exported' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 30 | exportedBy | String | - | No (null allowed) | Display name of the user in exportedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 31 | exportedAt | Date | Datetime | No (null allowed) | Export time | `ISODate("2026-09-16T10:45:00.000+0000")` |  |
| 32 | archivedAt | Date | Datetime | No (null allowed) | Time the record was archived | `null` |  |
| 33 | status | String | - | Yes | Primary lifecycle state of the document | `"Approved"` | Open; In Execution; Compiled; Under Review; Approved; Archived |
| 34 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 35 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T05:30:00.000+0000")` |  |
| 36 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 37 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 38 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T10:45:00.000+0000")` |  |
| 39 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 40 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Open, In Execution, Compiled, Under Review, Approved, Archived. Initial state: Open. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 4 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 5 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 6 | `{ masterManufacturingRecordId: 1 }` | No | Look-up of documents by master manufacturing record |
| 7 | `{ lineClearanceId: 1 }` | No | Look-up of documents by line clearance |
| 8 | `{ siteId: 1, openedAt: -1 }` | No | Time-ordered lists and reports by opened at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/11_batch_manufacturing_record/validators/u_mes_bmr_batchManufacturingRecord.json
- Indexes: 03_design/11_batch_manufacturing_record/indexes/u_mes_bmr_batchManufacturingRecord.js
- Sample documents (10): 03_design/11_batch_manufacturing_record/samples/u_mes_bmr_batchManufacturingRecord.js
