# data_model_register.md

MES on MongoDB - Front Brake Caliper Assembly LH - Pune
Register version: 2.2 | Date: 11 October 2026 | Database: mes | Model version 2.2 | 11 October 2026 | 299 collections (148 entity, 76 child, 67 relationship, 8 value-list), 6058 keys

This file is the single reference for collection names, identifiers and master IDs. It follows 00_governance/data_modeling_standard.md. Field-level detail: 02_architecture/collection_keys.md and 02_architecture/field_lists. Machine-readable copy: 05_generator/model/flat_model.json.

## 1. Conventions in force

- Collection name: `u_mes_<moduleCode>_<singularCollectionName>`, lower camelCase singular noun.
- Flat documents (DATA-001): no embedded documents, no arrays. A repeated value or association is a separate collection with one document per occurrence.
- `_id`: String, pattern in section 4. `recordNo`: String, the business identifier, present in every collection.
- Reference: `<entity>Id` followed by `<entity>Name` (display value copied from the target). User references that record an action: `<action>ById` + `<action>By`.
- Polymorphic reference: `relatedCollectionName` + `relatedEntityId` + `relatedEntityName`.
- `siteId` + `siteName` in every collection except `u_mes_mdm_site`.
- Classification values (DATA-003): a list the plant maintains is a master collection referenced by `<entity>Id` + `<entity>Name`; a list fixed by the application stays coded text with its values in `u_mes_sys_enumerationValue`.
- `status`: primary lifecycle state, only where the collection has one; values in 04_reference_data/code_lists/status_values.md.
- Audit keys `createdAt, createdById, createdBy, updatedAt, updatedById, updatedBy`: transaction collections only.
- `schemaVersion` (Int32) in every collection.
- Types (DATA-002): Date, Int32, Int64, Decimal128 for measurements and money, Double only for geoLatitude, geoLongitude, tagValue, powerFactor, Boolean, String.

## 2. Seed-data frame

| Item | Value |
|---|---|
| Enterprise | ENT-VBS - Varuna Brake Systems Pvt. Ltd. (fictional) |
| Site | SITE-PN1 - Chakan Plant, Pune, Maharashtra (timezone Asia/Kolkata) |
| OEM customer | CUS-SML - Sahyadri Motors Ltd. (fictional) |
| Production period | Mon 28 Sep 2026 06:00 IST to Sat 10 Oct 2026 22:00 IST |
| Non-working days | Fri 2 Oct 2026 (Gandhi Jayanti), Sun 4 Oct 2026 (weekly off) |
| Shifts | SH-A 06:00-14:00, SH-B 14:00-22:00, SH-C 22:00-06:00 IST (UTC starts 00:30, 08:30, 16:30) |
| Documents per collection | 10, except u_mes_prd_operation (11) and u_mes_prd_item (12) |

## 3. Master ID registry

### 3.1 Items (u_mes_prd_item)

| _id | recordNo | name | Type | Drawing revision |
|---|---|---|---|---|
| ITM-5110-10-0100 | 5110-10-0100 | Front Brake Caliper Assembly, LH | Finished good | D |
| ITM-5110-10-0200 | 5110-10-0200 | Front Brake Caliper Assembly, RH | Finished good | D |
| ITM-5110-20-0110 | 5110-20-0110 | Caliper Body, LH, machined and anodised | Semi-finished | C |
| ITM-5110-20-0105 | 5110-20-0105 | Caliper Body Casting, LH, T6 | Semi-finished | B |
| ITM-5110-30-0010 | 5110-30-0010 | Piston, dia 54 mm, steel, chrome plated | Purchased | B |
| ITM-5110-30-0020 | 5110-30-0020 | Piston Seal, square section, EPDM | Purchased | A |
| ITM-5110-30-0030 | 5110-30-0030 | Dust Boot, EPDM | Purchased | A |
| ITM-5110-30-0040 | 5110-30-0040 | Bleed Screw M10 x 1.0 with cap | Purchased | A |
| ITM-5110-30-0050 | 5110-30-0050 | Guide Pin with boot | Purchased | B |
| ITM-5110-30-0060 | 5110-30-0060 | Brake Pad Set | Purchased | A |
| ITM-5110-30-0070 | 5110-30-0070 | Mounting Bracket | Purchased | B |
| ITM-RM-A356 | RM-A356 | Aluminium alloy ingot AlSi7Mg0.3 (A356) | Raw material | - |

### 3.2 Operations and work centers

| Step | u_mes_prd_operation._id | name | u_mes_mdm_workCenter._id | u_mes_mdm_line._id | u_mes_mdm_area._id | Tracking grain |
|---|---|---|---|---|---|---|
| OP010 | OPN-OP010 | Gravity die casting | WC-GDC-01 | LN-GDC-01 | AR-FDY | Lot |
| OP020 | OPN-OP020 | Heat treatment T6 | WC-HT-01 | LN-HT-01 | AR-HT | Lot |
| OP030 | OPN-OP030 | CNC machining | WC-CNC-01 | LN-MC-01 | AR-MC | Lot |
| OP040 | OPN-OP040 | Washing | WC-WSH-01 | LN-WSH-01 | AR-SF | Lot |
| OP050 | OPN-OP050 | Anodising | WC-ANO-01 | LN-ANO-01 | AR-SF | Lot |
| OP060 | OPN-OP060 | Piston and seal assembly | WC-ASY-01 | LN-ASY-01 | AR-ASY | Unit |
| OP070 | OPN-OP070 | Bleed screw torque | WC-TRQ-01 | LN-ASY-01 | AR-ASY | Unit |
| OP080 | OPN-OP080 | Pressure leak test | WC-LKT-01 | LN-ASY-01 | AR-ASY | Unit |
| OP090 | OPN-OP090 | Laser marking (serial and 2D code) | WC-LSR-01 | LN-ASY-01 | AR-ASY | Unit |
| OP100 | OPN-OP100 | Final inspection | WC-FIP-01 | LN-FIP-01 | AR-FIP | Unit |
| OP110 | OPN-OP110 | Packing | WC-FIP-01 | LN-PKG-01 | AR-FIP | Container |

Dispatch is recorded in u_mes_mat_shipment from area AR-WH; it is not a routing operation.

### 3.3 Areas and lines

Areas (u_mes_mdm_area): AR-FDY Foundry, AR-HT Heat treatment, AR-MC Machining, AR-SF Surface treatment (washing and anodising), AR-ASY Assembly and test, AR-FIP Final inspection and packing, AR-WH Stores and dispatch, AR-QL Quality laboratory, AR-TR Tool room, AR-UT Utilities.

Lines (u_mes_mdm_line): LN-GDC-01, LN-GDC-02, LN-HT-01, LN-MC-01, LN-MC-02, LN-WSH-01, LN-ANO-01, LN-ASY-01, LN-FIP-01, LN-PKG-01.

System account for automated writes: USR-SYSTEM, display name "MES System" (exists in u_mes_mdm_user).

### 3.4 IDs still to be assigned

Equipment, users, roles, suppliers, remaining customers, gauges, tools, characteristics, defect codes and reason codes are assigned when their collection specification is written and are added here at that point.

## 4. Collection register


### mdm - Master data

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_mdm_enterprise | entity | master | ENT-<recordNo> | enterpriseCode | - | 26 |
| 2 | u_mes_mdm_enterpriseContact | child | master | <enterpriseId>-C<nnn> | parent recordNo + -C<nnn> | u_mes_mdm_enterprise | 12 |
| 3 | u_mes_mdm_site | entity | master | SITE-<recordNo> | siteCode | - | 30 |
| 4 | u_mes_mdm_siteCertificate | child | master | <siteId>-C<nnn> | parent recordNo + -C<nnn> | u_mes_mdm_site | 12 |
| 5 | u_mes_mdm_area | entity | master | AR-<recordNo> | areaCode | - | 17 |
| 6 | u_mes_mdm_line | entity | master | LN-<recordNo> | lineCode | - | 22 |
| 7 | u_mes_mdm_lineDefaultShift | relationship | master | <lineId>-DS<nnn> | parent recordNo + -DS<nnn> | u_mes_mdm_line | 10 |
| 8 | u_mes_mdm_lineIdealRate | child | master | <lineId>-IR<nnn> | parent recordNo + -IR<nnn> | u_mes_mdm_line | 12 |
| 9 | u_mes_mdm_workCenter | entity | master | WC-<recordNo> | workCentreCode | - | 24 |
| 10 | u_mes_mdm_workCenterEquipment | relationship | master | <workCenterId>-E<nnn> | parent recordNo + -E<nnn> | u_mes_mdm_workCenter | 10 |
| 11 | u_mes_mdm_workCenterOperation | relationship | master | <workCenterId>-O<nnn> | parent recordNo + -O<nnn> | u_mes_mdm_workCenter | 10 |
| 12 | u_mes_mdm_workCenterRequiresSkill | relationship | master | <workCenterId>-RS<nnn> | parent recordNo + -RS<nnn> | u_mes_mdm_workCenter | 10 |
| 13 | u_mes_mdm_equipment | entity | master | EQ-<recordNo> | equipmentCode | - | 41 |
| 14 | u_mes_mdm_equipmentIotDevice | relationship | master | <equipmentId>-ID<nnn> | parent recordNo + -ID<nnn> | u_mes_mdm_equipment | 10 |
| 15 | u_mes_mdm_shift | entity | master | SH-<recordNo> | shiftCode | - | 14 |
| 16 | u_mes_mdm_shiftBreak | child | master | <shiftId>-B<nnn> | parent recordNo + -B<nnn> | u_mes_mdm_shift | 12 |
| 17 | u_mes_mdm_shiftWorkingDay | valueList | master | <shiftId>-WD<nnn> | parent recordNo + -WD<nnn> | u_mes_mdm_shift | 9 |
| 18 | u_mes_mdm_workCalendar | entity | master | CAL-<recordNo> | calendarCode | - | 11 |
| 19 | u_mes_mdm_workCalendarLine | relationship | master | <workCalendarId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_mdm_workCalendar | 10 |
| 20 | u_mes_mdm_workCalendarShift | relationship | master | <workCalendarId>-S<nnn> | parent recordNo + -S<nnn> | u_mes_mdm_workCalendar | 10 |
| 21 | u_mes_mdm_workCalendarWeeklyOffDay | valueList | master | <workCalendarId>-WOD<nnn> | parent recordNo + -WOD<nnn> | u_mes_mdm_workCalendar | 9 |
| 22 | u_mes_mdm_workCalendarException | child | master | <workCalendarId>-E<nnn> | parent recordNo + -E<nnn> | u_mes_mdm_workCalendar | 12 |
| 23 | u_mes_mdm_workCalendarExceptionShift | relationship | master | <workCalendarExceptionId>-S<nnn> | parent recordNo + -S<nnn> | u_mes_mdm_workCalendarException | 10 |
| 24 | u_mes_mdm_shiftRoster | entity | transaction | ROS-<recordNo> | rosterNo | - | 25 |
| 25 | u_mes_mdm_shiftRosterAssignment | child | transaction | <shiftRosterId>-A<nnn> | parent recordNo + -A<nnn> | u_mes_mdm_shiftRoster | 22 |
| 26 | u_mes_mdm_role | entity | master | ROLE-<recordNo> | roleCode | - | 12 |
| 27 | u_mes_mdm_rolePermission | relationship | master | <roleId>-P<nnn> | parent recordNo + -P<nnn> | u_mes_mdm_role | 10 |
| 28 | u_mes_mdm_roleSignatureMeaning | relationship | master | <roleId>-SM<nnn> | parent recordNo + -SM<nnn> | u_mes_mdm_role | 10 |
| 29 | u_mes_mdm_user | entity | master | USR-<recordNo> | employeeNo | - | 33 |
| 30 | u_mes_mdm_userRole | relationship | master | <userId>-R<nnn> | parent recordNo + -R<nnn> | u_mes_mdm_user | 10 |
| 31 | u_mes_mdm_skill | entity | master | SKL-<recordNo> | skillCode | - | 16 |
| 32 | u_mes_mdm_skillOperation | relationship | master | <skillId>-O<nnn> | parent recordNo + -O<nnn> | u_mes_mdm_skill | 10 |
| 33 | u_mes_mdm_skillLevelScale | child | master | <skillId>-LS<nnn> | parent recordNo + -LS<nnn> | u_mes_mdm_skill | 10 |
| 34 | u_mes_mdm_skillCertification | entity | transaction | CERT-<recordNo> | certificationNo | - | 31 |
| 35 | u_mes_mdm_customer | entity | master | CUS-<recordNo> | customerCode | - | 26 |
| 36 | u_mes_mdm_customerShipTo | child | master | <customerId>-ST<nnn> | parent recordNo + -ST<nnn> | u_mes_mdm_customer | 16 |
| 37 | u_mes_mdm_customerContact | child | master | <customerId>-C<nnn> | parent recordNo + -C<nnn> | u_mes_mdm_customer | 12 |
| 38 | u_mes_mdm_supplier | entity | master | SUP-<recordNo> | supplierCode | - | 26 |
| 39 | u_mes_mdm_supplierContact | child | master | <supplierId>-C<nnn> | parent recordNo + -C<nnn> | u_mes_mdm_supplier | 12 |
| 40 | u_mes_mdm_supplierCertificate | child | master | <supplierId>-C2<nnn> | parent recordNo + -C2<nnn> | u_mes_mdm_supplier | 11 |
| 41 | u_mes_mdm_supplierSuppliedItem | relationship | master | <supplierId>-SI<nnn> | parent recordNo + -SI<nnn> | u_mes_mdm_supplier | 10 |
| 42 | u_mes_mdm_unitOfMeasure | entity | master | UOM-<recordNo> | uomCode | - | 17 |
| 43 | u_mes_mdm_department | entity | master | DEPT-<recordNo> | code | - | 15 |
| 44 | u_mes_mdm_designation | entity | master | DSG-<recordNo> | code | - | 13 |
| 45 | u_mes_mdm_employmentType | entity | master | EMT-<recordNo> | code | - | 10 |
| 46 | u_mes_mdm_costCenter | entity | master | CC-<recordNo> | code | - | 11 |
| 47 | u_mes_mdm_manufacturer | entity | master | MFR-<recordNo> | code | - | 12 |
| 48 | u_mes_mdm_equipmentType | entity | master | EQT-<recordNo> | code | - | 9 |
| 49 | u_mes_mdm_skillCategory | entity | master | SKC-<recordNo> | code | - | 9 |
| 50 | u_mes_mdm_permission | entity | master | PRM-<recordNo> | code | - | 11 |
| 51 | u_mes_mdm_signatureMeaning | entity | master | SGM-<recordNo> | code | - | 9 |
| 52 | u_mes_mdm_currency | entity | master | CUR-<recordNo> | code | - | 11 |
| 53 | u_mes_mdm_country | entity | master | CTY-<recordNo> | code | - | 10 |
| 54 | u_mes_mdm_language | entity | master | LNG-<recordNo> | code | - | 9 |
| 55 | u_mes_mdm_transporter | entity | master | TRP-<recordNo> | code | - | 11 |
| 56 | u_mes_mdm_commodity | entity | master | CMD-<recordNo> | code | - | 9 |

### prd - Product definition

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_prd_item | entity | master | ITM-<recordNo> | itemNo | - | 35 |
| 2 | u_mes_prd_itemRevision | child | master | <itemId>-R<nnn> | parent recordNo + -R<nnn> | u_mes_prd_item | 13 |
| 3 | u_mes_prd_itemCustomerPart | child | master | <itemId>-CP<nnn> | parent recordNo + -CP<nnn> | u_mes_prd_item | 12 |
| 4 | u_mes_prd_productVariant | entity | master | VAR-<recordNo> | variantCode | - | 28 |
| 5 | u_mes_prd_billOfMaterial | entity | master | BOM-<recordNo> | bomNo | - | 22 |
| 6 | u_mes_prd_billOfMaterialComponent | child | master | <billOfMaterialId>-C<nnn> | parent recordNo + -C<nnn> | u_mes_prd_billOfMaterial | 20 |
| 7 | u_mes_prd_billOfMaterialComponentProductVariant | relationship | master | <billOfMaterialComponentId>-PV<nnn> | parent recordNo + -PV<nnn> | u_mes_prd_billOfMaterialComponent | 10 |
| 8 | u_mes_prd_billOfMaterialComponentAlternateItem | relationship | master | <billOfMaterialComponentId>-AI<nnn> | parent recordNo + -AI<nnn> | u_mes_prd_billOfMaterialComponent | 10 |
| 9 | u_mes_prd_operation | entity | master | OPN-<recordNo> | operationCode | - | 21 |
| 10 | u_mes_prd_operationRequiredSkill | relationship | master | <operationId>-RS<nnn> | parent recordNo + -RS<nnn> | u_mes_prd_operation | 10 |
| 11 | u_mes_prd_routing | entity | master | RTG-<recordNo> | routingNo | - | 23 |
| 12 | u_mes_prd_routingStep | child | master | <routingId>-S<nnn> | parent recordNo + -S<nnn> | u_mes_prd_routing | 19 |
| 13 | u_mes_prd_routingStepAlternateWorkCenter | relationship | master | <routingStepId>-AWC<nnn> | parent recordNo + -AWC<nnn> | u_mes_prd_routingStep | 10 |
| 14 | u_mes_prd_routingStepNextStep | child | master | <routingStepId>-NS<nnn> | parent recordNo + -NS<nnn> | u_mes_prd_routingStep | 9 |
| 15 | u_mes_prd_billOfProcess | entity | master | BOP-<recordNo> | bopNo | - | 19 |
| 16 | u_mes_prd_billOfProcessStep | child | master | <billOfProcessId>-S<nnn> | parent recordNo + -S<nnn> | u_mes_prd_billOfProcess | 18 |
| 17 | u_mes_prd_billOfProcessStepEquipment | relationship | master | <billOfProcessStepId>-E<nnn> | parent recordNo + -E<nnn> | u_mes_prd_billOfProcessStep | 10 |
| 18 | u_mes_prd_billOfProcessStepTool | relationship | master | <billOfProcessStepId>-T<nnn> | parent recordNo + -T<nnn> | u_mes_prd_billOfProcessStep | 10 |
| 19 | u_mes_prd_billOfProcessStepRequiredSkill | relationship | master | <billOfProcessStepId>-RS<nnn> | parent recordNo + -RS<nnn> | u_mes_prd_billOfProcessStep | 10 |
| 20 | u_mes_prd_billOfProcessStepConsumedComponent | child | master | <billOfProcessStepId>-CC<nnn> | parent recordNo + -CC<nnn> | u_mes_prd_billOfProcessStep | 12 |
| 21 | u_mes_prd_billOfProcessStepInterlock | child | master | <billOfProcessStepId>-I<nnn> | parent recordNo + -I<nnn> | u_mes_prd_billOfProcessStep | 11 |
| 22 | u_mes_prd_billOfProcessStepProcessParameter | child | master | <billOfProcessStepId>-PP<nnn> | parent recordNo + -PP<nnn> | u_mes_prd_billOfProcessStep | 14 |
| 23 | u_mes_prd_workInstruction | entity | master | WI-<recordNo> | instructionNo | - | 25 |
| 24 | u_mes_prd_workInstructionStep | child | master | <workInstructionId>-S<nnn> | parent recordNo + -S<nnn> | u_mes_prd_workInstruction | 18 |
| 25 | u_mes_prd_workInstructionStepMediaControlledDocument | relationship | master | <workInstructionStepId>-MCD<nnn> | parent recordNo + -MCD<nnn> | u_mes_prd_workInstructionStep | 10 |
| 26 | u_mes_prd_workInstructionStepProductVariant | relationship | master | <workInstructionStepId>-PV<nnn> | parent recordNo + -PV<nnn> | u_mes_prd_workInstructionStep | 10 |
| 27 | u_mes_prd_workInstructionStepTool | relationship | master | <workInstructionStepId>-T<nnn> | parent recordNo + -T<nnn> | u_mes_prd_workInstructionStep | 10 |
| 28 | u_mes_prd_workInstructionStepCharacteristic | relationship | master | <workInstructionStepId>-C<nnn> | parent recordNo + -C<nnn> | u_mes_prd_workInstructionStep | 10 |
| 29 | u_mes_prd_workInstructionPpeItem | relationship | master | <workInstructionId>-PI<nnn> | parent recordNo + -PI<nnn> | u_mes_prd_workInstruction | 10 |
| 30 | u_mes_prd_workInstructionKeyPoint | valueList | master | <workInstructionId>-KP<nnn> | parent recordNo + -KP<nnn> | u_mes_prd_workInstruction | 9 |
| 31 | u_mes_prd_recipe | entity | master | RCP-<recordNo> | recipeNo | - | 25 |
| 32 | u_mes_prd_recipeParameter | child | master | <recipeId>-P<nnn> | parent recordNo + -P<nnn> | u_mes_prd_recipe | 18 |
| 33 | u_mes_prd_recipeStage | child | master | <recipeId>-S<nnn> | parent recordNo + -S<nnn> | u_mes_prd_recipe | 11 |
| 34 | u_mes_prd_engineeringChange | entity | transaction | ECN-<recordNo> | ecnNo | - | 31 |
| 35 | u_mes_prd_engineeringChangeAffectedItem | child | transaction | <engineeringChangeId>-AI<nnn> | parent recordNo + -AI<nnn> | u_mes_prd_engineeringChange | 18 |
| 36 | u_mes_prd_engineeringChangeAffectedObject | child | transaction | <engineeringChangeId>-AO<nnn> | parent recordNo + -AO<nnn> | u_mes_prd_engineeringChange | 18 |
| 37 | u_mes_prd_engineeringChangeApproval | child | transaction | <engineeringChangeId>-A<nnn> | parent recordNo + -A<nnn> | u_mes_prd_engineeringChange | 20 |
| 38 | u_mes_prd_engineeringChangeControlledDocument | relationship | transaction | <engineeringChangeId>-CD<nnn> | parent recordNo + -CD<nnn> | u_mes_prd_engineeringChange | 16 |
| 39 | u_mes_prd_itemGroup | entity | master | IGR-<recordNo> | code | - | 9 |
| 40 | u_mes_prd_itemFamily | entity | master | IFM-<recordNo> | code | - | 9 |
| 41 | u_mes_prd_ppeItem | entity | master | PPE-<recordNo> | code | - | 9 |
| 42 | u_mes_prd_market | entity | master | MKT-<recordNo> | code | - | 9 |
| 43 | u_mes_prd_padCompound | entity | master | PDC-<recordNo> | code | - | 9 |
| 44 | u_mes_prd_surfaceFinish | entity | master | SFN-<recordNo> | code | - | 9 |
| 45 | u_mes_prd_vehicleModel | entity | master | VHM-<recordNo> | code | - | 13 |

### exe - Planning and execution

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_exe_customerSchedule | entity | transaction | CSR-<recordNo> | releaseNo | - | 23 |
| 2 | u_mes_exe_customerScheduleLine | child | transaction | <customerScheduleId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_exe_customerSchedule | 23 |
| 3 | u_mes_exe_productionOrder | entity | transaction | PO-<recordNo> | orderNo | - | 47 |
| 4 | u_mes_exe_productionOrderRelease | child | transaction | <productionOrderId>-R<nnn> | parent recordNo + -R<nnn> | u_mes_exe_productionOrder | 18 |
| 5 | u_mes_exe_productionOrderLot | relationship | transaction | <productionOrderId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_exe_productionOrder | 16 |
| 6 | u_mes_exe_productionSchedule | entity | transaction | SCH-<recordNo> | scheduleNo | - | 27 |
| 7 | u_mes_exe_productionScheduleSlot | child | transaction | <productionScheduleId>-S<nnn> | parent recordNo + -S<nnn> | u_mes_exe_productionSchedule | 23 |
| 8 | u_mes_exe_dispatchList | entity | transaction | DSP-<recordNo> | dispatchNo | - | 22 |
| 9 | u_mes_exe_dispatchListEntry | child | transaction | <dispatchListId>-E<nnn> | parent recordNo + -E<nnn> | u_mes_exe_dispatchList | 28 |
| 10 | u_mes_exe_operationExecution | entity | transaction | OPX-<recordNo> | executionNo | - | 53 |
| 11 | u_mes_exe_operationExecutionDefectCode | relationship | transaction | <operationExecutionId>-DC<nnn> | parent recordNo + -DC<nnn> | u_mes_exe_operationExecution | 16 |
| 12 | u_mes_exe_operationExecutionTool | relationship | transaction | <operationExecutionId>-T<nnn> | parent recordNo + -T<nnn> | u_mes_exe_operationExecution | 16 |
| 13 | u_mes_exe_stepCompletion | entity | transaction | STC-<recordNo> | completionNo | - | 40 |
| 14 | u_mes_exe_wipUnit | entity | transaction | WU-<recordNo> | unitNo | - | 47 |
| 15 | u_mes_exe_wipUnitCompletedStep | valueList | transaction | <wipUnitId>-CS<nnn> | parent recordNo + -CS<nnn> | u_mes_exe_wipUnit | 15 |
| 16 | u_mes_exe_lot | entity | transaction | LOT-<recordNo> | lotNo | - | 47 |
| 17 | u_mes_exe_lotParentLot | relationship | transaction | <lotId>-PL<nnn> | parent recordNo + -PL<nnn> | u_mes_exe_lot | 16 |
| 18 | u_mes_exe_lotAttributesCavityNo | valueList | transaction | <lotId>-ACN<nnn> | parent recordNo + -ACN<nnn> | u_mes_exe_lot | 15 |
| 19 | u_mes_exe_container | entity | transaction | CNT-<recordNo> | containerNo | - | 39 |
| 20 | u_mes_exe_containerLot | relationship | transaction | <containerId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_exe_container | 16 |
| 21 | u_mes_exe_labourBooking | entity | transaction | LAB-<recordNo> | bookingNo | - | 36 |
| 22 | u_mes_exe_changeover | entity | transaction | CHG-<recordNo> | changeoverNo | - | 40 |
| 23 | u_mes_exe_changeoverStep | child | transaction | <changeoverId>-S<nnn> | parent recordNo + -S<nnn> | u_mes_exe_changeover | 19 |
| 24 | u_mes_exe_changeoverRemovedTool | relationship | transaction | <changeoverId>-RT<nnn> | parent recordNo + -RT<nnn> | u_mes_exe_changeover | 16 |
| 25 | u_mes_exe_changeoverInstalledTool | relationship | transaction | <changeoverId>-IT<nnn> | parent recordNo + -IT<nnn> | u_mes_exe_changeover | 16 |
| 26 | u_mes_exe_changeoverPerformedByUser | relationship | transaction | <changeoverId>-PBU<nnn> | parent recordNo + -PBU<nnn> | u_mes_exe_changeover | 16 |
| 27 | u_mes_exe_shiftHandover | entity | transaction | SHO-<recordNo> | handoverNo | - | 32 |
| 28 | u_mes_exe_shiftHandoverProductionOrder | relationship | transaction | <shiftHandoverId>-PO<nnn> | parent recordNo + -PO<nnn> | u_mes_exe_shiftHandover | 16 |
| 29 | u_mes_exe_shiftHandoverDowntimeEvent | relationship | transaction | <shiftHandoverId>-DE<nnn> | parent recordNo + -DE<nnn> | u_mes_exe_shiftHandover | 16 |
| 30 | u_mes_exe_shiftHandoverNonconformance | relationship | transaction | <shiftHandoverId>-N<nnn> | parent recordNo + -N<nnn> | u_mes_exe_shiftHandover | 16 |
| 31 | u_mes_exe_shiftHandoverOpenItem | child | transaction | <shiftHandoverId>-OI<nnn> | parent recordNo + -OI<nnn> | u_mes_exe_shiftHandover | 19 |
| 32 | u_mes_exe_indirectActivity | entity | master | IND-<recordNo> | code | - | 12 |
| 33 | u_mes_exe_containerType | entity | master | CTT-<recordNo> | code | - | 14 |

### mat - Materials

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_mat_storageLocation | entity | master | LOC-<recordNo> | locationCode | - | 24 |
| 2 | u_mes_mat_inventoryBalance | entity | transaction | INV-<recordNo> | inventoryNo | - | 33 |
| 3 | u_mes_mat_materialMovement | entity | transaction | MM-<recordNo> | movementNo | - | 48 |
| 4 | u_mes_mat_goodsReceipt | entity | transaction | GRN-<recordNo> | grnNo | - | 25 |
| 5 | u_mes_mat_goodsReceiptLine | child | transaction | <goodsReceiptId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_mat_goodsReceipt | 29 |
| 6 | u_mes_mat_goodsReceiptLineInspectionResult | relationship | transaction | <goodsReceiptLineId>-IR<nnn> | parent recordNo + -IR<nnn> | u_mes_mat_goodsReceiptLine | 16 |
| 7 | u_mes_mat_kit | entity | transaction | KIT-<recordNo> | kitNo | - | 28 |
| 8 | u_mes_mat_kitLine | child | transaction | <kitId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_mat_kit | 23 |
| 9 | u_mes_mat_materialRequest | entity | transaction | MRQ-<recordNo> | requestNo | - | 39 |
| 10 | u_mes_mat_materialConsumption | entity | transaction | CON-<recordNo> | consumptionNo | - | 43 |
| 11 | u_mes_mat_packagingSpecification | entity | master | PKS-<recordNo> | packSpecNo | - | 28 |
| 12 | u_mes_mat_packagingSpecificationLevel | child | master | <packagingSpecificationId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_mat_packagingSpecification | 14 |
| 13 | u_mes_mat_labelTemplate | entity | master | LBT-<recordNo> | templateCode | - | 19 |
| 14 | u_mes_mat_labelTemplateField | child | master | <labelTemplateId>-F<nnn> | parent recordNo + -F<nnn> | u_mes_mat_labelTemplate | 14 |
| 15 | u_mes_mat_label | entity | transaction | LBL-<recordNo> | labelNo | - | 41 |
| 16 | u_mes_mat_shipment | entity | transaction | SHP-<recordNo> | shipmentNo | - | 39 |
| 17 | u_mes_mat_shipmentLine | child | transaction | <shipmentId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_mat_shipment | 18 |
| 18 | u_mes_mat_shipmentLineContainer | relationship | transaction | <shipmentLineId>-C<nnn> | parent recordNo + -C<nnn> | u_mes_mat_shipmentLine | 16 |
| 19 | u_mes_mat_shipmentLineLot | relationship | transaction | <shipmentLineId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_mat_shipmentLine | 16 |
| 20 | u_mes_mat_movementType | entity | master | MVT-<recordNo> | code | - | 12 |
| 21 | u_mes_mat_stockStatus | entity | master | STS-<recordNo> | code | - | 11 |
| 22 | u_mes_mat_packType | entity | master | PKT-<recordNo> | code | - | 9 |

### trc - Traceability

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_trc_serialNumber | entity | transaction | SN-<recordNo> | serialNo | - | 40 |
| 2 | u_mes_trc_genealogyLink | entity | transaction | GEN-<recordNo> | linkNo | - | 39 |
| 3 | u_mes_trc_componentLotLink | entity | transaction | CLL-<recordNo> | lotLinkNo | - | 32 |
| 4 | u_mes_trc_asBuiltRecord | entity | transaction | ABR-<recordNo> | recordNo | - | 51 |
| 5 | u_mes_trc_asBuiltRecordComponent | child | transaction | <asBuiltRecordId>-C<nnn> | parent recordNo + -C<nnn> | u_mes_trc_asBuiltRecord | 22 |
| 6 | u_mes_trc_asBuiltRecordOperation | child | transaction | <asBuiltRecordId>-O<nnn> | parent recordNo + -O<nnn> | u_mes_trc_asBuiltRecord | 24 |
| 7 | u_mes_trc_asBuiltRecordInspectionResult | relationship | transaction | <asBuiltRecordId>-IR<nnn> | parent recordNo + -IR<nnn> | u_mes_trc_asBuiltRecord | 16 |

### qlt - Quality

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_qlt_characteristic | entity | master | CHR-<recordNo> | characteristicCode | - | 32 |
| 2 | u_mes_qlt_controlPlan | entity | master | CP-<recordNo> | controlPlanNo | - | 26 |
| 3 | u_mes_qlt_controlPlanCoreTeamUser | relationship | master | <controlPlanId>-CTU<nnn> | parent recordNo + -CTU<nnn> | u_mes_qlt_controlPlan | 10 |
| 4 | u_mes_qlt_controlPlanLine | child | master | <controlPlanId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_qlt_controlPlan | 24 |
| 5 | u_mes_qlt_inspectionPlan | entity | master | IP-<recordNo> | inspectionPlanNo | - | 26 |
| 6 | u_mes_qlt_inspectionPlanLine | child | master | <inspectionPlanId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_qlt_inspectionPlan | 20 |
| 7 | u_mes_qlt_samplingPlan | entity | master | SMP-<recordNo> | samplingPlanCode | - | 18 |
| 8 | u_mes_qlt_samplingPlanSizeRow | child | master | <samplingPlanId>-SR<nnn> | parent recordNo + -SR<nnn> | u_mes_qlt_samplingPlan | 13 |
| 9 | u_mes_qlt_checkSheet | entity | master | CKS-<recordNo> | checkSheetCode | - | 24 |
| 10 | u_mes_qlt_checkSheetItem | child | master | <checkSheetId>-I<nnn> | parent recordNo + -I<nnn> | u_mes_qlt_checkSheet | 16 |
| 11 | u_mes_qlt_checkSheetResult | entity | transaction | CKR-<recordNo> | checkResultNo | - | 36 |
| 12 | u_mes_qlt_checkSheetResultAnswer | child | transaction | <checkSheetResultId>-A<nnn> | parent recordNo + -A<nnn> | u_mes_qlt_checkSheetResult | 18 |
| 13 | u_mes_qlt_inspectionResult | entity | transaction | IR-<recordNo> | resultNo | - | 54 |
| 14 | u_mes_qlt_spcChart | entity | master | SPC-<recordNo> | chartNo | - | 29 |
| 15 | u_mes_qlt_spcChartControlLimit | child | master | <spcChartId>-CL<nnn> | parent recordNo + -CL<nnn> | u_mes_qlt_spcChart | 16 |
| 16 | u_mes_qlt_spcChartRule | valueList | master | <spcChartId>-R<nnn> | parent recordNo + -R<nnn> | u_mes_qlt_spcChart | 9 |
| 17 | u_mes_qlt_spcSample | entity | transaction | SPS-<recordNo> | sampleNo | - | 36 |
| 18 | u_mes_qlt_spcSampleReading | valueList | transaction | <spcSampleId>-R<nnn> | parent recordNo + -R<nnn> | u_mes_qlt_spcSample | 15 |
| 19 | u_mes_qlt_spcSampleInspectionResult | relationship | transaction | <spcSampleId>-IR<nnn> | parent recordNo + -IR<nnn> | u_mes_qlt_spcSample | 16 |
| 20 | u_mes_qlt_spcSampleViolation | child | transaction | <spcSampleId>-V<nnn> | parent recordNo + -V<nnn> | u_mes_qlt_spcSample | 16 |
| 21 | u_mes_qlt_defectCode | entity | master | DEF-<recordNo> | defectCode | - | 21 |
| 22 | u_mes_qlt_defectCodeApplicableOperation | relationship | master | <defectCodeId>-AO<nnn> | parent recordNo + -AO<nnn> | u_mes_qlt_defectCode | 10 |
| 23 | u_mes_qlt_nonconformance | entity | transaction | NCR-<recordNo> | ncrNo | - | 45 |
| 24 | u_mes_qlt_nonconformanceAffectedObject | child | transaction | <nonconformanceId>-AO<nnn> | parent recordNo + -AO<nnn> | u_mes_qlt_nonconformance | 23 |
| 25 | u_mes_qlt_nonconformanceContainmentAction | child | transaction | <nonconformanceId>-CA<nnn> | parent recordNo + -CA<nnn> | u_mes_qlt_nonconformance | 18 |
| 26 | u_mes_qlt_nonconformanceInspectionResult | relationship | transaction | <nonconformanceId>-IR<nnn> | parent recordNo + -IR<nnn> | u_mes_qlt_nonconformance | 16 |
| 27 | u_mes_qlt_nonconformanceReworkOrder | relationship | transaction | <nonconformanceId>-RO<nnn> | parent recordNo + -RO<nnn> | u_mes_qlt_nonconformance | 16 |
| 28 | u_mes_qlt_nonconformanceScrapRecord | relationship | transaction | <nonconformanceId>-SR<nnn> | parent recordNo + -SR<nnn> | u_mes_qlt_nonconformance | 16 |
| 29 | u_mes_qlt_nonconformancePhotoControlledDocument | relationship | transaction | <nonconformanceId>-PCD<nnn> | parent recordNo + -PCD<nnn> | u_mes_qlt_nonconformance | 16 |
| 30 | u_mes_qlt_nonconformanceMrbUser | relationship | transaction | <nonconformanceId>-MU<nnn> | parent recordNo + -MU<nnn> | u_mes_qlt_nonconformance | 16 |
| 31 | u_mes_qlt_reworkOrder | entity | transaction | RWK-<recordNo> | reworkNo | - | 39 |
| 32 | u_mes_qlt_reworkOrderWipUnit | relationship | transaction | <reworkOrderId>-WU<nnn> | parent recordNo + -WU<nnn> | u_mes_qlt_reworkOrder | 16 |
| 33 | u_mes_qlt_reworkOrderStep | child | transaction | <reworkOrderId>-S<nnn> | parent recordNo + -S<nnn> | u_mes_qlt_reworkOrder | 20 |
| 34 | u_mes_qlt_scrapRecord | entity | transaction | SCR-<recordNo> | scrapNo | - | 46 |
| 35 | u_mes_qlt_qualityHold | entity | transaction | HLD-<recordNo> | holdNo | - | 33 |
| 36 | u_mes_qlt_qualityHoldHeldObject | child | transaction | <qualityHoldId>-HO<nnn> | parent recordNo + -HO<nnn> | u_mes_qlt_qualityHold | 20 |
| 37 | u_mes_qlt_deviationPermit | entity | transaction | DEV-<recordNo> | deviationNo | - | 38 |
| 38 | u_mes_qlt_deviationPermitApproval | child | transaction | <deviationPermitId>-A<nnn> | parent recordNo + -A<nnn> | u_mes_qlt_deviationPermit | 19 |
| 39 | u_mes_qlt_capa | entity | transaction | CAPA-<recordNo> | capaNo | - | 42 |
| 40 | u_mes_qlt_capaNonconformance | relationship | transaction | <capaId>-N<nnn> | parent recordNo + -N<nnn> | u_mes_qlt_capa | 16 |
| 41 | u_mes_qlt_capaTeamMember | child | transaction | <capaId>-TM<nnn> | parent recordNo + -TM<nnn> | u_mes_qlt_capa | 17 |
| 42 | u_mes_qlt_capaContainmentAction | child | transaction | <capaId>-CA<nnn> | parent recordNo + -CA<nnn> | u_mes_qlt_capa | 18 |
| 43 | u_mes_qlt_capaCorrectiveAction | child | transaction | <capaId>-CA2<nnn> | parent recordNo + -CA2<nnn> | u_mes_qlt_capa | 18 |
| 44 | u_mes_qlt_capaImplementationAction | child | transaction | <capaId>-IA<nnn> | parent recordNo + -IA<nnn> | u_mes_qlt_capa | 19 |
| 45 | u_mes_qlt_capaControlledDocument | relationship | transaction | <capaId>-CD<nnn> | parent recordNo + -CD<nnn> | u_mes_qlt_capa | 16 |
| 46 | u_mes_qlt_pfmea | entity | master | FMEA-<recordNo> | pfmeaNo | - | 19 |
| 47 | u_mes_qlt_pfmeaCoreTeamUser | relationship | master | <pfmeaId>-CTU<nnn> | parent recordNo + -CTU<nnn> | u_mes_qlt_pfmea | 10 |
| 48 | u_mes_qlt_pfmeaLine | child | master | <pfmeaId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_qlt_pfmea | 32 |
| 49 | u_mes_qlt_ppapSubmission | entity | transaction | PPAP-<recordNo> | ppapNo | - | 35 |
| 50 | u_mes_qlt_ppapSubmissionElement | child | transaction | <ppapSubmissionId>-E<nnn> | parent recordNo + -E<nnn> | u_mes_qlt_ppapSubmission | 19 |
| 51 | u_mes_qlt_ppapSubmissionMsaStudy | relationship | transaction | <ppapSubmissionId>-MS<nnn> | parent recordNo + -MS<nnn> | u_mes_qlt_ppapSubmission | 16 |
| 52 | u_mes_qlt_gauge | entity | master | GAU-<recordNo> | gaugeNo | - | 37 |
| 53 | u_mes_qlt_gaugeCalibration | entity | transaction | GCAL-<recordNo> | calibrationNo | - | 35 |
| 54 | u_mes_qlt_gaugeCalibrationReading | child | transaction | <gaugeCalibrationId>-R<nnn> | parent recordNo + -R<nnn> | u_mes_qlt_gaugeCalibration | 19 |
| 55 | u_mes_qlt_msaStudy | entity | transaction | MSA-<recordNo> | msaNo | - | 41 |
| 56 | u_mes_qlt_msaStudyAppraiserUser | relationship | transaction | <msaStudyId>-AU<nnn> | parent recordNo + -AU<nnn> | u_mes_qlt_msaStudy | 16 |
| 57 | u_mes_qlt_msaStudyTrial | child | transaction | <msaStudyId>-T<nnn> | parent recordNo + -T<nnn> | u_mes_qlt_msaStudy | 18 |
| 58 | u_mes_qlt_audit | entity | transaction | AUD-<recordNo> | auditNo | - | 39 |
| 59 | u_mes_qlt_auditAuditorUser | relationship | transaction | <auditId>-AU<nnn> | parent recordNo + -AU<nnn> | u_mes_qlt_audit | 16 |
| 60 | u_mes_qlt_auditFinding | child | transaction | <auditId>-F<nnn> | parent recordNo + -F<nnn> | u_mes_qlt_audit | 23 |
| 61 | u_mes_qlt_customerComplaint | entity | transaction | CMP-<recordNo> | complaintNo | - | 43 |
| 62 | u_mes_qlt_customerComplaintSerialNumber | relationship | transaction | <customerComplaintId>-SN<nnn> | parent recordNo + -SN<nnn> | u_mes_qlt_customerComplaint | 16 |
| 63 | u_mes_qlt_customerComplaintShipment | relationship | transaction | <customerComplaintId>-S<nnn> | parent recordNo + -S<nnn> | u_mes_qlt_customerComplaint | 16 |
| 64 | u_mes_qlt_customerComplaintSuspectLot | relationship | transaction | <customerComplaintId>-SL<nnn> | parent recordNo + -SL<nnn> | u_mes_qlt_customerComplaint | 16 |
| 65 | u_mes_qlt_customerComplaintCommunication | child | transaction | <customerComplaintId>-C<nnn> | parent recordNo + -C<nnn> | u_mes_qlt_customerComplaint | 19 |
| 66 | u_mes_qlt_defectGroup | entity | master | DGR-<recordNo> | code | - | 9 |
| 67 | u_mes_qlt_gaugeType | entity | master | GTY-<recordNo> | code | - | 9 |
| 68 | u_mes_qlt_dispositionType | entity | master | DSP-T-<recordNo> | code | - | 12 |
| 69 | u_mes_qlt_complaintType | entity | master | CPT-<recordNo> | code | - | 9 |

### eqp - Equipment and performance

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_eqp_reasonCode | entity | master | RSN-<recordNo> | reasonCode | - | 23 |
| 2 | u_mes_eqp_equipmentState | entity | transaction | EST-<recordNo> | stateEventNo | - | 30 |
| 3 | u_mes_eqp_downtimeEvent | entity | transaction | DT-<recordNo> | downtimeNo | - | 47 |
| 4 | u_mes_eqp_downtimeEventComment | child | transaction | <downtimeEventId>-C<nnn> | parent recordNo + -C<nnn> | u_mes_eqp_downtimeEvent | 18 |
| 5 | u_mes_eqp_productionCount | entity | transaction | PC-<recordNo> | countNo | - | 34 |
| 6 | u_mes_eqp_oeeRecord | entity | transaction | OEE-<recordNo> | oeeRecordNo | - | 42 |
| 7 | u_mes_eqp_oeeRecordLoss | child | transaction | <oeeRecordId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_eqp_oeeRecord | 20 |
| 8 | u_mes_eqp_processTag | entity | master | TAG-<recordNo> | tagName | - | 28 |
| 9 | u_mes_eqp_processReading | entity | transaction | PD-<recordNo> | readingNo | - | 24 |
| 10 | u_mes_eqp_alarm | entity | transaction | ALM-<recordNo> | alarmNo | - | 36 |
| 11 | u_mes_eqp_torqueResult | entity | transaction | TRQ-<recordNo> | torqueResultNo | - | 46 |
| 12 | u_mes_eqp_leakTestResult | entity | transaction | LKT-<recordNo> | leakTestNo | - | 35 |
| 13 | u_mes_eqp_leakTestResultStage | child | transaction | <leakTestResultId>-S<nnn> | parent recordNo + -S<nnn> | u_mes_eqp_leakTestResult | 24 |
| 14 | u_mes_eqp_lossCategory | entity | master | LSC-<recordNo> | code | - | 11 |
| 15 | u_mes_eqp_reasonCategory | entity | master | RCT-<recordNo> | code | - | 9 |

### mnt - Maintenance and tooling

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_mnt_maintenancePlan | entity | master | MP-<recordNo> | planNo | - | 24 |
| 2 | u_mes_mnt_maintenancePlanTask | child | master | <maintenancePlanId>-T<nnn> | parent recordNo + -T<nnn> | u_mes_mnt_maintenancePlan | 12 |
| 3 | u_mes_mnt_maintenancePlanRequiredSkill | relationship | master | <maintenancePlanId>-RS<nnn> | parent recordNo + -RS<nnn> | u_mes_mnt_maintenancePlan | 10 |
| 4 | u_mes_mnt_maintenancePlanRequiredSparePart | child | master | <maintenancePlanId>-RSP<nnn> | parent recordNo + -RSP<nnn> | u_mes_mnt_maintenancePlan | 11 |
| 5 | u_mes_mnt_maintenanceWorkOrder | entity | transaction | MWO-<recordNo> | workOrderNo | - | 43 |
| 6 | u_mes_mnt_maintenanceWorkOrderAssignedToUser | relationship | transaction | <maintenanceWorkOrderId>-ATU<nnn> | parent recordNo + -ATU<nnn> | u_mes_mnt_maintenanceWorkOrder | 16 |
| 7 | u_mes_mnt_maintenanceWorkOrderLabour | child | transaction | <maintenanceWorkOrderId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_mnt_maintenanceWorkOrder | 17 |
| 8 | u_mes_mnt_maintenanceWorkOrderUsedSparePart | child | transaction | <maintenanceWorkOrderId>-USP<nnn> | parent recordNo + -USP<nnn> | u_mes_mnt_maintenanceWorkOrder | 18 |
| 9 | u_mes_mnt_sparePart | entity | master | SPR-<recordNo> | sparePartNo | - | 26 |
| 10 | u_mes_mnt_sparePartUsedOnEquipment | relationship | master | <sparePartId>-UOE<nnn> | parent recordNo + -UOE<nnn> | u_mes_mnt_sparePart | 10 |
| 11 | u_mes_mnt_tool | entity | master | TL-<recordNo> | toolNo | - | 33 |
| 12 | u_mes_mnt_toolItem | relationship | master | <toolId>-I<nnn> | parent recordNo + -I<nnn> | u_mes_mnt_tool | 10 |
| 13 | u_mes_mnt_toolLifeRecord | entity | transaction | TLR-<recordNo> | toolLifeNo | - | 33 |
| 14 | u_mes_mnt_toolType | entity | master | TLT-<recordNo> | code | - | 10 |

### sys - Integration and system

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_sys_erpMessage | entity | transaction | MSG-<recordNo> | messageNo | - | 40 |
| 2 | u_mes_sys_integrationConnector | entity | master | ICN-<recordNo> | connectorCode | - | 22 |
| 3 | u_mes_sys_integrationConnectorFunction | child | master | <integrationConnectorId>-F<nnn> | parent recordNo + -F<nnn> | u_mes_sys_integrationConnector | 13 |
| 4 | u_mes_sys_iotDevice | entity | master | IOT-<recordNo> | deviceCode | - | 31 |
| 5 | u_mes_sys_operatorApp | entity | master | APP-<recordNo> | appCode | - | 17 |
| 6 | u_mes_sys_operatorAppWorkCenter | relationship | master | <operatorAppId>-WC<nnn> | parent recordNo + -WC<nnn> | u_mes_sys_operatorApp | 10 |
| 7 | u_mes_sys_operatorAppOperation | relationship | master | <operatorAppId>-O<nnn> | parent recordNo + -O<nnn> | u_mes_sys_operatorApp | 10 |
| 8 | u_mes_sys_operatorAppStep | child | master | <operatorAppId>-S<nnn> | parent recordNo + -S<nnn> | u_mes_sys_operatorApp | 15 |
| 9 | u_mes_sys_operatorAppStepTrigger | child | master | <operatorAppStepId>-T<nnn> | parent recordNo + -T<nnn> | u_mes_sys_operatorAppStep | 11 |
| 10 | u_mes_sys_operatorAppDeviceBinding | child | master | <operatorAppId>-DB<nnn> | parent recordNo + -DB<nnn> | u_mes_sys_operatorApp | 11 |
| 11 | u_mes_sys_operatorAppLanguage | relationship | master | <operatorAppId>-L<nnn> | parent recordNo + -L<nnn> | u_mes_sys_operatorApp | 10 |
| 12 | u_mes_sys_businessEvent | entity | transaction | EVT-<recordNo> | eventNo | - | 32 |
| 13 | u_mes_sys_auditTrail | entity | transaction | ADT-<recordNo> | auditTrailNo | - | 27 |
| 14 | u_mes_sys_auditTrailChange | child | transaction | <auditTrailId>-C<nnn> | parent recordNo + -C<nnn> | u_mes_sys_auditTrail | 17 |
| 15 | u_mes_sys_electronicSignature | entity | transaction | SIG-<recordNo> | signatureNo | - | 29 |
| 16 | u_mes_sys_notification | entity | transaction | NTF-<recordNo> | notificationNo | - | 32 |
| 17 | u_mes_sys_notificationRecipient | child | transaction | <notificationId>-R<nnn> | parent recordNo + -R<nnn> | u_mes_sys_notification | 22 |
| 18 | u_mes_sys_controlledDocument | entity | transaction | DOC-<recordNo> | documentNo | - | 38 |
| 19 | u_mes_sys_controlledDocumentTag | valueList | transaction | <controlledDocumentId>-T<nnn> | parent recordNo + -T<nnn> | u_mes_sys_controlledDocument | 15 |
| 20 | u_mes_sys_numberRange | entity | master | NR-<recordNo> | rangeCode | - | 24 |
| 21 | u_mes_sys_systemConfiguration | entity | master | CFG-<recordNo> | configKey | - | 18 |
| 22 | u_mes_sys_documentType | entity | master | DCT-<recordNo> | code | - | 11 |
| 23 | u_mes_sys_deviceType | entity | master | DVT-<recordNo> | code | - | 9 |
| 24 | u_mes_sys_notificationType | entity | master | NTT-<recordNo> | code | - | 9 |
| 25 | u_mes_sys_statusDefinition | entity | master | STD-<recordNo> | definition code | - | 15 |
| 26 | u_mes_sys_enumerationValue | entity | master | ENV-<recordNo> | definition code | - | 13 |
| 27 | u_mes_sys_statusTransition | entity | master | STT-<recordNo> | definition code | - | 15 |

### ehs - Energy, safety and andon

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_ehs_energyReading | entity | transaction | ENR-<recordNo> | energyReadingNo | - | 34 |
| 2 | u_mes_ehs_andonEvent | entity | transaction | AND-<recordNo> | andonNo | - | 38 |
| 3 | u_mes_ehs_andonEventEscalation | child | transaction | <andonEventId>-E<nnn> | parent recordNo + -E<nnn> | u_mes_ehs_andonEvent | 19 |
| 4 | u_mes_ehs_safetyIncident | entity | transaction | SAF-<recordNo> | incidentNo | - | 44 |
| 5 | u_mes_ehs_safetyIncidentWitnessUser | relationship | transaction | <safetyIncidentId>-WU<nnn> | parent recordNo + -WU<nnn> | u_mes_ehs_safetyIncident | 16 |
| 6 | u_mes_ehs_safetyIncidentAction | child | transaction | <safetyIncidentId>-A<nnn> | parent recordNo + -A<nnn> | u_mes_ehs_safetyIncident | 19 |
| 7 | u_mes_ehs_andonType | entity | master | ANT-<recordNo> | code | - | 13 |
| 8 | u_mes_ehs_incidentType | entity | master | ICT-<recordNo> | code | - | 11 |
| 9 | u_mes_ehs_energyType | entity | master | ENT-T-<recordNo> | code | - | 11 |
| 10 | u_mes_ehs_bodyPart | entity | master | BDP-<recordNo> | code | - | 9 |
| 11 | u_mes_ehs_injuryType | entity | master | INJ-<recordNo> | code | - | 9 |

## 5. Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 11 Oct 2026 | 104 collections registered (nested model), conventions, seed frame, first master IDs |
| 1.1 | 11 Oct 2026 | Key list added |
| 2.0 | 11 Oct 2026 | Requirements of 11 Oct applied: u_mes_<moduleCode>_<singular> names, flat documents, ID plus display pairs, recordNo, audit keys on transaction data only, status mapping collections; 104 concepts became 299 collections; operations 11 and items 12 documents confirmed; work centre spelling changed to workCenter |
| 2.2 | 11 Oct 2026 | Master data review: 41 master collections added (department, designation, employmentType and others), 67 text keys converted to master references, fixed enumerations mapped in u_mes_sys_enumerationValue; see 08_validation/reports/master_data_review.md |
| 2.1 | 11 Oct 2026 | Collection specifications written for all modules: field dictionary, validator, indexes and sample per collection under 03_design; check report in 08_validation/reports/specification_check.md |
