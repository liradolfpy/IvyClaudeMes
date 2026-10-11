# Master data review

Run: 11 October 2026 | Trigger: owner review of the user document (department, designation, employmentType held as text without a master collection).

Scope: every text key of every collection was reviewed against data_modeling_standard.md section 11.

| Result | Count |
|---|---|
| New master collections | 41 |
| Keys converted from text to a master reference | 67 |
| Keys kept as fixed enumerations (values in u_mes_sys_enumerationValue) | 205 |

## New master collections

| # | Collection | Purpose | Keys |
|---|---|---|---|
| 1 | u_mes_mdm_department | Departments of the site (production, quality, maintenance ...) | _id, recordNo, siteId, siteName, name, description, parentDepartmentId, parentDepartmentName, headUserId, headUserName, costCenterId, costCenterName, sequenceNo, status, schemaVersion |
| 2 | u_mes_mdm_designation | Job designations of employees | _id, recordNo, siteId, siteName, name, description, departmentId, departmentName, gradeLevel, isSupervisory, sequenceNo, status, schemaVersion |
| 3 | u_mes_mdm_employmentType | Types of employment (permanent, contract, trainee, apprentice) | _id, recordNo, siteId, siteName, name, description, isContract, sequenceNo, status, schemaVersion |
| 4 | u_mes_mdm_costCenter | Cost centers charged with activities, mapped to ERP | _id, recordNo, siteId, siteName, name, description, erpCostCenterCode, validFrom, validTo, status, schemaVersion |
| 5 | u_mes_mdm_manufacturer | Manufacturers of equipment, gauges, devices and spare parts | _id, recordNo, siteId, siteName, name, description, countryId, countryName, website, supportPhone, status, schemaVersion |
| 6 | u_mes_mdm_equipmentType | Types of equipment (casting machine, furnace, nutrunner, leak tester ...) | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 7 | u_mes_mdm_skillCategory | Categories of skills (process, quality, maintenance, safety) | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 8 | u_mes_mdm_permission | Permissions that can be granted to roles | _id, recordNo, siteId, siteName, name, description, resourceName, actionName, sequenceNo, status, schemaVersion |
| 9 | u_mes_mdm_signatureMeaning | Meanings an electronic signature can carry (approved, reviewed, released ...) | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 10 | u_mes_mdm_currency | Currencies used for costs and invoices | _id, recordNo, siteId, siteName, name, symbol, decimalPlaces, isoNumericCode, sequenceNo, status, schemaVersion |
| 11 | u_mes_mdm_country | Countries used in addresses | _id, recordNo, siteId, siteName, name, isoAlpha3Code, dialCode, sequenceNo, status, schemaVersion |
| 12 | u_mes_mdm_language | Languages of users, instructions and documents | _id, recordNo, siteId, siteName, name, nativeName, sequenceNo, status, schemaVersion |
| 13 | u_mes_mdm_transporter | Transport companies used for dispatch | _id, recordNo, siteId, siteName, name, gstin, phone, email, sequenceNo, status, schemaVersion |
| 14 | u_mes_mdm_commodity | Purchasing commodities used to classify suppliers | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 15 | u_mes_prd_itemGroup | Item groups (brake caliper, piston, seal, fastener ...) | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 16 | u_mes_prd_itemFamily | Product families a line is built for (front caliper, rear caliper) | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 17 | u_mes_prd_ppeItem | Personal protective equipment that a work instruction can require | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 18 | u_mes_prd_market | Sales markets of a product variant (domestic, export) | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 19 | u_mes_prd_padCompound | Brake pad friction compounds offered as a variant option | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 20 | u_mes_prd_surfaceFinish | Surface finishes offered as a variant option | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 21 | u_mes_prd_vehicleModel | Customer vehicle models the parts are fitted to | _id, recordNo, siteId, siteName, name, description, customerId, customerName, modelYear, platformCode, sequenceNo, status, schemaVersion |
| 22 | u_mes_exe_indirectActivity | Indirect labour activities (cleaning, training, waiting for material ...) | _id, recordNo, siteId, siteName, name, description, isPaid, costCenterId, costCenterName, sequenceNo, status, schemaVersion |
| 23 | u_mes_exe_containerType | Types of container with dimensions and tare weight | _id, recordNo, siteId, siteName, name, description, lengthMm, widthMm, heightMm, tareWeightKg, isReturnable, sequenceNo, status, schemaVersion |
| 24 | u_mes_mat_movementType | Stock movement types with their ERP movement code and stock effect | _id, recordNo, siteId, siteName, name, description, erpMovementType, stockEffect, requiresReason, sequenceNo, status, schemaVersion |
| 25 | u_mes_mat_stockStatus | Stock statuses (unrestricted, quality inspection, blocked, reserved) | _id, recordNo, siteId, siteName, name, description, isUsable, erpStockType, sequenceNo, status, schemaVersion |
| 26 | u_mes_mat_packType | Pack levels used in packaging specifications (bag, tray, bin, pallet) | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 27 | u_mes_qlt_defectGroup | Groups of defect codes (casting, machining, leak, torque ...) | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 28 | u_mes_qlt_gaugeType | Types of gauge and measuring instrument | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 29 | u_mes_qlt_dispositionType | Dispositions for nonconforming material (use as is, rework, scrap, return, sort) | _id, recordNo, siteId, siteName, name, description, requiresRework, requiresScrap, requiresCustomerApproval, sequenceNo, status, schemaVersion |
| 30 | u_mes_qlt_complaintType | Types of customer complaint (line rejection, zero kilometre, warranty, logistics) | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 31 | u_mes_eqp_lossCategory | OEE loss categories with the OEE factor they reduce | _id, recordNo, siteId, siteName, name, description, oeeImpact, sixBigLossNo, sequenceNo, status, schemaVersion |
| 32 | u_mes_eqp_reasonCategory | Categories of reason codes (mechanical, electrical, process, material ...) | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 33 | u_mes_mnt_toolType | Types of tool (die, fixture, cutting tool, socket, test seal) | _id, recordNo, siteId, siteName, name, description, lifeUom, sequenceNo, status, schemaVersion |
| 34 | u_mes_sys_documentType | Types of controlled document with retention | _id, recordNo, siteId, siteName, name, description, retentionYears, isControlled, sequenceNo, status, schemaVersion |
| 35 | u_mes_sys_deviceType | Types of connected device (PLC, nutrunner controller, leak tester, printer ...) | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 36 | u_mes_sys_notificationType | Types of notification sent by the system | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 37 | u_mes_ehs_andonType | Types of andon call with responsible department and target response time | _id, recordNo, siteId, siteName, name, description, colourCode, responsibleDepartmentId, responsibleDepartmentName, targetResponseSec, sequenceNo, status, schemaVersion |
| 38 | u_mes_ehs_incidentType | Types of safety incident | _id, recordNo, siteId, siteName, name, description, isInjury, reportableToAuthority, sequenceNo, status, schemaVersion |
| 39 | u_mes_ehs_energyType | Types of energy and utility that are metered | _id, recordNo, siteId, siteName, name, description, unitOfMeasureId, unitOfMeasureName, sequenceNo, status, schemaVersion |
| 40 | u_mes_ehs_bodyPart | Body parts for injury records | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 41 | u_mes_ehs_injuryType | Types of injury | _id, recordNo, siteId, siteName, name, description, sequenceNo, status, schemaVersion |

## Keys converted

Array notation refers to the concept model; in the flat model an array of references is a relationship collection.

| # | Concept collection | Key before | Key after | Master collection |
|---|---|---|---|---|
| 1 | u_mes_mdm_enterprise | contacts[].designation | contacts[].jobTitle | none (renamed only, to avoid confusion with designationId) |
| 2 | u_mes_mdm_enterprise | baseCurrency | baseCurrencyId | u_mes_mdm_currency |
| 3 | u_mes_mdm_enterprise | registeredAddress.country | registeredAddress.countryId | u_mes_mdm_country |
| 4 | u_mes_mdm_site | address.country | address.countryId | u_mes_mdm_country |
| 5 | u_mes_mdm_site | currency | currencyId | u_mes_mdm_currency |
| 6 | u_mes_mdm_site | language | languageId | u_mes_mdm_language |
| 7 | u_mes_mdm_area | costCentre | costCenterId | u_mes_mdm_costCenter |
| 8 | u_mes_mdm_line | costCentre | costCenterId | u_mes_mdm_costCenter |
| 9 | u_mes_mdm_line | itemFamily | itemFamilyId | u_mes_prd_itemFamily |
| 10 | u_mes_mdm_workCenter | costCentre | costCenterId | u_mes_mdm_costCenter |
| 11 | u_mes_mdm_equipment | equipmentType | equipmentTypeId | u_mes_mdm_equipmentType |
| 12 | u_mes_mdm_equipment | manufacturer | manufacturerId | u_mes_mdm_manufacturer |
| 13 | u_mes_mdm_role | permissions[] | permissionIds[] | u_mes_mdm_permission |
| 14 | u_mes_mdm_role | signatureMeanings[] | signatureMeaningIds[] | u_mes_mdm_signatureMeaning |
| 15 | u_mes_mdm_user | department | departmentId | u_mes_mdm_department |
| 16 | u_mes_mdm_user | designation | designationId | u_mes_mdm_designation |
| 17 | u_mes_mdm_user | employmentType | employmentTypeId | u_mes_mdm_employmentType |
| 18 | u_mes_mdm_user | language | languageId | u_mes_mdm_language |
| 19 | u_mes_mdm_skill | skillCategory | skillCategoryId | u_mes_mdm_skillCategory |
| 20 | u_mes_mdm_customer | billingAddress.country | billingAddress.countryId | u_mes_mdm_country |
| 21 | u_mes_mdm_customer | currency | currencyId | u_mes_mdm_currency |
| 22 | u_mes_mdm_supplier | address.country | address.countryId | u_mes_mdm_country |
| 23 | u_mes_mdm_supplier | currency | currencyId | u_mes_mdm_currency |
| 24 | u_mes_mdm_supplier | commodity | commodityId | u_mes_mdm_commodity |
| 25 | u_mes_prd_item | itemGroup | itemGroupId | u_mes_prd_itemGroup |
| 26 | u_mes_prd_productVariant | options.padCompound | options.padCompoundId | u_mes_prd_padCompound |
| 27 | u_mes_prd_productVariant | options.market | options.marketId | u_mes_prd_market |
| 28 | u_mes_prd_productVariant | options.surfaceFinish | options.surfaceFinishId | u_mes_prd_surfaceFinish |
| 29 | u_mes_prd_productVariant | modelCode | vehicleModelId | u_mes_prd_vehicleModel |
| 30 | u_mes_prd_workInstruction | language | languageId | u_mes_mdm_language |
| 31 | u_mes_prd_workInstruction | ppeRequired[] | ppeItemIds[] | u_mes_prd_ppeItem |
| 32 | u_mes_prd_engineeringChange | stockDisposition | stockDispositionTypeId | u_mes_qlt_dispositionType |
| 33 | u_mes_exe_container | containerType | containerTypeId | u_mes_exe_containerType |
| 34 | u_mes_exe_labourBooking | indirectActivity | indirectActivityId | u_mes_exe_indirectActivity |
| 35 | u_mes_mat_inventoryBalance | stockStatus | stockStatusId | u_mes_mat_stockStatus |
| 36 | u_mes_mat_materialMovement | movementType | movementTypeId | u_mes_mat_movementType |
| 37 | u_mes_mat_materialMovement | fromStockStatus | fromStockStatusId | u_mes_mat_stockStatus |
| 38 | u_mes_mat_materialMovement | toStockStatus | toStockStatusId | u_mes_mat_stockStatus |
| 39 | u_mes_mat_packagingSpecification | containerType | containerTypeId | u_mes_exe_containerType |
| 40 | u_mes_mat_packagingSpecification | levels[].packType | levels[].packTypeId | u_mes_mat_packType |
| 41 | u_mes_mat_shipment | transporter | transporterId | u_mes_mdm_transporter |
| 42 | u_mes_qlt_characteristic | gaugeType | gaugeTypeId | u_mes_qlt_gaugeType |
| 43 | u_mes_qlt_defectCode | defectGroup | defectGroupId | u_mes_qlt_defectGroup |
| 44 | u_mes_qlt_defectCode | defaultDisposition | defaultDispositionTypeId | u_mes_qlt_dispositionType |
| 45 | u_mes_qlt_nonconformance | affectedObjects[].disposition | affectedObjects[].dispositionTypeId | u_mes_qlt_dispositionType |
| 46 | u_mes_qlt_gauge | gaugeType | gaugeTypeId | u_mes_qlt_gaugeType |
| 47 | u_mes_qlt_gauge | manufacturer | manufacturerId | u_mes_mdm_manufacturer |
| 48 | u_mes_qlt_customerComplaint | complaintType | complaintTypeId | u_mes_qlt_complaintType |
| 49 | u_mes_qlt_customerComplaint | vehicleModel | vehicleModelId | u_mes_prd_vehicleModel |
| 50 | u_mes_eqp_reasonCode | category | reasonCategoryId | u_mes_eqp_reasonCategory |
| 51 | u_mes_eqp_reasonCode | lossCategory | lossCategoryId | u_mes_eqp_lossCategory |
| 52 | u_mes_eqp_reasonCode | responsibleDepartment | responsibleDepartmentId | u_mes_mdm_department |
| 53 | u_mes_eqp_oeeRecord | losses[].lossCategory | losses[].lossCategoryId | u_mes_eqp_lossCategory |
| 54 | u_mes_mnt_maintenancePlan | ownerDepartment | ownerDepartmentId | u_mes_mdm_department |
| 55 | u_mes_mnt_sparePart | manufacturer | manufacturerId | u_mes_mdm_manufacturer |
| 56 | u_mes_mnt_tool | toolType | toolTypeId | u_mes_mnt_toolType |
| 57 | u_mes_sys_iotDevice | deviceType | deviceTypeId | u_mes_sys_deviceType |
| 58 | u_mes_sys_iotDevice | manufacturer | manufacturerId | u_mes_mdm_manufacturer |
| 59 | u_mes_sys_operatorApp | languages[] | languageIds[] | u_mes_mdm_language |
| 60 | u_mes_sys_electronicSignature | meaning | signatureMeaningId | u_mes_mdm_signatureMeaning |
| 61 | u_mes_sys_notification | notificationType | notificationTypeId | u_mes_sys_notificationType |
| 62 | u_mes_sys_controlledDocument | documentType | documentTypeId | u_mes_sys_documentType |
| 63 | u_mes_sys_controlledDocument | language | languageId | u_mes_mdm_language |
| 64 | u_mes_ehs_energyReading | energyType | energyTypeId | u_mes_ehs_energyType |
| 65 | u_mes_ehs_andonEvent | andonType | andonTypeId | u_mes_ehs_andonType |
| 66 | u_mes_ehs_safetyIncident | incidentType | incidentTypeId | u_mes_ehs_incidentType |
| 67 | u_mes_ehs_safetyIncident | bodyPart | bodyPartId | u_mes_ehs_bodyPart |
| 68 | u_mes_ehs_safetyIncident | injuryType | injuryTypeId | u_mes_ehs_injuryType |

## Keys reviewed and kept as fixed enumerations

Listed with their values in 04_reference_data/code_lists/enumeration_values.md.
