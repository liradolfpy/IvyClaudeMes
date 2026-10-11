# u_mes_syst_iotDevice

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Registry of PLCs, gateways, nutrunner controllers, leak testers, scanners, printers, energy meters |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | IOT-<recordNo> |
| Display value used by references | name |
| Keys | 31 (23 required, 8 may be null) |
| Estimated volume per year | 300-1,500 |
| Storage | standard |

## Structure

Flat entity collection: one document per IoT device, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: IOT-<recordNo> | `"IOT-NR-CTRL-01"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"NR-CTRL-01"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the IoT device; used as its display value in other collections | `"Nutrunner controller, torque station 1"` |  |
| 6 | deviceTypeId | String | Yes | Reference to u_mes_syst_deviceType._id | `"DVT-NR-CTRL"` | Reference: u_mes_syst_deviceType._id |
| 7 | deviceTypeName | String | Yes | Display value of deviceTypeId, copied from u_mes_syst_deviceType.name | `"Nutrunner Controller"` |  |
| 8 | manufacturerId | String | No (null allowed) | Reference to u_mes_mast_manufacturer._id | `"MFR-ATLAS-COPCO"` | Reference: u_mes_mast_manufacturer._id |
| 9 | manufacturerName | String | No (null allowed) | Display value of manufacturerId, copied from u_mes_mast_manufacturer.name | `"Atlas Copco"` |  |
| 10 | model | String | Yes | Model of the IoT device | `"PF6000 with ETV STR61"` |  |
| 11 | serialNo | String | Yes | Serial number | `"AC-PF6-2231907"` |  |
| 12 | firmwareVersion | String | Yes | Firmware version | `"3.9.12"` |  |
| 13 | equipmentId | String | No (null allowed) | Reference to u_mes_mast_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mast_equipment._id |
| 14 | equipmentName | String | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 15 | workCenterId | String | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mast_workCenter._id |
| 16 | workCenterName | String | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 17 | integrationConnectorId | String | Yes | Reference to u_mes_syst_integrationConnector._id | `"ICN-ERP-PRD"` | Reference: u_mes_syst_integrationConnector._id |
| 18 | integrationConnectorName | String | Yes | Display value of integrationConnectorId, copied from u_mes_syst_integrationConnector.name | `"ERP production interface"` |  |
| 19 | ipAddress | String | Yes | Ip address | `"10.21.6.41"` |  |
| 20 | macAddress | String | Yes | Mac address | `"00:1B:2C:4D:6E:91"` |  |
| 21 | port | Int32 | Yes | Port of the IoT device | `NumberInt(4545)` |  |
| 22 | protocol | String | Yes | Protocol of the IoT device | `"HTTPS REST"` | HTTPS REST; OPC UA; Open Protocol; Modbus TCP; MQTT; ZPL Over TCP; SMTP |
| 23 | vlan | Int32 | Yes | Vlan of the IoT device | `NumberInt(216)` |  |
| 24 | opcNodeAddress | String | No (null allowed) | OPC node address | `"ns=3;s=\"NR1\""` |  |
| 25 | pollIntervalMs | Int32 | Yes | Poll interval (milliseconds) | `NumberInt(1000)` |  |
| 26 | lastSeenAt | Date | No (null allowed) | Last seen date and time | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 27 | connectionStatus | String | Yes | Connection status | `"Online"` | Online; Offline; Degraded |
| 28 | certificateExpiresAt | Date | Yes | Certificate expires date and time | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 29 | installedAt | Date | Yes | Date and time when the record was installed | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 30 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive; Retired |
| 31 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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
- Sample document: 03_design/09_system_integration/samples/u_mes_syst_iotDevice.js
