# u_mes_syst_businessEvent

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Business event stream (order released, unit started, recipe downloaded, hold placed) |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 32 (19 required, 13 may be null) |
| Estimated volume per year | ~30 million |
| Storage | standard, TTL or time-series candidate |

## Structure

Flat entity collection: one document per business event, all keys top-level and scalar.

Storage note: this collection is a candidate for a MongoDB time-series collection (time key and meta key to be fixed at deployment). A time-series collection cannot carry a JSON Schema validator, so the validator file then serves as the rule the application enforces.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1240000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"EVT-2026-000231"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | eventType | String | - | Yes | Event type | `"User Logged In"` | Order Released; Operation Started; Operation Completed; Recipe Downloaded; Hold Placed; Hold Released; Label Printed; Unit Scrapped; Shipment Dispatched; User Logged In |
| 6 | eventCategory | String | - | Yes | Event category | `"Execution"` | Execution; Quality; Material; Maintenance; Integration; Security |
| 7 | occurredAt | Date | Datetime | Yes | Date and time when the record was occurred. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 8 | relatedCollectionName | String | - | Yes | Name of the collection the related document is in | `"u_mes_plan_operationExecution"` |  |
| 9 | relatedEntityId | String | - | No (null allowed) | _id of the related document in the collection named by relatedCollectionName | `"1090000000000001"` | Reference: Any collection (see relatedCollectionName) |
| 10 | relatedEntityName | String | - | No (null allowed) | Display value of the related document | `"OPX-2026-000376"` |  |
| 11 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 12 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 13 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 14 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 15 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000004"` | Reference: u_mes_plan_productionOrder._id |
| 16 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000433"` |  |
| 17 | userId | String | - | No (null allowed) | Reference to u_mes_mast_user._id | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 18 | userName | String | - | No (null allowed) | Display value of userId, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 19 | iotDeviceId | String | - | No (null allowed) | Reference to u_mes_syst_iotDevice._id | `"1232000000000001"` | Reference: u_mes_syst_iotDevice._id |
| 20 | iotDeviceName | String | - | No (null allowed) | Display value of iotDeviceId, copied from u_mes_syst_iotDevice.name | `"PLC, casting machine 1"` |  |
| 21 | severity | Int32 | - | Yes | Severity rating 1 to 10 | `NumberInt(8)` |  |
| 22 | messageText | String | - | Yes | Message text | `"Operation OP070 completed OK on unit U260929A0184"` |  |
| 23 | eventPayloadText | String | - | No (null allowed) | Event details as JSON text | `"{\"finalTorqueNm\":\"14.2\",\"attemptNo\":1}"` |  |
| 24 | correlationNo | String | - | Yes | Identifier shared by records that belong to the same business transaction | `"c7a41e06-2d1f-4b7e-9a52-0c5f3e8b1d44"` |  |
| 25 | source | String | - | Yes | Where the record originated | `"MES Terminal"` | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| 26 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 27 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 28 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 29 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"MES System"` |  |
| 30 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-17T06:51:40.000+0000")` |  |
| 31 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000010"` | Reference: u_mes_mast_user._id |
| 32 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"MES System"` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 3 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 4 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 5 | `{ userId: 1 }` | No | Look-up of documents by user |
| 6 | `{ iotDeviceId: 1 }` | No | Look-up of documents by IoT device |
| 7 | `{ relatedCollectionName: 1, relatedEntityId: 1 }` | No | Look-up by the related document |
| 8 | `{ siteId: 1, occurredAt: -1 }` | No | Time-ordered lists and reports by occurred at |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_businessEvent.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_businessEvent.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_businessEvent.js
