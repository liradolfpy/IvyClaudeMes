# u_mes_qual_defectRecord

| Property | Value |
|---|---|
| Module | QualityManagement (qual) |
| Purpose | One logged defect on one unit (or lot sample) with first-fail station, origin, 4M category and follow-up links. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 62 (30 required, 32 may be null) |
| Estimated volume per year | about 6,000 |
| Storage | standard collection |

## Structure

Flat entity collection: one document per defect record, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1321000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"DFR-20260915-00230"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | defectCodeId | String | - | Yes | Reference to u_mes_qual_defectCode._id | `"1158000000000007"` | Reference: u_mes_qual_defectCode._id |
| 7 | defectCodeName | String | - | Yes | Display value of defectCodeId, copied from u_mes_qual_defectCode.name | `"Torque below minimum"` |  |
| 8 | wipUnitId | String | - | No (null allowed) | Reference to u_mes_plan_wipUnit._id | `"1094000000000004"` | Reference: u_mes_plan_wipUnit._id |
| 9 | wipUnitName | String | - | No (null allowed) | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915B0223"` |  |
| 10 | serialNumberId | String | - | No (null allowed) | Reference to u_mes_trac_serialNumber._id | `"1131000000000004"` | Reference: u_mes_trac_serialNumber._id |
| 11 | serialNumberName | String | - | No (null allowed) | Display value of serialNumberId, copied from u_mes_trac_serialNumber.recordNo | `"VB26258B00223"` |  |
| 12 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `null` | Reference: u_mes_plan_lot._id |
| 13 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `null` |  |
| 14 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000002"` | Reference: u_mes_prod_item._id |
| 15 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, RH"` |  |
| 16 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000002"` | Reference: u_mes_prod_productVariant._id |
| 17 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper RH, Standard"` |  |
| 18 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000002"` | Reference: u_mes_plan_productionOrder._id |
| 19 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000419"` |  |
| 20 | detectedAtOperationId | String | - | Yes | Reference to u_mes_prod_operation._id: detected at operation | `"1051000000000007"` | Reference: u_mes_prod_operation._id |
| 21 | detectedAtOperationName | String | - | Yes | Display value of detectedAtOperationId, copied from u_mes_prod_operation.name | `"Bleed screw torque"` |  |
| 22 | detectedAtWorkCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id: detected at work center | `"1009000000000007"` | Reference: u_mes_mast_workCenter._id |
| 23 | detectedAtWorkCenterName | String | - | Yes | Display value of detectedAtWorkCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 24 | originOperationId | String | - | No (null allowed) | Reference to u_mes_prod_operation._id: origin operation | `"1051000000000007"` | Reference: u_mes_prod_operation._id |
| 25 | originOperationName | String | - | No (null allowed) | Display value of originOperationId, copied from u_mes_prod_operation.name | `"Bleed screw torque"` |  |
| 26 | isFirstFail | Boolean | - | Yes | First failure of this unit | `true` |  |
| 27 | positionNo | Int32 | - | No (null allowed) | Position on the part | `null` |  |
| 28 | defectLocationText | String | - | No (null allowed) | Location description, e.g. Bore B edge | `"Bleed screw seat"` |  |
| 29 | quantity | Int32 | - | Yes | Quantity defective | `NumberInt(1)` |  |
| 30 | fourMCategory | String | - | Yes | 4M category | `"Machine"` | Man; Machine; Material; Method |
| 31 | operatorUserId | String | - | No (null allowed) | Reference to u_mes_mast_user._id: operator user | `"1029000000000002"` | Reference: u_mes_mast_user._id |
| 32 | operatorUserName | String | - | No (null allowed) | Display value of operatorUserId, copied from u_mes_mast_user.fullName | `"Kavita Bhosale"` |  |
| 33 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000007"` | Reference: u_mes_mast_equipment._id |
| 34 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 35 | componentLotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id: component lot | `"1096000000000008"` | Reference: u_mes_plan_lot._id |
| 36 | componentLotName | String | - | No (null allowed) | Display value of componentLotId, copied from u_mes_plan_lot.recordNo | `"L260901-BLS-022"` |  |
| 37 | operationExecutionId | String | - | No (null allowed) | Reference to u_mes_plan_operationExecution._id | `"1090000000000005"` | Reference: u_mes_plan_operationExecution._id |
| 38 | operationExecutionName | String | - | No (null allowed) | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000388"` |  |
| 39 | inspectionResultId | String | - | No (null allowed) | Reference to u_mes_qual_inspectionResult._id | `null` | Reference: u_mes_qual_inspectionResult._id |
| 40 | inspectionResultName | String | - | No (null allowed) | Display value of inspectionResultId, copied from u_mes_qual_inspectionResult.recordNo | `null` |  |
| 41 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000002"` | Reference: u_mes_mast_shift._id |
| 42 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift B"` |  |
| 43 | productionDate | Date | Date | Yes | Production date | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 44 | detectedAt | Date | Datetime | Yes | Detection time | `ISODate("2026-09-15T14:21:00.000+0000")` |  |
| 45 | detectedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'detected' | `"1029000000000002"` | Reference: u_mes_mast_user._id |
| 46 | detectedBy | String | - | Yes | Display name of the user in detectedById, copied from u_mes_mast_user.fullName | `"Kavita Bhosale"` |  |
| 47 | imageControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: image controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 48 | imageControlledDocumentName | String | - | No (null allowed) | Display value of imageControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 49 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `"1160000000000007"` | Reference: u_mes_qual_nonconformance._id |
| 50 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `"Bleed screw torque below minimum on three units"` |  |
| 51 | reworkOrderId | String | - | No (null allowed) | Reference to u_mes_qual_reworkOrder._id | `"1168000000000003"` | Reference: u_mes_qual_reworkOrder._id |
| 52 | reworkOrderName | String | - | No (null allowed) | Display value of reworkOrderId, copied from u_mes_qual_reworkOrder.recordNo | `"RWK-2026-000058"` |  |
| 53 | scrapRecordId | String | - | No (null allowed) | Reference to u_mes_qual_scrapRecord._id | `null` | Reference: u_mes_qual_scrapRecord._id |
| 54 | scrapRecordName | String | - | No (null allowed) | Display value of scrapRecordId, copied from u_mes_qual_scrapRecord.recordNo | `null` |  |
| 55 | status | String | - | Yes | Primary lifecycle state of the document | `"Open"` | Open; Reworked; Scrapped; Accepted; Closed |
| 56 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 57 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 58 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 59 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 60 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T14:21:00.000+0000")` |  |
| 61 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 62 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

## Status values

Open, Reworked, Scrapped, Accepted, Closed. Initial state: Open. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ defectCodeId: 1 }` | No | Look-up of documents by defect code |
| 4 | `{ wipUnitId: 1 }` | No | Look-up of documents by wip unit |
| 5 | `{ serialNumberId: 1 }` | No | Look-up of documents by serial number |
| 6 | `{ lotId: 1 }` | No | Look-up of documents by lot |
| 7 | `{ itemId: 1 }` | No | Look-up of documents by item |
| 8 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/06_quality_management/validators/u_mes_qual_defectRecord.json
- Indexes: 03_design/06_quality_management/indexes/u_mes_qual_defectRecord.js
- Sample documents (10): 03_design/06_quality_management/samples/u_mes_qual_defectRecord.js
