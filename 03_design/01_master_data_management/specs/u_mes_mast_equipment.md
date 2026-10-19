# u_mes_mast_equipment

| Property | Value |
|---|---|
| Module | MasterDataManagement (mast) |
| Purpose | Machines, furnaces, testers (ISA-95 Unit / Equipment); hierarchy, make, model, capability |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 54 (39 required, 15 may be null) |
| Estimated volume per year | 200-1,000 per site |
| Storage | standard |

## Structure

Flat entity collection: one document per equipment, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with equipmentId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mast_equipmentIotDevice | Relationship | IoT device |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1013000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"GDC-01-M1"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the equipment; used as its display value in other collections | `"Gravity Die Casting Machine 1"` |  |
| 7 | equipmentTypeId | String | - | Yes | Reference to u_mes_mast_equipmentType._id | `"1261000000000001"` | Reference: u_mes_mast_equipmentType._id |
| 8 | equipmentTypeName | String | - | Yes | Display value of equipmentTypeId, copied from u_mes_mast_equipmentType.name | `"Gravity Die Casting Machine"` |  |
| 9 | equipmentClass | String | - | Yes | Equipment class | `"Production Equipment"` | Production Equipment; Test Equipment; Measuring Equipment; Utility |
| 10 | lineId | String | - | Yes | Reference to u_mes_mast_line._id | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 11 | lineName | String | - | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 12 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 13 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 14 | parentEquipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id: parent equipment | `null` | Reference: u_mes_mast_equipment._id |
| 15 | parentEquipmentName | String | - | No (null allowed) | Display value of parentEquipmentId, copied from u_mes_mast_equipment.name | `null` |  |
| 16 | manufacturerId | String | - | No (null allowed) | Reference to u_mes_mast_manufacturer._id | `"1260000000000001"` | Reference: u_mes_mast_manufacturer._id |
| 17 | manufacturerName | String | - | No (null allowed) | Display value of manufacturerId, copied from u_mes_mast_manufacturer.name | `"LK Machinery"` |  |
| 18 | model | String | - | Yes | Model of the equipment | `"GDC-600T tilting"` |  |
| 19 | serialNo | String | - | Yes | Serial number | `"LK-GDC-190457"` |  |
| 20 | yearOfManufacture | Int32 | - | Yes | Year of manufacture | `NumberInt(2021)` |  |
| 21 | supplierId | String | - | No (null allowed) | Reference to u_mes_mast_supplier._id | `null` | Reference: u_mes_mast_supplier._id |
| 22 | supplierName | String | - | No (null allowed) | Display value of supplierId, copied from u_mes_mast_supplier.name | `null` |  |
| 23 | assetNo | String | - | Yes | Asset number | `"FA-PN1-004512"` |  |
| 24 | commissionedAt | Date | Datetime | Yes | Date and time when the record was commissioned. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2019-01-04T00:00:00.000+0000")` |  |
| 25 | ratedCapacity | Decimal128 | - | Yes | Rated CAPAcity | `50.0` |  |
| 26 | ratedCapacityUnitOfMeasureId | String | - | Yes | Reference to u_mes_mast_unitOfMeasure._id: rated CAPAcity unit of measure | `"1042000000000008"` | Reference: u_mes_mast_unitOfMeasure._id |
| 27 | ratedCapacityUnitOfMeasureName | String | - | Yes | Display value of ratedCapacityUnitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Degree Celsius"` |  |
| 28 | ratedPowerKw | Decimal128 | - | Yes | Rated power (kW) | `1.5` |  |
| 29 | controllerMake | String | - | Yes | Controller make | `"Siemens"` |  |
| 30 | controllerModel | String | - | Yes | Controller model | `"S7-1500"` |  |
| 31 | controllerIpAddress | String | - | Yes | Controller ip address | `"10.21.6.41"` |  |
| 32 | controllerProtocol | String | - | Yes | Controller protocol | `"OPC UA"` | OPC UA; Open Protocol; Modbus TCP; Profinet; MQTT; Ethernet/IP |
| 33 | criticality | String | - | Yes | A = failure stops the line or affects safety, B = reduced output, C = no immediate effect | `"A"` | A; B; C |
| 34 | currentState | String | - | Yes | Current state | `"Running"` | Running; Idle; Setup; Down; Starved; Blocked; Planned Stop |
| 35 | currentStateSince | Date | Datetime | Yes | Current state since. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 36 | lifetimeCycles | Int64 | - | Yes | Lifetime cycles | `NumberLong("1284500")` |  |
| 37 | lifetimeRunHours | Decimal128 | - | Yes | Lifetime run hours | `14820.5` |  |
| 38 | nextMaintenanceDueAt | Date | Date | Yes | Next maintenance due at. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-10-06T00:00:00.000+0000")` |  |
| 39 | calibrationRequired | Boolean | - | Yes | True when: calibration required | `true` |  |
| 40 | safetyCategory | String | - | Yes | Performance level of the safety function (ISO 13849-1) | `"PL d"` | PL a; PL b; PL c; PL d; PL e |
| 41 | isProductionReady | Boolean | - | Yes | True when the equipment may receive work: not down, not in maintenance, PM and calibration not overdue | `true` |  |
| 42 | readinessReasonText | String | - | No (null allowed) | Why the equipment is not production-ready; null when it is ready | `null` |  |
| 43 | healthScore | Decimal128 | - | No (null allowed) | Rule-based health score from 0 (failed) to 100 (as new) | `84` |  |
| 44 | healthScoreAt | Date | Datetime | No (null allowed) | Time the health score was last calculated | `ISODate("2026-09-24T23:00:00.000+0000")` |  |
| 45 | acquisitionCostInr | Decimal128 | - | No (null allowed) | Purchase and installation cost (Indian rupees) | `14500000.00` |  |
| 46 | plannedReplacementDate | Date | Date | No (null allowed) | Planned replacement date from the lifecycle review | `ISODate("2027-11-30T00:00:00.000+0000")` |  |
| 47 | qualificationStatus | String | - | Yes | Qualification status of the equipment (GMP-33, GMP-35) | `"Qualified"` | Qualified; Not Qualified; Requalification Due |
| 48 | requalificationDueDate | Date | Date | No (null allowed) | Date the next requalification is due; null when not qualification-relevant | `ISODate("2027-07-17T00:00:00.000+0000")` |  |
| 49 | cleanStatus | String | - | Yes | Cleaning status shown on the equipment (GMP-34, GMP-35) | `"Dirty"` | Clean; Dirty; In Cleaning; Clean Hold Expired; Not Applicable |
| 50 | cleanHoldExpiresAt | Date | Datetime | No (null allowed) | End of the clean hold time of the last cleaning | `null` |  |
| 51 | lastCleaningRecordId | String | - | No (null allowed) | Reference to u_mes_maint_cleaningRecord._id: last cleaning record | `null` | Reference: u_mes_maint_cleaningRecord._id |
| 52 | lastCleaningRecordName | String | - | No (null allowed) | Display value of lastCleaningRecordId, copied from u_mes_maint_cleaningRecord.recordNo | `null` |  |
| 53 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Under Maintenance; Decommissioned |
| 54 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Under Maintenance, Decommissioned. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentTypeId: 1 }` | No | Look-up of documents by equipment type |
| 4 | `{ lineId: 1 }` | No | Look-up of documents by line |
| 5 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 6 | `{ parentEquipmentId: 1 }` | No | Look-up of documents by parent equipment |
| 7 | `{ manufacturerId: 1 }` | No | Look-up of documents by manufacturer |

## Referenced by

u_mes_mast_workCenterEquipment, u_mes_mast_equipment, u_mes_mast_equipmentIotDevice, u_mes_prod_billOfProcessStepEquipment, u_mes_prod_recipe, u_mes_plan_operationExecution, u_mes_plan_changeover, u_mes_trac_serialNumber, u_mes_trac_asBuiltRecordOperation, u_mes_qual_checkSheet, u_mes_qual_checkSheetResult, u_mes_qual_spcChart, u_mes_qual_gauge, u_mes_perf_equipmentState, u_mes_perf_downtimeEvent, u_mes_perf_oeeRecord, u_mes_perf_processTag, u_mes_perf_processReading, u_mes_perf_alarm, u_mes_perf_torqueResult, u_mes_perf_leakTestResult, u_mes_maint_maintenancePlan, u_mes_maint_maintenanceWorkOrder, u_mes_maint_sparePartUsedOnEquipment, u_mes_maint_tool, u_mes_maint_toolLifeRecord, u_mes_syst_iotDevice, u_mes_syst_businessEvent, u_mes_perf_energyReading, u_mes_plan_andonEvent, u_mes_ehs_safetyIncident, u_mes_plan_operatorSession, u_mes_plan_interlockEvent, u_mes_plan_recipeDownload, u_mes_plan_setupVerification, u_mes_qual_measurementCurve, u_mes_qual_defectRecord, u_mes_maint_sparePartTransaction, u_mes_maint_reliabilitySummary, u_mes_maint_equipmentLifecycleEvent, u_mes_syst_alertRule, u_mes_syst_analyticsModel, u_mes_syst_computerisedSystem, u_mes_maint_cleaningRecord, u_mes_maint_equipmentQualification, u_mes_syst_iotHubIdentity, u_mes_syst_unsRejectedMessage.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_equipment.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_equipment.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_equipment.js
