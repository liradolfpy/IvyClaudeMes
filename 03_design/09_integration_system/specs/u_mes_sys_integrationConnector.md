# u_mes_sys_integrationConnector

| Property | Value |
|---|---|
| Module | Integration and system (sys) |
| Purpose | Connector definitions to ERP, PLM, OPC UA servers, tool controllers, label printers |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | ICN-<recordNo> |
| Display value used by references | name |
| Keys | 22 (18 required, 4 may be null) |
| Estimated volume per year | 20-80 |
| Storage | standard |

## Structure

Flat entity collection: one document per integration connector, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with integrationConnectorId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_sys_integrationConnectorFunction | Child | function |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: ICN-<recordNo> | `"ICN-ERP-PRD"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"ERP-PRD"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | Yes | Name of the integration connector; used as its display value in other collections | `"ERP production interface"` |  |
| 6 | connectorType | String | Yes | Connector type | `"ERP"` | ERP; PLM; OPC UA Server; Tool Controller; Label Printer; Leak Tester; Email Gateway |
| 7 | targetSystem | String | Yes | Target system | `"SAP S/4HANA"` |  |
| 8 | protocol | String | Yes | Protocol of the integration connector | `"HTTPS REST"` | HTTPS REST; OPC UA; Open Protocol; Modbus TCP; MQTT; ZPL Over TCP; SMTP |
| 9 | endpoint | String | Yes | Endpoint of the integration connector | `"https://erp-prd.varunabrakes.example/api/mes"` |  |
| 10 | environment | String | Yes | Environment of the integration connector | `"Production"` | Production; Quality; Development |
| 11 | authMethod | String | Yes | Auth method | `"OAuth2 Client Credentials"` | OAuth2 Client Credentials; Certificate; Basic; None |
| 12 | credentialRef | String | Yes | Pointer to the secret in the vault; the secret itself is never stored | `"vault://mes/pn1/erp-prd"` |  |
| 13 | timeoutMs | Int32 | Yes | Timeout (milliseconds) | `NumberInt(15000)` |  |
| 14 | retryPolicyMaxAttempts | Int32 | Yes | Retry policy maximum attempts | `NumberInt(5)` |  |
| 15 | retryPolicyBackoffSec | Int32 | Yes | Retry policy backoff (seconds) | `NumberInt(60)` |  |
| 16 | lastSuccessAt | Date | No (null allowed) | Last success date and time | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 17 | lastFailureAt | Date | No (null allowed) | Last failure date and time | `null` |  |
| 18 | healthStatus | String | Yes | Health status | `"Healthy"` | Healthy; Degraded; Down |
| 19 | ownerUserId | String | No (null allowed) | Reference to u_mes_mdm_user._id: owner user | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 20 | ownerUserName | String | No (null allowed) | Display value of ownerUserId, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 21 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Disabled |
| 22 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Disabled. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ ownerUserId: 1 }` | No | Look-up of documents by owner user |

## Referenced by

u_mes_sys_erpMessage, u_mes_sys_integrationConnectorFunction, u_mes_sys_iotDevice.

## Files

- Validator: 03_design/09_integration_system/validators/u_mes_sys_integrationConnector.json
- Indexes: 03_design/09_integration_system/indexes/u_mes_sys_integrationConnector.js
- Sample document: 03_design/09_integration_system/samples/u_mes_sys_integrationConnector.js
