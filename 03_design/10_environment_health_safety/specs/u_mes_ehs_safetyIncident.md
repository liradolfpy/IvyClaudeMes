# u_mes_ehs_safetyIncident

| Property | Value |
|---|---|
| Module | Environment Health and Safety (ehs) |
| Purpose | Near misses, unsafe conditions, first-aid and lost-time incidents with investigation and actions |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | title |
| Keys | 45 (30 required, 15 may be null) |
| Estimated volume per year | ~400 |
| Storage | standard |

## Structure

Flat entity collection: one document per safety incident, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with safetyIncidentId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_ehs_safetyIncidentWitnessUser | Relationship | witness user |
| u_mes_ehs_safetyIncidentAction | Child | action |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1253000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SAF-2026-0003"` |  |
| 3 | app | String | - | Yes | Application context of the document: Auto = automotive caliper MES, Gamp = pharmaceutical GMP, Common = reference data shared by both | `"Auto"` | Auto; Gamp; Common |
| 4 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 5 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 6 | title | String | - | Yes | Title of the safety incident; used as its display value in other collections | `"Molten metal splash near casting machine 1"` |  |
| 7 | incidentTypeId | String | - | Yes | Reference to u_mes_ehs_incidentType._id | `"1293000000000001"` | Reference: u_mes_ehs_incidentType._id |
| 8 | incidentTypeName | String | - | Yes | Display value of incidentTypeId, copied from u_mes_ehs_incidentType.name | `"Near Miss"` |  |
| 9 | severity | Int32 | - | Yes | Severity rating 1 to 10 | `NumberInt(8)` |  |
| 10 | areaId | String | - | Yes | Reference to u_mes_mast_area._id | `"1005000000000001"` | Reference: u_mes_mast_area._id |
| 11 | areaName | String | - | Yes | Display value of areaId, copied from u_mes_mast_area.name | `"Foundry"` |  |
| 12 | workCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id | `"1009000000000001"` | Reference: u_mes_mast_workCenter._id |
| 13 | workCenterName | String | - | No (null allowed) | Display value of workCenterId, copied from u_mes_mast_workCenter.name | `"Gravity Die Casting Cell 1"` |  |
| 14 | equipmentId | String | - | No (null allowed) | Reference to u_mes_mast_equipment._id | `"1013000000000001"` | Reference: u_mes_mast_equipment._id |
| 15 | equipmentName | String | - | No (null allowed) | Display value of equipmentId, copied from u_mes_mast_equipment.name | `"Gravity Die Casting Machine 1"` |  |
| 16 | occurredAt | Date | Datetime | Yes | Date and time when the record was occurred. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 17 | reportedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'reported' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 18 | reportedBy | String | - | Yes | Display name of the user in reportedById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 19 | reportedAt | Date | Datetime | Yes | Date and time when the record was reported. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 20 | description | String | - | Yes | Description of the safety incident | `"Molten metal splash near casting machine 1; area made safe and the incident reported to the shift supervisor"` |  |
| 21 | injuredUserId | String | - | No (null allowed) | Reference to u_mes_mast_user._id: injured user | `null` | Reference: u_mes_mast_user._id |
| 22 | injuredUserName | String | - | No (null allowed) | Display value of injuredUserId, copied from u_mes_mast_user.fullName | `null` |  |
| 23 | bodyPartId | String | - | No (null allowed) | Reference to u_mes_ehs_bodyPart._id | `null` | Reference: u_mes_ehs_bodyPart._id |
| 24 | bodyPartName | String | - | No (null allowed) | Display value of bodyPartId, copied from u_mes_ehs_bodyPart.name | `null` |  |
| 25 | injuryTypeId | String | - | No (null allowed) | Reference to u_mes_ehs_injuryType._id | `null` | Reference: u_mes_ehs_injuryType._id |
| 26 | injuryTypeName | String | - | No (null allowed) | Display value of injuryTypeId, copied from u_mes_ehs_injuryType.name | `null` |  |
| 27 | firstAidGiven | Boolean | - | Yes | True when: first aid given | `false` |  |
| 28 | lostTimeDays | Int32 | - | Yes | Lost time (days) | `NumberInt(0)` |  |
| 29 | immediateAction | String | - | Yes | Immediate action | `"Area cordoned, spill cleaned, operator briefed"` |  |
| 30 | rootCause | String | - | No (null allowed) | Root cause | `"Ejector pin galled after die coating build-up"` |  |
| 31 | capaId | String | - | No (null allowed) | Reference to u_mes_qual_capa._id | `null` | Reference: u_mes_qual_capa._id |
| 32 | capaName | String | - | No (null allowed) | Display value of capaId, copied from u_mes_qual_capa.title | `null` |  |
| 33 | investigatedById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'investigated' | `"1029000000000004"` | Reference: u_mes_mast_user._id |
| 34 | investigatedBy | String | - | Yes | Display name of the user in investigatedById, copied from u_mes_mast_user.fullName | `"Anita Kulkarni"` |  |
| 35 | investigationCompletedAt | Date | Datetime | No (null allowed) | Investigation completed date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 36 | reportableToAuthority | Boolean | - | Yes | True when: reportable to authority | `false` |  |
| 37 | closedAt | Date | Datetime | No (null allowed) | Date and time when the record was closed. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 38 | status | String | - | Yes | Primary lifecycle state of the document | `"Reported"` | Reported; Under Investigation; Actions Open; Closed |
| 39 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 40 | createdAt | Date | Datetime | Yes | Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 41 | createdById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that created the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 42 | createdBy | String | - | Yes | Display name of the creator, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 43 | updatedAt | Date | Datetime | Yes | Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-09-15T06:00:00.000+0000")` |  |
| 44 | updatedById | String | - | Yes | Reference to u_mes_mast_user._id: user or process that last updated the document | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 45 | updatedBy | String | - | Yes | Display name of the last updater, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Reported, Under Investigation, Actions Open, Closed. Initial state: Reported. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ incidentTypeId: 1 }` | No | Look-up of documents by incident type |
| 4 | `{ areaId: 1 }` | No | Look-up of documents by area |
| 5 | `{ workCenterId: 1 }` | No | Look-up of documents by work center |
| 6 | `{ equipmentId: 1 }` | No | Look-up of documents by equipment |
| 7 | `{ injuredUserId: 1 }` | No | Look-up of documents by injured user |
| 8 | `{ siteId: 1, occurredAt: -1 }` | No | Time-ordered lists and reports by occurred at |

## Referenced by

u_mes_ehs_safetyIncidentWitnessUser, u_mes_ehs_safetyIncidentAction.

## Files

- Validator: 03_design/10_environment_health_safety/validators/u_mes_ehs_safetyIncident.json
- Indexes: 03_design/10_environment_health_safety/indexes/u_mes_ehs_safetyIncident.js
- Sample documents (10): 03_design/10_environment_health_safety/samples/u_mes_ehs_safetyIncident.js
