# Field list - Master Data Management (mast)

Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/01_master_data_management/specs.

Shell constructors: String = "text"; Date = ISODate("YYYY-MM-DDTHH:mm:ss.sss+0000"); Int32 = NumberInt(n); Int64 = NumberLong("n"); Decimal128 = NumberDecimal("n.nn"); Double = Double(n); Boolean = true / false.

## u_mes_mast_enterprise

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | legalName | String | - |  |
| 8 | scope | String | - |  |
| 9 | parentEnterpriseId | String | - | u_mes_mast_enterprise._id |
| 10 | parentEnterpriseName | String | - |  |
| 11 | cin | String | - |  |
| 12 | gstin | String | - |  |
| 13 | pan | String | - |  |
| 14 | industryCode | String | - |  |
| 15 | registeredAddressLine1 | String | - |  |
| 16 | registeredAddressLine2 | String | - |  |
| 17 | registeredAddressCity | String | - |  |
| 18 | registeredAddressState | String | - |  |
| 19 | registeredAddressPostalCode | String | - |  |
| 20 | registeredAddressCountryId | String | - | u_mes_mast_country._id |
| 21 | registeredAddressCountryName | String | - |  |
| 22 | baseCurrencyId | String | - | u_mes_mast_currency._id |
| 23 | baseCurrencyName | String | - |  |
| 24 | fiscalYearStartMonth | Int32 | - |  |
| 25 | website | String | - |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |

## u_mes_mast_enterpriseContact

Kind: child | Data class: master | Parent: u_mes_mast_enterprise | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | enterpriseId | String | - | u_mes_mast_enterprise._id |
| 7 | enterpriseName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | name | String | - |  |
| 10 | jobTitle | String | - |  |
| 11 | email | String | - |  |
| 12 | phone | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_mast_site

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | name | String | - |  |
| 5 | enterpriseId | String | - | u_mes_mast_enterprise._id |
| 6 | enterpriseName | String | - |  |
| 7 | siteType | String | - |  |
| 8 | timezone | String | - |  |
| 9 | utcOffsetMinutes | Int32 | - |  |
| 10 | addressLine1 | String | - |  |
| 11 | addressLine2 | String | - |  |
| 12 | addressCity | String | - |  |
| 13 | addressDistrict | String | - |  |
| 14 | addressState | String | - |  |
| 15 | addressPostalCode | String | - |  |
| 16 | addressCountryId | String | - | u_mes_mast_country._id |
| 17 | addressCountryName | String | - |  |
| 18 | geoLatitude | Double | - |  |
| 19 | geoLongitude | Double | - |  |
| 20 | gstin | String | - |  |
| 21 | factoryLicenceNo | String | - |  |
| 22 | erpPlantCode | String | - |  |
| 23 | defaultWorkCalendarId | String | - | u_mes_mast_workCalendar._id |
| 24 | defaultWorkCalendarName | String | - |  |
| 25 | currencyId | String | - | u_mes_mast_currency._id |
| 26 | currencyName | String | - |  |
| 27 | languageId | String | - | u_mes_mast_language._id |
| 28 | languageName | String | - |  |
| 29 | headcount | Int32 | - |  |
| 30 | status | String | - |  |
| 31 | schemaVersion | Int32 | - |  |

## u_mes_mast_siteCertificate

Kind: child | Data class: master | Parent: u_mes_mast_site | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | sequenceNo | Int32 | - |  |
| 7 | standard | String | - |  |
| 8 | certificateNo | String | - |  |
| 9 | issuedById | String | - | u_mes_mast_user._id |
| 10 | issuedBy | String | - |  |
| 11 | validFrom | Date | Date |  |
| 12 | validTo | Date | Date |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_mast_area

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | areaType | String | - |  |
| 8 | parentAreaId | String | - | u_mes_mast_area._id |
| 9 | parentAreaName | String | - |  |
| 10 | costCenterId | String | - | u_mes_mast_costCenter._id |
| 11 | costCenterName | String | - |  |
| 12 | supervisorUserId | String | - | u_mes_mast_user._id |
| 13 | supervisorUserName | String | - |  |
| 14 | floorAreaSqm | Decimal128 | - |  |
| 15 | isProductionArea | Boolean | - |  |
| 16 | sequenceNo | Int32 | - |  |
| 17 | cleanlinessClass | String | - |  |
| 18 | environmentallyMonitored | Boolean | - |  |
| 19 | gowningRequired | Boolean | - |  |
| 20 | status | String | - |  |
| 21 | schemaVersion | Int32 | - |  |

## u_mes_mast_line

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | areaId | String | - | u_mes_mast_area._id |
| 8 | areaName | String | - |  |
| 9 | lineType | String | - |  |
| 10 | itemFamilyId | String | - | u_mes_prod_itemFamily._id |
| 11 | itemFamilyName | String | - |  |
| 12 | workCalendarId | String | - | u_mes_mast_workCalendar._id |
| 13 | workCalendarName | String | - |  |
| 14 | taktTimeSec | Decimal128 | - |  |
| 15 | manningStandard | Int32 | - |  |
| 16 | bottleneckWorkCenterId | String | - | u_mes_mast_workCenter._id |
| 17 | bottleneckWorkCenterName | String | - |  |
| 18 | oeeTarget | Decimal128 | - |  |
| 19 | costCenterId | String | - | u_mes_mast_costCenter._id |
| 20 | costCenterName | String | - |  |
| 21 | sequenceNo | Int32 | - |  |
| 22 | status | String | - |  |
| 23 | schemaVersion | Int32 | - |  |

## u_mes_mast_lineDefaultShift

Kind: relationship | Data class: master | Parent: u_mes_mast_line | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | lineId | String | - | u_mes_mast_line._id |
| 7 | lineName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | defaultShiftId | String | - | u_mes_mast_shift._id |
| 10 | defaultShiftName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_lineIdealRate

Kind: child | Data class: master | Parent: u_mes_mast_line | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | lineId | String | - | u_mes_mast_line._id |
| 7 | lineName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | itemId | String | - | u_mes_prod_item._id |
| 10 | itemName | String | - |  |
| 11 | idealCycleTimeSec | Decimal128 | - |  |
| 12 | targetPerHour | Int32 | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCenter

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | areaId | String | - | u_mes_mast_area._id |
| 8 | areaName | String | - |  |
| 9 | lineId | String | - | u_mes_mast_line._id |
| 10 | lineName | String | - |  |
| 11 | workCenterType | String | - |  |
| 12 | erpWorkCenterCode | String | - |  |
| 13 | costCenterId | String | - | u_mes_mast_costCenter._id |
| 14 | costCenterName | String | - |  |
| 15 | capacityPerShift | Int32 | - |  |
| 16 | standardManning | Int32 | - |  |
| 17 | trackingGrain | String | - |  |
| 18 | inputLocationId | String | - | u_mes_matl_storageLocation._id |
| 19 | inputLocationName | String | - |  |
| 20 | outputLocationId | String | - | u_mes_matl_storageLocation._id |
| 21 | outputLocationName | String | - |  |
| 22 | andonEnabled | Boolean | - |  |
| 23 | sequenceNo | Int32 | - |  |
| 24 | status | String | - |  |
| 25 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCenterEquipment

Kind: relationship | Data class: master | Parent: u_mes_mast_workCenter | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 7 | workCenterName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | equipmentId | String | - | u_mes_mast_equipment._id |
| 10 | equipmentName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCenterOperation

Kind: relationship | Data class: master | Parent: u_mes_mast_workCenter | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 7 | workCenterName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | operationId | String | - | u_mes_prod_operation._id |
| 10 | operationName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCenterRequiresSkill

Kind: relationship | Data class: master | Parent: u_mes_mast_workCenter | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 7 | workCenterName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | requiresSkillId | String | - | u_mes_mast_skill._id |
| 10 | requiresSkillName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_equipment

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | equipmentTypeId | String | - | u_mes_mast_equipmentType._id |
| 8 | equipmentTypeName | String | - |  |
| 9 | equipmentClass | String | - |  |
| 10 | lineId | String | - | u_mes_mast_line._id |
| 11 | lineName | String | - |  |
| 12 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 13 | workCenterName | String | - |  |
| 14 | parentEquipmentId | String | - | u_mes_mast_equipment._id |
| 15 | parentEquipmentName | String | - |  |
| 16 | manufacturerId | String | - | u_mes_mast_manufacturer._id |
| 17 | manufacturerName | String | - |  |
| 18 | model | String | - |  |
| 19 | serialNo | String | - |  |
| 20 | yearOfManufacture | Int32 | - |  |
| 21 | supplierId | String | - | u_mes_mast_supplier._id |
| 22 | supplierName | String | - |  |
| 23 | assetNo | String | - |  |
| 24 | commissionedAt | Date | Datetime |  |
| 25 | ratedCapacity | Decimal128 | - |  |
| 26 | ratedCapacityUnitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 27 | ratedCapacityUnitOfMeasureName | String | - |  |
| 28 | ratedPowerKw | Decimal128 | - |  |
| 29 | controllerMake | String | - |  |
| 30 | controllerModel | String | - |  |
| 31 | controllerIpAddress | String | - |  |
| 32 | controllerProtocol | String | - |  |
| 33 | criticality | String | - |  |
| 34 | currentState | String | - |  |
| 35 | currentStateSince | Date | Datetime |  |
| 36 | lifetimeCycles | Int64 | - |  |
| 37 | lifetimeRunHours | Decimal128 | - |  |
| 38 | nextMaintenanceDueAt | Date | Date |  |
| 39 | calibrationRequired | Boolean | - |  |
| 40 | safetyCategory | String | - |  |
| 41 | isProductionReady | Boolean | - |  |
| 42 | readinessReasonText | String | - |  |
| 43 | healthScore | Decimal128 | - |  |
| 44 | healthScoreAt | Date | Datetime |  |
| 45 | acquisitionCostInr | Decimal128 | - |  |
| 46 | plannedReplacementDate | Date | Date |  |
| 47 | qualificationStatus | String | - |  |
| 48 | requalificationDueDate | Date | Date |  |
| 49 | cleanStatus | String | - |  |
| 50 | cleanHoldExpiresAt | Date | Datetime |  |
| 51 | lastCleaningRecordId | String | - | u_mes_maint_cleaningRecord._id |
| 52 | lastCleaningRecordName | String | - |  |
| 53 | status | String | - |  |
| 54 | schemaVersion | Int32 | - |  |

## u_mes_mast_equipmentIotDevice

Kind: relationship | Data class: master | Parent: u_mes_mast_equipment | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | equipmentId | String | - | u_mes_mast_equipment._id |
| 7 | equipmentName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | iotDeviceId | String | - | u_mes_syst_iotDevice._id |
| 10 | iotDeviceName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_shift

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | startTimeLocal | String | - |  |
| 8 | endTimeLocal | String | - |  |
| 9 | crossesMidnight | Boolean | - |  |
| 10 | durationMinutes | Int32 | - |  |
| 11 | plannedProductionMinutes | Int32 | - |  |
| 12 | shiftAllowancePerDay | Decimal128 | - |  |
| 13 | sequenceNo | Int32 | - |  |
| 14 | status | String | - |  |
| 15 | schemaVersion | Int32 | - |  |

## u_mes_mast_shiftBreak

Kind: child | Data class: master | Parent: u_mes_mast_shift | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | shiftId | String | - | u_mes_mast_shift._id |
| 7 | shiftName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | name | String | - |  |
| 10 | startTimeLocal | String | - |  |
| 11 | durationMinutes | Int32 | - |  |
| 12 | paid | Boolean | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_mast_shiftWorkingDay

Kind: valueList | Data class: master | Parent: u_mes_mast_shift | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | shiftId | String | - | u_mes_mast_shift._id |
| 7 | shiftName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | workingDay | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCalendar

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | year | Int32 | - |  |
| 8 | workingDaysCount | Int32 | - |  |
| 9 | validFrom | Date | Date |  |
| 10 | validTo | Date | Date |  |
| 11 | status | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCalendarLine

Kind: relationship | Data class: master | Parent: u_mes_mast_workCalendar | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workCalendarId | String | - | u_mes_mast_workCalendar._id |
| 7 | workCalendarName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | lineId | String | - | u_mes_mast_line._id |
| 10 | lineName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCalendarShift

Kind: relationship | Data class: master | Parent: u_mes_mast_workCalendar | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workCalendarId | String | - | u_mes_mast_workCalendar._id |
| 7 | workCalendarName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | shiftId | String | - | u_mes_mast_shift._id |
| 10 | shiftName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCalendarWeeklyOffDay

Kind: valueList | Data class: master | Parent: u_mes_mast_workCalendar | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workCalendarId | String | - | u_mes_mast_workCalendar._id |
| 7 | workCalendarName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | weeklyOffDay | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCalendarException

Kind: child | Data class: master | Parent: u_mes_mast_workCalendar | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workCalendarId | String | - | u_mes_mast_workCalendar._id |
| 7 | workCalendarName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | exceptionDate | Date | Date |  |
| 10 | exceptionType | String | - |  |
| 11 | description | String | - |  |
| 12 | isWorking | Boolean | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_mast_workCalendarExceptionShift

Kind: relationship | Data class: master | Parent: u_mes_mast_workCalendarException | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | workCalendarExceptionId | String | - | u_mes_mast_workCalendarException._id |
| 7 | workCalendarExceptionName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | shiftId | String | - | u_mes_mast_shift._id |
| 10 | shiftName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_shiftRoster

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | productionDate | Date | Date |  |
| 7 | shiftId | String | - | u_mes_mast_shift._id |
| 8 | shiftName | String | - |  |
| 9 | lineId | String | - | u_mes_mast_line._id |
| 10 | lineName | String | - |  |
| 11 | supervisorUserId | String | - | u_mes_mast_user._id |
| 12 | supervisorUserName | String | - |  |
| 13 | plannedHeadcount | Int32 | - |  |
| 14 | actualHeadcount | Int32 | - |  |
| 15 | absentCount | Int32 | - |  |
| 16 | overtimeMinutes | Int32 | - |  |
| 17 | remarks | String | - |  |
| 18 | publishedAt | Date | Datetime |  |
| 19 | status | String | - |  |
| 20 | schemaVersion | Int32 | - |  |
| 21 | createdAt | Date | Datetime |  |
| 22 | createdById | String | - | u_mes_mast_user._id |
| 23 | createdBy | String | - |  |
| 24 | updatedAt | Date | Datetime |  |
| 25 | updatedById | String | - | u_mes_mast_user._id |
| 26 | updatedBy | String | - |  |

## u_mes_mast_shiftRosterAssignment

Kind: child | Data class: transaction | Parent: u_mes_mast_shiftRoster | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | shiftRosterId | String | - | u_mes_mast_shiftRoster._id |
| 7 | shiftRosterName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | userId | String | - | u_mes_mast_user._id |
| 10 | userName | String | - |  |
| 11 | workCenterId | String | - | u_mes_mast_workCenter._id |
| 12 | workCenterName | String | - |  |
| 13 | roleInCrew | String | - |  |
| 14 | attendance | String | - |  |
| 15 | replacedUserId | String | - | u_mes_mast_user._id |
| 16 | replacedUserName | String | - |  |
| 17 | assignedFromAt | Date | Datetime |  |
| 18 | assignedToAt | Date | Datetime |  |
| 19 | assignmentSource | String | - |  |
| 20 | suggestionScore | Decimal128 | - |  |
| 21 | schemaVersion | Int32 | - |  |
| 22 | createdAt | Date | Datetime |  |
| 23 | createdById | String | - | u_mes_mast_user._id |
| 24 | createdBy | String | - |  |
| 25 | updatedAt | Date | Datetime |  |
| 26 | updatedById | String | - | u_mes_mast_user._id |
| 27 | updatedBy | String | - |  |

## u_mes_mast_role

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | scope | String | - |  |
| 8 | description | String | - |  |
| 9 | canSign | Boolean | - |  |
| 10 | approvalLimitInr | Decimal128 | - |  |
| 11 | isSystemRole | Boolean | - |  |
| 12 | status | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_mast_rolePermission

Kind: relationship | Data class: master | Parent: u_mes_mast_role | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | roleId | String | - | u_mes_mast_role._id |
| 7 | roleName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | permissionId | String | - | u_mes_mast_permission._id |
| 10 | permissionName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_roleSignatureMeaning

Kind: relationship | Data class: master | Parent: u_mes_mast_role | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | roleId | String | - | u_mes_mast_role._id |
| 7 | roleName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | signatureMeaningId | String | - | u_mes_mast_signatureMeaning._id |
| 10 | signatureMeaningName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_user

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | userName | String | - |  |
| 7 | fullName | String | - |  |
| 8 | userType | String | - |  |
| 9 | departmentId | String | - | u_mes_mast_department._id |
| 10 | departmentName | String | - |  |
| 11 | designationId | String | - | u_mes_mast_designation._id |
| 12 | designationName | String | - |  |
| 13 | badgeNo | String | - |  |
| 14 | email | String | - |  |
| 15 | mobile | String | - |  |
| 16 | defaultShiftId | String | - | u_mes_mast_shift._id |
| 17 | defaultShiftName | String | - |  |
| 18 | homeWorkCenterId | String | - | u_mes_mast_workCenter._id |
| 19 | homeWorkCenterName | String | - |  |
| 20 | reportsToUserId | String | - | u_mes_mast_user._id |
| 21 | reportsToUserName | String | - |  |
| 22 | dateOfJoining | Date | Date |  |
| 23 | employmentTypeId | String | - | u_mes_mast_employmentType._id |
| 24 | employmentTypeName | String | - |  |
| 25 | contractorSupplierId | String | - | u_mes_mast_supplier._id |
| 26 | contractorSupplierName | String | - |  |
| 27 | languageId | String | - | u_mes_mast_language._id |
| 28 | languageName | String | - |  |
| 29 | lastLoginAt | Date | Datetime |  |
| 30 | failedLoginCount | Int32 | - |  |
| 31 | passwordChangedAt | Date | Datetime |  |
| 32 | isLocked | Boolean | - |  |
| 33 | lastAccessReviewDate | Date | Date |  |
| 34 | passwordExpiryDate | Date | Date |  |
| 35 | status | String | - |  |
| 36 | schemaVersion | Int32 | - |  |

## u_mes_mast_userRole

Kind: relationship | Data class: master | Parent: u_mes_mast_user | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | userId | String | - | u_mes_mast_user._id |
| 7 | userName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | roleId | String | - | u_mes_mast_role._id |
| 10 | roleName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_skill

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | skillCategoryId | String | - | u_mes_mast_skillCategory._id |
| 8 | skillCategoryName | String | - |  |
| 9 | description | String | - |  |
| 10 | minimumLevelRequired | Int32 | - |  |
| 11 | validityMonths | Int32 | - |  |
| 12 | trainingControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 13 | trainingControlledDocumentName | String | - |  |
| 14 | assessmentMethod | String | - |  |
| 15 | isSafetyCritical | Boolean | - |  |
| 16 | status | String | - |  |
| 17 | schemaVersion | Int32 | - |  |

## u_mes_mast_skillOperation

Kind: relationship | Data class: master | Parent: u_mes_mast_skill | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | skillId | String | - | u_mes_mast_skill._id |
| 7 | skillName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | operationId | String | - | u_mes_prod_operation._id |
| 10 | operationName | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_skillLevelScale

Kind: child | Data class: master | Parent: u_mes_mast_skill | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | skillId | String | - | u_mes_mast_skill._id |
| 7 | skillName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | level | Int32 | - |  |
| 10 | description | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_skillCertification

Kind: entity | Data class: transaction | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | userId | String | - | u_mes_mast_user._id |
| 7 | userName | String | - |  |
| 8 | skillId | String | - | u_mes_mast_skill._id |
| 9 | skillName | String | - |  |
| 10 | level | Int32 | - |  |
| 11 | awardedAt | Date | Datetime |  |
| 12 | validFrom | Date | Date |  |
| 13 | validTo | Date | Date |  |
| 14 | assessorUserId | String | - | u_mes_mast_user._id |
| 15 | assessorUserName | String | - |  |
| 16 | assessmentScore | Decimal128 | - |  |
| 17 | assessmentMethod | String | - |  |
| 18 | trainingHours | Decimal128 | - |  |
| 19 | evidenceControlledDocumentId | String | - | u_mes_syst_controlledDocument._id |
| 20 | evidenceControlledDocumentName | String | - |  |
| 21 | restrictions | String | - |  |
| 22 | revokedAt | Date | Datetime |  |
| 23 | revokedReason | String | - |  |
| 24 | nextReviewAt | Date | Date |  |
| 25 | trainedDocumentRevision | String | - |  |
| 26 | requalificationRequired | Boolean | - |  |
| 27 | revocationSource | String | - |  |
| 28 | status | String | - |  |
| 29 | schemaVersion | Int32 | - |  |
| 30 | createdAt | Date | Datetime |  |
| 31 | createdById | String | - | u_mes_mast_user._id |
| 32 | createdBy | String | - |  |
| 33 | updatedAt | Date | Datetime |  |
| 34 | updatedById | String | - | u_mes_mast_user._id |
| 35 | updatedBy | String | - |  |

## u_mes_mast_customer

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | customerType | String | - |  |
| 8 | parentCustomerCode | String | - |  |
| 9 | gstin | String | - |  |
| 10 | billingAddressLine1 | String | - |  |
| 11 | billingAddressCity | String | - |  |
| 12 | billingAddressState | String | - |  |
| 13 | billingAddressPostalCode | String | - |  |
| 14 | billingAddressCountryId | String | - | u_mes_mast_country._id |
| 15 | billingAddressCountryName | String | - |  |
| 16 | supplierCodeAtCustomer | String | - |  |
| 17 | labelTemplateId | String | - | u_mes_matl_labelTemplate._id |
| 18 | labelTemplateName | String | - |  |
| 19 | asnRequired | Boolean | - |  |
| 20 | ppapLevelDefault | Int32 | - |  |
| 21 | ppmTarget | Int32 | - |  |
| 22 | paymentTermsDays | Int32 | - |  |
| 23 | currencyId | String | - | u_mes_mast_currency._id |
| 24 | currencyName | String | - |  |
| 25 | portalUrl | String | - |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |

## u_mes_mast_customerShipTo

Kind: child | Data class: master | Parent: u_mes_mast_customer | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | customerId | String | - | u_mes_mast_customer._id |
| 7 | customerName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | shipToCode | String | - |  |
| 10 | name | String | - |  |
| 11 | line1 | String | - |  |
| 12 | city | String | - |  |
| 13 | state | String | - |  |
| 14 | postalCode | String | - |  |
| 15 | dockCode | String | - |  |
| 16 | transitDays | Int32 | - |  |
| 17 | schemaVersion | Int32 | - |  |

## u_mes_mast_customerContact

Kind: child | Data class: master | Parent: u_mes_mast_customer | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | customerId | String | - | u_mes_mast_customer._id |
| 7 | customerName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | name | String | - |  |
| 10 | businessFunction | String | - |  |
| 11 | email | String | - |  |
| 12 | phone | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_mast_supplier

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | supplierType | String | - |  |
| 8 | commodityId | String | - | u_mes_mast_commodity._id |
| 9 | commodityName | String | - |  |
| 10 | gstin | String | - |  |
| 11 | addressLine1 | String | - |  |
| 12 | addressCity | String | - |  |
| 13 | addressState | String | - |  |
| 14 | addressPostalCode | String | - |  |
| 15 | addressCountryId | String | - | u_mes_mast_country._id |
| 16 | addressCountryName | String | - |  |
| 17 | approvedAt | Date | Datetime |  |
| 18 | ppmLast12Months | Int32 | - |  |
| 19 | deliveryRatingPct | Decimal128 | - |  |
| 20 | qualityRatingPct | Decimal128 | - |  |
| 21 | leadTimeDays | Int32 | - |  |
| 22 | paymentTermsDays | Int32 | - |  |
| 23 | currencyId | String | - | u_mes_mast_currency._id |
| 24 | currencyName | String | - |  |
| 25 | isDirectedSource | Boolean | - |  |
| 26 | status | String | - |  |
| 27 | schemaVersion | Int32 | - |  |

## u_mes_mast_supplierContact

Kind: child | Data class: master | Parent: u_mes_mast_supplier | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | supplierId | String | - | u_mes_mast_supplier._id |
| 7 | supplierName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | name | String | - |  |
| 10 | businessFunction | String | - |  |
| 11 | email | String | - |  |
| 12 | phone | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_mast_supplierCertificate

Kind: child | Data class: master | Parent: u_mes_mast_supplier | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | supplierId | String | - | u_mes_mast_supplier._id |
| 7 | supplierName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | standard | String | - |  |
| 10 | certificateNo | String | - |  |
| 11 | validTo | Date | Date |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_supplierSuppliedItem

Kind: relationship | Data class: master | Parent: u_mes_mast_supplier | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | supplierId | String | - | u_mes_mast_supplier._id |
| 7 | supplierName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | suppliedItemId | String | - | u_mes_prod_item._id |
| 10 | suppliedItemName | String | - |  |
| 11 | qualificationStatus | String | - |  |
| 12 | qualifiedUntilDate | Date | Date |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_mast_unitOfMeasure

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | scope | String | - |  |
| 8 | symbol | String | - |  |
| 9 | dimension | String | - |  |
| 10 | baseUnitOfMeasureId | String | - | u_mes_mast_unitOfMeasure._id |
| 11 | baseUnitOfMeasureName | String | - |  |
| 12 | factorToBase | Decimal128 | - |  |
| 13 | offsetToBase | Decimal128 | - |  |
| 14 | decimalPlaces | Int32 | - |  |
| 15 | isoCode | String | - |  |
| 16 | isBaseUnit | Boolean | - |  |
| 17 | status | String | - |  |
| 18 | schemaVersion | Int32 | - |  |

## u_mes_mast_department

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
| 8 | parentDepartmentId | String | - | u_mes_mast_department._id |
| 9 | parentDepartmentName | String | - |  |
| 10 | headUserId | String | - | u_mes_mast_user._id |
| 11 | headUserName | String | - |  |
| 12 | costCenterId | String | - | u_mes_mast_costCenter._id |
| 13 | costCenterName | String | - |  |
| 14 | sequenceNo | Int32 | - |  |
| 15 | status | String | - |  |
| 16 | schemaVersion | Int32 | - |  |

## u_mes_mast_designation

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
| 8 | departmentId | String | - | u_mes_mast_department._id |
| 9 | departmentName | String | - |  |
| 10 | gradeLevel | Int32 | - |  |
| 11 | isSupervisory | Boolean | - |  |
| 12 | sequenceNo | Int32 | - |  |
| 13 | status | String | - |  |
| 14 | schemaVersion | Int32 | - |  |

## u_mes_mast_employmentType

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
| 8 | isContract | Boolean | - |  |
| 9 | sequenceNo | Int32 | - |  |
| 10 | status | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_costCenter

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
| 8 | erpCostCenterCode | String | - |  |
| 9 | validFrom | Date | Date |  |
| 10 | validTo | Date | Date |  |
| 11 | status | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_manufacturer

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
| 8 | countryId | String | - | u_mes_mast_country._id |
| 9 | countryName | String | - |  |
| 10 | website | String | - |  |
| 11 | supportPhone | String | - |  |
| 12 | status | String | - |  |
| 13 | schemaVersion | Int32 | - |  |

## u_mes_mast_equipmentType

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

## u_mes_mast_skillCategory

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

## u_mes_mast_permission

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
| 8 | resourceName | String | - |  |
| 9 | actionName | String | - |  |
| 10 | sequenceNo | Int32 | - |  |
| 11 | status | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_signatureMeaning

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

## u_mes_mast_currency

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | symbol | String | - |  |
| 8 | decimalPlaces | Int32 | - |  |
| 9 | isoNumericCode | String | - |  |
| 10 | sequenceNo | Int32 | - |  |
| 11 | status | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_country

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | isoAlpha3Code | String | - |  |
| 8 | dialCode | String | - |  |
| 9 | sequenceNo | Int32 | - |  |
| 10 | status | String | - |  |
| 11 | schemaVersion | Int32 | - |  |

## u_mes_mast_language

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | nativeName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | status | String | - |  |
| 10 | schemaVersion | Int32 | - |  |

## u_mes_mast_transporter

Kind: entity | Data class: master | Parent: - | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | name | String | - |  |
| 7 | gstin | String | - |  |
| 8 | phone | String | - |  |
| 9 | email | String | - |  |
| 10 | sequenceNo | Int32 | - |  |
| 11 | status | String | - |  |
| 12 | schemaVersion | Int32 | - |  |

## u_mes_mast_commodity

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

## u_mes_mast_roleRequiredSkill

Kind: relationship | Data class: master | Parent: u_mes_mast_role | _id pattern: 16-digit numeric string

| # | Key | BSON type | Date tag | References |
|---|---|---|---|---|
| 1 | _id | String | - |  |
| 2 | recordNo | String | - |  |
| 3 | app | String | - |  |
| 4 | siteId | String | - | u_mes_mast_site._id |
| 5 | siteName | String | - |  |
| 6 | roleId | String | - | u_mes_mast_role._id |
| 7 | roleName | String | - |  |
| 8 | sequenceNo | Int32 | - |  |
| 9 | requiredSkillId | String | - | u_mes_mast_skill._id |
| 10 | requiredSkillName | String | - |  |
| 11 | minimumLevel | Int32 | - |  |
| 12 | schemaVersion | Int32 | - |  |
