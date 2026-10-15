# u_mes_syst_iotDevice

| Property | Value |
|---|---|
| Module | SystemAndIntegration (syst) |
| Purpose | Registry of PLCs, gateways, nutrunner controllers, leak testers, scanners, printers, energy meters |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 32 (24 required, 8 may be null) |
| Estimated volume per year | 300-1,500 |
| Storage | standard |

## Structure

Flat entity collection: one document per IoT device, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1232000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PLC-GDC-01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the IoT device; used as its display value in other collections | `"PLC, casting machine 1"` |  |
| 7 | deviceTypeId | String | - | Yes | Reference to u_mes_syst_deviceType._id | `"1290000000000001"` | Reference: u_mes_syst_deviceType._id |
| 8 | deviceTypeName | String | - | Yes | Display value of deviceTypeId, copied from u_mes_syst_deviceType.name | `"PLC"` |  |
| 9 | manufacturerId | String | - | No (null allowed) | Reference to u_mes_mast_manufacturer._id | `"1260000000000001"` | Reference: u_mes_mast_manufacturer._id |
| 10 | manufacturerName | String | - | No (null allowed) | Display value of manufacturerId, copied from u_mes_mast_manufacturer.name | `"LK Machinery"` |  |
| 11 | model | String | - | Yes | Model of the IoT device | `"PF6000 with ETV STR61"` |  |
| 12 | serialNo | String | - | Yes | Serial number | `"AC-PF6-2231907"` |  |
| 13 | firmwareVersion | String | - | Yes | Firmware version | `"3.9.12"` |  |
| 14 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 15 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 16 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 17 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 18 | integrationConnectorId | String | - | Yes | Reference to u_mes_syst_integrationConnector._id | `"1230000000000001"` | Reference: u_mes_syst_integrationConnector._id |
| 19 | integrationConnectorName | String | - | Yes | Display value of integrationConnectorId, copied from u_mes_syst_integrationConnector.name | `"ERP production interface"` |  |
| 20 | ipAddress | String | - | Yes | Ip address | `"10.21.6.41"` |  |
| 21 | macAddress | String | - | Yes | Mac address | `"00:1B:2C:4D:6E:91"` |  |
| 22 | port | Int32 | - | Yes | Port of the IoT device | `NumberInt(4545)` |  |
| 23 | protocol | String | - | Yes | Protocol of the IoT device | `"HTTPS REST"` | HTTPS REST; OPC UA; Open Protocol; Modbus TCP; MQTT; ZPL Over TCP; SMTP |
| 24 | vlan | Int32 | - | Yes | Vlan of the IoT device | `NumberInt(216)` |  |
| 25 | opcNodeAddress | String | - | No (null allowed) | OPC node address | `"ns=3;s=\"NR1\""` |  |
| 26 | pollIntervalMs | Int32 | - | Yes | Poll interval (milliseconds) | `NumberInt(1000)` |  |
| 27 | lastSeenAt | Date | Datetime | No (null allowed) | Last seen date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 28 | connectionStatus | String | - | Yes | Connection status | `"Online"` | Online; Offline; Degraded |
| 29 | certificateExpiresAt | Date | Date | Yes | Certificate expires at. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 30 | installedAt | Date | Datetime | Yes | Date and time when the record was installed. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2019-01-04T00:00:00.000+0000")` |  |
| 31 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive; Retired |
| 32 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive, Retired. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ deviceTypeId: 1 }` | No | Look-up of documents by device type |
| 4 | `{ manufacturerId: 1 }` | No | Look-up of documents by manufacturer |
| 5 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 6 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 7 | `{ integrationConnectorId: 1 }` | No | Look-up of documents by integration connector |

## Referenced by

u_mes_mast_equipmentIotDevice, u_mes_matl_label, u_mes_perf_processTag, u_mes_perf_alarm, u_mes_perf_torqueResult, u_mes_perf_leakTestResult, u_mes_syst_operatorAppDeviceBinding, u_mes_syst_businessEvent, u_mes_perf_energyReading.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_iotDevice.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_iotDevice.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_iotDevice.js
