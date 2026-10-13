# u_mes_bmr_yieldReconciliation

| Property | Value |
|---|---|
| Module | Batch Manufacturing Record (bmr) |
| Purpose | Calculated yield of an order, and reconciliation of issued components and labels against use, return and destruction, with the limits and the outcome. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 36 (31 required, 5 may be null) |
| Estimated volume per year | about 7,500 per year |
| Storage | standard collection |

## Structure

Flat entity collection: one document per yield reconciliation, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1353000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"YRC-PO-1000412-01"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | productionOrderId | String | - | Yes | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 6 | productionOrderName | String | - | Yes | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 7 | reconciliationType | String | - | Yes | What is reconciled | `"Product Yield"` | Product Yield; Component Reconciliation; Label Reconciliation |
| 8 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000001"` | Reference: u_mes_prod_item._id |
| 9 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 10 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 11 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 12 | theoreticalQuantity | Decimal128 | - | Yes | Quantity expected from the order quantity | `NumberDecimal("480")` |  |
| 13 | issuedQuantity | Decimal128 | - | Yes | Quantity issued or started | `NumberDecimal("480")` |  |
| 14 | outputQuantity | Decimal128 | - | Yes | Good output, or quantity used | `NumberDecimal("474")` |  |
| 15 | rejectedQuantity | Decimal128 | - | Yes | Rejected or scrapped | `NumberDecimal("2")` |  |
| 16 | destroyedQuantity | Decimal128 | - | Yes | Destroyed (damaged labels, test pieces) | `NumberDecimal("0")` |  |
| 17 | returnedQuantity | Decimal128 | - | Yes | Returned to stores | `NumberDecimal("4")` |  |
| 18 | unaccountedQuantity | Decimal128 | - | Yes | Issued minus output, rejected, destroyed and returned | `NumberDecimal("0")` |  |
| 19 | yieldPct | Decimal128 | - | Yes | Yield (percent) | `NumberDecimal("98.75")` |  |
| 20 | lowerLimitPct | Decimal128 | - | Yes | Lower acceptance limit (percent) | `NumberDecimal("98.00")` |  |
| 21 | upperLimitPct | Decimal128 | - | Yes | Upper acceptance limit (percent) | `NumberDecimal("100.00")` |  |
| 22 | withinLimits | Boolean | - | Yes | True when the yield is within limits and nothing is unaccounted | `true` |  |
| 23 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `null` | Reference: u_mes_qual_nonconformance._id |
| 24 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `null` |  |
| 25 | calculatedAt | Date | Datetime | Yes | Time of the calculation | `ISODate("2026-09-15T14:05:00.000+0000")` |  |
| 26 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 27 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 28 | approvedAt | Date | Datetime | No (null allowed) | Approval time | `ISODate("2026-09-16T10:15:00.000+0000")` |  |
| 29 | status | String | - | Yes | Primary lifecycle state of the document | `"Approved"` | Calculated; Under Investigation; Approved |
| 30 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 31 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T14:05:00.000+0000")` |  |
| 32 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 33 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 34 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-16T10:15:00.000+0000")` |  |
| 35 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 36 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

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
