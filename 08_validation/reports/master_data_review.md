# Master data review

Run: 11 October 2026 | Trigger: owner review of the user document (department, designation, employmentType held as text without a master collection).

Scope: every text key of every collection was reviewed against data_modeling_standard.md section 11.

| Result | Count |
|---|---|
| New master collections | 41 |
| Keys converted from text to a master reference | 67 |
| Keys kept as fixed enumerations (values in u_mes_syst_enumerationValue) | 689 |

## New master collections

| # | Collection | Purpose | Keys |
|---|---|---|---|
| 1 | u_mes_mast_department | Departments of the site (production, quality, maintenance ...) | _id, recordNo, app, siteId, siteName, name, description, parentDepartmentId, parentDepartmentName, headUserId, headUserName, costCenterId, costCenterName, sequenceNo, status, schemaVersion |
| 2 | u_mes_mast_designation | Job designations of employees | _id, recordNo, app, siteId, siteName, name, description, departmentId, departmentName, gradeLevel, isSupervisory, sequenceNo, status, schemaVersion |
| 3 | u_mes_mast_employmentType | Types of employment (permanent, contract, trainee, apprentice) | _id, recordNo, app, siteId, siteName, name, description, isContract, sequenceNo, status, schemaVersion |
| 4 | u_mes_mast_costCenter | Cost centers charged with activities, mapped to ERP | _id, recordNo, app, siteId, siteName, name, description, erpCostCenterCode, validFrom, validTo, status, schemaVersion |
| 5 | u_mes_mast_manufacturer | Manufacturers of equipment, gauges, devices and spare parts | _id, recordNo, app, siteId, siteName, name, description, countryId, countryName, website, supportPhone, status, schemaVersion |
| 6 | u_mes_mast_equipmentType | Types of equipment (casting machine, furnace, nutrunner, leak tester ...) | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 7 | u_mes_mast_skillCategory | Categories of skills (process, quality, maintenance, safety) | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 8 | u_mes_mast_permission | Permissions that can be granted to roles | _id, recordNo, app, siteId, siteName, name, description, resourceName, actionName, sequenceNo, status, schemaVersion |
| 9 | u_mes_mast_signatureMeaning | Meanings an electronic signature can carry (approved, reviewed, released ...) | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 10 | u_mes_mast_currency | Currencies used for costs and invoices | _id, recordNo, app, siteId, siteName, name, symbol, decimalPlaces, isoNumericCode, sequenceNo, status, schemaVersion |
| 11 | u_mes_mast_country | Countries used in addresses | _id, recordNo, app, siteId, siteName, name, isoAlpha3Code, dialCode, sequenceNo, status, schemaVersion |
| 12 | u_mes_mast_language | Languages of users, instructions and documents | _id, recordNo, app, siteId, siteName, name, nativeName, sequenceNo, status, schemaVersion |
| 13 | u_mes_mast_transporter | Transport companies used for dispatch | _id, recordNo, app, siteId, siteName, name, gstin, phone, email, sequenceNo, status, schemaVersion |
| 14 | u_mes_mast_commodity | Purchasing commodities used to classify suppliers | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 15 | u_mes_prod_itemGroup | Item groups (brake caliper, piston, seal, fastener ...) | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 16 | u_mes_prod_itemFamily | Product families a line is built for (front caliper, rear caliper) | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 17 | u_mes_prod_ppeItem | Personal protective equipment that a work instruction can require | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 18 | u_mes_prod_market | Sales markets of a product variant (domestic, export) | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 19 | u_mes_prod_padCompound | Brake pad friction compounds offered as a variant option | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 20 | u_mes_prod_surfaceFinish | Surface finishes offered as a variant option | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 21 | u_mes_prod_vehicleModel | Customer vehicle models the parts are fitted to | _id, recordNo, app, siteId, siteName, name, description, customerId, customerName, modelYear, platformCode, sequenceNo, status, schemaVersion |
| 22 | u_mes_plan_indirectActivity | Indirect labour activities (cleaning, training, waiting for material ...) | _id, recordNo, app, siteId, siteName, name, description, isPaid, costCenterId, costCenterName, sequenceNo, status, schemaVersion |
| 23 | u_mes_plan_containerType | Types of container with dimensions and tare weight | _id, recordNo, app, siteId, siteName, name, description, lengthMm, widthMm, heightMm, tareWeightKg, isReturnable, sequenceNo, status, schemaVersion |
| 24 | u_mes_matl_movementType | Stock movement types with their ERP movement code and stock effect | _id, recordNo, app, siteId, siteName, name, description, erpMovementType, stockEffect, requiresReason, sequenceNo, status, schemaVersion |
| 25 | u_mes_matl_stockStatus | Stock statuses (unrestricted, quality inspection, blocked, reserved) | _id, recordNo, app, siteId, siteName, name, description, isUsable, erpStockType, sequenceNo, status, schemaVersion |
| 26 | u_mes_matl_packType | Pack levels used in packaging specifications (bag, tray, bin, pallet) | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 27 | u_mes_qual_defectGroup | Groups of defect codes (casting, machining, leak, torque ...) | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 28 | u_mes_qual_gaugeType | Types of gauge and measuring instrument | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 29 | u_mes_qual_dispositionType | Dispositions for nonconforming material (use as is, rework, scrap, return, sort) | _id, recordNo, app, siteId, siteName, name, description, requiresRework, requiresScrap, requiresCustomerApproval, sequenceNo, status, schemaVersion |
| 30 | u_mes_qual_complaintType | Types of customer complaint (line rejection, zero kilometre, warranty, logistics) | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 31 | u_mes_perf_lossCategory | OEE loss categories with the OEE factor they reduce | _id, recordNo, app, siteId, siteName, name, description, oeeImpact, sixBigLossNo, sequenceNo, status, schemaVersion |
| 32 | u_mes_perf_reasonCategory | Categories of reason codes (mechanical, electrical, process, material ...) | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 33 | u_mes_maint_toolType | Types of tool (die, fixture, cutting tool, socket, test seal) | _id, recordNo, app, siteId, siteName, name, description, lifeUom, sequenceNo, status, schemaVersion |
| 34 | u_mes_syst_documentType | Types of controlled document with retention | _id, recordNo, app, siteId, siteName, name, description, retentionYears, isControlled, sequenceNo, status, schemaVersion |
| 35 | u_mes_syst_deviceType | Types of connected device (PLC, nutrunner controller, leak tester, printer ...) | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 36 | u_mes_syst_notificationType | Types of notification sent by the system | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 37 | u_mes_plan_andonType | Types of andon call with responsible department and target response time | _id, recordNo, app, siteId, siteName, name, description, colourCode, responsibleDepartmentId, responsibleDepartmentName, targetResponseSec, sequenceNo, targetRepairSec, escalationRuleId, escalationRuleName, status, schemaVersion |
| 38 | u_mes_ehs_incidentType | Types of safety incident | _id, recordNo, app, siteId, siteName, name, description, isInjury, reportableToAuthority, sequenceNo, status, schemaVersion |
| 39 | u_mes_perf_energyType | Types of energy and utility that are metered | _id, recordNo, app, siteId, siteName, name, description, unitOfMeasureId, unitOfMeasureName, sequenceNo, status, schemaVersion |
| 40 | u_mes_ehs_bodyPart | Body parts for injury records | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |
| 41 | u_mes_ehs_injuryType | Types of injury | _id, recordNo, app, siteId, siteName, name, description, sequenceNo, status, schemaVersion |

## Keys converted

Array notation refers to the concept model; in the flat model an array of references is a relationship collection.

| # | Concept collection | Key before | Key after | Master collection |
|---|---|---|---|---|
| 1 | u_mes_mast_enterprise | contacts[].designation | contacts[].jobTitle | none (renamed only, to avoid confusion with designationId) |
| 2 | u_mes_mast_enterprise | baseCurrency | baseCurrencyId | u_mes_mast_currency |
| 3 | u_mes_mast_enterprise | registeredAddress.country | registeredAddress.countryId | u_mes_mast_country |
| 4 | u_mes_mast_site | address.country | address.countryId | u_mes_mast_country |
| 5 | u_mes_mast_site | currency | currencyId | u_mes_mast_currency |
| 6 | u_mes_mast_site | language | languageId | u_mes_mast_language |
| 7 | u_mes_mast_area | costCentre | costCenterId | u_mes_mast_costCenter |
| 8 | u_mes_mast_line | costCentre | costCenterId | u_mes_mast_costCenter |
| 9 | u_mes_mast_line | itemFamily | itemFamilyId | u_mes_prod_itemFamily |
| 10 | u_mes_mast_workCenter | costCentre | costCenterId | u_mes_mast_costCenter |
| 11 | u_mes_mast_equipment | equipmentType | equipmentTypeId | u_mes_mast_equipmentType |
| 12 | u_mes_mast_equipment | manufacturer | manufacturerId | u_mes_mast_manufacturer |
| 13 | u_mes_mast_role | permissions[] | permissionIds[] | u_mes_mast_permission |
| 14 | u_mes_mast_role | signatureMeanings[] | signatureMeaningIds[] | u_mes_mast_signatureMeaning |
| 15 | u_mes_mast_user | department | departmentId | u_mes_mast_department |
| 16 | u_mes_mast_user | designation | designationId | u_mes_mast_designation |
| 17 | u_mes_mast_user | employmentType | employmentTypeId | u_mes_mast_employmentType |
| 18 | u_mes_mast_user | language | languageId | u_mes_mast_language |
| 19 | u_mes_mast_skill | skillCategory | skillCategoryId | u_mes_mast_skillCategory |
| 20 | u_mes_mast_customer | billingAddress.country | billingAddress.countryId | u_mes_mast_country |
| 21 | u_mes_mast_customer | currency | currencyId | u_mes_mast_currency |
| 22 | u_mes_mast_supplier | address.country | address.countryId | u_mes_mast_country |
| 23 | u_mes_mast_supplier | currency | currencyId | u_mes_mast_currency |
| 24 | u_mes_mast_supplier | commodity | commodityId | u_mes_mast_commodity |
| 25 | u_mes_prod_item | itemGroup | itemGroupId | u_mes_prod_itemGroup |
| 26 | u_mes_prod_productVariant | options.padCompound | options.padCompoundId | u_mes_prod_padCompound |
| 27 | u_mes_prod_productVariant | options.market | options.marketId | u_mes_prod_market |
| 28 | u_mes_prod_productVariant | options.surfaceFinish | options.surfaceFinishId | u_mes_prod_surfaceFinish |
| 29 | u_mes_prod_productVariant | modelCode | vehicleModelId | u_mes_prod_vehicleModel |
| 30 | u_mes_prod_workInstruction | language | languageId | u_mes_mast_language |
| 31 | u_mes_prod_workInstruction | ppeRequired[] | ppeItemIds[] | u_mes_prod_ppeItem |
| 32 | u_mes_prod_engineeringChange | stockDisposition | stockDispositionTypeId | u_mes_qual_dispositionType |
| 33 | u_mes_plan_container | containerType | containerTypeId | u_mes_plan_containerType |
| 34 | u_mes_plan_labourBooking | indirectActivity | indirectActivityId | u_mes_plan_indirectActivity |
| 35 | u_mes_matl_inventoryBalance | stockStatus | stockStatusId | u_mes_matl_stockStatus |
| 36 | u_mes_matl_materialMovement | movementType | movementTypeId | u_mes_matl_movementType |
| 37 | u_mes_matl_materialMovement | fromStockStatus | fromStockStatusId | u_mes_matl_stockStatus |
| 38 | u_mes_matl_materialMovement | toStockStatus | toStockStatusId | u_mes_matl_stockStatus |
| 39 | u_mes_matl_packagingSpecification | containerType | containerTypeId | u_mes_plan_containerType |
| 40 | u_mes_matl_packagingSpecification | levels[].packType | levels[].packTypeId | u_mes_matl_packType |
| 41 | u_mes_matl_shipment | transporter | transporterId | u_mes_mast_transporter |
| 42 | u_mes_qual_characteristic | gaugeType | gaugeTypeId | u_mes_qual_gaugeType |
| 43 | u_mes_qual_defectCode | defectGroup | defectGroupId | u_mes_qual_defectGroup |
| 44 | u_mes_qual_defectCode | defaultDisposition | defaultDispositionTypeId | u_mes_qual_dispositionType |
| 45 | u_mes_qual_nonconformance | affectedObjects[].disposition | affectedObjects[].dispositionTypeId | u_mes_qual_dispositionType |
| 46 | u_mes_qual_gauge | gaugeType | gaugeTypeId | u_mes_qual_gaugeType |
| 47 | u_mes_qual_gauge | manufacturer | manufacturerId | u_mes_mast_manufacturer |
| 48 | u_mes_qual_customerComplaint | complaintType | complaintTypeId | u_mes_qual_complaintType |
| 49 | u_mes_qual_customerComplaint | vehicleModel | vehicleModelId | u_mes_prod_vehicleModel |
| 50 | u_mes_perf_reasonCode | category | reasonCategoryId | u_mes_perf_reasonCategory |
| 51 | u_mes_perf_reasonCode | lossCategory | lossCategoryId | u_mes_perf_lossCategory |
| 52 | u_mes_perf_reasonCode | responsibleDepartment | responsibleDepartmentId | u_mes_mast_department |
| 53 | u_mes_perf_oeeRecord | losses[].lossCategory | losses[].lossCategoryId | u_mes_perf_lossCategory |
| 54 | u_mes_maint_maintenancePlan | ownerDepartment | ownerDepartmentId | u_mes_mast_department |
| 55 | u_mes_maint_sparePart | manufacturer | manufacturerId | u_mes_mast_manufacturer |
| 56 | u_mes_maint_tool | toolType | toolTypeId | u_mes_maint_toolType |
| 57 | u_mes_syst_iotDevice | deviceType | deviceTypeId | u_mes_syst_deviceType |
| 58 | u_mes_syst_iotDevice | manufacturer | manufacturerId | u_mes_mast_manufacturer |
| 59 | u_mes_syst_operatorApp | languages[] | languageIds[] | u_mes_mast_language |
| 60 | u_mes_syst_electronicSignature | meaning | signatureMeaningId | u_mes_mast_signatureMeaning |
| 61 | u_mes_syst_notification | notificationType | notificationTypeId | u_mes_syst_notificationType |
| 62 | u_mes_syst_controlledDocument | documentType | documentTypeId | u_mes_syst_documentType |
| 63 | u_mes_syst_controlledDocument | language | languageId | u_mes_mast_language |
| 64 | u_mes_perf_energyReading | energyType | energyTypeId | u_mes_perf_energyType |
| 65 | u_mes_plan_andonEvent | andonType | andonTypeId | u_mes_plan_andonType |
| 66 | u_mes_ehs_safetyIncident | incidentType | incidentTypeId | u_mes_ehs_incidentType |
| 67 | u_mes_ehs_safetyIncident | bodyPart | bodyPartId | u_mes_ehs_bodyPart |
| 68 | u_mes_ehs_safetyIncident | injuryType | injuryTypeId | u_mes_ehs_injuryType |

## Keys reviewed and kept as fixed enumerations

Listed with their values in 04_reference_data/code_lists/enumeration_values.md.
