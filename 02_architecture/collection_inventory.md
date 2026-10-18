# Collection inventory

Model version 2.9 | 12 October 2026 | 369 collections (200 entity, 85 child, 76 relationship, 8 value-list), 8614 keys

Authority for collection names. Naming: `u_mes_<moduleCode>_<singularCollectionName>`. Each business concept appears once. Data class decides audit keys: transaction collections carry the six audit keys, master collections do not.

## Module codes

Menu = short module name shown as the main (level 0) menu label in the UI (owner list, 18 Oct 2026).

| Module code | Module | Menu | Collections |
|---|---|---|---|
| mast | MasterDataManagement | Master Data | 57 |
| prod | ProductDefinition | Product | 49 |
| plan | PlanningAndExecution | Plan | 43 |
| matl | MaterialManagement | Mtl Mgt | 27 |
| trac | Traceability | Trace | 9 |
| qual | QualityManagement | Quality | 85 |
| perf | PerformanceManagement | Performance | 21 |
| maint | ToolingAndMaintenance | Maint | 21 |
| syst | SystemAndIntegration | System | 44 |
| ehs | EnvironmentHealthAndSafety | EHS | 6 |
| bmr | BatchManufacturingRecord | BMR | 5 |
| mmr | MasterManufacturingRecord | MMR | 2 |

## mast - MasterDataManagement

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_mast_enterprise | entity | master | - | Legal entities of the group (ISA-95 Enterprise level); tax and registration data | name |
| 2 | u_mes_mast_enterpriseContact | child | master | u_mes_mast_enterprise | One document per contact of a enterprise | recordNo |
| 3 | u_mes_mast_site | entity | master | - | Plants and warehouses (ISA-95 Site); timezone, address, IATF certificate | name |
| 4 | u_mes_mast_siteCertificate | child | master | u_mes_mast_site | One document per certificate of a site | recordNo |
| 5 | u_mes_mast_area | entity | master | - | Production and support areas inside a site (ISA-95 Area) | name |
| 6 | u_mes_mast_line | entity | master | - | Production lines / cells (ISA-95 Production Line / Work Cell) | name |
| 7 | u_mes_mast_lineDefaultShift | relationship | master | u_mes_mast_line | Links one line to one default shift (one document per link) | recordNo |
| 8 | u_mes_mast_lineIdealRate | child | master | u_mes_mast_line | One document per ideal rate of a line | recordNo |
| 9 | u_mes_mast_workCenter | entity | master | - | Stations where operations are executed and booked; ERP work centre mapping | name |
| 10 | u_mes_mast_workCenterEquipment | relationship | master | u_mes_mast_workCenter | Links one workCenter to one equipment (one document per link) | recordNo |
| 11 | u_mes_mast_workCenterOperation | relationship | master | u_mes_mast_workCenter | Links one workCenter to one operation (one document per link) | recordNo |
| 12 | u_mes_mast_workCenterRequiresSkill | relationship | master | u_mes_mast_workCenter | Links one workCenter to one requires skill (one document per link) | recordNo |
| 13 | u_mes_mast_equipment | entity | master | - | Machines, furnaces, testers (ISA-95 Unit / Equipment); hierarchy, make, model, capability | name |
| 14 | u_mes_mast_equipmentIotDevice | relationship | master | u_mes_mast_equipment | Links one equipment to one iot device (one document per link) | recordNo |
| 15 | u_mes_mast_shift | entity | master | - | Shift patterns with start/end and breaks | name |
| 16 | u_mes_mast_shiftBreak | child | master | u_mes_mast_shift | One document per break of a shift | recordNo |
| 17 | u_mes_mast_shiftWorkingDay | valueList | master | u_mes_mast_shift | One document per working day value of a shift | recordNo |
| 18 | u_mes_mast_workCalendar | entity | master | - | Working calendars with holidays and exception days per site / line | name |
| 19 | u_mes_mast_workCalendarLine | relationship | master | u_mes_mast_workCalendar | Links one workCalendar to one line (one document per link) | recordNo |
| 20 | u_mes_mast_workCalendarShift | relationship | master | u_mes_mast_workCalendar | Links one workCalendar to one shift (one document per link) | recordNo |
| 21 | u_mes_mast_workCalendarWeeklyOffDay | valueList | master | u_mes_mast_workCalendar | One document per weekly off day value of a workCalendar | recordNo |
| 22 | u_mes_mast_workCalendarException | child | master | u_mes_mast_workCalendar | One document per exception of a workCalendar | recordNo |
| 23 | u_mes_mast_workCalendarExceptionShift | relationship | master | u_mes_mast_workCalendarException | Links one workCalendarException to one shift (one document per link) | recordNo |
| 24 | u_mes_mast_shiftRoster | entity | transaction | - | Crew assignment per production day, shift and line (who is planned where) | recordNo |
| 25 | u_mes_mast_shiftRosterAssignment | child | transaction | u_mes_mast_shiftRoster | One document per assignment of a shiftRoster | recordNo |
| 26 | u_mes_mast_role | entity | master | - | Named sets of permissions (operator, setter, quality engineer ...) | name |
| 27 | u_mes_mast_rolePermission | relationship | master | u_mes_mast_role | Links one role to one permission (one document per link) | recordNo |
| 28 | u_mes_mast_roleSignatureMeaning | relationship | master | u_mes_mast_role | Links one role to one signature meaning (one document per link) | recordNo |
| 29 | u_mes_mast_user | entity | master | - | People and system accounts; badge id, role, home work centre | fullName |
| 30 | u_mes_mast_userRole | relationship | master | u_mes_mast_user | Links one user to one role (one document per link) | recordNo |
| 31 | u_mes_mast_skill | entity | master | - | Skill definitions required by operations (e.g. leak-test operation, CMM programming) | name |
| 32 | u_mes_mast_skillOperation | relationship | master | u_mes_mast_skill | Links one skill to one operation (one document per link) | recordNo |
| 33 | u_mes_mast_skillLevelScale | child | master | u_mes_mast_skill | One document per level scale of a skill | recordNo |
| 34 | u_mes_mast_skillCertification | entity | transaction | - | Skills-matrix entries: user x skill, level, valid-from/to, assessor; used for operator lock-out | recordNo |
| 35 | u_mes_mast_customer | entity | master | - | OEMs and aftermarket customers; ship-to addresses, label and ASN requirements | name |
| 36 | u_mes_mast_customerShipTo | child | master | u_mes_mast_customer | One document per ship to of a customer | recordNo |
| 37 | u_mes_mast_customerContact | child | master | u_mes_mast_customer | One document per contact of a customer | recordNo |
| 38 | u_mes_mast_supplier | entity | master | - | Material, tooling and service suppliers; approval status, certificates, PPM rating | name |
| 39 | u_mes_mast_supplierContact | child | master | u_mes_mast_supplier | One document per contact of a supplier | recordNo |
| 40 | u_mes_mast_supplierCertificate | child | master | u_mes_mast_supplier | One document per certificate of a supplier | recordNo |
| 41 | u_mes_mast_supplierSuppliedItem | relationship | master | u_mes_mast_supplier | Links one supplier to one supplied item (one document per link) | recordNo |
| 42 | u_mes_mast_unitOfMeasure | entity | master | - | Units and conversion factors (EA, kg, N.m, bar, mm, um, kWh) | name |
| 43 | u_mes_mast_department | entity | master | - | Departments of the site (production, quality, maintenance ...) | name |
| 44 | u_mes_mast_designation | entity | master | - | Job designations of employees | name |
| 45 | u_mes_mast_employmentType | entity | master | - | Types of employment (permanent, contract, trainee, apprentice) | name |
| 46 | u_mes_mast_costCenter | entity | master | - | Cost centers charged with activities, mapped to ERP | name |
| 47 | u_mes_mast_manufacturer | entity | master | - | Manufacturers of equipment, gauges, devices and spare parts | name |
| 48 | u_mes_mast_equipmentType | entity | master | - | Types of equipment (casting machine, furnace, nutrunner, leak tester ...) | name |
| 49 | u_mes_mast_skillCategory | entity | master | - | Categories of skills (process, quality, maintenance, safety) | name |
| 50 | u_mes_mast_permission | entity | master | - | Permissions that can be granted to roles | name |
| 51 | u_mes_mast_signatureMeaning | entity | master | - | Meanings an electronic signature can carry (approved, reviewed, released ...) | name |
| 52 | u_mes_mast_currency | entity | master | - | Currencies used for costs and invoices | name |
| 53 | u_mes_mast_country | entity | master | - | Countries used in addresses | name |
| 54 | u_mes_mast_language | entity | master | - | Languages of users, instructions and documents | name |
| 55 | u_mes_mast_transporter | entity | master | - | Transport companies used for dispatch | name |
| 56 | u_mes_mast_commodity | entity | master | - | Purchasing commodities used to classify suppliers | name |
| 57 | u_mes_mast_roleRequiredSkill | relationship | master | u_mes_mast_role | Links one role to one required skill (one document per link) | recordNo |

## prod - ProductDefinition

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_prod_item | entity | master | - | Parts: finished caliper, semi-finished body, purchased components, raw material, consumables; drawing revision | description |
| 2 | u_mes_prod_itemRevision | child | master | u_mes_prod_item | One document per revision of a item | recordNo |
| 3 | u_mes_prod_itemCustomerPart | child | master | u_mes_prod_item | One document per customer part of a item | recordNo |
| 4 | u_mes_prod_productVariant | entity | master | - | Product variants (LH/RH, piston diameter, pad compound, market) that drive BOM, instruction and label selection | name |
| 5 | u_mes_prod_billOfMaterial | entity | master | - | Multi-level bills of material per item revision with effectivity | recordNo |
| 6 | u_mes_prod_billOfMaterialComponent | child | master | u_mes_prod_billOfMaterial | One document per component of a billOfMaterial | recordNo |
| 7 | u_mes_prod_billOfMaterialComponentProductVariant | relationship | master | u_mes_prod_billOfMaterialComponent | Links one billOfMaterialComponent to one product variant (one document per link) | recordNo |
| 8 | u_mes_prod_billOfMaterialComponentAlternateItem | relationship | master | u_mes_prod_billOfMaterialComponent | Links one billOfMaterialComponent to one alternate item (one document per link) | recordNo |
| 9 | u_mes_prod_operation | entity | master | - | Standard operation library (casting, T6, machining ... packing) reused by routings | name |
| 10 | u_mes_prod_operationRequiredSkill | relationship | master | u_mes_prod_operation | Links one operation to one required skill (one document per link) | recordNo |
| 11 | u_mes_prod_routing | entity | master | - | Sequence of operations per item, including rework / disposition routings and alternate paths | description |
| 12 | u_mes_prod_routingStep | child | master | u_mes_prod_routing | One document per step of a routing | recordNo |
| 13 | u_mes_prod_routingStepAlternateWorkCenter | relationship | master | u_mes_prod_routingStep | Links one routingStep to one alternate work center (one document per link) | recordNo |
| 14 | u_mes_prod_routingStepNextStep | child | master | u_mes_prod_routingStep | One document per next step of a routingStep | recordNo |
| 15 | u_mes_prod_billOfProcess | entity | master | - | Per routing step: required equipment, tools, recipe, work instruction, data collection, consumed components, cycle time | recordNo |
| 16 | u_mes_prod_billOfProcessStep | child | master | u_mes_prod_billOfProcess | One document per step of a billOfProcess | recordNo |
| 17 | u_mes_prod_billOfProcessStepEquipment | relationship | master | u_mes_prod_billOfProcessStep | Links one billOfProcessStep to one equipment (one document per link) | recordNo |
| 18 | u_mes_prod_billOfProcessStepTool | relationship | master | u_mes_prod_billOfProcessStep | Links one billOfProcessStep to one tool (one document per link) | recordNo |
| 19 | u_mes_prod_billOfProcessStepRequiredSkill | relationship | master | u_mes_prod_billOfProcessStep | Links one billOfProcessStep to one required skill (one document per link) | recordNo |
| 20 | u_mes_prod_billOfProcessStepConsumedComponent | child | master | u_mes_prod_billOfProcessStep | One document per consumed component of a billOfProcessStep | recordNo |
| 21 | u_mes_prod_billOfProcessStepInterlock | child | master | u_mes_prod_billOfProcessStep | One document per interlock of a billOfProcessStep | recordNo |
| 22 | u_mes_prod_billOfProcessStepProcessParameter | child | master | u_mes_prod_billOfProcessStep | One document per process parameter of a billOfProcessStep | recordNo |
| 23 | u_mes_prod_workInstruction | entity | master | - | Versioned visual work instructions with steps, media, cautions, variant applicability, required checks | title |
| 24 | u_mes_prod_workInstructionStep | child | master | u_mes_prod_workInstruction | One document per step of a workInstruction | recordNo |
| 25 | u_mes_prod_workInstructionStepMediaControlledDocument | relationship | master | u_mes_prod_workInstructionStep | Links one workInstructionStep to one media controlled document (one document per link) | recordNo |
| 26 | u_mes_prod_workInstructionStepProductVariant | relationship | master | u_mes_prod_workInstructionStep | Links one workInstructionStep to one product variant (one document per link) | recordNo |
| 27 | u_mes_prod_workInstructionStepTool | relationship | master | u_mes_prod_workInstructionStep | Links one workInstructionStep to one tool (one document per link) | recordNo |
| 28 | u_mes_prod_workInstructionStepCharacteristic | relationship | master | u_mes_prod_workInstructionStep | Links one workInstructionStep to one characteristic (one document per link) | recordNo |
| 29 | u_mes_prod_workInstructionPpeItem | relationship | master | u_mes_prod_workInstruction | Links one workInstruction to one ppe item (one document per link) | recordNo |
| 30 | u_mes_prod_workInstructionKeyPoint | valueList | master | u_mes_prod_workInstruction | One document per key point value of a workInstruction | recordNo |
| 31 | u_mes_prod_recipe | entity | master | - | Machine parameter sets with set-points and limits (die temperature, furnace profile, CNC program, torque program, leak-test program) | name |
| 32 | u_mes_prod_recipeParameter | child | master | u_mes_prod_recipe | One document per parameter of a recipe | recordNo |
| 33 | u_mes_prod_recipeStage | child | master | u_mes_prod_recipe | One document per stage of a recipe | recordNo |
| 34 | u_mes_prod_engineeringChange | entity | transaction | - | Engineering change notices with affected objects, approvals and effectivity (cut-in serial / date) | title |
| 35 | u_mes_prod_engineeringChangeAffectedItem | child | transaction | u_mes_prod_engineeringChange | One document per affected item of a engineeringChange | recordNo |
| 36 | u_mes_prod_engineeringChangeAffectedObject | child | transaction | u_mes_prod_engineeringChange | One document per affected object of a engineeringChange | recordNo |
| 37 | u_mes_prod_engineeringChangeApproval | child | transaction | u_mes_prod_engineeringChange | One document per approval of a engineeringChange | recordNo |
| 38 | u_mes_prod_engineeringChangeControlledDocument | relationship | transaction | u_mes_prod_engineeringChange | Links one engineeringChange to one controlled document (one document per link) | recordNo |
| 39 | u_mes_prod_itemGroup | entity | master | - | Item groups (brake caliper, piston, seal, fastener ...) | name |
| 40 | u_mes_prod_itemFamily | entity | master | - | Product families a line is built for (front caliper, rear caliper) | name |
| 41 | u_mes_prod_ppeItem | entity | master | - | Personal protective equipment that a work instruction can require | name |
| 42 | u_mes_prod_market | entity | master | - | Sales markets of a product variant (domestic, export) | name |
| 43 | u_mes_prod_padCompound | entity | master | - | Brake pad friction compounds offered as a variant option | name |
| 44 | u_mes_prod_surfaceFinish | entity | master | - | Surface finishes offered as a variant option | name |
| 45 | u_mes_prod_vehicleModel | entity | master | - | Customer vehicle models the parts are fitted to | name |
| 46 | u_mes_prod_recipeProductVariant | relationship | master | u_mes_prod_recipe | Links one recipe to one product variant (one document per link) | recordNo |
| 47 | u_mes_prod_recipeControlledDocument | relationship | master | u_mes_prod_recipe | Links one recipe to one controlled document (one document per link) | recordNo |
| 48 | u_mes_prod_workInstructionWorkCenter | relationship | master | u_mes_prod_workInstruction | Links one workInstruction to one work center (one document per link) | recordNo |
| 49 | u_mes_prod_workInstructionProductVariant | relationship | master | u_mes_prod_workInstruction | Links one workInstruction to one product variant (one document per link) | recordNo |

## plan - PlanningAndExecution

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_plan_customerSchedule | entity | transaction | - | OEM delivery schedules / releases (demand that drives production orders and shipments) | recordNo |
| 2 | u_mes_plan_customerScheduleLine | child | transaction | u_mes_plan_customerSchedule | One document per line of a customerSchedule | recordNo |
| 3 | u_mes_plan_productionOrder | entity | transaction | - | Shop orders from ERP: item, quantity, routing/BOM version, partial releases, status | recordNo |
| 4 | u_mes_plan_productionOrderRelease | child | transaction | u_mes_plan_productionOrder | One document per release of a productionOrder | recordNo |
| 5 | u_mes_plan_productionOrderLot | relationship | transaction | u_mes_plan_productionOrder | Links one productionOrder to one lot (one document per link) | recordNo |
| 6 | u_mes_plan_productionSchedule | entity | transaction | - | Finite schedule per line and shift with sequenced orders, planned start/end | recordNo |
| 7 | u_mes_plan_productionScheduleSlot | child | transaction | u_mes_plan_productionSchedule | One document per slot of a productionSchedule | recordNo |
| 8 | u_mes_plan_dispatchList | entity | transaction | - | Prioritised work queue per work centre shown to the operator | recordNo |
| 9 | u_mes_plan_dispatchListEntry | child | transaction | u_mes_plan_dispatchList | One document per entry of a dispatchList | recordNo |
| 10 | u_mes_plan_operationExecution | entity | transaction | - | Start / complete record of an operation on a unit or lot: who, where, when, result, cycle time (track-in / track-out) | recordNo |
| 11 | u_mes_plan_operationExecutionDefectCode | relationship | transaction | u_mes_plan_operationExecution | Links one operationExecution to one defect code (one document per link) | recordNo |
| 12 | u_mes_plan_operationExecutionTool | relationship | transaction | u_mes_plan_operationExecution | Links one operationExecution to one tool (one document per link) | recordNo |
| 13 | u_mes_plan_stepCompletion | entity | transaction | - | Completion record for each work-instruction step: values entered, confirmations, duration, device data | recordNo |
| 14 | u_mes_plan_wipUnit | entity | transaction | - | Serialised unit in production (shop-floor control number): current operation, status, quality state | recordNo |
| 15 | u_mes_plan_wipUnitCompletedStep | valueList | transaction | u_mes_plan_wipUnit | One document per completed step value of a wipUnit | recordNo |
| 16 | u_mes_plan_lot | entity | transaction | - | Lots and batches: supplier lots, melt/heat lots, casting lots, heat-treatment charges, anodising loads | recordNo |
| 17 | u_mes_plan_lotParentLot | relationship | transaction | u_mes_plan_lot | Links one lot to one parent lot (one document per link) | recordNo |
| 18 | u_mes_plan_lotAttributesCavityNo | valueList | transaction | u_mes_plan_lot | One document per attributes cavity no value of a lot | recordNo |
| 19 | u_mes_plan_container | entity | transaction | - | Bins, trolleys, returnable crates and pallets with contents and nesting | recordNo |
| 20 | u_mes_plan_containerLot | relationship | transaction | u_mes_plan_container | Links one container to one lot (one document per link) | recordNo |
| 21 | u_mes_plan_labourBooking | entity | transaction | - | Clock-on / clock-off of people against orders, operations and indirect activities | recordNo |
| 22 | u_mes_plan_changeover | entity | transaction | - | Changeover from one item / variant to another: planned vs actual duration, checklist, first-off approval | recordNo |
| 23 | u_mes_plan_changeoverStep | child | transaction | u_mes_plan_changeover | One document per step of a changeover | recordNo |
| 24 | u_mes_plan_changeoverRemovedTool | relationship | transaction | u_mes_plan_changeover | Links one changeover to one removed tool (one document per link) | recordNo |
| 25 | u_mes_plan_changeoverInstalledTool | relationship | transaction | u_mes_plan_changeover | Links one changeover to one installed tool (one document per link) | recordNo |
| 26 | u_mes_plan_changeoverPerformedByUser | relationship | transaction | u_mes_plan_changeover | Links one changeover to one performed by user (one document per link) | recordNo |
| 27 | u_mes_plan_shiftHandover | entity | transaction | - | Shift logbook: output, open issues, safety and quality notes, acknowledgements | recordNo |
| 28 | u_mes_plan_shiftHandoverProductionOrder | relationship | transaction | u_mes_plan_shiftHandover | Links one shiftHandover to one production order (one document per link) | recordNo |
| 29 | u_mes_plan_shiftHandoverDowntimeEvent | relationship | transaction | u_mes_plan_shiftHandover | Links one shiftHandover to one downtime event (one document per link) | recordNo |
| 30 | u_mes_plan_shiftHandoverNonconformance | relationship | transaction | u_mes_plan_shiftHandover | Links one shiftHandover to one nonconformance (one document per link) | recordNo |
| 31 | u_mes_plan_shiftHandoverOpenItem | child | transaction | u_mes_plan_shiftHandover | One document per open item of a shiftHandover | recordNo |
| 32 | u_mes_plan_andonEvent | entity | transaction | - | Help calls from stations (quality, material, maintenance, safety) with response and escalation times | description |
| 33 | u_mes_plan_andonEventEscalation | child | transaction | u_mes_plan_andonEvent | One document per escalation of a andonEvent | recordNo |
| 34 | u_mes_plan_indirectActivity | entity | master | - | Indirect labour activities (cleaning, training, waiting for material ...) | name |
| 35 | u_mes_plan_containerType | entity | master | - | Types of container with dimensions and tare weight | name |
| 36 | u_mes_plan_andonType | entity | master | - | Types of andon call with responsible department and target response time | name |
| 37 | u_mes_plan_operatorSession | entity | transaction | - | One login-to-logout session of an operator at a station, with the authentication method and the checks done at login. | recordNo |
| 38 | u_mes_plan_documentAcknowledgement | entity | transaction | - | Operator confirmation that a specific revision of a work instruction, recipe or controlled document was read at a station. | recordNo |
| 39 | u_mes_plan_interlockEvent | entity | transaction | - | Every time an interlock rule blocks a transaction, is overridden or is cleared: what was checked, expected and found, and who authorised the override. | recordNo |
| 40 | u_mes_plan_recipeDownload | entity | transaction | - | Each download or selection of a program / recipe on a machine with the checksum verification result. | recordNo |
| 41 | u_mes_plan_setupVerification | entity | transaction | - | Pre-start verification of the set-up of a station or machine against the order, variant and bill of process. | recordNo |
| 42 | u_mes_plan_setupVerificationItem | child | transaction | u_mes_plan_setupVerification | One document per item of a setupVerification | recordNo |
| 43 | u_mes_plan_lineClearance | entity | transaction | - | Check that a line or station is free of materials, labels, documents and product of the previous order before the next order starts, with a second-person verification. | recordNo |

## matl - MaterialManagement

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_matl_storageLocation | entity | master | - | Warehouses, racks, line-side supermarkets, quarantine cage, dispatch bay | name |
| 2 | u_mes_matl_inventoryBalance | entity | transaction | - | Stock on hand per item, lot, location and stock status | recordNo |
| 3 | u_mes_matl_materialMovement | entity | transaction | - | Every stock transaction: receipt, putaway, issue to line, return, scrap, transfer, shipment | recordNo |
| 4 | u_mes_matl_goodsReceipt | entity | transaction | - | Receipts from suppliers with lines, supplier lot, certificate, incoming inspection status | recordNo |
| 5 | u_mes_matl_goodsReceiptLine | child | transaction | u_mes_matl_goodsReceipt | One document per line of a goodsReceipt | recordNo |
| 6 | u_mes_matl_goodsReceiptLineInspectionResult | relationship | transaction | u_mes_matl_goodsReceiptLine | Links one goodsReceiptLine to one inspection result (one document per link) | recordNo |
| 7 | u_mes_matl_kit | entity | transaction | - | Kits of components picked for an order / line-side delivery | recordNo |
| 8 | u_mes_matl_kitLine | child | transaction | u_mes_matl_kit | One document per line of a kit | recordNo |
| 9 | u_mes_matl_materialRequest | entity | transaction | - | Line-side replenishment calls (e-kanban) from a work centre to stores | recordNo |
| 10 | u_mes_matl_materialConsumption | entity | transaction | - | Component / lot consumed at an operation on a unit or lot (backflush or scanned) | recordNo |
| 11 | u_mes_matl_packagingSpecification | entity | master | - | Pack instruction: container type, quantity per bin, layers, dunnage, label template | recordNo |
| 12 | u_mes_matl_packagingSpecificationLevel | child | master | u_mes_matl_packagingSpecification | One document per level of a packagingSpecification | recordNo |
| 13 | u_mes_matl_labelTemplate | entity | master | - | Label layouts (unit 2D code, bin label, customer shipping label, hold tag) | name |
| 14 | u_mes_matl_labelTemplateField | child | master | u_mes_matl_labelTemplate | One document per field of a labelTemplate | recordNo |
| 15 | u_mes_matl_label | entity | transaction | - | Printed label instances with payload, printer, reprint count | recordNo |
| 16 | u_mes_matl_shipment | entity | transaction | - | Dispatch to customer: invoice / ASN, vehicle, containers shipped, proof of delivery | recordNo |
| 17 | u_mes_matl_shipmentLine | child | transaction | u_mes_matl_shipment | One document per line of a shipment | recordNo |
| 18 | u_mes_matl_shipmentLineContainer | relationship | transaction | u_mes_matl_shipmentLine | Links one shipmentLine to one container (one document per link) | recordNo |
| 19 | u_mes_matl_shipmentLineLot | relationship | transaction | u_mes_matl_shipmentLine | Links one shipmentLine to one lot (one document per link) | recordNo |
| 20 | u_mes_matl_movementType | entity | master | - | Stock movement types with their ERP movement code and stock effect | name |
| 21 | u_mes_matl_stockStatus | entity | master | - | Stock statuses (unrestricted, quality inspection, blocked, reserved) | name |
| 22 | u_mes_matl_packType | entity | master | - | Pack levels used in packaging specifications (bag, tray, bin, pallet) | name |
| 23 | u_mes_matl_exposureTimer | entity | transaction | - | Floor-life, pot-life or open-time clock for a lot or container of an exposure-controlled item. | recordNo |
| 24 | u_mes_matl_replenishmentRule | entity | master | - | Min-max or e-Kanban rule for replenishing an item at a line-side location. | recordNo |
| 25 | u_mes_matl_materialDemandForecast | entity | transaction | - | Short-term component demand and projected line-side shortage per item, line and time bucket. | recordNo |
| 26 | u_mes_matl_storageLocationAllowedItem | relationship | master | u_mes_matl_storageLocation | Links one storageLocation to one allowed item (one document per link) | recordNo |
| 27 | u_mes_matl_dispenseRecord | entity | transaction | - | Weighing or counting of a material lot for an order, with target, tolerance, tare, gross and net weight and the second-person or system verification. | recordNo |

## trac - Traceability

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_trac_serialNumber | entity | transaction | - | Registry of every serial / 2D code issued: status, mark grade, unit and shipment linkage | recordNo |
| 2 | u_mes_trac_genealogyLink | entity | transaction | - | As-built parent-child edges: unit to component serial or component lot, with operation and time | recordNo |
| 3 | u_mes_trac_componentLotLink | entity | transaction | - | Lot-to-lot lineage: ingot heat to melt to casting lot to heat-treatment charge to anodising load; split and merge | recordNo |
| 4 | u_mes_trac_asBuiltRecord | entity | transaction | - | Device-history summary per shipped unit: components, key results, operators, sign-off (digital birth certificate) | recordNo |
| 5 | u_mes_trac_asBuiltRecordComponent | child | transaction | u_mes_trac_asBuiltRecord | One document per component of a asBuiltRecord | recordNo |
| 6 | u_mes_trac_asBuiltRecordOperation | child | transaction | u_mes_trac_asBuiltRecord | One document per operation of a asBuiltRecord | recordNo |
| 7 | u_mes_trac_asBuiltRecordInspectionResult | relationship | transaction | u_mes_trac_asBuiltRecord | Links one asBuiltRecord to one inspection result (one document per link) | recordNo |
| 8 | u_mes_trac_traceInvestigation | entity | transaction | - | A saved forward or reverse trace run, its starting object and the containment it fed. | title |
| 9 | u_mes_trac_traceInvestigationResult | child | transaction | u_mes_trac_traceInvestigation | One document per result of a traceInvestigation | recordNo |

## qual - QualityManagement

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_qual_characteristic | entity | master | - | Product and process characteristics with nominal, tolerance, class (critical / significant), method | name |
| 2 | u_mes_qual_controlPlan | entity | master | - | AIAG control plan per item and phase (prototype, pre-launch, production) | recordNo |
| 3 | u_mes_qual_controlPlanCoreTeamUser | relationship | master | u_mes_qual_controlPlan | Links one controlPlan to one core team user (one document per link) | recordNo |
| 4 | u_mes_qual_controlPlanLine | child | master | u_mes_qual_controlPlan | One document per line of a controlPlan | recordNo |
| 5 | u_mes_qual_inspectionPlan | entity | master | - | Executable data-collection group per operation: which characteristics, sample size, frequency, reaction | name |
| 6 | u_mes_qual_inspectionPlanLine | child | master | u_mes_qual_inspectionPlan | One document per line of a inspectionPlan | recordNo |
| 7 | u_mes_qual_samplingPlan | entity | master | - | Sampling rules: AQL tables, skip-lot, time or counter based frequency | name |
| 8 | u_mes_qual_samplingPlanSizeRow | child | master | u_mes_qual_samplingPlan | One document per size row of a samplingPlan | recordNo |
| 9 | u_mes_qual_checkSheet | entity | master | - | Check sheet definitions: start-of-shift checks, poka-yoke verification, first-off, autonomous maintenance | name |
| 10 | u_mes_qual_checkSheetItem | child | master | u_mes_qual_checkSheet | One document per item of a checkSheet | recordNo |
| 11 | u_mes_qual_checkSheetResult | entity | transaction | - | Completed check sheets with answers, failures and reactions | recordNo |
| 12 | u_mes_qual_checkSheetResultAnswer | child | transaction | u_mes_qual_checkSheetResult | One document per answer of a checkSheetResult | recordNo |
| 13 | u_mes_qual_inspectionResult | entity | transaction | - | Measured and attribute results per unit / lot / receipt against a characteristic | recordNo |
| 14 | u_mes_qual_spcChart | entity | master | - | Chart definition per characteristic and work centre: chart type, subgroup size, control limits, rules | name |
| 15 | u_mes_qual_spcChartControlLimit | child | master | u_mes_qual_spcChart | One document per control limit of a spcChart | recordNo |
| 16 | u_mes_qual_spcChartRule | valueList | master | u_mes_qual_spcChart | One document per rule value of a spcChart | recordNo |
| 17 | u_mes_qual_spcSample | entity | transaction | - | Subgroups with readings, mean, range, rule violations and reaction | recordNo |
| 18 | u_mes_qual_spcSampleReading | valueList | transaction | u_mes_qual_spcSample | One document per reading value of a spcSample | recordNo |
| 19 | u_mes_qual_spcSampleInspectionResult | relationship | transaction | u_mes_qual_spcSample | Links one spcSample to one inspection result (one document per link) | recordNo |
| 20 | u_mes_qual_spcSampleViolation | child | transaction | u_mes_qual_spcSample | One document per violation of a spcSample | recordNo |
| 21 | u_mes_qual_defectCode | entity | master | - | Defect / NC code catalogue with group, default disposition routing and severity | name |
| 22 | u_mes_qual_defectCodeApplicableOperation | relationship | master | u_mes_qual_defectCode | Links one defectCode to one applicable operation (one document per link) | recordNo |
| 23 | u_mes_qual_nonconformance | entity | transaction | - | Nonconformance reports: what, where, quantity, containment, disposition (use-as-is, rework, scrap, return) | title |
| 24 | u_mes_qual_nonconformanceAffectedObject | child | transaction | u_mes_qual_nonconformance | One document per affected object of a nonconformance | recordNo |
| 25 | u_mes_qual_nonconformanceContainmentAction | child | transaction | u_mes_qual_nonconformance | One document per containment action of a nonconformance | recordNo |
| 26 | u_mes_qual_nonconformanceInspectionResult | relationship | transaction | u_mes_qual_nonconformance | Links one nonconformance to one inspection result (one document per link) | recordNo |
| 27 | u_mes_qual_nonconformanceReworkOrder | relationship | transaction | u_mes_qual_nonconformance | Links one nonconformance to one rework order (one document per link) | recordNo |
| 28 | u_mes_qual_nonconformanceScrapRecord | relationship | transaction | u_mes_qual_nonconformance | Links one nonconformance to one scrap record (one document per link) | recordNo |
| 29 | u_mes_qual_nonconformancePhotoControlledDocument | relationship | transaction | u_mes_qual_nonconformance | Links one nonconformance to one photo controlled document (one document per link) | recordNo |
| 30 | u_mes_qual_nonconformanceMrbUser | relationship | transaction | u_mes_qual_nonconformance | Links one nonconformance to one mrb user (one document per link) | recordNo |
| 31 | u_mes_qual_reworkOrder | entity | transaction | - | Rework instruction and execution on the rework routing with re-inspection result | recordNo |
| 32 | u_mes_qual_reworkOrderWipUnit | relationship | transaction | u_mes_qual_reworkOrder | Links one reworkOrder to one wip unit (one document per link) | recordNo |
| 33 | u_mes_qual_reworkOrderStep | child | transaction | u_mes_qual_reworkOrder | One document per step of a reworkOrder | recordNo |
| 34 | u_mes_qual_scrapRecord | entity | transaction | - | Scrap declaration with quantity, weight, cost, defect code and operation of origin | recordNo |
| 35 | u_mes_qual_qualityHold | entity | transaction | - | Hold / quarantine on units, lots, containers or locations with reason and release decision | recordNo |
| 36 | u_mes_qual_qualityHoldHeldObject | child | transaction | u_mes_qual_qualityHold | One document per held object of a qualityHold | recordNo |
| 37 | u_mes_qual_deviationPermit | entity | transaction | - | Temporary deviations / concessions approved by the customer with quantity or date limit | title |
| 38 | u_mes_qual_deviationPermitApproval | child | transaction | u_mes_qual_deviationPermit | One document per approval of a deviationPermit | recordNo |
| 39 | u_mes_qual_capa | entity | transaction | - | Corrective and preventive actions in 8D structure (D1-D8) with team, root cause, actions, verification | title |
| 40 | u_mes_qual_capaNonconformance | relationship | transaction | u_mes_qual_capa | Links one capa to one nonconformance (one document per link) | recordNo |
| 41 | u_mes_qual_capaTeamMember | child | transaction | u_mes_qual_capa | One document per team member of a capa | recordNo |
| 42 | u_mes_qual_capaContainmentAction | child | transaction | u_mes_qual_capa | One document per containment action of a capa | recordNo |
| 43 | u_mes_qual_capaCorrectiveAction | child | transaction | u_mes_qual_capa | One document per corrective action of a capa | recordNo |
| 44 | u_mes_qual_capaImplementationAction | child | transaction | u_mes_qual_capa | One document per implementation action of a capa | recordNo |
| 45 | u_mes_qual_capaControlledDocument | relationship | transaction | u_mes_qual_capa | Links one capa to one controlled document (one document per link) | recordNo |
| 46 | u_mes_qual_pfmea | entity | master | - | Process FMEA per item / process: failure modes, effects, causes, S-O-D, action priority | title |
| 47 | u_mes_qual_pfmeaCoreTeamUser | relationship | master | u_mes_qual_pfmea | Links one pfmea to one core team user (one document per link) | recordNo |
| 48 | u_mes_qual_pfmeaLine | child | master | u_mes_qual_pfmea | One document per line of a pfmea | recordNo |
| 49 | u_mes_qual_ppapSubmission | entity | transaction | - | PPAP package: level, 18 elements with status, PSW, customer decision | recordNo |
| 50 | u_mes_qual_ppapSubmissionElement | child | transaction | u_mes_qual_ppapSubmission | One document per element of a ppapSubmission | recordNo |
| 51 | u_mes_qual_ppapSubmissionMsaStudy | relationship | transaction | u_mes_qual_ppapSubmission | Links one ppapSubmission to one msa study (one document per link) | recordNo |
| 52 | u_mes_qual_gauge | entity | master | - | Gauges and measuring instruments: type, range, resolution, calibration interval and due date, status | name |
| 53 | u_mes_qual_gaugeCalibration | entity | transaction | - | Calibration events: as-found / as-left readings, standard used, result, certificate | recordNo |
| 54 | u_mes_qual_gaugeCalibrationReading | child | transaction | u_mes_qual_gaugeCalibration | One document per reading of a gaugeCalibration | recordNo |
| 55 | u_mes_qual_msaStudy | entity | transaction | - | Measurement system analysis: gauge R&R, bias, linearity, attribute agreement | recordNo |
| 56 | u_mes_qual_msaStudyAppraiserUser | relationship | transaction | u_mes_qual_msaStudy | Links one msaStudy to one appraiser user (one document per link) | recordNo |
| 57 | u_mes_qual_msaStudyTrial | child | transaction | u_mes_qual_msaStudy | One document per trial of a msaStudy | recordNo |
| 58 | u_mes_qual_audit | entity | transaction | - | Layered process, process (VDA 6.3), product and system audits with findings | title |
| 59 | u_mes_qual_auditAuditorUser | relationship | transaction | u_mes_qual_audit | Links one audit to one auditor user (one document per link) | recordNo |
| 60 | u_mes_qual_auditFinding | child | transaction | u_mes_qual_audit | One document per finding of a audit | recordNo |
| 61 | u_mes_qual_customerComplaint | entity | transaction | - | Customer complaints / line rejections / warranty returns with affected serials and PPM impact | description |
| 62 | u_mes_qual_customerComplaintSerialNumber | relationship | transaction | u_mes_qual_customerComplaint | Links one customerComplaint to one serial number (one document per link) | recordNo |
| 63 | u_mes_qual_customerComplaintShipment | relationship | transaction | u_mes_qual_customerComplaint | Links one customerComplaint to one shipment (one document per link) | recordNo |
| 64 | u_mes_qual_customerComplaintSuspectLot | relationship | transaction | u_mes_qual_customerComplaint | Links one customerComplaint to one suspect lot (one document per link) | recordNo |
| 65 | u_mes_qual_customerComplaintCommunication | child | transaction | u_mes_qual_customerComplaint | One document per communication of a customerComplaint | recordNo |
| 66 | u_mes_qual_defectGroup | entity | master | - | Groups of defect codes (casting, machining, leak, torque ...) | name |
| 67 | u_mes_qual_gaugeType | entity | master | - | Types of gauge and measuring instrument | name |
| 68 | u_mes_qual_dispositionType | entity | master | - | Dispositions for nonconforming material (use as is, rework, scrap, return, sort) | name |
| 69 | u_mes_qual_complaintType | entity | master | - | Types of customer complaint (line rejection, zero kilometre, warranty, logistics) | name |
| 70 | u_mes_qual_characteristicPosition | child | master | u_mes_qual_characteristic | One document per position of a characteristic | recordNo |
| 71 | u_mes_qual_curveEnvelope | entity | master | - | Approved golden-sample envelope for a force–displacement, torque–angle, pressure–time or signal curve. | name |
| 72 | u_mes_qual_curveEnvelopeWindow | child | master | u_mes_qual_curveEnvelope | One document per window of a curveEnvelope | recordNo |
| 73 | u_mes_qual_measurementCurve | entity | transaction | - | One captured curve per unit, position and test, with the envelope verdict and summary values. | recordNo |
| 74 | u_mes_qual_measurementCurvePoint | entity | transaction | - | Points of a measurement curve. Created as a MongoDB time-series collection: timeField `sampledAt`, metaField `measurementCurveId`, granularity seconds. | recordNo |
| 75 | u_mes_qual_defectRecord | entity | transaction | - | One logged defect on one unit (or lot sample) with first-fail station, origin, 4M category and follow-up links. | recordNo |
| 76 | u_mes_qual_auditSchedule | entity | master | - | Plan for layered process audits (and other recurring audits): layer, area or line, check sheet, frequency and auditor. | name |
| 77 | u_mes_qual_inspectionPlanProductVariant | relationship | master | u_mes_qual_inspectionPlan | Links one inspectionPlan to one product variant (one document per link) | recordNo |
| 78 | u_mes_qual_environmentalMonitoringPoint | entity | master | - | A monitored location and parameter in a controlled area, with its alert and action limits and sampling frequency. | name |
| 79 | u_mes_qual_environmentalMonitoringResult | entity | transaction | - | One environmental monitoring result with its evaluation against alert and action limits and the excursion handling. | recordNo |
| 80 | u_mes_qual_retentionSample | entity | transaction | - | Reserve or retention sample taken from a lot, with quantity, storage location, retention date and withdrawals. | recordNo |
| 81 | u_mes_qual_riskAssessment | entity | transaction | - | Documented quality risk assessment of a change, system, deviation, equipment or product: method, initial and residual risk, controls and acceptance. | title |
| 82 | u_mes_qual_productQualityReview | entity | transaction | - | Periodic product quality review of an item: lots made, released and rejected, deviations, complaints, CAPA, changes, recalls and capability over the review period, with conclusion and actions. | recordNo |
| 83 | u_mes_qual_productRecall | entity | transaction | - | Recall or field action for product already shipped: class, scope, reason, linked complaint, investigation and trace, quantities shipped and recovered, authority notification and effectiveness check. | title |
| 84 | u_mes_qual_productRecallLot | child | transaction | u_mes_qual_productRecall | One document per lot of a productRecall | recordNo |
| 85 | u_mes_qual_processValidation | entity | transaction | - | Process validation study of an item on a line by lifecycle stage (process design, process qualification, continued process verification), with protocol, lots, acceptance criteria and result. | title |

## perf - PerformanceManagement

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_perf_reasonCode | entity | master | - | Reason tree (up to 4 levels) for downtime, scrap, hold and andon with planned / unplanned category | name |
| 2 | u_mes_perf_equipmentState | entity | transaction | - | State intervals per equipment: running, idle, setup, down, starved, blocked | recordNo |
| 3 | u_mes_perf_downtimeEvent | entity | transaction | - | Classified stops with fault, reason path, action taken, duration, responsible group | recordNo |
| 4 | u_mes_perf_downtimeEventComment | child | transaction | u_mes_perf_downtimeEvent | One document per comment of a downtimeEvent | recordNo |
| 5 | u_mes_perf_productionCount | entity | transaction | - | Hourly good / reject / rework counts per work centre against target (hour-by-hour board) | recordNo |
| 6 | u_mes_perf_oeeRecord | entity | transaction | - | OEE per equipment / line and shift: availability, performance, quality with the time and count basis | recordNo |
| 7 | u_mes_perf_oeeRecordLoss | child | transaction | u_mes_perf_oeeRecord | One document per loss of a oeeRecord | recordNo |
| 8 | u_mes_perf_processTag | entity | master | - | Tag definitions: source address, unit, deadband, limits, equipment | description |
| 9 | u_mes_perf_processReading | entity | transaction | - | Tag values over time (die temperature, furnace zone temperature, spindle load, bath pH, current) | recordNo |
| 10 | u_mes_perf_alarm | entity | transaction | - | Alarm occurrences with severity, raised / acknowledged / cleared times | recordNo |
| 11 | u_mes_perf_torqueResult | entity | transaction | - | Tightening results per unit: program, final torque, angle, status, curve reference | recordNo |
| 12 | u_mes_perf_leakTestResult | entity | transaction | - | Leak test per unit: stage pressures, decay, leak rate, limits, verdict, retest counter | recordNo |
| 13 | u_mes_perf_leakTestResultStage | child | transaction | u_mes_perf_leakTestResult | One document per stage of a leakTestResult | recordNo |
| 14 | u_mes_perf_energyReading | entity | transaction | - | Interval energy, compressed air and gas consumption per meter and equipment | recordNo |
| 15 | u_mes_perf_lossCategory | entity | master | - | OEE loss categories with the OEE factor they reduce | name |
| 16 | u_mes_perf_reasonCategory | entity | master | - | Categories of reason codes (mechanical, electrical, process, material ...) | name |
| 17 | u_mes_perf_energyType | entity | master | - | Types of energy and utility that are metered | name |
| 18 | u_mes_perf_alarmDefinition | entity | master | - | Alarm code master per equipment type with class, severity, restart-block and escalation settings. | recordNo |
| 19 | u_mes_perf_lossSummary | entity | transaction | - | Loss Pareto row per line, shift, production date and reason code (downtime, speed and quality losses). | recordNo |
| 20 | u_mes_perf_workCenterPerformance | entity | transaction | - | Hourly station performance: throughput, cycle time against takt, WIP, blocked and starved time and constraint flag. | recordNo |
| 21 | u_mes_perf_operatorPerformance | entity | transaction | - | Labour efficiency per operator, station, variant, shift and date. | recordNo |

## maint - ToolingAndMaintenance

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_maint_maintenancePlan | entity | master | - | Preventive / condition-based plans per equipment or tool with tasks, interval and next due | name |
| 2 | u_mes_maint_maintenancePlanTask | child | master | u_mes_maint_maintenancePlan | One document per task of a maintenancePlan | recordNo |
| 3 | u_mes_maint_maintenancePlanRequiredSkill | relationship | master | u_mes_maint_maintenancePlan | Links one maintenancePlan to one required skill (one document per link) | recordNo |
| 4 | u_mes_maint_maintenancePlanRequiredSparePart | child | master | u_mes_maint_maintenancePlan | One document per required spare part of a maintenancePlan | recordNo |
| 5 | u_mes_maint_maintenanceWorkOrder | entity | transaction | - | Breakdown, preventive and improvement work orders with labour, parts used, root cause | title |
| 6 | u_mes_maint_maintenanceWorkOrderAssignedToUser | relationship | transaction | u_mes_maint_maintenanceWorkOrder | Links one maintenanceWorkOrder to one assigned to user (one document per link) | recordNo |
| 7 | u_mes_maint_maintenanceWorkOrderLabour | child | transaction | u_mes_maint_maintenanceWorkOrder | One document per labour of a maintenanceWorkOrder | recordNo |
| 8 | u_mes_maint_maintenanceWorkOrderUsedSparePart | child | transaction | u_mes_maint_maintenanceWorkOrder | One document per used spare part of a maintenanceWorkOrder | recordNo |
| 9 | u_mes_maint_sparePart | entity | master | - | Maintenance spares with stock, minimum, location, where-used | description |
| 10 | u_mes_maint_sparePartUsedOnEquipment | relationship | master | u_mes_maint_sparePart | Links one sparePart to one used on equipment (one document per link) | recordNo |
| 11 | u_mes_maint_tool | entity | master | - | Dies, fixtures, cutting tools, nutrunner spindles, test seals: life limit, life used, status, location | name |
| 12 | u_mes_maint_toolItem | relationship | master | u_mes_maint_tool | Links one tool to one item (one document per link) | recordNo |
| 13 | u_mes_maint_toolLifeRecord | entity | transaction | - | Tool mount / dismount / usage / regrind events with shots or cycles consumed | recordNo |
| 14 | u_mes_maint_toolType | entity | master | - | Types of tool (die, fixture, cutting tool, socket, test seal) | name |
| 15 | u_mes_maint_maintenanceWorkOrderTask | child | transaction | u_mes_maint_maintenanceWorkOrder | One document per task of a maintenanceWorkOrder | recordNo |
| 16 | u_mes_maint_sparePartTransaction | entity | transaction | - | Spare-part issue, return, receipt, adjustment and scrap with work order and equipment. | recordNo |
| 17 | u_mes_maint_reliabilitySummary | entity | transaction | - | MTBF and MTTR per equipment, line and period. | recordNo |
| 18 | u_mes_maint_equipmentLifecycleEvent | entity | transaction | - | Lifecycle events of an equipment: commissioning, relocation, overhaul, refurbishment, upgrade, health assessment, replacement recommendation, decommissioning. | description |
| 19 | u_mes_maint_logbookEntry | entity | transaction | - | Chronological use log of a piece of equipment or an area: production, cleaning, maintenance, calibration, line clearance, qualification and idle periods, with the order and lot concerned. | recordNo |
| 20 | u_mes_maint_cleaningRecord | entity | transaction | - | Cleaning of a piece of equipment after use or before a product change: procedure, dirty hold time, cleaning, verification and the clean hold time it opens. | recordNo |
| 21 | u_mes_maint_equipmentQualification | entity | transaction | - | Qualification of a piece of equipment by phase (design, installation, operational, performance, periodic requalification), with protocol, tests, deviations, approval and the next requalification date. | recordNo |

## syst - SystemAndIntegration

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_syst_erpMessage | entity | transaction | - | Inbound and outbound interface messages (order download, confirmation, goods movement) with payload, status, retries | recordNo |
| 2 | u_mes_syst_integrationConnector | entity | master | - | Connector definitions to ERP, PLM, OPC UA servers, tool controllers, label printers | name |
| 3 | u_mes_syst_integrationConnectorFunction | child | master | u_mes_syst_integrationConnector | One document per function of a integrationConnector | recordNo |
| 4 | u_mes_syst_iotDevice | entity | master | - | Registry of PLCs, gateways, nutrunner controllers, leak testers, scanners, printers, energy meters | name |
| 5 | u_mes_syst_operatorApp | entity | master | - | Composable operator screen definitions (versioned) bound to work centres and operations | name |
| 6 | u_mes_syst_operatorAppWorkCenter | relationship | master | u_mes_syst_operatorApp | Links one operatorApp to one work center (one document per link) | recordNo |
| 7 | u_mes_syst_operatorAppOperation | relationship | master | u_mes_syst_operatorApp | Links one operatorApp to one operation (one document per link) | recordNo |
| 8 | u_mes_syst_operatorAppStep | child | master | u_mes_syst_operatorApp | One document per step of a operatorApp | recordNo |
| 9 | u_mes_syst_operatorAppStepTrigger | child | master | u_mes_syst_operatorAppStep | One document per trigger of a operatorAppStep | recordNo |
| 10 | u_mes_syst_operatorAppDeviceBinding | child | master | u_mes_syst_operatorApp | One document per device binding of a operatorApp | recordNo |
| 11 | u_mes_syst_operatorAppLanguage | relationship | master | u_mes_syst_operatorApp | Links one operatorApp to one language (one document per link) | recordNo |
| 12 | u_mes_syst_businessEvent | entity | transaction | - | Business event stream (order released, unit started, recipe downloaded, hold placed) | recordNo |
| 13 | u_mes_syst_auditTrail | entity | transaction | - | Field-level change history of master and quality data (who, when, old, new, reason) | recordNo |
| 14 | u_mes_syst_auditTrailChange | child | transaction | u_mes_syst_auditTrail | One document per change of a auditTrail | recordNo |
| 15 | u_mes_syst_electronicSignature | entity | transaction | - | Signature records for approvals and releases with meaning and signed-content hash | recordNo |
| 16 | u_mes_syst_notification | entity | transaction | - | Alerts and escalations sent to users / groups with delivery and acknowledgement status | title |
| 17 | u_mes_syst_notificationRecipient | child | transaction | u_mes_syst_notification | One document per recipient of a notification | recordNo |
| 18 | u_mes_syst_controlledDocument | entity | transaction | - | Controlled documents and attachments metadata (drawings, certificates, photos, reports); file in object store | title |
| 19 | u_mes_syst_controlledDocumentTag | valueList | transaction | u_mes_syst_controlledDocument | One document per tag value of a controlledDocument | recordNo |
| 20 | u_mes_syst_numberRange | entity | master | - | Counters and format masks for serials, lots, orders, labels, NCRs | name |
| 21 | u_mes_syst_systemConfiguration | entity | master | - | Site and module settings (OEE basis, SPC rules, retention, label printer mapping) | description |
| 22 | u_mes_syst_documentType | entity | master | - | Types of controlled document with retention | name |
| 23 | u_mes_syst_deviceType | entity | master | - | Types of connected device (PLC, nutrunner controller, leak tester, printer ...) | name |
| 24 | u_mes_syst_notificationType | entity | master | - | Types of notification sent by the system | name |
| 25 | u_mes_syst_statusDefinition | entity | master | - | Status values and allowed transitions per collection (status mapping) | statusName |
| 26 | u_mes_syst_enumerationValue | entity | master | - | Allowed values of fixed enumeration keys, one document per collection, key and value | valueName |
| 27 | u_mes_syst_statusTransition | entity | master | - | Status values and allowed transitions per collection (status mapping) | transitionName |
| 28 | u_mes_syst_interlockRule | entity | master | - | Configured check that the application must pass before a transaction is allowed, with its scope and override policy. | name |
| 29 | u_mes_syst_statusTransitionRole | relationship | master | u_mes_syst_statusTransition | Links one statusTransition to one role (one document per link) | recordNo |
| 30 | u_mes_syst_escalationRule | entity | master | - | Routing and SLA rule for an exception type: first owner role, response and resolution targets. | name |
| 31 | u_mes_syst_escalationRuleLevel | child | master | u_mes_syst_escalationRule | One document per level of a escalationRule | recordNo |
| 32 | u_mes_syst_alertRule | entity | master | - | Threshold rule on a KPI or signal with the resulting action. | name |
| 33 | u_mes_syst_analyticsModel | entity | master | - | Registry of AI / ML / rule models and their released versions. | name |
| 34 | u_mes_syst_modelPrediction | entity | transaction | - | Each prediction, classification, forecast or recommendation produced by a model, with the action and the actual outcome. | recordNo |
| 35 | u_mes_syst_simulationStudy | entity | transaction | - | Digital-twin / what-if study with its input snapshot, result, approval and controlled rollout and pre / post comparison. | title |
| 36 | u_mes_syst_recordPolicy | entity | master | - | Edit, lock and retention policy per collection. | recordNo |
| 37 | u_mes_syst_savedView | entity | master | - | Saved dashboard and comparison filters per user or role. | name |
| 38 | u_mes_syst_backupRun | entity | transaction | - | Evidence of database backups and restore tests with measured recovery time (optional). | recordNo |
| 39 | u_mes_syst_computerisedSystem | entity | master | - | Inventory of the computerised systems that create, hold or process GMP records, with their GxP impact, GAMP category, owners and periodic review cycle. | name |
| 40 | u_mes_syst_systemValidation | entity | transaction | - | One validation or computer software assurance activity on a computerised system: initial validation, revalidation after a change, or decommissioning, with its test evidence and approval. | title |
| 41 | u_mes_syst_systemPeriodicReview | entity | transaction | - | Periodic evaluation that a computerised system remains in a validated state: changes, incidents, deviations, audit trails, access and backup over the review period. | recordNo |
| 42 | u_mes_syst_auditTrailReview | entity | transaction | - | Documented review of the audit-trail entries of a production record, a system or an investigation: period, number of entries, critical entries, anomalies and outcome. | recordNo |
| 43 | u_mes_syst_userAccessReview | entity | transaction | - | Periodic review of the user accounts and roles of a computerised system, confirming that every account is still needed and has the right authority. | recordNo |
| 44 | u_mes_syst_userAccessReviewLine | child | transaction | u_mes_syst_userAccessReview | One document per line of a userAccessReview | recordNo |

## ehs - EnvironmentHealthAndSafety

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_ehs_safetyIncident | entity | transaction | - | Near misses, unsafe conditions, first-aid and lost-time incidents with investigation and actions | title |
| 2 | u_mes_ehs_safetyIncidentWitnessUser | relationship | transaction | u_mes_ehs_safetyIncident | Links one safetyIncident to one witness user (one document per link) | recordNo |
| 3 | u_mes_ehs_safetyIncidentAction | child | transaction | u_mes_ehs_safetyIncident | One document per action of a safetyIncident | recordNo |
| 4 | u_mes_ehs_incidentType | entity | master | - | Types of safety incident | name |
| 5 | u_mes_ehs_bodyPart | entity | master | - | Body parts for injury records | name |
| 6 | u_mes_ehs_injuryType | entity | master | - | Types of injury | name |

## bmr - BatchManufacturingRecord

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_bmr_batchRecordReview | entity | transaction | - | Review of the electronic production record of an order before release: production review, quality review by exception, exceptions found and their closure. | recordNo |
| 2 | u_mes_bmr_batchRecordReviewException | child | transaction | u_mes_bmr_batchRecordReview | One document per exception of a batchRecordReview | recordNo |
| 3 | u_mes_bmr_batchRelease | entity | transaction | - | Release decision of the quality unit for a lot after review of its production record: released, conditionally released under a deviation, or rejected. | recordNo |
| 4 | u_mes_bmr_yieldReconciliation | entity | transaction | - | Calculated yield of an order, and reconciliation of issued components and labels against use, return and destruction, with the limits and the outcome. | recordNo |
| 5 | u_mes_bmr_batchManufacturingRecord | entity | transaction | - | Header of the executed batch record of one production order: the master record version frozen at opening, links to line clearance, yield reconciliation, review and release, and the exported true copy of the compiled record with its checksum. | recordNo |

## mmr - MasterManufacturingRecord

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_mmr_masterManufacturingRecord | entity | master | - | One approved, versioned master manufacturing record per item revision: the bill of material, routing, bill of process, recipes, control plan, inspection plan, packaging specification and label template that together define how a batch is made, with standard batch size, theoretical yield, yield limits, effective dates and approvals. | title |
| 2 | u_mes_mmr_masterManufacturingRecordRecipe | relationship | master | u_mes_mmr_masterManufacturingRecord | Links one masterManufacturingRecord to one recipe (one document per link) | recordNo |
