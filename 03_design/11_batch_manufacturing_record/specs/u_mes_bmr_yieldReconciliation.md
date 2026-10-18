# u_mes_bmr_yieldReconciliation

| Property | Value |
|---|---|
| Module | BatchManufacturingRecord (bmr) |
| Purpose | Calculated yield of an order, and reconciliation of issued components and labels against use, return and destruction, with the limits and the outcome. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 37 (32 required, 5 may be null) |
| Estimated volume per year | about 7,500 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per yield reconciliation, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1353000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"YRC-PCM5B26091-01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Gamp"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000011"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Ranjangaon OSD Plant, Pune"` |  |
| 6 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000011"` | Reference: u_mes_plan_productionOrder._id |
| 7 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PCM5B26091"` |  |
| 8 | reconciliationType | String | - | Yes | What is reconciled | `"Product Yield"` | Product Yield; Component Reconciliation; Label Reconciliation |
| 9 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000011"` | Reference: u_mes_prod_item._id |
| 10 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Paracetamol Tablets IP 500 mg, blister 10 x 10"` |  |
| 11 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000011"` | Reference: u_mes_mast_unitOfMeasure._id |
| 12 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 13 | theoreticalQuantity | Decimal128 | - | Yes | Quantity expected from the order quantity | `4800` |  |
| 14 | issuedQuantity | Decimal128 | - | Yes | Quantity issued or started | `4800` |  |
| 15 | outputQuantity | Decimal128 | - | Yes | Good output, or quantity used | `4741` |  |
| 16 | rejectedQuantity | Decimal128 | - | Yes | Rejected or scrapped | `22` |  |
| 17 | destroyedQuantity | Decimal128 | - | Yes | Destroyed (damaged labels, test pieces) | `25` |  |
| 18 | returnedQuantity | Decimal128 | - | Yes | Returned to stores | `12` |  |
| 19 | unaccountedQuantity | Decimal128 | - | Yes | Issued minus output, rejected, destroyed and returned | `0` |  |
| 20 | yieldPct | Decimal128 | - | Yes | Yield (percent) | `98.77` |  |
| 21 | lowerLimitPct | Decimal128 | - | Yes | Lower acceptance limit (percent) | `98.00` |  |
| 22 | upperLimitPct | Decimal128 | - | Yes | Upper acceptance limit (percent) | `100.00` |  |
| 23 | withinLimits | Boolean | - | Yes | True when the yield is within limits and nothing is unaccounted | `true` |  |
| 24 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `null` | Reference: u_mes_qual_nonconformance._id |
| 25 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `null` |  |
| 26 | calculatedAt | Date | Datetime | Yes | Time of the calculation | `ISODate("2026-09-15T14:05:00.000+0000")` |  |
| 27 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 28 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 29 | approvedAt | Date | Datetime | No (null allowed) | Approval time | `ISODate("2026-09-16T10:15:00.000+0000")` |  |
| 30 | status | String | - | Yes | Primary lifecycle state of the document | `"Approved"` | Calculated; Under Investigation; Approved |
| 31 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 32 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T14:05:00.000+0000")` |  |
| 33 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 34 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |
| 35 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T10:15:00.000+0000")` |  |
| 36 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000014"` | Reference: u_mes_mast_user._id |
| 37 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Shalini Rao"` |  |

## Status values

Calculated, Under Investigation, Approved. Initial state: Calculated. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 4 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 5 | `{ unitOfMeasureId: 1 }` | No | Look-up of documents by unit of measure |
| 6 | `{ nonconformanceId: 1 }` | No | Look-up of documents by nonconformance |
| 7 | `{ siteId: 1, calculatedAt: -1 }` | No | Time-ordered lists and reports by calculated at |

## Referenced by

u_mes_bmr_batchRecordReview, u_mes_bmr_batchManufacturingRecord.

## Files

- Validator: 03_design/11_batch_manufacturing_record/validators/u_mes_bmr_yieldReconciliation.json
- Indexes: 03_design/11_batch_manufacturing_record/indexes/u_mes_bmr_yieldReconciliation.js
- Sample documents (10): 03_design/11_batch_manufacturing_record/samples/u_mes_bmr_yieldReconciliation.js
