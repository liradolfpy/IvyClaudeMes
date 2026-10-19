# u_mes_syst_integrationConnector

| Property | Value |
|---|---|
| Module | SystemAndIntegration (syst) |
| Purpose | Connector definitions to ERP, PLM, OPC UA servers, tool controllers, label printers |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 23 (19 required, 4 may be null) |
| Estimated volume per year | 20-80 |
| Storage | standard |

## Structure

Flat entity collection: one document per integration connector, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with integrationConnectorId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_syst_integrationConnectorFunction | Child | function |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1230000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"ERP-PRD"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Name of the integration connector; used as its display value in other collections | `"ERP production interface"` |  |
| 7 | connectorType | String | - | Yes | Connector type | `"ERP"` | ERP; PLM; OPC UA Server; Tool Controller; Label Printer; Leak Tester; Email Gateway; LIMS; Weighing System; Serialisation Server; Track And Trace Portal; Document Management; Azure IoT Hub |
| 8 | targetSystem | String | - | Yes | Target system | `"SAP S/4HANA"` |  |
| 9 | protocol | String | - | Yes | Protocol of the integration connector | `"HTTPS REST"` | HTTPS REST; OPC UA; Open Protocol; Modbus TCP; MQTT; ZPL Over TCP; SMTP; Serial Over TCP |
| 10 | endpoint | String | - | Yes | Endpoint of the integration connector | `"https://erp-prd.varunabrakes.example/api/mes"` |  |
| 11 | environment | String | - | Yes | Environment of the integration connector | `"Production"` | Production; Quality; Development |
| 12 | authMethod | String | - | Yes | Auth method | `"OAuth2 Client Credentials"` | OAuth2 Client Credentials; Certificate; Basic; None |
| 13 | credentialRef | String | - | Yes | Pointer to the secret in the vault; the secret itself is never stored | `"vault://mes/pn1/erp-prd"` |  |
| 14 | timeoutMs | Int32 | - | Yes | Timeout (milliseconds) | `NumberInt(15000)` |  |
| 15 | retryPolicyMaxAttempts | Int32 | - | Yes | Retry policy maximum attempts | `NumberInt(5)` |  |
| 16 | retryPolicyBackoffSec | Int32 | - | Yes | Retry policy backoff (seconds) | `NumberInt(60)` |  |
| 17 | lastSuccessAt | Date | Datetime | No (null allowed) | Last success date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 18 | lastFailureAt | Date | Datetime | No (null allowed) | Last failure date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 19 | healthStatus | String | - | Yes | Health status | `"Healthy"` | Healthy; Degraded; Down |
| 20 | ownerUserId | String | - | No (null allowed) | Reference to u_mes_mast_user._id: owner user | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 21 | ownerUserName | String | - | No (null allowed) | Display value of ownerUserId, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 22 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Disabled |
| 23 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Disabled. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ ownerUserId: 1 }` | No | Look-up of documents by owner user |

## Referenced by

u_mes_syst_erpMessage, u_mes_syst_integrationConnectorFunction, u_mes_syst_iotDevice.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_integrationConnector.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_integrationConnector.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_integrationConnector.js
