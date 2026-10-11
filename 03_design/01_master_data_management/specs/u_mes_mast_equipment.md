# u_mes_mast_equipment

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | Machines, furnaces, testers (ISA-95 Unit / Equipment); hierarchy, make, model, capability |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 41 (35 required, 6 may be null) |
| Estimated volume per year | 200-1,000 per site |
| Storage | standard |

## Structure

Flat entity collection: one document per equipment, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with equipmentId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mast_equipmentIotDevice | Relationship | IoT device |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1013000000000001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"GDC-01-M1"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the equipment; used as its display value in other collections | `"Gravity Die Casting Machine 1"` |  |
| 6 | equipmentTypeId | String | Yes | Reference to u_mes_mast_equipmentType._id | `"1261000000000001"` | Reference: u_mes_mast_equipmentType._id |
| 7 | equipmentTypeName | String | Yes | Display value of equipmentTypeId, copied from u_mes_mast_equipmentType.name | `"Gravity Die Casting Machine"` |  |
| 8 | equipmentClass | String | Yes | Equipment class | `"Production Equipment"` | Production Equipment; Test Equipment; Measuring Equipment; Utility |
| 9 | lineId | String | Yes | Reference to u_mes_mast_line._id | `"1006000000000001"` | Reference: u_mes_mast_line._id |
| 10 | lineName | String | Yes | Display value of lineId, copied from u_mes_mast_line.name | `"Gravity Die Casting Line 1"` |  |
| 11 | workCenterId | String | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 12 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 13 | parentEquipmentId | String | No (null allowed) | Reference to u_mes_mast_equipment._id: parent equipment | `null` | Reference: u_mes_mast_equipment._id |
| 14 | parentEquipmentName | String | No (null allowed) | Display value of parentEquipmentId, copied from u_mes_mast_equipment.name | `null` |  |
| 15 | manufacturerId | String | No (null allowed) | Reference to u_mes_mast_manufacturer._id | `"1260000000000001"` | Reference: u_mes_mast_manufacturer._id |
| 16 | manufacturerName | String | No (null allowed) | Display value of manufacturerId, copied from u_mes_mast_manufacturer.name | `"LK Machinery"` |  |
| 17 | model | String | Yes | Model of the equipment | `"GDC-600T tilting"` |  |
| 18 | serialNo | String | Yes | Serial number | `"LK-GDC-190457"` |  |
| 19 | yearOfManufacture | Int32 | Yes | Year of manufacture | `NumberInt(2021)` |  |
| 20 | supplierId | String | No (null allowed) | Reference to u_mes_mast_supplier._id | `null` | Reference: u_mes_mast_supplier._id |
| 21 | supplierName | String | No (null allowed) | Display value of supplierId, copied from u_mes_mast_supplier.name | `null` |  |
| 22 | assetNo | String | Yes | Asset number | `"FA-PN1-004512"` |  |
| 23 | commissionedAt | Date | Yes | Date and time when the record was commissioned | `ISODate("2019-01-03T18:30:00.000+0000")` |  |
| 24 | ratedCapacity | Decimal128 | Yes | Rated CAPAcity | `NumberDecimal("50.0")` |  |
| 25 | ratedCapacityUnitOfMeasureId | String | Yes | Reference to u_mes_mast_unitOfMeasure._id: rated CAPAcity unit of measure | `"1042000000000008"` | Reference: u_mes_mast_unitOfMeasure._id |
| 26 | ratedCapacityUnitOfMeasureName | String | Yes | Display value of ratedCapacityUnitOfMeasureId, copied from u_mes_mast_unitOfMeasure.name | `"Degree Celsius"` |  |
| 27 | ratedPowerKw | Decimal128 | Yes | Rated power (kW) | `NumberDecimal("1.5")` |  |
| 28 | controllerMake | String | Yes | Controller make | `"Siemens"` |  |
| 29 | controllerModel | String | Yes | Controller model | `"S7-1500"` |  |
| 30 | controllerIpAddress | String | Yes | Controller ip address | `"10.21.6.41"` |  |
| 31 | controllerProtocol | String | Yes | Controller protocol | `"OPC UA"` | OPC UA; Open Protocol; Modbus TCP; Profinet; MQTT; Ethernet/IP |
| 32 | criticality | String | Yes | A = failure stops the line or affects safety, B = reduced output, C = no immediate effect | `"A"` | A; B; C |
| 33 | currentState | String | Yes | Current state | `"Running"` | Running; Idle; Setup; Down; Starved; Blocked; Planned Stop |
| 34 | currentStateSince | Date | Yes | Current state since (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-04-01T18:30:00.000+0000")` |  |
| 35 | lifetimeCycles | Int64 | Yes | Lifetime cycles | `NumberLong("1284500")` |  |
| 36 | lifetimeRunHours | Decimal128 | Yes | Lifetime run hours | `NumberDecimal("14820.5")` |  |
| 37 | nextMaintenanceDueAt | Date | Yes | Next maintenance due date and time | `ISODate("2026-10-05T18:30:00.000+0000")` |  |
| 38 | calibrationRequired | Boolean | Yes | True when: calibration required | `true` |  |
| 39 | safetyCategory | String | Yes | Performance level of the safety function (ISO 13849-1) | `"PL d"` | PL a; PL b; PL c; PL d; PL e |
| 40 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Under Maintenance; Decommissioned |
| 41 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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

u_mes_mast_workCenterEquipment, u_mes_mast_equipment, u_mes_mast_equipmentIotDevice, u_mes_prod_billOfProcessStepEquipment, u_mes_prod_recipe, u_mes_plan_operationExecution, u_mes_plan_changeover, u_mes_trac_serialNumber, u_mes_trac_asBuiltRecordOperation, u_mes_qual_checkSheet, u_mes_qual_checkSheetResult, u_mes_qual_spcChart, u_mes_perf_equipmentState, u_mes_perf_downtimeEvent, u_mes_perf_oeeRecord, u_mes_perf_processTag, u_mes_perf_processReading, u_mes_perf_alarm, u_mes_perf_torqueResult, u_mes_perf_leakTestResult, u_mes_maint_maintenancePlan, u_mes_maint_maintenanceWorkOrder, u_mes_maint_sparePartUsedOnEquipment, u_mes_maint_tool, u_mes_maint_toolLifeRecord, u_mes_syst_iotDevice, u_mes_syst_businessEvent, u_mes_perf_energyReading, u_mes_ehs_safetyIncident.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_equipment.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_equipment.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_equipment.js
