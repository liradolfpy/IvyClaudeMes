# data_model_register.md

MES on MongoDB - Front Brake Caliper Assembly LH - Pune
Register version: 2.9 | Date: 12 October 2026 | Database: mes | Model version 2.9 | 12 October 2026 | 369 collections (200 entity, 85 child, 76 relationship, 8 value-list), 8614 keys

This file is the single reference for collection names, identifiers and master IDs. It follows 00_governance/data_modeling_standard.md. Field-level detail: 02_architecture/collection_keys.md and 02_architecture/field_lists. Machine-readable copy: 05_generator/model/flat_model.json.

## 1. Conventions in force

- Collection name: `u_mes_<moduleCode>_<singularCollectionName>`, lower camelCase singular noun.
- Flat documents (DATA-001): no embedded documents, no arrays. A repeated value or association is a separate collection with one document per occurrence.
- `_id`: String of 16 digits, never ObjectId and never a UUID. `recordNo`: String, the business identifier, present in every collection.
- Reference: `<entity>Id` followed by `<entity>Name` (display value copied from the target). User references that record an action: `<action>ById` + `<action>By`.
- Polymorphic reference: `relatedCollectionName` + `relatedEntityId` + `relatedEntityName`.
- `siteId` + `siteName` in every collection except `u_mes_mast_site`.
- Classification values (DATA-003): a list the plant maintains is a master collection referenced by `<entity>Id` + `<entity>Name`; a list fixed by the application stays coded text with its values in `u_mes_syst_enumerationValue`.
- `status`: primary lifecycle state, only where the collection has one; values in 04_reference_data/code_lists/status_values.md.
- Audit keys `createdAt, createdById, createdBy, updatedAt, updatedById, updatedBy`: transaction collections only.
- `schemaVersion` (Int32) in every collection.
- Dates (DATA-004): every date and time is local plant time (IST) written with the +0000 suffix, without UTC conversion. Each date key is tagged Date (calendar date, stored as 00:00:00) or Datetime.
- Types (DATA-002): Date, Int32, Int64, Decimal128 for measurements and money, Double only for geoLatitude, geoLongitude, tagValue, powerFactor, Boolean, String.

## 2. Sample-data frame

| Item | Value |
|---|---|
| Enterprise | Varuna Brake Systems Pvt. Ltd. (fictional) |
| Site of all transactions | Chakan Plant, Pune (timezone Asia/Kolkata) |
| OEM customer | Sahyadri Motors Ltd. (fictional) |
| Sample period | April to September 2026; production fortnight Tue 15 Sep to Sat 26 Sep 2026 |
| Non-working days | Mon 14 Sep 2026 (Ganesh Chaturthi), Sun 20 Sep 2026 (weekly off) |
| Shifts | A 06:00-14:00, B 14:00-22:00, C 22:00-06:00 IST, stored as 06:00, 14:00, 22:00 with the +0000 suffix |
| Documents per collection | Exactly 10 |

## 3. Master ID registry

The registry of every _id, business number and display value in the sample data is 04_reference_data/sample_data_registry.md. It is generated together with the sample documents, so it always matches them. System IDs are 16-digit numeric strings: the first four digits are the collection number (1001 onwards, in inventory order), the last twelve are a running number.

## 4. Collection register


### mast - Master Data Management

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_mast_enterprise | entity | master | 16-digit numeric string | enterpriseCode | - | 27 |
| 2 | u_mes_mast_enterpriseContact | child | master | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_mast_enterprise | 13 |
| 3 | u_mes_mast_site | entity | master | 16-digit numeric string | siteCode | - | 31 |
| 4 | u_mes_mast_siteCertificate | child | master | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_mast_site | 13 |
| 5 | u_mes_mast_area | entity | master | 16-digit numeric string | areaCode | - | 21 |
| 6 | u_mes_mast_line | entity | master | 16-digit numeric string | lineCode | - | 23 |
| 7 | u_mes_mast_lineDefaultShift | relationship | master | 16-digit numeric string | parent recordNo + -DS<nnn> | u_mes_mast_line | 11 |
| 8 | u_mes_mast_lineIdealRate | child | master | 16-digit numeric string | parent recordNo + -IR<nnn> | u_mes_mast_line | 13 |
| 9 | u_mes_mast_workCenter | entity | master | 16-digit numeric string | workCentreCode | - | 25 |
| 10 | u_mes_mast_workCenterEquipment | relationship | master | 16-digit numeric string | parent recordNo + -E<nnn> | u_mes_mast_workCenter | 11 |
| 11 | u_mes_mast_workCenterOperation | relationship | master | 16-digit numeric string | parent recordNo + -O<nnn> | u_mes_mast_workCenter | 11 |
| 12 | u_mes_mast_workCenterRequiresSkill | relationship | master | 16-digit numeric string | parent recordNo + -RS<nnn> | u_mes_mast_workCenter | 11 |
| 13 | u_mes_mast_equipment | entity | master | 16-digit numeric string | equipmentCode | - | 54 |
| 14 | u_mes_mast_equipmentIotDevice | relationship | master | 16-digit numeric string | parent recordNo + -ID<nnn> | u_mes_mast_equipment | 11 |
| 15 | u_mes_mast_shift | entity | master | 16-digit numeric string | shiftCode | - | 15 |
| 16 | u_mes_mast_shiftBreak | child | master | 16-digit numeric string | parent recordNo + -B<nnn> | u_mes_mast_shift | 13 |
| 17 | u_mes_mast_shiftWorkingDay | valueList | master | 16-digit numeric string | parent recordNo + -WD<nnn> | u_mes_mast_shift | 10 |
| 18 | u_mes_mast_workCalendar | entity | master | 16-digit numeric string | calendarCode | - | 12 |
| 19 | u_mes_mast_workCalendarLine | relationship | master | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_mast_workCalendar | 11 |
| 20 | u_mes_mast_workCalendarShift | relationship | master | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_mast_workCalendar | 11 |
| 21 | u_mes_mast_workCalendarWeeklyOffDay | valueList | master | 16-digit numeric string | parent recordNo + -WOD<nnn> | u_mes_mast_workCalendar | 10 |
| 22 | u_mes_mast_workCalendarException | child | master | 16-digit numeric string | parent recordNo + -E<nnn> | u_mes_mast_workCalendar | 13 |
| 23 | u_mes_mast_workCalendarExceptionShift | relationship | master | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_mast_workCalendarException | 11 |
| 24 | u_mes_mast_shiftRoster | entity | transaction | 16-digit numeric string | rosterNo | - | 26 |
| 25 | u_mes_mast_shiftRosterAssignment | child | transaction | 16-digit numeric string | parent recordNo + -A<nnn> | u_mes_mast_shiftRoster | 27 |
| 26 | u_mes_mast_role | entity | master | 16-digit numeric string | roleCode | - | 13 |
| 27 | u_mes_mast_rolePermission | relationship | master | 16-digit numeric string | parent recordNo + -P<nnn> | u_mes_mast_role | 11 |
| 28 | u_mes_mast_roleSignatureMeaning | relationship | master | 16-digit numeric string | parent recordNo + -SM<nnn> | u_mes_mast_role | 11 |
| 29 | u_mes_mast_user | entity | master | 16-digit numeric string | employeeNo | - | 36 |
| 30 | u_mes_mast_userRole | relationship | master | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_mast_user | 11 |
| 31 | u_mes_mast_skill | entity | master | 16-digit numeric string | skillCode | - | 17 |
| 32 | u_mes_mast_skillOperation | relationship | master | 16-digit numeric string | parent recordNo + -O<nnn> | u_mes_mast_skill | 11 |
| 33 | u_mes_mast_skillLevelScale | child | master | 16-digit numeric string | parent recordNo + -LS<nnn> | u_mes_mast_skill | 11 |
| 34 | u_mes_mast_skillCertification | entity | transaction | 16-digit numeric string | certificationNo | - | 35 |
| 35 | u_mes_mast_customer | entity | master | 16-digit numeric string | customerCode | - | 27 |
| 36 | u_mes_mast_customerShipTo | child | master | 16-digit numeric string | parent recordNo + -ST<nnn> | u_mes_mast_customer | 17 |
| 37 | u_mes_mast_customerContact | child | master | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_mast_customer | 13 |
| 38 | u_mes_mast_supplier | entity | master | 16-digit numeric string | supplierCode | - | 27 |
| 39 | u_mes_mast_supplierContact | child | master | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_mast_supplier | 13 |
| 40 | u_mes_mast_supplierCertificate | child | master | 16-digit numeric string | parent recordNo + -C2<nnn> | u_mes_mast_supplier | 12 |
| 41 | u_mes_mast_supplierSuppliedItem | relationship | master | 16-digit numeric string | parent recordNo + -SI<nnn> | u_mes_mast_supplier | 13 |
| 42 | u_mes_mast_unitOfMeasure | entity | master | 16-digit numeric string | uomCode | - | 18 |
| 43 | u_mes_mast_department | entity | master | 16-digit numeric string | code | - | 16 |
| 44 | u_mes_mast_designation | entity | master | 16-digit numeric string | code | - | 14 |
| 45 | u_mes_mast_employmentType | entity | master | 16-digit numeric string | code | - | 11 |
| 46 | u_mes_mast_costCenter | entity | master | 16-digit numeric string | code | - | 12 |
| 47 | u_mes_mast_manufacturer | entity | master | 16-digit numeric string | code | - | 13 |
| 48 | u_mes_mast_equipmentType | entity | master | 16-digit numeric string | code | - | 10 |
| 49 | u_mes_mast_skillCategory | entity | master | 16-digit numeric string | code | - | 10 |
| 50 | u_mes_mast_permission | entity | master | 16-digit numeric string | code | - | 12 |
| 51 | u_mes_mast_signatureMeaning | entity | master | 16-digit numeric string | code | - | 10 |
| 52 | u_mes_mast_currency | entity | master | 16-digit numeric string | code | - | 12 |
| 53 | u_mes_mast_country | entity | master | 16-digit numeric string | code | - | 11 |
| 54 | u_mes_mast_language | entity | master | 16-digit numeric string | code | - | 10 |
| 55 | u_mes_mast_transporter | entity | master | 16-digit numeric string | code | - | 12 |
| 56 | u_mes_mast_commodity | entity | master | 16-digit numeric string | code | - | 10 |
| 57 | u_mes_mast_roleRequiredSkill | relationship | master | 16-digit numeric string | parent recordNo + -RS<nnn> | u_mes_mast_role | 12 |

### prod - Product Definition

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_prod_item | entity | master | 16-digit numeric string | itemNo | - | 39 |
| 2 | u_mes_prod_itemRevision | child | master | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_prod_item | 14 |
| 3 | u_mes_prod_itemCustomerPart | child | master | 16-digit numeric string | parent recordNo + -CP<nnn> | u_mes_prod_item | 13 |
| 4 | u_mes_prod_productVariant | entity | master | 16-digit numeric string | variantCode | - | 29 |
| 5 | u_mes_prod_billOfMaterial | entity | master | 16-digit numeric string | bomNo | - | 23 |
| 6 | u_mes_prod_billOfMaterialComponent | child | master | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_prod_billOfMaterial | 21 |
| 7 | u_mes_prod_billOfMaterialComponentProductVariant | relationship | master | 16-digit numeric string | parent recordNo + -PV<nnn> | u_mes_prod_billOfMaterialComponent | 11 |
| 8 | u_mes_prod_billOfMaterialComponentAlternateItem | relationship | master | 16-digit numeric string | parent recordNo + -AI<nnn> | u_mes_prod_billOfMaterialComponent | 11 |
| 9 | u_mes_prod_operation | entity | master | 16-digit numeric string | operationCode | - | 22 |
| 10 | u_mes_prod_operationRequiredSkill | relationship | master | 16-digit numeric string | parent recordNo + -RS<nnn> | u_mes_prod_operation | 11 |
| 11 | u_mes_prod_routing | entity | master | 16-digit numeric string | routingNo | - | 24 |
| 12 | u_mes_prod_routingStep | child | master | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_prod_routing | 20 |
| 13 | u_mes_prod_routingStepAlternateWorkCenter | relationship | master | 16-digit numeric string | parent recordNo + -AWC<nnn> | u_mes_prod_routingStep | 11 |
| 14 | u_mes_prod_routingStepNextStep | child | master | 16-digit numeric string | parent recordNo + -NS<nnn> | u_mes_prod_routingStep | 10 |
| 15 | u_mes_prod_billOfProcess | entity | master | 16-digit numeric string | bopNo | - | 20 |
| 16 | u_mes_prod_billOfProcessStep | child | master | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_prod_billOfProcess | 19 |
| 17 | u_mes_prod_billOfProcessStepEquipment | relationship | master | 16-digit numeric string | parent recordNo + -E<nnn> | u_mes_prod_billOfProcessStep | 11 |
| 18 | u_mes_prod_billOfProcessStepTool | relationship | master | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_prod_billOfProcessStep | 11 |
| 19 | u_mes_prod_billOfProcessStepRequiredSkill | relationship | master | 16-digit numeric string | parent recordNo + -RS<nnn> | u_mes_prod_billOfProcessStep | 11 |
| 20 | u_mes_prod_billOfProcessStepConsumedComponent | child | master | 16-digit numeric string | parent recordNo + -CC<nnn> | u_mes_prod_billOfProcessStep | 13 |
| 21 | u_mes_prod_billOfProcessStepInterlock | child | master | 16-digit numeric string | parent recordNo + -I<nnn> | u_mes_prod_billOfProcessStep | 12 |
| 22 | u_mes_prod_billOfProcessStepProcessParameter | child | master | 16-digit numeric string | parent recordNo + -PP<nnn> | u_mes_prod_billOfProcessStep | 15 |
| 23 | u_mes_prod_workInstruction | entity | master | 16-digit numeric string | instructionNo | - | 30 |
| 24 | u_mes_prod_workInstructionStep | child | master | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_prod_workInstruction | 22 |
| 25 | u_mes_prod_workInstructionStepMediaControlledDocument | relationship | master | 16-digit numeric string | parent recordNo + -MCD<nnn> | u_mes_prod_workInstructionStep | 11 |
| 26 | u_mes_prod_workInstructionStepProductVariant | relationship | master | 16-digit numeric string | parent recordNo + -PV<nnn> | u_mes_prod_workInstructionStep | 11 |
| 27 | u_mes_prod_workInstructionStepTool | relationship | master | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_prod_workInstructionStep | 11 |
| 28 | u_mes_prod_workInstructionStepCharacteristic | relationship | master | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_prod_workInstructionStep | 11 |
| 29 | u_mes_prod_workInstructionPpeItem | relationship | master | 16-digit numeric string | parent recordNo + -PI<nnn> | u_mes_prod_workInstruction | 11 |
| 30 | u_mes_prod_workInstructionKeyPoint | valueList | master | 16-digit numeric string | parent recordNo + -KP<nnn> | u_mes_prod_workInstruction | 10 |
| 31 | u_mes_prod_recipe | entity | master | 16-digit numeric string | recipeNo | - | 37 |
| 32 | u_mes_prod_recipeParameter | child | master | 16-digit numeric string | parent recordNo + -P<nnn> | u_mes_prod_recipe | 19 |
| 33 | u_mes_prod_recipeStage | child | master | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_prod_recipe | 12 |
| 34 | u_mes_prod_engineeringChange | entity | transaction | 16-digit numeric string | ecnNo | - | 37 |
| 35 | u_mes_prod_engineeringChangeAffectedItem | child | transaction | 16-digit numeric string | parent recordNo + -AI<nnn> | u_mes_prod_engineeringChange | 19 |
| 36 | u_mes_prod_engineeringChangeAffectedObject | child | transaction | 16-digit numeric string | parent recordNo + -AO<nnn> | u_mes_prod_engineeringChange | 19 |
| 37 | u_mes_prod_engineeringChangeApproval | child | transaction | 16-digit numeric string | parent recordNo + -A<nnn> | u_mes_prod_engineeringChange | 21 |
| 38 | u_mes_prod_engineeringChangeControlledDocument | relationship | transaction | 16-digit numeric string | parent recordNo + -CD<nnn> | u_mes_prod_engineeringChange | 17 |
| 39 | u_mes_prod_itemGroup | entity | master | 16-digit numeric string | code | - | 10 |
| 40 | u_mes_prod_itemFamily | entity | master | 16-digit numeric string | code | - | 10 |
| 41 | u_mes_prod_ppeItem | entity | master | 16-digit numeric string | code | - | 10 |
| 42 | u_mes_prod_market | entity | master | 16-digit numeric string | code | - | 10 |
| 43 | u_mes_prod_padCompound | entity | master | 16-digit numeric string | code | - | 10 |
| 44 | u_mes_prod_surfaceFinish | entity | master | 16-digit numeric string | code | - | 10 |
| 45 | u_mes_prod_vehicleModel | entity | master | 16-digit numeric string | code | - | 14 |
| 46 | u_mes_prod_recipeProductVariant | relationship | master | 16-digit numeric string | parent recordNo + -PV<nnn> | u_mes_prod_recipe | 11 |
| 47 | u_mes_prod_recipeControlledDocument | relationship | master | 16-digit numeric string | parent recordNo + -CD<nnn> | u_mes_prod_recipe | 12 |
| 48 | u_mes_prod_workInstructionWorkCenter | relationship | master | 16-digit numeric string | parent recordNo + -WC<nnn> | u_mes_prod_workInstruction | 11 |
| 49 | u_mes_prod_workInstructionProductVariant | relationship | master | 16-digit numeric string | parent recordNo + -PV<nnn> | u_mes_prod_workInstruction | 11 |

### plan - Planning and Execution

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_plan_customerSchedule | entity | transaction | 16-digit numeric string | releaseNo | - | 24 |
| 2 | u_mes_plan_customerScheduleLine | child | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_plan_customerSchedule | 24 |
| 3 | u_mes_plan_productionOrder | entity | transaction | 16-digit numeric string | orderNo | - | 59 |
| 4 | u_mes_plan_productionOrderRelease | child | transaction | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_plan_productionOrder | 19 |
| 5 | u_mes_plan_productionOrderLot | relationship | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_plan_productionOrder | 17 |
| 6 | u_mes_plan_productionSchedule | entity | transaction | 16-digit numeric string | scheduleNo | - | 28 |
| 7 | u_mes_plan_productionScheduleSlot | child | transaction | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_plan_productionSchedule | 24 |
| 8 | u_mes_plan_dispatchList | entity | transaction | 16-digit numeric string | dispatchNo | - | 23 |
| 9 | u_mes_plan_dispatchListEntry | child | transaction | 16-digit numeric string | parent recordNo + -E<nnn> | u_mes_plan_dispatchList | 29 |
| 10 | u_mes_plan_operationExecution | entity | transaction | 16-digit numeric string | executionNo | - | 71 |
| 11 | u_mes_plan_operationExecutionDefectCode | relationship | transaction | 16-digit numeric string | parent recordNo + -DC<nnn> | u_mes_plan_operationExecution | 17 |
| 12 | u_mes_plan_operationExecutionTool | relationship | transaction | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_plan_operationExecution | 17 |
| 13 | u_mes_plan_stepCompletion | entity | transaction | 16-digit numeric string | completionNo | - | 44 |
| 14 | u_mes_plan_wipUnit | entity | transaction | 16-digit numeric string | unitNo | - | 48 |
| 15 | u_mes_plan_wipUnitCompletedStep | valueList | transaction | 16-digit numeric string | parent recordNo + -CS<nnn> | u_mes_plan_wipUnit | 16 |
| 16 | u_mes_plan_lot | entity | transaction | 16-digit numeric string | lotNo | - | 51 |
| 17 | u_mes_plan_lotParentLot | relationship | transaction | 16-digit numeric string | parent recordNo + -PL<nnn> | u_mes_plan_lot | 17 |
| 18 | u_mes_plan_lotAttributesCavityNo | valueList | transaction | 16-digit numeric string | parent recordNo + -ACN<nnn> | u_mes_plan_lot | 16 |
| 19 | u_mes_plan_container | entity | transaction | 16-digit numeric string | containerNo | - | 40 |
| 20 | u_mes_plan_containerLot | relationship | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_plan_container | 17 |
| 21 | u_mes_plan_labourBooking | entity | transaction | 16-digit numeric string | bookingNo | - | 43 |
| 22 | u_mes_plan_changeover | entity | transaction | 16-digit numeric string | changeoverNo | - | 41 |
| 23 | u_mes_plan_changeoverStep | child | transaction | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_plan_changeover | 20 |
| 24 | u_mes_plan_changeoverRemovedTool | relationship | transaction | 16-digit numeric string | parent recordNo + -RT<nnn> | u_mes_plan_changeover | 17 |
| 25 | u_mes_plan_changeoverInstalledTool | relationship | transaction | 16-digit numeric string | parent recordNo + -IT<nnn> | u_mes_plan_changeover | 17 |
| 26 | u_mes_plan_changeoverPerformedByUser | relationship | transaction | 16-digit numeric string | parent recordNo + -PBU<nnn> | u_mes_plan_changeover | 17 |
| 27 | u_mes_plan_shiftHandover | entity | transaction | 16-digit numeric string | handoverNo | - | 33 |
| 28 | u_mes_plan_shiftHandoverProductionOrder | relationship | transaction | 16-digit numeric string | parent recordNo + -PO<nnn> | u_mes_plan_shiftHandover | 17 |
| 29 | u_mes_plan_shiftHandoverDowntimeEvent | relationship | transaction | 16-digit numeric string | parent recordNo + -DE<nnn> | u_mes_plan_shiftHandover | 17 |
| 30 | u_mes_plan_shiftHandoverNonconformance | relationship | transaction | 16-digit numeric string | parent recordNo + -N<nnn> | u_mes_plan_shiftHandover | 17 |
| 31 | u_mes_plan_shiftHandoverOpenItem | child | transaction | 16-digit numeric string | parent recordNo + -OI<nnn> | u_mes_plan_shiftHandover | 20 |
| 32 | u_mes_plan_andonEvent | entity | transaction | 16-digit numeric string | andonNo | - | 46 |
| 33 | u_mes_plan_andonEventEscalation | child | transaction | 16-digit numeric string | parent recordNo + -E<nnn> | u_mes_plan_andonEvent | 20 |
| 34 | u_mes_plan_indirectActivity | entity | master | 16-digit numeric string | code | - | 13 |
| 35 | u_mes_plan_containerType | entity | master | 16-digit numeric string | code | - | 15 |
| 36 | u_mes_plan_andonType | entity | master | 16-digit numeric string | code | - | 17 |
| 37 | u_mes_plan_operatorSession | entity | transaction | 16-digit numeric string | OSN-<yyyymmdd>-<nnnnn>, e.g. OSN-20260916-00042 | - | 33 |
| 38 | u_mes_plan_documentAcknowledgement | entity | transaction | 16-digit numeric string | ACK-<yyyymmdd>-<nnnnn> | - | 34 |
| 39 | u_mes_plan_interlockEvent | entity | transaction | 16-digit numeric string | ILK-<yyyymmdd>-<nnnnn> | - | 51 |
| 40 | u_mes_plan_recipeDownload | entity | transaction | 16-digit numeric string | RDL-<yyyymmdd>-<nnnnn> | - | 34 |
| 41 | u_mes_plan_setupVerification | entity | transaction | 16-digit numeric string | SUV-<yyyymmdd>-<nnnnn> | - | 33 |
| 42 | u_mes_plan_setupVerificationItem | child | transaction | 16-digit numeric string | parent recordNo + -I<nnn> | u_mes_plan_setupVerification | 26 |
| 43 | u_mes_plan_lineClearance | entity | transaction | 16-digit numeric string | LCL-<yyyymmdd>-<nnn>, e.g. LCL-20260915-001 | - | 40 |

### matl - Material Management

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_matl_storageLocation | entity | master | 16-digit numeric string | locationCode | - | 25 |
| 2 | u_mes_matl_inventoryBalance | entity | transaction | 16-digit numeric string | inventoryNo | - | 34 |
| 3 | u_mes_matl_materialMovement | entity | transaction | 16-digit numeric string | movementNo | - | 49 |
| 4 | u_mes_matl_goodsReceipt | entity | transaction | 16-digit numeric string | grnNo | - | 26 |
| 5 | u_mes_matl_goodsReceiptLine | child | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_matl_goodsReceipt | 30 |
| 6 | u_mes_matl_goodsReceiptLineInspectionResult | relationship | transaction | 16-digit numeric string | parent recordNo + -IR<nnn> | u_mes_matl_goodsReceiptLine | 17 |
| 7 | u_mes_matl_kit | entity | transaction | 16-digit numeric string | kitNo | - | 29 |
| 8 | u_mes_matl_kitLine | child | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_matl_kit | 30 |
| 9 | u_mes_matl_materialRequest | entity | transaction | 16-digit numeric string | requestNo | - | 42 |
| 10 | u_mes_matl_materialConsumption | entity | transaction | 16-digit numeric string | consumptionNo | - | 44 |
| 11 | u_mes_matl_packagingSpecification | entity | master | 16-digit numeric string | packSpecNo | - | 29 |
| 12 | u_mes_matl_packagingSpecificationLevel | child | master | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_matl_packagingSpecification | 15 |
| 13 | u_mes_matl_labelTemplate | entity | master | 16-digit numeric string | templateCode | - | 20 |
| 14 | u_mes_matl_labelTemplateField | child | master | 16-digit numeric string | parent recordNo + -F<nnn> | u_mes_matl_labelTemplate | 15 |
| 15 | u_mes_matl_label | entity | transaction | 16-digit numeric string | labelNo | - | 42 |
| 16 | u_mes_matl_shipment | entity | transaction | 16-digit numeric string | shipmentNo | - | 40 |
| 17 | u_mes_matl_shipmentLine | child | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_matl_shipment | 19 |
| 18 | u_mes_matl_shipmentLineContainer | relationship | transaction | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_matl_shipmentLine | 17 |
| 19 | u_mes_matl_shipmentLineLot | relationship | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_matl_shipmentLine | 17 |
| 20 | u_mes_matl_movementType | entity | master | 16-digit numeric string | code | - | 13 |
| 21 | u_mes_matl_stockStatus | entity | master | 16-digit numeric string | code | - | 12 |
| 22 | u_mes_matl_packType | entity | master | 16-digit numeric string | code | - | 10 |
| 23 | u_mes_matl_exposureTimer | entity | transaction | 16-digit numeric string | EXT-<yyyymmdd>-<nnnnn> | - | 32 |
| 24 | u_mes_matl_replenishmentRule | entity | master | 16-digit numeric string | RPL-<item code>-<location code>, e.g. RPL-PST-54-LS-OP060 | - | 28 |
| 25 | u_mes_matl_materialDemandForecast | entity | transaction | 16-digit numeric string | MDF-<yyyymmdd>-<line code>-<item code>-<hh> | - | 31 |
| 26 | u_mes_matl_storageLocationAllowedItem | relationship | master | 16-digit numeric string | parent recordNo + -AI<nnn> | u_mes_matl_storageLocation | 13 |
| 27 | u_mes_matl_dispenseRecord | entity | transaction | 16-digit numeric string | DSP-<yyyymmdd>-<nnnn>, e.g. DSP-20260915-0031 | - | 42 |

### trac - Traceability

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_trac_serialNumber | entity | transaction | 16-digit numeric string | serialNo | - | 44 |
| 2 | u_mes_trac_genealogyLink | entity | transaction | 16-digit numeric string | linkNo | - | 44 |
| 3 | u_mes_trac_componentLotLink | entity | transaction | 16-digit numeric string | lotLinkNo | - | 33 |
| 4 | u_mes_trac_asBuiltRecord | entity | transaction | 16-digit numeric string | recordNo | - | 54 |
| 5 | u_mes_trac_asBuiltRecordComponent | child | transaction | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_trac_asBuiltRecord | 23 |
| 6 | u_mes_trac_asBuiltRecordOperation | child | transaction | 16-digit numeric string | parent recordNo + -O<nnn> | u_mes_trac_asBuiltRecord | 29 |
| 7 | u_mes_trac_asBuiltRecordInspectionResult | relationship | transaction | 16-digit numeric string | parent recordNo + -IR<nnn> | u_mes_trac_asBuiltRecord | 17 |
| 8 | u_mes_trac_traceInvestigation | entity | transaction | 16-digit numeric string | TRC-<yyyymmdd>-<nnn> | - | 33 |
| 9 | u_mes_trac_traceInvestigationResult | child | transaction | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_trac_traceInvestigation | 29 |

### qual - Quality Management

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_qual_characteristic | entity | master | 16-digit numeric string | characteristicCode | - | 34 |
| 2 | u_mes_qual_controlPlan | entity | master | 16-digit numeric string | controlPlanNo | - | 27 |
| 3 | u_mes_qual_controlPlanCoreTeamUser | relationship | master | 16-digit numeric string | parent recordNo + -CTU<nnn> | u_mes_qual_controlPlan | 11 |
| 4 | u_mes_qual_controlPlanLine | child | master | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_qual_controlPlan | 25 |
| 5 | u_mes_qual_inspectionPlan | entity | master | 16-digit numeric string | inspectionPlanNo | - | 28 |
| 6 | u_mes_qual_inspectionPlanLine | child | master | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_qual_inspectionPlan | 21 |
| 7 | u_mes_qual_samplingPlan | entity | master | 16-digit numeric string | samplingPlanCode | - | 19 |
| 8 | u_mes_qual_samplingPlanSizeRow | child | master | 16-digit numeric string | parent recordNo + -SR<nnn> | u_mes_qual_samplingPlan | 14 |
| 9 | u_mes_qual_checkSheet | entity | master | 16-digit numeric string | checkSheetCode | - | 25 |
| 10 | u_mes_qual_checkSheetItem | child | master | 16-digit numeric string | parent recordNo + -I<nnn> | u_mes_qual_checkSheet | 17 |
| 11 | u_mes_qual_checkSheetResult | entity | transaction | 16-digit numeric string | checkResultNo | - | 37 |
| 12 | u_mes_qual_checkSheetResultAnswer | child | transaction | 16-digit numeric string | parent recordNo + -A<nnn> | u_mes_qual_checkSheetResult | 19 |
| 13 | u_mes_qual_inspectionResult | entity | transaction | 16-digit numeric string | resultNo | - | 66 |
| 14 | u_mes_qual_spcChart | entity | master | 16-digit numeric string | chartNo | - | 30 |
| 15 | u_mes_qual_spcChartControlLimit | child | master | 16-digit numeric string | parent recordNo + -CL<nnn> | u_mes_qual_spcChart | 17 |
| 16 | u_mes_qual_spcChartRule | valueList | master | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_qual_spcChart | 10 |
| 17 | u_mes_qual_spcSample | entity | transaction | 16-digit numeric string | sampleNo | - | 42 |
| 18 | u_mes_qual_spcSampleReading | valueList | transaction | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_qual_spcSample | 16 |
| 19 | u_mes_qual_spcSampleInspectionResult | relationship | transaction | 16-digit numeric string | parent recordNo + -IR<nnn> | u_mes_qual_spcSample | 17 |
| 20 | u_mes_qual_spcSampleViolation | child | transaction | 16-digit numeric string | parent recordNo + -V<nnn> | u_mes_qual_spcSample | 17 |
| 21 | u_mes_qual_defectCode | entity | master | 16-digit numeric string | defectCode | - | 22 |
| 22 | u_mes_qual_defectCodeApplicableOperation | relationship | master | 16-digit numeric string | parent recordNo + -AO<nnn> | u_mes_qual_defectCode | 11 |
| 23 | u_mes_qual_nonconformance | entity | transaction | 16-digit numeric string | ncrNo | - | 54 |
| 24 | u_mes_qual_nonconformanceAffectedObject | child | transaction | 16-digit numeric string | parent recordNo + -AO<nnn> | u_mes_qual_nonconformance | 24 |
| 25 | u_mes_qual_nonconformanceContainmentAction | child | transaction | 16-digit numeric string | parent recordNo + -CA<nnn> | u_mes_qual_nonconformance | 19 |
| 26 | u_mes_qual_nonconformanceInspectionResult | relationship | transaction | 16-digit numeric string | parent recordNo + -IR<nnn> | u_mes_qual_nonconformance | 17 |
| 27 | u_mes_qual_nonconformanceReworkOrder | relationship | transaction | 16-digit numeric string | parent recordNo + -RO<nnn> | u_mes_qual_nonconformance | 17 |
| 28 | u_mes_qual_nonconformanceScrapRecord | relationship | transaction | 16-digit numeric string | parent recordNo + -SR<nnn> | u_mes_qual_nonconformance | 17 |
| 29 | u_mes_qual_nonconformancePhotoControlledDocument | relationship | transaction | 16-digit numeric string | parent recordNo + -PCD<nnn> | u_mes_qual_nonconformance | 17 |
| 30 | u_mes_qual_nonconformanceMrbUser | relationship | transaction | 16-digit numeric string | parent recordNo + -MU<nnn> | u_mes_qual_nonconformance | 17 |
| 31 | u_mes_qual_reworkOrder | entity | transaction | 16-digit numeric string | reworkNo | - | 45 |
| 32 | u_mes_qual_reworkOrderWipUnit | relationship | transaction | 16-digit numeric string | parent recordNo + -WU<nnn> | u_mes_qual_reworkOrder | 17 |
| 33 | u_mes_qual_reworkOrderStep | child | transaction | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_qual_reworkOrder | 21 |
| 34 | u_mes_qual_scrapRecord | entity | transaction | 16-digit numeric string | scrapNo | - | 51 |
| 35 | u_mes_qual_qualityHold | entity | transaction | 16-digit numeric string | holdNo | - | 38 |
| 36 | u_mes_qual_qualityHoldHeldObject | child | transaction | 16-digit numeric string | parent recordNo + -HO<nnn> | u_mes_qual_qualityHold | 21 |
| 37 | u_mes_qual_deviationPermit | entity | transaction | 16-digit numeric string | deviationNo | - | 39 |
| 38 | u_mes_qual_deviationPermitApproval | child | transaction | 16-digit numeric string | parent recordNo + -A<nnn> | u_mes_qual_deviationPermit | 20 |
| 39 | u_mes_qual_capa | entity | transaction | 16-digit numeric string | capaNo | - | 43 |
| 40 | u_mes_qual_capaNonconformance | relationship | transaction | 16-digit numeric string | parent recordNo + -N<nnn> | u_mes_qual_capa | 17 |
| 41 | u_mes_qual_capaTeamMember | child | transaction | 16-digit numeric string | parent recordNo + -TM<nnn> | u_mes_qual_capa | 18 |
| 42 | u_mes_qual_capaContainmentAction | child | transaction | 16-digit numeric string | parent recordNo + -CA<nnn> | u_mes_qual_capa | 19 |
| 43 | u_mes_qual_capaCorrectiveAction | child | transaction | 16-digit numeric string | parent recordNo + -CA2<nnn> | u_mes_qual_capa | 19 |
| 44 | u_mes_qual_capaImplementationAction | child | transaction | 16-digit numeric string | parent recordNo + -IA<nnn> | u_mes_qual_capa | 20 |
| 45 | u_mes_qual_capaControlledDocument | relationship | transaction | 16-digit numeric string | parent recordNo + -CD<nnn> | u_mes_qual_capa | 17 |
| 46 | u_mes_qual_pfmea | entity | master | 16-digit numeric string | pfmeaNo | - | 20 |
| 47 | u_mes_qual_pfmeaCoreTeamUser | relationship | master | 16-digit numeric string | parent recordNo + -CTU<nnn> | u_mes_qual_pfmea | 11 |
| 48 | u_mes_qual_pfmeaLine | child | master | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_qual_pfmea | 33 |
| 49 | u_mes_qual_ppapSubmission | entity | transaction | 16-digit numeric string | ppapNo | - | 36 |
| 50 | u_mes_qual_ppapSubmissionElement | child | transaction | 16-digit numeric string | parent recordNo + -E<nnn> | u_mes_qual_ppapSubmission | 20 |
| 51 | u_mes_qual_ppapSubmissionMsaStudy | relationship | transaction | 16-digit numeric string | parent recordNo + -MS<nnn> | u_mes_qual_ppapSubmission | 17 |
| 52 | u_mes_qual_gauge | entity | master | 16-digit numeric string | gaugeNo | - | 40 |
| 53 | u_mes_qual_gaugeCalibration | entity | transaction | 16-digit numeric string | calibrationNo | - | 36 |
| 54 | u_mes_qual_gaugeCalibrationReading | child | transaction | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_qual_gaugeCalibration | 20 |
| 55 | u_mes_qual_msaStudy | entity | transaction | 16-digit numeric string | msaNo | - | 42 |
| 56 | u_mes_qual_msaStudyAppraiserUser | relationship | transaction | 16-digit numeric string | parent recordNo + -AU<nnn> | u_mes_qual_msaStudy | 17 |
| 57 | u_mes_qual_msaStudyTrial | child | transaction | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_qual_msaStudy | 19 |
| 58 | u_mes_qual_audit | entity | transaction | 16-digit numeric string | auditNo | - | 45 |
| 59 | u_mes_qual_auditAuditorUser | relationship | transaction | 16-digit numeric string | parent recordNo + -AU<nnn> | u_mes_qual_audit | 17 |
| 60 | u_mes_qual_auditFinding | child | transaction | 16-digit numeric string | parent recordNo + -F<nnn> | u_mes_qual_audit | 24 |
| 61 | u_mes_qual_customerComplaint | entity | transaction | 16-digit numeric string | complaintNo | - | 44 |
| 62 | u_mes_qual_customerComplaintSerialNumber | relationship | transaction | 16-digit numeric string | parent recordNo + -SN<nnn> | u_mes_qual_customerComplaint | 17 |
| 63 | u_mes_qual_customerComplaintShipment | relationship | transaction | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_qual_customerComplaint | 17 |
| 64 | u_mes_qual_customerComplaintSuspectLot | relationship | transaction | 16-digit numeric string | parent recordNo + -SL<nnn> | u_mes_qual_customerComplaint | 17 |
| 65 | u_mes_qual_customerComplaintCommunication | child | transaction | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_qual_customerComplaint | 20 |
| 66 | u_mes_qual_defectGroup | entity | master | 16-digit numeric string | code | - | 10 |
| 67 | u_mes_qual_gaugeType | entity | master | 16-digit numeric string | code | - | 10 |
| 68 | u_mes_qual_dispositionType | entity | master | 16-digit numeric string | code | - | 13 |
| 69 | u_mes_qual_complaintType | entity | master | 16-digit numeric string | code | - | 10 |
| 70 | u_mes_qual_characteristicPosition | child | master | 16-digit numeric string | parent recordNo + -P<nnn> | u_mes_qual_characteristic | 17 |
| 71 | u_mes_qual_curveEnvelope | entity | master | 16-digit numeric string | ENV-<characteristic code>-<version>, e.g. ENV-OP060-PISTON-PRESS-02 | - | 32 |
| 72 | u_mes_qual_curveEnvelopeWindow | child | master | 16-digit numeric string | parent recordNo + -W<nnn> | u_mes_qual_curveEnvelope | 16 |
| 73 | u_mes_qual_measurementCurve | entity | transaction | 16-digit numeric string | CRV-<yyyymmdd>-<nnnnnn> | - | 39 |
| 74 | u_mes_qual_measurementCurvePoint | entity | transaction | 16-digit numeric string | parent curve recordNo + -<nnnn> | - | 18 |
| 75 | u_mes_qual_defectRecord | entity | transaction | 16-digit numeric string | DEF-<yyyymmdd>-<nnnnn> | - | 62 |
| 76 | u_mes_qual_auditSchedule | entity | master | 16-digit numeric string | LPA-<layer>-<line code>-<nn>, e.g. LPA-L2-LN-CAL-01 | - | 30 |
| 77 | u_mes_qual_inspectionPlanProductVariant | relationship | master | 16-digit numeric string | parent recordNo + -PV<nnn> | u_mes_qual_inspectionPlan | 11 |
| 78 | u_mes_qual_environmentalMonitoringPoint | entity | master | 16-digit numeric string | EMP-<area code>-<nn>, e.g. EMP-ASY-01 | - | 21 |
| 79 | u_mes_qual_environmentalMonitoringResult | entity | transaction | 16-digit numeric string | EMR-<yyyymmdd>-<nnnn>, e.g. EMR-20260915-0012 | - | 25 |
| 80 | u_mes_qual_retentionSample | entity | transaction | 16-digit numeric string | RSM-<lot number>-<nn>, e.g. RSM-L260915-GDC-014-01 | - | 35 |
| 81 | u_mes_qual_riskAssessment | entity | transaction | 16-digit numeric string | QRA-<yyyy>-<nnn>, e.g. QRA-2026-031 | - | 29 |
| 82 | u_mes_qual_productQualityReview | entity | transaction | 16-digit numeric string | PQR-<item>-<yyyy>-<period>, e.g. PQR-5110-10-0100-2026-H1 | - | 34 |
| 83 | u_mes_qual_productRecall | entity | transaction | 16-digit numeric string | RCL-<yyyy>-<nnn>, e.g. RCL-2026-003 | - | 38 |
| 84 | u_mes_qual_productRecallLot | child | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_qual_productRecall | 21 |
| 85 | u_mes_qual_processValidation | entity | transaction | 16-digit numeric string | PVL-<yyyy>-<nnn>, e.g. PVL-2026-007 | - | 35 |

### perf - Performance Management

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_perf_reasonCode | entity | master | 16-digit numeric string | reasonCode | - | 24 |
| 2 | u_mes_perf_equipmentState | entity | transaction | 16-digit numeric string | stateEventNo | - | 31 |
| 3 | u_mes_perf_downtimeEvent | entity | transaction | 16-digit numeric string | downtimeNo | - | 55 |
| 4 | u_mes_perf_downtimeEventComment | child | transaction | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_perf_downtimeEvent | 19 |
| 5 | u_mes_perf_productionCount | entity | transaction | 16-digit numeric string | countNo | - | 35 |
| 6 | u_mes_perf_oeeRecord | entity | transaction | 16-digit numeric string | oeeRecordNo | - | 43 |
| 7 | u_mes_perf_oeeRecordLoss | child | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_perf_oeeRecord | 21 |
| 8 | u_mes_perf_processTag | entity | master | 16-digit numeric string | tagName | - | 35 |
| 9 | u_mes_perf_processReading | entity | transaction | 16-digit numeric string | readingNo | - | 30 |
| 10 | u_mes_perf_alarm | entity | transaction | 16-digit numeric string | alarmNo | - | 55 |
| 11 | u_mes_perf_torqueResult | entity | transaction | 16-digit numeric string | torqueResultNo | - | 52 |
| 12 | u_mes_perf_leakTestResult | entity | transaction | 16-digit numeric string | leakTestNo | - | 38 |
| 13 | u_mes_perf_leakTestResultStage | child | transaction | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_perf_leakTestResult | 25 |
| 14 | u_mes_perf_energyReading | entity | transaction | 16-digit numeric string | energyReadingNo | - | 35 |
| 15 | u_mes_perf_lossCategory | entity | master | 16-digit numeric string | code | - | 12 |
| 16 | u_mes_perf_reasonCategory | entity | master | 16-digit numeric string | code | - | 10 |
| 17 | u_mes_perf_energyType | entity | master | 16-digit numeric string | code | - | 12 |
| 18 | u_mes_perf_alarmDefinition | entity | master | 16-digit numeric string | ALM-<equipment type code>-<alarm code>, e.g. ALM-LEAKTESTER-E104 | - | 22 |
| 19 | u_mes_perf_lossSummary | entity | transaction | 16-digit numeric string | LSS-<yyyymmdd>-<line code>-<shift code>-<reason code> | - | 34 |
| 20 | u_mes_perf_workCenterPerformance | entity | transaction | 16-digit numeric string | WCP-<yyyymmddhh>-<work centre code> | - | 35 |
| 21 | u_mes_perf_operatorPerformance | entity | transaction | 16-digit numeric string | OPF-<yyyymmdd>-<badge no>-<work centre code> | - | 30 |

### maint - Tooling And Maintenance

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_maint_maintenancePlan | entity | master | 16-digit numeric string | planNo | - | 25 |
| 2 | u_mes_maint_maintenancePlanTask | child | master | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_maint_maintenancePlan | 13 |
| 3 | u_mes_maint_maintenancePlanRequiredSkill | relationship | master | 16-digit numeric string | parent recordNo + -RS<nnn> | u_mes_maint_maintenancePlan | 11 |
| 4 | u_mes_maint_maintenancePlanRequiredSparePart | child | master | 16-digit numeric string | parent recordNo + -RSP<nnn> | u_mes_maint_maintenancePlan | 12 |
| 5 | u_mes_maint_maintenanceWorkOrder | entity | transaction | 16-digit numeric string | workOrderNo | - | 57 |
| 6 | u_mes_maint_maintenanceWorkOrderAssignedToUser | relationship | transaction | 16-digit numeric string | parent recordNo + -ATU<nnn> | u_mes_maint_maintenanceWorkOrder | 17 |
| 7 | u_mes_maint_maintenanceWorkOrderLabour | child | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_maint_maintenanceWorkOrder | 18 |
| 8 | u_mes_maint_maintenanceWorkOrderUsedSparePart | child | transaction | 16-digit numeric string | parent recordNo + -USP<nnn> | u_mes_maint_maintenanceWorkOrder | 19 |
| 9 | u_mes_maint_sparePart | entity | master | 16-digit numeric string | sparePartNo | - | 27 |
| 10 | u_mes_maint_sparePartUsedOnEquipment | relationship | master | 16-digit numeric string | parent recordNo + -UOE<nnn> | u_mes_maint_sparePart | 11 |
| 11 | u_mes_maint_tool | entity | master | 16-digit numeric string | toolNo | - | 39 |
| 12 | u_mes_maint_toolItem | relationship | master | 16-digit numeric string | parent recordNo + -I<nnn> | u_mes_maint_tool | 11 |
| 13 | u_mes_maint_toolLifeRecord | entity | transaction | 16-digit numeric string | toolLifeNo | - | 40 |
| 14 | u_mes_maint_toolType | entity | master | 16-digit numeric string | code | - | 11 |
| 15 | u_mes_maint_maintenanceWorkOrderTask | child | transaction | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_maint_maintenanceWorkOrder | 26 |
| 16 | u_mes_maint_sparePartTransaction | entity | transaction | 16-digit numeric string | SPT-<yyyymmdd>-<nnnnn> | - | 31 |
| 17 | u_mes_maint_reliabilitySummary | entity | transaction | 16-digit numeric string | REL-<yyyymm or yyyymmdd>-<equipment code> | - | 29 |
| 18 | u_mes_maint_equipmentLifecycleEvent | entity | transaction | 16-digit numeric string | ELE-<equipment code>-<nnn> | - | 31 |
| 19 | u_mes_maint_logbookEntry | entity | transaction | 16-digit numeric string | LOG-<equipment or area code>-<nnnnn>, e.g. LOG-ASY-01-P1-00412 | - | 35 |
| 20 | u_mes_maint_cleaningRecord | entity | transaction | 16-digit numeric string | CLN-<yyyymmdd>-<nnn>, e.g. CLN-20260915-003 | - | 37 |
| 21 | u_mes_maint_equipmentQualification | entity | transaction | 16-digit numeric string | EQQ-<equipment code>-<phase>-<nn>, e.g. EQQ-LKT-01-T1-PQ-01 | - | 35 |

### syst - System and Integration

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_syst_erpMessage | entity | transaction | 16-digit numeric string | messageNo | - | 41 |
| 2 | u_mes_syst_integrationConnector | entity | master | 16-digit numeric string | connectorCode | - | 23 |
| 3 | u_mes_syst_integrationConnectorFunction | child | master | 16-digit numeric string | parent recordNo + -F<nnn> | u_mes_syst_integrationConnector | 14 |
| 4 | u_mes_syst_iotDevice | entity | master | 16-digit numeric string | deviceCode | - | 32 |
| 5 | u_mes_syst_operatorApp | entity | master | 16-digit numeric string | appCode | - | 18 |
| 6 | u_mes_syst_operatorAppWorkCenter | relationship | master | 16-digit numeric string | parent recordNo + -WC<nnn> | u_mes_syst_operatorApp | 11 |
| 7 | u_mes_syst_operatorAppOperation | relationship | master | 16-digit numeric string | parent recordNo + -O<nnn> | u_mes_syst_operatorApp | 11 |
| 8 | u_mes_syst_operatorAppStep | child | master | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_syst_operatorApp | 16 |
| 9 | u_mes_syst_operatorAppStepTrigger | child | master | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_syst_operatorAppStep | 12 |
| 10 | u_mes_syst_operatorAppDeviceBinding | child | master | 16-digit numeric string | parent recordNo + -DB<nnn> | u_mes_syst_operatorApp | 12 |
| 11 | u_mes_syst_operatorAppLanguage | relationship | master | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_syst_operatorApp | 11 |
| 12 | u_mes_syst_businessEvent | entity | transaction | 16-digit numeric string | eventNo | - | 33 |
| 13 | u_mes_syst_auditTrail | entity | transaction | 16-digit numeric string | auditTrailNo | - | 31 |
| 14 | u_mes_syst_auditTrailChange | child | transaction | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_syst_auditTrail | 18 |
| 15 | u_mes_syst_electronicSignature | entity | transaction | 16-digit numeric string | signatureNo | - | 33 |
| 16 | u_mes_syst_notification | entity | transaction | 16-digit numeric string | notificationNo | - | 43 |
| 17 | u_mes_syst_notificationRecipient | child | transaction | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_syst_notification | 23 |
| 18 | u_mes_syst_controlledDocument | entity | transaction | 16-digit numeric string | documentNo | - | 39 |
| 19 | u_mes_syst_controlledDocumentTag | valueList | transaction | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_syst_controlledDocument | 16 |
| 20 | u_mes_syst_numberRange | entity | master | 16-digit numeric string | rangeCode | - | 25 |
| 21 | u_mes_syst_systemConfiguration | entity | master | 16-digit numeric string | configKey | - | 19 |
| 22 | u_mes_syst_documentType | entity | master | 16-digit numeric string | code | - | 12 |
| 23 | u_mes_syst_deviceType | entity | master | 16-digit numeric string | code | - | 10 |
| 24 | u_mes_syst_notificationType | entity | master | 16-digit numeric string | code | - | 10 |
| 25 | u_mes_syst_statusDefinition | entity | master | 16-digit numeric string | definition code | - | 16 |
| 26 | u_mes_syst_enumerationValue | entity | master | 16-digit numeric string | definition code | - | 14 |
| 27 | u_mes_syst_statusTransition | entity | master | 16-digit numeric string | definition code | - | 16 |
| 28 | u_mes_syst_interlockRule | entity | master | 16-digit numeric string | ILR-<rule type code>-<nnn>, e.g. ILR-SEQ-001 | - | 29 |
| 29 | u_mes_syst_statusTransitionRole | relationship | master | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_syst_statusTransition | 11 |
| 30 | u_mes_syst_escalationRule | entity | master | 16-digit numeric string | ESC-<code>, e.g. ESC-BREAKDOWN-CRIT | - | 18 |
| 31 | u_mes_syst_escalationRuleLevel | child | master | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_syst_escalationRule | 16 |
| 32 | u_mes_syst_alertRule | entity | master | 16-digit numeric string | ALR-<metric code>-<nnn> | - | 30 |
| 33 | u_mes_syst_analyticsModel | entity | master | 16-digit numeric string | AIM-<code>-<version>, e.g. AIM-VIS-BOOT-1.3 | - | 23 |
| 34 | u_mes_syst_modelPrediction | entity | transaction | 16-digit numeric string | PRD-<yyyymmdd>-<nnnnnn> | - | 40 |
| 35 | u_mes_syst_simulationStudy | entity | transaction | 16-digit numeric string | SIM-<yyyy>-<nnn> | - | 34 |
| 36 | u_mes_syst_recordPolicy | entity | master | 16-digit numeric string | RPO-<collection name> | - | 19 |
| 37 | u_mes_syst_savedView | entity | master | 16-digit numeric string | VIEW-<user or role code>-<nnn> | - | 17 |
| 38 | u_mes_syst_backupRun | entity | transaction | 16-digit numeric string | BKP-<yyyymmdd>-<nn> | - | 24 |
| 39 | u_mes_syst_computerisedSystem | entity | master | 16-digit numeric string | CSY-<system code>, e.g. CSY-MES-PN1 | - | 28 |
| 40 | u_mes_syst_systemValidation | entity | transaction | 16-digit numeric string | CSV-<yyyy>-<nnn>, e.g. CSV-2026-014 | - | 39 |
| 41 | u_mes_syst_systemPeriodicReview | entity | transaction | 16-digit numeric string | SPR-<system code>-<yyyy>-<nn>, e.g. SPR-MES-PN1-2026-01 | - | 32 |
| 42 | u_mes_syst_auditTrailReview | entity | transaction | 16-digit numeric string | ATR-<yyyymmdd>-<nnn>, e.g. ATR-20260916-004 | - | 32 |
| 43 | u_mes_syst_userAccessReview | entity | transaction | 16-digit numeric string | UAR-<system code>-<yyyy>-<nn>, e.g. UAR-MES-PN1-2026-03 | - | 26 |
| 44 | u_mes_syst_userAccessReviewLine | child | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_syst_userAccessReview | 23 |

### ehs - Environment Health and Safety

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_ehs_safetyIncident | entity | transaction | 16-digit numeric string | incidentNo | - | 45 |
| 2 | u_mes_ehs_safetyIncidentWitnessUser | relationship | transaction | 16-digit numeric string | parent recordNo + -WU<nnn> | u_mes_ehs_safetyIncident | 17 |
| 3 | u_mes_ehs_safetyIncidentAction | child | transaction | 16-digit numeric string | parent recordNo + -A<nnn> | u_mes_ehs_safetyIncident | 20 |
| 4 | u_mes_ehs_incidentType | entity | master | 16-digit numeric string | code | - | 12 |
| 5 | u_mes_ehs_bodyPart | entity | master | 16-digit numeric string | code | - | 10 |
| 6 | u_mes_ehs_injuryType | entity | master | 16-digit numeric string | code | - | 10 |

### bmr - Batch Manufacturing Record

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_bmr_batchRecordReview | entity | transaction | 16-digit numeric string | BRR-<order number>, e.g. BRR-PO-1000412 | - | 37 |
| 2 | u_mes_bmr_batchRecordReviewException | child | transaction | 16-digit numeric string | parent recordNo + -E<nnn> | u_mes_bmr_batchRecordReview | 24 |
| 3 | u_mes_bmr_batchRelease | entity | transaction | 16-digit numeric string | BRL-<lot number>, e.g. BRL-L260915-GDC-014 | - | 36 |
| 4 | u_mes_bmr_yieldReconciliation | entity | transaction | 16-digit numeric string | YRC-<order number>-<nn>, e.g. YRC-PO-1000412-01 | - | 37 |
| 5 | u_mes_bmr_batchManufacturingRecord | entity | transaction | 16-digit numeric string | BMR-<order number>, e.g. BMR-PO-1000412 | - | 41 |

### mmr - Master Manufacturing Record

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_mmr_masterManufacturingRecord | entity | master | 16-digit numeric string | MMR-<item number>-<version>, e.g. MMR-5110-10-0100-03 | - | 54 |
| 2 | u_mes_mmr_masterManufacturingRecordRecipe | relationship | master | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_mmr_masterManufacturingRecord | 11 |

## 5. Change log

| Version | Date | Change |
|---|---|---|
| 2.9 | 15 Oct 2026 | Module maint renamed Tooling And Maintenance; ampersand removed from all module names (D060). No collection, key or ID changes |
| 1.0 | 11 Oct 2026 | 104 collections registered (nested model), conventions, seed frame, first master IDs |
| 1.1 | 11 Oct 2026 | Key list added |
| 2.0 | 11 Oct 2026 | Requirements of 11 Oct applied: u_mes_<moduleCode>_<singular> names, flat documents, ID plus display pairs, recordNo, audit keys on transaction data only, status mapping collections; 104 concepts became 369 collections; operations 11 and items 12 documents confirmed; work centre spelling changed to workCenter |
| 2.9 | 12 Oct 2026 | Owner decisions on the BMR / MMR designation (D057-D059): u_mes_mmr_masterManufacturingRecord (1367) with the relationship u_mes_mmr_masterManufacturingRecordRecipe (1368), and u_mes_bmr_batchManufacturingRecord (1369) added; line clearance and dispensing stay in plan and matl, audit-trail review stays in syst |
| 2.8 | 12 Oct 2026 | Modules bmr (Batch Manufacturing Record) and mmr (Master Manufacturing Record) added on the owner's instruction (D054-D056). Collections unique to the batch manufacturing record moved to bmr with their numbers and _id values unchanged: u_mes_qual_batchRecordReview, u_mes_qual_batchRecordReviewException and u_mes_qual_batchRelease to u_mes_bmr_*, u_mes_plan_yieldReconciliation to u_mes_bmr_yieldReconciliation. No collection is unique to the master manufacturing record, so mmr has no collections yet. Collections shared by BMR / MMR and the rest of the MES are listed in 01_research/BMR_MMR_module_designation.md and were not moved |
| 2.7 | 12 Oct 2026 | GMP_Pharma_01 implemented (D047-D053): 23 collections added (numbers 1344-1366, existing numbers unchanged), 33 keys added to 11 existing collections (41 keys with display pairs), allowed values extended; computerised system inventory, system validation, periodic review, audit-trail review, user access review, batch record review by exception, batch release, yield and label reconciliation, line clearance, equipment and area logbook, cleaning records, environmental monitoring, dispensing, retention samples, quality risk assessment, product quality review, recalls, process validation, equipment qualification. Analysis: 01_research/GMP_Pharma_01_impact_analysis.md |
| 2.6 | 12 Oct 2026 | MES_ExternalRequirement_01 implemented (D036-D042): 44 collections added (numbers 1300-1343, existing numbers unchanged), 212 keys added to 38 existing collections, allowed values extended; interlock rules and events, escalation and alert rules, operator sessions, document acknowledgements, recipe downloads, set-up verification, exposure timers, replenishment rules, trace investigations, per-position results and measurement curves, defect records, LPA schedules, alarm definitions, loss and performance reports, maintenance checklists, spare-part transactions, lifecycle events, analytics models and predictions, simulation studies, record policies, saved views, backup runs. Analysis: 01_research/MES_ExternalRequirement_01_impact_analysis.md |
| 2.5 | 12 Oct 2026 | DATA-004: dates and times stored as local plant time (IST) with the +0000 suffix; every date key tagged Date or Datetime; sample data regenerated |
| 2.4 | 12 Oct 2026 | Sample documents: exactly 10 per collection in 03_design/<module>/samples; system IDs changed to 16-digit numeric strings; sample period moved to April-September 2026; master ID registry replaced by the generated 04_reference_data/sample_data_registry.md; child, relationship and value-list collections use recordNo as display value |
| 2.3 | 11 Oct 2026 | Module codes and names changed on the owner's instruction: mast, prod, plan, matl, trac, qual, perf, maint, syst, ehs. Every collection name changed with its module code. Module Energy, safety and andon dissolved: andon collections moved to plan, energy collections to perf, safety collections kept in the new module ehs (Environment Health and Safety). Module folders renamed |
| 2.2 | 11 Oct 2026 | Master data review: 41 master collections added (department, designation, employmentType and others), 67 text keys converted to master references, fixed enumerations mapped in u_mes_syst_enumerationValue; see 08_validation/reports/master_data_review.md |
| 2.1 | 11 Oct 2026 | Collection specifications written for all modules: field dictionary, validator, indexes and sample per collection under 03_design; check report in 08_validation/reports/specification_check.md |
