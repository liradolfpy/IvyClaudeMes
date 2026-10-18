## u_mes_ehs_bodyPart - Body Parts (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_ehs_bodyPart.json | _id: mes_ehs_bodyPartStable | rel: CL20261018-23:51 | samples: 10 | columns: 5 | total width: 560px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 8 | 110px | left |
| 2 | name | Name | String | 8 | 80px | left |
| 3 | description | Description | String | 19 | 160px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_ehs_incidentType - Incident Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_ehs_incidentType.json | _id: mes_ehs_incidentTypeStable | rel: CL20261018-23:51 | samples: 10 | columns: 7 | total width: 1060px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 11 | 110px | left |
| 2 | name | Name | String | 22 | 180px | left |
| 3 | description | Description | String | 34 | 260px | left |
| 4 | isInjury | Injury | Boolean | 3 | 90px | center |
| 5 | reportableToAuthority | Reportable to Authority | Boolean | 3 | 210px | center |
| 6 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 7 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_ehs_injuryType - Injury Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_ehs_injuryType.json | _id: mes_ehs_injuryTypeStable | rel: CL20261018-23:51 | samples: 10 | columns: 5 | total width: 690px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | name | Name | String | 19 | 160px | left |
| 3 | description | Description | String | 27 | 210px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_ehs_safetyIncident - Safety Incidents (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_ehs_safetyIncident.json | _id: mes_ehs_safetyIncidentStable | rel: CL20261018-23:51 | samples: 10 | columns: 28 | total width: 4980px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | title | Title | String | 61 | 300px | left |
| 3 | incidentTypeName | Incident Type | String | 22 | 180px | left |
| 4 | severity | Severity | Int32 | 2 | 100px | right |
| 5 | areaName | Area | String | 28 | 220px | left |
| 6 | workCenterName | Work Center | String | 33 | 260px | left |
| 7 | equipmentName | Equipment | String | 31 | 240px | left |
| 8 | occurredAt | Occurred At | Date/Datetime | 19 | 160px | center |
| 9 | reportedBy | Reported By | String | 14 | 120px | left |
| 10 | reportedAt | Reported At | Date/Datetime | 19 | 160px | center |
| 11 | description | Description | String | 127 | 300px | left |
| 12 | injuredUserName | Injured User | String | 0 | 130px | left |
| 13 | bodyPartName | Body Part | String | 6 | 110px | left |
| 14 | injuryTypeName | Injury Type | String | 14 | 120px | left |
| 15 | firstAidGiven | First Aid Given | Boolean | 3 | 150px | center |
| 16 | lostTimeDays | Lost Time (days) | Int32 | 1 | 160px | right |
| 17 | immediateAction | Immediate Action | String | 46 | 300px | left |
| 18 | rootCause | Root Cause | String | 74 | 300px | left |
| 19 | capaName | CAPA | String | 0 | 80px | left |
| 20 | investigatedBy | Investigated By | String | 14 | 150px | left |
| 21 | investigationCompletedAt | Investigation Completed At | Date/Datetime | 19 | 230px | center |
| 22 | reportableToAuthority | Reportable to Authority | Boolean | 3 | 210px | center |
| 23 | closedAt | Closed At | Date/Datetime | 19 | 160px | center |
| 24 | status | Status | String | 19 | 160px | left |
| 25 | createdBy | Created By | String | 14 | 120px | left |
| 26 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 27 | updatedBy | Updated By | String | 14 | 120px | left |
| 28 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); incidentTypeId (reference key, shown through incidentTypeName); areaId (reference key, shown through areaName); workCenterId (reference key, shown through workCenterName); equipmentId (reference key, shown through equipmentName); reportedById (reference key, shown through reportedBy); injuredUserId (reference key, shown through injuredUserName); bodyPartId (reference key, shown through bodyPartName); injuryTypeId (reference key, shown through injuryTypeName); capaId (reference key, shown through capaName); investigatedById (reference key, shown through investigatedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): injuredUserName, capaName

## u_mes_ehs_safetyIncidentAction - Safety Incident Actions (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_ehs_safetyIncidentAction.json | _id: mes_ehs_safetyIncidentActionStable | rel: CL20261018-23:51 | samples: 10 | columns: 11 | total width: 1850px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | safetyIncidentName | Safety Incident | String | 61 | 300px | left |
| 3 | actionNo | Action No | Int32 | 1 | 110px | right |
| 4 | description | Description | String | 62 | 300px | left |
| 5 | ownerUserName | Owner User | String | 14 | 120px | left |
| 6 | dueAt | Due At | Date/Datetime | 19 | 160px | center |
| 7 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 8 | createdBy | Created By | String | 14 | 120px | left |
| 9 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 10 | updatedBy | Updated By | String | 14 | 120px | left |
| 11 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); safetyIncidentId (reference key, shown through safetyIncidentName); ownerUserId (reference key, shown through ownerUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_ehs_safetyIncidentWitnessUser - Safety Incident Witnesses (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_ehs_safetyIncidentWitnessUser.json | _id: mes_ehs_safetyIncidentWitnessUserStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1260px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | safetyIncidentName | Safety Incident | String | 61 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | witnessUserName | Witness User | String | 15 | 130px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); safetyIncidentId (reference key, shown through safetyIncidentName); witnessUserId (reference key, shown through witnessUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))
