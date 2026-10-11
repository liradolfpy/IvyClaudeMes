# Field list - Environment Health and Safety (ehs)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/10_environment_health_safety/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_ehs_safetyIncident

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | title | String |  |
| 6 | incidentTypeId | String | u_mes_ehs_incidentType._id |
| 7 | incidentTypeName | String |  |
| 8 | severity | Int32 |  |
| 9 | areaId | String | u_mes_mast_area._id |
| 10 | areaName | String |  |
| 11 | workCenterId | String | u_mes_mast_workCenter._id |
| 12 | workCenterName | String |  |
| 13 | equipmentId | String | u_mes_mast_equipment._id |
| 14 | equipmentName | String |  |
| 15 | occurredAt | Date |  |
| 16 | reportedById | String | u_mes_mast_user._id |
| 17 | reportedBy | String |  |
| 18 | reportedAt | Date |  |
| 19 | description | String |  |
| 20 | injuredUserId | String | u_mes_mast_user._id |
| 21 | injuredUserName | String |  |
| 22 | bodyPartId | String | u_mes_ehs_bodyPart._id |
| 23 | bodyPartName | String |  |
| 24 | injuryTypeId | String | u_mes_ehs_injuryType._id |
| 25 | injuryTypeName | String |  |
| 26 | firstAidGiven | Boolean |  |
| 27 | lostTimeDays | Int32 |  |
| 28 | immediateAction | String |  |
| 29 | rootCause | String |  |
| 30 | capaId | String | u_mes_qual_capa._id |
| 31 | capaName | String |  |
| 32 | investigatedById | String | u_mes_mast_user._id |
| 33 | investigatedBy | String |  |
| 34 | investigationCompletedAt | Date |  |
| 35 | reportableToAuthority | Boolean |  |
| 36 | closedAt | Date |  |
| 37 | status | String |  |
| 38 | schemaVersion | Int32 |  |
| 39 | createdAt | Date |  |
| 40 | createdById | String | u_mes_mast_user._id |
| 41 | createdBy | String |  |
| 42 | updatedAt | Date |  |
| 43 | updatedById | String | u_mes_mast_user._id |
| 44 | updatedBy | String |  |

## u_mes_ehs_safetyIncidentWitnessUser

Kind: relationship | Data class: transaction | Parent: u_mes_ehs_safetyIncident | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | safetyIncidentId | String | u_mes_ehs_safetyIncident._id |
| 6 | safetyIncidentName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | witnessUserId | String | u_mes_mast_user._id |
| 9 | witnessUserName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mast_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mast_user._id |
| 16 | updatedBy | String |  |

## u_mes_ehs_safetyIncidentAction

Kind: child | Data class: transaction | Parent: u_mes_ehs_safetyIncident | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | safetyIncidentId | String | u_mes_ehs_safetyIncident._id |
| 6 | safetyIncidentName | String |  |
| 7 | actionNo | Int32 |  |
| 8 | description | String |  |
| 9 | ownerUserId | String | u_mes_mast_user._id |
| 10 | ownerUserName | String |  |
| 11 | dueAt | Date |  |
| 12 | completedAt | Date |  |
| 13 | schemaVersion | Int32 |  |
| 14 | createdAt | Date |  |
| 15 | createdById | String | u_mes_mast_user._id |
| 16 | createdBy | String |  |
| 17 | updatedAt | Date |  |
| 18 | updatedById | String | u_mes_mast_user._id |
| 19 | updatedBy | String |  |

## u_mes_ehs_incidentType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | description | String |  |
| 7 | isInjury | Boolean |  |
| 8 | reportableToAuthority | Boolean |  |
| 9 | sequenceNo | Int32 |  |
| 10 | status | String |  |
| 11 | schemaVersion | Int32 |  |

## u_mes_ehs_bodyPart

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | description | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | status | String |  |
| 9 | schemaVersion | Int32 |  |

## u_mes_ehs_injuryType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mast_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | description | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | status | String |  |
| 9 | schemaVersion | Int32 |  |
