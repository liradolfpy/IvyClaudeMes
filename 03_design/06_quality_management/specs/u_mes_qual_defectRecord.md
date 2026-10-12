# u_mes_qual_defectRecord

| Property | Value |
|---|---|
| Module | Quality Management (qual) |
| Purpose | One logged defect on one unit (or lot sample) with first-fail station, origin, 4M category and follow-up links. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 61 (29 required, 32 may be null) |
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
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | defectCodeId | String | - | Yes | Reference to u_mes_qual_defectCode._id | `"1158000000000007"` | Reference: u_mes_qual_defectCode._id |
| 6 | defectCodeName | String | - | Yes | Display value of defectCodeId, copied from u_mes_qual_defectCode.name | `"Torque below minimum"` |  |
| 7 | wipUnitId | String | - | No (null allowed) | Reference to u_mes_plan_wipUnit._id | `"1094000000000004"` | Reference: u_mes_plan_wipUnit._id |
| 8 | wipUnitName | String | - | No (null allowed) | Display value of wipUnitId, copied from u_mes_plan_wipUnit.recordNo | `"U260915B0223"` |  |
| 9 | serialNumberId | String | - | No (null allowed) | Reference to u_mes_trac_serialNumber._id | `"1131000000000004"` | Reference: u_mes_trac_serialNumber._id |
| 10 | serialNumberName | String | - | No (null allowed) | Display value of serialNumberId, copied from u_mes_trac_serialNumber.recordNo | `"VB26258B00223"` |  |
| 11 | lotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id | `null` | Reference: u_mes_plan_lot._id |
| 12 | lotName | String | - | No (null allowed) | Display value of lotId, copied from u_mes_plan_lot.recordNo | `null` |  |
| 13 | itemId | String | - | Yes | Reference to u_mes_prod_item._id | `"1043000000000002"` | Reference: u_mes_prod_item._id |
| 14 | itemName | String | - | Yes | Display value of itemId, copied from u_mes_prod_item.description | `"Front Brake Caliper Assembly, RH"` |  |
| 15 | productVariantId | String | - | No (null allowed) | Reference to u_mes_prod_productVariant._id | `"1046000000000002"` | Reference: u_mes_prod_productVariant._id |
| 16 | productVariantName | String | - | No (null allowed) | Display value of productVariantId, copied from u_mes_prod_productVariant.name | `"Front Caliper RH, Standard"` |  |
| 17 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000002"` | Reference: u_mes_plan_productionOrder._id |
| 18 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000419"` |  |
| 19 | detectedAtOperationId | String | - | Yes | Reference to u_mes_prod_operation._id: detected at operation | `"1051000000000007"` | Reference: u_mes_prod_operation._id |
| 20 | detectedAtOperationName | String | - | Yes | Display value of detectedAtOperationId, copied from u_mes_prod_operation.name | `"Bleed screw torque"` |  |
| 21 | detectedAtWorkCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id: detected at work center | `"1009000000000007"` | Reference: u_mes_mast_workCenter._id |
| 22 | detectedAtWorkCenterName | String | - | Yes | Display value of detectedAtWorkCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 23 | originOperationId | String | - | No (null allowed) | Reference to u_mes_prod_operation._id: origin operation | `"1051000000000007"` | Reference: u_mes_prod_operation._id |
| 24 | originOperationName | String | - | No (null allowed) | Display value of originOperationId, copied from u_mes_prod_operation.name | `"Bleed screw torque"` |  |
| 25 | isFirstFail | Boolean | - | Yes | First failure of this unit | `true` |  |
| 26 | positionNo | Int32 | - | No (null allowed) | Position on the part | `null` |  |
| 27 | defectLocationText | String | - | No (null allowed) | Location description, e.g. Bore B edge | `"Bleed screw seat"` |  |
| 28 | quantity | Int32 | - | Yes | Quantity defective | `NumberInt(1)` |  |
| 29 | fourMCategory | String | - | Yes | 4M category | `"Machine"` | Man; Machine; Material; Method |
| 30 | operatorUserId | String | - | No (null allowed) | Reference to u_mes_mast_user._id: operator user | `"1029000000000002"` | Reference: u_mes_mast_user._id |
| 31 | operatorUserName | String | - | No (null allowed) | Display value of operatorUserId, copied from u_mes_mast_user.fullName | `"Kavita Bhosale"` |  |
| 32 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000007"` | Reference: u_mes_mast_equipment._id |
| 33 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 34 | componentLotId | String | - | No (null allowed) | Reference to u_mes_plan_lot._id: component lot | `"1096000000000008"` | Reference: u_mes_plan_lot._id |
| 35 | componentLotName | String | - | No (null allowed) | Display value of componentLotId, copied from u_mes_plan_lot.recordNo | `"L260901-BLS-022"` |  |
| 36 | operationExecutionId | String | - | No (null allowed) | Reference to u_mes_plan_operationExecution._id | `"1090000000000005"` | Reference: u_mes_plan_operationExecution._id |
| 37 | operationExecutionName | String | - | No (null allowed) | Display value of operationExecutionId, copied from u_mes_plan_operationExecution.recordNo | `"OPX-2026-000388"` |  |
| 38 | inspectionResultId | String | - | No (null allowed) | Reference to u_mes_qual_inspectionResult._id | `null` | Reference: u_mes_qual_inspectionResult._id |
| 39 | inspectionResultName | String | - | No (null allowed) | Display value of inspectionResultId, copied from u_mes_qual_inspectionResult.recordNo | `null` |  |
| 40 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000002"` | Reference: u_mes_mast_shift._id |
| 41 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift B"` |  |
| 42 | productionDate | Date | Date | Yes | Production date | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 43 | detectedAt | Date | Datetime | Yes | Detection time | `ISODate("2026-09-15T14:21:00.000+0000")` |  |
| 44 | detectedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'detected' | `"1029000000000002"` | Reference: u_mes_mast_user._id |
| 45 | detectedBy | String | - | Yes | Display name of the user in detectedById, copied from u_mes_mast_user.fullName | `"Kavita Bhosale"` |  |
| 46 | imageControlledDocumentId | String | - | No (null allowed) | Reference to u_mes_syst_controlledDocument._id: image controlled document | `null` | Reference: u_mes_syst_controlledDocument._id |
| 47 | imageControlledDocumentName | String | - | No (null allowed) | Display value of imageControlledDocumentId, copied from u_mes_syst_controlledDocument.title | `null` |  |
| 48 | nonconformanceId | String | - | No (null allowed) | Reference to u_mes_qual_nonconformance._id | `"1160000000000007"` | Reference: u_mes_qual_nonconformance._id |
| 49 | nonconformanceName | String | - | No (null allowed) | Display value of nonconformanceId, copied from u_mes_qual_nonconformance.title | `"Bleed screw torque below minimum on three units"` |  |
| 50 | reworkOrderId | String | - | No (null allowed) | Reference to u_mes_qual_reworkOrder._id | `"1168000000000003"` | Reference: u_mes_qual_reworkOrder._id |
| 51 | reworkOrderName | String | - | No (null allowed) | Display value of reworkOrderId, copied from u_mes_qual_reworkOrder.recordNo | `"RWK-2026-000058"` |  |
| 52 | scrapRecordId | String | - | No (null allowed) | Reference to u_mes_qual_scrapRecord._id | `null` | Reference: u_mes_qual_scrapRecord._id |
| 53 | scrapRecordName | String | - | No (null allowed) | Display value of scrapRecordId, copied from u_mes_qual_scrapRecord.recordNo | `null` |  |
| 54 | status | String | - | Yes | Primary lifecycle state of the document | `"Open"` | Open; Reworked; Scrapped; Accepted; Closed |
| 55 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 56 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 57 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 58 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 59 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T14:21:00.000+0000")` |  |
| 60 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 61 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |

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
