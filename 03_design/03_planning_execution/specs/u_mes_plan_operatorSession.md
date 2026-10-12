# u_mes_plan_operatorSession

| Property | Value |
|---|---|
| Module | Planning and Execution (plan) |
| Purpose | One login-to-logout session of an operator at a station, with the authentication method and the checks done at login. |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | recordNo |
| Keys | 32 (23 required, 9 may be null) |
| Estimated volume per year | about 40,000 |
| Storage | standard collection, TTL archive after the retention period |

## Structure

Flat entity collection: one document per operator session, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1305000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"OSN-20260915-00041"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | userId | String | - | Yes | Reference to u_mes_mast_user._id | `"1029000000000002"` | Reference: u_mes_mast_user._id |
| 6 | userName | String | - | Yes | Display value of userId, copied from u_mes_mast_user.fullName | `"Kavita Bhosale"` |  |
| 7 | workCenterId | String | - | Yes | Reference to u_mes_mast_workCenter._id | `"1009000000000006"` | Reference: u_mes_mast_workCenter._id |
| 8 | workCenterName | String | - | Yes | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Piston and Seal Assembly Station"` |  |
| 9 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000006"` | Reference: u_mes_mast_equipment._id |
| 10 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Piston Assembly Press 1"` |  |
| 11 | shiftId | String | - | Yes | Reference to u_mes_mast_shift._id | `"1015000000000002"` | Reference: u_mes_mast_shift._id |
| 12 | shiftName | String | - | Yes | Display value of shiftId, copied from u_mes_mast_shift.name | `"Shift B"` |  |
| 13 | productionDate | Date | Date | Yes | Production date the session belongs to | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 14 | productionOrderId | String | - | No (null allowed) | Reference to u_mes_plan_productionOrder._id | `"1083000000000001"` | Reference: u_mes_plan_productionOrder._id |
| 15 | productionOrderName | String | - | No (null allowed) | Display value of productionOrderId, copied from u_mes_plan_productionOrder.recordNo | `"PO-1000412"` |  |
| 16 | authenticationMethod | String | - | Yes | How the operator was authenticated | `"Badge"` | Badge; Biometric; Badge And PIN; Password |
| 17 | loginAt | Date | Datetime | Yes | Login time | `ISODate("2026-09-15T05:36:27.000+0000")` |  |
| 18 | logoutAt | Date | Datetime | No (null allowed) | Logout time; null while the session is active | `ISODate("2026-09-15T08:57:00.000+0000")` |  |
| 19 | logoutReason | String | - | No (null allowed) | Why the session ended | `"Shift End"` | Operator Logout; Shift End; Timeout; Supervisor Logout; Skill Revoked |
| 20 | skillVerified | Boolean | - | Yes | Required skills were valid at login | `true` |  |
| 21 | trainingVerified | Boolean | - | Yes | Mandatory training for the station's current documents was valid at login | `true` |  |
| 22 | interlockEventId | String | - | No (null allowed) | Reference to u_mes_plan_interlockEvent._id | `null` | Reference: u_mes_plan_interlockEvent._id |
| 23 | interlockEventName | String | - | No (null allowed) | Display value of interlockEventId, copied from u_mes_plan_interlockEvent.recordNo | `null` |  |
| 24 | clientWorkstation | String | - | No (null allowed) | Terminal or HMI name | `"PN1-ASY01-HMI-01"` |  |
| 25 | status | String | - | Yes | Primary lifecycle state of the document | `"Closed"` | Active; Closed; Rejected |
| 26 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 27 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T00:00:00.000+0000")` |  |
| 28 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 29 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 30 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T08:57:00.000+0000")` |  |
| 31 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 32 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Active, Closed, Rejected. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ userId: 1 }` | No | Look-up of documents by user |
| 4 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 5 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 6 | `{ shiftId: 1 }` | No | Look-up of documents by shift |
| 7 | `{ productionOrderId: 1 }` | No | Look-up of documents by production order |
| 8 | `{ siteId: 1, productionDate: -1 }` | No | Time-ordered lists and reports by production date |

## Referenced by

u_mes_plan_operationExecution, u_mes_plan_labourBooking, u_mes_plan_documentAcknowledgement.

## Files

- Validator: 03_design/03_planning_execution/validators/u_mes_plan_operatorSession.json
- Indexes: 03_design/03_planning_execution/indexes/u_mes_plan_operatorSession.js
- Sample documents (10): 03_design/03_planning_execution/samples/u_mes_plan_operatorSession.js
