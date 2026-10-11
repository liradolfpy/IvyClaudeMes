# u_mes_qlt_scrapRecord

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | Scrap declaration with quantity, weight, cost, defect code and operation of origin |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | SCR-<recordNo> |
| Display value used by references | recordNo |
| Keys | 46 (33 required, 13 may be null) |
| Estimated volume per year | ~15,000 |
| Storage | standard |

## Structure

Flat entity collection: one document per scrap record, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: SCR-<recordNo> | `"SCR-2026-000203"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-000203"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | nonconformanceId | String | No (null allowed) | Reference to u_mes_qlt_nonconformance._id | `"NCR-2026-000118"` | Reference: u_mes_qlt_nonconformance._id |
| 6 | nonconformanceName | String | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qlt_nonconformance.title | `"Leak test failures on caliper LH"` |  |
| 7 | defectCodeId | String | Yes | Reference to u_mes_qlt_defectCode._id | `"DEF-LK01"` | Reference: u_mes_qlt_defectCode._id |
| 8 | defectCodeName | String | Yes | Display value of defectCodeId, copied from u_mes_qlt_defectCode.name | `"Leak at piston seal"` |  |
| 9 | wipUnitId | String | No (null allowed) | Reference to u_mes_exe_wipUnit._id | `"WU-U260929A0184"` | Reference: u_mes_exe_wipUnit._id |
| 10 | wipUnitName | String | No (null allowed) | Display value of wipUnitId, copied from u_mes_exe_wipUnit.recordNo | `"U260929A0184"` |  |
| 11 | lotId | String | No (null allowed) | Reference to u_mes_exe_lot._id | `"LOT-L260928-GDC-014"` | Reference: u_mes_exe_lot._id |
| 12 | lotName | String | No (null allowed) | Display value of lotId, copied from u_mes_exe_lot.recordNo | `"L260928-GDC-014"` |  |
| 13 | itemId | String | Yes | Reference to u_mes_prd_item._id | `"ITM-5110-10-0100"` | Reference: u_mes_prd_item._id |
| 14 | itemName | String | Yes | Display value of itemId, copied from u_mes_prd_item.description | `"Front Brake Caliper Assembly, LH"` |  |
| 15 | quantity | Int32 | Yes | Quantity of the scrap record | `NumberInt(1)` |  |
| 16 | unitOfMeasureId | String | Yes | Reference to u_mes_mdm_unitOfMeasure._id | `"UOM-EA"` | Reference: u_mes_mdm_unitOfMeasure._id |
| 17 | unitOfMeasureName | String | Yes | Display value of unitOfMeasureId, copied from u_mes_mdm_unitOfMeasure.name | `"Each"` |  |
| 18 | weightKg | Decimal128 | Yes | Weight (kg) | `NumberDecimal("6.840")` |  |
| 19 | originOperationId | String | Yes | Reference to u_mes_prd_operation._id: origin operation | `"OPN-OP070"` | Reference: u_mes_prd_operation._id |
| 20 | originOperationName | String | Yes | Display value of originOperationId, copied from u_mes_prd_operation.name | `"Bleed screw torque"` |  |
| 21 | detectedAtOperationId | String | No (null allowed) | Reference to u_mes_prd_operation._id: detected at operation | `"OPN-OP070"` | Reference: u_mes_prd_operation._id |
| 22 | detectedAtOperationName | String | No (null allowed) | Display value of detectedAtOperationId, copied from u_mes_prd_operation.name | `"Bleed screw torque"` |  |
| 23 | workCenterId | String | Yes | Reference to u_mes_mdm_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 24 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 25 | shiftId | String | Yes | Reference to u_mes_mdm_shift._id | `"SH-A"` | Reference: u_mes_mdm_shift._id |
| 26 | shiftName | String | Yes | Display value of shiftId, copied from u_mes_mdm_shift.name | `"Shift A"` |  |
| 27 | scrapType | String | Yes | Scrap type | `"Process Scrap"` | Process Scrap; Setup Scrap; Material Defect; Destructive Test |
| 28 | scrapCostInr | Decimal128 | Yes | Scrap cost (Indian rupees) | `NumberDecimal("4369.00")` |  |
| 29 | declaredById | String | Yes | Reference to u_mes_mdm_user._id: user recorded for 'declared' | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 30 | declaredBy | String | Yes | Display name of the user in declaredById, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 31 | declaredAt | Date | Yes | Date and time when the record was declared | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 32 | approvedById | String | No (null allowed) | Reference to u_mes_mdm_user._id: user recorded for 'approved' | `"USR-10019"` | Reference: u_mes_mdm_user._id |
| 33 | approvedBy | String | No (null allowed) | Display name of the user in approvedById, copied from u_mes_mdm_user.fullName | `"Meera Deshpande"` |  |
| 34 | approvedAt | Date | No (null allowed) | Date and time when the record was approved | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 35 | scrapLocationId | String | No (null allowed) | Reference to u_mes_mat_storageLocation._id: scrap location | `"LOC-LS-ASY-01"` | Reference: u_mes_mat_storageLocation._id |
| 36 | scrapLocationName | String | No (null allowed) | Display value of scrapLocationId, copied from u_mes_mat_storageLocation.name | `"Line-side supermarket, Assembly 1"` |  |
| 37 | disposalMethod | String | Yes | Disposal method | `"Remelt"` | Remelt; Sell As Scrap; Return To Supplier |
| 38 | erpPosted | Boolean | Yes | True when: ERP posted | `true` |  |
| 39 | status | String | Yes | Primary lifecycle state of the document | `"Approved"` | Declared; Approved; Disposed |
| 40 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 41 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 42 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 43 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 44 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 45 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 46 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Declared, Approved, Disposed. Initial state: Declared. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_qlt_nonconformanceScrapRecord.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_scrapRecord.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_scrapRecord.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_scrapRecord.js
