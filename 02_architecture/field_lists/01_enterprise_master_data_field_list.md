# Field list - Master data (mdm)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/01_enterprise_master_data/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_mdm_enterprise

Kind: entity | Data class: master | Parent: - | _id pattern: ENT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | legalName | String |  |
| 7 | scope | String |  |
| 8 | parentEnterpriseId | String | u_mes_mdm_enterprise._id |
| 9 | parentEnterpriseName | String |  |
| 10 | cin | String |  |
| 11 | gstin | String |  |
| 12 | pan | String |  |
| 13 | industryCode | String |  |
| 14 | registeredAddressLine1 | String |  |
| 15 | registeredAddressLine2 | String |  |
| 16 | registeredAddressCity | String |  |
| 17 | registeredAddressState | String |  |
| 18 | registeredAddressPostalCode | String |  |
| 19 | registeredAddressCountry | String |  |
| 20 | baseCurrency | String |  |
| 21 | fiscalYearStartMonth | Int32 |  |
| 22 | website | String |  |
| 23 | status | String |  |
| 24 | schemaVersion | Int32 |  |

## u_mes_mdm_enterpriseContact

Kind: child | Data class: master | Parent: u_mes_mdm_enterprise | _id pattern: <enterpriseId>-C<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | enterpriseId | String | u_mes_mdm_enterprise._id |
| 6 | enterpriseName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | name | String |  |
| 9 | designation | String |  |
| 10 | email | String |  |
| 11 | phone | String |  |
| 12 | schemaVersion | Int32 |  |

## u_mes_mdm_site

Kind: entity | Data class: master | Parent: - | _id pattern: SITE-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | name | String |  |
| 4 | enterpriseId | String | u_mes_mdm_enterprise._id |
| 5 | enterpriseName | String |  |
| 6 | siteType | String |  |
| 7 | timezone | String |  |
| 8 | utcOffsetMinutes | Int32 |  |
| 9 | addressLine1 | String |  |
| 10 | addressLine2 | String |  |
| 11 | addressCity | String |  |
| 12 | addressDistrict | String |  |
| 13 | addressState | String |  |
| 14 | addressPostalCode | String |  |
| 15 | addressCountry | String |  |
| 16 | geoLatitude | Double |  |
| 17 | geoLongitude | Double |  |
| 18 | gstin | String |  |
| 19 | factoryLicenceNo | String |  |
| 20 | erpPlantCode | String |  |
| 21 | defaultWorkCalendarId | String | u_mes_mdm_workCalendar._id |
| 22 | defaultWorkCalendarName | String |  |
| 23 | currency | String |  |
| 24 | language | String |  |
| 25 | headcount | Int32 |  |
| 26 | status | String |  |
| 27 | schemaVersion | Int32 |  |

## u_mes_mdm_siteCertificate

Kind: child | Data class: master | Parent: u_mes_mdm_site | _id pattern: <siteId>-C<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | sequenceNo | Int32 |  |
| 6 | standard | String |  |
| 7 | certificateNo | String |  |
| 8 | issuedById | String | u_mes_mdm_user._id |
| 9 | issuedBy | String |  |
| 10 | validFrom | Date |  |
| 11 | validTo | Date |  |
| 12 | schemaVersion | Int32 |  |

## u_mes_mdm_area

Kind: entity | Data class: master | Parent: - | _id pattern: AR-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | areaType | String |  |
| 7 | parentAreaId | String | u_mes_mdm_area._id |
| 8 | parentAreaName | String |  |
| 9 | costCenter | String |  |
| 10 | supervisorUserId | String | u_mes_mdm_user._id |
| 11 | supervisorUserName | String |  |
| 12 | floorAreaSqm | Decimal128 |  |
| 13 | isProductionArea | Boolean |  |
| 14 | sequenceNo | Int32 |  |
| 15 | status | String |  |
| 16 | schemaVersion | Int32 |  |

## u_mes_mdm_line

Kind: entity | Data class: master | Parent: - | _id pattern: LN-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | areaId | String | u_mes_mdm_area._id |
| 7 | areaName | String |  |
| 8 | lineType | String |  |
| 9 | itemFamily | String |  |
| 10 | workCalendarId | String | u_mes_mdm_workCalendar._id |
| 11 | workCalendarName | String |  |
| 12 | taktTimeSec | Decimal128 |  |
| 13 | manningStandard | Int32 |  |
| 14 | bottleneckWorkCenterId | String | u_mes_mdm_workCenter._id |
| 15 | bottleneckWorkCenterName | String |  |
| 16 | oeeTarget | Decimal128 |  |
| 17 | costCenter | String |  |
| 18 | sequenceNo | Int32 |  |
| 19 | status | String |  |
| 20 | schemaVersion | Int32 |  |

## u_mes_mdm_lineDefaultShift

Kind: relationship | Data class: master | Parent: u_mes_mdm_line | _id pattern: <lineId>-DS<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | lineId | String | u_mes_mdm_line._id |
| 6 | lineName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | defaultShiftId | String | u_mes_mdm_shift._id |
| 9 | defaultShiftName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mdm_lineIdealRate

Kind: child | Data class: master | Parent: u_mes_mdm_line | _id pattern: <lineId>-IR<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | lineId | String | u_mes_mdm_line._id |
| 6 | lineName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | itemId | String | u_mes_prd_item._id |
| 9 | itemName | String |  |
| 10 | idealCycleTimeSec | Decimal128 |  |
| 11 | targetPerHour | Int32 |  |
| 12 | schemaVersion | Int32 |  |

## u_mes_mdm_workCenter

Kind: entity | Data class: master | Parent: - | _id pattern: WC-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | areaId | String | u_mes_mdm_area._id |
| 7 | areaName | String |  |
| 8 | lineId | String | u_mes_mdm_line._id |
| 9 | lineName | String |  |
| 10 | workCenterType | String |  |
| 11 | erpWorkCenterCode | String |  |
| 12 | costCenter | String |  |
| 13 | capacityPerShift | Int32 |  |
| 14 | standardManning | Int32 |  |
| 15 | trackingGrain | String |  |
| 16 | inputLocationId | String | u_mes_mat_storageLocation._id |
| 17 | inputLocationName | String |  |
| 18 | outputLocationId | String | u_mes_mat_storageLocation._id |
| 19 | outputLocationName | String |  |
| 20 | andonEnabled | Boolean |  |
| 21 | sequenceNo | Int32 |  |
| 22 | status | String |  |
| 23 | schemaVersion | Int32 |  |

## u_mes_mdm_workCenterEquipment

Kind: relationship | Data class: master | Parent: u_mes_mdm_workCenter | _id pattern: <workCenterId>-E<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workCenterId | String | u_mes_mdm_workCenter._id |
| 6 | workCenterName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | equipmentId | String | u_mes_mdm_equipment._id |
| 9 | equipmentName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mdm_workCenterOperation

Kind: relationship | Data class: master | Parent: u_mes_mdm_workCenter | _id pattern: <workCenterId>-O<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workCenterId | String | u_mes_mdm_workCenter._id |
| 6 | workCenterName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | operationId | String | u_mes_prd_operation._id |
| 9 | operationName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mdm_workCenterRequiresSkill

Kind: relationship | Data class: master | Parent: u_mes_mdm_workCenter | _id pattern: <workCenterId>-RS<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workCenterId | String | u_mes_mdm_workCenter._id |
| 6 | workCenterName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | requiresSkillId | String | u_mes_mdm_skill._id |
| 9 | requiresSkillName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mdm_equipment

Kind: entity | Data class: master | Parent: - | _id pattern: EQ-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | equipmentType | String |  |
| 7 | equipmentClass | String |  |
| 8 | lineId | String | u_mes_mdm_line._id |
| 9 | lineName | String |  |
| 10 | workCenterId | String | u_mes_mdm_workCenter._id |
| 11 | workCenterName | String |  |
| 12 | parentEquipmentId | String | u_mes_mdm_equipment._id |
| 13 | parentEquipmentName | String |  |
| 14 | manufacturer | String |  |
| 15 | model | String |  |
| 16 | serialNo | String |  |
| 17 | yearOfManufacture | Int32 |  |
| 18 | supplierId | String | u_mes_mdm_supplier._id |
| 19 | supplierName | String |  |
| 20 | assetNo | String |  |
| 21 | commissionedAt | Date |  |
| 22 | ratedCapacity | Decimal128 |  |
| 23 | ratedCapacityUnitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 24 | ratedCapacityUnitOfMeasureName | String |  |
| 25 | ratedPowerKw | Decimal128 |  |
| 26 | controllerMake | String |  |
| 27 | controllerModel | String |  |
| 28 | controllerIpAddress | String |  |
| 29 | controllerProtocol | String |  |
| 30 | criticality | String |  |
| 31 | currentState | String |  |
| 32 | currentStateSince | Date |  |
| 33 | lifetimeCycles | Int64 |  |
| 34 | lifetimeRunHours | Decimal128 |  |
| 35 | nextMaintenanceDueAt | Date |  |
| 36 | calibrationRequired | Boolean |  |
| 37 | safetyCategory | String |  |
| 38 | status | String |  |
| 39 | schemaVersion | Int32 |  |

## u_mes_mdm_equipmentIotDevice

Kind: relationship | Data class: master | Parent: u_mes_mdm_equipment | _id pattern: <equipmentId>-ID<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | equipmentId | String | u_mes_mdm_equipment._id |
| 6 | equipmentName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | iotDeviceId | String | u_mes_sys_iotDevice._id |
| 9 | iotDeviceName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mdm_shift

Kind: entity | Data class: master | Parent: - | _id pattern: SH-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | startTimeLocal | String |  |
| 7 | endTimeLocal | String |  |
| 8 | crossesMidnight | Boolean |  |
| 9 | durationMinutes | Int32 |  |
| 10 | plannedProductionMinutes | Int32 |  |
| 11 | shiftAllowancePerDay | Decimal128 |  |
| 12 | sequenceNo | Int32 |  |
| 13 | status | String |  |
| 14 | schemaVersion | Int32 |  |

## u_mes_mdm_shiftBreak

Kind: child | Data class: master | Parent: u_mes_mdm_shift | _id pattern: <shiftId>-B<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | shiftId | String | u_mes_mdm_shift._id |
| 6 | shiftName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | name | String |  |
| 9 | startTimeLocal | String |  |
| 10 | durationMinutes | Int32 |  |
| 11 | paid | Boolean |  |
| 12 | schemaVersion | Int32 |  |

## u_mes_mdm_shiftWorkingDay

Kind: valueList | Data class: master | Parent: u_mes_mdm_shift | _id pattern: <shiftId>-WD<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | shiftId | String | u_mes_mdm_shift._id |
| 6 | shiftName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | workingDay | String |  |
| 9 | schemaVersion | Int32 |  |

## u_mes_mdm_workCalendar

Kind: entity | Data class: master | Parent: - | _id pattern: CAL-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | year | Int32 |  |
| 7 | workingDaysCount | Int32 |  |
| 8 | validFrom | Date |  |
| 9 | validTo | Date |  |
| 10 | status | String |  |
| 11 | schemaVersion | Int32 |  |

## u_mes_mdm_workCalendarLine

Kind: relationship | Data class: master | Parent: u_mes_mdm_workCalendar | _id pattern: <workCalendarId>-L<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workCalendarId | String | u_mes_mdm_workCalendar._id |
| 6 | workCalendarName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | lineId | String | u_mes_mdm_line._id |
| 9 | lineName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mdm_workCalendarShift

Kind: relationship | Data class: master | Parent: u_mes_mdm_workCalendar | _id pattern: <workCalendarId>-S<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workCalendarId | String | u_mes_mdm_workCalendar._id |
| 6 | workCalendarName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | shiftId | String | u_mes_mdm_shift._id |
| 9 | shiftName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mdm_workCalendarWeeklyOffDay

Kind: valueList | Data class: master | Parent: u_mes_mdm_workCalendar | _id pattern: <workCalendarId>-WOD<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workCalendarId | String | u_mes_mdm_workCalendar._id |
| 6 | workCalendarName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | weeklyOffDay | String |  |
| 9 | schemaVersion | Int32 |  |

## u_mes_mdm_workCalendarException

Kind: child | Data class: master | Parent: u_mes_mdm_workCalendar | _id pattern: <workCalendarId>-E<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workCalendarId | String | u_mes_mdm_workCalendar._id |
| 6 | workCalendarName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | exceptionDate | Date |  |
| 9 | exceptionType | String |  |
| 10 | description | String |  |
| 11 | isWorking | Boolean |  |
| 12 | schemaVersion | Int32 |  |

## u_mes_mdm_workCalendarExceptionShift

Kind: relationship | Data class: master | Parent: u_mes_mdm_workCalendarException | _id pattern: <workCalendarExceptionId>-S<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | workCalendarExceptionId | String | u_mes_mdm_workCalendarException._id |
| 6 | workCalendarExceptionName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | shiftId | String | u_mes_mdm_shift._id |
| 9 | shiftName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mdm_shiftRoster

Kind: entity | Data class: transaction | Parent: - | _id pattern: ROS-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | productionDate | Date |  |
| 6 | shiftId | String | u_mes_mdm_shift._id |
| 7 | shiftName | String |  |
| 8 | lineId | String | u_mes_mdm_line._id |
| 9 | lineName | String |  |
| 10 | supervisorUserId | String | u_mes_mdm_user._id |
| 11 | supervisorUserName | String |  |
| 12 | plannedHeadcount | Int32 |  |
| 13 | actualHeadcount | Int32 |  |
| 14 | absentCount | Int32 |  |
| 15 | overtimeMinutes | Int32 |  |
| 16 | remarks | String |  |
| 17 | publishedAt | Date |  |
| 18 | status | String |  |
| 19 | schemaVersion | Int32 |  |
| 20 | createdAt | Date |  |
| 21 | createdById | String | u_mes_mdm_user._id |
| 22 | createdBy | String |  |
| 23 | updatedAt | Date |  |
| 24 | updatedById | String | u_mes_mdm_user._id |
| 25 | updatedBy | String |  |

## u_mes_mdm_shiftRosterAssignment

Kind: child | Data class: transaction | Parent: u_mes_mdm_shiftRoster | _id pattern: <shiftRosterId>-A<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | shiftRosterId | String | u_mes_mdm_shiftRoster._id |
| 6 | shiftRosterName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | userId | String | u_mes_mdm_user._id |
| 9 | userName | String |  |
| 10 | workCenterId | String | u_mes_mdm_workCenter._id |
| 11 | workCenterName | String |  |
| 12 | roleInCrew | String |  |
| 13 | attendance | String |  |
| 14 | replacedUserId | String | u_mes_mdm_user._id |
| 15 | replacedUserName | String |  |
| 16 | schemaVersion | Int32 |  |
| 17 | createdAt | Date |  |
| 18 | createdById | String | u_mes_mdm_user._id |
| 19 | createdBy | String |  |
| 20 | updatedAt | Date |  |
| 21 | updatedById | String | u_mes_mdm_user._id |
| 22 | updatedBy | String |  |

## u_mes_mdm_role

Kind: entity | Data class: master | Parent: - | _id pattern: ROLE-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | scope | String |  |
| 7 | description | String |  |
| 8 | canSign | Boolean |  |
| 9 | approvalLimitInr | Decimal128 |  |
| 10 | isSystemRole | Boolean |  |
| 11 | status | String |  |
| 12 | schemaVersion | Int32 |  |

## u_mes_mdm_rolePermission

Kind: valueList | Data class: master | Parent: u_mes_mdm_role | _id pattern: <roleId>-P<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | roleId | String | u_mes_mdm_role._id |
| 6 | roleName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | permission | String |  |
| 9 | schemaVersion | Int32 |  |

## u_mes_mdm_roleSignatureMeaning

Kind: valueList | Data class: master | Parent: u_mes_mdm_role | _id pattern: <roleId>-SM<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | roleId | String | u_mes_mdm_role._id |
| 6 | roleName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | signatureMeaning | String |  |
| 9 | schemaVersion | Int32 |  |

## u_mes_mdm_user

Kind: entity | Data class: master | Parent: - | _id pattern: USR-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | userName | String |  |
| 6 | fullName | String |  |
| 7 | userType | String |  |
| 8 | department | String |  |
| 9 | designation | String |  |
| 10 | badgeNo | String |  |
| 11 | email | String |  |
| 12 | mobile | String |  |
| 13 | defaultShiftId | String | u_mes_mdm_shift._id |
| 14 | defaultShiftName | String |  |
| 15 | homeWorkCenterId | String | u_mes_mdm_workCenter._id |
| 16 | homeWorkCenterName | String |  |
| 17 | reportsToUserId | String | u_mes_mdm_user._id |
| 18 | reportsToUserName | String |  |
| 19 | dateOfJoining | Date |  |
| 20 | employmentType | String |  |
| 21 | contractorSupplierId | String | u_mes_mdm_supplier._id |
| 22 | contractorSupplierName | String |  |
| 23 | language | String |  |
| 24 | lastLoginAt | Date |  |
| 25 | failedLoginCount | Int32 |  |
| 26 | passwordChangedAt | Date |  |
| 27 | isLocked | Boolean |  |
| 28 | status | String |  |
| 29 | schemaVersion | Int32 |  |

## u_mes_mdm_userRole

Kind: relationship | Data class: master | Parent: u_mes_mdm_user | _id pattern: <userId>-R<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | userId | String | u_mes_mdm_user._id |
| 6 | userName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | roleId | String | u_mes_mdm_role._id |
| 9 | roleName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mdm_skill

Kind: entity | Data class: master | Parent: - | _id pattern: SKL-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | skillCategory | String |  |
| 7 | description | String |  |
| 8 | minimumLevelRequired | Int32 |  |
| 9 | validityMonths | Int32 |  |
| 10 | trainingControlledDocumentId | String | u_mes_sys_controlledDocument._id |
| 11 | trainingControlledDocumentName | String |  |
| 12 | assessmentMethod | String |  |
| 13 | isSafetyCritical | Boolean |  |
| 14 | status | String |  |
| 15 | schemaVersion | Int32 |  |

## u_mes_mdm_skillOperation

Kind: relationship | Data class: master | Parent: u_mes_mdm_skill | _id pattern: <skillId>-O<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | skillId | String | u_mes_mdm_skill._id |
| 6 | skillName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | operationId | String | u_mes_prd_operation._id |
| 9 | operationName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mdm_skillLevelScale

Kind: child | Data class: master | Parent: u_mes_mdm_skill | _id pattern: <skillId>-LS<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | skillId | String | u_mes_mdm_skill._id |
| 6 | skillName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | level | Int32 |  |
| 9 | description | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mdm_skillCertification

Kind: entity | Data class: transaction | Parent: - | _id pattern: CERT-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | userId | String | u_mes_mdm_user._id |
| 6 | userName | String |  |
| 7 | skillId | String | u_mes_mdm_skill._id |
| 8 | skillName | String |  |
| 9 | level | Int32 |  |
| 10 | awardedAt | Date |  |
| 11 | validFrom | Date |  |
| 12 | validTo | Date |  |
| 13 | assessorUserId | String | u_mes_mdm_user._id |
| 14 | assessorUserName | String |  |
| 15 | assessmentScore | Decimal128 |  |
| 16 | assessmentMethod | String |  |
| 17 | trainingHours | Decimal128 |  |
| 18 | evidenceControlledDocumentId | String | u_mes_sys_controlledDocument._id |
| 19 | evidenceControlledDocumentName | String |  |
| 20 | restrictions | String |  |
| 21 | revokedAt | Date |  |
| 22 | revokedReason | String |  |
| 23 | nextReviewAt | Date |  |
| 24 | status | String |  |
| 25 | schemaVersion | Int32 |  |
| 26 | createdAt | Date |  |
| 27 | createdById | String | u_mes_mdm_user._id |
| 28 | createdBy | String |  |
| 29 | updatedAt | Date |  |
| 30 | updatedById | String | u_mes_mdm_user._id |
| 31 | updatedBy | String |  |

## u_mes_mdm_customer

Kind: entity | Data class: master | Parent: - | _id pattern: CUS-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | customerType | String |  |
| 7 | parentCustomerCode | String |  |
| 8 | gstin | String |  |
| 9 | billingAddressLine1 | String |  |
| 10 | billingAddressCity | String |  |
| 11 | billingAddressState | String |  |
| 12 | billingAddressPostalCode | String |  |
| 13 | billingAddressCountry | String |  |
| 14 | supplierCodeAtCustomer | String |  |
| 15 | labelTemplateId | String | u_mes_mat_labelTemplate._id |
| 16 | labelTemplateName | String |  |
| 17 | asnRequired | Boolean |  |
| 18 | ppapLevelDefault | Int32 |  |
| 19 | ppmTarget | Int32 |  |
| 20 | paymentTermsDays | Int32 |  |
| 21 | currency | String |  |
| 22 | portalUrl | String |  |
| 23 | status | String |  |
| 24 | schemaVersion | Int32 |  |

## u_mes_mdm_customerShipTo

Kind: child | Data class: master | Parent: u_mes_mdm_customer | _id pattern: <customerId>-ST<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | customerId | String | u_mes_mdm_customer._id |
| 6 | customerName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | shipToCode | String |  |
| 9 | name | String |  |
| 10 | line1 | String |  |
| 11 | city | String |  |
| 12 | state | String |  |
| 13 | postalCode | String |  |
| 14 | dockCode | String |  |
| 15 | transitDays | Int32 |  |
| 16 | schemaVersion | Int32 |  |

## u_mes_mdm_customerContact

Kind: child | Data class: master | Parent: u_mes_mdm_customer | _id pattern: <customerId>-C<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | customerId | String | u_mes_mdm_customer._id |
| 6 | customerName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | name | String |  |
| 9 | businessFunction | String |  |
| 10 | email | String |  |
| 11 | phone | String |  |
| 12 | schemaVersion | Int32 |  |

## u_mes_mdm_supplier

Kind: entity | Data class: master | Parent: - | _id pattern: SUP-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | supplierType | String |  |
| 7 | commodity | String |  |
| 8 | gstin | String |  |
| 9 | addressLine1 | String |  |
| 10 | addressCity | String |  |
| 11 | addressState | String |  |
| 12 | addressPostalCode | String |  |
| 13 | addressCountry | String |  |
| 14 | approvedAt | Date |  |
| 15 | ppmLast12Months | Int32 |  |
| 16 | deliveryRatingPct | Decimal128 |  |
| 17 | qualityRatingPct | Decimal128 |  |
| 18 | leadTimeDays | Int32 |  |
| 19 | paymentTermsDays | Int32 |  |
| 20 | currency | String |  |
| 21 | isDirectedSource | Boolean |  |
| 22 | status | String |  |
| 23 | schemaVersion | Int32 |  |

## u_mes_mdm_supplierContact

Kind: child | Data class: master | Parent: u_mes_mdm_supplier | _id pattern: <supplierId>-C<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | supplierId | String | u_mes_mdm_supplier._id |
| 6 | supplierName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | name | String |  |
| 9 | businessFunction | String |  |
| 10 | email | String |  |
| 11 | phone | String |  |
| 12 | schemaVersion | Int32 |  |

## u_mes_mdm_supplierCertificate

Kind: child | Data class: master | Parent: u_mes_mdm_supplier | _id pattern: <supplierId>-C2<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | supplierId | String | u_mes_mdm_supplier._id |
| 6 | supplierName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | standard | String |  |
| 9 | certificateNo | String |  |
| 10 | validTo | Date |  |
| 11 | schemaVersion | Int32 |  |

## u_mes_mdm_supplierSuppliedItem

Kind: relationship | Data class: master | Parent: u_mes_mdm_supplier | _id pattern: <supplierId>-SI<nnn>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | supplierId | String | u_mes_mdm_supplier._id |
| 6 | supplierName | String |  |
| 7 | sequenceNo | Int32 |  |
| 8 | suppliedItemId | String | u_mes_prd_item._id |
| 9 | suppliedItemName | String |  |
| 10 | schemaVersion | Int32 |  |

## u_mes_mdm_unitOfMeasure

Kind: entity | Data class: master | Parent: - | _id pattern: UOM-<recordNo>

| # | Key | BSON type | References |
|---|---|---|---|
| 1 | _id | String |  |
| 2 | recordNo | String |  |
| 3 | siteId | String | u_mes_mdm_site._id |
| 4 | siteName | String |  |
| 5 | name | String |  |
| 6 | scope | String |  |
| 7 | symbol | String |  |
| 8 | dimension | String |  |
| 9 | baseUnitOfMeasureId | String | u_mes_mdm_unitOfMeasure._id |
| 10 | baseUnitOfMeasureName | String |  |
| 11 | factorToBase | Decimal128 |  |
| 12 | offsetToBase | Decimal128 |  |
| 13 | decimalPlaces | Int32 |  |
| 14 | isoCode | String |  |
| 15 | isBaseUnit | Boolean |  |
| 16 | status | String |  |
| 17 | schemaVersion | Int32 |  |
