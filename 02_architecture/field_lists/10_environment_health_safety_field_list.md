# Field list - Environment Health and Safety (ehs)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/10_environment_health_safety/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_ehs_safetyIncident

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | title | String | - |  |
| 7 | incidentTypeId | String | - | u_mes_ehs_incidentType._id |
| 8 | incidentTypeName | String | - |  |
| 9 | severity | Int32 | - |  |
| 10 | areaId | String | - | u_mes_mast_area._id |
| 11 | areaName | String | - |  |
| 12 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 13 | workCenterName | String | - |  |
| 14 | equipmentId | String | - | u_mes_mast_equipment._id |
| 15 | equipmentName | String | - |  |
| 16 | occurredAt | Date | Datetime |  |
| 17 | reportedById | String | - | u_mes_mast_user._id |
| 18 | reportedBy | String | - |  |
| 19 | reportedAt | Date | Datetime |  |
| 20 | description | String | - |  |
| 21 | injuredUserId | String | - | u_mes_mast_user._id |
| 22 | injuredUserName | String | - |  |
| 23 | bodyPartId | String | - | u_mes_ehs_bodyPart._id |
| 24 | bodyPartName | String | - |  |
| 25 | injuryTypeId | String | - | u_mes_ehs_injuryType._id |
| 26 | injuryTypeName | String | - |  |
| 27 | firstAidGiven | Boolean | - |  |
| 28 | lostTimeDays | Int32 | - |  |
| 29 | immediateAction | String | - |  |
| 30 | rootCause | String | - |  |
| 31 | capaId | String | - | u_mes_qual_capa._id |
| 32 | capaName | String | - |  |
| 33 | investigatedById | String | - | u_mes_mast_user._id |
| 34 | investigatedBy | String | - |  |
| 35 | investigationCompletedAt | Date | Datetime |  |
| 36 | reportableToAuthority | Boolean | - |  |
| 37 | closedAt | Date | Datetime |  |
| 38 | status | String | - |  |
| 39 | schemaVersion | Int32 | - |  |
| 40 | createdAt | Date | Datetime |  |
| 41 | createdById | String | - | u_mes_mast_user._id |
| 42 | createdBy | String | - |  |
| 43 | updatedAt | Date | Datetime |  |
| 44 | updatedById | String | - | u_mes_mast_user._id |
| 45 | updatedBy | String | - |  |

## u_mes_ehs_safetyIncidentWitnessUser

Kind: relationship | Data class: transaction | Parent: u_mes_ehs_safetyIncident | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | safetyIncidentId | String | - | u_mes_ehs_safetyIncident._id |
| 7 | safetyIncidentName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | witnessUserId | String | - | u_mes_mast_user._id |
| 10 | witnessUserName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |
| 12 | createdAt | Date | Datetime |  |
| 13 | createdById | String | - | u_mes_mast_user._id |
| 14 | createdBy | String | - |  |
| 15 | updatedAt | Date | Datetime |  |
| 16 | updatedById | String | - | u_mes_mast_user._id |
| 17 | updatedBy | String | - |  |

## u_mes_ehs_safetyIncidentAction

Kind: child | Data class: transaction | Parent: u_mes_ehs_safetyIncident | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | safetyIncidentId | String | - | u_mes_ehs_safetyIncident._id |
| 7 | safetyIncidentName | String | - |  |
| 8 | actionNo | Int32 | - |  |
| 9 | description | String | - |  |
| 10 | ownerUserId | String | - | u_mes_mast_user._id |
| 11 | ownerUserName | String | - |  |
| 12 | dueAt | Date | Datetime |  |
| 13 | completedAt | Date | Datetime |  |
| 14 | schemaVersion | Int32 | - |  |
| 15 | createdAt | Date | Datetime |  |
| 16 | createdById | String | - | u_mes_mast_user._id |
| 17 | createdBy | String | - |  |
| 18 | updatedAt | Date | Datetime |  |
| 19 | updatedById | String | - | u_mes_mast_user._id |
| 20 | updatedBy | String | - |  |

## u_mes_ehs_incidentType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | isInjury | Boolean | - |  |
| 9 | reportableToAuthority | Boolean | - |  |
| 10 | sequenceNo | Int32 | - |  |
| 11 | status | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_ehs_bodyPart

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | status | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_ehs_injuryType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | description | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | status | String | - |  |
| 10 | schemaVersion | Int32 | - |  |
