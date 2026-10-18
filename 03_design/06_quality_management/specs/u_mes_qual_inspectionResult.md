# u_mes_qual_inspectionResult

| Property | Value |
|---|---|
| Module | QualityManagement (qual) |
| Purpose | Measured and attribute results per unit / lot / receipt against a characteristic |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 66 (33 required, 33 may be null) |
| Estimated volume per year | ~12 million |
| Storage | standard, partitioned by month |

## Structure

Flat entity collection: one document per inspection result, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1150000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"IR-2026-000162"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | inspectionPlanId | String | - | No (null allowed) | Reference to u_mes_qual_inspectionPlan._id | `"1142000000000001"` | Reference: u_mes_qual_inspectionPlan._id |
| 7 | inspectionPlanName | String | - | No (null allowed) | Display value of inspectionPlanId, copied from u_mes_qual_inspectionPlan.name | `"In-process inspection, gravity die casting"` |  |
| 8 | planLineNo | Int32 | - | Yes | Plan line number | `NumberInt(10)` |  |
| 9 | characteristicId | String | - | Yes | Reference to u_mes_qual_characteristic._id | `"1138000000000001"` | Reference: u_mes_qual_characteristic._id |
| 10 | characteristicName | String | - | Yes | Display value of characteristicId, copied from u_mes_qual_characteristic.name | `"Casting wall thickness at bridge"` |  |
| 11 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 12 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 13 | wipUnitId | String | - | No (null allowed) | Reference to u_mes_plan_wipUnit._id | `null` | Reference: u_mes_plan_wipUnit._id |
| 14 | wipUnitName | String | - | No (null allowed) | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `null` |  |
| 15 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `"1096000000000001"` | Reference: u_mes_plan_lot._id |
| 16 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `"L260915-GDC-014"` |  |
| 17 | goodsReceiptId | String | - | No (null allowed) | Reference to u_mes_matl_goodsReceipt._id | `null` | Reference: u_mes_matl_goodsReceipt._id |
| 18 | goodsReceiptName | String | - | No (null allowed) | Display value of goodsReceiptId, copied from u_mes_matl_goodsReceipt.recordNo | `null` |  |
| 19 | operationExecutionId | String | - | No (null allowed) | Reference to u_mes_plan_operationExecution._id | `"1090000000000001"` | Reference: u_mes_plan_operationExecution._id |
| 20 | operationExecutionName | String | - | No (null allowed) | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000376"` |  |
| 21 | operationId | String | - | Yes | Reference to u_mes_prod_operation._id | `"1051000000000001"` | Reference: u_mes_prod_operation._id |
| 22 | operationName | String | - | Yes | Display value of operationId, copied from u_mes_prod_operation.name | `"Gravity die casting"` |  |
| 23 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 24 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 25 | inspectionType | String | - | Yes | Inspection type | `"In Process"` | Incoming; In Process; First Off; Final; Audit |
| 26 | sampleNo | Int32 | - | Yes | Sample number | `NumberInt(3)` |  |
| 27 | measuredValue | Decimal128 | - | No (null allowed) | Measured value | `8.05` |  |
| 28 | attributeResult | String | - | No (null allowed) | Attribute result | `null` | Pass; Fail |
| 29 | nominal | Decimal128 | - | Yes | Nominal of the inspection result | `8.00` |  |
| 30 | lowerSpecLimit | Decimal128 | - | No (null allowed) | Lower spec limit | `7.50` |  |
| 31 | upperSpecLimit | Decimal128 | - | No (null allowed) | Upper spec limit | `8.50` |  |
| 32 | unitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id | `"1042000000000003"` | Reference: u_mes_mast_unitOfMeasure._id |
| 33 | unitOfMeasureName | String | - | Yes | Display value of unitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Millimetre"` |  |
| 34 | deviation | Decimal128 | - | No (null allowed) | Measured value minus nominal | `0.05` |  |
| 35 | result | String | - | Yes | Result of the inspection result | `"OK"` | OK; Not OK |
| 36 | gaugeId | String | - | No (null allowed) | Reference to u_mes_qual_gauge._id | `"1189000000000001"` | Reference: u_mes_qual_gauge._id |
| 37 | gaugeName | String | - | No (null allowed) | Display value of gaugeId, copied from u_mes_qual_gauge.name | `"Ultrasonic thickness gauge 1-25 mm"` |  |
| 38 | measuredById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'measured' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 39 | measuredBy | String | - | Yes | Display name of the user in measuredById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 40 | measuredAt | Date | Datetime | Yes | Date and time when the record was measured. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:50.000+0000")` |  |
| 41 | source | String | - | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 42 | defectCodeId | String | - | No (null allowed) | Reference to u_mes_qual_defectCode._id | `null` | Reference: u_mes_qual_defectCode._id |
| 43 | defectCodeName | String | - | No (null allowed) | Display value of defectCodeId, copied from u_mes_qual_defectCode.name | `null` |  |
| 44 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `null` | Reference: u_mes_qual_nonconformance._id |
| 45 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `null` |  |
| 46 | overridden | Boolean | - | Yes | True when: overridden | `false` |  |
| 47 | remarks | String | - | No (null allowed) | Remarks of the inspection result | `"No abnormality observed"` |  |
| 48 | positionNo | Int32 | - | No (null allowed) | Position number (u_mes_qual_characteristicPosition.positionNo) | `NumberInt(1)` |  |
| 49 | positionName | String | - | No (null allowed) | Position name | `"Bridge, left of centre"` |  |
| 50 | imageControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: image controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 51 | imageControlledDocumentName | String | - | No (null allowed) | Display value of imageControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 52 | measurementCurveId | String | - | No (null allowed) | Reference to u_mes_qual_measurementCurve._id | `null` | Reference: u_mes_qual_measurementCurve._id |
| 53 | measurementCurveName | String | - | No (null allowed) | Display value of measurementCurveId, copied from u_mes_qual_measurementCurve.recordNo | `null` |  |
| 54 | analyticsModelId | String | - | No (null allowed) | Reference to u_mes_syst_analyticsModel._id | `null` | Reference: u_mes_syst_analyticsModel._id |
| 55 | analyticsModelName | String | - | No (null allowed) | Display value of analyticsModelId, copied from u_mes_syst_analyticsModel.name | `null` |  |
| 56 | modelVersion | String | - | No (null allowed) | Version of the model | `null` |  |
| 57 | modelClass | String | - | No (null allowed) | Class returned by the model, e.g. OK, NOK, Low Confidence | `null` |  |
| 58 | modelConfidence | Decimal128 | - | No (null allowed) | Confidence of the model classification (0 to 1) | `null` |  |
| 59 | status | String | - | Yes | Primary lifecycle state of the document | `"Recorded"` | Recorded; Voided |
| 60 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 61 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:20.000+0000")` |  |
| 62 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 63 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 64 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:52:50.000+0000")` |  |
| 65 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 66 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Recorded, Voided. Initial state: Recorded. The values are maintained in u_mes_syst_statusDefinition.

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

u_mes_matl_goodsReceiptLineInspectionResult, u_mes_trac_asBuiltRecordInspectionResult, u_mes_qual_spcSampleInspectionResult, u_mes_qual_nonconformanceInspectionResult, u_mes_qual_measurementCurve, u_mes_qual_defectRecord.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_inspectionResult.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_inspectionResult.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_inspectionResult.js
