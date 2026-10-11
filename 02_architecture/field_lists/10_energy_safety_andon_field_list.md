# Field list - Energy, safety and andon (ehs)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/10_energy_safety_andon/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_ehs_energyReading

Kind: entity | Data class: transaction | Parent: - | _id pattern: ENR-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | meterIotDeviceId | String | u_mes_sys_iotDevice._id |
| 6 | meterIotDeviceName | String |  |
| 7 | equipmentId | String | u_mes_mdm_equipment._id |
| 8 | equipmentName | String |  |
| 9 | lineId | String | u_mes_mdm_line._id |
| 10 | lineName | String |  |
| 11 | shiftId | String | u_mes_mdm_shift._id |
| 12 | shiftName | String |  |
| 13 | energyTypeId | String | u_mes_ehs_energyType._id |
| 14 | energyTypeName | String |  |
| 15 | intervalStartAt | Date |  |
| 16 | intervalEndAt | Date |  |
| 17 | consumption | Decimal128 |  |
| 18 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 19 | unitOfMeasureName | String |  |
| 20 | meterReadingStart | Decimal128 |  |
| 21 | meterReadingEnd | Decimal128 |  |
| 22 | demandKw | Decimal128 |  |
| 23 | powerFactor | Double |  |
| 24 | costInr | Decimal128 |  |
| 25 | unitsProduced | Int32 |  |
| 26 | specificConsumption | Decimal128 |  |
| 27 | signalQuality | String |  |
| 28 | schemaVersion | Int32 |  |
| 29 | createdAt | Date |  |
| 30 | createdById | String | u_mes_mdm_user._id |
| 31 | createdBy | String |  |
| 32 | updatedAt | Date |  |
| 33 | updatedById | String | u_mes_mdm_user._id |
| 34 | updatedBy | String |  |

## u_mes_ehs_andonEvent

Kind: entity | Data class: transaction | Parent: - | _id pattern: AND-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workCenterId | String | u_mes_mdm_workCenter._id |
| 6 | workCenterName | String |  |
| 7 | lineId | String | u_mes_mdm_line._id |
| 8 | lineName | String |  |
| 9 | shiftId | String | u_mes_mdm_shift._id |
| 10 | shiftName | String |  |
| 11 | andonTypeId | String | u_mes_ehs_andonType._id |
| 12 | andonTypeName | String |  |
| 13 | reasonCodeId | String | u_mes_eqp_reasonCode._id |
| 14 | reasonCodeName | String |  |
| 15 | raisedById | String | u_mes_mdm_user._id |
| 16 | raisedBy | String |  |
| 17 | raisedAt | Date |  |
| 18 | acknowledgedById | String | u_mes_mdm_user._id |
| 19 | acknowledgedBy | String |  |
| 20 | acknowledgedAt | Date |  |
| 21 | resolvedById | String | u_mes_mdm_user._id |
| 22 | resolvedBy | String |  |
| 23 | resolvedAt | Date |  |
| 24 | responseSec | Int32 |  |
| 25 | resolutionSec | Int32 |  |
| 26 | lineStopped | Boolean |  |
| 27 | downtimeEventId | String | u_mes_eqp_downtimeEvent._id |
| 28 | downtimeEventName | String |  |
| 29 | description | String |  |
| 30 | resolutionText | String |  |
| 31 | status | String |  |
| 32 | schemaVersion | Int32 |  |
| 33 | createdAt | Date |  |
| 34 | createdById | String | u_mes_mdm_user._id |
| 35 | createdBy | String |  |
| 36 | updatedAt | Date |  |
| 37 | updatedById | String | u_mes_mdm_user._id |
| 38 | updatedBy | String |  |

## u_mes_ehs_andonEventEscalation

Kind: child | Data class: transaction | Parent: u_mes_ehs_andonEvent | _id pattern: <andonEventId>-E<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | andonEventId | String | u_mes_ehs_andonEvent._id |
| 6 | andonEventName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | level | Int32 |  |
| 9 | escalatedAt | Date |  |
| 10 | toUserId | String | u_mes_mdm_user._id |
| 11 | toUserName | String |  |
| 12 | channel | String |  |
| 13 | schemaVersion | Int32 |  |
| 14 | createdAt | Date |  |
| 15 | createdById | String | u_mes_mdm_user._id |
| 16 | createdBy | String |  |
| 17 | updatedAt | Date |  |
| 18 | updatedById | String | u_mes_mdm_user._id |
| 19 | updatedBy | String |  |

## u_mes_ehs_safetyIncident

Kind: entity | Data class: transaction | Parent: - | _id pattern: SAF-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | title | String |  |
| 6 | incidentTypeId | String | u_mes_ehs_incidentType._id |
| 7 | incidentTypeName | String |  |
| 8 | severity | Int32 |  |
| 9 | areaId | String | u_mes_mdm_area._id |
| 10 | areaName | String |  |
| 11 | workCenterId | String | u_mes_mdm_workCenter._id |
| 12 | workCenterName | String |  |
| 13 | equipmentId | String | u_mes_mdm_equipment._id |
| 14 | equipmentName | String |  |
| 15 | occurredAt | Date |  |
| 16 | reportedById | String | u_mes_mdm_user._id |
| 17 | reportedBy | String |  |
| 18 | reportedAt | Date |  |
| 19 | description | String |  |
| 20 | injuredUserId | String | u_mes_mdm_user._id |
| 21 | injuredUserName | String |  |
| 22 | bodyPartId | String | u_mes_ehs_bodyPart._id |
| 23 | bodyPartName | String |  |
| 24 | injuryTypeId | String | u_mes_ehs_injuryType._id |
| 25 | injuryTypeName | String |  |
| 26 | firstAidGiven | Boolean |  |
| 27 | lostTimeDays | Int32 |  |
| 28 | immediateAction | String |  |
| 29 | rootCause | String |  |
| 30 | capaId | String | u_mes_qlt_capa._id |
| 31 | capaName | String |  |
| 32 | investigatedById | String | u_mes_mdm_user._id |
| 33 | investigatedBy | String |  |
| 34 | investigationCompletedAt | Date |  |
| 35 | reportableToAuthority | Boolean |  |
| 36 | closedAt | Date |  |
| 37 | status | String |  |
| 38 | schemaVersion | Int32 |  |
| 39 | createdAt | Date |  |
| 40 | createdById | String | u_mes_mdm_user._id |
| 41 | createdBy | String |  |
| 42 | updatedAt | Date |  |
| 43 | updatedById | String | u_mes_mdm_user._id |
| 44 | updatedBy | String |  |

## u_mes_ehs_safetyIncidentWitnessUser

Kind: relationship | Data class: transaction | Parent: u_mes_ehs_safetyIncident | _id pattern: <safetyIncidentId>-WU<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | safetyIncidentId | String | u_mes_ehs_safetyIncident._id |
| 6 | safetyIncidentName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | witnessUserId | String | u_mes_mdm_user._id |
| 9 | witnessUserName | String |  |
| 10 | schemaVersion | Int32 |  |
| 11 | createdAt | Date |  |
| 12 | createdById | String | u_mes_mdm_user._id |
| 13 | createdBy | String |  |
| 14 | updatedAt | Date |  |
| 15 | updatedById | String | u_mes_mdm_user._id |
| 16 | updatedBy | String |  |

## u_mes_ehs_safetyIncidentAction

Kind: child | Data class: transaction | Parent: u_mes_ehs_safetyIncident | _id pattern: <safetyIncidentId>-A<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | safetyIncidentId | String | u_mes_ehs_safetyIncident._id |
| 6 | safetyIncidentName | String |  |
| 7 | actionNo | Int32 |  |
| 8 | description | String |  |
| 9 | ownerUserId | String | u_mes_mdm_user._id |
| 10 | ownerUserName | String |  |
| 11 | dueAt | Date |  |
| 12 | completedAt | Date |  |
| 13 | schemaVersion | Int32 |  |
| 14 | createdAt | Date |  |
| 15 | createdById | String | u_mes_mdm_user._id |
| 16 | createdBy | String |  |
| 17 | updatedAt | Date |  |
| 18 | updatedById | String | u_mes_mdm_user._id |
| 19 | updatedBy | String |  |

## u_mes_ehs_andonType

Kind: entity | Data class: master | Parent: - | _id pattern: ANT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | description | String |  |
| 7 | colourCode | String |  |
| 8 | responsibleDepartmentId | String | u_mes_mdm_department._id |
| 9 | responsibleDepartmentName | String |  |
| 10 | targetResponseSec | Int32 |  |
| 11 | sequenceNo | Int32 |  |
| 12 | status | String |  |
| 13 | schemaVersion | Int32 |  |

## u_mes_ehs_incidentType

Kind: entity | Data class: master | Parent: - | _id pattern: ICT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | description | String |  |
| 7 | isInjury | Boolean |  |
| 8 | reportableToAuthority | Boolean |  |
| 9 | sequenceNo | Int32 |  |
| 10 | status | String |  |
| 11 | schemaVersion | Int32 |  |

## u_mes_ehs_energyType

Kind: entity | Data class: master | Parent: - | _id pattern: ENT-T-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | description | String |  |
| 7 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 8 | unitOfMeasureName | String |  |
| 9 | sequenceNo | Int32 |  |
| 10 | status | String |  |
| 11 | schemaVersion | Int32 |  |

## u_mes_ehs_bodyPart

Kind: entity | Data class: master | Parent: - | _id pattern: BDP-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | description | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | status | String |  |
| 9 | schemaVersion | Int32 |  |

## u_mes_ehs_injuryType

Kind: entity | Data class: master | Parent: - | _id pattern: INJ-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | description | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | status | String |  |
| 9 | schemaVersion | Int32 |  |
