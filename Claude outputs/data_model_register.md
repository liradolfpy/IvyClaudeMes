# data_model_register.md

MES on MongoDB - Front Brake Caliper Assembly LH - Pune
Register version: 2.6 | Date: 12 October 2026 | Database: mes | Model version 2.6 | 12 October 2026 | 343 collections (178 entity, 82 child, 75 relationship, 8 value-list), 7383 keys

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


### mast - MasterDataManagement

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_mast_enterprise | entity | master | 16-digit numeric string | enterpriseCode | - | 26 |
| 2 | u_mes_mast_enterpriseContact | child | master | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_mast_enterprise | 12 |
| 3 | u_mes_mast_site | entity | master | 16-digit numeric string | siteCode | - | 30 |
| 4 | u_mes_mast_siteCertificate | child | master | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_mast_site | 12 |
| 5 | u_mes_mast_area | entity | master | 16-digit numeric string | areaCode | - | 17 |
| 6 | u_mes_mast_line | entity | master | 16-digit numeric string | lineCode | - | 22 |
| 7 | u_mes_mast_lineDefaultShift | relationship | master | 16-digit numeric string | parent recordNo + -DS<nnn> | u_mes_mast_line | 10 |
| 8 | u_mes_mast_lineIdealRate | child | master | 16-digit numeric string | parent recordNo + -IR<nnn> | u_mes_mast_line | 12 |
| 9 | u_mes_mast_workCenter | entity | master | 16-digit numeric string | workCentreCode | - | 24 |
| 10 | u_mes_mast_workCenterEquipment | relationship | master | 16-digit numeric string | parent recordNo + -E<nnn> | u_mes_mast_workCenter | 10 |
| 11 | u_mes_mast_workCenterOperation | relationship | master | 16-digit numeric string | parent recordNo + -O<nnn> | u_mes_mast_workCenter | 10 |
| 12 | u_mes_mast_workCenterRequiresSkill | relationship | master | 16-digit numeric string | parent recordNo + -RS<nnn> | u_mes_mast_workCenter | 10 |
| 13 | u_mes_mast_equipment | entity | master | 16-digit numeric string | equipmentCode | - | 47 |
| 14 | u_mes_mast_equipmentIotDevice | relationship | master | 16-digit numeric string | parent recordNo + -ID<nnn> | u_mes_mast_equipment | 10 |
| 15 | u_mes_mast_shift | entity | master | 16-digit numeric string | shiftCode | - | 14 |
| 16 | u_mes_mast_shiftBreak | child | master | 16-digit numeric string | parent recordNo + -B<nnn> | u_mes_mast_shift | 12 |
| 17 | u_mes_mast_shiftWorkingDay | valueList | master | 16-digit numeric string | parent recordNo + -WD<nnn> | u_mes_mast_shift | 9 |
| 18 | u_mes_mast_workCalendar | entity | master | 16-digit numeric string | calendarCode | - | 11 |
| 19 | u_mes_mast_workCalendarLine | relationship | master | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_mast_workCalendar | 10 |
| 20 | u_mes_mast_workCalendarShift | relationship | master | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_mast_workCalendar | 10 |
| 21 | u_mes_mast_workCalendarWeeklyOffDay | valueList | master | 16-digit numeric string | parent recordNo + -WOD<nnn> | u_mes_mast_workCalendar | 9 |
| 22 | u_mes_mast_workCalendarException | child | master | 16-digit numeric string | parent recordNo + -E<nnn> | u_mes_mast_workCalendar | 12 |
| 23 | u_mes_mast_workCalendarExceptionShift | relationship | master | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_mast_workCalendarException | 10 |
| 24 | u_mes_mast_shiftRoster | entity | transaction | 16-digit numeric string | rosterNo | - | 25 |
| 25 | u_mes_mast_shiftRosterAssignment | child | transaction | 16-digit numeric string | parent recordNo + -A<nnn> | u_mes_mast_shiftRoster | 26 |
| 26 | u_mes_mast_role | entity | master | 16-digit numeric string | roleCode | - | 12 |
| 27 | u_mes_mast_rolePermission | relationship | master | 16-digit numeric string | parent recordNo + -P<nnn> | u_mes_mast_role | 10 |
| 28 | u_mes_mast_roleSignatureMeaning | relationship | master | 16-digit numeric string | parent recordNo + -SM<nnn> | u_mes_mast_role | 10 |
| 29 | u_mes_mast_user | entity | master | 16-digit numeric string | employeeNo | - | 33 |
| 30 | u_mes_mast_userRole | relationship | master | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_mast_user | 10 |
| 31 | u_mes_mast_skill | entity | master | 16-digit numeric string | skillCode | - | 16 |
| 32 | u_mes_mast_skillOperation | relationship | master | 16-digit numeric string | parent recordNo + -O<nnn> | u_mes_mast_skill | 10 |
| 33 | u_mes_mast_skillLevelScale | child | master | 16-digit numeric string | parent recordNo + -LS<nnn> | u_mes_mast_skill | 10 |
| 34 | u_mes_mast_skillCertification | entity | transaction | 16-digit numeric string | certificationNo | - | 34 |
| 35 | u_mes_mast_customer | entity | master | 16-digit numeric string | customerCode | - | 26 |
| 36 | u_mes_mast_customerShipTo | child | master | 16-digit numeric string | parent recordNo + -ST<nnn> | u_mes_mast_customer | 16 |
| 37 | u_mes_mast_customerContact | child | master | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_mast_customer | 12 |
| 38 | u_mes_mast_supplier | entity | master | 16-digit numeric string | supplierCode | - | 26 |
| 39 | u_mes_mast_supplierContact | child | master | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_mast_supplier | 12 |
| 40 | u_mes_mast_supplierCertificate | child | master | 16-digit numeric string | parent recordNo + -C2<nnn> | u_mes_mast_supplier | 11 |
| 41 | u_mes_mast_supplierSuppliedItem | relationship | master | 16-digit numeric string | parent recordNo + -SI<nnn> | u_mes_mast_supplier | 10 |
| 42 | u_mes_mast_unitOfMeasure | entity | master | 16-digit numeric string | uomCode | - | 17 |
| 43 | u_mes_mast_department | entity | master | 16-digit numeric string | code | - | 15 |
| 44 | u_mes_mast_designation | entity | master | 16-digit numeric string | code | - | 13 |
| 45 | u_mes_mast_employmentType | entity | master | 16-digit numeric string | code | - | 10 |
| 46 | u_mes_mast_costCenter | entity | master | 16-digit numeric string | code | - | 11 |
| 47 | u_mes_mast_manufacturer | entity | master | 16-digit numeric string | code | - | 12 |
| 48 | u_mes_mast_equipmentType | entity | master | 16-digit numeric string | code | - | 9 |
| 49 | u_mes_mast_skillCategory | entity | master | 16-digit numeric string | code | - | 9 |
| 50 | u_mes_mast_permission | entity | master | 16-digit numeric string | code | - | 11 |
| 51 | u_mes_mast_signatureMeaning | entity | master | 16-digit numeric string | code | - | 9 |
| 52 | u_mes_mast_currency | entity | master | 16-digit numeric string | code | - | 11 |
| 53 | u_mes_mast_country | entity | master | 16-digit numeric string | code | - | 10 |
| 54 | u_mes_mast_language | entity | master | 16-digit numeric string | code | - | 9 |
| 55 | u_mes_mast_transporter | entity | master | 16-digit numeric string | code | - | 11 |
| 56 | u_mes_mast_commodity | entity | master | 16-digit numeric string | code | - | 9 |
| 57 | u_mes_mast_roleRequiredSkill | relationship | master | 16-digit numeric string | parent recordNo + -RS<nnn> | u_mes_mast_role | 11 |

### prod - ProductDefinition

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_prod_item | entity | master | 16-digit numeric string | itemNo | - | 38 |
| 2 | u_mes_prod_itemRevision | child | master | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_prod_item | 13 |
| 3 | u_mes_prod_itemCustomerPart | child | master | 16-digit numeric string | parent recordNo + -CP<nnn> | u_mes_prod_item | 12 |
| 4 | u_mes_prod_productVariant | entity | master | 16-digit numeric string | variantCode | - | 28 |
| 5 | u_mes_prod_billOfMaterial | entity | master | 16-digit numeric string | bomNo | - | 22 |
| 6 | u_mes_prod_billOfMaterialComponent | child | master | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_prod_billOfMaterial | 20 |
| 7 | u_mes_prod_billOfMaterialComponentProductVariant | relationship | master | 16-digit numeric string | parent recordNo + -PV<nnn> | u_mes_prod_billOfMaterialComponent | 10 |
| 8 | u_mes_prod_billOfMaterialComponentAlternateItem | relationship | master | 16-digit numeric string | parent recordNo + -AI<nnn> | u_mes_prod_billOfMaterialComponent | 10 |
| 9 | u_mes_prod_operation | entity | master | 16-digit numeric string | operationCode | - | 21 |
| 10 | u_mes_prod_operationRequiredSkill | relationship | master | 16-digit numeric string | parent recordNo + -RS<nnn> | u_mes_prod_operation | 10 |
| 11 | u_mes_prod_routing | entity | master | 16-digit numeric string | routingNo | - | 23 |
| 12 | u_mes_prod_routingStep | child | master | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_prod_routing | 19 |
| 13 | u_mes_prod_routingStepAlternateWorkCenter | relationship | master | 16-digit numeric string | parent recordNo + -AWC<nnn> | u_mes_prod_routingStep | 10 |
| 14 | u_mes_prod_routingStepNextStep | child | master | 16-digit numeric string | parent recordNo + -NS<nnn> | u_mes_prod_routingStep | 9 |
| 15 | u_mes_prod_billOfProcess | entity | master | 16-digit numeric string | bopNo | - | 19 |
| 16 | u_mes_prod_billOfProcessStep | child | master | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_prod_billOfProcess | 18 |
| 17 | u_mes_prod_billOfProcessStepEquipment | relationship | master | 16-digit numeric string | parent recordNo + -E<nnn> | u_mes_prod_billOfProcessStep | 10 |
| 18 | u_mes_prod_billOfProcessStepTool | relationship | master | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_prod_billOfProcessStep | 10 |
| 19 | u_mes_prod_billOfProcessStepRequiredSkill | relationship | master | 16-digit numeric string | parent recordNo + -RS<nnn> | u_mes_prod_billOfProcessStep | 10 |
| 20 | u_mes_prod_billOfProcessStepConsumedComponent | child | master | 16-digit numeric string | parent recordNo + -CC<nnn> | u_mes_prod_billOfProcessStep | 12 |
| 21 | u_mes_prod_billOfProcessStepInterlock | child | master | 16-digit numeric string | parent recordNo + -I<nnn> | u_mes_prod_billOfProcessStep | 11 |
| 22 | u_mes_prod_billOfProcessStepProcessParameter | child | master | 16-digit numeric string | parent recordNo + -PP<nnn> | u_mes_prod_billOfProcessStep | 14 |
| 23 | u_mes_prod_workInstruction | entity | master | 16-digit numeric string | instructionNo | - | 29 |
| 24 | u_mes_prod_workInstructionStep | child | master | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_prod_workInstruction | 21 |
| 25 | u_mes_prod_workInstructionStepMediaControlledDocument | relationship | master | 16-digit numeric string | parent recordNo + -MCD<nnn> | u_mes_prod_workInstructionStep | 10 |
| 26 | u_mes_prod_workInstructionStepProductVariant | relationship | master | 16-digit numeric string | parent recordNo + -PV<nnn> | u_mes_prod_workInstructionStep | 10 |
| 27 | u_mes_prod_workInstructionStepTool | relationship | master | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_prod_workInstructionStep | 10 |
| 28 | u_mes_prod_workInstructionStepCharacteristic | relationship | master | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_prod_workInstructionStep | 10 |
| 29 | u_mes_prod_workInstructionPpeItem | relationship | master | 16-digit numeric string | parent recordNo + -PI<nnn> | u_mes_prod_workInstruction | 10 |
| 30 | u_mes_prod_workInstructionKeyPoint | valueList | master | 16-digit numeric string | parent recordNo + -KP<nnn> | u_mes_prod_workInstruction | 9 |
| 31 | u_mes_prod_recipe | entity | master | 16-digit numeric string | recipeNo | - | 36 |
| 32 | u_mes_prod_recipeParameter | child | master | 16-digit numeric string | parent recordNo + -P<nnn> | u_mes_prod_recipe | 18 |
| 33 | u_mes_prod_recipeStage | child | master | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_prod_recipe | 11 |
| 34 | u_mes_prod_engineeringChange | entity | transaction | 16-digit numeric string | ecnNo | - | 31 |
| 35 | u_mes_prod_engineeringChangeAffectedItem | child | transaction | 16-digit numeric string | parent recordNo + -AI<nnn> | u_mes_prod_engineeringChange | 18 |
| 36 | u_mes_prod_engineeringChangeAffectedObject | child | transaction | 16-digit numeric string | parent recordNo + -AO<nnn> | u_mes_prod_engineeringChange | 18 |
| 37 | u_mes_prod_engineeringChangeApproval | child | transaction | 16-digit numeric string | parent recordNo + -A<nnn> | u_mes_prod_engineeringChange | 20 |
| 38 | u_mes_prod_engineeringChangeControlledDocument | relationship | transaction | 16-digit numeric string | parent recordNo + -CD<nnn> | u_mes_prod_engineeringChange | 16 |
| 39 | u_mes_prod_itemGroup | entity | master | 16-digit numeric string | code | - | 9 |
| 40 | u_mes_prod_itemFamily | entity | master | 16-digit numeric string | code | - | 9 |
| 41 | u_mes_prod_ppeItem | entity | master | 16-digit numeric string | code | - | 9 |
| 42 | u_mes_prod_market | entity | master | 16-digit numeric string | code | - | 9 |
| 43 | u_mes_prod_padCompound | entity | master | 16-digit numeric string | code | - | 9 |
| 44 | u_mes_prod_surfaceFinish | entity | master | 16-digit numeric string | code | - | 9 |
| 45 | u_mes_prod_vehicleModel | entity | master | 16-digit numeric string | code | - | 13 |
| 46 | u_mes_prod_recipeProductVariant | relationship | master | 16-digit numeric string | parent recordNo + -PV<nnn> | u_mes_prod_recipe | 10 |
| 47 | u_mes_prod_recipeControlledDocument | relationship | master | 16-digit numeric string | parent recordNo + -CD<nnn> | u_mes_prod_recipe | 11 |
| 48 | u_mes_prod_workInstructionWorkCenter | relationship | master | 16-digit numeric string | parent recordNo + -WC<nnn> | u_mes_prod_workInstruction | 10 |
| 49 | u_mes_prod_workInstructionProductVariant | relationship | master | 16-digit numeric string | parent recordNo + -PV<nnn> | u_mes_prod_workInstruction | 10 |

### plan - PlanningAndExecution

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_plan_customerSchedule | entity | transaction | 16-digit numeric string | releaseNo | - | 23 |
| 2 | u_mes_plan_customerScheduleLine | child | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_plan_customerSchedule | 23 |
| 3 | u_mes_plan_productionOrder | entity | transaction | 16-digit numeric string | orderNo | - | 53 |
| 4 | u_mes_plan_productionOrderRelease | child | transaction | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_plan_productionOrder | 18 |
| 5 | u_mes_plan_productionOrderLot | relationship | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_plan_productionOrder | 16 |
| 6 | u_mes_plan_productionSchedule | entity | transaction | 16-digit numeric string | scheduleNo | - | 27 |
| 7 | u_mes_plan_productionScheduleSlot | child | transaction | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_plan_productionSchedule | 23 |
| 8 | u_mes_plan_dispatchList | entity | transaction | 16-digit numeric string | dispatchNo | - | 22 |
| 9 | u_mes_plan_dispatchListEntry | child | transaction | 16-digit numeric string | parent recordNo + -E<nnn> | u_mes_plan_dispatchList | 28 |
| 10 | u_mes_plan_operationExecution | entity | transaction | 16-digit numeric string | executionNo | - | 70 |
| 11 | u_mes_plan_operationExecutionDefectCode | relationship | transaction | 16-digit numeric string | parent recordNo + -DC<nnn> | u_mes_plan_operationExecution | 16 |
| 12 | u_mes_plan_operationExecutionTool | relationship | transaction | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_plan_operationExecution | 16 |
| 13 | u_mes_plan_stepCompletion | entity | transaction | 16-digit numeric string | completionNo | - | 43 |
| 14 | u_mes_plan_wipUnit | entity | transaction | 16-digit numeric string | unitNo | - | 47 |
| 15 | u_mes_plan_wipUnitCompletedStep | valueList | transaction | 16-digit numeric string | parent recordNo + -CS<nnn> | u_mes_plan_wipUnit | 15 |
| 16 | u_mes_plan_lot | entity | transaction | 16-digit numeric string | lotNo | - | 47 |
| 17 | u_mes_plan_lotParentLot | relationship | transaction | 16-digit numeric string | parent recordNo + -PL<nnn> | u_mes_plan_lot | 16 |
| 18 | u_mes_plan_lotAttributesCavityNo | valueList | transaction | 16-digit numeric string | parent recordNo + -ACN<nnn> | u_mes_plan_lot | 15 |
| 19 | u_mes_plan_container | entity | transaction | 16-digit numeric string | containerNo | - | 39 |
| 20 | u_mes_plan_containerLot | relationship | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_plan_container | 16 |
| 21 | u_mes_plan_labourBooking | entity | transaction | 16-digit numeric string | bookingNo | - | 42 |
| 22 | u_mes_plan_changeover | entity | transaction | 16-digit numeric string | changeoverNo | - | 40 |
| 23 | u_mes_plan_changeoverStep | child | transaction | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_plan_changeover | 19 |
| 24 | u_mes_plan_changeoverRemovedTool | relationship | transaction | 16-digit numeric string | parent recordNo + -RT<nnn> | u_mes_plan_changeover | 16 |
| 25 | u_mes_plan_changeoverInstalledTool | relationship | transaction | 16-digit numeric string | parent recordNo + -IT<nnn> | u_mes_plan_changeover | 16 |
| 26 | u_mes_plan_changeoverPerformedByUser | relationship | transaction | 16-digit numeric string | parent recordNo + -PBU<nnn> | u_mes_plan_changeover | 16 |
| 27 | u_mes_plan_shiftHandover | entity | transaction | 16-digit numeric string | handoverNo | - | 32 |
| 28 | u_mes_plan_shiftHandoverProductionOrder | relationship | transaction | 16-digit numeric string | parent recordNo + -PO<nnn> | u_mes_plan_shiftHandover | 16 |
| 29 | u_mes_plan_shiftHandoverDowntimeEvent | relationship | transaction | 16-digit numeric string | parent recordNo + -DE<nnn> | u_mes_plan_shiftHandover | 16 |
| 30 | u_mes_plan_shiftHandoverNonconformance | relationship | transaction | 16-digit numeric string | parent recordNo + -N<nnn> | u_mes_plan_shiftHandover | 16 |
| 31 | u_mes_plan_shiftHandoverOpenItem | child | transaction | 16-digit numeric string | parent recordNo + -OI<nnn> | u_mes_plan_shiftHandover | 19 |
| 32 | u_mes_plan_andonEvent | entity | transaction | 16-digit numeric string | andonNo | - | 45 |
| 33 | u_mes_plan_andonEventEscalation | child | transaction | 16-digit numeric string | parent recordNo + -E<nnn> | u_mes_plan_andonEvent | 19 |
| 34 | u_mes_plan_indirectActivity | entity | master | 16-digit numeric string | code | - | 12 |
| 35 | u_mes_plan_containerType | entity | master | 16-digit numeric string | code | - | 14 |
| 36 | u_mes_plan_andonType | entity | master | 16-digit numeric string | code | - | 16 |
| 37 | u_mes_plan_operatorSession | entity | transaction | 16-digit numeric string | OSN-<yyyymmdd>-<nnnnn>, e.g. OSN-20260916-00042 | - | 32 |
| 38 | u_mes_plan_documentAcknowledgement | entity | transaction | 16-digit numeric string | ACK-<yyyymmdd>-<nnnnn> | - | 33 |
| 39 | u_mes_plan_interlockEvent | entity | transaction | 16-digit numeric string | ILK-<yyyymmdd>-<nnnnn> | - | 50 |
| 40 | u_mes_plan_recipeDownload | entity | transaction | 16-digit numeric string | RDL-<yyyymmdd>-<nnnnn> | - | 33 |
| 41 | u_mes_plan_setupVerification | entity | transaction | 16-digit numeric string | SUV-<yyyymmdd>-<nnnnn> | - | 32 |
| 42 | u_mes_plan_setupVerificationItem | child | transaction | 16-digit numeric string | parent recordNo + -I<nnn> | u_mes_plan_setupVerification | 25 |

### matl - MaterialManagement

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_matl_storageLocation | entity | master | 16-digit numeric string | locationCode | - | 24 |
| 2 | u_mes_matl_inventoryBalance | entity | transaction | 16-digit numeric string | inventoryNo | - | 33 |
| 3 | u_mes_matl_materialMovement | entity | transaction | 16-digit numeric string | movementNo | - | 48 |
| 4 | u_mes_matl_goodsReceipt | entity | transaction | 16-digit numeric string | grnNo | - | 25 |
| 5 | u_mes_matl_goodsReceiptLine | child | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_matl_goodsReceipt | 29 |
| 6 | u_mes_matl_goodsReceiptLineInspectionResult | relationship | transaction | 16-digit numeric string | parent recordNo + -IR<nnn> | u_mes_matl_goodsReceiptLine | 16 |
| 7 | u_mes_matl_kit | entity | transaction | 16-digit numeric string | kitNo | - | 28 |
| 8 | u_mes_matl_kitLine | child | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_matl_kit | 29 |
| 9 | u_mes_matl_materialRequest | entity | transaction | 16-digit numeric string | requestNo | - | 41 |
| 10 | u_mes_matl_materialConsumption | entity | transaction | 16-digit numeric string | consumptionNo | - | 43 |
| 11 | u_mes_matl_packagingSpecification | entity | master | 16-digit numeric string | packSpecNo | - | 28 |
| 12 | u_mes_matl_packagingSpecificationLevel | child | master | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_matl_packagingSpecification | 14 |
| 13 | u_mes_matl_labelTemplate | entity | master | 16-digit numeric string | templateCode | - | 19 |
| 14 | u_mes_matl_labelTemplateField | child | master | 16-digit numeric string | parent recordNo + -F<nnn> | u_mes_matl_labelTemplate | 14 |
| 15 | u_mes_matl_label | entity | transaction | 16-digit numeric string | labelNo | - | 41 |
| 16 | u_mes_matl_shipment | entity | transaction | 16-digit numeric string | shipmentNo | - | 39 |
| 17 | u_mes_matl_shipmentLine | child | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_matl_shipment | 18 |
| 18 | u_mes_matl_shipmentLineContainer | relationship | transaction | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_matl_shipmentLine | 16 |
| 19 | u_mes_matl_shipmentLineLot | relationship | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_matl_shipmentLine | 16 |
| 20 | u_mes_matl_movementType | entity | master | 16-digit numeric string | code | - | 12 |
| 21 | u_mes_matl_stockStatus | entity | master | 16-digit numeric string | code | - | 11 |
| 22 | u_mes_matl_packType | entity | master | 16-digit numeric string | code | - | 9 |
| 23 | u_mes_matl_exposureTimer | entity | transaction | 16-digit numeric string | EXT-<yyyymmdd>-<nnnnn> | - | 31 |
| 24 | u_mes_matl_replenishmentRule | entity | master | 16-digit numeric string | RPL-<item code>-<location code>, e.g. RPL-PST-54-LS-OP060 | - | 27 |
| 25 | u_mes_matl_materialDemandForecast | entity | transaction | 16-digit numeric string | MDF-<yyyymmdd>-<line code>-<item code>-<hh> | - | 30 |
| 26 | u_mes_matl_storageLocationAllowedItem | relationship | master | 16-digit numeric string | parent recordNo + -AI<nnn> | u_mes_matl_storageLocation | 12 |

### trac - Traceability

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_trac_serialNumber | entity | transaction | 16-digit numeric string | serialNo | - | 43 |
| 2 | u_mes_trac_genealogyLink | entity | transaction | 16-digit numeric string | linkNo | - | 43 |
| 3 | u_mes_trac_componentLotLink | entity | transaction | 16-digit numeric string | lotLinkNo | - | 32 |
| 4 | u_mes_trac_asBuiltRecord | entity | transaction | 16-digit numeric string | recordNo | - | 53 |
| 5 | u_mes_trac_asBuiltRecordComponent | child | transaction | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_trac_asBuiltRecord | 22 |
| 6 | u_mes_trac_asBuiltRecordOperation | child | transaction | 16-digit numeric string | parent recordNo + -O<nnn> | u_mes_trac_asBuiltRecord | 28 |
| 7 | u_mes_trac_asBuiltRecordInspectionResult | relationship | transaction | 16-digit numeric string | parent recordNo + -IR<nnn> | u_mes_trac_asBuiltRecord | 16 |
| 8 | u_mes_trac_traceInvestigation | entity | transaction | 16-digit numeric string | TRC-<yyyymmdd>-<nnn> | - | 32 |
| 9 | u_mes_trac_traceInvestigationResult | child | transaction | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_trac_traceInvestigation | 28 |

### qual - QualityManagement

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_qual_characteristic | entity | master | 16-digit numeric string | characteristicCode | - | 33 |
| 2 | u_mes_qual_controlPlan | entity | master | 16-digit numeric string | controlPlanNo | - | 26 |
| 3 | u_mes_qual_controlPlanCoreTeamUser | relationship | master | 16-digit numeric string | parent recordNo + -CTU<nnn> | u_mes_qual_controlPlan | 10 |
| 4 | u_mes_qual_controlPlanLine | child | master | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_qual_controlPlan | 24 |
| 5 | u_mes_qual_inspectionPlan | entity | master | 16-digit numeric string | inspectionPlanNo | - | 27 |
| 6 | u_mes_qual_inspectionPlanLine | child | master | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_qual_inspectionPlan | 20 |
| 7 | u_mes_qual_samplingPlan | entity | master | 16-digit numeric string | samplingPlanCode | - | 18 |
| 8 | u_mes_qual_samplingPlanSizeRow | child | master | 16-digit numeric string | parent recordNo + -SR<nnn> | u_mes_qual_samplingPlan | 13 |
| 9 | u_mes_qual_checkSheet | entity | master | 16-digit numeric string | checkSheetCode | - | 24 |
| 10 | u_mes_qual_checkSheetItem | child | master | 16-digit numeric string | parent recordNo + -I<nnn> | u_mes_qual_checkSheet | 16 |
| 11 | u_mes_qual_checkSheetResult | entity | transaction | 16-digit numeric string | checkResultNo | - | 36 |
| 12 | u_mes_qual_checkSheetResultAnswer | child | transaction | 16-digit numeric string | parent recordNo + -A<nnn> | u_mes_qual_checkSheetResult | 18 |
| 13 | u_mes_qual_inspectionResult | entity | transaction | 16-digit numeric string | resultNo | - | 65 |
| 14 | u_mes_qual_spcChart | entity | master | 16-digit numeric string | chartNo | - | 29 |
| 15 | u_mes_qual_spcChartControlLimit | child | master | 16-digit numeric string | parent recordNo + -CL<nnn> | u_mes_qual_spcChart | 16 |
| 16 | u_mes_qual_spcChartRule | valueList | master | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_qual_spcChart | 9 |
| 17 | u_mes_qual_spcSample | entity | transaction | 16-digit numeric string | sampleNo | - | 41 |
| 18 | u_mes_qual_spcSampleReading | valueList | transaction | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_qual_spcSample | 15 |
| 19 | u_mes_qual_spcSampleInspectionResult | relationship | transaction | 16-digit numeric string | parent recordNo + -IR<nnn> | u_mes_qual_spcSample | 16 |
| 20 | u_mes_qual_spcSampleViolation | child | transaction | 16-digit numeric string | parent recordNo + -V<nnn> | u_mes_qual_spcSample | 16 |
| 21 | u_mes_qual_defectCode | entity | master | 16-digit numeric string | defectCode | - | 21 |
| 22 | u_mes_qual_defectCodeApplicableOperation | relationship | master | 16-digit numeric string | parent recordNo + -AO<nnn> | u_mes_qual_defectCode | 10 |
| 23 | u_mes_qual_nonconformance | entity | transaction | 16-digit numeric string | ncrNo | - | 45 |
| 24 | u_mes_qual_nonconformanceAffectedObject | child | transaction | 16-digit numeric string | parent recordNo + -AO<nnn> | u_mes_qual_nonconformance | 23 |
| 25 | u_mes_qual_nonconformanceContainmentAction | child | transaction | 16-digit numeric string | parent recordNo + -CA<nnn> | u_mes_qual_nonconformance | 18 |
| 26 | u_mes_qual_nonconformanceInspectionResult | relationship | transaction | 16-digit numeric string | parent recordNo + -IR<nnn> | u_mes_qual_nonconformance | 16 |
| 27 | u_mes_qual_nonconformanceReworkOrder | relationship | transaction | 16-digit numeric string | parent recordNo + -RO<nnn> | u_mes_qual_nonconformance | 16 |
| 28 | u_mes_qual_nonconformanceScrapRecord | relationship | transaction | 16-digit numeric string | parent recordNo + -SR<nnn> | u_mes_qual_nonconformance | 16 |
| 29 | u_mes_qual_nonconformancePhotoControlledDocument | relationship | transaction | 16-digit numeric string | parent recordNo + -PCD<nnn> | u_mes_qual_nonconformance | 16 |
| 30 | u_mes_qual_nonconformanceMrbUser | relationship | transaction | 16-digit numeric string | parent recordNo + -MU<nnn> | u_mes_qual_nonconformance | 16 |
| 31 | u_mes_qual_reworkOrder | entity | transaction | 16-digit numeric string | reworkNo | - | 44 |
| 32 | u_mes_qual_reworkOrderWipUnit | relationship | transaction | 16-digit numeric string | parent recordNo + -WU<nnn> | u_mes_qual_reworkOrder | 16 |
| 33 | u_mes_qual_reworkOrderStep | child | transaction | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_qual_reworkOrder | 20 |
| 34 | u_mes_qual_scrapRecord | entity | transaction | 16-digit numeric string | scrapNo | - | 50 |
| 35 | u_mes_qual_qualityHold | entity | transaction | 16-digit numeric string | holdNo | - | 37 |
| 36 | u_mes_qual_qualityHoldHeldObject | child | transaction | 16-digit numeric string | parent recordNo + -HO<nnn> | u_mes_qual_qualityHold | 20 |
| 37 | u_mes_qual_deviationPermit | entity | transaction | 16-digit numeric string | deviationNo | - | 38 |
| 38 | u_mes_qual_deviationPermitApproval | child | transaction | 16-digit numeric string | parent recordNo + -A<nnn> | u_mes_qual_deviationPermit | 19 |
| 39 | u_mes_qual_capa | entity | transaction | 16-digit numeric string | capaNo | - | 42 |
| 40 | u_mes_qual_capaNonconformance | relationship | transaction | 16-digit numeric string | parent recordNo + -N<nnn> | u_mes_qual_capa | 16 |
| 41 | u_mes_qual_capaTeamMember | child | transaction | 16-digit numeric string | parent recordNo + -TM<nnn> | u_mes_qual_capa | 17 |
| 42 | u_mes_qual_capaContainmentAction | child | transaction | 16-digit numeric string | parent recordNo + -CA<nnn> | u_mes_qual_capa | 18 |
| 43 | u_mes_qual_capaCorrectiveAction | child | transaction | 16-digit numeric string | parent recordNo + -CA2<nnn> | u_mes_qual_capa | 18 |
| 44 | u_mes_qual_capaImplementationAction | child | transaction | 16-digit numeric string | parent recordNo + -IA<nnn> | u_mes_qual_capa | 19 |
| 45 | u_mes_qual_capaControlledDocument | relationship | transaction | 16-digit numeric string | parent recordNo + -CD<nnn> | u_mes_qual_capa | 16 |
| 46 | u_mes_qual_pfmea | entity | master | 16-digit numeric string | pfmeaNo | - | 19 |
| 47 | u_mes_qual_pfmeaCoreTeamUser | relationship | master | 16-digit numeric string | parent recordNo + -CTU<nnn> | u_mes_qual_pfmea | 10 |
| 48 | u_mes_qual_pfmeaLine | child | master | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_qual_pfmea | 32 |
| 49 | u_mes_qual_ppapSubmission | entity | transaction | 16-digit numeric string | ppapNo | - | 35 |
| 50 | u_mes_qual_ppapSubmissionElement | child | transaction | 16-digit numeric string | parent recordNo + -E<nnn> | u_mes_qual_ppapSubmission | 19 |
| 51 | u_mes_qual_ppapSubmissionMsaStudy | relationship | transaction | 16-digit numeric string | parent recordNo + -MS<nnn> | u_mes_qual_ppapSubmission | 16 |
| 52 | u_mes_qual_gauge | entity | master | 16-digit numeric string | gaugeNo | - | 39 |
| 53 | u_mes_qual_gaugeCalibration | entity | transaction | 16-digit numeric string | calibrationNo | - | 35 |
| 54 | u_mes_qual_gaugeCalibrationReading | child | transaction | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_qual_gaugeCalibration | 19 |
| 55 | u_mes_qual_msaStudy | entity | transaction | 16-digit numeric string | msaNo | - | 41 |
| 56 | u_mes_qual_msaStudyAppraiserUser | relationship | transaction | 16-digit numeric string | parent recordNo + -AU<nnn> | u_mes_qual_msaStudy | 16 |
| 57 | u_mes_qual_msaStudyTrial | child | transaction | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_qual_msaStudy | 18 |
| 58 | u_mes_qual_audit | entity | transaction | 16-digit numeric string | auditNo | - | 44 |
| 59 | u_mes_qual_auditAuditorUser | relationship | transaction | 16-digit numeric string | parent recordNo + -AU<nnn> | u_mes_qual_audit | 16 |
| 60 | u_mes_qual_auditFinding | child | transaction | 16-digit numeric string | parent recordNo + -F<nnn> | u_mes_qual_audit | 23 |
| 61 | u_mes_qual_customerComplaint | entity | transaction | 16-digit numeric string | complaintNo | - | 43 |
| 62 | u_mes_qual_customerComplaintSerialNumber | relationship | transaction | 16-digit numeric string | parent recordNo + -SN<nnn> | u_mes_qual_customerComplaint | 16 |
| 63 | u_mes_qual_customerComplaintShipment | relationship | transaction | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_qual_customerComplaint | 16 |
| 64 | u_mes_qual_customerComplaintSuspectLot | relationship | transaction | 16-digit numeric string | parent recordNo + -SL<nnn> | u_mes_qual_customerComplaint | 16 |
| 65 | u_mes_qual_customerComplaintCommunication | child | transaction | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_qual_customerComplaint | 19 |
| 66 | u_mes_qual_defectGroup | entity | master | 16-digit numeric string | code | - | 9 |
| 67 | u_mes_qual_gaugeType | entity | master | 16-digit numeric string | code | - | 9 |
| 68 | u_mes_qual_dispositionType | entity | master | 16-digit numeric string | code | - | 12 |
| 69 | u_mes_qual_complaintType | entity | master | 16-digit numeric string | code | - | 9 |
| 70 | u_mes_qual_characteristicPosition | child | master | 16-digit numeric string | parent recordNo + -P<nnn> | u_mes_qual_characteristic | 16 |
| 71 | u_mes_qual_curveEnvelope | entity | master | 16-digit numeric string | ENV-<characteristic code>-<version>, e.g. ENV-OP060-PISTON-PRESS-02 | - | 31 |
| 72 | u_mes_qual_curveEnvelopeWindow | child | master | 16-digit numeric string | parent recordNo + -W<nnn> | u_mes_qual_curveEnvelope | 15 |
| 73 | u_mes_qual_measurementCurve | entity | transaction | 16-digit numeric string | CRV-<yyyymmdd>-<nnnnnn> | - | 38 |
| 74 | u_mes_qual_measurementCurvePoint | entity | transaction | 16-digit numeric string | parent curve recordNo + -<nnnn> | - | 17 |
| 75 | u_mes_qual_defectRecord | entity | transaction | 16-digit numeric string | DEF-<yyyymmdd>-<nnnnn> | - | 61 |
| 76 | u_mes_qual_auditSchedule | entity | master | 16-digit numeric string | LPA-<layer>-<line code>-<nn>, e.g. LPA-L2-LN-CAL-01 | - | 29 |
| 77 | u_mes_qual_inspectionPlanProductVariant | relationship | master | 16-digit numeric string | parent recordNo + -PV<nnn> | u_mes_qual_inspectionPlan | 10 |

### perf - PerformanceManagement

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_perf_reasonCode | entity | master | 16-digit numeric string | reasonCode | - | 23 |
| 2 | u_mes_perf_equipmentState | entity | transaction | 16-digit numeric string | stateEventNo | - | 30 |
| 3 | u_mes_perf_downtimeEvent | entity | transaction | 16-digit numeric string | downtimeNo | - | 54 |
| 4 | u_mes_perf_downtimeEventComment | child | transaction | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_perf_downtimeEvent | 18 |
| 5 | u_mes_perf_productionCount | entity | transaction | 16-digit numeric string | countNo | - | 34 |
| 6 | u_mes_perf_oeeRecord | entity | transaction | 16-digit numeric string | oeeRecordNo | - | 42 |
| 7 | u_mes_perf_oeeRecordLoss | child | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_perf_oeeRecord | 20 |
| 8 | u_mes_perf_processTag | entity | master | 16-digit numeric string | tagName | - | 34 |
| 9 | u_mes_perf_processReading | entity | transaction | 16-digit numeric string | readingNo | - | 29 |
| 10 | u_mes_perf_alarm | entity | transaction | 16-digit numeric string | alarmNo | - | 54 |
| 11 | u_mes_perf_torqueResult | entity | transaction | 16-digit numeric string | torqueResultNo | - | 51 |
| 12 | u_mes_perf_leakTestResult | entity | transaction | 16-digit numeric string | leakTestNo | - | 37 |
| 13 | u_mes_perf_leakTestResultStage | child | transaction | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_perf_leakTestResult | 24 |
| 14 | u_mes_perf_energyReading | entity | transaction | 16-digit numeric string | energyReadingNo | - | 34 |
| 15 | u_mes_perf_lossCategory | entity | master | 16-digit numeric string | code | - | 11 |
| 16 | u_mes_perf_reasonCategory | entity | master | 16-digit numeric string | code | - | 9 |
| 17 | u_mes_perf_energyType | entity | master | 16-digit numeric string | code | - | 11 |
| 18 | u_mes_perf_alarmDefinition | entity | master | 16-digit numeric string | ALM-<equipment type code>-<alarm code>, e.g. ALM-LEAKTESTER-E104 | - | 21 |
| 19 | u_mes_perf_lossSummary | entity | transaction | 16-digit numeric string | LSS-<yyyymmdd>-<line code>-<shift code>-<reason code> | - | 33 |
| 20 | u_mes_perf_workCenterPerformance | entity | transaction | 16-digit numeric string | WCP-<yyyymmddhh>-<work centre code> | - | 34 |
| 21 | u_mes_perf_operatorPerformance | entity | transaction | 16-digit numeric string | OPF-<yyyymmdd>-<badge no>-<work centre code> | - | 29 |

### maint - ToolingAndMaintenance

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_maint_maintenancePlan | entity | master | 16-digit numeric string | planNo | - | 24 |
| 2 | u_mes_maint_maintenancePlanTask | child | master | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_maint_maintenancePlan | 12 |
| 3 | u_mes_maint_maintenancePlanRequiredSkill | relationship | master | 16-digit numeric string | parent recordNo + -RS<nnn> | u_mes_maint_maintenancePlan | 10 |
| 4 | u_mes_maint_maintenancePlanRequiredSparePart | child | master | 16-digit numeric string | parent recordNo + -RSP<nnn> | u_mes_maint_maintenancePlan | 11 |
| 5 | u_mes_maint_maintenanceWorkOrder | entity | transaction | 16-digit numeric string | workOrderNo | - | 56 |
| 6 | u_mes_maint_maintenanceWorkOrderAssignedToUser | relationship | transaction | 16-digit numeric string | parent recordNo + -ATU<nnn> | u_mes_maint_maintenanceWorkOrder | 16 |
| 7 | u_mes_maint_maintenanceWorkOrderLabour | child | transaction | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_maint_maintenanceWorkOrder | 17 |
| 8 | u_mes_maint_maintenanceWorkOrderUsedSparePart | child | transaction | 16-digit numeric string | parent recordNo + -USP<nnn> | u_mes_maint_maintenanceWorkOrder | 18 |
| 9 | u_mes_maint_sparePart | entity | master | 16-digit numeric string | sparePartNo | - | 26 |
| 10 | u_mes_maint_sparePartUsedOnEquipment | relationship | master | 16-digit numeric string | parent recordNo + -UOE<nnn> | u_mes_maint_sparePart | 10 |
| 11 | u_mes_maint_tool | entity | master | 16-digit numeric string | toolNo | - | 38 |
| 12 | u_mes_maint_toolItem | relationship | master | 16-digit numeric string | parent recordNo + -I<nnn> | u_mes_maint_tool | 10 |
| 13 | u_mes_maint_toolLifeRecord | entity | transaction | 16-digit numeric string | toolLifeNo | - | 39 |
| 14 | u_mes_maint_toolType | entity | master | 16-digit numeric string | code | - | 10 |
| 15 | u_mes_maint_maintenanceWorkOrderTask | child | transaction | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_maint_maintenanceWorkOrder | 25 |
| 16 | u_mes_maint_sparePartTransaction | entity | transaction | 16-digit numeric string | SPT-<yyyymmdd>-<nnnnn> | - | 30 |
| 17 | u_mes_maint_reliabilitySummary | entity | transaction | 16-digit numeric string | REL-<yyyymm or yyyymmdd>-<equipment code> | - | 28 |
| 18 | u_mes_maint_equipmentLifecycleEvent | entity | transaction | 16-digit numeric string | ELE-<equipment code>-<nnn> | - | 30 |

### syst - SystemAndIntegration

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_syst_erpMessage | entity | transaction | 16-digit numeric string | messageNo | - | 40 |
| 2 | u_mes_syst_integrationConnector | entity | master | 16-digit numeric string | connectorCode | - | 22 |
| 3 | u_mes_syst_integrationConnectorFunction | child | master | 16-digit numeric string | parent recordNo + -F<nnn> | u_mes_syst_integrationConnector | 13 |
| 4 | u_mes_syst_iotDevice | entity | master | 16-digit numeric string | deviceCode | - | 31 |
| 5 | u_mes_syst_operatorApp | entity | master | 16-digit numeric string | appCode | - | 17 |
| 6 | u_mes_syst_operatorAppWorkCenter | relationship | master | 16-digit numeric string | parent recordNo + -WC<nnn> | u_mes_syst_operatorApp | 10 |
| 7 | u_mes_syst_operatorAppOperation | relationship | master | 16-digit numeric string | parent recordNo + -O<nnn> | u_mes_syst_operatorApp | 10 |
| 8 | u_mes_syst_operatorAppStep | child | master | 16-digit numeric string | parent recordNo + -S<nnn> | u_mes_syst_operatorApp | 15 |
| 9 | u_mes_syst_operatorAppStepTrigger | child | master | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_syst_operatorAppStep | 11 |
| 10 | u_mes_syst_operatorAppDeviceBinding | child | master | 16-digit numeric string | parent recordNo + -DB<nnn> | u_mes_syst_operatorApp | 11 |
| 11 | u_mes_syst_operatorAppLanguage | relationship | master | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_syst_operatorApp | 10 |
| 12 | u_mes_syst_businessEvent | entity | transaction | 16-digit numeric string | eventNo | - | 32 |
| 13 | u_mes_syst_auditTrail | entity | transaction | 16-digit numeric string | auditTrailNo | - | 27 |
| 14 | u_mes_syst_auditTrailChange | child | transaction | 16-digit numeric string | parent recordNo + -C<nnn> | u_mes_syst_auditTrail | 17 |
| 15 | u_mes_syst_electronicSignature | entity | transaction | 16-digit numeric string | signatureNo | - | 29 |
| 16 | u_mes_syst_notification | entity | transaction | 16-digit numeric string | notificationNo | - | 42 |
| 17 | u_mes_syst_notificationRecipient | child | transaction | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_syst_notification | 22 |
| 18 | u_mes_syst_controlledDocument | entity | transaction | 16-digit numeric string | documentNo | - | 38 |
| 19 | u_mes_syst_controlledDocumentTag | valueList | transaction | 16-digit numeric string | parent recordNo + -T<nnn> | u_mes_syst_controlledDocument | 15 |
| 20 | u_mes_syst_numberRange | entity | master | 16-digit numeric string | rangeCode | - | 24 |
| 21 | u_mes_syst_systemConfiguration | entity | master | 16-digit numeric string | configKey | - | 18 |
| 22 | u_mes_syst_documentType | entity | master | 16-digit numeric string | code | - | 11 |
| 23 | u_mes_syst_deviceType | entity | master | 16-digit numeric string | code | - | 9 |
| 24 | u_mes_syst_notificationType | entity | master | 16-digit numeric string | code | - | 9 |
| 25 | u_mes_syst_statusDefinition | entity | master | 16-digit numeric string | definition code | - | 15 |
| 26 | u_mes_syst_enumerationValue | entity | master | 16-digit numeric string | definition code | - | 13 |
| 27 | u_mes_syst_statusTransition | entity | master | 16-digit numeric string | definition code | - | 15 |
| 28 | u_mes_syst_interlockRule | entity | master | 16-digit numeric string | ILR-<rule type code>-<nnn>, e.g. ILR-SEQ-001 | - | 28 |
| 29 | u_mes_syst_statusTransitionRole | relationship | master | 16-digit numeric string | parent recordNo + -R<nnn> | u_mes_syst_statusTransition | 10 |
| 30 | u_mes_syst_escalationRule | entity | master | 16-digit numeric string | ESC-<code>, e.g. ESC-BREAKDOWN-CRIT | - | 17 |
| 31 | u_mes_syst_escalationRuleLevel | child | master | 16-digit numeric string | parent recordNo + -L<nnn> | u_mes_syst_escalationRule | 15 |
| 32 | u_mes_syst_alertRule | entity | master | 16-digit numeric string | ALR-<metric code>-<nnn> | - | 29 |
| 33 | u_mes_syst_analyticsModel | entity | master | 16-digit numeric string | AIM-<code>-<version>, e.g. AIM-VIS-BOOT-1.3 | - | 22 |
| 34 | u_mes_syst_modelPrediction | entity | transaction | 16-digit numeric string | PRD-<yyyymmdd>-<nnnnnn> | - | 39 |
| 35 | u_mes_syst_simulationStudy | entity | transaction | 16-digit numeric string | SIM-<yyyy>-<nnn> | - | 33 |
| 36 | u_mes_syst_recordPolicy | entity | master | 16-digit numeric string | RPO-<collection name> | - | 17 |
| 37 | u_mes_syst_savedView | entity | master | 16-digit numeric string | VIEW-<user or role code>-<nnn> | - | 16 |
| 38 | u_mes_syst_backupRun | entity | transaction | 16-digit numeric string | BKP-<yyyymmdd>-<nn> | - | 23 |

### ehs - EnvironmentHealthAndSafety

| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_ehs_safetyIncident | entity | transaction | 16-digit numeric string | incidentNo | - | 44 |
| 2 | u_mes_ehs_safetyIncidentWitnessUser | relationship | transaction | 16-digit numeric string | parent recordNo + -WU<nnn> | u_mes_ehs_safetyIncident | 16 |
| 3 | u_mes_ehs_safetyIncidentAction | child | transaction | 16-digit numeric string | parent recordNo + -A<nnn> | u_mes_ehs_safetyIncident | 19 |
| 4 | u_mes_ehs_incidentType | entity | master | 16-digit numeric string | code | - | 11 |
| 5 | u_mes_ehs_bodyPart | entity | master | 16-digit numeric string | code | - | 9 |
| 6 | u_mes_ehs_injuryType | entity | master | 16-digit numeric string | code | - | 9 |

## 5. Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 11 Oct 2026 | 104 collections registered (nested model), conventions, seed frame, first master IDs |
| 1.1 | 11 Oct 2026 | Key list added |
| 2.0 | 11 Oct 2026 | Requirements of 11 Oct applied: u_mes_<moduleCode>_<singular> names, flat documents, ID plus display pairs, recordNo, audit keys on transaction data only, status mapping collections; 104 concepts became 343 collections; operations 11 and items 12 documents confirmed; work centre spelling changed to workCenter |
| 2.6 | 12 Oct 2026 | MES_ExternalRequirement_01 implemented (D036-D042): 44 collections added (numbers 1300-1343, existing numbers unchanged), 212 keys added to 38 existing collections, allowed values extended; interlock rules and events, escalation and alert rules, operator sessions, document acknowledgements, recipe downloads, set-up verification, exposure timers, replenishment rules, trace investigations, per-position results and measurement curves, defect records, LPA schedules, alarm definitions, loss and performance reports, maintenance checklists, spare-part transactions, lifecycle events, analytics models and predictions, simulation studies, record policies, saved views, backup runs. Analysis: 01_research/MES_ExternalRequirement_01_impact_analysis.md |
| 2.5 | 12 Oct 2026 | DATA-004: dates and times stored as local plant time (IST) with the +0000 suffix; every date key tagged Date or Datetime; sample data regenerated |
| 2.4 | 12 Oct 2026 | Sample documents: exactly 10 per collection in 03_design/<module>/samples; system IDs changed to 16-digit numeric strings; sample period moved to April-September 2026; master ID registry replaced by the generated 04_reference_data/sample_data_registry.md; child, relationship and value-list collections use recordNo as display value |
| 2.3 | 11 Oct 2026 | Module codes and names changed on the owner's instruction: mast, prod, plan, matl, trac, qual, perf, maint, syst, ehs. Every collection name changed with its module code. Module Energy, safety and andon dissolved: andon collections moved to plan, energy collections to perf, safety collections kept in the new module ehs (EnvironmentHealthAndSafety). Module folders renamed |
| 2.2 | 11 Oct 2026 | Master data review: 41 master collections added (department, designation, employmentType and others), 67 text keys converted to master references, fixed enumerations mapped in u_mes_syst_enumerationValue; see 08_validation/reports/master_data_review.md |
| 2.1 | 11 Oct 2026 | Collection specifications written for all modules: field dictionary, validator, indexes and sample per collection under 03_design; check report in 08_validation/reports/specification_check.md |
