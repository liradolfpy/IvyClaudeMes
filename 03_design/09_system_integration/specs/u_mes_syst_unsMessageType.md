# u_mes_syst_unsMessageType

| Property | Value |
|---|---|
| Module | SystemAndIntegration (syst) |
| Purpose | Catalogue of the message types carried by the Unified Namespace on Azure IoT Hub: namespace, message type, payload schema and version, message class, the MES collection the ingestion service writes and the device twin property that holds the current state. |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 20 (18 required, 2 may be null) |
| Estimated volume per year | about 30 |
| Storage | standard collection |

## Structure

Flat entity collection: one document per uns message type, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1370000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"edge.state"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | name | String | - | Yes | Display name of the message type | `"Equipment state"` |  |
| 7 | description | String | - | Yes | What the message carries and when it is sent | `"Running, idle, setup, down, starved, blocked or planned stop of one piece of equipment, sent on every change of state"` |  |
| 8 | unsNamespace | String | - | Yes | UNS namespace of the message; sent in lower case as the application property ns | `"Edge"` | Edge; MES; KPI |
| 9 | messageTypeCode | String | - | Yes | Message type within the namespace, sent as the application property msgType | `"state"` |  |
| 10 | payloadSchemaName | String | - | Yes | Payload schema name carried in the envelope field schema | `"uns.edge.state"` |  |
| 11 | payloadSchemaVersion | Int32 | - | Yes | Major version of the payload schema | `NumberInt(1)` |  |
| 12 | messageClass | String | - | Yes | State, event or measurement | `"State"` | State; Event; Measurement |
| 13 | hierarchyLevel | String | - | Yes | ISA-95 level of the node the message describes | `"Equipment"` | Site; Area; Line; Work Center; Equipment |
| 14 | senderType | String | - | Yes | Kind of IoT Hub identity that sends the message | `"IoT Edge Gateway"` | IoT Edge Gateway; MES Publisher |
| 15 | targetCollectionName | String | - | No (null allowed) | MES collection the ingestion service writes; null when the MES does not store the message | `"u_mes_perf_equipmentState"` |  |
| 16 | twinPropertyPath | String | - | No (null allowed) | Device twin property that holds the current state; null for events | `"properties.reported.state"` |  |
| 17 | ingestedByMes | Boolean | - | Yes | True when the MES ingestion service stores the message | `true` |  |
| 18 | routedToDataLake | Boolean | - | Yes | True when IoT Hub routing writes the message to the client data lake | `true` |  |
| 19 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 20 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ unsNamespace: 1, messageTypeCode: 1, payloadSchemaVersion: 1 }` | Yes | One definition per namespace, message type and schema version |

## Referenced by

u_mes_syst_unsRejectedMessage.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_unsMessageType.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_unsMessageType.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_unsMessageType.js
