# Collection inventory

Model version 2.0 | 11 October 2026 | 257 collections (106 entity, 76 child, 63 relationship, 12 value-list), 5553 keys

Authority for collection names. Naming: `u_mes_<moduleCode>_<singularCollectionName>`. Each business concept appears once. Data class decides audit keys: transaction collections carry the six audit keys, master collections do not.

## Module codes

| Module code | Module | Collections |
|---|---|---|
| mdm | Master data | 42 |
| prd | Product definition | 38 |
| exe | Planning and execution | 31 |
| mat | Materials | 19 |
| trc | Traceability | 7 |
| qlt | Quality | 65 |
| eqp | Equipment and performance | 13 |
| mnt | Maintenance and tooling | 13 |
| sys | Integration and system | 23 |
| ehs | Energy, safety and andon | 6 |

## mdm - Master data

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_mdm_enterprise | entity | master | - | Legal entities of the group (ISA-95 Enterprise level); tax and registration data | name |
| 2 | u_mes_mdm_enterpriseContact | child | master | u_mes_mdm_enterprise | One document per contact of a enterprise | name |
| 3 | u_mes_mdm_site | entity | master | - | Plants and warehouses (ISA-95 Site); timezone, address, IATF certificate | name |
| 4 | u_mes_mdm_siteCertificate | child | master | u_mes_mdm_site | One document per certificate of a site | recordNo |
| 5 | u_mes_mdm_area | entity | master | - | Production and support areas inside a site (ISA-95 Area) | name |
| 6 | u_mes_mdm_line | entity | master | - | Production lines / cells (ISA-95 Production Line / Work Cell) | name |
| 7 | u_mes_mdm_lineDefaultShift | relationship | master | u_mes_mdm_line | Links one line to one default shift (one document per link) | recordNo |
| 8 | u_mes_mdm_lineIdealRate | child | master | u_mes_mdm_line | One document per ideal rate of a line | recordNo |
| 9 | u_mes_mdm_workCenter | entity | master | - | Stations where operations are executed and booked; ERP work centre mapping | name |
| 10 | u_mes_mdm_workCenterEquipment | relationship | master | u_mes_mdm_workCenter | Links one workCenter to one equipment (one document per link) | recordNo |
| 11 | u_mes_mdm_workCenterOperation | relationship | master | u_mes_mdm_workCenter | Links one workCenter to one operation (one document per link) | recordNo |
| 12 | u_mes_mdm_workCenterRequiresSkill | relationship | master | u_mes_mdm_workCenter | Links one workCenter to one requires skill (one document per link) | recordNo |
| 13 | u_mes_mdm_equipment | entity | master | - | Machines, furnaces, testers (ISA-95 Unit / Equipment); hierarchy, make, model, capability | name |
| 14 | u_mes_mdm_equipmentIotDevice | relationship | master | u_mes_mdm_equipment | Links one equipment to one iot device (one document per link) | recordNo |
| 15 | u_mes_mdm_shift | entity | master | - | Shift patterns with start/end and breaks | name |
| 16 | u_mes_mdm_shiftBreak | child | master | u_mes_mdm_shift | One document per break of a shift | name |
| 17 | u_mes_mdm_shiftWorkingDay | valueList | master | u_mes_mdm_shift | One document per working day value of a shift | recordNo |
| 18 | u_mes_mdm_workCalendar | entity | master | - | Working calendars with holidays and exception days per site / line | name |
| 19 | u_mes_mdm_workCalendarLine | relationship | master | u_mes_mdm_workCalendar | Links one workCalendar to one line (one document per link) | recordNo |
| 20 | u_mes_mdm_workCalendarShift | relationship | master | u_mes_mdm_workCalendar | Links one workCalendar to one shift (one document per link) | recordNo |
| 21 | u_mes_mdm_workCalendarWeeklyOffDay | valueList | master | u_mes_mdm_workCalendar | One document per weekly off day value of a workCalendar | recordNo |
| 22 | u_mes_mdm_workCalendarException | child | master | u_mes_mdm_workCalendar | One document per exception of a workCalendar | description |
| 23 | u_mes_mdm_workCalendarExceptionShift | relationship | master | u_mes_mdm_workCalendarException | Links one workCalendarException to one shift (one document per link) | recordNo |
| 24 | u_mes_mdm_shiftRoster | entity | transaction | - | Crew assignment per production day, shift and line (who is planned where) | recordNo |
| 25 | u_mes_mdm_shiftRosterAssignment | child | transaction | u_mes_mdm_shiftRoster | One document per assignment of a shiftRoster | recordNo |
| 26 | u_mes_mdm_role | entity | master | - | Named sets of permissions (operator, setter, quality engineer ...) | name |
| 27 | u_mes_mdm_rolePermission | valueList | master | u_mes_mdm_role | One document per permission value of a role | recordNo |
| 28 | u_mes_mdm_roleSignatureMeaning | valueList | master | u_mes_mdm_role | One document per signature meaning value of a role | recordNo |
| 29 | u_mes_mdm_user | entity | master | - | People and system accounts; badge id, role, home work centre | fullName |
| 30 | u_mes_mdm_userRole | relationship | master | u_mes_mdm_user | Links one user to one role (one document per link) | recordNo |
| 31 | u_mes_mdm_skill | entity | master | - | Skill definitions required by operations (e.g. leak-test operation, CMM programming) | name |
| 32 | u_mes_mdm_skillOperation | relationship | master | u_mes_mdm_skill | Links one skill to one operation (one document per link) | recordNo |
| 33 | u_mes_mdm_skillLevelScale | child | master | u_mes_mdm_skill | One document per level scale of a skill | description |
| 34 | u_mes_mdm_skillCertification | entity | transaction | - | Skills-matrix entries: user x skill, level, valid-from/to, assessor; used for operator lock-out | recordNo |
| 35 | u_mes_mdm_customer | entity | master | - | OEMs and aftermarket customers; ship-to addresses, label and ASN requirements | name |
| 36 | u_mes_mdm_customerShipTo | child | master | u_mes_mdm_customer | One document per ship to of a customer | name |
| 37 | u_mes_mdm_customerContact | child | master | u_mes_mdm_customer | One document per contact of a customer | name |
| 38 | u_mes_mdm_supplier | entity | master | - | Material, tooling and service suppliers; approval status, certificates, PPM rating | name |
| 39 | u_mes_mdm_supplierContact | child | master | u_mes_mdm_supplier | One document per contact of a supplier | name |
| 40 | u_mes_mdm_supplierCertificate | child | master | u_mes_mdm_supplier | One document per certificate of a supplier | recordNo |
| 41 | u_mes_mdm_supplierSuppliedItem | relationship | master | u_mes_mdm_supplier | Links one supplier to one supplied item (one document per link) | recordNo |
| 42 | u_mes_mdm_unitOfMeasure | entity | master | - | Units and conversion factors (EA, kg, N.m, bar, mm, um, kWh) | name |

## prd - Product definition

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_prd_item | entity | master | - | Parts: finished caliper, semi-finished body, purchased components, raw material, consumables; drawing revision | description |
| 2 | u_mes_prd_itemRevision | child | master | u_mes_prd_item | One document per revision of a item | description |
| 3 | u_mes_prd_itemCustomerPart | child | master | u_mes_prd_item | One document per customer part of a item | recordNo |
| 4 | u_mes_prd_productVariant | entity | master | - | Product variants (LH/RH, piston diameter, pad compound, market) that drive BOM, instruction and label selection | name |
| 5 | u_mes_prd_billOfMaterial | entity | master | - | Multi-level bills of material per item revision with effectivity | recordNo |
| 6 | u_mes_prd_billOfMaterialComponent | child | master | u_mes_prd_billOfMaterial | One document per component of a billOfMaterial | recordNo |
| 7 | u_mes_prd_billOfMaterialComponentProductVariant | relationship | master | u_mes_prd_billOfMaterialComponent | Links one billOfMaterialComponent to one product variant (one document per link) | recordNo |
| 8 | u_mes_prd_billOfMaterialComponentAlternateItem | relationship | master | u_mes_prd_billOfMaterialComponent | Links one billOfMaterialComponent to one alternate item (one document per link) | recordNo |
| 9 | u_mes_prd_operation | entity | master | - | Standard operation library (casting, T6, machining ... packing) reused by routings | name |
| 10 | u_mes_prd_operationRequiredSkill | relationship | master | u_mes_prd_operation | Links one operation to one required skill (one document per link) | recordNo |
| 11 | u_mes_prd_routing | entity | master | - | Sequence of operations per item, including rework / disposition routings and alternate paths | description |
| 12 | u_mes_prd_routingStep | child | master | u_mes_prd_routing | One document per step of a routing | recordNo |
| 13 | u_mes_prd_routingStepAlternateWorkCenter | relationship | master | u_mes_prd_routingStep | Links one routingStep to one alternate work center (one document per link) | recordNo |
| 14 | u_mes_prd_routingStepNextStep | child | master | u_mes_prd_routingStep | One document per next step of a routingStep | recordNo |
| 15 | u_mes_prd_billOfProcess | entity | master | - | Per routing step: required equipment, tools, recipe, work instruction, data collection, consumed components, cycle time | recordNo |
| 16 | u_mes_prd_billOfProcessStep | child | master | u_mes_prd_billOfProcess | One document per step of a billOfProcess | recordNo |
| 17 | u_mes_prd_billOfProcessStepEquipment | relationship | master | u_mes_prd_billOfProcessStep | Links one billOfProcessStep to one equipment (one document per link) | recordNo |
| 18 | u_mes_prd_billOfProcessStepTool | relationship | master | u_mes_prd_billOfProcessStep | Links one billOfProcessStep to one tool (one document per link) | recordNo |
| 19 | u_mes_prd_billOfProcessStepRequiredSkill | relationship | master | u_mes_prd_billOfProcessStep | Links one billOfProcessStep to one required skill (one document per link) | recordNo |
| 20 | u_mes_prd_billOfProcessStepConsumedComponent | child | master | u_mes_prd_billOfProcessStep | One document per consumed component of a billOfProcessStep | recordNo |
| 21 | u_mes_prd_billOfProcessStepInterlock | child | master | u_mes_prd_billOfProcessStep | One document per interlock of a billOfProcessStep | description |
| 22 | u_mes_prd_billOfProcessStepProcessParameter | child | master | u_mes_prd_billOfProcessStep | One document per process parameter of a billOfProcessStep | name |
| 23 | u_mes_prd_workInstruction | entity | master | - | Versioned visual work instructions with steps, media, cautions, variant applicability, required checks | title |
| 24 | u_mes_prd_workInstructionStep | child | master | u_mes_prd_workInstruction | One document per step of a workInstruction | title |
| 25 | u_mes_prd_workInstructionStepMediaControlledDocument | relationship | master | u_mes_prd_workInstructionStep | Links one workInstructionStep to one media controlled document (one document per link) | recordNo |
| 26 | u_mes_prd_workInstructionStepProductVariant | relationship | master | u_mes_prd_workInstructionStep | Links one workInstructionStep to one product variant (one document per link) | recordNo |
| 27 | u_mes_prd_workInstructionStepTool | relationship | master | u_mes_prd_workInstructionStep | Links one workInstructionStep to one tool (one document per link) | recordNo |
| 28 | u_mes_prd_workInstructionStepCharacteristic | relationship | master | u_mes_prd_workInstructionStep | Links one workInstructionStep to one characteristic (one document per link) | recordNo |
| 29 | u_mes_prd_workInstructionPpeItem | valueList | master | u_mes_prd_workInstruction | One document per ppe item value of a workInstruction | recordNo |
| 30 | u_mes_prd_workInstructionKeyPoint | valueList | master | u_mes_prd_workInstruction | One document per key point value of a workInstruction | recordNo |
| 31 | u_mes_prd_recipe | entity | master | - | Machine parameter sets with set-points and limits (die temperature, furnace profile, CNC program, torque program, leak-test program) | name |
| 32 | u_mes_prd_recipeParameter | child | master | u_mes_prd_recipe | One document per parameter of a recipe | name |
| 33 | u_mes_prd_recipeStage | child | master | u_mes_prd_recipe | One document per stage of a recipe | name |
| 34 | u_mes_prd_engineeringChange | entity | transaction | - | Engineering change notices with affected objects, approvals and effectivity (cut-in serial / date) | title |
| 35 | u_mes_prd_engineeringChangeAffectedItem | child | transaction | u_mes_prd_engineeringChange | One document per affected item of a engineeringChange | recordNo |
| 36 | u_mes_prd_engineeringChangeAffectedObject | child | transaction | u_mes_prd_engineeringChange | One document per affected object of a engineeringChange | recordNo |
| 37 | u_mes_prd_engineeringChangeApproval | child | transaction | u_mes_prd_engineeringChange | One document per approval of a engineeringChange | recordNo |
| 38 | u_mes_prd_engineeringChangeControlledDocument | relationship | transaction | u_mes_prd_engineeringChange | Links one engineeringChange to one controlled document (one document per link) | recordNo |

## exe - Planning and execution

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_exe_customerSchedule | entity | transaction | - | OEM delivery schedules / releases (demand that drives production orders and shipments) | recordNo |
| 2 | u_mes_exe_customerScheduleLine | child | transaction | u_mes_exe_customerSchedule | One document per line of a customerSchedule | recordNo |
| 3 | u_mes_exe_productionOrder | entity | transaction | - | Shop orders from ERP: item, quantity, routing/BOM version, partial releases, status | recordNo |
| 4 | u_mes_exe_productionOrderRelease | child | transaction | u_mes_exe_productionOrder | One document per release of a productionOrder | recordNo |
| 5 | u_mes_exe_productionOrderLot | relationship | transaction | u_mes_exe_productionOrder | Links one productionOrder to one lot (one document per link) | recordNo |
| 6 | u_mes_exe_productionSchedule | entity | transaction | - | Finite schedule per line and shift with sequenced orders, planned start/end | recordNo |
| 7 | u_mes_exe_productionScheduleSlot | child | transaction | u_mes_exe_productionSchedule | One document per slot of a productionSchedule | recordNo |
| 8 | u_mes_exe_dispatchList | entity | transaction | - | Prioritised work queue per work centre shown to the operator | recordNo |
| 9 | u_mes_exe_dispatchListEntry | child | transaction | u_mes_exe_dispatchList | One document per entry of a dispatchList | recordNo |
| 10 | u_mes_exe_operationExecution | entity | transaction | - | Start / complete record of an operation on a unit or lot: who, where, when, result, cycle time (track-in / track-out) | recordNo |
| 11 | u_mes_exe_operationExecutionDefectCode | relationship | transaction | u_mes_exe_operationExecution | Links one operationExecution to one defect code (one document per link) | recordNo |
| 12 | u_mes_exe_operationExecutionTool | relationship | transaction | u_mes_exe_operationExecution | Links one operationExecution to one tool (one document per link) | recordNo |
| 13 | u_mes_exe_stepCompletion | entity | transaction | - | Completion record for each work-instruction step: values entered, confirmations, duration, device data | recordNo |
| 14 | u_mes_exe_wipUnit | entity | transaction | - | Serialised unit in production (shop-floor control number): current operation, status, quality state | recordNo |
| 15 | u_mes_exe_wipUnitCompletedStep | valueList | transaction | u_mes_exe_wipUnit | One document per completed step value of a wipUnit | recordNo |
| 16 | u_mes_exe_lot | entity | transaction | - | Lots and batches: supplier lots, melt/heat lots, casting lots, heat-treatment charges, anodising loads | recordNo |
| 17 | u_mes_exe_lotParentLot | relationship | transaction | u_mes_exe_lot | Links one lot to one parent lot (one document per link) | recordNo |
| 18 | u_mes_exe_lotAttributesCavityNo | valueList | transaction | u_mes_exe_lot | One document per attributes cavity no value of a lot | recordNo |
| 19 | u_mes_exe_container | entity | transaction | - | Bins, trolleys, returnable crates and pallets with contents and nesting | recordNo |
| 20 | u_mes_exe_containerLot | relationship | transaction | u_mes_exe_container | Links one container to one lot (one document per link) | recordNo |
| 21 | u_mes_exe_labourBooking | entity | transaction | - | Clock-on / clock-off of people against orders, operations and indirect activities | recordNo |
| 22 | u_mes_exe_changeover | entity | transaction | - | Changeover from one item / variant to another: planned vs actual duration, checklist, first-off approval | recordNo |
| 23 | u_mes_exe_changeoverStep | child | transaction | u_mes_exe_changeover | One document per step of a changeover | description |
| 24 | u_mes_exe_changeoverRemovedTool | relationship | transaction | u_mes_exe_changeover | Links one changeover to one removed tool (one document per link) | recordNo |
| 25 | u_mes_exe_changeoverInstalledTool | relationship | transaction | u_mes_exe_changeover | Links one changeover to one installed tool (one document per link) | recordNo |
| 26 | u_mes_exe_changeoverPerformedByUser | relationship | transaction | u_mes_exe_changeover | Links one changeover to one performed by user (one document per link) | recordNo |
| 27 | u_mes_exe_shiftHandover | entity | transaction | - | Shift logbook: output, open issues, safety and quality notes, acknowledgements | recordNo |
| 28 | u_mes_exe_shiftHandoverProductionOrder | relationship | transaction | u_mes_exe_shiftHandover | Links one shiftHandover to one production order (one document per link) | recordNo |
| 29 | u_mes_exe_shiftHandoverDowntimeEvent | relationship | transaction | u_mes_exe_shiftHandover | Links one shiftHandover to one downtime event (one document per link) | recordNo |
| 30 | u_mes_exe_shiftHandoverNonconformance | relationship | transaction | u_mes_exe_shiftHandover | Links one shiftHandover to one nonconformance (one document per link) | recordNo |
| 31 | u_mes_exe_shiftHandoverOpenItem | child | transaction | u_mes_exe_shiftHandover | One document per open item of a shiftHandover | description |

## mat - Materials

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_mat_storageLocation | entity | master | - | Warehouses, racks, line-side supermarkets, quarantine cage, dispatch bay | name |
| 2 | u_mes_mat_inventoryBalance | entity | transaction | - | Stock on hand per item, lot, location and stock status | recordNo |
| 3 | u_mes_mat_materialMovement | entity | transaction | - | Every stock transaction: receipt, putaway, issue to line, return, scrap, transfer, shipment | recordNo |
| 4 | u_mes_mat_goodsReceipt | entity | transaction | - | Receipts from suppliers with lines, supplier lot, certificate, incoming inspection status | recordNo |
| 5 | u_mes_mat_goodsReceiptLine | child | transaction | u_mes_mat_goodsReceipt | One document per line of a goodsReceipt | recordNo |
| 6 | u_mes_mat_goodsReceiptLineInspectionResult | relationship | transaction | u_mes_mat_goodsReceiptLine | Links one goodsReceiptLine to one inspection result (one document per link) | recordNo |
| 7 | u_mes_mat_kit | entity | transaction | - | Kits of components picked for an order / line-side delivery | recordNo |
| 8 | u_mes_mat_kitLine | child | transaction | u_mes_mat_kit | One document per line of a kit | recordNo |
| 9 | u_mes_mat_materialRequest | entity | transaction | - | Line-side replenishment calls (e-kanban) from a work centre to stores | recordNo |
| 10 | u_mes_mat_materialConsumption | entity | transaction | - | Component / lot consumed at an operation on a unit or lot (backflush or scanned) | recordNo |
| 11 | u_mes_mat_packagingSpecification | entity | master | - | Pack instruction: container type, quantity per bin, layers, dunnage, label template | recordNo |
| 12 | u_mes_mat_packagingSpecificationLevel | child | master | u_mes_mat_packagingSpecification | One document per level of a packagingSpecification | recordNo |
| 13 | u_mes_mat_labelTemplate | entity | master | - | Label layouts (unit 2D code, bin label, customer shipping label, hold tag) | name |
| 14 | u_mes_mat_labelTemplateField | child | master | u_mes_mat_labelTemplate | One document per field of a labelTemplate | recordNo |
| 15 | u_mes_mat_label | entity | transaction | - | Printed label instances with payload, printer, reprint count | recordNo |
| 16 | u_mes_mat_shipment | entity | transaction | - | Dispatch to customer: invoice / ASN, vehicle, containers shipped, proof of delivery | recordNo |
| 17 | u_mes_mat_shipmentLine | child | transaction | u_mes_mat_shipment | One document per line of a shipment | recordNo |
| 18 | u_mes_mat_shipmentLineContainer | relationship | transaction | u_mes_mat_shipmentLine | Links one shipmentLine to one container (one document per link) | recordNo |
| 19 | u_mes_mat_shipmentLineLot | relationship | transaction | u_mes_mat_shipmentLine | Links one shipmentLine to one lot (one document per link) | recordNo |

## trc - Traceability

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_trc_serialNumber | entity | transaction | - | Registry of every serial / 2D code issued: status, mark grade, unit and shipment linkage | recordNo |
| 2 | u_mes_trc_genealogyLink | entity | transaction | - | As-built parent-child edges: unit to component serial or component lot, with operation and time | recordNo |
| 3 | u_mes_trc_componentLotLink | entity | transaction | - | Lot-to-lot lineage: ingot heat to melt to casting lot to heat-treatment charge to anodising load; split and merge | recordNo |
| 4 | u_mes_trc_asBuiltRecord | entity | transaction | - | Device-history summary per shipped unit: components, key results, operators, sign-off (digital birth certificate) | recordNo |
| 5 | u_mes_trc_asBuiltRecordComponent | child | transaction | u_mes_trc_asBuiltRecord | One document per component of a asBuiltRecord | recordNo |
| 6 | u_mes_trc_asBuiltRecordOperation | child | transaction | u_mes_trc_asBuiltRecord | One document per operation of a asBuiltRecord | recordNo |
| 7 | u_mes_trc_asBuiltRecordInspectionResult | relationship | transaction | u_mes_trc_asBuiltRecord | Links one asBuiltRecord to one inspection result (one document per link) | recordNo |

## qlt - Quality

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_qlt_characteristic | entity | master | - | Product and process characteristics with nominal, tolerance, class (critical / significant), method | name |
| 2 | u_mes_qlt_controlPlan | entity | master | - | AIAG control plan per item and phase (prototype, pre-launch, production) | recordNo |
| 3 | u_mes_qlt_controlPlanCoreTeamUser | relationship | master | u_mes_qlt_controlPlan | Links one controlPlan to one core team user (one document per link) | recordNo |
| 4 | u_mes_qlt_controlPlanLine | child | master | u_mes_qlt_controlPlan | One document per line of a controlPlan | recordNo |
| 5 | u_mes_qlt_inspectionPlan | entity | master | - | Executable data-collection group per operation: which characteristics, sample size, frequency, reaction | name |
| 6 | u_mes_qlt_inspectionPlanLine | child | master | u_mes_qlt_inspectionPlan | One document per line of a inspectionPlan | recordNo |
| 7 | u_mes_qlt_samplingPlan | entity | master | - | Sampling rules: AQL tables, skip-lot, time or counter based frequency | name |
| 8 | u_mes_qlt_samplingPlanSizeRow | child | master | u_mes_qlt_samplingPlan | One document per size row of a samplingPlan | recordNo |
| 9 | u_mes_qlt_checkSheet | entity | master | - | Check sheet definitions: start-of-shift checks, poka-yoke verification, first-off, autonomous maintenance | name |
| 10 | u_mes_qlt_checkSheetItem | child | master | u_mes_qlt_checkSheet | One document per item of a checkSheet | recordNo |
| 11 | u_mes_qlt_checkSheetResult | entity | transaction | - | Completed check sheets with answers, failures and reactions | recordNo |
| 12 | u_mes_qlt_checkSheetResultAnswer | child | transaction | u_mes_qlt_checkSheetResult | One document per answer of a checkSheetResult | recordNo |
| 13 | u_mes_qlt_inspectionResult | entity | transaction | - | Measured and attribute results per unit / lot / receipt against a characteristic | recordNo |
| 14 | u_mes_qlt_spcChart | entity | master | - | Chart definition per characteristic and work centre: chart type, subgroup size, control limits, rules | name |
| 15 | u_mes_qlt_spcChartControlLimit | child | master | u_mes_qlt_spcChart | One document per control limit of a spcChart | recordNo |
| 16 | u_mes_qlt_spcChartRule | valueList | master | u_mes_qlt_spcChart | One document per rule value of a spcChart | recordNo |
| 17 | u_mes_qlt_spcSample | entity | transaction | - | Subgroups with readings, mean, range, rule violations and reaction | recordNo |
| 18 | u_mes_qlt_spcSampleReading | valueList | transaction | u_mes_qlt_spcSample | One document per reading value of a spcSample | recordNo |
| 19 | u_mes_qlt_spcSampleInspectionResult | relationship | transaction | u_mes_qlt_spcSample | Links one spcSample to one inspection result (one document per link) | recordNo |
| 20 | u_mes_qlt_spcSampleViolation | child | transaction | u_mes_qlt_spcSample | One document per violation of a spcSample | description |
| 21 | u_mes_qlt_defectCode | entity | master | - | Defect / NC code catalogue with group, default disposition routing and severity | name |
| 22 | u_mes_qlt_defectCodeApplicableOperation | relationship | master | u_mes_qlt_defectCode | Links one defectCode to one applicable operation (one document per link) | recordNo |
| 23 | u_mes_qlt_nonconformance | entity | transaction | - | Nonconformance reports: what, where, quantity, containment, disposition (use-as-is, rework, scrap, return) | title |
| 24 | u_mes_qlt_nonconformanceAffectedObject | child | transaction | u_mes_qlt_nonconformance | One document per affected object of a nonconformance | recordNo |
| 25 | u_mes_qlt_nonconformanceContainmentAction | child | transaction | u_mes_qlt_nonconformance | One document per containment action of a nonconformance | description |
| 26 | u_mes_qlt_nonconformanceInspectionResult | relationship | transaction | u_mes_qlt_nonconformance | Links one nonconformance to one inspection result (one document per link) | recordNo |
| 27 | u_mes_qlt_nonconformanceReworkOrder | relationship | transaction | u_mes_qlt_nonconformance | Links one nonconformance to one rework order (one document per link) | recordNo |
| 28 | u_mes_qlt_nonconformanceScrapRecord | relationship | transaction | u_mes_qlt_nonconformance | Links one nonconformance to one scrap record (one document per link) | recordNo |
| 29 | u_mes_qlt_nonconformancePhotoControlledDocument | relationship | transaction | u_mes_qlt_nonconformance | Links one nonconformance to one photo controlled document (one document per link) | recordNo |
| 30 | u_mes_qlt_nonconformanceMrbUser | relationship | transaction | u_mes_qlt_nonconformance | Links one nonconformance to one mrb user (one document per link) | recordNo |
| 31 | u_mes_qlt_reworkOrder | entity | transaction | - | Rework instruction and execution on the rework routing with re-inspection result | recordNo |
| 32 | u_mes_qlt_reworkOrderWipUnit | relationship | transaction | u_mes_qlt_reworkOrder | Links one reworkOrder to one wip unit (one document per link) | recordNo |
| 33 | u_mes_qlt_reworkOrderStep | child | transaction | u_mes_qlt_reworkOrder | One document per step of a reworkOrder | description |
| 34 | u_mes_qlt_scrapRecord | entity | transaction | - | Scrap declaration with quantity, weight, cost, defect code and operation of origin | recordNo |
| 35 | u_mes_qlt_qualityHold | entity | transaction | - | Hold / quarantine on units, lots, containers or locations with reason and release decision | recordNo |
| 36 | u_mes_qlt_qualityHoldHeldObject | child | transaction | u_mes_qlt_qualityHold | One document per held object of a qualityHold | recordNo |
| 37 | u_mes_qlt_deviationPermit | entity | transaction | - | Temporary deviations / concessions approved by the customer with quantity or date limit | title |
| 38 | u_mes_qlt_deviationPermitApproval | child | transaction | u_mes_qlt_deviationPermit | One document per approval of a deviationPermit | recordNo |
| 39 | u_mes_qlt_capa | entity | transaction | - | Corrective and preventive actions in 8D structure (D1-D8) with team, root cause, actions, verification | title |
| 40 | u_mes_qlt_capaNonconformance | relationship | transaction | u_mes_qlt_capa | Links one capa to one nonconformance (one document per link) | recordNo |
| 41 | u_mes_qlt_capaTeamMember | child | transaction | u_mes_qlt_capa | One document per team member of a capa | recordNo |
| 42 | u_mes_qlt_capaContainmentAction | child | transaction | u_mes_qlt_capa | One document per containment action of a capa | description |
| 43 | u_mes_qlt_capaCorrectiveAction | child | transaction | u_mes_qlt_capa | One document per corrective action of a capa | description |
| 44 | u_mes_qlt_capaImplementationAction | child | transaction | u_mes_qlt_capa | One document per implementation action of a capa | description |
| 45 | u_mes_qlt_capaControlledDocument | relationship | transaction | u_mes_qlt_capa | Links one capa to one controlled document (one document per link) | recordNo |
| 46 | u_mes_qlt_pfmea | entity | master | - | Process FMEA per item / process: failure modes, effects, causes, S-O-D, action priority | title |
| 47 | u_mes_qlt_pfmeaCoreTeamUser | relationship | master | u_mes_qlt_pfmea | Links one pfmea to one core team user (one document per link) | recordNo |
| 48 | u_mes_qlt_pfmeaLine | child | master | u_mes_qlt_pfmea | One document per line of a pfmea | recordNo |
| 49 | u_mes_qlt_ppapSubmission | entity | transaction | - | PPAP package: level, 18 elements with status, PSW, customer decision | recordNo |
| 50 | u_mes_qlt_ppapSubmissionElement | child | transaction | u_mes_qlt_ppapSubmission | One document per element of a ppapSubmission | name |
| 51 | u_mes_qlt_ppapSubmissionMsaStudy | relationship | transaction | u_mes_qlt_ppapSubmission | Links one ppapSubmission to one msa study (one document per link) | recordNo |
| 52 | u_mes_qlt_gauge | entity | master | - | Gauges and measuring instruments: type, range, resolution, calibration interval and due date, status | name |
| 53 | u_mes_qlt_gaugeCalibration | entity | transaction | - | Calibration events: as-found / as-left readings, standard used, result, certificate | recordNo |
| 54 | u_mes_qlt_gaugeCalibrationReading | child | transaction | u_mes_qlt_gaugeCalibration | One document per reading of a gaugeCalibration | recordNo |
| 55 | u_mes_qlt_msaStudy | entity | transaction | - | Measurement system analysis: gauge R&R, bias, linearity, attribute agreement | recordNo |
| 56 | u_mes_qlt_msaStudyAppraiserUser | relationship | transaction | u_mes_qlt_msaStudy | Links one msaStudy to one appraiser user (one document per link) | recordNo |
| 57 | u_mes_qlt_msaStudyTrial | child | transaction | u_mes_qlt_msaStudy | One document per trial of a msaStudy | recordNo |
| 58 | u_mes_qlt_audit | entity | transaction | - | Layered process, process (VDA 6.3), product and system audits with findings | title |
| 59 | u_mes_qlt_auditAuditorUser | relationship | transaction | u_mes_qlt_audit | Links one audit to one auditor user (one document per link) | recordNo |
| 60 | u_mes_qlt_auditFinding | child | transaction | u_mes_qlt_audit | One document per finding of a audit | description |
| 61 | u_mes_qlt_customerComplaint | entity | transaction | - | Customer complaints / line rejections / warranty returns with affected serials and PPM impact | description |
| 62 | u_mes_qlt_customerComplaintSerialNumber | relationship | transaction | u_mes_qlt_customerComplaint | Links one customerComplaint to one serial number (one document per link) | recordNo |
| 63 | u_mes_qlt_customerComplaintShipment | relationship | transaction | u_mes_qlt_customerComplaint | Links one customerComplaint to one shipment (one document per link) | recordNo |
| 64 | u_mes_qlt_customerComplaintSuspectLot | relationship | transaction | u_mes_qlt_customerComplaint | Links one customerComplaint to one suspect lot (one document per link) | recordNo |
| 65 | u_mes_qlt_customerComplaintCommunication | child | transaction | u_mes_qlt_customerComplaint | One document per communication of a customerComplaint | recordNo |

## eqp - Equipment and performance

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_eqp_reasonCode | entity | master | - | Reason tree (up to 4 levels) for downtime, scrap, hold and andon with planned / unplanned category | name |
| 2 | u_mes_eqp_equipmentState | entity | transaction | - | State intervals per equipment: running, idle, setup, down, starved, blocked | recordNo |
| 3 | u_mes_eqp_downtimeEvent | entity | transaction | - | Classified stops with fault, reason path, action taken, duration, responsible group | recordNo |
| 4 | u_mes_eqp_downtimeEventComment | child | transaction | u_mes_eqp_downtimeEvent | One document per comment of a downtimeEvent | recordNo |
| 5 | u_mes_eqp_productionCount | entity | transaction | - | Hourly good / reject / rework counts per work centre against target (hour-by-hour board) | recordNo |
| 6 | u_mes_eqp_oeeRecord | entity | transaction | - | OEE per equipment / line and shift: availability, performance, quality with the time and count basis | recordNo |
| 7 | u_mes_eqp_oeeRecordLoss | child | transaction | u_mes_eqp_oeeRecord | One document per loss of a oeeRecord | recordNo |
| 8 | u_mes_eqp_processTag | entity | master | - | Tag definitions: source address, unit, deadband, limits, equipment | description |
| 9 | u_mes_eqp_processReading | entity | transaction | - | Tag values over time (die temperature, furnace zone temperature, spindle load, bath pH, current) | recordNo |
| 10 | u_mes_eqp_alarm | entity | transaction | - | Alarm occurrences with severity, raised / acknowledged / cleared times | recordNo |
| 11 | u_mes_eqp_torqueResult | entity | transaction | - | Tightening results per unit: program, final torque, angle, status, curve reference | recordNo |
| 12 | u_mes_eqp_leakTestResult | entity | transaction | - | Leak test per unit: stage pressures, decay, leak rate, limits, verdict, retest counter | recordNo |
| 13 | u_mes_eqp_leakTestResultStage | child | transaction | u_mes_eqp_leakTestResult | One document per stage of a leakTestResult | recordNo |

## mnt - Maintenance and tooling

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_mnt_maintenancePlan | entity | master | - | Preventive / condition-based plans per equipment or tool with tasks, interval and next due | name |
| 2 | u_mes_mnt_maintenancePlanTask | child | master | u_mes_mnt_maintenancePlan | One document per task of a maintenancePlan | description |
| 3 | u_mes_mnt_maintenancePlanRequiredSkill | relationship | master | u_mes_mnt_maintenancePlan | Links one maintenancePlan to one required skill (one document per link) | recordNo |
| 4 | u_mes_mnt_maintenancePlanRequiredSparePart | child | master | u_mes_mnt_maintenancePlan | One document per required spare part of a maintenancePlan | recordNo |
| 5 | u_mes_mnt_maintenanceWorkOrder | entity | transaction | - | Breakdown, preventive and improvement work orders with labour, parts used, root cause | title |
| 6 | u_mes_mnt_maintenanceWorkOrderAssignedToUser | relationship | transaction | u_mes_mnt_maintenanceWorkOrder | Links one maintenanceWorkOrder to one assigned to user (one document per link) | recordNo |
| 7 | u_mes_mnt_maintenanceWorkOrderLabour | child | transaction | u_mes_mnt_maintenanceWorkOrder | One document per labour of a maintenanceWorkOrder | recordNo |
| 8 | u_mes_mnt_maintenanceWorkOrderUsedSparePart | child | transaction | u_mes_mnt_maintenanceWorkOrder | One document per used spare part of a maintenanceWorkOrder | recordNo |
| 9 | u_mes_mnt_sparePart | entity | master | - | Maintenance spares with stock, minimum, location, where-used | description |
| 10 | u_mes_mnt_sparePartUsedOnEquipment | relationship | master | u_mes_mnt_sparePart | Links one sparePart to one used on equipment (one document per link) | recordNo |
| 11 | u_mes_mnt_tool | entity | master | - | Dies, fixtures, cutting tools, nutrunner spindles, test seals: life limit, life used, status, location | name |
| 12 | u_mes_mnt_toolItem | relationship | master | u_mes_mnt_tool | Links one tool to one item (one document per link) | recordNo |
| 13 | u_mes_mnt_toolLifeRecord | entity | transaction | - | Tool mount / dismount / usage / regrind events with shots or cycles consumed | recordNo |

## sys - Integration and system

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_sys_erpMessage | entity | transaction | - | Inbound and outbound interface messages (order download, confirmation, goods movement) with payload, status, retries | recordNo |
| 2 | u_mes_sys_integrationConnector | entity | master | - | Connector definitions to ERP, PLM, OPC UA servers, tool controllers, label printers | name |
| 3 | u_mes_sys_integrationConnectorFunction | child | master | u_mes_sys_integrationConnector | One document per function of a integrationConnector | recordNo |
| 4 | u_mes_sys_iotDevice | entity | master | - | Registry of PLCs, gateways, nutrunner controllers, leak testers, scanners, printers, energy meters | name |
| 5 | u_mes_sys_operatorApp | entity | master | - | Composable operator screen definitions (versioned) bound to work centres and operations | name |
| 6 | u_mes_sys_operatorAppWorkCenter | relationship | master | u_mes_sys_operatorApp | Links one operatorApp to one work center (one document per link) | recordNo |
| 7 | u_mes_sys_operatorAppOperation | relationship | master | u_mes_sys_operatorApp | Links one operatorApp to one operation (one document per link) | recordNo |
| 8 | u_mes_sys_operatorAppStep | child | master | u_mes_sys_operatorApp | One document per step of a operatorApp | name |
| 9 | u_mes_sys_operatorAppStepTrigger | child | master | u_mes_sys_operatorAppStep | One document per trigger of a operatorAppStep | recordNo |
| 10 | u_mes_sys_operatorAppDeviceBinding | child | master | u_mes_sys_operatorApp | One document per device binding of a operatorApp | recordNo |
| 11 | u_mes_sys_operatorAppLanguage | valueList | master | u_mes_sys_operatorApp | One document per language value of a operatorApp | recordNo |
| 12 | u_mes_sys_businessEvent | entity | transaction | - | Business event stream (order released, unit started, recipe downloaded, hold placed) | recordNo |
| 13 | u_mes_sys_auditTrail | entity | transaction | - | Field-level change history of master and quality data (who, when, old, new, reason) | recordNo |
| 14 | u_mes_sys_auditTrailChange | child | transaction | u_mes_sys_auditTrail | One document per change of a auditTrail | recordNo |
| 15 | u_mes_sys_electronicSignature | entity | transaction | - | Signature records for approvals and releases with meaning and signed-content hash | recordNo |
| 16 | u_mes_sys_notification | entity | transaction | - | Alerts and escalations sent to users / groups with delivery and acknowledgement status | title |
| 17 | u_mes_sys_notificationRecipient | child | transaction | u_mes_sys_notification | One document per recipient of a notification | recordNo |
| 18 | u_mes_sys_controlledDocument | entity | transaction | - | Controlled documents and attachments metadata (drawings, certificates, photos, reports); file in object store | title |
| 19 | u_mes_sys_controlledDocumentTag | valueList | transaction | u_mes_sys_controlledDocument | One document per tag value of a controlledDocument | recordNo |
| 20 | u_mes_sys_numberRange | entity | master | - | Counters and format masks for serials, lots, orders, labels, NCRs | name |
| 21 | u_mes_sys_systemConfiguration | entity | master | - | Site and module settings (OEE basis, SPC rules, retention, label printer mapping) | description |
| 22 | u_mes_sys_statusDefinition | entity | master | - | Status values and allowed transitions per collection (status mapping) | statusName |
| 23 | u_mes_sys_statusTransition | entity | master | - | Status values and allowed transitions per collection (status mapping) | transitionName |

## ehs - Energy, safety and andon

| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |
|---|---|---|---|---|---|---|
| 1 | u_mes_ehs_energyReading | entity | transaction | - | Interval energy, compressed air and gas consumption per meter and equipment | recordNo |
| 2 | u_mes_ehs_andonEvent | entity | transaction | - | Help calls from stations (quality, material, maintenance, safety) with response and escalation times | description |
| 3 | u_mes_ehs_andonEventEscalation | child | transaction | u_mes_ehs_andonEvent | One document per escalation of a andonEvent | recordNo |
| 4 | u_mes_ehs_safetyIncident | entity | transaction | - | Near misses, unsafe conditions, first-aid and lost-time incidents with investigation and actions | title |
| 5 | u_mes_ehs_safetyIncidentWitnessUser | relationship | transaction | u_mes_ehs_safetyIncident | Links one safetyIncident to one witness user (one document per link) | recordNo |
| 6 | u_mes_ehs_safetyIncidentAction | child | transaction | u_mes_ehs_safetyIncident | One document per action of a safetyIncident | description |
