## u_mes_perf_alarm - Alarms (Telemetry)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_alarm.json | _id: mes_perf_alarmStable | rel: CL20261018-22:43 | samples: 10 | columns: 35 | total width: 5880px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | equipmentName | Equipment | String | 31 | 240px | left |
| 3 | processTagName | Process Tag | String | 46 | 300px | left |
| 4 | iotDeviceName | IoT Device | String | 38 | 290px | left |
| 5 | alarmCode | Alarm Code | String | 5 | 110px | left |
| 6 | alarmText | Alarm Text | String | 56 | 300px | left |
| 7 | alarmClass | Alarm Class | String | 7 | 120px | left |
| 8 | severity | Severity | Int32 | 2 | 100px | right |
| 9 | raisedAt | Raised At | Date/Datetime | 19 | 160px | center |
| 10 | acknowledgedAt | Acknowledged At | Date/Datetime | 19 | 160px | center |
| 11 | acknowledgedBy | Acknowledged By | String | 12 | 150px | left |
| 12 | clearedAt | Cleared At | Date/Datetime | 19 | 160px | center |
| 13 | durationSec | Duration (s) | Int32 | 2 | 130px | right |
| 14 | triggerValue | Trigger Value | Decimal128 | 5 | 140px | right |
| 15 | limitValue | Limit Value | Decimal128 | 5 | 120px | right |
| 16 | productionOrderName | Production Order | String | 10 | 160px | left |
| 17 | causedStop | Caused Stop | Boolean | 3 | 120px | center |
| 18 | downtimeEventName | Downtime Event | String | 14 | 140px | left |
| 19 | actionTaken | Action Taken | String | 69 | 300px | left |
| 20 | alarmDefinitionName | Alarm Definition | String | 13 | 160px | left |
| 21 | lineName | Line | String | 35 | 270px | left |
| 22 | workCenterName | Work Center | String | 33 | 260px | left |
| 23 | shiftName | Shift | String | 7 | 80px | left |
| 24 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 25 | wipUnitName | WIP Unit | String | 0 | 100px | left |
| 26 | blocksRestart | Blocks Restart | Boolean | 3 | 140px | center |
| 27 | restartAuthorizedBy | Restart Authorized By | String | 12 | 190px | left |
| 28 | restartAuthorizedAt | Restart Authorized At | Date/Datetime | 19 | 190px | center |
| 29 | closureReasonCodeName | Closure Reason Code | String | 25 | 200px | left |
| 30 | escalationLevel | Escalation Level | Int32 | 1 | 160px | right |
| 31 | status | Status | String | 12 | 110px | left |
| 32 | createdBy | Created By | String | 10 | 110px | left |
| 33 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 34 | updatedBy | Updated By | String | 10 | 110px | left |
| 35 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); processTagId (reference key, shown through processTagName); iotDeviceId (reference key, shown through iotDeviceName); acknowledgedById (reference key, shown through acknowledgedBy); productionOrderId (reference key, shown through productionOrderName); downtimeEventId (reference key, shown through downtimeEventName); alarmDefinitionId (reference key, shown through alarmDefinitionName); lineId (reference key, shown through lineName); workCenterId (reference key, shown through workCenterName); shiftId (reference key, shown through shiftName); wipUnitId (reference key, shown through wipUnitName); restartAuthorizedById (reference key, shown through restartAuthorizedBy); closureReasonCodeId (reference key, shown through closureReasonCodeName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): wipUnitName

## u_mes_perf_downtimeEvent - Downtime Events (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_downtimeEvent.json | _id: mes_perf_downtimeEventStable | rel: CL20261018-22:43 | samples: 10 | columns: 35 | total width: 5910px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | equipmentName | Equipment | String | 31 | 240px | left |
| 3 | lineName | Line | String | 35 | 270px | left |
| 4 | workCenterName | Work Center | String | 33 | 260px | left |
| 5 | shiftName | Shift | String | 7 | 80px | left |
| 6 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 7 | productionOrderName | Production Order | String | 10 | 160px | left |
| 8 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 9 | endedAt | Ended At | Date/Datetime | 19 | 160px | center |
| 10 | durationMinutes | Duration (min) | Int32 | 3 | 140px | right |
| 11 | downtimeType | Downtime Type | String | 9 | 140px | left |
| 12 | faultCode | Fault Code | String | 5 | 110px | left |
| 13 | faultText | Fault Text | String | 46 | 300px | left |
| 14 | reasonCodeName | Reason Code | String | 27 | 210px | left |
| 15 | reasonPathText | Reason Path Text | String | 48 | 300px | left |
| 16 | actionText | Action Text | String | 69 | 300px | left |
| 17 | isPlanned | Planned | Boolean | 3 | 90px | center |
| 18 | isMicroStop | Micro Stop | Boolean | 3 | 110px | center |
| 19 | alarmName | Alarm | String | 15 | 130px | left |
| 20 | maintenanceWorkOrderName | Maintenance Work Order | String | 50 | 300px | left |
| 21 | reportedBy | Reported By | String | 14 | 120px | left |
| 22 | classifiedBy | Classified By | String | 12 | 140px | left |
| 23 | classifiedAt | Classified At | Date/Datetime | 19 | 160px | center |
| 24 | responseMinutes | Response (min) | Int32 | 1 | 140px | right |
| 25 | repairMinutes | Repair (min) | Int32 | 3 | 130px | right |
| 26 | unitsLost | Units Lost | Int32 | 2 | 110px | right |
| 27 | captureSource | Capture Source | String | 16 | 140px | left |
| 28 | equipmentStateName | Equipment State | String | 15 | 150px | left |
| 29 | productVariantName | Product Variant | String | 26 | 210px | left |
| 30 | capaName | CAPA | String | 29 | 230px | left |
| 31 | status | Status | String | 10 | 90px | left |
| 32 | createdBy | Created By | String | 14 | 120px | left |
| 33 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 34 | updatedBy | Updated By | String | 14 | 120px | left |
| 35 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); lineId (reference key, shown through lineName); workCenterId (reference key, shown through workCenterName); shiftId (reference key, shown through shiftName); productionOrderId (reference key, shown through productionOrderName); reasonCodeId (reference key, shown through reasonCodeName); alarmId (reference key, shown through alarmName); maintenanceWorkOrderId (reference key, shown through maintenanceWorkOrderName); reportedById (reference key, shown through reportedBy); classifiedById (reference key, shown through classifiedBy); equipmentStateId (reference key, shown through equipmentStateName); productVariantId (reference key, shown through productVariantName); capaId (reference key, shown through capaName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_perf_workCenterPerformance - Station Performance (Reports)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_workCenterPerformance.json | _id: mes_perf_workCenterPerformanceStable | rel: CL20261018-22:43 | samples: 10 | columns: 24 | total width: 3750px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 21 | 170px | left |
| 2 | workCenterName | Work Center | String | 33 | 260px | left |
| 3 | lineName | Line | String | 35 | 270px | left |
| 4 | shiftName | Shift | String | 7 | 80px | left |
| 5 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 6 | periodStartAt | Period Start At | Date/Datetime | 19 | 160px | center |
| 7 | periodEndAt | Period End At | Date/Datetime | 19 | 160px | center |
| 8 | productVariantName | Product Variant | String | 26 | 210px | left |
| 9 | unitsCompleted | Units Completed | Int32 | 3 | 150px | right |
| 10 | throughputPerHour | Throughput per Hour | Decimal128 | 3 | 180px | right |
| 11 | averageCycleTimeSec | Average Cycle Time (s) | Decimal128 | 4 | 200px | right |
| 12 | taktTimeSec | Takt Time (s) | Decimal128 | 4 | 140px | right |
| 13 | taktBreachCount | Takt Breach Count | Int32 | 2 | 160px | right |
| 14 | wipQuantity | WIP Quantity | Int32 | 2 | 130px | right |
| 15 | blockedMinutes | Blocked (min) | Decimal128 | 4 | 140px | right |
| 16 | starvedMinutes | Starved (min) | Decimal128 | 3 | 140px | right |
| 17 | isConstraint | Constraint | Boolean | 3 | 110px | center |
| 18 | rankInLine | Rank in Line | Int32 | 1 | 130px | right |
| 19 | calculatedAt | Calculated At | Date/Datetime | 19 | 160px | center |
| 20 | status | Status | String | 10 | 90px | left |
| 21 | createdBy | Created By | String | 14 | 120px | left |
| 22 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 23 | updatedBy | Updated By | String | 14 | 120px | left |
| 24 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCenterId (reference key, shown through workCenterName); lineId (reference key, shown through lineName); shiftId (reference key, shown through shiftName); productVariantId (reference key, shown through productVariantName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))
