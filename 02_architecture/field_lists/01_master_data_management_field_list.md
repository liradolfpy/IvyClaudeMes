# Field list - Master Data Management (mast)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/01_master_data_management/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_mast_enterprise

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | legalName | String | - |  |
| 7 | scope | String | - |  |
| 8 | parentEnterpriseId | String | - | u_mes_mast_enterprise._id |
| 9 | parentEnterpriseName | String | - |  |
| 10 | cin | String | - |  |
| 11 | gstin | String | - |  |
| 12 | pan | String | - |  |
| 13 | industryCode | String | - |  |
| 14 | registeredAddressLine1 | String | - |  |
| 15 | registeredAddressLine2 | String | - |  |
| 16 | registeredAddressCity | String | - |  |
| 17 | registeredAddressState | String | - |  |
| 18 | registeredAddressPostalCode | String | - |  |
| 19 | registeredAddressCountryId | String | - | u_mes_mast_country._id |
| 20 | registeredAddressCountryName | String | - |  |
| 21 | baseCurrencyId | String | - | u_mes_mast_currency._id |
| 22 | baseCurrencyName | String | - |  |
| 23 | fiscalYearStartMonth | Int32 | - |  |
| 24 | website | String | - |  |
| 25 | status | String | - |  |
| 26 | schemaVersion | Int32 | - |  |

## u_mes_mast_enterpriseContact

Kind: child | Data class: master | Parent: u_mes_mast_enterprise | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | enterpriseId | String | - | u_mes_mast_enterprise._id |
| 6 | enterpriseName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | name | String | - |  |
| 9 | jobTitle | String | - |  |
| 10 | email | String | - |  |
| 11 | phone | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_site

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | name | String | - |  |
| 4 | enterpriseId | String | - | u_mes_mast_enterprise._id |
| 5 | enterpriseName | String | - |  |
| 6 | siteType | String | - |  |
| 7 | timezone | String | - |  |
| 8 | utcOffsetMinutes | Int32 | - |  |
| 9 | addressLine1 | String | - |  |
| 10 | addressLine2 | String | - |  |
| 11 | addressCity | String | - |  |
| 12 | addressDistrict | String | - |  |
| 13 | addressState | String | - |  |
| 14 | addressPostalCode | String | - |  |
| 15 | addressCountryId | String | - | u_mes_mast_country._id |
| 16 | addressCountryName | String | - |  |
| 17 | geoLatitude | Double | - |  |
| 18 | geoLongitude | Double | - |  |
| 19 | gstin | String | - |  |
| 20 | factoryLicenceNo | String | - |  |
| 21 | erpPlantCode | String | - |  |
| 22 | defaultWorkCalendarId | String | - | u_mes_mast_workCalendar._id |
| 23 | defaultWorkCalendarName | String | - |  |
| 24 | currencyId | String | - | u_mes_mast_currency._id |
| 25 | currencyName | String | - |  |
| 26 | languageId | String | - | u_mes_mast_language._id |
| 27 | languageName | String | - |  |
| 28 | headcount | Int32 | - |  |
| 29 | status | String | - |  |
| 30 | schemaVersion | Int32 | - |  |

## u_mes_mast_siteCertificate

Kind: child | Data class: master | Parent: u_mes_mast_site | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | sequenceNo | Int32 | - |  |
| 6 | standard | String | - |  |
| 7 | certificateNo | String | - |  |
| 8 | issuedById | String | - | u_mes_mast_user._id |
| 9 | issuedBy | String | - |  |
| 10 | validFrom | Date | Date |  |
| 11 | validTo | Date | Date |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_area

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | areaType | String | - |  |
| 7 | parentAreaId | String | - | u_mes_mast_area._id |
| 8 | parentAreaName | String | - |  |
| 9 | costCenterId | String | - | u_mes_mast_costCenter._id |
| 10 | costCenterName | String | - |  |
| 11 | supervisorUserId | String | - | u_mes_mast_user._id |
| 12 | supervisorUserName | String | - |  |
| 13 | floorAreaSqm | Decimal128 | - |  |
| 14 | isProductionArea | Boolean | - |  |
| 15 | sequenceNo | Int32 | - |  |
| 16 | cleanlinessClass | String | - |  |
| 17 | environmentallyMonitored | Boolean | - |  |
| 18 | gowningRequired | Boolean | - |  |
| 19 | status | String | - |  |
| 20 | schemaVersion | Int32 | - |  |

## u_mes_mast_line

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | areaId | String | - | u_mes_mast_area._id |
| 7 | areaName | String | - |  |
| 8 | lineType | String | - |  |
| 9 | itemFamilyId | String | - | u_mes_prod_itemFamily._id |
| 10 | itemFamilyName | String | - |  |
| 11 | workCalendarId | String | - | u_mes_mast_workCalendar._id |
| 12 | workCalendarName | String | - |  |
| 13 | taktTimeSec | Decimal128 | - |  |
| 14 | manningStandard | Int32 | - |  |
| 15 | bottleneckWorkCenterId | String | - | u_mes_mast_workCenter._id |
| 16 | bottleneckWorkCenterName | String | - |  |
| 17 | oeeTarget | Decimal128 | - |  |
| 18 | costCenterId | String | - | u_mes_mast_costCenter._id |
| 19 | costCenterName | String | - |  |
| 20 | sequenceNo | Int32 | - |  |
| 21 | status | String | - |  |
| 22 | schemaVersion | Int32 | - |  |

## u_mes_mast_lineDefaultShift

Kind: relationship | Data class: master | Parent: u_mes_mast_line | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | lineId | String | - | u_mes_mast_line._id |
| 6 | lineName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | defaultShiftId | String | - | u_mes_mast_shift._id |
| 9 | defaultShiftName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_lineIdealRate

Kind: child | Data class: master | Parent: u_mes_mast_line | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | lineId | String | - | u_mes_mast_line._id |
| 6 | lineName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | itemId | String | - | u_mes_prod_item._id |
| 9 | itemName | String | - |  |
| 10 | idealCycleTimeSec | Decimal128 | - |  |
| 11 | targetPerHour | Int32 | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCenter

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | areaId | String | - | u_mes_mast_area._id |
| 7 | areaName | String | - |  |
| 8 | lineId | String | - | u_mes_mast_line._id |
| 9 | lineName | String | - |  |
| 10 | workCenterType | String | - |  |
| 11 | erpWorkCenterCode | String | - |  |
| 12 | costCenterId | String | - | u_mes_mast_costCenter._id |
| 13 | costCenterName | String | - |  |
| 14 | capacityPerShift | Int32 | - |  |
| 15 | standardManning | Int32 | - |  |
| 16 | trackingGrain | String | - |  |
| 17 | inputLocationId | String | - | u_mes_matl_storageLocation._id |
| 18 | inputLocationName | String | - |  |
| 19 | outputLocationId | String | - | u_mes_matl_storageLocation._id |
| 20 | outputLocationName | String | - |  |
| 21 | andonEnabled | Boolean | - |  |
| 22 | sequenceNo | Int32 | - |  |
| 23 | status | String | - |  |
| 24 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCenterEquipment

Kind: relationship | Data class: master | Parent: u_mes_mast_workCenter | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 6 | workCenterName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | equipmentId | String | - | u_mes_mast_equipment._id |
| 9 | equipmentName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCenterOperation

Kind: relationship | Data class: master | Parent: u_mes_mast_workCenter | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 6 | workCenterName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | operationId | String | - | u_mes_prod_operation._id |
| 9 | operationName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCenterRequiresSkill

Kind: relationship | Data class: master | Parent: u_mes_mast_workCenter | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 6 | workCenterName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | requiresSkillId | String | - | u_mes_mast_skill._id |
| 9 | requiresSkillName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_equipment

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | equipmentTypeId | String | - | u_mes_mast_equipmentType._id |
| 7 | equipmentTypeName | String | - |  |
| 8 | equipmentClass | String | - |  |
| 9 | lineId | String | - | u_mes_mast_line._id |
| 10 | lineName | String | - |  |
| 11 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 12 | workCenterName | String | - |  |
| 13 | parentEquipmentId | String | - | u_mes_mast_equipment._id |
| 14 | parentEquipmentName | String | - |  |
| 15 | manufacturerId | String | - | u_mes_mast_manufacturer._id |
| 16 | manufacturerName | String | - |  |
| 17 | model | String | - |  |
| 18 | serialNo | String | - |  |
| 19 | yearOfManufacture | Int32 | - |  |
| 20 | supplierId | String | - | u_mes_mast_supplier._id |
| 21 | supplierName | String | - |  |
| 22 | assetNo | String | - |  |
| 23 | commissionedAt | Date | Datetime |  |
| 24 | ratedCapacity | Decimal128 | - |  |
| 25 | ratedCapacityUnitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 26 | ratedCapacityUnitOfMeasureName | String | - |  |
| 27 | ratedPowerKw | Decimal128 | - |  |
| 28 | controllerMake | String | - |  |
| 29 | controllerModel | String | - |  |
| 30 | controllerIpAddress | String | - |  |
| 31 | controllerProtocol | String | - |  |
| 32 | criticality | String | - |  |
| 33 | currentState | String | - |  |
| 34 | currentStateSince | Date | Datetime |  |
| 35 | lifetimeCycles | Int64 | - |  |
| 36 | lifetimeRunHours | Decimal128 | - |  |
| 37 | nextMaintenanceDueAt | Date | Date |  |
| 38 | calibrationRequired | Boolean | - |  |
| 39 | safetyCategory | String | - |  |
| 40 | isProductionReady | Boolean | - |  |
| 41 | readinessReasonText | String | - |  |
| 42 | healthScore | Decimal128 | - |  |
| 43 | healthScoreAt | Date | Datetime |  |
| 44 | acquisitionCostInr | Decimal128 | - |  |
| 45 | plannedReplacementDate | Date | Date |  |
| 46 | qualificationStatus | String | - |  |
| 47 | requalificationDueDate | Date | Date |  |
| 48 | cleanStatus | String | - |  |
| 49 | cleanHoldExpiresAt | Date | Datetime |  |
| 50 | lastCleaningRecordId | String | - | u_mes_maint_cleaningRecord._id |
| 51 | lastCleaningRecordName | String | - |  |
| 52 | status | String | - |  |
| 53 | schemaVersion | Int32 | - |  |

## u_mes_mast_equipmentIotDevice

Kind: relationship | Data class: master | Parent: u_mes_mast_equipment | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | equipmentId | String | - | u_mes_mast_equipment._id |
| 6 | equipmentName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | iotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 9 | iotDeviceName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_shift

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | startTimeLocal | String | - |  |
| 7 | endTimeLocal | String | - |  |
| 8 | crossesMidnight | Boolean | - |  |
| 9 | durationMinutes | Int32 | - |  |
| 10 | plannedProductionMinutes | Int32 | - |  |
| 11 | shiftAllowancePerDay | Decimal128 | - |  |
| 12 | sequenceNo | Int32 | - |  |
| 13 | status | String | - |  |
| 14 | schemaVersion | Int32 | - |  |

## u_mes_mast_shiftBreak

Kind: child | Data class: master | Parent: u_mes_mast_shift | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | shiftId | String | - | u_mes_mast_shift._id |
| 6 | shiftName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | name | String | - |  |
| 9 | startTimeLocal | String | - |  |
| 10 | durationMinutes | Int32 | - |  |
| 11 | paid | Boolean | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_shiftWorkingDay

Kind: valueList | Data class: master | Parent: u_mes_mast_shift | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | shiftId | String | - | u_mes_mast_shift._id |
| 6 | shiftName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | workingDay | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCalendar

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | year | Int32 | - |  |
| 7 | workingDaysCount | Int32 | - |  |
| 8 | validFrom | Date | Date |  |
| 9 | validTo | Date | Date |  |
| 10 | status | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCalendarLine

Kind: relationship | Data class: master | Parent: u_mes_mast_workCalendar | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workCalendarId | String | - | u_mes_mast_workCalendar._id |
| 6 | workCalendarName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | lineId | String | - | u_mes_mast_line._id |
| 9 | lineName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCalendarShift

Kind: relationship | Data class: master | Parent: u_mes_mast_workCalendar | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workCalendarId | String | - | u_mes_mast_workCalendar._id |
| 6 | workCalendarName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | shiftId | String | - | u_mes_mast_shift._id |
| 9 | shiftName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCalendarWeeklyOffDay

Kind: valueList | Data class: master | Parent: u_mes_mast_workCalendar | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workCalendarId | String | - | u_mes_mast_workCalendar._id |
| 6 | workCalendarName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | weeklyOffDay | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCalendarException

Kind: child | Data class: master | Parent: u_mes_mast_workCalendar | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workCalendarId | String | - | u_mes_mast_workCalendar._id |
| 6 | workCalendarName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | exceptionDate | Date | Date |  |
| 9 | exceptionType | String | - |  |
| 10 | description | String | - |  |
| 11 | isWorking | Boolean | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCalendarExceptionShift

Kind: relationship | Data class: master | Parent: u_mes_mast_workCalendarException | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | workCalendarExceptionId | String | - | u_mes_mast_workCalendarException._id |
| 6 | workCalendarExceptionName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | shiftId | String | - | u_mes_mast_shift._id |
| 9 | shiftName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_shiftRoster

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | productionDate | Date | Date |  |
| 6 | shiftId | String | - | u_mes_mast_shift._id |
| 7 | shiftName | String | - |  |
| 8 | lineId | String | - | u_mes_mast_line._id |
| 9 | lineName | String | - |  |
| 10 | supervisorUserId | String | - | u_mes_mast_user._id |
| 11 | supervisorUserName | String | - |  |
| 12 | plannedHeadcount | Int32 | - |  |
| 13 | actualHeadcount | Int32 | - |  |
| 14 | absentCount | Int32 | - |  |
| 15 | overtimeMinutes | Int32 | - |  |
| 16 | remarks | String | - |  |
| 17 | publishedAt | Date | Datetime |  |
| 18 | status | String | - |  |
| 19 | schemaVersion | Int32 | - |  |
| 20 | createdAt | Date | Datetime |  |
| 21 | createdById | String | - | u_mes_mast_user._id |
| 22 | createdBy | String | - |  |
| 23 | updatedAt | Date | Datetime |  |
| 24 | updatedById | String | - | u_mes_mast_user._id |
| 25 | updatedBy | String | - |  |

## u_mes_mast_shiftRosterAssignment

Kind: child | Data class: transaction | Parent: u_mes_mast_shiftRoster | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | shiftRosterId | String | - | u_mes_mast_shiftRoster._id |
| 6 | shiftRosterName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | userId | String | - | u_mes_mast_user._id |
| 9 | userName | String | - |  |
| 10 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 11 | workCenterName | String | - |  |
| 12 | roleInCrew | String | - |  |
| 13 | attendance | String | - |  |
| 14 | replacedUserId | String | - | u_mes_mast_user._id |
| 15 | replacedUserName | String | - |  |
| 16 | assignedFromAt | Date | Datetime |  |
| 17 | assignedToAt | Date | Datetime |  |
| 18 | assignmentSource | String | - |  |
| 19 | suggestionScore | Decimal128 | - |  |
| 20 | schemaVersion | Int32 | - |  |
| 21 | createdAt | Date | Datetime |  |
| 22 | createdById | String | - | u_mes_mast_user._id |
| 23 | createdBy | String | - |  |
| 24 | updatedAt | Date | Datetime |  |
| 25 | updatedById | String | - | u_mes_mast_user._id |
| 26 | updatedBy | String | - |  |

## u_mes_mast_role

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | scope | String | - |  |
| 7 | description | String | - |  |
| 8 | canSign | Boolean | - |  |
| 9 | approvalLimitInr | Decimal128 | - |  |
| 10 | isSystemRole | Boolean | - |  |
| 11 | status | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_rolePermission

Kind: relationship | Data class: master | Parent: u_mes_mast_role | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | roleId | String | - | u_mes_mast_role._id |
| 6 | roleName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | permissionId | String | - | u_mes_mast_permission._id |
| 9 | permissionName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_roleSignatureMeaning

Kind: relationship | Data class: master | Parent: u_mes_mast_role | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | roleId | String | - | u_mes_mast_role._id |
| 6 | roleName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | signatureMeaningId | String | - | u_mes_mast_signatureMeaning._id |
| 9 | signatureMeaningName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_user

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | userName | String | - |  |
| 6 | fullName | String | - |  |
| 7 | userType | String | - |  |
| 8 | departmentId | String | - | u_mes_mast_department._id |
| 9 | departmentName | String | - |  |
| 10 | designationId | String | - | u_mes_mast_designation._id |
| 11 | designationName | String | - |  |
| 12 | badgeNo | String | - |  |
| 13 | email | String | - |  |
| 14 | mobile | String | - |  |
| 15 | defaultShiftId | String | - | u_mes_mast_shift._id |
| 16 | defaultShiftName | String | - |  |
| 17 | homeWorkCenterId | String | - | u_mes_mast_workCenter._id |
| 18 | homeWorkCenterName | String | - |  |
| 19 | reportsToUserId | String | - | u_mes_mast_user._id |
| 20 | reportsToUserName | String | - |  |
| 21 | dateOfJoining | Date | Date |  |
| 22 | employmentTypeId | String | - | u_mes_mast_employmentType._id |
| 23 | employmentTypeName | String | - |  |
| 24 | contractorSupplierId | String | - | u_mes_mast_supplier._id |
| 25 | contractorSupplierName | String | - |  |
| 26 | languageId | String | - | u_mes_mast_language._id |
| 27 | languageName | String | - |  |
| 28 | lastLoginAt | Date | Datetime |  |
| 29 | failedLoginCount | Int32 | - |  |
| 30 | passwordChangedAt | Date | Datetime |  |
| 31 | isLocked | Boolean | - |  |
| 32 | lastAccessReviewDate | Date | Date |  |
| 33 | passwordExpiryDate | Date | Date |  |
| 34 | status | String | - |  |
| 35 | schemaVersion | Int32 | - |  |

## u_mes_mast_userRole

Kind: relationship | Data class: master | Parent: u_mes_mast_user | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | userId | String | - | u_mes_mast_user._id |
| 6 | userName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | roleId | String | - | u_mes_mast_role._id |
| 9 | roleName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_skill

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | skillCategoryId | String | - | u_mes_mast_skillCategory._id |
| 7 | skillCategoryName | String | - |  |
| 8 | description | String | - |  |
| 9 | minimumLevelRequired | Int32 | - |  |
| 10 | validityMonths | Int32 | - |  |
| 11 | trainingControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 12 | trainingControlledDocumentName | String | - |  |
| 13 | assessmentMethod | String | - |  |
| 14 | isSafetyCritical | Boolean | - |  |
| 15 | status | String | - |  |
| 16 | schemaVersion | Int32 | - |  |

## u_mes_mast_skillOperation

Kind: relationship | Data class: master | Parent: u_mes_mast_skill | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | skillId | String | - | u_mes_mast_skill._id |
| 6 | skillName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | operationId | String | - | u_mes_prod_operation._id |
| 9 | operationName | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_skillLevelScale

Kind: child | Data class: master | Parent: u_mes_mast_skill | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | skillId | String | - | u_mes_mast_skill._id |
| 6 | skillName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | level | Int32 | - |  |
| 9 | description | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_skillCertification

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | userId | String | - | u_mes_mast_user._id |
| 6 | userName | String | - |  |
| 7 | skillId | String | - | u_mes_mast_skill._id |
| 8 | skillName | String | - |  |
| 9 | level | Int32 | - |  |
| 10 | awardedAt | Date | Datetime |  |
| 11 | validFrom | Date | Date |  |
| 12 | validTo | Date | Date |  |
| 13 | assessorUserId | String | - | u_mes_mast_user._id |
| 14 | assessorUserName | String | - |  |
| 15 | assessmentScore | Decimal128 | - |  |
| 16 | assessmentMethod | String | - |  |
| 17 | trainingHours | Decimal128 | - |  |
| 18 | evidenceControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 19 | evidenceControlledDocumentName | String | - |  |
| 20 | restrictions | String | - |  |
| 21 | revokedAt | Date | Datetime |  |
| 22 | revokedReason | String | - |  |
| 23 | nextReviewAt | Date | Date |  |
| 24 | trainedDocumentRevision | String | - |  |
| 25 | requalificationRequired | Boolean | - |  |
| 26 | revocationSource | String | - |  |
| 27 | status | String | - |  |
| 28 | schemaVersion | Int32 | - |  |
| 29 | createdAt | Date | Datetime |  |
| 30 | createdById | String | - | u_mes_mast_user._id |
| 31 | createdBy | String | - |  |
| 32 | updatedAt | Date | Datetime |  |
| 33 | updatedById | String | - | u_mes_mast_user._id |
| 34 | updatedBy | String | - |  |

## u_mes_mast_customer

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | customerType | String | - |  |
| 7 | parentCustomerCode | String | - |  |
| 8 | gstin | String | - |  |
| 9 | billingAddressLine1 | String | - |  |
| 10 | billingAddressCity | String | - |  |
| 11 | billingAddressState | String | - |  |
| 12 | billingAddressPostalCode | String | - |  |
| 13 | billingAddressCountryId | String | - | u_mes_mast_country._id |
| 14 | billingAddressCountryName | String | - |  |
| 15 | supplierCodeAtCustomer | String | - |  |
| 16 | labelTemplateId | String | - | u_mes_matl_labelTemplate._id |
| 17 | labelTemplateName | String | - |  |
| 18 | asnRequired | Boolean | - |  |
| 19 | ppapLevelDefault | Int32 | - |  |
| 20 | ppmTarget | Int32 | - |  |
| 21 | paymentTermsDays | Int32 | - |  |
| 22 | currencyId | String | - | u_mes_mast_currency._id |
| 23 | currencyName | String | - |  |
| 24 | portalUrl | String | - |  |
| 25 | status | String | - |  |
| 26 | schemaVersion | Int32 | - |  |

## u_mes_mast_customerShipTo

Kind: child | Data class: master | Parent: u_mes_mast_customer | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | customerId | String | - | u_mes_mast_customer._id |
| 6 | customerName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | shipToCode | String | - |  |
| 9 | name | String | - |  |
| 10 | line1 | String | - |  |
| 11 | city | String | - |  |
| 12 | state | String | - |  |
| 13 | postalCode | String | - |  |
| 14 | dockCode | String | - |  |
| 15 | transitDays | Int32 | - |  |
| 16 | schemaVersion | Int32 | - |  |

## u_mes_mast_customerContact

Kind: child | Data class: master | Parent: u_mes_mast_customer | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | customerId | String | - | u_mes_mast_customer._id |
| 6 | customerName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | name | String | - |  |
| 9 | businessFunction | String | - |  |
| 10 | email | String | - |  |
| 11 | phone | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_supplier

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | supplierType | String | - |  |
| 7 | commodityId | String | - | u_mes_mast_commodity._id |
| 8 | commodityName | String | - |  |
| 9 | gstin | String | - |  |
| 10 | addressLine1 | String | - |  |
| 11 | addressCity | String | - |  |
| 12 | addressState | String | - |  |
| 13 | addressPostalCode | String | - |  |
| 14 | addressCountryId | String | - | u_mes_mast_country._id |
| 15 | addressCountryName | String | - |  |
| 16 | approvedAt | Date | Datetime |  |
| 17 | ppmLast12Months | Int32 | - |  |
| 18 | deliveryRatingPct | Decimal128 | - |  |
| 19 | qualityRatingPct | Decimal128 | - |  |
| 20 | leadTimeDays | Int32 | - |  |
| 21 | paymentTermsDays | Int32 | - |  |
| 22 | currencyId | String | - | u_mes_mast_currency._id |
| 23 | currencyName | String | - |  |
| 24 | isDirectedSource | Boolean | - |  |
| 25 | status | String | - |  |
| 26 | schemaVersion | Int32 | - |  |

## u_mes_mast_supplierContact

Kind: child | Data class: master | Parent: u_mes_mast_supplier | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | supplierId | String | - | u_mes_mast_supplier._id |
| 6 | supplierName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | name | String | - |  |
| 9 | businessFunction | String | - |  |
| 10 | email | String | - |  |
| 11 | phone | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_supplierCertificate

Kind: child | Data class: master | Parent: u_mes_mast_supplier | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | supplierId | String | - | u_mes_mast_supplier._id |
| 6 | supplierName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | standard | String | - |  |
| 9 | certificateNo | String | - |  |
| 10 | validTo | Date | Date |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_supplierSuppliedItem

Kind: relationship | Data class: master | Parent: u_mes_mast_supplier | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | supplierId | String | - | u_mes_mast_supplier._id |
| 6 | supplierName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | suppliedItemId | String | - | u_mes_prod_item._id |
| 9 | suppliedItemName | String | - |  |
| 10 | qualificationStatus | String | - |  |
| 11 | qualifiedUntilDate | Date | Date |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_unitOfMeasure

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | scope | String | - |  |
| 7 | symbol | String | - |  |
| 8 | dimension | String | - |  |
| 9 | baseUnitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 10 | baseUnitOfMeasureName | String | - |  |
| 11 | factorToBase | Decimal128 | - |  |
| 12 | offsetToBase | Decimal128 | - |  |
| 13 | decimalPlaces | Int32 | - |  |
| 14 | isoCode | String | - |  |
| 15 | isBaseUnit | Boolean | - |  |
| 16 | status | String | - |  |
| 17 | schemaVersion | Int32 | - |  |

## u_mes_mast_department

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | parentDepartmentId | String | - | u_mes_mast_department._id |
| 8 | parentDepartmentName | String | - |  |
| 9 | headUserId | String | - | u_mes_mast_user._id |
| 10 | headUserName | String | - |  |
| 11 | costCenterId | String | - | u_mes_mast_costCenter._id |
| 12 | costCenterName | String | - |  |
| 13 | sequenceNo | Int32 | - |  |
| 14 | status | String | - |  |
| 15 | schemaVersion | Int32 | - |  |

## u_mes_mast_designation

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | departmentId | String | - | u_mes_mast_department._id |
| 8 | departmentName | String | - |  |
| 9 | gradeLevel | Int32 | - |  |
| 10 | isSupervisory | Boolean | - |  |
| 11 | sequenceNo | Int32 | - |  |
| 12 | status | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_mast_employmentType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | isContract | Boolean | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | status | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_costCenter

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | erpCostCenterCode | String | - |  |
| 8 | validFrom | Date | Date |  |
| 9 | validTo | Date | Date |  |
| 10 | status | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_manufacturer

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | countryId | String | - | u_mes_mast_country._id |
| 8 | countryName | String | - |  |
| 9 | website | String | - |  |
| 10 | supportPhone | String | - |  |
| 11 | status | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_equipmentType

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | status | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_mast_skillCategory

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | status | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_mast_permission

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | resourceName | String | - |  |
| 8 | actionName | String | - |  |
| 9 | sequenceNo | Int32 | - |  |
| 10 | status | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_signatureMeaning

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | status | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_mast_currency

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | symbol | String | - |  |
| 7 | decimalPlaces | Int32 | - |  |
| 8 | isoNumericCode | String | - |  |
| 9 | sequenceNo | Int32 | - |  |
| 10 | status | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_country

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | isoAlpha3Code | String | - |  |
| 7 | dialCode | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | status | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_language

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | nativeName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | status | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_mast_transporter

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | gstin | String | - |  |
| 7 | phone | String | - |  |
| 8 | email | String | - |  |
| 9 | sequenceNo | Int32 | - |  |
| 10 | status | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_commodity

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | name | String | - |  |
| 6 | description | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | status | String | - |  |
| 9 | schemaVersion | Int32 | - |  |

## u_mes_mast_roleRequiredSkill

Kind: relationship | Data class: master | Parent: u_mes_mast_role | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | siteId | String | - | u_mes_mast_site._id |
| 4 | siteName | String | - |  |
| 5 | roleId | String | - | u_mes_mast_role._id |
| 6 | roleName | String | - |  |
| 7 | sequenceNo | Int32 | - |  |
| 8 | requiredSkillId | String | - | u_mes_mast_skill._id |
| 9 | requiredSkillName | String | - |  |
| 10 | minimumLevel | Int32 | - |  |
| 11 | schemaVersion | Int32 | - |  |
