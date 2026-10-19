# u_mes_syst_iotHubIdentity

| Property | Value |
|---|---|
| Module | SystemAndIntegration (syst) |
| Purpose | One Azure IoT Hub device identity: an equipment identity, an IoT Edge gateway or the MES publisher, with its parent gateway, authentication, certificate, provisioning state, last registry sync and last connection state. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 25 (14 required, 11 may be null) |
| Estimated volume per year | about 20 per site |
| Storage | standard collection |

## Structure

Flat entity collection: one document per IoT hub IDentity, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1371000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"PN1-EGW-FDY-01"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Display name of the identity | `"IoT Edge gateway, foundry"` |  |
| 7 | identityType | String | - | Yes | Equipment, IoT Edge gateway or MES publisher | `"IoT Edge Gateway"` | Equipment; IoT Edge Gateway; MES Publisher |
| 8 | iotHubName | String | - | Yes | Azure IoT Hub the identity is registered in | `"iothub-vbs-pn1"` |  |
| 9 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `null` | Reference: u_mes_mast_equipment._id |
| 10 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `null` |  |
| 11 | iotDeviceId | String | - | No (null allowed) | Reference to u_mes_syst_iotDevice._id | `null` | Reference: u_mes_syst_iotDevice._id |
| 12 | iotDeviceName | String | - | No (null allowed) | Display value of iotDeviceId, copied from u_mes_syst_iotDevice.name | `null` |  |
| 13 | parentIotHubIdentityId | String | - | No (null allowed) | Reference to u_mes_syst_iotHubIdentity._id: parent IoT hub IDentity | `null` | Reference: u_mes_syst_iotHubIdentity._id |
| 14 | parentIotHubIdentityName | String | - | No (null allowed) | Display value of parentIotHubIdentityId, copied from u_mes_syst_iotHubIdentity.name | `null` |  |
| 15 | authenticationMethod | String | - | Yes | How the identity authenticates to IoT Hub | `"X.509 CA Signed"` | X.509 CA Signed; X.509 Self Signed; Symmetric Key |
| 16 | certificateThumbprint | String | - | No (null allowed) | SHA-1 thumbprint of the client certificate; null for symmetric key authentication | `"339962C375971175F022A31922D1CB3060A07CA9"` |  |
| 17 | certificateExpiresAt | Date | Date | No (null allowed) | Expiry of the client certificate; null for symmetric key authentication | `ISODate("2028-08-31T00:00:00.000+0000")` |  |
| 18 | provisioningStatus | String | - | Yes | State of the identity in IoT Hub | `"Provisioned"` | Not Provisioned; Provisioned; Sync Failed; Disabled |
| 19 | lastRegistrySyncAt | Date | Datetime | No (null allowed) | Last time the registry sync service wrote the identity and its twin tags; null before the first sync | `ISODate("2026-09-14T18:00:00.000+0000")` |  |
| 20 | twinTagsVersion | Int32 | - | Yes | Version of the twin tags last written; increases with each master data change that touches the identity | `NumberInt(1)` |  |
| 21 | lastSyncErrorText | String | - | No (null allowed) | Error of the last failed sync; null when the last sync succeeded | `null` |  |
| 22 | connectionState | String | - | Yes | Last connection state reported by IoT Hub | `"Connected"` | Connected; Disconnected; Never Connected |
| 23 | connectionStateAt | Date | Datetime | No (null allowed) | Time of the last device connection state event; null when the identity never connected | `ISODate("2026-09-14T18:20:00.000+0000")` |  |
| 24 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 25 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ iotDeviceId: 1 }` | No | Look-up of documents by IoT device |
| 5 | `{ parentIotHubIdentityId: 1 }` | No | Look-up of documents by parent IoT hub IDentity |
| 6 | `{ provisioningStatus: 1 }` | No | Registry sync work list |

## Referenced by

u_mes_syst_iotHubIdentity, u_mes_syst_unsRejectedMessage.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_iotHubIdentity.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_iotHubIdentity.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_iotHubIdentity.js
