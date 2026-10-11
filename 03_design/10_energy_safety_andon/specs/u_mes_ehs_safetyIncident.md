# u_mes_ehs_safetyIncident

| Property | Value |
|---|---|
| Module | Energy, safety and andon (ehs) |
| Purpose | Near misses, unsafe conditions, first-aid and lost-time incidents with investigation and actions |
| Kind | Entity |
| Data class | Transaction |
| Parent collection | none |
| _id pattern | SAF-<recordNo> |
| Display value used by references | title |
| Keys | 44 (29 required, 15 may be null) |
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

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: SAF-<recordNo> | `"SAF-2026-0003"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"2026-0003"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | title | String | Yes | Title of the safety incident; used as its display value in other collections | `"Coolant spill near HMC-01 walkway"` |  |
| 6 | incidentTypeId | String | Yes | Reference to u_mes_ehs_incidentType._id | `"ICT-NEAR-MISS"` | Reference: u_mes_ehs_incidentType._id |
| 7 | incidentTypeName | String | Yes | Display value of incidentTypeId, copied from u_mes_ehs_incidentType.name | `"Near Miss"` |  |
| 8 | severity | Int32 | Yes | Severity rating 1 to 10 | `NumberInt(8)` |  |
| 9 | areaId | String | Yes | Reference to u_mes_mdm_area._id | `"AR-ASY"` | Reference: u_mes_mdm_area._id |
| 10 | areaName | String | Yes | Display value of areaId, copied from u_mes_mdm_area.name | `"Assembly and Test"` |  |
| 11 | workCenterId | String | No (null allowed) | Reference to u_mes_mdm_workCenter._id | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 12 | workCenterName | String | No (null allowed) | Display value of workCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 13 | equipmentId | String | No (null allowed) | Reference to u_mes_mdm_equipment._id | `"EQ-TRQ-01-NR1"` | Reference: u_mes_mdm_equipment._id |
| 14 | equipmentName | String | No (null allowed) | Display value of equipmentId, copied from u_mes_mdm_equipment.name | `"DC Nutrunner Station 1"` |  |
| 15 | occurredAt | Date | Yes | Date and time when the record was occurred | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 16 | reportedById | String | Yes | Reference to u_mes_mdm_user._id: user recorded for 'reported' | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 17 | reportedBy | String | Yes | Display name of the user in reportedById, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 18 | reportedAt | Date | Yes | Date and time when the record was reported | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 19 | description | String | Yes | Description of the safety incident | `"Coolant hose leak left a wet patch on the walkway; no one slipped"` |  |
| 20 | injuredUserId | String | No (null allowed) | Reference to u_mes_mdm_user._id: injured user | `null` | Reference: u_mes_mdm_user._id |
| 21 | injuredUserName | String | No (null allowed) | Display value of injuredUserId, copied from u_mes_mdm_user.fullName | `null` |  |
| 22 | bodyPartId | String | No (null allowed) | Reference to u_mes_ehs_bodyPart._id | `null` | Reference: u_mes_ehs_bodyPart._id |
| 23 | bodyPartName | String | No (null allowed) | Display value of bodyPartId, copied from u_mes_ehs_bodyPart.name | `null` |  |
| 24 | injuryTypeId | String | No (null allowed) | Reference to u_mes_ehs_injuryType._id | `null` | Reference: u_mes_ehs_injuryType._id |
| 25 | injuryTypeName | String | No (null allowed) | Display value of injuryTypeId, copied from u_mes_ehs_injuryType.name | `null` |  |
| 26 | firstAidGiven | Boolean | Yes | True when: first aid given | `false` |  |
| 27 | lostTimeDays | Int32 | Yes | Lost time (days) | `NumberInt(0)` |  |
| 28 | immediateAction | String | Yes | Immediate action | `"Area cordoned, spill cleaned, operator briefed"` |  |
| 29 | rootCause | String | No (null allowed) | Root cause | `"Socket drive worn beyond limit"` |  |
| 30 | capaId | String | No (null allowed) | Reference to u_mes_qlt_capa._id | `"CAPA-2026-0014"` | Reference: u_mes_qlt_capa._id |
| 31 | capaName | String | No (null allowed) | Display value of capaId, copied from u_mes_qlt_capa.title | `"8D - Leak at piston seal"` |  |
| 32 | investigatedById | String | Yes | Reference to u_mes_mdm_user._id: user recorded for 'investigated' | `"USR-10087"` | Reference: u_mes_mdm_user._id |
| 33 | investigatedBy | String | Yes | Display name of the user in investigatedById, copied from u_mes_mdm_user.fullName | `"Anita Kulkarni"` |  |
| 34 | investigationCompletedAt | Date | No (null allowed) | Investigation completed date and time | `ISODate("2026-09-29T02:10:00.000+0000")` |  |
| 35 | reportableToAuthority | Boolean | Yes | True when: reportable to authority | `false` |  |
| 36 | closedAt | Date | No (null allowed) | Date and time when the record was closed | `ISODate("2026-09-29T03:45:00.000+0000")` |  |
| 37 | status | String | Yes | Primary lifecycle state of the document | `"Closed"` | Reported; Under Investigation; Actions Open; Closed |
| 38 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |
| 39 | createdAt | Date | Yes | Date and time the document was created | `ISODate("2026-09-29T00:30:00.000+0000")` |  |
| 40 | createdById | String | Yes | Reference to u_mes_mdm_user._id: user or process that created the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 41 | createdBy | String | Yes | Display name of the creator, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |
| 42 | updatedAt | Date | Yes | Date and time of the most recent update | `ISODate("2026-09-29T03:45:00.000+0000")` |  |
| 43 | updatedById | String | Yes | Reference to u_mes_mdm_user._id: user or process that last updated the document | `"USR-10231"` | Reference: u_mes_mdm_user._id |
| 44 | updatedBy | String | Yes | Display name of the last updater, copied from u_mes_mdm_user.fullName | `"Sunil Jadhav"` |  |

## Status values

Reported, Under Investigation, Actions Open, Closed. Initial state: Reported. The values are maintained in u_mes_sys_statusDefinition.

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

- Validator: 03_design/10_energy_safety_andon/validators/u_mes_ehs_safetyIncident.json
- Indexes: 03_design/10_energy_safety_andon/indexes/u_mes_ehs_safetyIncident.js
- Sample document: 03_design/10_energy_safety_andon/samples/u_mes_ehs_safetyIncident.js
