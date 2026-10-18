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

## u_mes_perf_alarmDefinition - Alarm Definitions (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_alarmDefinition.json | _id: mes_perf_alarmDefinitionStable | rel: CL20261018-23:51 | samples: 10 | columns: 13 | total width: 2330px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | equipmentTypeName | Equipment Type | String | 27 | 210px | left |
| 3 | alarmCode | Alarm Code | String | 5 | 110px | left |
| 4 | alarmText | Alarm Text | String | 56 | 300px | left |
| 5 | alarmClass | Alarm Class | String | 7 | 120px | left |
| 6 | severityClass | Severity Class | String | 8 | 140px | left |
| 7 | blocksRestart | Blocks Restart | Boolean | 3 | 140px | center |
| 8 | authorizingRoleName | Authorizing Role | String | 21 | 170px | left |
| 9 | defaultReasonCodeName | Default Reason Code | String | 27 | 210px | left |
| 10 | escalationRuleName | Escalation Rule | String | 34 | 260px | left |
| 11 | createsDowntime | Creates Downtime | Boolean | 3 | 160px | center |
| 12 | responseInstruction | Response Instruction | String | 100 | 300px | left |
| 13 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentTypeId (reference key, shown through equipmentTypeName); authorizingRoleId (reference key, shown through authorizingRoleName); defaultReasonCodeId (reference key, shown through defaultReasonCodeName); escalationRuleId (reference key, shown through escalationRuleName); schemaVersion (excluded key (identifier, site, app or schema))

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

## u_mes_perf_downtimeEventComment - Downtime Event Comments (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_downtimeEventComment.json | _id: mes_perf_downtimeEventCommentStable | rel: CL20261018-23:51 | samples: 10 | columns: 10 | total width: 1510px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | downtimeEventName | Downtime Event | String | 14 | 140px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | commentedAt | Commented At | Date/Datetime | 19 | 160px | center |
| 5 | authorUserName | Author User | String | 14 | 120px | left |
| 6 | commentText | Comment Text | String | 33 | 260px | left |
| 7 | createdBy | Created By | String | 14 | 120px | left |
| 8 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 9 | updatedBy | Updated By | String | 14 | 120px | left |
| 10 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); downtimeEventId (reference key, shown through downtimeEventName); authorUserId (reference key, shown through authorUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_perf_energyReading - Energy Readings (Telemetry)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_energyReading.json | _id: mes_perf_energyReadingStable | rel: CL20261018-23:51 | samples: 10 | columns: 22 | total width: 3400px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | meterIotDeviceName | Meter IoT Device | String | 36 | 280px | left |
| 3 | equipmentName | Equipment | String | 31 | 240px | left |
| 4 | lineName | Line | String | 35 | 270px | left |
| 5 | shiftName | Shift | String | 7 | 80px | left |
| 6 | energyTypeName | Energy Type | String | 11 | 120px | left |
| 7 | intervalStartAt | Interval Start At | Date/Datetime | 19 | 160px | center |
| 8 | intervalEndAt | Interval End At | Date/Datetime | 19 | 160px | center |
| 9 | consumption | Consumption | Decimal128 | 4 | 120px | right |
| 10 | unitOfMeasureName | Unit of Measure | String | 13 | 150px | left |
| 11 | meterReadingStart | Meter Reading Start | Decimal128 | 8 | 180px | right |
| 12 | meterReadingEnd | Meter Reading End | Decimal128 | 8 | 160px | right |
| 13 | demandKw | Demand Kw | Decimal128 | 4 | 110px | right |
| 14 | powerFactor | Power Factor | Double | 4 | 130px | right |
| 15 | costInr | Cost (INR) | Decimal128 | 7 | 110px | right |
| 16 | unitsProduced | Units Produced | Int32 | 3 | 140px | right |
| 17 | specificConsumption | Specific Consumption | Decimal128 | 6 | 180px | right |
| 18 | signalQuality | Signal Quality | String | 9 | 140px | left |
| 19 | createdBy | Created By | String | 10 | 110px | left |
| 20 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 21 | updatedBy | Updated By | String | 10 | 110px | left |
| 22 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); meterIotDeviceId (reference key, shown through meterIotDeviceName); equipmentId (reference key, shown through equipmentName); lineId (reference key, shown through lineName); shiftId (reference key, shown through shiftName); energyTypeId (reference key, shown through energyTypeName); unitOfMeasureId (reference key, shown through unitOfMeasureName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_perf_energyType - Energy Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_energyType.json | _id: mes_perf_energyTypeStable | rel: CL20261018-23:51 | samples: 10 | columns: 6 | total width: 860px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 8 | 110px | left |
| 2 | name | Name | String | 20 | 160px | left |
| 3 | description | Description | String | 30 | 230px | left |
| 4 | unitOfMeasureName | Unit of Measure | String | 4 | 150px | left |
| 5 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 6 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); unitOfMeasureId (reference key, shown through unitOfMeasureName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_perf_equipmentState - Equipment States (Telemetry)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_equipmentState.json | _id: mes_perf_equipmentStateStable | rel: CL20261018-23:51 | samples: 10 | columns: 19 | total width: 2740px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | equipmentName | Equipment | String | 31 | 240px | left |
| 3 | workCenterName | Work Center | String | 33 | 260px | left |
| 4 | stateCode | State Code | String | 7 | 110px | left |
| 5 | subStateCode | Sub State Code | String | 10 | 140px | left |
| 6 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 7 | endedAt | Ended At | Date/Datetime | 19 | 160px | center |
| 8 | durationSec | Duration (s) | Int32 | 4 | 130px | right |
| 9 | productionOrderName | Production Order | String | 10 | 160px | left |
| 10 | shiftName | Shift | String | 7 | 80px | left |
| 11 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 12 | source | Source | String | 12 | 110px | left |
| 13 | plcStateCode | PLC State Code | String | 1 | 140px | left |
| 14 | downtimeEventName | Downtime Event | String | 14 | 140px | left |
| 15 | status | Status | String | 6 | 90px | left |
| 16 | createdBy | Created By | String | 10 | 110px | left |
| 17 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 18 | updatedBy | Updated By | String | 10 | 110px | left |
| 19 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); workCenterId (reference key, shown through workCenterName); productionOrderId (reference key, shown through productionOrderName); shiftId (reference key, shown through shiftName); downtimeEventId (reference key, shown through downtimeEventName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_perf_leakTestResult - Leak Test Results (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_leakTestResult.json | _id: mes_perf_leakTestResultStable | rel: CL20261018-23:51 | samples: 20 | columns: 23 | total width: 4040px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | wipUnitName | WIP Unit | String | 20 | 160px | left |
| 3 | operationExecutionName | Operation Execution | String | 15 | 180px | left |
| 4 | equipmentName | Equipment | String | 31 | 240px | left |
| 5 | recipeName | Recipe | String | 56 | 300px | left |
| 6 | testerIotDeviceName | Tester IoT Device | String | 34 | 260px | left |
| 7 | operatorUserName | Operator User | String | 14 | 140px | left |
| 8 | programNo | Program No | String | 12 | 110px | left |
| 9 | testMedium | Test Medium | String | 7 | 120px | left |
| 10 | attemptNo | Attempt No | Int32 | 1 | 110px | right |
| 11 | ambientTemperatureC | Ambient Temperature C | Decimal128 | 4 | 190px | right |
| 12 | partTemperatureC | Part Temperature C | Decimal128 | 4 | 170px | right |
| 13 | fixtureToolName | Fixture Tool | String | 46 | 300px | left |
| 14 | masterLeakVerifiedAt | Master Leak Verified At | Date/Datetime | 19 | 210px | center |
| 15 | verdict | Verdict | String | 4 | 90px | left |
| 16 | failureReason | Failure Reason | String | 91 | 300px | left |
| 17 | testedAt | Tested At | Date/Datetime | 19 | 160px | center |
| 18 | measurementCurveName | Measurement Curve | String | 18 | 160px | left |
| 19 | status | Status | String | 8 | 90px | left |
| 20 | createdBy | Created By | String | 18 | 150px | left |
| 21 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 22 | updatedBy | Updated By | String | 18 | 150px | left |
| 23 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); wipUnitId (reference key, shown through wipUnitName); operationExecutionId (reference key, shown through operationExecutionName); equipmentId (reference key, shown through equipmentName); recipeId (reference key, shown through recipeName); testerIotDeviceId (reference key, shown through testerIotDeviceName); operatorUserId (reference key, shown through operatorUserName); fixtureToolId (reference key, shown through fixtureToolName); measurementCurveId (reference key, shown through measurementCurveName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_perf_leakTestResultStage - Leak Test Result Stages (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_leakTestResultStage.json | _id: mes_perf_leakTestResultStageStable | rel: CL20261018-23:51 | samples: 20 | columns: 17 | total width: 2580px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | leakTestResultName | Leak Test Result | String | 15 | 160px | left |
| 3 | stageNo | Stage No | Int32 | 1 | 100px | right |
| 4 | stageName | Stage Name | String | 13 | 120px | left |
| 5 | testPressureBar | Test Pressure Bar | Decimal128 | 5 | 160px | right |
| 6 | fillTimeSec | Fill Time (s) | Decimal128 | 3 | 140px | right |
| 7 | stabiliseTimeSec | Stabilise Time (s) | Decimal128 | 3 | 170px | right |
| 8 | testTimeSec | Test Time (s) | Decimal128 | 4 | 140px | right |
| 9 | pressureDropPa | Pressure Drop Pa | Decimal128 | 5 | 160px | right |
| 10 | leakRateSccm | Leak Rate Sccm | Decimal128 | 5 | 140px | right |
| 11 | limitPressureDropPa | Limit Pressure Drop Pa | Decimal128 | 5 | 200px | right |
| 12 | limitLeakRateSccm | Limit Leak Rate Sccm | Decimal128 | 5 | 180px | right |
| 13 | stageResult | Stage Result | String | 4 | 130px | left |
| 14 | createdBy | Created By | String | 18 | 150px | left |
| 15 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 16 | updatedBy | Updated By | String | 18 | 150px | left |
| 17 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); leakTestResultId (reference key, shown through leakTestResultName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_perf_lossCategory - Loss Categories (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_lossCategory.json | _id: mes_perf_lossCategoryStable | rel: CL20261018-23:51 | samples: 20 | columns: 7 | total width: 1090px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | name | Name | String | 27 | 210px | left |
| 3 | description | Description | String | 38 | 290px | left |
| 4 | oeeImpact | OEE Impact | String | 12 | 110px | left |
| 5 | sixBigLossNo | Six Big Loss No | Int32 | 1 | 150px | right |
| 6 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 7 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_perf_lossSummary - Loss Summary (Reports)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_lossSummary.json | _id: mes_perf_lossSummaryStable | rel: CL20261018-23:51 | samples: 10 | columns: 22 | total width: 3490px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 33 | 260px | left |
| 2 | lineName | Line | String | 35 | 270px | left |
| 3 | workCenterName | Work Center | String | 33 | 260px | left |
| 4 | shiftName | Shift | String | 7 | 80px | left |
| 5 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 6 | lossCategoryName | Loss Category | String | 17 | 140px | left |
| 7 | reasonCodeName | Reason Code | String | 27 | 210px | left |
| 8 | isPlanned | Planned | Boolean | 3 | 90px | center |
| 9 | occurrenceCount | Occurrence Count | Int32 | 1 | 160px | right |
| 10 | lossMinutes | Loss (min) | Int32 | 3 | 110px | right |
| 11 | lossUnits | Loss Units | Int32 | 3 | 110px | right |
| 12 | lossPctOfPlannedTime | Loss Pct of Planned Time | Decimal128 | 4 | 210px | right |
| 13 | paretoRank | Pareto Rank | Int32 | 1 | 120px | right |
| 14 | cumulativePct | Cumulative (%) | Decimal128 | 5 | 140px | right |
| 15 | maintenanceWorkOrderCount | Maintenance Work Order Count | Int32 | 1 | 240px | right |
| 16 | capaCount | CAPA Count | Int32 | 1 | 110px | right |
| 17 | calculatedAt | Calculated At | Date/Datetime | 19 | 160px | center |
| 18 | status | Status | String | 12 | 110px | left |
| 19 | createdBy | Created By | String | 14 | 120px | left |
| 20 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 21 | updatedBy | Updated By | String | 14 | 120px | left |
| 22 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); lineId (reference key, shown through lineName); workCenterId (reference key, shown through workCenterName); shiftId (reference key, shown through shiftName); lossCategoryId (reference key, shown through lossCategoryName); reasonCodeId (reference key, shown through reasonCodeName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_perf_oeeRecord - OEE Records (Reports)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_oeeRecord.json | _id: mes_perf_oeeRecordStable | rel: CL20261018-23:51 | samples: 10 | columns: 31 | total width: 4800px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | equipmentName | Equipment | String | 31 | 240px | left |
| 3 | lineName | Line | String | 35 | 270px | left |
| 4 | shiftName | Shift | String | 7 | 80px | left |
| 5 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 6 | itemName | Item | String | 39 | 300px | left |
| 7 | productionOrderName | Production Order | String | 10 | 160px | left |
| 8 | periodStartAt | Period Start At | Date/Datetime | 19 | 160px | center |
| 9 | periodEndAt | Period End At | Date/Datetime | 19 | 160px | center |
| 10 | calendarMinutes | Calendar (min) | Int32 | 3 | 140px | right |
| 11 | plannedProductionMinutes | Planned Production (min) | Int32 | 3 | 210px | right |
| 12 | plannedDowntimeMinutes | Planned Downtime (min) | Int32 | 2 | 200px | right |
| 13 | unplannedDowntimeMinutes | Unplanned Downtime (min) | Int32 | 2 | 210px | right |
| 14 | runMinutes | Run (min) | Int32 | 3 | 110px | right |
| 15 | idealCycleTimeSec | Ideal Cycle Time (s) | Decimal128 | 7 | 180px | right |
| 16 | totalCount | Total Count | Int32 | 4 | 120px | right |
| 17 | goodCount | Good Count | Int32 | 4 | 110px | right |
| 18 | rejectCount | Reject Count | Int32 | 1 | 130px | right |
| 19 | reworkCount | Rework Count | Int32 | 1 | 130px | right |
| 20 | availabilityPct | Availability (%) | Decimal128 | 4 | 160px | right |
| 21 | performancePct | Performance (%) | Decimal128 | 4 | 150px | right |
| 22 | qualityPct | Quality (%) | Decimal128 | 5 | 120px | right |
| 23 | oeePct | OEE (%) | Decimal128 | 4 | 90px | right |
| 24 | teepPct | Teep (%) | Decimal128 | 4 | 100px | right |
| 25 | calculatedAt | Calculated At | Date/Datetime | 19 | 160px | center |
| 26 | calculationVersion | Calculation Version | Int32 | 1 | 180px | right |
| 27 | status | Status | String | 12 | 110px | left |
| 28 | createdBy | Created By | String | 10 | 110px | left |
| 29 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 30 | updatedBy | Updated By | String | 10 | 110px | left |
| 31 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); lineId (reference key, shown through lineName); shiftId (reference key, shown through shiftName); itemId (reference key, shown through itemName); productionOrderId (reference key, shown through productionOrderName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_perf_oeeRecordLoss - OEE Record Losses (Reports)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_oeeRecordLoss.json | _id: mes_perf_oeeRecordLossStable | rel: CL20261018-23:51 | samples: 10 | columns: 11 | total width: 1540px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | oeeRecordName | OEE Record | String | 15 | 130px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | lossCategoryName | Loss Category | String | 20 | 160px | left |
| 5 | reasonCodeName | Reason Code | String | 27 | 210px | left |
| 6 | lossMinutes | Loss (min) | Int32 | 2 | 110px | right |
| 7 | lossUnits | Loss Units | Int32 | 2 | 110px | right |
| 8 | createdBy | Created By | String | 10 | 110px | left |
| 9 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 10 | updatedBy | Updated By | String | 10 | 110px | left |
| 11 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); oeeRecordId (reference key, shown through oeeRecordName); lossCategoryId (reference key, shown through lossCategoryName); reasonCodeId (reference key, shown through reasonCodeName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_perf_operatorPerformance - Operator Performance (Reports)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_operatorPerformance.json | _id: mes_perf_operatorPerformanceStable | rel: CL20261018-23:51 | samples: 10 | columns: 19 | total width: 2820px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 25 | 200px | left |
| 2 | userName | User | String | 14 | 120px | left |
| 3 | workCenterName | Work Center | String | 33 | 260px | left |
| 4 | productVariantName | Product Variant | String | 26 | 210px | left |
| 5 | shiftName | Shift | String | 7 | 80px | left |
| 6 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 7 | attendedMinutes | Attended (min) | Decimal128 | 3 | 140px | right |
| 8 | earnedMinutes | Earned (min) | Decimal128 | 3 | 130px | right |
| 9 | efficiencyPct | Efficiency (%) | Decimal128 | 4 | 140px | right |
| 10 | goodQuantity | Good Quantity | Int32 | 4 | 140px | right |
| 11 | rejectQuantity | Reject Quantity | Int32 | 1 | 150px | right |
| 12 | errorCount | Error Count | Int32 | 1 | 120px | right |
| 13 | interlockCount | Interlock Count | Int32 | 1 | 150px | right |
| 14 | calculatedAt | Calculated At | Date/Datetime | 19 | 160px | center |
| 15 | status | Status | String | 12 | 110px | left |
| 16 | createdBy | Created By | String | 14 | 120px | left |
| 17 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 18 | updatedBy | Updated By | String | 14 | 120px | left |
| 19 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); userId (reference key, shown through userName); workCenterId (reference key, shown through workCenterName); productVariantId (reference key, shown through productVariantName); shiftId (reference key, shown through shiftName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_perf_processReading - Process Readings (Telemetry)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_processReading.json | _id: mes_perf_processReadingStable | rel: CL20261018-23:51 | samples: 20 | columns: 17 | total width: 2700px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | processTagName | Process Tag | String | 46 | 300px | left |
| 3 | equipmentName | Equipment | String | 54 | 300px | left |
| 4 | timestamp | Timestamp | Date/Datetime | 19 | 160px | center |
| 5 | tagValue | Tag Value | Double | 6 | 110px | right |
| 6 | tagValueText | Tag Value Text | String | 0 | 140px | left |
| 7 | signalQuality | Signal Quality | String | 9 | 140px | left |
| 8 | productionOrderName | Production Order | String | 10 | 160px | left |
| 9 | lotName | Lot | String | 15 | 130px | left |
| 10 | inLimits | In Limits | Boolean | 3 | 110px | center |
| 11 | areaName | Area | String | 22 | 180px | left |
| 12 | shiftName | Shift | String | 7 | 80px | left |
| 13 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 14 | createdBy | Created By | String | 18 | 150px | left |
| 15 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 16 | updatedBy | Updated By | String | 18 | 150px | left |
| 17 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); processTagId (reference key, shown through processTagName); equipmentId (reference key, shown through equipmentName); productionOrderId (reference key, shown through productionOrderName); lotId (reference key, shown through lotName); areaId (reference key, shown through areaName); shiftId (reference key, shown through shiftName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): tagValueText

## u_mes_perf_processTag - Process Tags (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_processTag.json | _id: mes_perf_processTagStable | rel: CL20261018-23:51 | samples: 20 | columns: 24 | total width: 4150px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 26 | 210px | left |
| 2 | description | Description | String | 46 | 300px | left |
| 3 | equipmentName | Equipment | String | 54 | 300px | left |
| 4 | iotDeviceName | IoT Device | String | 47 | 300px | left |
| 5 | sourceAddress | Source Address | String | 34 | 260px | left |
| 6 | dataType | Data Type | String | 8 | 110px | left |
| 7 | unitOfMeasureName | Unit of Measure | String | 14 | 150px | left |
| 8 | tagClass | Tag Class | String | 13 | 120px | left |
| 9 | scanRateMs | Scan Rate Ms | Int32 | 4 | 130px | right |
| 10 | deadband | Deadband | Decimal128 | 3 | 100px | right |
| 11 | lowLimit | Low Limit | Decimal128 | 7 | 110px | right |
| 12 | highLimit | High Limit | Decimal128 | 7 | 110px | right |
| 13 | lowLowLimit | Low Low Limit | Decimal128 | 7 | 140px | right |
| 14 | highHighLimit | High High Limit | Decimal128 | 7 | 150px | right |
| 15 | engineeringMin | Engineering Min | Decimal128 | 3 | 150px | right |
| 16 | engineeringMax | Engineering Max | Decimal128 | 7 | 150px | right |
| 17 | isCritical | Critical | Boolean | 3 | 100px | center |
| 18 | historise | Historise | Boolean | 3 | 110px | center |
| 19 | retentionDays | Retention (days) | Int32 | 3 | 160px | right |
| 20 | aggregation | Aggregation | String | 4 | 120px | left |
| 21 | areaName | Area | String | 29 | 230px | left |
| 22 | lineName | Line | String | 35 | 270px | left |
| 23 | workCenterName | Work Center | String | 37 | 280px | left |
| 24 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); iotDeviceId (reference key, shown through iotDeviceName); unitOfMeasureId (reference key, shown through unitOfMeasureName); areaId (reference key, shown through areaName); lineId (reference key, shown through lineName); workCenterId (reference key, shown through workCenterName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_perf_productionCount - Hourly Production Counts (Reports)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_productionCount.json | _id: mes_perf_productionCountStable | rel: CL20261018-23:51 | samples: 10 | columns: 23 | total width: 3700px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | workCenterName | Work Center | String | 33 | 260px | left |
| 3 | lineName | Line | String | 35 | 270px | left |
| 4 | shiftName | Shift | String | 7 | 80px | left |
| 5 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 6 | hourStartAt | Hour Start At | Date/Datetime | 19 | 160px | center |
| 7 | hourEndAt | Hour End At | Date/Datetime | 19 | 160px | center |
| 8 | productionOrderName | Production Order | String | 10 | 160px | left |
| 9 | itemName | Item | String | 39 | 300px | left |
| 10 | targetQuantity | Target Quantity | Int32 | 3 | 150px | right |
| 11 | goodQuantity | Good Quantity | Int32 | 3 | 140px | right |
| 12 | rejectQuantity | Reject Quantity | Int32 | 1 | 150px | right |
| 13 | reworkQuantity | Rework Quantity | Int32 | 1 | 150px | right |
| 14 | cumulativeTarget | Cumulative Target | Int32 | 3 | 160px | right |
| 15 | cumulativeGood | Cumulative Good | Int32 | 3 | 150px | right |
| 16 | downtimeMinutes | Downtime (min) | Int32 | 2 | 140px | right |
| 17 | source | Source | String | 12 | 110px | left |
| 18 | gapReason | Gap Reason | String | 34 | 260px | left |
| 19 | status | Status | String | 6 | 90px | left |
| 20 | createdBy | Created By | String | 10 | 110px | left |
| 21 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 22 | updatedBy | Updated By | String | 10 | 110px | left |
| 23 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCenterId (reference key, shown through workCenterName); lineId (reference key, shown through lineName); shiftId (reference key, shown through shiftName); productionOrderId (reference key, shown through productionOrderName); itemId (reference key, shown through itemName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_perf_reasonCategory - Reason Categories (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_reasonCategory.json | _id: mes_perf_reasonCategoryStable | rel: CL20261018-23:51 | samples: 20 | columns: 5 | total width: 740px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 4 | 110px | left |
| 2 | name | Name | String | 24 | 190px | left |
| 3 | description | Description | String | 30 | 230px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_perf_reasonCode - Reason Codes (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_reasonCode.json | _id: mes_perf_reasonCodeStable | rel: CL20261018-23:51 | samples: 20 | columns: 15 | total width: 2420px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 11 | 110px | left |
| 2 | name | Name | String | 27 | 210px | left |
| 3 | reasonType | Reason Type | String | 8 | 120px | left |
| 4 | level | Level | Int32 | 1 | 80px | right |
| 5 | parentReasonCodeName | Parent Reason Code | String | 0 | 170px | left |
| 6 | pathText | Path Text | String | 58 | 300px | left |
| 7 | reasonCategoryName | Reason Category | String | 24 | 190px | left |
| 8 | lossCategoryName | Loss Category | String | 27 | 210px | left |
| 9 | oeeImpact | OEE Impact | String | 12 | 110px | left |
| 10 | isPlanned | Planned | Boolean | 3 | 90px | center |
| 11 | responsibleDepartmentName | Responsible Department | String | 10 | 200px | left |
| 12 | requiresComment | Requires Comment | Boolean | 3 | 160px | center |
| 13 | requiresMaintenanceWorkOrder | Requires Maintenance Work Order | Boolean | 3 | 260px | center |
| 14 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 15 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); parentReasonCodeId (reference key, shown through parentReasonCodeName); reasonCategoryId (reference key, shown through reasonCategoryName); lossCategoryId (reference key, shown through lossCategoryName); responsibleDepartmentId (reference key, shown through responsibleDepartmentName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): parentReasonCodeName

## u_mes_perf_torqueResult - Torque Results (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_perf_torqueResult.json | _id: mes_perf_torqueResultStable | rel: CL20261018-23:51 | samples: 20 | columns: 35 | total width: 6120px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | wipUnitName | WIP Unit | String | 20 | 160px | left |
| 3 | operationExecutionName | Operation Execution | String | 15 | 180px | left |
| 4 | equipmentName | Equipment | String | 33 | 260px | left |
| 5 | toolName | Tool | String | 33 | 260px | left |
| 6 | recipeName | Recipe | String | 50 | 300px | left |
| 7 | controllerIotDeviceName | Controller IoT Device | String | 38 | 290px | left |
| 8 | operatorUserName | Operator User | String | 14 | 140px | left |
| 9 | jointName | Joint Name | String | 31 | 240px | left |
| 10 | programNo | Program No | String | 9 | 110px | left |
| 11 | tighteningNo | Tightening No | Int32 | 1 | 140px | right |
| 12 | attemptNo | Attempt No | Int32 | 1 | 110px | right |
| 13 | targetTorqueNm | Target Torque Nm | Decimal128 | 4 | 160px | right |
| 14 | minTorqueNm | Min Torque Nm | Decimal128 | 4 | 140px | right |
| 15 | maxTorqueNm | Max Torque Nm | Decimal128 | 4 | 140px | right |
| 16 | finalTorqueNm | Final Torque Nm | Decimal128 | 4 | 150px | right |
| 17 | targetAngleDeg | Target Angle Deg | Decimal128 | 5 | 160px | right |
| 18 | minAngleDeg | Min Angle Deg | Decimal128 | 5 | 140px | right |
| 19 | maxAngleDeg | Max Angle Deg | Decimal128 | 5 | 140px | right |
| 20 | finalAngleDeg | Final Angle Deg | Decimal128 | 5 | 150px | right |
| 21 | rundownTimeMs | Rundown Time Ms | Int32 | 4 | 150px | right |
| 22 | strategy | Strategy | String | 14 | 120px | left |
| 23 | result | Result | String | 6 | 90px | left |
| 24 | failureReason | Failure Reason | String | 59 | 300px | left |
| 25 | curveControlledDocumentName | Curve Controlled Document | String | 44 | 300px | left |
| 26 | tightenedAt | Tightened At | Date/Datetime | 19 | 160px | center |
| 27 | controllerResultNo | Controller Result No | String | 13 | 180px | left |
| 28 | curveEnvelopeName | Curve Envelope | String | 67 | 300px | left |
| 29 | measurementCurveName | Measurement Curve | String | 18 | 160px | left |
| 30 | envelopeResult | Envelope Result | String | 3 | 150px | left |
| 31 | status | Status | String | 8 | 90px | left |
| 32 | createdBy | Created By | String | 18 | 150px | left |
| 33 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 34 | updatedBy | Updated By | String | 18 | 150px | left |
| 35 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); wipUnitId (reference key, shown through wipUnitName); operationExecutionId (reference key, shown through operationExecutionName); equipmentId (reference key, shown through equipmentName); toolId (reference key, shown through toolName); recipeId (reference key, shown through recipeName); controllerIotDeviceId (reference key, shown through controllerIotDeviceName); operatorUserId (reference key, shown through operatorUserName); curveControlledDocumentId (reference key, shown through curveControlledDocumentName); curveEnvelopeId (reference key, shown through curveEnvelopeName); measurementCurveId (reference key, shown through measurementCurveName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

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
