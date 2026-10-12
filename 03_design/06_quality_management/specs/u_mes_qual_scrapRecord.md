# u_mes_qual_scrapRecord

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | Scrap declaration with quantity, weight, cost, defect code and operation of origin |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 46 (33 required, 13 may be null) |
| Estimated volume per year | ~15,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per scrap record, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1171000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SCR-2026-000203"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `"1160000000000001"` | Reference: u_mes_qual_nonconformance._id |
| 6 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `"Shrinkage porosity found on casting lot from die 2"` |  |
| 7 | defectCodeId | String | - | Yes | Reference to u_mes_qual_defectCode._id | `"1158000000000001"` | Reference: u_mes_qual_defectCode._id |
| 8 | defectCodeName | String | - | Yes | Display value of defectCodeId, copied from u_mes_qual_defectCode.name | `"Shrinkage porosity"` |  |
| 9 | wipUnitId | String | - | No (null allowed) | Reference to u_mes_plan_wipUnit._id | `null` | Reference: u_mes_plan_wipUnit._id |
| 10 | wipUnitName | String | - | No (null allowed) | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `null` |  |
| 11 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `"1096000000000001"` | Reference: u_mes_plan_lot._id |
| 12 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260915-GDC-014"` |  |
| 13 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 14 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 15 | quantity | Int32 | - | Yes | Quantity of the scrap record | `NumberInt(1)` |  |
| 16 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000001"` | Reference: u_mes_mast_unitOfMeasure._id |
| 17 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Each"` |  |
| 18 | weightKg | Decimal128 | - | Yes | Weight (kg) | `NumberDecimal("6.840")` |  |
| 19 | originOperationId | String | - | Yes | Reference to u_mes_prod_operation._id: origin operation | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 20 | originOperationName | String | - | Yes | Display value of originOperationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 21 | detectedAtOperationId | String | - | No (null allowed) | Reference to u_mes_prod_operation._id: detected at operation | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 22 | detectedAtOperationName | String | - | No (null allowed) | Display value of detectedAtOperationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 23 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 24 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 25 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 26 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 27 | scrapType | String | - | Yes | Scrap type | `"Process Scrap"` | Process Scrap; Setup Scrap; Material Defect; Destructive Test |
| 28 | scrapCostInr | Decimal128 | - | Yes | Scrap cost (Indian rupees) | `NumberDecimal("4369.00")` |  |
| 29 | declaredById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'declared' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 30 | declaredBy | String | - | Yes | Display name of the user in declaredById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 31 | declaredAt | Date | Datetime | Yes | Date and time when the record was declared. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:50.000+0000")` |  |
| 32 | approvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'approved' | `null` | Reference: u_mes_mast_user._id |
| 33 | approvedBy | String | - | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 34 | approvedAt | Date | Datetime | No (null allowed) | Date and time when the record was approved. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 35 | scrapLocationId | String | - | No (null allowed) | Reference to u_mes_matl_storageLocation._id: scrap location | `"1112000000000010"` | Reference: u_mes_matl_storageLocation._id |
| 36 | scrapLocationName | String | - | No (null allowed) | Display value of scrapLocationId, copied from u_mes_matl_storageLocation.name | `"Scrap yard, aluminium"` |  |
| 37 | disposalMethod | String | - | Yes | Disposal method | `"Remelt"` | Remelt; Sell As Scrap; Return To Supplier |
| 38 | erpPosted | Boolean | - | Yes | True when: ERP posted | `true` |  |
| 39 | status | String | - | Yes | Primary lifecycle state of the document | `"Declared"` | Declared; Approved; Disposed |
| 40 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 41 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:20.000+0000")` |  |
| 42 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 43 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 44 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:50.000+0000")` |  |
| 45 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 46 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Declared, Approved, Disposed. Initial state: Declared. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ nonconformanceId: 1 }` | No | Look-up of documents by nonconformance |
| 4 | `{ defectCodeId: 1 }` | No | Look-up of documents by defect code |
| 5 | `{ wipUnitId: 1 }` | No | Look-up of documents by wip unit |
| 6 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 7 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 8 | `{ siteId: 1, declaredAt: -1 }` | No | Time-ordered lists and reports by declared at |

## Referenced by

u_mes_qual_nonconformanceScrapRecord.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_scrapRecord.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_scrapRecord.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_scrapRecord.js
