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
| 13 | energyType | String |  |
| 14 | intervalStartAt | Date |  |
| 15 | intervalEndAt | Date |  |
| 16 | consumption | Decimal128 |  |
| 17 | unitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 18 | unitOfMeasureName | String |  |
| 19 | meterReadingStart | Decimal128 |  |
| 20 | meterReadingEnd | Decimal128 |  |
| 21 | demandKw | Decimal128 |  |
| 22 | powerFactor | Double |  |
| 23 | costInr | Decimal128 |  |
| 24 | unitsProduced | Int32 |  |
| 25 | specificConsumption | Decimal128 |  |
| 26 | signalQuality | String |  |
| 27 | schemaVersion | Int32 |  |
| 28 | createdAt | Date |  |
| 29 | createdById | String | u_mes_mdm_user._id |
| 30 | createdBy | String |  |
| 31 | updatedAt | Date |  |
| 32 | updatedById | String | u_mes_mdm_user._id |
| 33 | updatedBy | String |  |

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
| 11 | andonType | String |  |
| 12 | reasonCodeId | String | u_mes_eqp_reasonCode._id |
| 13 | reasonCodeName | String |  |
| 14 | raisedById | String | u_mes_mdm_user._id |
| 15 | raisedBy | String |  |
| 16 | raisedAt | Date |  |
| 17 | acknowledgedById | String | u_mes_mdm_user._id |
| 18 | acknowledgedBy | String |  |
| 19 | acknowledgedAt | Date |  |
| 20 | resolvedById | String | u_mes_mdm_user._id |
| 21 | resolvedBy | String |  |
| 22 | resolvedAt | Date |  |
| 23 | responseSec | Int32 |  |
| 24 | resolutionSec | Int32 |  |
| 25 | lineStopped | Boolean |  |
| 26 | downtimeEventId | String | u_mes_eqp_downtimeEvent._id |
| 27 | downtimeEventName | String |  |
| 28 | description | String |  |
| 29 | resolutionText | String |  |
| 30 | status | String |  |
| 31 | schemaVersion | Int32 |  |
| 32 | createdAt | Date |  |
| 33 | createdById | String | u_mes_mdm_user._id |
| 34 | createdBy | String |  |
| 35 | updatedAt | Date |  |
| 36 | updatedById | String | u_mes_mdm_user._id |
| 37 | updatedBy | String |  |

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
| 6 | incidentType | String |  |
| 7 | severity | Int32 |  |
| 8 | areaId | String | u_mes_mdm_area._id |
| 9 | areaName | String |  |
| 10 | workCenterId | String | u_mes_mdm_workCenter._id |
| 11 | workCenterName | String |  |
| 12 | equipmentId | String | u_mes_mdm_equipment._id |
| 13 | equipmentName | String |  |
| 14 | occurredAt | Date |  |
| 15 | reportedById | String | u_mes_mdm_user._id |
| 16 | reportedBy | String |  |
| 17 | reportedAt | Date |  |
| 18 | description | String |  |
| 19 | injuredUserId | String | u_mes_mdm_user._id |
| 20 | injuredUserName | String |  |
| 21 | bodyPart | String |  |
| 22 | injuryType | String |  |
| 23 | firstAidGiven | Boolean |  |
| 24 | lostTimeDays | Int32 |  |
| 25 | immediateAction | String |  |
| 26 | rootCause | String |  |
| 27 | capaId | String | u_mes_qlt_capa._id |
| 28 | capaName | String |  |
| 29 | investigatedById | String | u_mes_mdm_user._id |
| 30 | investigatedBy | String |  |
| 31 | investigationCompletedAt | Date |  |
| 32 | reportableToAuthority | Boolean |  |
| 33 | closedAt | Date |  |
| 34 | status | String |  |
| 35 | schemaVersion | Int32 |  |
| 36 | createdAt | Date |  |
| 37 | createdById | String | u_mes_mdm_user._id |
| 38 | createdBy | String |  |
| 39 | updatedAt | Date |  |
| 40 | updatedById | String | u_mes_mdm_user._id |
| 41 | updatedBy | String |  |

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
