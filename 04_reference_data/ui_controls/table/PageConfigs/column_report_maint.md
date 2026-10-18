## u_mes_maint_cleaningRecord - Cleaning Records (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_cleaningRecord.json | _id: mes_maint_cleaningRecordStable | rel: CL20261018-22:43 | samples: 10 | columns: 22 | total width: 4040px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | equipmentName | Equipment | String | 54 | 300px | left |
| 3 | workCenterName | Work Center | String | 37 | 280px | left |
| 4 | cleaningType | Cleaning Type | String | 27 | 210px | left |
| 5 | procedureControlledDocumentName | Procedure Controlled Document | String | 61 | 300px | left |
| 6 | previousProductionOrderName | Previous Production Order | String | 10 | 220px | left |
| 7 | previousItemName | Previous Item | String | 61 | 300px | left |
| 8 | dirtyHoldStartAt | Dirty Hold Start At | Date/Datetime | 19 | 180px | center |
| 9 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 10 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 11 | cleanedBy | Cleaned By | String | 14 | 120px | left |
| 12 | verificationMethod | Verification Method | String | 17 | 180px | left |
| 13 | verificationResult | Verification Result | String | 4 | 180px | left |
| 14 | verifiedBy | Verified By | String | 13 | 120px | left |
| 15 | verifiedAt | Verified At | Date/Datetime | 19 | 160px | center |
| 16 | cleanHoldExpiresAt | Clean Hold Expires At | Date/Datetime | 19 | 190px | center |
| 17 | electronicSignatureName | Electronic Signature | String | 0 | 180px | left |
| 18 | status | Status | String | 11 | 100px | left |
| 19 | createdBy | Created By | String | 14 | 120px | left |
| 20 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 21 | updatedBy | Updated By | String | 14 | 120px | left |
| 22 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); workCenterId (reference key, shown through workCenterName); procedureControlledDocumentId (reference key, shown through procedureControlledDocumentName); previousProductionOrderId (reference key, shown through previousProductionOrderName); previousItemId (reference key, shown through previousItemName); cleanedById (reference key, shown through cleanedBy); verifiedById (reference key, shown through verifiedBy); electronicSignatureId (reference key, shown through electronicSignatureName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): electronicSignatureName

## u_mes_maint_equipmentLifecycleEvent - Equipment Lifecycle (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_equipmentLifecycleEvent.json | _id: mes_maint_equipmentLifecycleEventStable | rel: CL20261018-22:43 | samples: 10 | columns: 19 | total width: 3410px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | equipmentName | Equipment | String | 31 | 240px | left |
| 3 | eventType | Event Type | String | 26 | 210px | left |
| 4 | eventAt | Event At | Date/Datetime | 19 | 160px | center |
| 5 | description | Description | String | 63 | 300px | left |
| 6 | costInr | Cost (INR) | Decimal128 | 9 | 110px | right |
| 7 | healthScore | Health Score | Decimal128 | 2 | 130px | right |
| 8 | lifetimeCyclesAtEvent | Lifetime Cycles At Event | Int64 | 7 | 210px | right |
| 9 | lifetimeRunHoursAtEvent | Lifetime Run Hours At Event | Decimal128 | 7 | 230px | right |
| 10 | maintenanceWorkOrderName | Maintenance Work Order | String | 45 | 300px | left |
| 11 | engineeringChangeName | Engineering Change | String | 47 | 300px | left |
| 12 | modelPredictionName | Model Prediction | String | 18 | 160px | left |
| 13 | approvedBy | Approved By | String | 15 | 130px | left |
| 14 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 15 | status | Status | String | 8 | 90px | left |
| 16 | createdBy | Created By | String | 12 | 110px | left |
| 17 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 18 | updatedBy | Updated By | String | 12 | 110px | left |
| 19 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); maintenanceWorkOrderId (reference key, shown through maintenanceWorkOrderName); engineeringChangeId (reference key, shown through engineeringChangeName); modelPredictionId (reference key, shown through modelPredictionName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_maint_equipmentQualification - Equipment Qualifications (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_equipmentQualification.json | _id: mes_maint_equipmentQualificationStable | rel: CL20261018-22:43 | samples: 10 | columns: 21 | total width: 3690px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | equipmentName | Equipment | String | 36 | 280px | left |
| 3 | qualificationPhase | Qualification Phase | String | 26 | 210px | left |
| 4 | engineeringChangeName | Engineering Change | String | 47 | 300px | left |
| 5 | protocolControlledDocumentName | Protocol Controlled Document | String | 0 | 240px | left |
| 6 | reportControlledDocumentName | Report Controlled Document | String | 0 | 230px | left |
| 7 | testCaseCount | Test Case Count | Int32 | 2 | 150px | right |
| 8 | testFailedCount | Test Failed Count | Int32 | 1 | 160px | right |
| 9 | openDeviationCount | Open Deviation Count | Int32 | 1 | 180px | right |
| 10 | executedBy | Executed By | String | 14 | 120px | left |
| 11 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 12 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 13 | approvedBy | Approved By | String | 11 | 120px | left |
| 14 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 15 | electronicSignatureName | Electronic Signature | String | 0 | 180px | left |
| 16 | requalificationDueDate | Requalification Due Date | Date/Date | 10 | 210px | center |
| 17 | status | Status | String | 12 | 110px | left |
| 18 | createdBy | Created By | String | 14 | 120px | left |
| 19 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 20 | updatedBy | Updated By | String | 14 | 120px | left |
| 21 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); engineeringChangeId (reference key, shown through engineeringChangeName); protocolControlledDocumentId (reference key, shown through protocolControlledDocumentName); reportControlledDocumentId (reference key, shown through reportControlledDocumentName); executedById (reference key, shown through executedBy); approvedById (reference key, shown through approvedBy); electronicSignatureId (reference key, shown through electronicSignatureName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): protocolControlledDocumentName, reportControlledDocumentName, electronicSignatureName

## u_mes_maint_logbookEntry - Equipment and Area Logbook (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_logbookEntry.json | _id: mes_maint_logbookEntryStable | rel: CL20261018-22:43 | samples: 10 | columns: 20 | total width: 3370px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | relatedCollectionName | Related Collection Name | String | 20 | 210px | left |
| 3 | relatedEntityName | Related Entity | String | 54 | 300px | left |
| 4 | activityType | Activity Type | String | 14 | 140px | left |
| 5 | productionOrderName | Production Order | String | 10 | 160px | left |
| 6 | lotName | Lot | String | 13 | 120px | left |
| 7 | cleaningRecordName | Cleaning Record | String | 16 | 150px | left |
| 8 | maintenanceWorkOrderName | Maintenance Work Order | String | 38 | 290px | left |
| 9 | lineClearanceName | Line Clearance | String | 16 | 140px | left |
| 10 | entryText | Entry Text | String | 90 | 300px | left |
| 11 | performedBy | Performed By | String | 18 | 150px | left |
| 12 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 13 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 14 | reviewedBy | Reviewed By | String | 13 | 120px | left |
| 15 | reviewedAt | Reviewed At | Date/Datetime | 19 | 160px | center |
| 16 | status | Status | String | 8 | 90px | left |
| 17 | createdBy | Created By | String | 14 | 120px | left |
| 18 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 19 | updatedBy | Updated By | String | 14 | 120px | left |
| 20 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); relatedEntityId (reference key, shown through relatedEntityName); productionOrderId (reference key, shown through productionOrderName); lotId (reference key, shown through lotName); cleaningRecordId (reference key, shown through cleaningRecordName); maintenanceWorkOrderId (reference key, shown through maintenanceWorkOrderName); lineClearanceId (reference key, shown through lineClearanceName); performedById (reference key, shown through performedBy); reviewedById (reference key, shown through reviewedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_maint_maintenancePlan - Maintenance Plans (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_maintenancePlan.json | _id: mes_maint_maintenancePlanStable | rel: CL20261018-22:43 | samples: 10 | columns: 17 | total width: 2780px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | name | Name | String | 55 | 300px | left |
| 3 | equipmentName | Equipment | String | 31 | 240px | left |
| 4 | toolName | Tool | String | 39 | 300px | left |
| 5 | planType | Plan Type | String | 10 | 110px | left |
| 6 | strategy | Strategy | String | 14 | 120px | left |
| 7 | intervalType | Interval Type | String | 8 | 140px | left |
| 8 | intervalValue | Interval Value | Decimal128 | 2 | 140px | right |
| 9 | intervalUom | Interval UoM | String | 4 | 130px | left |
| 10 | counterSource | Counter Source | String | 0 | 140px | left |
| 11 | estimatedMinutes | Estimated (min) | Int32 | 1 | 150px | right |
| 12 | lastDoneAt | Last Done At | Date/Datetime | 0 | 130px | center |
| 13 | nextDueAt | Next Due At | Date/Date | 10 | 120px | center |
| 14 | toleranceDays | Tolerance (days) | Int32 | 1 | 160px | right |
| 15 | blockEquipmentWhenOverdue | Block Equipment When Overdue | Boolean | 3 | 240px | center |
| 16 | ownerDepartmentName | Owner Department | String | 11 | 160px | left |
| 17 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); toolId (reference key, shown through toolName); ownerDepartmentId (reference key, shown through ownerDepartmentName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): counterSource, lastDoneAt

## u_mes_maint_maintenancePlanRequiredSkill - Maintenance Plan Required Skills (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_maintenancePlanRequiredSkill.json | _id: mes_maint_maintenancePlanRequiredSkillStable | rel: CL20261018-22:43 | samples: 10 | columns: 4 | total width: 810px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | maintenancePlanName | Maintenance Plan | String | 55 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | requiredSkillName | Required Skill | String | 32 | 250px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); maintenancePlanId (reference key, shown through maintenancePlanName); requiredSkillId (reference key, shown through requiredSkillName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_maint_maintenancePlanRequiredSparePart - Maintenance Plan Required Spare Parts (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_maintenancePlanRequiredSparePart.json | _id: mes_maint_maintenancePlanRequiredSparePartStable | rel: CL20261018-22:43 | samples: 10 | columns: 5 | total width: 970px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | maintenancePlanName | Maintenance Plan | String | 54 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | sparePartName | Spare Part | String | 55 | 300px | left |
| 5 | quantity | Quantity | Decimal128 | 1 | 100px | right |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); maintenancePlanId (reference key, shown through maintenancePlanName); sparePartId (reference key, shown through sparePartName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_maint_maintenancePlanTask - Maintenance Plan Tasks (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_maintenancePlanTask.json | _id: mes_maint_maintenancePlanTaskStable | rel: CL20261018-22:43 | samples: 10 | columns: 7 | total width: 1430px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | maintenancePlanName | Maintenance Plan | String | 54 | 300px | left |
| 3 | taskNo | Task No | Int32 | 2 | 90px | right |
| 4 | description | Description | String | 83 | 300px | left |
| 5 | standardMinutes | Standard (min) | Int32 | 2 | 140px | right |
| 6 | requiresShutdown | Requires Shutdown | Boolean | 3 | 160px | center |
| 7 | acceptanceCriteria | Acceptance Criteria | String | 61 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); maintenancePlanId (reference key, shown through maintenancePlanName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_maint_maintenanceWorkOrder - Maintenance Work Orders (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_maintenanceWorkOrder.json | _id: mes_maint_maintenanceWorkOrderStable | rel: CL20261018-22:43 | samples: 20 | columns: 39 | total width: 7260px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | title | Title | String | 63 | 300px | left |
| 3 | workOrderType | Work Order Type | String | 10 | 150px | left |
| 4 | equipmentName | Equipment | String | 54 | 300px | left |
| 5 | toolName | Tool | String | 46 | 300px | left |
| 6 | maintenancePlanName | Maintenance Plan | String | 55 | 300px | left |
| 7 | downtimeEventName | Downtime Event | String | 14 | 140px | left |
| 8 | priority | Priority | String | 6 | 100px | left |
| 9 | reportedBy | Reported By | String | 14 | 120px | left |
| 10 | reportedAt | Reported At | Date/Datetime | 19 | 160px | center |
| 11 | problemDescription | Problem Description | String | 75 | 300px | left |
| 12 | reasonCodeName | Reason Code | String | 27 | 210px | left |
| 13 | failureMode | Failure Mode | String | 40 | 300px | left |
| 14 | rootCause | Root Cause | String | 74 | 300px | left |
| 15 | actionTaken | Action Taken | String | 69 | 300px | left |
| 16 | plannedStartAt | Planned Start At | Date/Datetime | 19 | 160px | center |
| 17 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 18 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 19 | downtimeMinutes | Downtime (min) | Int32 | 3 | 140px | right |
| 20 | responseMinutes | Response (min) | Int32 | 1 | 140px | right |
| 21 | repairMinutes | Repair (min) | Int32 | 2 | 130px | right |
| 22 | totalCostInr | Total Cost (INR) | Decimal128 | 7 | 160px | right |
| 23 | equipmentReleasedBy | Equipment Released By | String | 15 | 190px | left |
| 24 | equipmentReleasedAt | Equipment Released At | Date/Datetime | 19 | 190px | center |
| 25 | followUpRequired | Follow Up Required | Boolean | 3 | 170px | center |
| 26 | shiftName | Shift | String | 7 | 80px | left |
| 27 | rootCauseCodeName | Root Cause Code | String | 27 | 210px | left |
| 28 | closureApprovedBy | Closure Approved By | String | 15 | 180px | left |
| 29 | closureApprovedAt | Closure Approved At | Date/Datetime | 19 | 180px | center |
| 30 | andonEventName | Andon Event | String | 60 | 300px | left |
| 31 | priorityScore | Priority Score | Decimal128 | 2 | 140px | right |
| 32 | schedulingSource | Scheduling Source | String | 6 | 160px | left |
| 33 | slaResponseDueAt | SLA Response Due At | Date/Datetime | 19 | 180px | center |
| 34 | slaRepairDueAt | SLA Repair Due At | Date/Datetime | 19 | 160px | center |
| 35 | status | Status | String | 11 | 100px | left |
| 36 | createdBy | Created By | String | 14 | 120px | left |
| 37 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 38 | updatedBy | Updated By | String | 14 | 120px | left |
| 39 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); toolId (reference key, shown through toolName); maintenancePlanId (reference key, shown through maintenancePlanName); downtimeEventId (reference key, shown through downtimeEventName); reportedById (reference key, shown through reportedBy); reasonCodeId (reference key, shown through reasonCodeName); equipmentReleasedById (reference key, shown through equipmentReleasedBy); shiftId (reference key, shown through shiftName); rootCauseCodeId (reference key, shown through rootCauseCodeName); closureApprovedById (reference key, shown through closureApprovedBy); andonEventId (reference key, shown through andonEventName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_maint_maintenanceWorkOrderAssignedToUser - Maintenance Work Order Assignees (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_maintenanceWorkOrderAssignedToUser.json | _id: mes_maint_maintenanceWorkOrderAssignedToUserStable | rel: CL20261018-22:43 | samples: 10 | columns: 8 | total width: 1290px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 21 | 170px | left |
| 2 | maintenanceWorkOrderName | Maintenance Work Order | String | 50 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | assignedToUserName | Assigned to User | String | 12 | 160px | left |
| 5 | createdBy | Created By | String | 12 | 110px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 12 | 110px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); maintenanceWorkOrderId (reference key, shown through maintenanceWorkOrderName); assignedToUserId (reference key, shown through assignedToUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_maint_maintenanceWorkOrderLabour - Maintenance Work Order Labour (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_maintenanceWorkOrderLabour.json | _id: mes_maint_maintenanceWorkOrderLabourStable | rel: CL20261018-22:43 | samples: 10 | columns: 9 | total width: 1360px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | maintenanceWorkOrderName | Maintenance Work Order | String | 50 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | userName | User | String | 12 | 110px | left |
| 5 | labourMinutes | Labour (min) | Int32 | 2 | 130px | right |
| 6 | createdBy | Created By | String | 12 | 110px | left |
| 7 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 8 | updatedBy | Updated By | String | 12 | 110px | left |
| 9 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); maintenanceWorkOrderId (reference key, shown through maintenanceWorkOrderName); userId (reference key, shown through userName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_maint_maintenanceWorkOrderTask - Work Order Checklist (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_maintenanceWorkOrderTask.json | _id: mes_maint_maintenanceWorkOrderTaskStable | rel: CL20261018-22:43 | samples: 10 | columns: 15 | total width: 2550px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | maintenanceWorkOrderName | Maintenance Work Order | String | 46 | 300px | left |
| 3 | taskNo | Task No | Int32 | 2 | 90px | right |
| 4 | maintenancePlanTaskName | Maintenance Plan Task | String | 0 | 190px | left |
| 5 | description | Description | String | 53 | 300px | left |
| 6 | result | Result | String | 8 | 90px | left |
| 7 | measuredValue | Measured Value | Decimal128 | 4 | 140px | right |
| 8 | unitOfMeasureName | Unit of Measure | String | 12 | 150px | left |
| 9 | comment | Comment | String | 45 | 300px | left |
| 10 | completedBy | Completed By | String | 12 | 130px | left |
| 11 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 12 | createdBy | Created By | String | 12 | 110px | left |
| 13 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 14 | updatedBy | Updated By | String | 12 | 110px | left |
| 15 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); maintenanceWorkOrderId (reference key, shown through maintenanceWorkOrderName); maintenancePlanTaskId (reference key, shown through maintenancePlanTaskName); unitOfMeasureId (reference key, shown through unitOfMeasureName); completedById (reference key, shown through completedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): maintenancePlanTaskName

## u_mes_maint_maintenanceWorkOrderUsedSparePart - Maintenance Work Order Used Spare Parts (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_maintenanceWorkOrderUsedSparePart.json | _id: mes_maint_maintenanceWorkOrderUsedSparePartStable | rel: CL20261018-22:43 | samples: 10 | columns: 10 | total width: 1640px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 21 | 170px | left |
| 2 | maintenanceWorkOrderName | Maintenance Work Order | String | 50 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | sparePartName | Spare Part | String | 55 | 300px | left |
| 5 | quantity | Quantity | Decimal128 | 1 | 100px | right |
| 6 | costInr | Cost (INR) | Decimal128 | 7 | 110px | right |
| 7 | createdBy | Created By | String | 12 | 110px | left |
| 8 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 9 | updatedBy | Updated By | String | 12 | 110px | left |
| 10 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); maintenanceWorkOrderId (reference key, shown through maintenanceWorkOrderName); sparePartId (reference key, shown through sparePartName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_maint_reliabilitySummary - Reliability Summary (Reports)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_reliabilitySummary.json | _id: mes_maint_reliabilitySummaryStable | rel: CL20261018-22:43 | samples: 10 | columns: 19 | total width: 2760px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | equipmentName | Equipment | String | 31 | 240px | left |
| 3 | lineName | Line | String | 35 | 270px | left |
| 4 | shiftName | Shift | String | 0 | 80px | left |
| 5 | periodType | Period Type | String | 5 | 120px | left |
| 6 | periodStartAt | Period Start At | Date/Datetime | 19 | 160px | center |
| 7 | periodEndAt | Period End At | Date/Datetime | 19 | 160px | center |
| 8 | operatingHours | Operating (h) | Decimal128 | 5 | 140px | right |
| 9 | failureCount | Failure Count | Int32 | 1 | 140px | right |
| 10 | repairMinutes | Repair (min) | Int32 | 3 | 130px | right |
| 11 | mtbfHours | MTBF (h) | Decimal128 | 5 | 100px | right |
| 12 | mttrMinutes | MTTR (min) | Decimal128 | 5 | 110px | right |
| 13 | availabilityPct | Availability (%) | Decimal128 | 4 | 160px | right |
| 14 | calculatedAt | Calculated At | Date/Datetime | 19 | 160px | center |
| 15 | status | Status | String | 10 | 90px | left |
| 16 | createdBy | Created By | String | 12 | 110px | left |
| 17 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 18 | updatedBy | Updated By | String | 12 | 110px | left |
| 19 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); lineId (reference key, shown through lineName); shiftId (reference key, shown through shiftName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): shiftName

## u_mes_maint_sparePart - Spare Parts (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_sparePart.json | _id: mes_maint_sparePartStable | rel: CL20261018-22:43 | samples: 10 | columns: 18 | total width: 3040px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 9 | 110px | left |
| 2 | description | Description | String | 55 | 300px | left |
| 3 | category | Category | String | 12 | 110px | left |
| 4 | manufacturerName | Manufacturer | String | 28 | 220px | left |
| 5 | manufacturerPartNo | Manufacturer Part No | String | 12 | 180px | left |
| 6 | supplierName | Supplier | String | 36 | 280px | left |
| 7 | unitOfMeasureName | Unit of Measure | String | 4 | 150px | left |
| 8 | storageLocationName | Storage Location | String | 33 | 260px | left |
| 9 | stockQuantity | Stock Quantity | Decimal128 | 2 | 140px | right |
| 10 | minimumQuantity | Minimum Quantity | Decimal128 | 1 | 160px | right |
| 11 | reorderQuantity | Reorder Quantity | Decimal128 | 1 | 160px | right |
| 12 | leadTimeDays | Lead Time (days) | Int32 | 2 | 160px | right |
| 13 | unitCostInr | Unit Cost (INR) | Decimal128 | 6 | 150px | right |
| 14 | criticality | Criticality | String | 1 | 120px | left |
| 15 | lastIssuedAt | Last Issued At | Date/Datetime | 0 | 140px | center |
| 16 | lastReceivedAt | Last Received At | Date/Datetime | 0 | 160px | center |
| 17 | isInsuranceSpare | Insurance Spare | Boolean | 3 | 150px | center |
| 18 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); manufacturerId (reference key, shown through manufacturerName); supplierId (reference key, shown through supplierName); unitOfMeasureId (reference key, shown through unitOfMeasureName); storageLocationId (reference key, shown through storageLocationName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): lastIssuedAt, lastReceivedAt

## u_mes_maint_sparePartTransaction - Spare Part Transactions (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_sparePartTransaction.json | _id: mes_maint_sparePartTransactionStable | rel: CL20261018-22:43 | samples: 10 | columns: 18 | total width: 2990px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | sparePartName | Spare Part | String | 55 | 300px | left |
| 3 | transactionType | Transaction Type | String | 7 | 160px | left |
| 4 | quantity | Quantity | Decimal128 | 2 | 100px | right |
| 5 | unitOfMeasureName | Unit of Measure | String | 4 | 150px | left |
| 6 | maintenanceWorkOrderName | Maintenance Work Order | String | 50 | 300px | left |
| 7 | equipmentName | Equipment | String | 31 | 240px | left |
| 8 | storageLocationName | Storage Location | String | 28 | 220px | left |
| 9 | scanVerified | Scan Verified | Boolean | 3 | 140px | center |
| 10 | unitCostInr | Unit Cost (INR) | Decimal128 | 6 | 150px | right |
| 11 | transactedAt | Transacted At | Date/Datetime | 19 | 160px | center |
| 12 | transactedBy | Transacted By | String | 12 | 140px | left |
| 13 | erpDocumentNo | ERP Document No | String | 10 | 150px | left |
| 14 | status | Status | String | 8 | 90px | left |
| 15 | createdBy | Created By | String | 12 | 110px | left |
| 16 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 17 | updatedBy | Updated By | String | 12 | 110px | left |
| 18 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); sparePartId (reference key, shown through sparePartName); unitOfMeasureId (reference key, shown through unitOfMeasureName); maintenanceWorkOrderId (reference key, shown through maintenanceWorkOrderName); equipmentId (reference key, shown through equipmentName); storageLocationId (reference key, shown through storageLocationName); transactedById (reference key, shown through transactedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_maint_sparePartUsedOnEquipment - Spare Part Used on Equipment (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_sparePartUsedOnEquipment.json | _id: mes_maint_sparePartUsedOnEquipmentStable | rel: CL20261018-22:43 | samples: 10 | columns: 4 | total width: 790px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | sparePartName | Spare Part | String | 55 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | usedOnEquipmentName | Used on Equipment | String | 31 | 240px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); sparePartId (reference key, shown through sparePartName); usedOnEquipmentId (reference key, shown through usedOnEquipmentName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_maint_tool - Tools (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_tool.json | _id: mes_maint_toolStable | rel: CL20261018-22:43 | samples: 20 | columns: 28 | total width: 4920px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | name | Name | String | 46 | 300px | left |
| 3 | toolTypeName | Tool Type | String | 21 | 170px | left |
| 4 | toolClass | Tool Class | String | 22 | 180px | left |
| 5 | equipmentName | Equipment | String | 54 | 300px | left |
| 6 | mountedPosition | Mounted Position | String | 9 | 160px | left |
| 7 | supplierName | Supplier | String | 44 | 300px | left |
| 8 | drawingNo | Drawing No | String | 14 | 120px | left |
| 9 | serialNo | Serial No | String | 14 | 120px | left |
| 10 | cavities | Cavities | Int32 | 2 | 100px | right |
| 11 | lifeUom | Life UoM | String | 7 | 100px | left |
| 12 | lifeLimit | Life Limit | Int64 | 8 | 110px | right |
| 13 | lifeUsed | Life Used | Int64 | 8 | 110px | right |
| 14 | lifeRemaining | Life Remaining | Int64 | 7 | 140px | right |
| 15 | warningThresholdPct | Warning Threshold (%) | Decimal128 | 4 | 190px | right |
| 16 | regrindCount | Regrind Count | Int32 | 1 | 140px | right |
| 17 | maxRegrinds | Max Regrinds | Int32 | 1 | 130px | right |
| 18 | storageLocationName | Storage Location | String | 33 | 260px | left |
| 19 | lastMaintainedAt | Last Maintained At | Date/Datetime | 19 | 170px | center |
| 20 | nextMaintenanceDueAt | Next Maintenance Due At | Date/Date | 10 | 210px | center |
| 21 | purchasedAt | Purchased At | Date/Datetime | 19 | 160px | center |
| 22 | costInr | Cost (INR) | Decimal128 | 7 | 110px | right |
| 23 | ownedByCustomerName | Owned By Customer | String | 42 | 300px | left |
| 24 | blockAtLifeLimit | Block At Life Limit | Boolean | 3 | 180px | center |
| 25 | lastCertifiedAt | Last Certified At | Date/Datetime | 19 | 160px | center |
| 26 | certificationDueDate | Certification Due Date | Date/Date | 10 | 200px | center |
| 27 | certificateControlledDocumentName | Certificate Controlled Document | String | 0 | 260px | left |
| 28 | status | Status | String | 14 | 120px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); toolTypeId (reference key, shown through toolTypeName); equipmentId (reference key, shown through equipmentName); supplierId (reference key, shown through supplierName); storageLocationId (reference key, shown through storageLocationName); ownedByCustomerId (reference key, shown through ownedByCustomerName); certificateControlledDocumentId (reference key, shown through certificateControlledDocumentName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): certificateControlledDocumentName

## u_mes_maint_toolItem - Tool Applicable Items (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_toolItem.json | _id: mes_maint_toolItemStable | rel: CL20261018-22:43 | samples: 10 | columns: 4 | total width: 870px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | toolName | Tool | String | 39 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | itemName | Item | String | 39 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); toolId (reference key, shown through toolName); itemId (reference key, shown through itemName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_maint_toolLifeRecord - Tool Life Records (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_toolLifeRecord.json | _id: mes_maint_toolLifeRecordStable | rel: CL20261018-22:43 | samples: 10 | columns: 25 | total width: 4400px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | toolName | Tool | String | 39 | 300px | left |
| 3 | equipmentName | Equipment | String | 31 | 240px | left |
| 4 | eventType | Event Type | String | 11 | 110px | left |
| 5 | productionOrderName | Production Order | String | 10 | 160px | left |
| 6 | eventAt | Event At | Date/Datetime | 19 | 160px | center |
| 7 | performedBy | Performed By | String | 14 | 130px | left |
| 8 | cyclesThisEvent | Cycles This Event | Int64 | 3 | 160px | right |
| 9 | lifeUsedBefore | Life Used Before | Int64 | 5 | 160px | right |
| 10 | lifeUsedAfter | Life Used After | Int64 | 5 | 150px | right |
| 11 | lifeRemaining | Life Remaining | Int64 | 6 | 140px | right |
| 12 | regrindNo | Regrind No | Int32 | 0 | 110px | right |
| 13 | conditionOnRemoval | Condition on Removal | String | 11 | 180px | left |
| 14 | removalReason | Removal Reason | String | 18 | 150px | left |
| 15 | measuredWearMm | Measured Wear (mm) | Decimal128 | 4 | 170px | right |
| 16 | maintenanceWorkOrderName | Maintenance Work Order | String | 48 | 300px | left |
| 17 | remarks | Remarks | String | 37 | 280px | left |
| 18 | workCenterName | Work Center | String | 33 | 260px | left |
| 19 | itemName | Item | String | 39 | 300px | left |
| 20 | operationExecutionName | Operation Execution | String | 0 | 180px | left |
| 21 | status | Status | String | 8 | 90px | left |
| 22 | createdBy | Created By | String | 12 | 110px | left |
| 23 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 24 | updatedBy | Updated By | String | 12 | 110px | left |
| 25 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); toolId (reference key, shown through toolName); equipmentId (reference key, shown through equipmentName); productionOrderId (reference key, shown through productionOrderName); performedById (reference key, shown through performedBy); maintenanceWorkOrderId (reference key, shown through maintenanceWorkOrderName); workCenterId (reference key, shown through workCenterName); itemId (reference key, shown through itemName); operationExecutionId (reference key, shown through operationExecutionName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): regrindNo, operationExecutionName

## u_mes_maint_toolType - Tool Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_maint_toolType.json | _id: mes_maint_toolTypeStable | rel: CL20261018-22:43 | samples: 20 | columns: 6 | total width: 850px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | name | Name | String | 21 | 170px | left |
| 3 | description | Description | String | 33 | 260px | left |
| 4 | lifeUom | Life UoM | String | 7 | 100px | left |
| 5 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 6 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))
