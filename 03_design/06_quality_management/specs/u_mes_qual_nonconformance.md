# u_mes_qual_nonconformance

| Property | Value |
|---|---|
| Module | QualityManagement (qual) |
| Purpose | Nonconformance reports: what, where, quantity, containment, disposition (use-as-is, rework, scrap, return) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 54 (32 required, 22 may be null) |
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

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1160000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"NCR-2026-000118"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | title | String | - | Yes | Title of the nonconformance; used as its display value in other collections | `"Shrinkage porosity found on casting lot from die 2"` |  |
| 7 | description | String | - | Yes | Description of the nonconformance | `"Porosity visible on machined face or found by X-ray sampling. Ejector pin sticks on cavity 2 and the casting does not release"` |  |
| 8 | ncType | String | - | Yes | Nc type | `"Internal"` | Internal; Supplier; Customer |
| 9 | source | String | - | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 10 | detectedAt | Date | Datetime | Yes | Date and time when the record was detected. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 11 | detectedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'detected' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 12 | detectedBy | String | - | Yes | Display name of the user in detectedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 13 | detectedAtOperationId | String | - | Yes | Reference to u_mes_prod_operation._id: detected at operation | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 14 | detectedAtOperationName | String | - | Yes | Display value of detectedAtOperationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 15 | detectedAtWorkCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id: detected at work center | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 16 | detectedAtWorkCenterName | String | - | Yes | Display value of detectedAtWorkCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 17 | originOperationId | String | - | No (null allowed) | Reference to u_mes_prod_operation._id: origin operation | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 18 | originOperationName | String | - | No (null allowed) | Display value of originOperationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 19 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 20 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 21 | defectCodeId | String | - | Yes | Reference to u_mes_qual_defectCode._id | `"1158000000000001"` | Reference: u_mes_qual_defectCode._id |
| 22 | defectCodeName | String | - | Yes | Display value of defectCodeId, copied from u_mes_qual_defectCode.name | `"Shrinkage porosity"` |  |
| 23 | supplierId | String | - | No (null allowed) | Reference to u_mes_mast_supplier._id | `null` | Reference: u_mes_mast_supplier._id |
| 24 | supplierName | String | - | No (null allowed) | Display value of supplierId, copied from u_mes_mast_supplier.name | `null` |  |
| 25 | customerId | String | - | No (null allowed) | Reference to u_mes_mast_customer._id | `null` | Reference: u_mes_mast_customer._id |
| 26 | customerName | String | - | No (null allowed) | Display value of customerId, copied from u_mes_mast_customer.name | `null` |  |
| 27 | quantityAffected | Int32 | - | Yes | Quantity affected | `NumberInt(480)` |  |
| 28 | quantityRejected | Int32 | - | Yes | Quantity rejected | `NumberInt(6)` |  |
| 29 | qualityHoldId | String | - | No (null allowed) | Reference to u_mes_qual_qualityHold._id | `"1172000000000005"` | Reference: u_mes_qual_qualityHold._id |
| 30 | qualityHoldName | String | - | No (null allowed) | Display value of qualityHoldId, copied from u_mes_qual_qualityHold.recordNo | `"HLD-2026-000029"` |  |
| 31 | capaId | String | - | No (null allowed) | Reference to u_mes_qual_capa._id | `"1176000000000001"` | Reference: u_mes_qual_capa._id |
| 32 | capaName | String | - | No (null allowed) | Display value of capaId, copied from u_mes_qual_capa.title | `"8D - Shrinkage porosity in bridge section"` |  |
| 33 | rootCauseSummary | String | - | No (null allowed) | Root cause summary | `"Ejector pin galled after die coating build-up"` |  |
| 34 | severity | Int32 | - | Yes | Severity rating 1 to 10 | `NumberInt(8)` |  |
| 35 | costInr | Decimal128 | - | Yes | Cost (Indian rupees) | `NumberDecimal("8640.00")` |  |
| 36 | closedAt | Date | Datetime | No (null allowed) | Date and time when the record was closed. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 37 | closedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'closed' | `null` | Reference: u_mes_mast_user._id |
| 38 | closedBy | String | - | No (null allowed) | Display name of the user in closedById, copied from u_mes_mast_user.fullName | `null` |  |
| 39 | deviationClass | String | - | No (null allowed) | GMP deviation classification; null when the nonconformance is not a GMP deviation (GMP-30) | `"Major"` | Minor; Major; Critical |
| 40 | productImpactText | String | - | No (null allowed) | Impact assessment on the product and on other batches | `"Castings of die 2 from the lot quarantined; other dies not affected"` |  |
| 41 | investigationDueDate | Date | Date | No (null allowed) | Due date of the investigation | `ISODate("2026-10-15T00:00:00.000+0000")` |  |
| 42 | qaApprovedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'qa approved' | `null` | Reference: u_mes_mast_user._id |
| 43 | qaApprovedBy | String | - | No (null allowed) | Display name of the user in qaApprovedById, copied from u_mes_mast_user.fullName | `null` |  |
| 44 | qaApprovedAt | Date | Datetime | No (null allowed) | Time of the quality approval | `null` |  |
| 45 | riskAssessmentId | String | - | No (null allowed) | Reference to u_mes_qual_riskAssessment._id | `null` | Reference: u_mes_qual_riskAssessment._id |
| 46 | riskAssessmentName | String | - | No (null allowed) | Display value of riskAssessmentId, copied from u_mes_qual_riskAssessment.title | `null` |  |
| 47 | status | String | - | Yes | Primary lifecycle state of the document | `"Open"` | Open; Contained; Dispositioned; Closed; Cancelled |
| 48 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 49 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 50 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 51 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 52 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 53 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 54 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

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

u_mes_plan_shiftHandoverNonconformance, u_mes_qual_checkSheetResult, u_mes_qual_inspectionResult, u_mes_qual_spcSample, u_mes_qual_nonconformanceAffectedObject, u_mes_qual_nonconformanceContainmentAction, u_mes_qual_nonconformanceInspectionResult, u_mes_qual_nonconformanceReworkOrder, u_mes_qual_nonconformanceScrapRecord, u_mes_qual_nonconformancePhotoControlledDocument, u_mes_qual_nonconformanceMrbUser, u_mes_qual_reworkOrder, u_mes_qual_scrapRecord, u_mes_qual_qualityHold, u_mes_qual_deviationPermit, u_mes_qual_capaNonconformance, u_mes_qual_customerComplaint, u_mes_syst_notification, u_mes_trac_traceInvestigation, u_mes_qual_defectRecord, u_mes_syst_auditTrailReview, u_mes_bmr_yieldReconciliation, u_mes_qual_environmentalMonitoringResult, u_mes_qual_productRecall.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_nonconformance.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_nonconformance.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_nonconformance.js
