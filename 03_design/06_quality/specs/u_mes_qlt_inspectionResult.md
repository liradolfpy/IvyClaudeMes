# u_mes_qlt_inspectionResult

| Property | Value |
|---|---|
| Module | Quality (qlt) |
| Purpose | Measured and attribute results per unit / lot / receipt against a characteristic |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | IR-<recordNo> |
| Display value used by references | recordNo |
| Keys | 54 (32 required, 22 may be null) |
| Estimated volume per year | ~12 million |
| Storage | standard, partitioned by month |

## Structure

Flat entity collection: one document per inspection result, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: IR-<recordNo> | `"IR-20260929-000342"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"20260929-000342"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | inspectionPlanId | String | No (null allowed) | Reference to u_mes_qlt_inspectionPlan._id | `"IP-OP030-INP-01"` | Reference: u_mes_qlt_inspectionPlan._id |
| 6 | inspectionPlanName | String | No (null allowed) | Display value of inspectionPlanId, copied from u_mes_qlt_inspectionPlan.name | `"Machining in-process inspection, caliper body LH"` |  |
| 7 | planLineNo | Int32 | Yes | Plan line number | `NumberInt(10)` |  |
| 8 | characteristicId | String | Yes | Reference to u_mes_qlt_characteristic._id | `"CHR-5110-20-0110-C012"` | Reference: u_mes_qlt_characteristic._id |
| 9 | characteristicName | String | Yes | Display value of characteristicId, copied from u_mes_qlt_characteristic.name | `"Piston bore diameter"` |  |
| 10 | itemId | String | Yes | Reference to u_mes_prd_item._id | `"ITM-5110-20-0110"` | Reference: u_mes_prd_item._id |
| 11 | itemName | String | Yes | Display value of itemId, copied from u_mes_prd_item.description | `"Caliper Body, LH, machined and anodised"` |  |
| 12 | wipUnitId | String | No (null allowed) | Reference to u_mes_exe_wipUnit._id | `"WU-U260929A0184"` | Reference: u_mes_exe_wipUnit._id |
| 13 | wipUnitName | String | No (null allowed) | Display value of wipUnitId, copied from u_mes_exe_wipUnit.recordNo | `"U260929A0184"` |  |
| 14 | lotId | String | No (null allowed) | Reference to u_mes_exe_lot._id | `"LOT-L260928-GDC-014"` | Reference: u_mes_exe_lot._id |
| 15 | lotName | String | No (null allowed) | Display value of lotId, copied from u_mes_exe_lot.recordNo | `"L260928-GDC-014"` |  |
| 16 | goodsReceiptId | String | No (null allowed) | Reference to u_mes_mat_goodsReceipt._id | `"GRN-2026-000918"` | Reference: u_mes_mat_goodsReceipt._id |
| 17 | goodsReceiptName | String | No (null allowed) | Display value of goodsReceiptId, copied from u_mes_mat_goodsReceipt.recordNo | `"2026-000918"` |  |
| 18 | operationExecutionId | String | No (null allowed) | Reference to u_mes_exe_operationExecution._id | `"OPX-20260929-000184"` | Reference: u_mes_exe_operationExecution._id |
| 19 | operationExecutionName | String | No (null allowed) | Display value of operationExecutionId, copied from u_mes_exe_operationExecution.recordNo | `"20260929-000184"` |  |
| 20 | operationId | String | Yes | Reference to u_mes_prd_operation._id | `"OPN-OP030"` | Reference: u_mes_prd_operation._id |
| 21 | operationName | String | Yes | Display value of operationId, copied from u_mes_prd_operation.name | `"CNC machining"` |  |
| 22 | workCenterId | String | Yes | Reference to u_mes_mdm_workCenter._id | `"WC-CNC-01"` | Reference: u_mes_mdm_workCenter._id |
| 23 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mdm_workCenter.name | `"CNC Machining Cell 1"` |  |
| 24 | inspectionType | String | Yes | Inspection type | `"In Process"` | Incoming; In Process; First Off; Final; Audit |
| 25 | sampleNo | Int32 | Yes | Sample number | `NumberInt(3)` |  |
| 26 | measuredValue | Decimal128 | No (null allowed) | Measured value | `NumberDecimal("54.018")` |  |
| 27 | attributeResult | String | No (null allowed) | Attribute result | `"Pass"` | Pass; Fail |
| 28 | nominal | Decimal128 | Yes | Nominal of the inspection result | `NumberDecimal("14.0")` |  |
| 29 | lowerSpecLimit | Decimal128 | No (null allowed) | Lower spec limit | `NumberDecimal("54.000")` |  |
| 30 | upperSpecLimit | Decimal128 | No (null allowed) | Upper spec limit | `NumberDecimal("54.046")` |  |
| 31 | unitOfMeasureId | String | Yes | Reference to u_mes_mdm_unitOfMeasure._id | `"UOM-MM"` | Reference: u_mes_mdm_unitOfMeasure._id |
| 32 | unitOfMeasureName | String | Yes | Display value of unitOfMeasureId, copied from u_mes_mdm_unitOfMeasure.name | `"Millimetre"` |  |
| 33 | deviation | Decimal128 | No (null allowed) | Measured value minus nominal | `NumberDecimal("0.018")` |  |
| 34 | result | String | Yes | Result of the inspection result | `"OK"` | OK; Not OK |
| 35 | gaugeId | String | No (null allowed) | Reference to u_mes_qlt_gauge._id | `"GAU-G-BG-054"` | Reference: u_mes_qlt_gauge._id |
| 36 | gaugeName | String | No (null allowed) | Display value of gaugeId, copied from u_mes_qlt_gauge.name | `"Bore gauge 50-75 mm"` |  |
| 37 | measuredById | String | Yes | Reference to u_mes_mdm_user._id: user recorded for 'measured' | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 38 | measuredBy | String | Yes | Display name of the user in measuredById, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 39 | measuredAt | Date | Yes | Date and time when the record was measured | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 40 | source | String | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 41 | defectCodeId | String | No (null allowed) | Reference to u_mes_qlt_defectCode._id | `"DEF-LK01"` | Reference: u_mes_qlt_defectCode._id |
| 42 | defectCodeName | String | No (null allowed) | Display value of defectCodeId, copied from u_mes_qlt_defectCode.name | `"Leak at piston seal"` |  |
| 43 | nonconformanceId | String | No (null allowed) | Reference to u_mes_qlt_nonconformance._id | `"NCR-2026-000118"` | Reference: u_mes_qlt_nonconformance._id |
| 44 | nonconformanceName | String | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qlt_nonconformance.title | `"Leak test failures on caliper LH"` |  |
| 45 | overridden | Boolean | Yes | True when: overridden | `false` |  |
| 46 | remarks | String | No (null allowed) | Remarks of the inspection result | `"No abnormality observed"` |  |
| 47 | status | String | Yes | Primary lifecycle state of the document | `"Recorded"` | Recorded; Voided |
| 48 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 49 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 50 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 51 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 52 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T00:30:34.000+0000")` |  |
| 53 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 54 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Recorded, Voided. Initial state: Recorded. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ inspectionPlanId: 1 }` | No | Look-up of documents by inspection plan |
| 4 | `{ characteristicId: 1 }` | No | Look-up of documents by characteristic |
| 5 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 6 | `{ wipUnitId: 1 }` | No | Look-up of documents by wip unit |
| 7 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 8 | `{ siteId: 1, measuredAt: -1 }` | No | Time-ordered lists and reports by measured at |

## Referenced by

u_mes_mat_goodsReceiptLineInspectionResult, u_mes_trc_asBuiltRecordInspectionResult, u_mes_qlt_spcSampleInspectionResult, u_mes_qlt_nonconformanceInspectionResult.

## Files

- Validator: 03_design/06_quality/validators/u_mes_qlt_inspectionResult.json
- Indexes: 03_design/06_quality/indexes/u_mes_qlt_inspectionResult.js
- Sample document: 03_design/06_quality/samples/u_mes_qlt_inspectionResult.js
