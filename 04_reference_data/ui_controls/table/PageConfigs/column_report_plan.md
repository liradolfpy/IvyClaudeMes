## u_mes_plan_andonEvent - Andon Events (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_andonEvent.json | _id: mes_plan_andonEventStable | rel: CL20261018-23:51 | samples: 10 | columns: 27 | total width: 4680px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | workCenterName | Work Center | String | 33 | 260px | left |
| 3 | lineName | Line | String | 35 | 270px | left |
| 4 | shiftName | Shift | String | 7 | 80px | left |
| 5 | andonTypeName | Andon Type | String | 18 | 150px | left |
| 6 | reasonCodeName | Reason Code | String | 27 | 210px | left |
| 7 | raisedBy | Raised By | String | 14 | 120px | left |
| 8 | raisedAt | Raised At | Date/Datetime | 19 | 160px | center |
| 9 | acknowledgedBy | Acknowledged By | String | 12 | 150px | left |
| 10 | acknowledgedAt | Acknowledged At | Date/Datetime | 19 | 160px | center |
| 11 | resolvedBy | Resolved By | String | 12 | 120px | left |
| 12 | resolvedAt | Resolved At | Date/Datetime | 19 | 160px | center |
| 13 | responseSec | Response (s) | Int32 | 3 | 130px | right |
| 14 | resolutionSec | Resolution (s) | Int32 | 4 | 140px | right |
| 15 | lineStopped | Line Stopped | Boolean | 3 | 130px | center |
| 16 | downtimeEventName | Downtime Event | String | 14 | 140px | left |
| 17 | description | Description | String | 60 | 300px | left |
| 18 | resolutionText | Resolution Text | String | 69 | 300px | left |
| 19 | equipmentName | Equipment | String | 30 | 230px | left |
| 20 | severityClass | Severity Class | String | 6 | 140px | left |
| 21 | maintenanceWorkOrderName | Maintenance Work Order | String | 46 | 300px | left |
| 22 | escalationRuleName | Escalation Rule | String | 30 | 230px | left |
| 23 | status | Status | String | 12 | 110px | left |
| 24 | createdBy | Created By | String | 14 | 120px | left |
| 25 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 26 | updatedBy | Updated By | String | 14 | 120px | left |
| 27 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCenterId (reference key, shown through workCenterName); lineId (reference key, shown through lineName); shiftId (reference key, shown through shiftName); andonTypeId (reference key, shown through andonTypeName); reasonCodeId (reference key, shown through reasonCodeName); raisedById (reference key, shown through raisedBy); acknowledgedById (reference key, shown through acknowledgedBy); resolvedById (reference key, shown through resolvedBy); downtimeEventId (reference key, shown through downtimeEventName); equipmentId (reference key, shown through equipmentName); maintenanceWorkOrderId (reference key, shown through maintenanceWorkOrderName); escalationRuleId (reference key, shown through escalationRuleName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_andonEventEscalation - Andon Event Escalations (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_andonEventEscalation.json | _id: mes_plan_andonEventEscalationStable | rel: CL20261018-23:51 | samples: 10 | columns: 11 | total width: 1600px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | andonEventName | Andon Event | String | 60 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | level | Level | Int32 | 1 | 80px | right |
| 5 | escalatedAt | Escalated At | Date/Datetime | 19 | 160px | center |
| 6 | toUserName | To User | String | 14 | 120px | left |
| 7 | channel | Channel | String | 11 | 100px | left |
| 8 | createdBy | Created By | String | 14 | 120px | left |
| 9 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 10 | updatedBy | Updated By | String | 14 | 120px | left |
| 11 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); andonEventId (reference key, shown through andonEventName); toUserId (reference key, shown through toUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_andonType - Andon Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_andonType.json | _id: mes_plan_andonTypeStable | rel: CL20261018-23:51 | samples: 10 | columns: 10 | total width: 1600px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 9 | 110px | left |
| 2 | name | Name | String | 19 | 160px | left |
| 3 | description | Description | String | 30 | 230px | left |
| 4 | colourCode | Colour Code | String | 7 | 120px | left |
| 5 | responsibleDepartmentName | Responsible Department | String | 10 | 200px | left |
| 6 | targetResponseSec | Target Response (s) | Int32 | 3 | 180px | right |
| 7 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 8 | targetRepairSec | Target Repair (s) | Int32 | 4 | 160px | right |
| 9 | escalationRuleName | Escalation Rule | String | 30 | 230px | left |
| 10 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); responsibleDepartmentId (reference key, shown through responsibleDepartmentName); escalationRuleId (reference key, shown through escalationRuleName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_plan_changeover - Changeovers (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_changeover.json | _id: mes_plan_changeoverStable | rel: CL20261018-23:51 | samples: 20 | columns: 24 | total width: 4840px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | lineName | Line | String | 35 | 270px | left |
| 3 | workCenterName | Work Center | String | 37 | 280px | left |
| 4 | equipmentName | Equipment | String | 54 | 300px | left |
| 5 | fromProductionOrderName | From Production Order | String | 10 | 190px | left |
| 6 | toProductionOrderName | To Production Order | String | 10 | 180px | left |
| 7 | fromItemName | From Item | String | 49 | 300px | left |
| 8 | toItemName | To Item | String | 61 | 300px | left |
| 9 | changeoverType | Changeover Type | String | 14 | 150px | left |
| 10 | plannedStartAt | Planned Start At | Date/Datetime | 19 | 160px | center |
| 11 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 12 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 13 | plannedMinutes | Planned (min) | Int32 | 2 | 140px | right |
| 14 | actualMinutes | Actual (min) | Int32 | 2 | 130px | right |
| 15 | recipeName | Recipe | String | 56 | 300px | left |
| 16 | firstOffCheckSheetResultName | First Off Check Sheet Result | String | 15 | 240px | left |
| 17 | firstOffApprovedBy | First Off Approved By | String | 15 | 190px | left |
| 18 | firstOffApprovedAt | First Off Approved At | Date/Datetime | 19 | 190px | center |
| 19 | lossReason | Loss Reason | String | 67 | 300px | left |
| 20 | status | Status | String | 27 | 210px | left |
| 21 | createdBy | Created By | String | 14 | 120px | left |
| 22 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 23 | updatedBy | Updated By | String | 14 | 120px | left |
| 24 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); lineId (reference key, shown through lineName); workCenterId (reference key, shown through workCenterName); equipmentId (reference key, shown through equipmentName); fromProductionOrderId (reference key, shown through fromProductionOrderName); toProductionOrderId (reference key, shown through toProductionOrderName); fromItemId (reference key, shown through fromItemName); toItemId (reference key, shown through toItemName); recipeId (reference key, shown through recipeName); firstOffCheckSheetResultId (reference key, shown through firstOffCheckSheetResultName); firstOffApprovedById (reference key, shown through firstOffApprovedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_changeoverInstalledTool - Changeover Installed Tools (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_changeoverInstalledTool.json | _id: mes_plan_changeoverInstalledToolStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1270px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | changeoverName | Changeover | String | 15 | 130px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | installedToolName | Installed Tool | String | 39 | 300px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); changeoverId (reference key, shown through changeoverName); installedToolId (reference key, shown through installedToolName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_changeoverPerformedByUser - Changeover Crew (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_changeoverPerformedByUser.json | _id: mes_plan_changeoverPerformedByUserStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1140px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 21 | 170px | left |
| 2 | changeoverName | Changeover | String | 15 | 130px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | performedByUserName | Performed By User | String | 14 | 160px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); changeoverId (reference key, shown through changeoverName); performedByUserId (reference key, shown through performedByUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_changeoverRemovedTool - Changeover Removed Tools (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_changeoverRemovedTool.json | _id: mes_plan_changeoverRemovedToolStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1270px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | changeoverName | Changeover | String | 15 | 130px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | removedToolName | Removed Tool | String | 39 | 300px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); changeoverId (reference key, shown through changeoverName); removedToolId (reference key, shown through removedToolName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_changeoverStep - Changeover Steps (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_changeoverStep.json | _id: mes_plan_changeoverStepStable | rel: CL20261018-23:51 | samples: 10 | columns: 11 | total width: 1690px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | changeoverName | Changeover | String | 15 | 130px | left |
| 3 | stepNo | Step No | Int32 | 2 | 90px | right |
| 4 | description | Description | String | 83 | 300px | left |
| 5 | internalExternal | Internal External | String | 8 | 160px | left |
| 6 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 7 | completedBy | Completed By | String | 14 | 130px | left |
| 8 | createdBy | Created By | String | 14 | 120px | left |
| 9 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 10 | updatedBy | Updated By | String | 14 | 120px | left |
| 11 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); changeoverId (reference key, shown through changeoverName); completedById (reference key, shown through completedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_container - Containers (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_container.json | _id: mes_plan_containerStable | rel: CL20261018-23:51 | samples: 20 | columns: 24 | total width: 3640px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | containerTypeName | Container Type | String | 33 | 260px | left |
| 3 | packagingSpecificationName | Packaging Specification | String | 25 | 210px | left |
| 4 | isReturnable | Returnable | Boolean | 3 | 110px | center |
| 5 | ownerCustomerName | Owner Customer | String | 24 | 190px | left |
| 6 | itemName | Item | String | 61 | 300px | left |
| 7 | quantity | Quantity | Int32 | 5 | 100px | right |
| 8 | capacity | Capacity | Int32 | 5 | 100px | right |
| 9 | storageLocationName | Storage Location | String | 32 | 250px | left |
| 10 | parentContainerName | Parent Container | String | 0 | 160px | left |
| 11 | tareWeightKg | Tare Weight Kg | Decimal128 | 4 | 140px | right |
| 12 | grossWeightKg | Gross Weight Kg | Decimal128 | 5 | 150px | right |
| 13 | onHold | On Hold | Boolean | 3 | 90px | center |
| 14 | packedAt | Packed At | Date/Datetime | 19 | 160px | center |
| 15 | packedBy | Packed By | String | 14 | 120px | left |
| 16 | labelName | Label | String | 15 | 130px | left |
| 17 | shipmentName | Shipment | String | 15 | 130px | left |
| 18 | lastCleanedAt | Last Cleaned At | Date/Datetime | 19 | 160px | center |
| 19 | cycleCount | Cycle Count | Int32 | 2 | 120px | right |
| 20 | status | Status | String | 7 | 90px | left |
| 21 | createdBy | Created By | String | 14 | 120px | left |
| 22 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 23 | updatedBy | Updated By | String | 14 | 120px | left |
| 24 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); containerTypeId (reference key, shown through containerTypeName); packagingSpecificationId (reference key, shown through packagingSpecificationName); ownerCustomerId (reference key, shown through ownerCustomerName); itemId (reference key, shown through itemName); storageLocationId (reference key, shown through storageLocationName); parentContainerId (reference key, shown through parentContainerName); packedById (reference key, shown through packedBy); labelId (reference key, shown through labelName); shipmentId (reference key, shown through shipmentName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): parentContainerName

## u_mes_plan_containerLot - Container Lots (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_containerLot.json | _id: mes_plan_containerLotStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1040px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | containerName | Container | String | 10 | 110px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | lotName | Lot | String | 15 | 130px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); containerId (reference key, shown through containerName); lotId (reference key, shown through lotName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_containerType - Container Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_containerType.json | _id: mes_plan_containerTypeStable | rel: CL20261018-23:51 | samples: 20 | columns: 10 | total width: 1480px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | name | Name | String | 33 | 260px | left |
| 3 | description | Description | String | 43 | 300px | left |
| 4 | lengthMm | Length (mm) | Decimal128 | 5 | 120px | right |
| 5 | widthMm | Width (mm) | Decimal128 | 5 | 110px | right |
| 6 | heightMm | Height (mm) | Decimal128 | 5 | 120px | right |
| 7 | tareWeightKg | Tare Weight Kg | Decimal128 | 4 | 140px | right |
| 8 | isReturnable | Returnable | Boolean | 3 | 110px | center |
| 9 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 10 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_plan_customerSchedule - Customer Schedules (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_customerSchedule.json | _id: mes_plan_customerScheduleStable | rel: CL20261018-23:51 | samples: 10 | columns: 15 | total width: 2310px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | customerName | Customer | String | 23 | 190px | left |
| 3 | shipToCode | Ship to Code | String | 10 | 130px | left |
| 4 | scheduleType | Schedule Type | String | 21 | 170px | left |
| 5 | customerOrderNo | Customer Order No | String | 10 | 160px | left |
| 6 | receivedAt | Received At | Date/Datetime | 19 | 160px | center |
| 7 | horizonFrom | Horizon From | Date/Date | 10 | 130px | center |
| 8 | horizonTo | Horizon to | Date/Date | 10 | 110px | center |
| 9 | supersedesCustomerScheduleName | Supersedes Customer Schedule | String | 0 | 240px | left |
| 10 | erpSalesOrderNo | ERP Sales Order No | String | 10 | 170px | left |
| 11 | status | Status | String | 17 | 140px | left |
| 12 | createdBy | Created By | String | 14 | 120px | left |
| 13 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 14 | updatedBy | Updated By | String | 14 | 120px | left |
| 15 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerId (reference key, shown through customerName); supersedesCustomerScheduleId (reference key, shown through supersedesCustomerScheduleName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): supersedesCustomerScheduleName

## u_mes_plan_customerScheduleLine - Customer Schedule Lines (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_customerScheduleLine.json | _id: mes_plan_customerScheduleLineStable | rel: CL20261018-23:51 | samples: 10 | columns: 15 | total width: 2210px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 22 | 180px | left |
| 2 | customerScheduleName | Customer Schedule | String | 18 | 160px | left |
| 3 | lineNo | Line No | Int32 | 2 | 90px | right |
| 4 | itemName | Item | String | 32 | 250px | left |
| 5 | customerPartNo | Customer Part No | String | 15 | 160px | left |
| 6 | dueDate | Due Date | Date/Date | 10 | 100px | center |
| 7 | quantity | Quantity | Int32 | 3 | 100px | right |
| 8 | cumulativeRequired | Cumulative Required | Int32 | 5 | 180px | right |
| 9 | cumulativeShipped | Cumulative Shipped | Int32 | 5 | 170px | right |
| 10 | firmness | Firmness | String | 4 | 100px | left |
| 11 | shippedQuantity | Shipped Quantity | Int32 | 3 | 160px | right |
| 12 | createdBy | Created By | String | 14 | 120px | left |
| 13 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 14 | updatedBy | Updated By | String | 14 | 120px | left |
| 15 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerScheduleId (reference key, shown through customerScheduleName); itemId (reference key, shown through itemName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_dispatchList - Dispatch Lists (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_dispatchList.json | _id: mes_plan_dispatchListStable | rel: CL20261018-23:51 | samples: 10 | columns: 13 | total width: 1900px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | workCenterName | Work Center | String | 33 | 260px | left |
| 3 | shiftName | Shift | String | 7 | 80px | left |
| 4 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 5 | generatedAt | Generated At | Date/Datetime | 19 | 160px | center |
| 6 | rule | Rule | String | 17 | 140px | left |
| 7 | acknowledgedBy | Acknowledged By | String | 12 | 150px | left |
| 8 | acknowledgedAt | Acknowledged At | Date/Datetime | 19 | 160px | center |
| 9 | status | Status | String | 12 | 110px | left |
| 10 | createdBy | Created By | String | 14 | 120px | left |
| 11 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 12 | updatedBy | Updated By | String | 14 | 120px | left |
| 13 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCenterId (reference key, shown through workCenterName); shiftId (reference key, shown through shiftName); acknowledgedById (reference key, shown through acknowledgedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_dispatchListEntry - Dispatch List Entries (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_dispatchListEntry.json | _id: mes_plan_dispatchListEntryStable | rel: CL20261018-23:51 | samples: 10 | columns: 18 | total width: 2570px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | dispatchListName | Dispatch List | String | 15 | 140px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | rank | Rank | Int32 | 1 | 80px | right |
| 5 | productionOrderName | Production Order | String | 10 | 160px | left |
| 6 | lotName | Lot | String | 15 | 130px | left |
| 7 | itemName | Item | String | 39 | 300px | left |
| 8 | quantity | Quantity | Int32 | 1 | 100px | right |
| 9 | dueAt | Due At | Date/Datetime | 19 | 160px | center |
| 10 | queueSince | Queue Since | Date/Datetime | 19 | 160px | center |
| 11 | priority | Priority | String | 6 | 100px | left |
| 12 | materialAvailable | Material Available | Boolean | 3 | 170px | center |
| 13 | toolAvailable | Tool Available | Boolean | 3 | 140px | center |
| 14 | status | Status | String | 9 | 90px | left |
| 15 | createdBy | Created By | String | 14 | 120px | left |
| 16 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 17 | updatedBy | Updated By | String | 14 | 120px | left |
| 18 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); dispatchListId (reference key, shown through dispatchListName); productionOrderId (reference key, shown through productionOrderName); lotId (reference key, shown through lotName); itemId (reference key, shown through itemName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_documentAcknowledgement - Document Acknowledgements (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_documentAcknowledgement.json | _id: mes_plan_documentAcknowledgementStable | rel: CL20261018-23:51 | samples: 20 | columns: 19 | total width: 3300px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | relatedCollectionName | Related Collection Name | String | 26 | 210px | left |
| 3 | relatedEntityName | Related Entity | String | 65 | 300px | left |
| 4 | documentVersion | Document Version | String | 1 | 160px | left |
| 5 | userName | User | String | 14 | 120px | left |
| 6 | workCenterName | Work Center | String | 37 | 280px | left |
| 7 | productVariantName | Product Variant | String | 44 | 300px | left |
| 8 | productionOrderName | Production Order | String | 10 | 160px | left |
| 9 | shiftName | Shift | String | 7 | 80px | left |
| 10 | operatorSessionName | Operator Session | String | 18 | 160px | left |
| 11 | acknowledgementType | Acknowledgement Type | String | 27 | 210px | left |
| 12 | method | Method | String | 20 | 160px | left |
| 13 | electronicSignatureName | Electronic Signature | String | 15 | 180px | left |
| 14 | acknowledgedAt | Acknowledged At | Date/Datetime | 19 | 160px | center |
| 15 | status | Status | String | 12 | 110px | left |
| 16 | createdBy | Created By | String | 14 | 120px | left |
| 17 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 18 | updatedBy | Updated By | String | 14 | 120px | left |
| 19 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); relatedEntityId (reference key, shown through relatedEntityName); userId (reference key, shown through userName); workCenterId (reference key, shown through workCenterName); productVariantId (reference key, shown through productVariantName); productionOrderId (reference key, shown through productionOrderName); shiftId (reference key, shown through shiftName); operatorSessionId (reference key, shown through operatorSessionName); electronicSignatureId (reference key, shown through electronicSignatureName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_indirectActivity - Indirect Activities (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_indirectActivity.json | _id: mes_plan_indirectActivityStable | rel: CL20261018-23:51 | samples: 10 | columns: 7 | total width: 1070px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 11 | 110px | left |
| 2 | name | Name | String | 23 | 190px | left |
| 3 | description | Description | String | 34 | 260px | left |
| 4 | isPaid | Paid | Boolean | 3 | 80px | center |
| 5 | costCenterName | Cost Center | String | 28 | 220px | left |
| 6 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 7 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); costCenterId (reference key, shown through costCenterName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_plan_interlockEvent - Interlock Events (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_interlockEvent.json | _id: mes_plan_interlockEventStable | rel: CL20261018-23:51 | samples: 20 | columns: 30 | total width: 5770px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | interlockRuleName | Interlock Rule | String | 51 | 300px | left |
| 3 | ruleType | Rule Type | String | 17 | 140px | left |
| 4 | workCenterName | Work Center | String | 37 | 280px | left |
| 5 | equipmentName | Equipment | String | 54 | 300px | left |
| 6 | productionOrderName | Production Order | String | 10 | 160px | left |
| 7 | wipUnitName | WIP Unit | String | 20 | 160px | left |
| 8 | lotName | Lot | String | 15 | 130px | left |
| 9 | operationExecutionName | Operation Execution | String | 0 | 180px | left |
| 10 | relatedCollectionName | Related Collection Name | String | 26 | 210px | left |
| 11 | relatedEntityName | Related Entity | String | 37 | 280px | left |
| 12 | foundValueText | Found Value Text | String | 67 | 300px | left |
| 13 | expectedValueText | Expected Value Text | String | 41 | 300px | left |
| 14 | messageText | Message Text | String | 93 | 300px | left |
| 15 | shiftName | Shift | String | 7 | 80px | left |
| 16 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 17 | operatorUserName | Operator User | String | 14 | 140px | left |
| 18 | raisedAt | Raised At | Date/Datetime | 19 | 160px | center |
| 19 | overrideReasonCodeName | Override Reason Code | String | 22 | 180px | left |
| 20 | overrideComment | Override Comment | String | 102 | 300px | left |
| 21 | overrideBy | Override By | String | 14 | 120px | left |
| 22 | overrideAt | Override At | Date/Datetime | 19 | 160px | center |
| 23 | electronicSignatureName | Electronic Signature | String | 0 | 180px | left |
| 24 | clearedAt | Cleared At | Date/Datetime | 19 | 160px | center |
| 25 | notificationName | Notification | String | 43 | 300px | left |
| 26 | status | Status | String | 10 | 90px | left |
| 27 | createdBy | Created By | String | 14 | 120px | left |
| 28 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 29 | updatedBy | Updated By | String | 14 | 120px | left |
| 30 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); interlockRuleId (reference key, shown through interlockRuleName); workCenterId (reference key, shown through workCenterName); equipmentId (reference key, shown through equipmentName); productionOrderId (reference key, shown through productionOrderName); wipUnitId (reference key, shown through wipUnitName); lotId (reference key, shown through lotName); operationExecutionId (reference key, shown through operationExecutionName); relatedEntityId (reference key, shown through relatedEntityName); shiftId (reference key, shown through shiftName); operatorUserId (reference key, shown through operatorUserName); overrideReasonCodeId (reference key, shown through overrideReasonCodeName); overrideById (reference key, shown through overrideBy); electronicSignatureId (reference key, shown through electronicSignatureName); notificationId (reference key, shown through notificationName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): operationExecutionName, electronicSignatureName

## u_mes_plan_labourBooking - Labour Bookings (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_labourBooking.json | _id: mes_plan_labourBookingStable | rel: CL20261018-23:51 | samples: 20 | columns: 26 | total width: 4050px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | userName | User | String | 14 | 120px | left |
| 3 | shiftName | Shift | String | 7 | 80px | left |
| 4 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 5 | bookingType | Booking Type | String | 8 | 130px | left |
| 6 | productionOrderName | Production Order | String | 10 | 160px | left |
| 7 | operationName | Operation | String | 30 | 230px | left |
| 8 | workCenterName | Work Center | String | 37 | 280px | left |
| 9 | indirectActivityName | Indirect Activity | String | 19 | 160px | left |
| 10 | clockOnAt | Clock on At | Date/Datetime | 19 | 160px | center |
| 11 | clockOffAt | Clock Off At | Date/Datetime | 19 | 160px | center |
| 12 | durationMinutes | Duration (min) | Int32 | 3 | 140px | right |
| 13 | overtimeMinutes | Overtime (min) | Int32 | 1 | 140px | right |
| 14 | quantityGood | Quantity Good | Int32 | 1 | 140px | right |
| 15 | approvedBy | Approved By | String | 15 | 130px | left |
| 16 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 17 | erpConfirmationNo | ERP Confirmation No | String | 10 | 180px | left |
| 18 | source | Source | String | 12 | 110px | left |
| 19 | operationExecutionName | Operation Execution | String | 15 | 180px | left |
| 20 | productVariantName | Product Variant | String | 44 | 300px | left |
| 21 | operatorSessionName | Operator Session | String | 18 | 160px | left |
| 22 | status | Status | String | 8 | 90px | left |
| 23 | createdBy | Created By | String | 14 | 120px | left |
| 24 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 25 | updatedBy | Updated By | String | 14 | 120px | left |
| 26 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); userId (reference key, shown through userName); shiftId (reference key, shown through shiftName); productionOrderId (reference key, shown through productionOrderName); operationId (reference key, shown through operationName); workCenterId (reference key, shown through workCenterName); indirectActivityId (reference key, shown through indirectActivityName); approvedById (reference key, shown through approvedBy); operationExecutionId (reference key, shown through operationExecutionName); productVariantId (reference key, shown through productVariantName); operatorSessionId (reference key, shown through operatorSessionName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_lineClearance - Line Clearances (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_lineClearance.json | _id: mes_plan_lineClearanceStable | rel: CL20261018-23:51 | samples: 10 | columns: 24 | total width: 3750px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | lineName | Line | String | 22 | 180px | left |
| 3 | workCenterName | Work Center | String | 0 | 120px | left |
| 4 | clearanceType | Clearance Type | String | 18 | 150px | left |
| 5 | previousProductionOrderName | Previous Production Order | String | 10 | 220px | left |
| 6 | productionOrderName | Production Order | String | 10 | 160px | left |
| 7 | changeoverName | Changeover | String | 15 | 130px | left |
| 8 | checkSheetResultName | Check Sheet Result | String | 15 | 170px | left |
| 9 | materialsRemoved | Materials Removed | Boolean | 3 | 160px | center |
| 10 | labelsRemoved | Labels Removed | Boolean | 3 | 140px | center |
| 11 | documentsRemoved | Documents Removed | Boolean | 3 | 160px | center |
| 12 | equipmentClean | Equipment Clean | Boolean | 3 | 150px | center |
| 13 | performedBy | Performed By | String | 14 | 130px | left |
| 14 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 15 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 16 | verifiedBy | Verified By | String | 13 | 120px | left |
| 17 | verifiedAt | Verified At | Date/Datetime | 19 | 160px | center |
| 18 | electronicSignatureName | Electronic Signature | String | 0 | 180px | left |
| 19 | failureText | Failure Text | String | 77 | 300px | left |
| 20 | status | Status | String | 11 | 100px | left |
| 21 | createdBy | Created By | String | 14 | 120px | left |
| 22 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 23 | updatedBy | Updated By | String | 14 | 120px | left |
| 24 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); lineId (reference key, shown through lineName); workCenterId (reference key, shown through workCenterName); previousProductionOrderId (reference key, shown through previousProductionOrderName); productionOrderId (reference key, shown through productionOrderName); changeoverId (reference key, shown through changeoverName); checkSheetResultId (reference key, shown through checkSheetResultName); performedById (reference key, shown through performedBy); verifiedById (reference key, shown through verifiedBy); electronicSignatureId (reference key, shown through electronicSignatureName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): workCenterName, electronicSignatureName

## u_mes_plan_lot - Lots and Batches (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_lot.json | _id: mes_plan_lotStable | rel: CL20261018-23:51 | samples: 20 | columns: 34 | total width: 5780px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | itemName | Item | String | 61 | 300px | left |
| 3 | lotType | Lot Type | String | 21 | 170px | left |
| 4 | supplierName | Supplier | String | 44 | 300px | left |
| 5 | supplierLotNo | Supplier Lot No | String | 13 | 150px | left |
| 6 | heatNo | Heat No | String | 8 | 90px | left |
| 7 | goodsReceiptName | Goods Receipt | String | 15 | 140px | left |
| 8 | productionOrderName | Production Order | String | 10 | 160px | left |
| 9 | manufacturedAt | Manufactured At | Date/Datetime | 19 | 160px | center |
| 10 | receivedAt | Received At | Date/Datetime | 19 | 160px | center |
| 11 | expiryAt | Expiry At | Date/Date | 10 | 110px | center |
| 12 | initialQuantity | Initial Quantity | Decimal128 | 6 | 160px | right |
| 13 | currentQuantity | Current Quantity | Decimal128 | 6 | 160px | right |
| 14 | unitOfMeasureName | Unit of Measure | String | 8 | 150px | left |
| 15 | qualityStatus | Quality Status | String | 8 | 140px | left |
| 16 | onHold | On Hold | Boolean | 3 | 90px | center |
| 17 | qualityHoldName | Quality Hold | String | 15 | 130px | left |
| 18 | storageLocationName | Storage Location | String | 33 | 260px | left |
| 19 | attributesDieNo | Attributes Die No | String | 14 | 160px | left |
| 20 | attributesFurnaceChargeNo | Attributes Furnace Charge No | String | 12 | 240px | left |
| 21 | attributesHardnessHbw | Attributes Hardness Hbw | Decimal128 | 4 | 210px | right |
| 22 | attributesAnodisingLoadNo | Attributes Anodising Load No | String | 12 | 240px | left |
| 23 | attributesCoatingThicknessUm | Attributes Coating Thickness Um | Decimal128 | 4 | 260px | right |
| 24 | attributesCureDate | Attributes Cure Date | Date/Date | 10 | 180px | center |
| 25 | certificateControlledDocumentName | Certificate Controlled Document | String | 78 | 300px | left |
| 26 | currentOperationName | Current Operation | String | 26 | 210px | left |
| 27 | closedAt | Closed At | Date/Datetime | 0 | 110px | center |
| 28 | retestDate | Retest Date | Date/Date | 10 | 120px | center |
| 29 | batchReleaseName | Batch Release | String | 17 | 140px | left |
| 30 | status | Status | String | 10 | 90px | left |
| 31 | createdBy | Created By | String | 14 | 120px | left |
| 32 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 33 | updatedBy | Updated By | String | 14 | 120px | left |
| 34 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); supplierId (reference key, shown through supplierName); goodsReceiptId (reference key, shown through goodsReceiptName); productionOrderId (reference key, shown through productionOrderName); unitOfMeasureId (reference key, shown through unitOfMeasureName); qualityHoldId (reference key, shown through qualityHoldName); storageLocationId (reference key, shown through storageLocationName); certificateControlledDocumentId (reference key, shown through certificateControlledDocumentName); currentOperationId (reference key, shown through currentOperationName); batchReleaseId (reference key, shown through batchReleaseName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): closedAt

## u_mes_plan_lotAttributesCavityNo - Lot Cavity Numbers (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_lotAttributesCavityNo.json | _id: mes_plan_lotAttributesCavityNoStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1160px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 21 | 170px | left |
| 2 | lotName | Lot | String | 15 | 130px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | attributesCavityNo | Attributes Cavity No | String | 1 | 180px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); lotId (reference key, shown through lotName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_lotParentLot - Lot Parent Lots (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_lotParentLot.json | _id: mes_plan_lotParentLotStable | rel: CL20261018-23:51 | samples: 20 | columns: 8 | total width: 1100px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | lotName | Lot | String | 15 | 130px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | parentLotName | Parent Lot | String | 15 | 130px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); lotId (reference key, shown through lotName); parentLotId (reference key, shown through parentLotName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_operationExecution - Operation Executions (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_operationExecution.json | _id: mes_plan_operationExecutionStable | rel: CL20261019-12:24 | samples: 20 | columns: 52 | total width: 9480px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | productionOrderName | Production Order | String | 10 | 160px | left |
| 3 | wipUnitName | WIP Unit | String | 20 | 160px | left |
| 4 | lotName | Lot | String | 15 | 130px | left |
| 5 | itemName | Item | String | 49 | 300px | left |
| 6 | routingName | Routing | String | 48 | 300px | left |
| 7 | stepNo | Step No | Int32 | 3 | 90px | right |
| 8 | operationName | Operation | String | 30 | 230px | left |
| 9 | workCenterName | Work Center | String | 37 | 280px | left |
| 10 | equipmentName | Equipment | String | 54 | 300px | left |
| 11 | recipeName | Recipe | String | 56 | 300px | left |
| 12 | shiftName | Shift | String | 7 | 80px | left |
| 13 | operatorUserName | Operator User | String | 14 | 140px | left |
| 14 | executionType | Execution Type | String | 10 | 140px | left |
| 15 | attemptNo | Attempt No | Int32 | 1 | 110px | right |
| 16 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 17 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 18 | cycleTimeSec | Cycle Time (s) | Decimal128 | 5 | 140px | right |
| 19 | standardCycleTimeSec | Standard Cycle Time (s) | Decimal128 | 5 | 210px | right |
| 20 | quantityIn | Quantity in | Int32 | 3 | 120px | right |
| 21 | quantityGood | Quantity Good | Int32 | 3 | 140px | right |
| 22 | quantityReject | Quantity Reject | Int32 | 1 | 150px | right |
| 23 | quantityRework | Quantity Rework | Int32 | 1 | 150px | right |
| 24 | result | Result | String | 6 | 90px | left |
| 25 | checksSkillVerified | Checks Skill Verified | Boolean | 3 | 190px | center |
| 26 | checksRecipeVerified | Checks Recipe Verified | Boolean | 3 | 200px | center |
| 27 | checksToolLifeOk | Checks Tool Life Ok | Boolean | 3 | 180px | center |
| 28 | checksGaugeCalibrationOk | Checks Gauge Calibration Ok | Boolean | 3 | 230px | center |
| 29 | checksPreviousStepComplete | Checks Previous Step Complete | Boolean | 3 | 250px | center |
| 30 | nextStepNo | Next Step No | Int32 | 3 | 130px | right |
| 31 | remarks | Remarks | String | 66 | 300px | left |
| 32 | productVariantName | Product Variant | String | 44 | 300px | left |
| 33 | recipeVersion | Recipe Version | String | 1 | 140px | left |
| 34 | recipeChecksum | Recipe Checksum | String | 16 | 150px | left |
| 35 | taktTimeSec | Takt Time (s) | Decimal128 | 4 | 140px | right |
| 36 | taktBreached | Takt Breached | Boolean | 3 | 140px | center |
| 37 | captureMethod | Capture Method | String | 10 | 140px | left |
| 38 | startScanCode | Start Scan Code | String | 59 | 300px | left |
| 39 | operatorSessionName | Operator Session | String | 18 | 160px | left |
| 40 | checksVariantVerified | Checks Variant Verified | Boolean | 3 | 210px | center |
| 41 | checksDocumentAcknowledged | Checks Document Acknowledged | Boolean | 3 | 240px | center |
| 42 | checksEquipmentReady | Checks Equipment Ready | Boolean | 3 | 200px | center |
| 43 | checksMaterialReleased | Checks Material Released | Boolean | 3 | 210px | center |
| 44 | checksSetupVerified | Checks Setup Verified | Boolean | 3 | 190px | center |
| 45 | checksEnvironmentOk | Checks Environment Ok | Boolean | 3 | 190px | center |
| 46 | interlockEventCount | Interlock Event Count | Int32 | 1 | 190px | right |
| 47 | sourceMessageUuid | Source Message Uuid | String | 36 | 280px | left |
| 48 | status | Status | String | 9 | 90px | left |
| 49 | createdBy | Created By | String | 14 | 120px | left |
| 50 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 51 | updatedBy | Updated By | String | 14 | 120px | left |
| 52 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); productionOrderId (reference key, shown through productionOrderName); wipUnitId (reference key, shown through wipUnitName); lotId (reference key, shown through lotName); itemId (reference key, shown through itemName); routingId (reference key, shown through routingName); operationId (reference key, shown through operationName); workCenterId (reference key, shown through workCenterName); equipmentId (reference key, shown through equipmentName); recipeId (reference key, shown through recipeName); shiftId (reference key, shown through shiftName); operatorUserId (reference key, shown through operatorUserName); productVariantId (reference key, shown through productVariantName); operatorSessionId (reference key, shown through operatorSessionName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_operationExecutionDefectCode - Operation Execution Defect Codes (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_operationExecutionDefectCode.json | _id: mes_plan_operationExecutionDefectCodeStable | rel: CL20261018-23:51 | samples: 20 | columns: 8 | total width: 1300px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | operationExecutionName | Operation Execution | String | 15 | 180px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | defectCodeName | Defect Code | String | 36 | 280px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); operationExecutionId (reference key, shown through operationExecutionName); defectCodeId (reference key, shown through defectCodeName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_operationExecutionTool - Operation Execution Tools (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_operationExecutionTool.json | _id: mes_plan_operationExecutionToolStable | rel: CL20261018-23:51 | samples: 20 | columns: 8 | total width: 1320px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | operationExecutionName | Operation Execution | String | 15 | 180px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | toolName | Tool | String | 46 | 300px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); operationExecutionId (reference key, shown through operationExecutionName); toolId (reference key, shown through toolName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_operatorSession - Operator Sessions (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_operatorSession.json | _id: mes_plan_operatorSessionStable | rel: CL20261018-23:51 | samples: 20 | columns: 20 | total width: 3110px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | userName | User | String | 14 | 120px | left |
| 3 | workCenterName | Work Center | String | 35 | 270px | left |
| 4 | equipmentName | Equipment | String | 33 | 260px | left |
| 5 | shiftName | Shift | String | 7 | 80px | left |
| 6 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 7 | productionOrderName | Production Order | String | 10 | 160px | left |
| 8 | authenticationMethod | Authentication Method | String | 13 | 190px | left |
| 9 | loginAt | Login At | Date/Datetime | 19 | 160px | center |
| 10 | logoutAt | Logout At | Date/Datetime | 19 | 160px | center |
| 11 | logoutReason | Logout Reason | String | 15 | 140px | left |
| 12 | skillVerified | Skill Verified | Boolean | 3 | 140px | center |
| 13 | trainingVerified | Training Verified | Boolean | 3 | 160px | center |
| 14 | interlockEventName | Interlock Event | String | 18 | 150px | left |
| 15 | clientWorkstation | Client Workstation | String | 16 | 170px | left |
| 16 | status | Status | String | 8 | 90px | left |
| 17 | createdBy | Created By | String | 14 | 120px | left |
| 18 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 19 | updatedBy | Updated By | String | 14 | 120px | left |
| 20 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); userId (reference key, shown through userName); workCenterId (reference key, shown through workCenterName); equipmentId (reference key, shown through equipmentName); shiftId (reference key, shown through shiftName); productionOrderId (reference key, shown through productionOrderName); interlockEventId (reference key, shown through interlockEventName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_productionOrder - Production Orders (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_productionOrder.json | _id: mes_plan_productionOrderStable | rel: CL20261018-23:51 | samples: 20 | columns: 39 | total width: 6310px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | erpOrderNo | ERP Order No | String | 12 | 130px | left |
| 3 | itemName | Item | String | 61 | 300px | left |
| 4 | itemRevision | Item Revision | String | 1 | 140px | left |
| 5 | productVariantName | Product Variant | String | 44 | 300px | left |
| 6 | billOfMaterialName | Bill of Material | String | 21 | 170px | left |
| 7 | routingName | Routing | String | 51 | 300px | left |
| 8 | lineName | Line | String | 29 | 230px | left |
| 9 | customerScheduleName | Customer Schedule | String | 0 | 160px | left |
| 10 | orderType | Order Type | String | 16 | 140px | left |
| 11 | priority | Priority | String | 6 | 100px | left |
| 12 | plannedQuantity | Planned Quantity | Int32 | 6 | 160px | right |
| 13 | releasedQuantity | Released Quantity | Int32 | 6 | 160px | right |
| 14 | startedQuantity | Started Quantity | Int32 | 6 | 160px | right |
| 15 | goodQuantity | Good Quantity | Int32 | 6 | 140px | right |
| 16 | scrapQuantity | Scrap Quantity | Int32 | 4 | 140px | right |
| 17 | reworkQuantity | Rework Quantity | Int32 | 1 | 150px | right |
| 18 | unitOfMeasureName | Unit of Measure | String | 8 | 150px | left |
| 19 | plannedStartAt | Planned Start At | Date/Datetime | 19 | 160px | center |
| 20 | plannedEndAt | Planned End At | Date/Datetime | 19 | 160px | center |
| 21 | actualStartAt | Actual Start At | Date/Datetime | 19 | 160px | center |
| 22 | actualEndAt | Actual End At | Date/Datetime | 19 | 160px | center |
| 23 | dueDate | Due Date | Date/Date | 10 | 100px | center |
| 24 | erpMessageName | ERP Message | String | 15 | 130px | left |
| 25 | closedAt | Closed At | Date/Datetime | 19 | 160px | center |
| 26 | closedBy | Closed By | String | 15 | 130px | left |
| 27 | remarks | Remarks | String | 48 | 300px | left |
| 28 | onHold | On Hold | Boolean | 3 | 90px | center |
| 29 | qualityHoldName | Quality Hold | String | 15 | 130px | left |
| 30 | holdReasonCodeName | Hold Reason Code | String | 19 | 160px | left |
| 31 | genealogyComplete | Genealogy Complete | Boolean | 3 | 170px | center |
| 32 | batchRecordReviewName | Batch Record Review | String | 14 | 180px | left |
| 33 | lineClearanceName | Line Clearance | String | 16 | 140px | left |
| 34 | yieldWithinLimits | Yield Within Limits | Boolean | 3 | 180px | center |
| 35 | status | Status | String | 11 | 100px | left |
| 36 | createdBy | Created By | String | 14 | 120px | left |
| 37 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 38 | updatedBy | Updated By | String | 14 | 120px | left |
| 39 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); productVariantId (reference key, shown through productVariantName); billOfMaterialId (reference key, shown through billOfMaterialName); routingId (reference key, shown through routingName); lineId (reference key, shown through lineName); customerScheduleId (reference key, shown through customerScheduleName); unitOfMeasureId (reference key, shown through unitOfMeasureName); erpMessageId (reference key, shown through erpMessageName); closedById (reference key, shown through closedBy); qualityHoldId (reference key, shown through qualityHoldName); holdReasonCodeId (reference key, shown through holdReasonCodeName); batchRecordReviewId (reference key, shown through batchRecordReviewName); lineClearanceId (reference key, shown through lineClearanceName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): customerScheduleName

## u_mes_plan_productionOrderLot - Production Order Lots (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_productionOrderLot.json | _id: mes_plan_productionOrderLotStable | rel: CL20261018-23:51 | samples: 20 | columns: 8 | total width: 1090px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | productionOrderName | Production Order | String | 10 | 160px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | lotName | Lot | String | 15 | 130px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); productionOrderId (reference key, shown through productionOrderName); lotId (reference key, shown through lotName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_productionOrderRelease - Production Order Releases (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_productionOrderRelease.json | _id: mes_plan_productionOrderReleaseStable | rel: CL20261018-23:51 | samples: 20 | columns: 10 | total width: 1340px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | productionOrderName | Production Order | String | 10 | 160px | left |
| 3 | releaseNo | Release No | Int32 | 1 | 110px | right |
| 4 | quantity | Quantity | Int32 | 1 | 100px | right |
| 5 | releasedAt | Released At | Date/Datetime | 19 | 160px | center |
| 6 | releasedBy | Released By | String | 15 | 130px | left |
| 7 | createdBy | Created By | String | 14 | 120px | left |
| 8 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 9 | updatedBy | Updated By | String | 14 | 120px | left |
| 10 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); productionOrderId (reference key, shown through productionOrderName); releasedById (reference key, shown through releasedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_productionSchedule - Production Schedules (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_productionSchedule.json | _id: mes_plan_productionScheduleStable | rel: CL20261018-23:51 | samples: 10 | columns: 17 | total width: 2420px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 3 | lineName | Line | String | 29 | 230px | left |
| 4 | shiftName | Shift | String | 7 | 80px | left |
| 5 | workCalendarName | Work Calendar | String | 26 | 210px | left |
| 6 | scheduleVersion | Schedule Version | Int32 | 1 | 160px | right |
| 7 | plannedOutput | Planned Output | Int32 | 4 | 140px | right |
| 8 | actualOutput | Actual Output | Int32 | 4 | 140px | right |
| 9 | attainmentPct | Attainment (%) | Decimal128 | 4 | 140px | right |
| 10 | frozen | Frozen | Boolean | 3 | 90px | center |
| 11 | publishedAt | Published At | Date/Datetime | 19 | 160px | center |
| 12 | publishedBy | Published By | String | 12 | 130px | left |
| 13 | status | Status | String | 11 | 100px | left |
| 14 | createdBy | Created By | String | 14 | 120px | left |
| 15 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 16 | updatedBy | Updated By | String | 14 | 120px | left |
| 17 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); lineId (reference key, shown through lineName); shiftId (reference key, shown through shiftName); workCalendarId (reference key, shown through workCalendarName); publishedById (reference key, shown through publishedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_productionScheduleSlot - Production Schedule Slots (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_productionScheduleSlot.json | _id: mes_plan_productionScheduleSlotStable | rel: CL20261018-23:51 | samples: 10 | columns: 14 | total width: 2270px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | productionScheduleName | Production Schedule | String | 15 | 180px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | productionOrderName | Production Order | String | 10 | 160px | left |
| 5 | itemName | Item | String | 39 | 300px | left |
| 6 | plannedQuantity | Planned Quantity | Int32 | 3 | 160px | right |
| 7 | plannedStartAt | Planned Start At | Date/Datetime | 19 | 160px | center |
| 8 | plannedEndAt | Planned End At | Date/Datetime | 19 | 160px | center |
| 9 | changeoverMinutes | Changeover (min) | Int32 | 1 | 160px | right |
| 10 | actualQuantity | Actual Quantity | Int32 | 3 | 150px | right |
| 11 | createdBy | Created By | String | 14 | 120px | left |
| 12 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 13 | updatedBy | Updated By | String | 14 | 120px | left |
| 14 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); productionScheduleId (reference key, shown through productionScheduleName); productionOrderId (reference key, shown through productionOrderName); itemId (reference key, shown through itemName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_recipeDownload - Recipe Downloads (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_recipeDownload.json | _id: mes_plan_recipeDownloadStable | rel: CL20261018-23:51 | samples: 20 | columns: 20 | total width: 3560px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | recipeName | Recipe | String | 56 | 300px | left |
| 3 | recipeVersion | Recipe Version | String | 1 | 140px | left |
| 4 | equipmentName | Equipment | String | 54 | 300px | left |
| 5 | workCenterName | Work Center | String | 37 | 280px | left |
| 6 | productionOrderName | Production Order | String | 10 | 160px | left |
| 7 | productVariantName | Product Variant | String | 44 | 300px | left |
| 8 | trigger | Trigger | String | 20 | 160px | left |
| 9 | checksumExpected | Checksum Expected | String | 16 | 160px | left |
| 10 | checksumReported | Checksum Reported | String | 16 | 160px | left |
| 11 | verificationResult | Verification Result | String | 8 | 180px | left |
| 12 | downloadedAt | Downloaded At | Date/Datetime | 19 | 160px | center |
| 13 | verifiedAt | Verified At | Date/Datetime | 19 | 160px | center |
| 14 | requestedBy | Requested By | String | 18 | 150px | left |
| 15 | interlockEventName | Interlock Event | String | 0 | 150px | left |
| 16 | status | Status | String | 8 | 90px | left |
| 17 | createdBy | Created By | String | 14 | 120px | left |
| 18 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 19 | updatedBy | Updated By | String | 14 | 120px | left |
| 20 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); recipeId (reference key, shown through recipeName); equipmentId (reference key, shown through equipmentName); workCenterId (reference key, shown through workCenterName); productionOrderId (reference key, shown through productionOrderName); productVariantId (reference key, shown through productVariantName); requestedById (reference key, shown through requestedBy); interlockEventId (reference key, shown through interlockEventName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): interlockEventName

## u_mes_plan_setupVerification - Setup Verifications (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_setupVerification.json | _id: mes_plan_setupVerificationStable | rel: CL20261018-23:51 | samples: 20 | columns: 18 | total width: 2950px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | workCenterName | Work Center | String | 37 | 280px | left |
| 3 | equipmentName | Equipment | String | 54 | 300px | left |
| 4 | productionOrderName | Production Order | String | 10 | 160px | left |
| 5 | productVariantName | Product Variant | String | 44 | 300px | left |
| 6 | changeoverName | Changeover | String | 0 | 110px | left |
| 7 | billOfProcessName | Bill of Process | String | 22 | 180px | left |
| 8 | trigger | Trigger | String | 17 | 140px | left |
| 9 | itemCount | Item Count | Int32 | 1 | 110px | right |
| 10 | failedCount | Failed Count | Int32 | 1 | 130px | right |
| 11 | verifiedBy | Verified By | String | 14 | 120px | left |
| 12 | verifiedAt | Verified At | Date/Datetime | 19 | 160px | center |
| 13 | interlockEventName | Interlock Event | String | 0 | 150px | left |
| 14 | status | Status | String | 11 | 100px | left |
| 15 | createdBy | Created By | String | 14 | 120px | left |
| 16 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 17 | updatedBy | Updated By | String | 14 | 120px | left |
| 18 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCenterId (reference key, shown through workCenterName); equipmentId (reference key, shown through equipmentName); productionOrderId (reference key, shown through productionOrderName); productVariantId (reference key, shown through productVariantName); changeoverId (reference key, shown through changeoverName); billOfProcessId (reference key, shown through billOfProcessName); verifiedById (reference key, shown through verifiedBy); interlockEventId (reference key, shown through interlockEventName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): changeoverName, interlockEventName

## u_mes_plan_setupVerificationItem - Setup Verification Items (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_setupVerificationItem.json | _id: mes_plan_setupVerificationItemStable | rel: CL20261018-23:51 | samples: 20 | columns: 16 | total width: 2510px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 22 | 180px | left |
| 2 | setupVerificationName | Setup Verification | String | 18 | 170px | left |
| 3 | itemNo | Item No | Int32 | 1 | 90px | right |
| 4 | checkType | Check Type | String | 9 | 110px | left |
| 5 | relatedCollectionName | Related Collection Name | String | 25 | 210px | left |
| 6 | relatedEntityName | Related Entity | String | 56 | 300px | left |
| 7 | scannedCode | Scanned Code | String | 28 | 220px | left |
| 8 | expectedValue | Expected Value | Decimal128 | 6 | 140px | right |
| 9 | actualValue | Actual Value | Decimal128 | 6 | 130px | right |
| 10 | unitOfMeasureName | Unit of Measure | String | 8 | 150px | left |
| 11 | passed | Passed | Boolean | 3 | 90px | center |
| 12 | checkedAt | Checked At | Date/Datetime | 19 | 160px | center |
| 13 | createdBy | Created By | String | 14 | 120px | left |
| 14 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 15 | updatedBy | Updated By | String | 14 | 120px | left |
| 16 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); setupVerificationId (reference key, shown through setupVerificationName); relatedEntityId (reference key, shown through relatedEntityName); unitOfMeasureId (reference key, shown through unitOfMeasureName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_shiftHandover - Shift Handovers (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_shiftHandover.json | _id: mes_plan_shiftHandoverStable | rel: CL20261018-23:51 | samples: 10 | columns: 22 | total width: 3810px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 3 | shiftName | Shift | String | 7 | 80px | left |
| 4 | lineName | Line | String | 35 | 270px | left |
| 5 | outgoingSupervisorUserName | Outgoing Supervisor User | String | 12 | 210px | left |
| 6 | incomingSupervisorUserName | Incoming Supervisor User | String | 12 | 210px | left |
| 7 | outputPlanned | Output Planned | Int32 | 4 | 140px | right |
| 8 | outputActual | Output Actual | Int32 | 4 | 140px | right |
| 9 | outputScrap | Output Scrap | Int32 | 1 | 130px | right |
| 10 | outputRework | Output Rework | Int32 | 2 | 140px | right |
| 11 | oeePct | OEE (%) | Decimal128 | 4 | 90px | right |
| 12 | safetyNotes | Safety Notes | String | 55 | 300px | left |
| 13 | qualityNotes | Quality Notes | String | 70 | 300px | left |
| 14 | maintenanceNotes | Maintenance Notes | String | 34 | 260px | left |
| 15 | materialNotes | Material Notes | String | 35 | 270px | left |
| 16 | handedOverAt | Handed Over At | Date/Datetime | 19 | 160px | center |
| 17 | acknowledgedAt | Acknowledged At | Date/Datetime | 19 | 160px | center |
| 18 | status | Status | String | 12 | 110px | left |
| 19 | createdBy | Created By | String | 14 | 120px | left |
| 20 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 21 | updatedBy | Updated By | String | 14 | 120px | left |
| 22 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); shiftId (reference key, shown through shiftName); lineId (reference key, shown through lineName); outgoingSupervisorUserId (reference key, shown through outgoingSupervisorUserName); incomingSupervisorUserId (reference key, shown through incomingSupervisorUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_shiftHandoverDowntimeEvent - Shift Handover Downtime Events (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_shiftHandoverDowntimeEvent.json | _id: mes_plan_shiftHandoverDowntimeEventStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1120px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | shiftHandoverName | Shift Handover | String | 15 | 140px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | downtimeEventName | Downtime Event | String | 14 | 140px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); shiftHandoverId (reference key, shown through shiftHandoverName); downtimeEventId (reference key, shown through downtimeEventName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_shiftHandoverNonconformance - Shift Handover Nonconformances (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_shiftHandoverNonconformance.json | _id: mes_plan_shiftHandoverNonconformanceStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1280px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | shiftHandoverName | Shift Handover | String | 15 | 140px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | nonconformanceName | Nonconformance | String | 55 | 300px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); shiftHandoverId (reference key, shown through shiftHandoverName); nonconformanceId (reference key, shown through nonconformanceName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_shiftHandoverOpenItem - Shift Handover Open Items (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_shiftHandoverOpenItem.json | _id: mes_plan_shiftHandoverOpenItemStable | rel: CL20261018-23:51 | samples: 10 | columns: 11 | total width: 1620px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | shiftHandoverName | Shift Handover | String | 15 | 140px | left |
| 3 | itemNo | Item No | Int32 | 1 | 90px | right |
| 4 | description | Description | String | 86 | 300px | left |
| 5 | ownerUserName | Owner User | String | 14 | 120px | left |
| 6 | dueAt | Due At | Date/Datetime | 19 | 160px | center |
| 7 | closed | Closed | Boolean | 3 | 90px | center |
| 8 | createdBy | Created By | String | 14 | 120px | left |
| 9 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 10 | updatedBy | Updated By | String | 14 | 120px | left |
| 11 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); shiftHandoverId (reference key, shown through shiftHandoverName); ownerUserId (reference key, shown through ownerUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_shiftHandoverProductionOrder - Shift Handover Production Orders (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_shiftHandoverProductionOrder.json | _id: mes_plan_shiftHandoverProductionOrderStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1140px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | shiftHandoverName | Shift Handover | String | 15 | 140px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | productionOrderName | Production Order | String | 10 | 160px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); shiftHandoverId (reference key, shown through shiftHandoverName); productionOrderId (reference key, shown through productionOrderName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_stepCompletion - Work Instruction Step Completions (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_stepCompletion.json | _id: mes_plan_stepCompletionStable | rel: CL20261018-23:51 | samples: 20 | columns: 29 | total width: 4620px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | operationExecutionName | Operation Execution | String | 15 | 180px | left |
| 3 | workInstructionName | Work Instruction | String | 65 | 300px | left |
| 4 | workInstructionVersion | Work Instruction Version | Int32 | 1 | 210px | right |
| 5 | stepNo | Step No | Int32 | 3 | 90px | right |
| 6 | wipUnitName | WIP Unit | String | 20 | 160px | left |
| 7 | workCenterName | Work Center | String | 37 | 280px | left |
| 8 | userName | User | String | 14 | 120px | left |
| 9 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 10 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 11 | durationSec | Duration (s) | Int32 | 2 | 130px | right |
| 12 | inputType | Input Type | String | 4 | 110px | left |
| 13 | enteredText | Entered Text | String | 19 | 160px | left |
| 14 | enteredNumber | Entered Number | Decimal128 | 5 | 140px | right |
| 15 | enteredFlag | Entered Flag | Boolean | 3 | 130px | center |
| 16 | scannedCode | Scanned Code | String | 26 | 210px | left |
| 17 | withinLimits | Within Limits | Boolean | 3 | 140px | center |
| 18 | deviceSource | Device Source | String | 12 | 140px | left |
| 19 | overridden | Overridden | Boolean | 3 | 110px | center |
| 20 | overrideBy | Override By | String | 14 | 120px | left |
| 21 | overrideReason | Override Reason | String | 0 | 150px | left |
| 22 | photoControlledDocumentName | Photo Controlled Document | String | 69 | 300px | left |
| 23 | overrideReasonCodeName | Override Reason Code | String | 25 | 200px | left |
| 24 | arSessionRef | Ar Session Ref | String | 0 | 140px | left |
| 25 | status | Status | String | 10 | 90px | left |
| 26 | createdBy | Created By | String | 14 | 120px | left |
| 27 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 28 | updatedBy | Updated By | String | 14 | 120px | left |
| 29 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); operationExecutionId (reference key, shown through operationExecutionName); workInstructionId (reference key, shown through workInstructionName); wipUnitId (reference key, shown through wipUnitName); workCenterId (reference key, shown through workCenterName); userId (reference key, shown through userName); overrideById (reference key, shown through overrideBy); photoControlledDocumentId (reference key, shown through photoControlledDocumentName); overrideReasonCodeId (reference key, shown through overrideReasonCodeName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): overrideReason, arSessionRef

## u_mes_plan_wipUnit - WIP Units (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_wipUnit.json | _id: mes_plan_wipUnitStable | rel: CL20261018-23:51 | samples: 20 | columns: 29 | total width: 4900px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | productionOrderName | Production Order | String | 10 | 160px | left |
| 3 | itemName | Item | String | 49 | 300px | left |
| 4 | itemRevision | Item Revision | String | 1 | 140px | left |
| 5 | productVariantName | Product Variant | String | 44 | 300px | left |
| 6 | serialNumberName | Serial Number | String | 13 | 140px | left |
| 7 | bodyLotName | Body Lot | String | 15 | 130px | left |
| 8 | routingName | Routing | String | 48 | 300px | left |
| 9 | currentStepNo | Current Step No | Int32 | 3 | 150px | right |
| 10 | currentOperationName | Current Operation | String | 30 | 230px | left |
| 11 | currentWorkCenterName | Current Work Center | String | 37 | 280px | left |
| 12 | qualityStatus | Quality Status | String | 8 | 140px | left |
| 13 | onHold | On Hold | Boolean | 3 | 90px | center |
| 14 | qualityHoldName | Quality Hold | String | 15 | 130px | left |
| 15 | reworkCount | Rework Count | Int32 | 1 | 130px | right |
| 16 | createdAtOperationName | Created At Operation | String | 30 | 230px | left |
| 17 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 18 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 19 | lastOperationExecutionName | Last Operation Execution | String | 15 | 210px | left |
| 20 | containerName | Container | String | 10 | 110px | left |
| 21 | bodyCavityNo | Body Cavity No | Int32 | 1 | 140px | right |
| 22 | castDateCode | Cast Date Code | String | 7 | 140px | left |
| 23 | scrappedAt | Scrapped At | Date/Datetime | 19 | 160px | center |
| 24 | shippedAt | Shipped At | Date/Datetime | 19 | 160px | center |
| 25 | status | Status | String | 10 | 90px | left |
| 26 | createdBy | Created By | String | 14 | 120px | left |
| 27 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 28 | updatedBy | Updated By | String | 14 | 120px | left |
| 29 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); productionOrderId (reference key, shown through productionOrderName); itemId (reference key, shown through itemName); productVariantId (reference key, shown through productVariantName); serialNumberId (reference key, shown through serialNumberName); bodyLotId (reference key, shown through bodyLotName); routingId (reference key, shown through routingName); currentOperationId (reference key, shown through currentOperationName); currentWorkCenterId (reference key, shown through currentWorkCenterName); qualityHoldId (reference key, shown through qualityHoldName); createdAtOperationId (reference key, shown through createdAtOperationName); lastOperationExecutionId (reference key, shown through lastOperationExecutionName); containerId (reference key, shown through containerName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_plan_wipUnitCompletedStep - WIP Unit Completed Steps (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_plan_wipUnitCompletedStep.json | _id: mes_plan_wipUnitCompletedStepStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1070px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | wipUnitName | WIP Unit | String | 12 | 110px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | completedStep | Completed Step | Int32 | 2 | 140px | right |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); wipUnitId (reference key, shown through wipUnitName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))
