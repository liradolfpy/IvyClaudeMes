# u_mes_mdm_equipment

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Machines, furnaces, testers (ISA-95 Unit / Equipment); hierarchy, make, model, capability |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | EQ-<recordNo> |
| Display value used by references | name |
| Keys | 41 (35 required, 6 may be null) |
| Estimated volume per year | 200-1,000 per site |
| Storage | standard |

## Structure

Flat entity collection: one document per equipment, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with equipmentId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mdm_equipmentIotDevice | Relationship | IoT device |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: EQ-<recordNo> | `"EQ-TRQ-01-NR1"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"TRQ-01-NR1"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the equipment; used as its display value in other collections | `"DC Nutrunner Station 1"` |  |
| 6 | equipmentTypeId | String | Yes | Reference to u_mes_mdm_equipmentType._id | `"EQT-DC-NUTRUNNER"` | Reference: u_mes_mdm_equipmentType._id |
| 7 | equipmentTypeName | String | Yes | Display value of equipmentTypeId, copied from u_mes_mdm_equipmentType.name | `"DC Nutrunner"` |  |
| 8 | equipmentClass | String | Yes | Equipment class | `"Production Equipment"` | Production Equipment; Test Equipment; Measuring Equipment; Utility |
| 9 | lineId | String | Yes | Reference to u_mes_mdm_line._id | `"LN-ASY-01"` | Reference: u_mes_mdm_line._id |
| 10 | lineName | String | Yes | Display value of lineId, copied from u_mes_mdm_line.name | `"Caliper Assembly Line 1"` |  |
| 11 | workCenterId | String | Yes | Reference to u_mes_mdm_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 12 | workCenterName | String | Yes | Display value of workCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 13 | parentEquipmentId | String | No (null allowed) | Reference to u_mes_mdm_equipment._id: parent equipment | `"EQ-ASY-01"` | Reference: u_mes_mdm_equipment._id |
| 14 | parentEquipmentName | String | No (null allowed) | Display value of parentEquipmentId, copied from u_mes_mdm_equipment.name | `"Assembly Cell 1"` |  |
| 15 | manufacturerId | String | No (null allowed) | Reference to u_mes_mdm_manufacturer._id | `"MFR-ATLAS-COPCO"` | Reference: u_mes_mdm_manufacturer._id |
| 16 | manufacturerName | String | No (null allowed) | Display value of manufacturerId, copied from u_mes_mdm_manufacturer.name | `"Atlas Copco"` |  |
| 17 | model | String | Yes | Model of the equipment | `"PF6000 with ETV STR61"` |  |
| 18 | serialNo | String | Yes | Serial number | `"AC-PF6-2231907"` |  |
| 19 | yearOfManufacture | Int32 | Yes | Year of manufacture | `NumberInt(2021)` |  |
| 20 | supplierId | String | No (null allowed) | Reference to u_mes_mdm_supplier._id | `"SUP-S1042"` | Reference: u_mes_mdm_supplier._id |
| 21 | supplierName | String | No (null allowed) | Display value of supplierId, copied from u_mes_mdm_supplier.name | `"Konkan Precision Pistons Pvt. Ltd."` |  |
| 22 | assetNo | String | Yes | Asset number | `"FA-PN1-004512"` |  |
| 23 | commissionedAt | Date | Yes | Date and time when the record was commissioned | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 24 | ratedCapacity | Decimal128 | Yes | Rated CAPAcity | `NumberDecimal("50.0")` |  |
| 25 | ratedCapacityUnitOfMeasureId | String | Yes | Reference to u_mes_mdm_unitOfMeasure._id: rated CAPAcity unit of measure | `"UOM-NM"` | Reference: u_mes_mdm_unitOfMeasure._id |
| 26 | ratedCapacityUnitOfMeasureName | String | Yes | Display value of ratedCapacityUnitOfMeasureId, copied from u_mes_mdm_unitOfMeasure.name | `"Newton metre"` |  |
| 27 | ratedPowerKw | Decimal128 | Yes | Rated power (kW) | `NumberDecimal("1.5")` |  |
| 28 | controllerMake | String | Yes | Controller make | `"Atlas Copco"` |  |
| 29 | controllerModel | String | Yes | Controller model | `"Power Focus 6000"` |  |
| 30 | controllerIpAddress | String | Yes | Controller ip address | `"10.21.6.41"` |  |
| 31 | controllerProtocol | String | Yes | Controller protocol | `"Open Protocol"` | OPC UA; Open Protocol; Modbus TCP; Profinet; MQTT; Ethernet/IP |
| 32 | criticality | String | Yes | A = failure stops the line or affects safety, B = reduced output, C = no immediate effect | `"A"` | A; B; C |
| 33 | currentState | String | Yes | Current state | `"Running"` | Running; Idle; Setup; Down; Starved; Blocked; Planned Stop |
| 34 | currentStateSince | Date | Yes | Current state since (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 35 | lifetimeCycles | Int64 | Yes | Lifetime cycles | `NumberLong("1284500")` |  |
| 36 | lifetimeRunHours | Decimal128 | Yes | Lifetime run hours | `NumberDecimal("14820.5")` |  |
| 37 | nextMaintenanceDueAt | Date | Yes | Next maintenance due date and time | `ISODate("2026-10-27T18:30:00.000+0000")` |  |
| 38 | calibrationRequired | Boolean | Yes | True when: calibration required | `true` |  |
| 39 | safetyCategory | String | Yes | Performance level of the safety function (ISO 13849-1) | `"PL d"` | PL a; PL b; PL c; PL d; PL e |
| 40 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Under Maintenance; Decommissioned |
| 41 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Under Maintenance, Decommissioned. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_mdm_workCenterEquipment, u_mes_mdm_equipment, u_mes_mdm_equipmentIotDevice, u_mes_prd_billOfProcessStepEquipment, u_mes_prd_recipe, u_mes_exe_operationExecution, u_mes_exe_changeover, u_mes_trc_serialNumber, u_mes_trc_asBuiltRecordOperation, u_mes_qlt_checkSheet, u_mes_qlt_checkSheetResult, u_mes_qlt_spcChart, u_mes_eqp_equipmentState, u_mes_eqp_downtimeEvent, u_mes_eqp_oeeRecord, u_mes_eqp_processTag, u_mes_eqp_processReading, u_mes_eqp_alarm, u_mes_eqp_torqueResult, u_mes_eqp_leakTestResult, u_mes_mnt_maintenancePlan, u_mes_mnt_maintenanceWorkOrder, u_mes_mnt_sparePartUsedOnEquipment, u_mes_mnt_tool, u_mes_mnt_toolLifeRecord, u_mes_sys_iotDevice, u_mes_sys_businessEvent, u_mes_ehs_energyReading, u_mes_ehs_safetyIncident.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_equipment.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_equipment.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_equipment.js
