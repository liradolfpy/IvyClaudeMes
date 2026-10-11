# u_mes_qual_nonconformance

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Nonconformance reports: what, where, quantity, containment, disposition (use-as-is, rework, scrap, return) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 45 (31 required, 14 may be null) |
| Estimated volume per year | ~9,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per nonconformance, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with nonconformanceId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_qual_nonconformanceAffectedObject | Child | affected object |
| u_mes_qual_nonconformanceContainmentAction | Child | containment action |
| u_mes_qual_nonconformanceInspectionResult | Relationship | inspection result |
| u_mes_qual_nonconformanceReworkOrder | Relationship | rework order |
| u_mes_qual_nonconformanceScrapRecord | Relationship | scrap record |
| u_mes_qual_nonconformancePhotoControlledDocument | Relationship | photo controlled document |
| u_mes_qual_nonconformanceMrbUser | Relationship | mrb user |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1160000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"NCR-2026-000118"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | Yes | Title of the nonconformance; used as its display value in other collections | `"Shrinkage porosity found on casting lot from die 2"` |  |
| 6 | description | String | Yes | Description of the nonconformance | `"Porosity visible on machined face or found by X-ray sampling. Ejector pin sticks on cavity 2 and the casting does not release"` |  |
| 7 | ncType | String | Yes | Nc type | `"Internal"` | Internal; Supplier; Customer |
| 8 | source | String | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 9 | detectedAt | Date | Yes | Date and time when the record was detected | `ISODate("2026-09-15T00:30:00.000+0000")` |  |
| 10 | detectedById | String | Yes | Reference to u_mes_mast_user._id: user recorded for 'detected' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 11 | detectedBy | String | Yes | Display name of the user in detectedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 12 | detectedAtOperationId | String | Yes | Reference to u_mes_prod_operation._id: detected at operation | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 13 | detectedAtOperationName | String | Yes | Display value of detectedAtOperationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 14 | detectedAtWorkCenterId | String | Yes | Reference to u_mes_mast_workCenter._id: detected at work center | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 15 | detectedAtWorkCenterName | String | Yes | Display value of detectedAtWorkCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 16 | originOperationId | String | No (null allowed) | Reference to u_mes_prod_operation._id: origin operation | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 17 | originOperationName | String | No (null allowed) | Display value of originOperationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 18 | itemId | String | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 19 | itemName | String | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 20 | defectCodeId | String | Yes | Reference to u_mes_qual_defectCode._id | `"1158000000000001"` | Reference: u_mes_qual_defectCode._id |
| 21 | defectCodeName | String | Yes | Display value of defectCodeId, copied from u_mes_qual_defectCode.name | `"Shrinkage porosity"` |  |
| 22 | supplierId | String | No (null allowed) | Reference to u_mes_mast_supplier._id | `null` | Reference: u_mes_mast_supplier._id |
| 23 | supplierName | String | No (null allowed) | Display value of supplierId, copied from u_mes_mast_supplier.name | `null` |  |
| 24 | customerId | String | No (null allowed) | Reference to u_mes_mast_customer._id | `null` | Reference: u_mes_mast_customer._id |
| 25 | customerName | String | No (null allowed) | Display value of customerId, copied from u_mes_mast_customer.name | `null` |  |
| 26 | quantityAffected | Int32 | Yes | Quantity affected | `NumberInt(480)` |  |
| 27 | quantityRejected | Int32 | Yes | Quantity rejected | `NumberInt(6)` |  |
| 28 | qualityHoldId | String | No (null allowed) | Reference to u_mes_qual_qualityHold._id | `"1172000000000005"` | Reference: u_mes_qual_qualityHold._id |
| 29 | qualityHoldName | String | No (null allowed) | Display value of qualityHoldId, copied from u_mes_qual_qualityHold.recordNo | `"HLD-2026-000029"` |  |
| 30 | capaId | String | No (null allowed) | Reference to u_mes_qual_capa._id | `"1176000000000001"` | Reference: u_mes_qual_capa._id |
| 31 | capaName | String | No (null allowed) | Display value of capaId, copied from u_mes_qual_capa.title | `"8D - Shrinkage porosity in bridge section"` |  |
| 32 | rootCauseSummary | String | No (null allowed) | Root cause summary | `"Ejector pin galled after die coating build-up"` |  |
| 33 | severity | Int32 | Yes | Severity rating 1 to 10 | `NumberInt(8)` |  |
| 34 | costInr | Decimal128 | Yes | Cost (Indian rupees) | `NumberDecimal("8640.00")` |  |
| 35 | closedAt | Date | No (null allowed) | Date and time when the record was closed | `null` |  |
| 36 | closedById | String | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'closed' | `null` | Reference: u_mes_mast_user._id |
| 37 | closedBy | String | No (null allowed) | Display name of the user in closedById, copied from u_mes_mast_user.fullName | `null` |  |
| 38 | status | String | Yes | Primary lifecycle state of the document | `"Open"` | Open; Contained; Dispositioned; Closed; Cancelled |
| 39 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 40 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-15T00:30:00.000+0000")` |  |
| 41 | createdById | String | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 42 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 43 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-15T00:30:00.000+0000")` |  |
| 44 | updatedById | String | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 45 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Open, Contained, Dispositioned, Closed, Cancelled. Initial state: Open. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ detectedAtOperationId: 1 }` | No | Look-up of documents by detected at operation |
| 4 | `{ detectedAtWorkCenterId: 1 }` | No | Look-up of documents by detected at work center |
| 5 | `{ originOperationId: 1 }` | No | Look-up of documents by origin operation |
| 6 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 7 | `{ defectCodeId: 1 }` | No | Look-up of documents by defect code |
| 8 | `{ siteId: 1, detectedAt: -1 }` | No | Time-ordered lists and reports by detected at |

## Referenced by

u_mes_plan_shiftHandoverNonconformance, u_mes_qual_checkSheetResult, u_mes_qual_inspectionResult, u_mes_qual_spcSample, u_mes_qual_nonconformanceAffectedObject, u_mes_qual_nonconformanceContainmentAction, u_mes_qual_nonconformanceInspectionResult, u_mes_qual_nonconformanceReworkOrder, u_mes_qual_nonconformanceScrapRecord, u_mes_qual_nonconformancePhotoControlledDocument, u_mes_qual_nonconformanceMrbUser, u_mes_qual_reworkOrder, u_mes_qual_scrapRecord, u_mes_qual_qualityHold, u_mes_qual_deviationPermit, u_mes_qual_capaNonconformance, u_mes_qual_customerComplaint, u_mes_syst_notification.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_nonconformance.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_nonconformance.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_nonconformance.js
