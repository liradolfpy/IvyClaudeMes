## u_mes_mast_area - Areas (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_area.json | _id: mes_mast_areaStable | rel: CL20261018-23:51 | samples: 20 | columns: 13 | total width: 2070px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 4 | 110px | left |
| 2 | name | Name | String | 36 | 280px | left |
| 3 | areaType | Area Type | String | 11 | 110px | left |
| 4 | parentAreaName | Parent Area | String | 0 | 120px | left |
| 5 | costCenterName | Cost Center | String | 28 | 220px | left |
| 6 | supervisorUserName | Supervisor User | String | 13 | 150px | left |
| 7 | floorAreaSqm | Floor Area Sqm | Decimal128 | 6 | 140px | right |
| 8 | isProductionArea | Production Area | Boolean | 3 | 150px | center |
| 9 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 10 | cleanlinessClass | Cleanliness Class | String | 25 | 200px | left |
| 11 | environmentallyMonitored | Environmentally Monitored | Boolean | 3 | 220px | center |
| 12 | gowningRequired | Gowning Required | Boolean | 3 | 160px | center |
| 13 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); parentAreaId (reference key, shown through parentAreaName); costCenterId (reference key, shown through costCenterName); supervisorUserId (reference key, shown through supervisorUserName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): parentAreaName

## u_mes_mast_commodity - Commodities (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_commodity.json | _id: mes_mast_commodityStable | rel: CL20261018-23:51 | samples: 20 | columns: 5 | total width: 890px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | name | Name | String | 35 | 270px | left |
| 3 | description | Description | String | 43 | 300px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_costCenter - Cost Centers (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_costCenter.json | _id: mes_mast_costCenterStable | rel: CL20261018-23:51 | samples: 20 | columns: 7 | total width: 1080px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 4 | 110px | left |
| 2 | name | Name | String | 28 | 220px | left |
| 3 | description | Description | String | 35 | 270px | left |
| 4 | erpCostCenterCode | ERP Cost Center Code | String | 8 | 180px | left |
| 5 | validFrom | Valid From | Date/Date | 10 | 110px | center |
| 6 | validTo | Valid to | Date/Date | 10 | 100px | center |
| 7 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_country - Countries (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_country.json | _id: mes_mast_countryStable | rel: CL20261018-23:51 | samples: 10 | columns: 6 | total width: 700px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 2 | 110px | left |
| 2 | name | Name | String | 14 | 120px | left |
| 3 | isoAlpha3Code | Iso Alpha3 Code | String | 3 | 150px | left |
| 4 | dialCode | Dial Code | String | 3 | 110px | left |
| 5 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 6 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_currency - Currencies (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_currency.json | _id: mes_mast_currencyStable | rel: CL20261018-23:51 | samples: 10 | columns: 7 | total width: 850px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 3 | 110px | left |
| 2 | name | Name | String | 16 | 140px | left |
| 3 | symbol | Symbol | String | 3 | 90px | left |
| 4 | decimalPlaces | Decimal Places | Int32 | 1 | 140px | right |
| 5 | isoNumericCode | Iso Numeric Code | String | 3 | 160px | left |
| 6 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 7 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_customer - Customers (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_customer.json | _id: mes_mast_customerStable | rel: CL20261018-23:51 | samples: 20 | columns: 19 | total width: 3580px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 3 | 110px | left |
| 2 | name | Name | String | 42 | 300px | left |
| 3 | customerType | Customer Type | String | 13 | 140px | left |
| 4 | parentCustomerCode | Parent Customer Code | String | 3 | 180px | left |
| 5 | gstin | Gstin | String | 15 | 130px | left |
| 6 | billingAddressLine1 | Billing Address Line1 | String | 40 | 300px | left |
| 7 | billingAddressCity | Billing Address City | String | 4 | 180px | left |
| 8 | billingAddressState | Billing Address State | String | 11 | 190px | left |
| 9 | billingAddressPostalCode | Billing Address Postal Code | String | 6 | 230px | left |
| 10 | billingAddressCountryName | Billing Address Country | String | 5 | 210px | left |
| 11 | supplierCodeAtCustomer | Supplier Code At Customer | String | 7 | 220px | left |
| 12 | labelTemplateName | Label Template | String | 44 | 300px | left |
| 13 | asnRequired | Asn Required | Boolean | 3 | 130px | center |
| 14 | ppapLevelDefault | Ppap Level Default | Int32 | 1 | 170px | right |
| 15 | ppmTarget | PPM Target | Int32 | 2 | 110px | right |
| 16 | paymentTermsDays | Payment Terms (days) | Int32 | 2 | 180px | right |
| 17 | currencyName | Currency | String | 12 | 110px | left |
| 18 | portalUrl | Portal Url | String | 39 | 300px | left |
| 19 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); billingAddressCountryId (reference key, shown through billingAddressCountryName); labelTemplateId (reference key, shown through labelTemplateName); currencyId (reference key, shown through currencyName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_customerContact - Customer Contacts (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_customerContact.json | _id: mes_mast_customerContactStable | rel: CL20261018-23:51 | samples: 10 | columns: 7 | total width: 1200px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 7 | 110px | left |
| 2 | customerName | Customer | String | 35 | 270px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | name | Name | String | 16 | 140px | left |
| 5 | businessFunction | Business Function | String | 7 | 160px | left |
| 6 | email | Email | String | 33 | 260px | left |
| 7 | phone | Phone | String | 17 | 140px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerId (reference key, shown through customerName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_customerShipTo - Customer Ship-To Addresses (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_customerShipTo.json | _id: mes_mast_customerShipToStable | rel: CL20261018-23:51 | samples: 10 | columns: 11 | total width: 1710px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 8 | 110px | left |
| 2 | customerName | Customer | String | 35 | 270px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | shipToCode | Ship to Code | String | 10 | 130px | left |
| 5 | name | Name | String | 43 | 300px | left |
| 6 | line1 | Line1 | String | 29 | 230px | left |
| 7 | city | City | String | 4 | 80px | left |
| 8 | state | State | String | 11 | 100px | left |
| 9 | postalCode | Postal Code | String | 6 | 120px | left |
| 10 | dockCode | Dock Code | String | 2 | 110px | left |
| 11 | transitDays | Transit (days) | Int32 | 1 | 140px | right |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerId (reference key, shown through customerName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_department - Departments (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_department.json | _id: mes_mast_departmentStable | rel: CL20261018-23:51 | samples: 20 | columns: 8 | total width: 1300px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 6 | 110px | left |
| 2 | name | Name | String | 29 | 230px | left |
| 3 | description | Description | String | 35 | 270px | left |
| 4 | parentDepartmentName | Parent Department | String | 0 | 160px | left |
| 5 | headUserName | Head User | String | 15 | 130px | left |
| 6 | costCenterName | Cost Center | String | 24 | 190px | left |
| 7 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 8 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); parentDepartmentId (reference key, shown through parentDepartmentName); headUserId (reference key, shown through headUserName); costCenterId (reference key, shown through costCenterName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): parentDepartmentName

## u_mes_mast_designation - Designations (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_designation.json | _id: mes_mast_designationStable | rel: CL20261018-23:51 | samples: 20 | columns: 8 | total width: 1310px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 8 | 110px | left |
| 2 | name | Name | String | 35 | 270px | left |
| 3 | description | Description | String | 45 | 300px | left |
| 4 | departmentName | Department | String | 22 | 180px | left |
| 5 | gradeLevel | Grade Level | Int32 | 1 | 120px | right |
| 6 | isSupervisory | Supervisory | Boolean | 3 | 120px | center |
| 7 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 8 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); departmentId (reference key, shown through departmentName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_employmentType - Employment Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_employmentType.json | _id: mes_mast_employmentTypeStable | rel: CL20261018-23:51 | samples: 10 | columns: 6 | total width: 910px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | name | Name | String | 26 | 210px | left |
| 3 | description | Description | String | 36 | 280px | left |
| 4 | isContract | Contract | Boolean | 3 | 100px | center |
| 5 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 6 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_enterprise - Enterprises (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_enterprise.json | _id: mes_mast_enterpriseStable | rel: CL20261018-23:51 | samples: 20 | columns: 19 | total width: 3630px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 3 | 110px | left |
| 2 | name | Name | String | 41 | 300px | left |
| 3 | legalName | Legal Name | String | 47 | 300px | left |
| 4 | scope | Scope | String | 10 | 90px | left |
| 5 | parentEnterpriseName | Parent Enterprise | String | 0 | 160px | left |
| 6 | cin | Cin | String | 21 | 170px | left |
| 7 | gstin | Gstin | String | 15 | 130px | left |
| 8 | pan | Pan | String | 10 | 90px | left |
| 9 | industryCode | Industry Code | String | 5 | 140px | left |
| 10 | registeredAddressLine1 | Registered Address Line1 | String | 39 | 300px | left |
| 11 | registeredAddressLine2 | Registered Address Line2 | String | 30 | 230px | left |
| 12 | registeredAddressCity | Registered Address City | String | 4 | 210px | left |
| 13 | registeredAddressState | Registered Address State | String | 11 | 210px | left |
| 14 | registeredAddressPostalCode | Registered Address Postal Code | String | 6 | 250px | left |
| 15 | registeredAddressCountryName | Registered Address Country | String | 5 | 230px | left |
| 16 | baseCurrencyName | Base Currency | String | 12 | 140px | left |
| 17 | fiscalYearStartMonth | Fiscal Year Start Month | Int32 | 1 | 210px | right |
| 18 | website | Website | String | 35 | 270px | left |
| 19 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); parentEnterpriseId (reference key, shown through parentEnterpriseName); registeredAddressCountryId (reference key, shown through registeredAddressCountryName); baseCurrencyId (reference key, shown through baseCurrencyName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): parentEnterpriseName

## u_mes_mast_enterpriseContact - Enterprise Contacts (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_enterpriseContact.json | _id: mes_mast_enterpriseContactStable | rel: CL20261018-23:51 | samples: 10 | columns: 7 | total width: 1140px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 7 | 110px | left |
| 2 | enterpriseName | Enterprise | String | 33 | 260px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | name | Name | String | 16 | 140px | left |
| 5 | jobTitle | Job Title | String | 10 | 110px | left |
| 6 | email | Email | String | 33 | 260px | left |
| 7 | phone | Phone | String | 17 | 140px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); enterpriseId (reference key, shown through enterpriseName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_equipment - Equipment (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_equipment.json | _id: mes_mast_equipmentStable | rel: CL20261018-23:51 | samples: 20 | columns: 41 | total width: 7420px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 9 | 110px | left |
| 2 | name | Name | String | 54 | 300px | left |
| 3 | equipmentTypeName | Equipment Type | String | 27 | 210px | left |
| 4 | equipmentClass | Equipment Class | String | 20 | 160px | left |
| 5 | lineName | Line | String | 35 | 270px | left |
| 6 | workCenterName | Work Center | String | 37 | 280px | left |
| 7 | parentEquipmentName | Parent Equipment | String | 0 | 160px | left |
| 8 | manufacturerName | Manufacturer | String | 28 | 220px | left |
| 9 | model | Model | String | 31 | 240px | left |
| 10 | serialNo | Serial No | String | 17 | 140px | left |
| 11 | yearOfManufacture | Year of Manufacture | Int32 | 4 | 180px | right |
| 12 | supplierName | Supplier | String | 0 | 100px | left |
| 13 | assetNo | Asset No | String | 13 | 120px | left |
| 14 | commissionedAt | Commissioned At | Date/Datetime | 19 | 160px | center |
| 15 | ratedCapacity | Rated Capacity | Decimal128 | 4 | 140px | right |
| 16 | ratedCapacityUnitOfMeasureName | Rated Capacity Unit of Measure | String | 14 | 250px | left |
| 17 | ratedPowerKw | Rated Power Kw | Decimal128 | 3 | 140px | right |
| 18 | controllerMake | Controller Make | String | 19 | 160px | left |
| 19 | controllerModel | Controller Model | String | 26 | 210px | left |
| 20 | controllerIpAddress | Controller IP Address | String | 10 | 190px | left |
| 21 | controllerProtocol | Controller Protocol | String | 13 | 180px | left |
| 22 | criticality | Criticality | String | 1 | 120px | left |
| 23 | currentState | Current State | String | 7 | 140px | left |
| 24 | currentStateSince | Current State Since | Date/Datetime | 19 | 180px | center |
| 25 | lifetimeCycles | Lifetime Cycles | Int64 | 7 | 150px | right |
| 26 | lifetimeRunHours | Lifetime Run (h) | Decimal128 | 7 | 160px | right |
| 27 | nextMaintenanceDueAt | Next Maintenance Due At | Date/Date | 10 | 210px | center |
| 28 | calibrationRequired | Calibration Required | Boolean | 3 | 180px | center |
| 29 | safetyCategory | Safety Category | String | 4 | 150px | left |
| 30 | isProductionReady | Production Ready | Boolean | 3 | 160px | center |
| 31 | readinessReasonText | Readiness Reason Text | String | 62 | 300px | left |
| 32 | healthScore | Health Score | Decimal128 | 2 | 130px | right |
| 33 | healthScoreAt | Health Score At | Date/Datetime | 19 | 160px | center |
| 34 | acquisitionCostInr | Acquisition Cost (INR) | Decimal128 | 10 | 200px | right |
| 35 | plannedReplacementDate | Planned Replacement Date | Date/Date | 10 | 210px | center |
| 36 | qualificationStatus | Qualification Status | String | 19 | 180px | left |
| 37 | requalificationDueDate | Requalification Due Date | Date/Date | 10 | 210px | center |
| 38 | cleanStatus | Clean Status | String | 18 | 150px | left |
| 39 | cleanHoldExpiresAt | Clean Hold Expires At | Date/Datetime | 19 | 190px | center |
| 40 | lastCleaningRecordName | Last Cleaning Record | String | 16 | 180px | left |
| 41 | status | Status | String | 17 | 140px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentTypeId (reference key, shown through equipmentTypeName); lineId (reference key, shown through lineName); workCenterId (reference key, shown through workCenterName); parentEquipmentId (reference key, shown through parentEquipmentName); manufacturerId (reference key, shown through manufacturerName); supplierId (reference key, shown through supplierName); ratedCapacityUnitOfMeasureId (reference key, shown through ratedCapacityUnitOfMeasureName); lastCleaningRecordId (reference key, shown through lastCleaningRecordName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): parentEquipmentName, supplierName

## u_mes_mast_equipmentIotDevice - Equipment IoT Devices (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_equipmentIotDevice.json | _id: mes_mast_equipmentIotDeviceStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 770px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | equipmentName | Equipment | String | 31 | 240px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | iotDeviceName | IoT Device | String | 38 | 290px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); equipmentId (reference key, shown through equipmentName); iotDeviceId (reference key, shown through iotDeviceName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_equipmentType - Equipment Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_equipmentType.json | _id: mes_mast_equipmentTypeStable | rel: CL20261018-23:51 | samples: 20 | columns: 5 | total width: 830px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | name | Name | String | 27 | 210px | left |
| 3 | description | Description | String | 41 | 300px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_language - Languages (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_language.json | _id: mes_mast_languageStable | rel: CL20261018-23:51 | samples: 10 | columns: 5 | total width: 520px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 2 | 110px | left |
| 2 | name | Name | String | 8 | 80px | left |
| 3 | nativeName | Native Name | String | 8 | 120px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_line - Lines (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_line.json | _id: mes_mast_lineStable | rel: CL20261018-23:51 | samples: 20 | columns: 13 | total width: 2330px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 6 | 110px | left |
| 2 | name | Name | String | 35 | 270px | left |
| 3 | areaName | Area | String | 29 | 230px | left |
| 4 | lineType | Line Type | String | 17 | 140px | left |
| 5 | itemFamilyName | Item Family | String | 21 | 170px | left |
| 6 | workCalendarName | Work Calendar | String | 42 | 300px | left |
| 7 | taktTimeSec | Takt Time (s) | Decimal128 | 4 | 140px | right |
| 8 | manningStandard | Manning Standard | Int32 | 1 | 160px | right |
| 9 | bottleneckWorkCenterName | Bottleneck Work Center | String | 35 | 270px | left |
| 10 | oeeTarget | OEE Target | Decimal128 | 4 | 110px | right |
| 11 | costCenterName | Cost Center | String | 28 | 220px | left |
| 12 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 13 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); areaId (reference key, shown through areaName); itemFamilyId (reference key, shown through itemFamilyName); workCalendarId (reference key, shown through workCalendarName); bottleneckWorkCenterId (reference key, shown through bottleneckWorkCenterName); costCenterId (reference key, shown through costCenterName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_lineDefaultShift - Line Default Shifts (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_lineDefaultShift.json | _id: mes_mast_lineDefaultShiftStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 640px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 11 | 110px | left |
| 2 | lineName | Line | String | 35 | 270px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | defaultShiftName | Default Shift | String | 7 | 140px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); lineId (reference key, shown through lineName); defaultShiftId (reference key, shown through defaultShiftName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_lineIdealRate - Line Ideal Rates (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_lineIdealRate.json | _id: mes_mast_lineIdealRateStable | rel: CL20261018-23:51 | samples: 10 | columns: 6 | total width: 1090px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 11 | 110px | left |
| 2 | lineName | Line | String | 29 | 230px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | itemName | Item | String | 39 | 300px | left |
| 5 | idealCycleTimeSec | Ideal Cycle Time (s) | Decimal128 | 7 | 180px | right |
| 6 | targetPerHour | Target per Hour | Int32 | 3 | 150px | right |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); lineId (reference key, shown through lineName); itemId (reference key, shown through itemName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_manufacturer - Manufacturers (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_manufacturer.json | _id: mes_mast_manufacturerStable | rel: CL20261018-23:51 | samples: 20 | columns: 7 | total width: 1160px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 3 | 110px | left |
| 2 | name | Name | String | 28 | 220px | left |
| 3 | description | Description | String | 34 | 260px | left |
| 4 | countryName | Country | String | 5 | 90px | left |
| 5 | website | Website | String | 32 | 250px | left |
| 6 | supportPhone | Support Phone | String | 16 | 140px | left |
| 7 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); countryId (reference key, shown through countryName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_permission - Permissions (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_permission.json | _id: mes_mast_permissionStable | rel: CL20261018-23:51 | samples: 10 | columns: 7 | total width: 1250px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 27 | 210px | left |
| 2 | name | Name | String | 34 | 260px | left |
| 3 | description | Description | String | 63 | 300px | left |
| 4 | resourceName | Resource Name | String | 18 | 150px | left |
| 5 | actionName | Action Name | String | 8 | 120px | left |
| 6 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 7 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_role - Roles (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_role.json | _id: mes_mast_roleStable | rel: CL20261018-23:51 | samples: 20 | columns: 8 | total width: 1270px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | name | Name | String | 35 | 270px | left |
| 3 | scope | Scope | String | 10 | 90px | left |
| 4 | description | Description | String | 120 | 300px | left |
| 5 | canSign | Can Sign | Boolean | 3 | 100px | center |
| 6 | approvalLimitInr | Approval Limit (INR) | Decimal128 | 3 | 180px | right |
| 7 | isSystemRole | System Role | Boolean | 3 | 120px | center |
| 8 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_rolePermission - Role Permissions (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_rolePermission.json | _id: mes_mast_rolePermissionStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 700px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | roleName | Role | String | 22 | 180px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | permissionName | Permission | String | 34 | 260px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); roleId (reference key, shown through roleName); permissionId (reference key, shown through permissionName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_roleRequiredSkill - Role Required Skills (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_roleRequiredSkill.json | _id: mes_mast_roleRequiredSkillStable | rel: CL20261018-23:51 | samples: 10 | columns: 5 | total width: 810px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | roleName | Role | String | 22 | 180px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | requiredSkillName | Required Skill | String | 30 | 230px | left |
| 5 | minimumLevel | Minimum Level | Int32 | 1 | 140px | right |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); roleId (reference key, shown through roleName); requiredSkillId (reference key, shown through requiredSkillName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_roleSignatureMeaning - Role Signature Meanings (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_roleSignatureMeaning.json | _id: mes_mast_roleSignatureMeaningStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 600px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | roleName | Role | String | 22 | 180px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | signatureMeaningName | Signature Meaning | String | 13 | 160px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); roleId (reference key, shown through roleName); signatureMeaningId (reference key, shown through signatureMeaningName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_shift - Shifts (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_shift.json | _id: mes_mast_shiftStable | rel: CL20261018-23:51 | samples: 20 | columns: 10 | total width: 1530px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 5 | 110px | left |
| 2 | name | Name | String | 23 | 190px | left |
| 3 | startTimeLocal | Start Time Local | String | 5 | 160px | left |
| 4 | endTimeLocal | End Time Local | String | 5 | 140px | left |
| 5 | crossesMidnight | Crosses Midnight | Boolean | 3 | 160px | center |
| 6 | durationMinutes | Duration (min) | Int32 | 3 | 140px | right |
| 7 | plannedProductionMinutes | Planned Production (min) | Int32 | 3 | 210px | right |
| 8 | shiftAllowancePerDay | Shift Allowance per Day | Decimal128 | 3 | 210px | right |
| 9 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 10 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_shiftBreak - Shift Breaks (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_shiftBreak.json | _id: mes_mast_shiftBreakStable | rel: CL20261018-23:51 | samples: 10 | columns: 7 | total width: 860px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 9 | 110px | left |
| 2 | shiftName | Shift | String | 16 | 140px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | name | Name | String | 12 | 110px | left |
| 5 | startTimeLocal | Start Time Local | String | 5 | 160px | left |
| 6 | durationMinutes | Duration (min) | Int32 | 3 | 140px | right |
| 7 | paid | Paid | Boolean | 3 | 80px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); shiftId (reference key, shown through shiftName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_shiftRoster - Shift Rosters (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_shiftRoster.json | _id: mes_mast_shiftRosterStable | rel: CL20261018-23:51 | samples: 10 | columns: 16 | total width: 2460px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 3 | shiftName | Shift | String | 7 | 80px | left |
| 4 | lineName | Line | String | 35 | 270px | left |
| 5 | supervisorUserName | Supervisor User | String | 12 | 150px | left |
| 6 | plannedHeadcount | Planned Headcount | Int32 | 1 | 160px | right |
| 7 | actualHeadcount | Actual Headcount | Int32 | 1 | 160px | right |
| 8 | absentCount | Absent Count | Int32 | 1 | 130px | right |
| 9 | overtimeMinutes | Overtime (min) | Int32 | 1 | 140px | right |
| 10 | remarks | Remarks | String | 37 | 280px | left |
| 11 | publishedAt | Published At | Date/Datetime | 19 | 160px | center |
| 12 | status | Status | String | 9 | 90px | left |
| 13 | createdBy | Created By | String | 14 | 120px | left |
| 14 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 15 | updatedBy | Updated By | String | 14 | 120px | left |
| 16 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); shiftId (reference key, shown through shiftName); lineId (reference key, shown through lineName); supervisorUserId (reference key, shown through supervisorUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_mast_shiftRosterAssignment - Shift Roster Assignments (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_shiftRosterAssignment.json | _id: mes_mast_shiftRosterAssignmentStable | rel: CL20261018-23:51 | samples: 10 | columns: 16 | total width: 2330px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | shiftRosterName | Shift Roster | String | 15 | 130px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | userName | User | String | 14 | 120px | left |
| 5 | workCenterName | Work Center | String | 26 | 210px | left |
| 6 | roleInCrew | Role in Crew | String | 17 | 140px | left |
| 7 | attendance | Attendance | String | 8 | 110px | left |
| 8 | replacedUserName | Replaced User | String | 0 | 140px | left |
| 9 | assignedFromAt | Assigned From At | Date/Datetime | 19 | 160px | center |
| 10 | assignedToAt | Assigned to At | Date/Datetime | 19 | 160px | center |
| 11 | assignmentSource | Assignment Source | String | 6 | 160px | left |
| 12 | suggestionScore | Suggestion Score | Decimal128 | 4 | 160px | right |
| 13 | createdBy | Created By | String | 14 | 120px | left |
| 14 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 15 | updatedBy | Updated By | String | 14 | 120px | left |
| 16 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); shiftRosterId (reference key, shown through shiftRosterName); userId (reference key, shown through userName); workCenterId (reference key, shown through workCenterName); replacedUserId (reference key, shown through replacedUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): replacedUserName

## u_mes_mast_shiftWorkingDay - Shift Working Days (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_shiftWorkingDay.json | _id: mes_mast_shiftWorkingDayStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 490px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | shiftName | Shift | String | 16 | 140px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | workingDay | Working Day | String | 9 | 120px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); shiftId (reference key, shown through shiftName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_signatureMeaning - Signature Meanings (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_signatureMeaning.json | _id: mes_mast_signatureMeaningStable | rel: CL20261018-23:51 | samples: 10 | columns: 5 | total width: 680px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | name | Name | String | 13 | 120px | left |
| 3 | description | Description | String | 29 | 230px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_site - Sites (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_site.json | _id: mes_mast_siteStable | rel: CL20261018-23:51 | samples: 20 | columns: 23 | total width: 3870px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 3 | 110px | left |
| 2 | name | Name | String | 41 | 300px | left |
| 3 | enterpriseName | Enterprise | String | 41 | 300px | left |
| 4 | siteType | Site Type | String | 19 | 160px | left |
| 5 | timezone | Timezone | String | 12 | 110px | left |
| 6 | utcOffsetMinutes | Utc Offset (min) | Int32 | 3 | 160px | right |
| 7 | addressLine1 | Address Line1 | String | 46 | 300px | left |
| 8 | addressLine2 | Address Line2 | String | 30 | 230px | left |
| 9 | addressCity | Address City | String | 9 | 130px | left |
| 10 | addressDistrict | Address District | String | 18 | 160px | left |
| 11 | addressState | Address State | String | 16 | 140px | left |
| 12 | addressPostalCode | Address Postal Code | String | 6 | 180px | left |
| 13 | addressCountryName | Address Country | String | 5 | 150px | left |
| 14 | geoLatitude | Geo Latitude | Double | 7 | 130px | right |
| 15 | geoLongitude | Geo Longitude | Double | 7 | 140px | right |
| 16 | gstin | Gstin | String | 15 | 130px | left |
| 17 | factoryLicenceNo | Factory Licence No | String | 30 | 230px | left |
| 18 | erpPlantCode | ERP Plant Code | String | 4 | 140px | left |
| 19 | defaultWorkCalendarName | Default Work Calendar | String | 34 | 260px | left |
| 20 | currencyName | Currency | String | 12 | 110px | left |
| 21 | languageName | Language | String | 7 | 100px | left |
| 22 | headcount | Headcount | Int32 | 3 | 110px | right |
| 23 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); enterpriseId (reference key, shown through enterpriseName); addressCountryId (reference key, shown through addressCountryName); defaultWorkCalendarId (reference key, shown through defaultWorkCalendarName); currencyId (reference key, shown through currencyName); languageId (reference key, shown through languageName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_siteCertificate - Site Certificates (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_siteCertificate.json | _id: mes_mast_siteCertificateStable | rel: CL20261018-23:51 | samples: 10 | columns: 7 | total width: 820px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 7 | 110px | left |
| 2 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 3 | standard | Standard | String | 15 | 130px | left |
| 4 | certificateNo | Certificate No | String | 12 | 140px | left |
| 5 | issuedBy | Issued By | String | 12 | 110px | left |
| 6 | validFrom | Valid From | Date/Date | 10 | 110px | center |
| 7 | validTo | Valid to | Date/Date | 10 | 100px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); issuedById (reference key, shown through issuedBy); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_skill - Skills (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_skill.json | _id: mes_mast_skillStable | rel: CL20261018-23:51 | samples: 20 | columns: 10 | total width: 1990px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | name | Name | String | 45 | 300px | left |
| 3 | skillCategoryName | Skill Category | String | 29 | 230px | left |
| 4 | description | Description | String | 96 | 300px | left |
| 5 | minimumLevelRequired | Minimum Level Required | Int32 | 1 | 200px | right |
| 6 | validityMonths | Validity Months | Int32 | 2 | 150px | right |
| 7 | trainingControlledDocumentName | Training Controlled Document | String | 78 | 300px | left |
| 8 | assessmentMethod | Assessment Method | String | 14 | 160px | left |
| 9 | isSafetyCritical | Safety Critical | Boolean | 3 | 150px | center |
| 10 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); skillCategoryId (reference key, shown through skillCategoryName); trainingControlledDocumentId (reference key, shown through trainingControlledDocumentName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_skillCategory - Skill Categories (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_skillCategory.json | _id: mes_mast_skillCategoryStable | rel: CL20261018-23:51 | samples: 20 | columns: 5 | total width: 850px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | name | Name | String | 29 | 230px | left |
| 3 | description | Description | String | 41 | 300px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_skillCertification - Skill Certifications (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_skillCertification.json | _id: mes_mast_skillCertificationStable | rel: CL20261018-23:51 | samples: 10 | columns: 24 | total width: 3910px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 23 | 190px | left |
| 2 | userName | User | String | 14 | 120px | left |
| 3 | skillName | Skill | String | 32 | 250px | left |
| 4 | level | Level | Int32 | 1 | 80px | right |
| 5 | awardedAt | Awarded At | Date/Datetime | 19 | 160px | center |
| 6 | validFrom | Valid From | Date/Date | 10 | 110px | center |
| 7 | validTo | Valid to | Date/Date | 10 | 100px | center |
| 8 | assessorUserName | Assessor User | String | 15 | 140px | left |
| 9 | assessmentScore | Assessment Score | Decimal128 | 4 | 160px | right |
| 10 | assessmentMethod | Assessment Method | String | 14 | 160px | left |
| 11 | trainingHours | Training (h) | Decimal128 | 4 | 130px | right |
| 12 | evidenceControlledDocumentName | Evidence Controlled Document | String | 64 | 300px | left |
| 13 | restrictions | Restrictions | String | 42 | 300px | left |
| 14 | revokedAt | Revoked At | Date/Datetime | 19 | 160px | center |
| 15 | revokedReason | Revoked Reason | String | 0 | 140px | left |
| 16 | nextReviewAt | Next Review At | Date/Date | 10 | 140px | center |
| 17 | trainedDocumentRevision | Trained Document Revision | String | 1 | 220px | left |
| 18 | requalificationRequired | Requalification Required | Boolean | 3 | 210px | center |
| 19 | revocationSource | Revocation Source | String | 18 | 160px | left |
| 20 | status | Status | String | 13 | 120px | left |
| 21 | createdBy | Created By | String | 14 | 120px | left |
| 22 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 23 | updatedBy | Updated By | String | 14 | 120px | left |
| 24 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); userId (reference key, shown through userName); skillId (reference key, shown through skillName); assessorUserId (reference key, shown through assessorUserName); evidenceControlledDocumentId (reference key, shown through evidenceControlledDocumentName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): revokedReason

## u_mes_mast_skillLevelScale - Skill Level Scales (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_skillLevelScale.json | _id: mes_mast_skillLevelScaleStable | rel: CL20261018-23:51 | samples: 10 | columns: 5 | total width: 860px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 11 | 110px | left |
| 2 | skillName | Skill | String | 32 | 250px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | level | Level | Int32 | 1 | 80px | right |
| 5 | description | Description | String | 59 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); skillId (reference key, shown through skillName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_skillOperation - Skill Operations (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_skillOperation.json | _id: mes_mast_skillOperationStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 700px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | skillName | Skill | String | 32 | 250px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | operationName | Operation | String | 24 | 190px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); skillId (reference key, shown through skillName); operationId (reference key, shown through operationName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_supplier - Suppliers (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_supplier.json | _id: mes_mast_supplierStable | rel: CL20261018-23:51 | samples: 20 | columns: 19 | total width: 3240px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 5 | 110px | left |
| 2 | name | Name | String | 44 | 300px | left |
| 3 | supplierType | Supplier Type | String | 22 | 180px | left |
| 4 | commodityName | Commodity | String | 35 | 270px | left |
| 5 | gstin | Gstin | String | 15 | 130px | left |
| 6 | addressLine1 | Address Line1 | String | 37 | 280px | left |
| 7 | addressCity | Address City | String | 11 | 130px | left |
| 8 | addressState | Address State | String | 11 | 140px | left |
| 9 | addressPostalCode | Address Postal Code | String | 6 | 180px | left |
| 10 | addressCountryName | Address Country | String | 5 | 150px | left |
| 11 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 12 | ppmLast12Months | PPM Last12 Months | Int32 | 2 | 160px | right |
| 13 | deliveryRatingPct | Delivery Rating (%) | Decimal128 | 4 | 180px | right |
| 14 | qualityRatingPct | Quality Rating (%) | Decimal128 | 5 | 170px | right |
| 15 | leadTimeDays | Lead Time (days) | Int32 | 2 | 160px | right |
| 16 | paymentTermsDays | Payment Terms (days) | Int32 | 2 | 180px | right |
| 17 | currencyName | Currency | String | 12 | 110px | left |
| 18 | isDirectedSource | Directed Source | Boolean | 3 | 150px | center |
| 19 | status | Status | String | 11 | 100px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); commodityId (reference key, shown through commodityName); addressCountryId (reference key, shown through addressCountryName); currencyId (reference key, shown through currencyName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_supplierCertificate - Supplier Certificates (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_supplierCertificate.json | _id: mes_mast_supplierCertificateStable | rel: CL20261018-23:51 | samples: 10 | columns: 6 | total width: 880px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | supplierName | Supplier | String | 36 | 280px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | standard | Standard | String | 15 | 130px | left |
| 5 | certificateNo | Certificate No | String | 12 | 140px | left |
| 6 | validTo | Valid to | Date/Date | 10 | 100px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); supplierId (reference key, shown through supplierName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_supplierContact - Supplier Contacts (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_supplierContact.json | _id: mes_mast_supplierContactStable | rel: CL20261018-23:51 | samples: 10 | columns: 7 | total width: 1210px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 9 | 110px | left |
| 2 | supplierName | Supplier | String | 36 | 280px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | name | Name | String | 16 | 140px | left |
| 5 | businessFunction | Business Function | String | 7 | 160px | left |
| 6 | email | Email | String | 33 | 260px | left |
| 7 | phone | Phone | String | 17 | 140px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); supplierId (reference key, shown through supplierName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_supplierSuppliedItem - Supplier Supplied Items (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_supplierSuppliedItem.json | _id: mes_mast_supplierSuppliedItemStable | rel: CL20261018-23:51 | samples: 20 | columns: 6 | total width: 1190px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | supplierName | Supplier | String | 44 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | suppliedItemName | Supplied Item | String | 61 | 300px | left |
| 5 | qualificationStatus | Qualification Status | String | 22 | 180px | left |
| 6 | qualifiedUntilDate | Qualified Until Date | Date/Date | 10 | 180px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); supplierId (reference key, shown through supplierName); suppliedItemId (reference key, shown through suppliedItemName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_transporter - Transporters (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_transporter.json | _id: mes_mast_transporterStable | rel: CL20261018-23:51 | samples: 20 | columns: 7 | total width: 1080px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 3 | 110px | left |
| 2 | name | Name | String | 30 | 230px | left |
| 3 | gstin | Gstin | String | 15 | 130px | left |
| 4 | phone | Phone | String | 17 | 140px | left |
| 5 | email | Email | String | 33 | 260px | left |
| 6 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 7 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_unitOfMeasure - Units of Measure (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_unitOfMeasure.json | _id: mes_mast_unitOfMeasureStable | rel: CL20261018-23:51 | samples: 20 | columns: 12 | total width: 1440px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 4 | 110px | left |
| 2 | name | Name | String | 16 | 140px | left |
| 3 | scope | Scope | String | 10 | 90px | left |
| 4 | symbol | Symbol | String | 4 | 90px | left |
| 5 | dimension | Dimension | String | 11 | 110px | left |
| 6 | baseUnitOfMeasureName | Base Unit of Measure | String | 0 | 180px | left |
| 7 | factorToBase | Factor to Base | Decimal128 | 3 | 140px | right |
| 8 | offsetToBase | Offset to Base | Decimal128 | 3 | 140px | right |
| 9 | decimalPlaces | Decimal Places | Int32 | 1 | 140px | right |
| 10 | isoCode | Iso Code | String | 3 | 100px | left |
| 11 | isBaseUnit | Base Unit | Boolean | 3 | 110px | center |
| 12 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); baseUnitOfMeasureId (reference key, shown through baseUnitOfMeasureName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): baseUnitOfMeasureName

## u_mes_mast_user - Users (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_user.json | _id: mes_mast_userStable | rel: CL20261018-23:51 | samples: 20 | columns: 23 | total width: 3660px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 9 | 110px | left |
| 2 | userName | User Name | String | 15 | 130px | left |
| 3 | fullName | Full Name | String | 18 | 150px | left |
| 4 | userType | User Type | String | 8 | 110px | left |
| 5 | departmentName | Department | String | 22 | 180px | left |
| 6 | designationName | Designation | String | 35 | 270px | left |
| 7 | badgeNo | Badge No | String | 9 | 100px | left |
| 8 | email | Email | String | 38 | 290px | left |
| 9 | mobile | Mobile | String | 15 | 130px | left |
| 10 | defaultShiftName | Default Shift | String | 13 | 140px | left |
| 11 | homeWorkCenterName | Home Work Center | String | 32 | 250px | left |
| 12 | reportsToUserName | Reports to User | String | 15 | 150px | left |
| 13 | dateOfJoining | Date of Joining | Date/Date | 10 | 150px | center |
| 14 | employmentTypeName | Employment Type | String | 14 | 150px | left |
| 15 | contractorSupplierName | Contractor Supplier | String | 24 | 190px | left |
| 16 | languageName | Language | String | 7 | 100px | left |
| 17 | lastLoginAt | Last Login At | Date/Datetime | 0 | 140px | center |
| 18 | failedLoginCount | Failed Login Count | Int32 | 1 | 170px | right |
| 19 | passwordChangedAt | Password Changed At | Date/Datetime | 19 | 180px | center |
| 20 | isLocked | Locked | Boolean | 3 | 90px | center |
| 21 | lastAccessReviewDate | Last Access Review Date | Date/Date | 10 | 210px | center |
| 22 | passwordExpiryDate | Password Expiry Date | Date/Date | 10 | 180px | center |
| 23 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); departmentId (reference key, shown through departmentName); designationId (reference key, shown through designationName); defaultShiftId (reference key, shown through defaultShiftName); homeWorkCenterId (reference key, shown through homeWorkCenterName); reportsToUserId (reference key, shown through reportsToUserName); employmentTypeId (reference key, shown through employmentTypeName); contractorSupplierId (reference key, shown through contractorSupplierName); languageId (reference key, shown through languageName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): lastLoginAt

## u_mes_mast_userRole - User Roles (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_userRole.json | _id: mes_mast_userRoleStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 540px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | userName | User | String | 15 | 130px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | roleName | Role | String | 22 | 180px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); userId (reference key, shown through userName); roleId (reference key, shown through roleName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_workCalendar - Work Calendars (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_workCalendar.json | _id: mes_mast_workCalendarStable | rel: CL20261018-23:51 | samples: 20 | columns: 7 | total width: 960px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | name | Name | String | 42 | 300px | left |
| 3 | year | Year | Int32 | 4 | 80px | right |
| 4 | workingDaysCount | Working Days Count | Int32 | 3 | 170px | right |
| 5 | validFrom | Valid From | Date/Date | 10 | 110px | center |
| 6 | validTo | Valid to | Date/Date | 10 | 100px | center |
| 7 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_workCalendarException - Work Calendar Exceptions (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_workCalendarException.json | _id: mes_mast_workCalendarExceptionStable | rel: CL20261018-23:51 | samples: 10 | columns: 7 | total width: 1230px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | workCalendarName | Work Calendar | String | 39 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | exceptionDate | Exception Date | Date/Date | 10 | 140px | center |
| 5 | exceptionType | Exception Type | String | 17 | 140px | left |
| 6 | description | Description | String | 41 | 300px | left |
| 7 | isWorking | Working | Boolean | 3 | 90px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCalendarId (reference key, shown through workCalendarName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_workCalendarExceptionShift - Work Calendar Exception Shifts (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_workCalendarExceptionShift.json | _id: mes_mast_workCalendarExceptionShiftStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 570px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | workCalendarExceptionName | Work Calendar Exception | String | 16 | 210px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | shiftName | Shift | String | 7 | 80px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCalendarExceptionId (reference key, shown through workCalendarExceptionName); shiftId (reference key, shown through shiftName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_workCalendarLine - Work Calendar Lines (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_workCalendarLine.json | _id: mes_mast_workCalendarLineStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 830px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | workCalendarName | Work Calendar | String | 42 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | lineName | Line | String | 35 | 270px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCalendarId (reference key, shown through workCalendarName); lineId (reference key, shown through lineName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_workCalendarShift - Work Calendar Shifts (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_workCalendarShift.json | _id: mes_mast_workCalendarShiftStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 640px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | workCalendarName | Work Calendar | String | 42 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | shiftName | Shift | String | 7 | 80px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCalendarId (reference key, shown through workCalendarName); shiftId (reference key, shown through shiftName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_workCalendarWeeklyOffDay - Work Calendar Weekly Off Days (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_workCalendarWeeklyOffDay.json | _id: mes_mast_workCalendarWeeklyOffDayStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 710px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | workCalendarName | Work Calendar | String | 39 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | weeklyOffDay | Weekly Off Day | String | 9 | 140px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCalendarId (reference key, shown through workCalendarName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_workCenter - Work Centers (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_workCenter.json | _id: mes_mast_workCenterStable | rel: CL20261018-23:51 | samples: 20 | columns: 15 | total width: 2790px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 6 | 110px | left |
| 2 | name | Name | String | 37 | 280px | left |
| 3 | areaName | Area | String | 29 | 230px | left |
| 4 | lineName | Line | String | 35 | 270px | left |
| 5 | workCenterType | Work Center Type | String | 18 | 160px | left |
| 6 | erpWorkCenterCode | ERP Work Center Code | String | 10 | 180px | left |
| 7 | costCenterName | Cost Center | String | 28 | 220px | left |
| 8 | capacityPerShift | Capacity per Shift | Int32 | 3 | 170px | right |
| 9 | standardManning | Standard Manning | Int32 | 1 | 160px | right |
| 10 | trackingGrain | Tracking Grain | String | 4 | 140px | left |
| 11 | inputLocationName | Input Location | String | 33 | 260px | left |
| 12 | outputLocationName | Output Location | String | 33 | 260px | left |
| 13 | andonEnabled | Andon Enabled | Boolean | 3 | 140px | center |
| 14 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 15 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); areaId (reference key, shown through areaName); lineId (reference key, shown through lineName); costCenterId (reference key, shown through costCenterName); inputLocationId (reference key, shown through inputLocationName); outputLocationId (reference key, shown through outputLocationName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_workCenterEquipment - Work Center Equipment (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_workCenterEquipment.json | _id: mes_mast_workCenterEquipmentStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 730px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | workCenterName | Work Center | String | 33 | 260px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | equipmentName | Equipment | String | 31 | 240px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCenterId (reference key, shown through workCenterName); equipmentId (reference key, shown through equipmentName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_workCenterOperation - Work Center Operations (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_workCenterOperation.json | _id: mes_mast_workCenterOperationStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 680px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | workCenterName | Work Center | String | 33 | 260px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | operationName | Operation | String | 24 | 190px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCenterId (reference key, shown through workCenterName); operationId (reference key, shown through operationName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mast_workCenterRequiresSkill - Work Center Required Skills (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mast_workCenterRequiresSkill.json | _id: mes_mast_workCenterRequiresSkillStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 740px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 11 | 110px | left |
| 2 | workCenterName | Work Center | String | 33 | 260px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | requiresSkillName | Requires Skill | String | 32 | 250px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCenterId (reference key, shown through workCenterName); requiresSkillId (reference key, shown through requiresSkillName); schemaVersion (excluded key (identifier, site, app or schema))
