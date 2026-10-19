# u_mes_syst_unsRejectedMessage

| Property | Value |
|---|---|
| Module | SystemAndIntegration (syst) |
| Purpose | One UNS message that the MES ingestion service could not store, with the reason, the payload as received, the copy in the dead-letter container and how it was resolved (sent again after correction, or discarded). |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 33 (21 required, 12 may be null) |
| Estimated volume per year | about 500 per year |
| Storage | standard collection, archive after 1 year |

## Structure

Flat entity collection: one document per uns rejected message, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1372000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"URM-20260915-00001"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | messageUuid | String | - | Yes | Envelope msgId and IoT Hub message-id of the rejected message | `"9b39d912-cd4b-5701-92bd-245b70e7b4fe"` |  |
| 7 | iotHubIdentityId | String | - | Yes | Reference to u_mes_syst_iotHubIdentity._id | `"1371000000000006"` | Reference: u_mes_syst_iotHubIdentity._id |
| 8 | iotHubIdentityName | String | - | Yes | Display value of iotHubIdentityId, copied from u_mes_syst_iotHubIdentity.name | `"DC Nutrunner Station 1"` |  |
| 9 | unsMessageTypeId | String | - | No (null allowed) | Reference to u_mes_syst_unsMessageType._id | `"1370000000000005"` | Reference: u_mes_syst_unsMessageType._id |
| 10 | unsMessageTypeName | String | - | No (null allowed) | Display value of unsMessageTypeId, copied from u_mes_syst_unsMessageType.name | `"Tightening result"` |  |
| 11 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000007"` | Reference: u_mes_mast_equipment._id |
| 12 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"DC Nutrunner Station 1"` |  |
| 13 | isa95Path | String | - | No (null allowed) | ISA-95 path stamped by IoT Hub message enrichment; null when missing | `"VBS/PN1/ASY/ASY-01/TRQ-01/TRQ-01-N1"` |  |
| 14 | payloadSchemaName | String | - | No (null allowed) | Schema named in the envelope; null when the envelope cannot be read | `"uns.edge.result.tightening/1"` |  |
| 15 | messageTimestamp | Date | Datetime | No (null allowed) | Envelope ts as plant time; null when missing or unreadable | `ISODate("2026-09-15T06:04:08.000+0000")` |  |
| 16 | receivedAt | Date | Datetime | Yes | Time the ingestion service read the message | `ISODate("2026-09-15T06:04:09.000+0000")` |  |
| 17 | rejectionReason | String | - | Yes | Rule that rejected the message | `"Unresolved Master Reference"` | Invalid Envelope; Unknown Schema; Unresolved Master Reference; Clock Skew; Validator Failure |
| 18 | rejectionDetailText | String | - | Yes | Detail of the failed check | `"data.unitId U260915A0198 not found among the WIP units; the unit label was printed but the WIP unit was not created at piston and seal assembly"` |  |
| 19 | payloadText | String | - | Yes | Message body as received (UTF-8 JSON text) | `"{\"schema\": \"uns.edge.result.tightening/1\", \"msgId\": \"9b39d912-cd4b-5701-92bd-245b70e7b4fe\", \"ts\": \"2026-09-15T06:04:08.000+05:30\", \"tsSource\": \"Device\", \"producer\": \"NR-CTRL-01\", \"seq\": 1000, \"data\": {\"controllerResultNo\": \"PF6-000418874\", \"unitId\": \"U260915A0198\", \"programNo\": \"PSET-07\", \"jointName\": \"Bleed screw M10x1.0\", \"tighteningNo\": 1, \"strategy\": \"Torque Control\", \"targetTorqueNm\": 14.0, \"minTorqueNm\": 12.0, \"maxTorqueNm\": 16.0, \"finalTorqueNm\": 14.1, \"targetAngleDeg\": 40.0, \"minAngleDeg\": 20.0, \"maxAngleDeg\": 70.0, \"finalAngleDeg\": 39.2, \"rundownTimeMs\": 1810, \"result\": \"OK\"}}"` |  |
| 20 | deadLetterBlobPath | String | - | Yes | Path of the copy in the uns-deadletter blob container | `"uns-deadletter/2026/09/15/9b39d912-cd4b-5701-92bd-245b70e7b4fe.json"` |  |
| 21 | resolvedById | String | - | No (null allowed) | Reference to u_mes_mast_user._id: user recorded for 'resolved' | `null` | Reference: u_mes_mast_user._id |
| 22 | resolvedBy | String | - | No (null allowed) | Display name of the user in resolvedById, copied from u_mes_mast_user.fullName | `null` |  |
| 23 | resolvedAt | Date | Datetime | No (null allowed) | Time of the resolution | `ISODate("2026-09-15T09:40:00.000+0000")` |  |
| 24 | resolutionText | String | - | No (null allowed) | What was corrected, or why the message was discarded | `"WIP unit U260915A0198 created by the supervisor after checking the unit at the station; message sent again and stored"` |  |
| 25 | resentMessageUuid | String | - | No (null allowed) | msgId of the corrected message sent again; null when open or discarded | `"194136e2-8a0c-5163-bd90-d62286c3711f"` |  |
| 26 | status | String | - | Yes | Primary lifecycle state of the document | `"Resent"` | Open; Resent; Discarded |
| 27 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 28 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:04:08.000+0000")` |  |
| 29 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 30 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 31 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T09:40:00.000+0000")` |  |
| 32 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 33 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Open, Resent, Discarded. Initial state: Open. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ iotHubIdentityId: 1 }` | No | Look-up of documents by IoT hub IDentity |
| 4 | `{ unsMessageTypeId: 1 }` | No | Look-up of documents by uns message type |
| 5 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 6 | `{ siteId: 1, messageTimestamp: -1 }` | No | Time-ordered lists and reports by message timestamp |
| 7 | `{ messageUuid: 1 }` | Yes | One rejection record per UNS message |
| 8 | `{ siteId: 1, status: 1, receivedAt: -1 }` | No | Open rejections, newest first |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_unsRejectedMessage.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_unsRejectedMessage.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_unsRejectedMessage.js
