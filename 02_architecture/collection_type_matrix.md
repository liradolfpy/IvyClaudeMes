# Collection type matrix

Model version 3.0 | 19 October 2026 | 372 collections (203 entity, 85 child, 76 relationship, 8 value-list), 8703 keys

Type of each collection and the label used for it in the UI menu. A child, relationship or value-list collection has the type of the entity it belongs to; its label starts with the parent's name, because it is opened from the parent's screen.

| Type | Meaning | Collections |
|---|---|---|
| Master | Reference data that changes rarely and is maintained by the plant | 189 |
| Transaction | Business records created by daily operations | 162 |
| Reports | Pre-aggregated or assembled records built from transactions for reporting | 12 |
| Telemetry | Machine-generated, time-ordered signals and states | 5 |
| Audit Trail | Append-only records of who did or changed what | 4 |

## Collections per module and type

| Code | ModuleName | Master | Transaction | Reports | Telemetry | Audit Trail | Total |
|---|---|---|---|---|---|---|---|
| mast | MasterDataManagement | 54 | 3 | 0 | 0 | 0 | 57 |
| prod | ProductDefinition | 44 | 5 | 0 | 0 | 0 | 49 |
| plan | PlanningAndExecution | 3 | 40 | 0 | 0 | 0 | 43 |
| matl | MaterialManagement | 10 | 16 | 1 | 0 | 0 | 27 |
| trac | Traceability | 0 | 5 | 4 | 0 | 0 | 9 |
| qual | QualityManagement | 29 | 55 | 0 | 1 | 0 | 85 |
| perf | PerformanceManagement | 6 | 5 | 6 | 4 | 0 | 21 |
| maint | ToolingAndMaintenance | 9 | 11 | 1 | 0 | 0 | 21 |
| syst | SystemAndIntegration | 29 | 14 | 0 | 0 | 4 | 47 |
| ehs | EnvironmentHealthAndSafety | 3 | 3 | 0 | 0 | 0 | 6 |
| bmr | BatchManufacturingRecord | 0 | 5 | 0 | 0 | 0 | 5 |
| mmr | MasterManufacturingRecord | 2 | 0 | 0 | 0 | 0 | 2 |

## Matrix

| Code | ModuleName | Collection | Type | Label |
|---|---|---|---|---|
| mast | MasterDataManagement | u_mes_mast_enterprise | Master | Enterprises |
| mast | MasterDataManagement | u_mes_mast_enterpriseContact | Master | Enterprise Contacts |
| mast | MasterDataManagement | u_mes_mast_site | Master | Sites |
| mast | MasterDataManagement | u_mes_mast_siteCertificate | Master | Site Certificates |
| mast | MasterDataManagement | u_mes_mast_area | Master | Areas |
| mast | MasterDataManagement | u_mes_mast_line | Master | Lines |
| mast | MasterDataManagement | u_mes_mast_lineDefaultShift | Master | Line Default Shifts |
| mast | MasterDataManagement | u_mes_mast_lineIdealRate | Master | Line Ideal Rates |
| mast | MasterDataManagement | u_mes_mast_workCenter | Master | Work Centers |
| mast | MasterDataManagement | u_mes_mast_workCenterEquipment | Master | Work Center Equipment |
| mast | MasterDataManagement | u_mes_mast_workCenterOperation | Master | Work Center Operations |
| mast | MasterDataManagement | u_mes_mast_workCenterRequiresSkill | Master | Work Center Required Skills |
| mast | MasterDataManagement | u_mes_mast_equipment | Master | Equipment |
| mast | MasterDataManagement | u_mes_mast_equipmentIotDevice | Master | Equipment IoT Devices |
| mast | MasterDataManagement | u_mes_mast_shift | Master | Shifts |
| mast | MasterDataManagement | u_mes_mast_shiftBreak | Master | Shift Breaks |
| mast | MasterDataManagement | u_mes_mast_shiftWorkingDay | Master | Shift Working Days |
| mast | MasterDataManagement | u_mes_mast_workCalendar | Master | Work Calendars |
| mast | MasterDataManagement | u_mes_mast_workCalendarLine | Master | Work Calendar Lines |
| mast | MasterDataManagement | u_mes_mast_workCalendarShift | Master | Work Calendar Shifts |
| mast | MasterDataManagement | u_mes_mast_workCalendarWeeklyOffDay | Master | Work Calendar Weekly Off Days |
| mast | MasterDataManagement | u_mes_mast_workCalendarException | Master | Work Calendar Exceptions |
| mast | MasterDataManagement | u_mes_mast_workCalendarExceptionShift | Master | Work Calendar Exception Shifts |
| mast | MasterDataManagement | u_mes_mast_shiftRoster | Transaction | Shift Rosters |
| mast | MasterDataManagement | u_mes_mast_shiftRosterAssignment | Transaction | Shift Roster Assignments |
| mast | MasterDataManagement | u_mes_mast_role | Master | Roles |
| mast | MasterDataManagement | u_mes_mast_rolePermission | Master | Role Permissions |
| mast | MasterDataManagement | u_mes_mast_roleSignatureMeaning | Master | Role Signature Meanings |
| mast | MasterDataManagement | u_mes_mast_user | Master | Users |
| mast | MasterDataManagement | u_mes_mast_userRole | Master | User Roles |
| mast | MasterDataManagement | u_mes_mast_skill | Master | Skills |
| mast | MasterDataManagement | u_mes_mast_skillOperation | Master | Skill Operations |
| mast | MasterDataManagement | u_mes_mast_skillLevelScale | Master | Skill Level Scales |
| mast | MasterDataManagement | u_mes_mast_skillCertification | Transaction | Skill Certifications |
| mast | MasterDataManagement | u_mes_mast_customer | Master | Customers |
| mast | MasterDataManagement | u_mes_mast_customerShipTo | Master | Customer Ship-To Addresses |
| mast | MasterDataManagement | u_mes_mast_customerContact | Master | Customer Contacts |
| mast | MasterDataManagement | u_mes_mast_supplier | Master | Suppliers |
| mast | MasterDataManagement | u_mes_mast_supplierContact | Master | Supplier Contacts |
| mast | MasterDataManagement | u_mes_mast_supplierCertificate | Master | Supplier Certificates |
| mast | MasterDataManagement | u_mes_mast_supplierSuppliedItem | Master | Supplier Supplied Items |
| mast | MasterDataManagement | u_mes_mast_unitOfMeasure | Master | Units of Measure |
| mast | MasterDataManagement | u_mes_mast_department | Master | Departments |
| mast | MasterDataManagement | u_mes_mast_designation | Master | Designations |
| mast | MasterDataManagement | u_mes_mast_employmentType | Master | Employment Types |
| mast | MasterDataManagement | u_mes_mast_costCenter | Master | Cost Centers |
| mast | MasterDataManagement | u_mes_mast_manufacturer | Master | Manufacturers |
| mast | MasterDataManagement | u_mes_mast_equipmentType | Master | Equipment Types |
| mast | MasterDataManagement | u_mes_mast_skillCategory | Master | Skill Categories |
| mast | MasterDataManagement | u_mes_mast_permission | Master | Permissions |
| mast | MasterDataManagement | u_mes_mast_signatureMeaning | Master | Signature Meanings |
| mast | MasterDataManagement | u_mes_mast_currency | Master | Currencies |
| mast | MasterDataManagement | u_mes_mast_country | Master | Countries |
| mast | MasterDataManagement | u_mes_mast_language | Master | Languages |
| mast | MasterDataManagement | u_mes_mast_transporter | Master | Transporters |
| mast | MasterDataManagement | u_mes_mast_commodity | Master | Commodities |
| mast | MasterDataManagement | u_mes_mast_roleRequiredSkill | Master | Role Required Skills |
| prod | ProductDefinition | u_mes_prod_item | Master | Items |
| prod | ProductDefinition | u_mes_prod_itemRevision | Master | Item Revisions |
| prod | ProductDefinition | u_mes_prod_itemCustomerPart | Master | Item Customer Parts |
| prod | ProductDefinition | u_mes_prod_productVariant | Master | Product Variants |
| prod | ProductDefinition | u_mes_prod_billOfMaterial | Master | Bills of Material |
| prod | ProductDefinition | u_mes_prod_billOfMaterialComponent | Master | BOM Components |
| prod | ProductDefinition | u_mes_prod_billOfMaterialComponentProductVariant | Master | BOM Component Variants |
| prod | ProductDefinition | u_mes_prod_billOfMaterialComponentAlternateItem | Master | BOM Component Alternate Items |
| prod | ProductDefinition | u_mes_prod_operation | Master | Operations |
| prod | ProductDefinition | u_mes_prod_operationRequiredSkill | Master | Operation Required Skills |
| prod | ProductDefinition | u_mes_prod_routing | Master | Routings |
| prod | ProductDefinition | u_mes_prod_routingStep | Master | Routing Steps |
| prod | ProductDefinition | u_mes_prod_routingStepAlternateWorkCenter | Master | Routing Step Alternate Work Centers |
| prod | ProductDefinition | u_mes_prod_routingStepNextStep | Master | Routing Step Next Steps |
| prod | ProductDefinition | u_mes_prod_billOfProcess | Master | Bills of Process |
| prod | ProductDefinition | u_mes_prod_billOfProcessStep | Master | BOP Steps |
| prod | ProductDefinition | u_mes_prod_billOfProcessStepEquipment | Master | BOP Step Equipment |
| prod | ProductDefinition | u_mes_prod_billOfProcessStepTool | Master | BOP Step Tools |
| prod | ProductDefinition | u_mes_prod_billOfProcessStepRequiredSkill | Master | BOP Step Required Skills |
| prod | ProductDefinition | u_mes_prod_billOfProcessStepConsumedComponent | Master | BOP Step Consumed Components |
| prod | ProductDefinition | u_mes_prod_billOfProcessStepInterlock | Master | BOP Step Interlocks |
| prod | ProductDefinition | u_mes_prod_billOfProcessStepProcessParameter | Master | BOP Step Process Parameters |
| prod | ProductDefinition | u_mes_prod_workInstruction | Master | Work Instructions |
| prod | ProductDefinition | u_mes_prod_workInstructionStep | Master | Work Instruction Steps |
| prod | ProductDefinition | u_mes_prod_workInstructionStepMediaControlledDocument | Master | Work Instruction Step Media |
| prod | ProductDefinition | u_mes_prod_workInstructionStepProductVariant | Master | Work Instruction Step Product Variants |
| prod | ProductDefinition | u_mes_prod_workInstructionStepTool | Master | Work Instruction Step Tools |
| prod | ProductDefinition | u_mes_prod_workInstructionStepCharacteristic | Master | Work Instruction Step Characteristics |
| prod | ProductDefinition | u_mes_prod_workInstructionPpeItem | Master | Work Instruction PPE Items |
| prod | ProductDefinition | u_mes_prod_workInstructionKeyPoint | Master | Work Instruction Key Points |
| prod | ProductDefinition | u_mes_prod_recipe | Master | Recipes |
| prod | ProductDefinition | u_mes_prod_recipeParameter | Master | Recipe Parameters |
| prod | ProductDefinition | u_mes_prod_recipeStage | Master | Recipe Stages |
| prod | ProductDefinition | u_mes_prod_engineeringChange | Transaction | Engineering Changes |
| prod | ProductDefinition | u_mes_prod_engineeringChangeAffectedItem | Transaction | Engineering Change Affected Items |
| prod | ProductDefinition | u_mes_prod_engineeringChangeAffectedObject | Transaction | Engineering Change Affected Objects |
| prod | ProductDefinition | u_mes_prod_engineeringChangeApproval | Transaction | Engineering Change Approvals |
| prod | ProductDefinition | u_mes_prod_engineeringChangeControlledDocument | Transaction | Engineering Change Documents |
| prod | ProductDefinition | u_mes_prod_itemGroup | Master | Item Groups |
| prod | ProductDefinition | u_mes_prod_itemFamily | Master | Item Families |
| prod | ProductDefinition | u_mes_prod_ppeItem | Master | PPE Items |
| prod | ProductDefinition | u_mes_prod_market | Master | Markets |
| prod | ProductDefinition | u_mes_prod_padCompound | Master | Pad Compounds |
| prod | ProductDefinition | u_mes_prod_surfaceFinish | Master | Surface Finishes |
| prod | ProductDefinition | u_mes_prod_vehicleModel | Master | Vehicle Models |
| prod | ProductDefinition | u_mes_prod_recipeProductVariant | Master | Recipe Variants |
| prod | ProductDefinition | u_mes_prod_recipeControlledDocument | Master | Recipe Reference Files |
| prod | ProductDefinition | u_mes_prod_workInstructionWorkCenter | Master | Work Instruction Stations |
| prod | ProductDefinition | u_mes_prod_workInstructionProductVariant | Master | Work Instruction Variants |
| plan | PlanningAndExecution | u_mes_plan_customerSchedule | Transaction | Customer Schedules |
| plan | PlanningAndExecution | u_mes_plan_customerScheduleLine | Transaction | Customer Schedule Lines |
| plan | PlanningAndExecution | u_mes_plan_productionOrder | Transaction | Production Orders |
| plan | PlanningAndExecution | u_mes_plan_productionOrderRelease | Transaction | Production Order Releases |
| plan | PlanningAndExecution | u_mes_plan_productionOrderLot | Transaction | Production Order Lots |
| plan | PlanningAndExecution | u_mes_plan_productionSchedule | Transaction | Production Schedules |
| plan | PlanningAndExecution | u_mes_plan_productionScheduleSlot | Transaction | Production Schedule Slots |
| plan | PlanningAndExecution | u_mes_plan_dispatchList | Transaction | Dispatch Lists |
| plan | PlanningAndExecution | u_mes_plan_dispatchListEntry | Transaction | Dispatch List Entries |
| plan | PlanningAndExecution | u_mes_plan_operationExecution | Transaction | Operation Executions |
| plan | PlanningAndExecution | u_mes_plan_operationExecutionDefectCode | Transaction | Operation Execution Defect Codes |
| plan | PlanningAndExecution | u_mes_plan_operationExecutionTool | Transaction | Operation Execution Tools |
| plan | PlanningAndExecution | u_mes_plan_stepCompletion | Transaction | Work Instruction Step Completions |
| plan | PlanningAndExecution | u_mes_plan_wipUnit | Transaction | WIP Units |
| plan | PlanningAndExecution | u_mes_plan_wipUnitCompletedStep | Transaction | WIP Unit Completed Steps |
| plan | PlanningAndExecution | u_mes_plan_lot | Transaction | Lots and Batches |
| plan | PlanningAndExecution | u_mes_plan_lotParentLot | Transaction | Lot Parent Lots |
| plan | PlanningAndExecution | u_mes_plan_lotAttributesCavityNo | Transaction | Lot Cavity Numbers |
| plan | PlanningAndExecution | u_mes_plan_container | Transaction | Containers |
| plan | PlanningAndExecution | u_mes_plan_containerLot | Transaction | Container Lots |
| plan | PlanningAndExecution | u_mes_plan_labourBooking | Transaction | Labour Bookings |
| plan | PlanningAndExecution | u_mes_plan_changeover | Transaction | Changeovers |
| plan | PlanningAndExecution | u_mes_plan_changeoverStep | Transaction | Changeover Steps |
| plan | PlanningAndExecution | u_mes_plan_changeoverRemovedTool | Transaction | Changeover Removed Tools |
| plan | PlanningAndExecution | u_mes_plan_changeoverInstalledTool | Transaction | Changeover Installed Tools |
| plan | PlanningAndExecution | u_mes_plan_changeoverPerformedByUser | Transaction | Changeover Crew |
| plan | PlanningAndExecution | u_mes_plan_shiftHandover | Transaction | Shift Handovers |
| plan | PlanningAndExecution | u_mes_plan_shiftHandoverProductionOrder | Transaction | Shift Handover Production Orders |
| plan | PlanningAndExecution | u_mes_plan_shiftHandoverDowntimeEvent | Transaction | Shift Handover Downtime Events |
| plan | PlanningAndExecution | u_mes_plan_shiftHandoverNonconformance | Transaction | Shift Handover Nonconformances |
| plan | PlanningAndExecution | u_mes_plan_shiftHandoverOpenItem | Transaction | Shift Handover Open Items |
| plan | PlanningAndExecution | u_mes_plan_andonEvent | Transaction | Andon Events |
| plan | PlanningAndExecution | u_mes_plan_andonEventEscalation | Transaction | Andon Event Escalations |
| plan | PlanningAndExecution | u_mes_plan_indirectActivity | Master | Indirect Activities |
| plan | PlanningAndExecution | u_mes_plan_containerType | Master | Container Types |
| plan | PlanningAndExecution | u_mes_plan_andonType | Master | Andon Types |
| plan | PlanningAndExecution | u_mes_plan_operatorSession | Transaction | Operator Sessions |
| plan | PlanningAndExecution | u_mes_plan_documentAcknowledgement | Transaction | Document Acknowledgements |
| plan | PlanningAndExecution | u_mes_plan_interlockEvent | Transaction | Interlock Events |
| plan | PlanningAndExecution | u_mes_plan_recipeDownload | Transaction | Recipe Downloads |
| plan | PlanningAndExecution | u_mes_plan_setupVerification | Transaction | Setup Verifications |
| plan | PlanningAndExecution | u_mes_plan_setupVerificationItem | Transaction | Setup Verification Items |
| plan | PlanningAndExecution | u_mes_plan_lineClearance | Transaction | Line Clearances |
| matl | MaterialManagement | u_mes_matl_storageLocation | Master | Storage Locations |
| matl | MaterialManagement | u_mes_matl_inventoryBalance | Transaction | Inventory Balances |
| matl | MaterialManagement | u_mes_matl_materialMovement | Transaction | Material Movements |
| matl | MaterialManagement | u_mes_matl_goodsReceipt | Transaction | Goods Receipts |
| matl | MaterialManagement | u_mes_matl_goodsReceiptLine | Transaction | Goods Receipt Lines |
| matl | MaterialManagement | u_mes_matl_goodsReceiptLineInspectionResult | Transaction | Goods Receipt Line Inspection Results |
| matl | MaterialManagement | u_mes_matl_kit | Transaction | Kits |
| matl | MaterialManagement | u_mes_matl_kitLine | Transaction | Kit Lines |
| matl | MaterialManagement | u_mes_matl_materialRequest | Transaction | Material Requests |
| matl | MaterialManagement | u_mes_matl_materialConsumption | Transaction | Material Consumptions |
| matl | MaterialManagement | u_mes_matl_packagingSpecification | Master | Packaging Specifications |
| matl | MaterialManagement | u_mes_matl_packagingSpecificationLevel | Master | Packaging Specification Levels |
| matl | MaterialManagement | u_mes_matl_labelTemplate | Master | Label Templates |
| matl | MaterialManagement | u_mes_matl_labelTemplateField | Master | Label Template Fields |
| matl | MaterialManagement | u_mes_matl_label | Transaction | Printed Labels |
| matl | MaterialManagement | u_mes_matl_shipment | Transaction | Shipments |
| matl | MaterialManagement | u_mes_matl_shipmentLine | Transaction | Shipment Lines |
| matl | MaterialManagement | u_mes_matl_shipmentLineContainer | Transaction | Shipment Line Containers |
| matl | MaterialManagement | u_mes_matl_shipmentLineLot | Transaction | Shipment Line Lots |
| matl | MaterialManagement | u_mes_matl_movementType | Master | Movement Types |
| matl | MaterialManagement | u_mes_matl_stockStatus | Master | Stock Statuses |
| matl | MaterialManagement | u_mes_matl_packType | Master | Pack Types |
| matl | MaterialManagement | u_mes_matl_exposureTimer | Transaction | Exposure Timers |
| matl | MaterialManagement | u_mes_matl_replenishmentRule | Master | Replenishment Rules |
| matl | MaterialManagement | u_mes_matl_materialDemandForecast | Reports | Material Demand Forecast |
| matl | MaterialManagement | u_mes_matl_storageLocationAllowedItem | Master | Storage Allowed Items |
| matl | MaterialManagement | u_mes_matl_dispenseRecord | Transaction | Dispense Records |
| trac | Traceability | u_mes_trac_serialNumber | Transaction | Serial Numbers |
| trac | Traceability | u_mes_trac_genealogyLink | Transaction | Genealogy Links |
| trac | Traceability | u_mes_trac_componentLotLink | Transaction | Component Lot Links |
| trac | Traceability | u_mes_trac_asBuiltRecord | Reports | As-Built Records |
| trac | Traceability | u_mes_trac_asBuiltRecordComponent | Reports | As-Built Record Components |
| trac | Traceability | u_mes_trac_asBuiltRecordOperation | Reports | As-Built Record Operations |
| trac | Traceability | u_mes_trac_asBuiltRecordInspectionResult | Reports | As-Built Record Inspection Results |
| trac | Traceability | u_mes_trac_traceInvestigation | Transaction | Trace Investigations |
| trac | Traceability | u_mes_trac_traceInvestigationResult | Transaction | Trace Investigation Results |
| qual | QualityManagement | u_mes_qual_characteristic | Master | Characteristics |
| qual | QualityManagement | u_mes_qual_controlPlan | Master | Control Plans |
| qual | QualityManagement | u_mes_qual_controlPlanCoreTeamUser | Master | Control Plan Core Team |
| qual | QualityManagement | u_mes_qual_controlPlanLine | Master | Control Plan Lines |
| qual | QualityManagement | u_mes_qual_inspectionPlan | Master | Inspection Plans |
| qual | QualityManagement | u_mes_qual_inspectionPlanLine | Master | Inspection Plan Lines |
| qual | QualityManagement | u_mes_qual_samplingPlan | Master | Sampling Plans |
| qual | QualityManagement | u_mes_qual_samplingPlanSizeRow | Master | Sampling Plan Sample Size Table |
| qual | QualityManagement | u_mes_qual_checkSheet | Master | Check Sheets |
| qual | QualityManagement | u_mes_qual_checkSheetItem | Master | Check Sheet Items |
| qual | QualityManagement | u_mes_qual_checkSheetResult | Transaction | Check Sheet Results |
| qual | QualityManagement | u_mes_qual_checkSheetResultAnswer | Transaction | Check Sheet Result Answers |
| qual | QualityManagement | u_mes_qual_inspectionResult | Transaction | Inspection Results |
| qual | QualityManagement | u_mes_qual_spcChart | Master | SPC Charts |
| qual | QualityManagement | u_mes_qual_spcChartControlLimit | Master | SPC Chart Control Limits |
| qual | QualityManagement | u_mes_qual_spcChartRule | Master | SPC Chart Rules |
| qual | QualityManagement | u_mes_qual_spcSample | Transaction | SPC Samples |
| qual | QualityManagement | u_mes_qual_spcSampleReading | Transaction | SPC Sample Readings |
| qual | QualityManagement | u_mes_qual_spcSampleInspectionResult | Transaction | SPC Sample Inspection Results |
| qual | QualityManagement | u_mes_qual_spcSampleViolation | Transaction | SPC Sample Violations |
| qual | QualityManagement | u_mes_qual_defectCode | Master | Defect Codes |
| qual | QualityManagement | u_mes_qual_defectCodeApplicableOperation | Master | Defect Code Applicable Operations |
| qual | QualityManagement | u_mes_qual_nonconformance | Transaction | Nonconformances |
| qual | QualityManagement | u_mes_qual_nonconformanceAffectedObject | Transaction | Nonconformance Affected Objects |
| qual | QualityManagement | u_mes_qual_nonconformanceContainmentAction | Transaction | Nonconformance Containment Actions |
| qual | QualityManagement | u_mes_qual_nonconformanceInspectionResult | Transaction | Nonconformance Inspection Results |
| qual | QualityManagement | u_mes_qual_nonconformanceReworkOrder | Transaction | Nonconformance Rework Orders |
| qual | QualityManagement | u_mes_qual_nonconformanceScrapRecord | Transaction | Nonconformance Scrap Records |
| qual | QualityManagement | u_mes_qual_nonconformancePhotoControlledDocument | Transaction | Nonconformance Photos |
| qual | QualityManagement | u_mes_qual_nonconformanceMrbUser | Transaction | Nonconformance MRB Members |
| qual | QualityManagement | u_mes_qual_reworkOrder | Transaction | Rework Orders |
| qual | QualityManagement | u_mes_qual_reworkOrderWipUnit | Transaction | Rework Order WIP Units |
| qual | QualityManagement | u_mes_qual_reworkOrderStep | Transaction | Rework Order Steps |
| qual | QualityManagement | u_mes_qual_scrapRecord | Transaction | Scrap Records |
| qual | QualityManagement | u_mes_qual_qualityHold | Transaction | Quality Holds |
| qual | QualityManagement | u_mes_qual_qualityHoldHeldObject | Transaction | Quality Hold Held Objects |
| qual | QualityManagement | u_mes_qual_deviationPermit | Transaction | Deviation Permits |
| qual | QualityManagement | u_mes_qual_deviationPermitApproval | Transaction | Deviation Permit Approvals |
| qual | QualityManagement | u_mes_qual_capa | Transaction | CAPA (8D) |
| qual | QualityManagement | u_mes_qual_capaNonconformance | Transaction | CAPA Nonconformances |
| qual | QualityManagement | u_mes_qual_capaTeamMember | Transaction | CAPA Team Members |
| qual | QualityManagement | u_mes_qual_capaContainmentAction | Transaction | CAPA Containment Actions |
| qual | QualityManagement | u_mes_qual_capaCorrectiveAction | Transaction | CAPA Corrective Actions |
| qual | QualityManagement | u_mes_qual_capaImplementationAction | Transaction | CAPA Implementation Actions |
| qual | QualityManagement | u_mes_qual_capaControlledDocument | Transaction | CAPA Documents |
| qual | QualityManagement | u_mes_qual_pfmea | Master | Process FMEAs |
| qual | QualityManagement | u_mes_qual_pfmeaCoreTeamUser | Master | PFMEA Core Team |
| qual | QualityManagement | u_mes_qual_pfmeaLine | Master | PFMEA Lines |
| qual | QualityManagement | u_mes_qual_ppapSubmission | Transaction | PPAP Submissions |
| qual | QualityManagement | u_mes_qual_ppapSubmissionElement | Transaction | PPAP Submission Elements |
| qual | QualityManagement | u_mes_qual_ppapSubmissionMsaStudy | Transaction | PPAP Submission MSA Studies |
| qual | QualityManagement | u_mes_qual_gauge | Master | Gauges |
| qual | QualityManagement | u_mes_qual_gaugeCalibration | Transaction | Gauge Calibrations |
| qual | QualityManagement | u_mes_qual_gaugeCalibrationReading | Transaction | Gauge Calibration Readings |
| qual | QualityManagement | u_mes_qual_msaStudy | Transaction | MSA Studies |
| qual | QualityManagement | u_mes_qual_msaStudyAppraiserUser | Transaction | MSA Study Appraisers |
| qual | QualityManagement | u_mes_qual_msaStudyTrial | Transaction | MSA Study Trials |
| qual | QualityManagement | u_mes_qual_audit | Transaction | Audits |
| qual | QualityManagement | u_mes_qual_auditAuditorUser | Transaction | Audit Auditors |
| qual | QualityManagement | u_mes_qual_auditFinding | Transaction | Audit Findings |
| qual | QualityManagement | u_mes_qual_customerComplaint | Transaction | Customer Complaints |
| qual | QualityManagement | u_mes_qual_customerComplaintSerialNumber | Transaction | Customer Complaint Serial Numbers |
| qual | QualityManagement | u_mes_qual_customerComplaintShipment | Transaction | Customer Complaint Shipments |
| qual | QualityManagement | u_mes_qual_customerComplaintSuspectLot | Transaction | Customer Complaint Suspect Lots |
| qual | QualityManagement | u_mes_qual_customerComplaintCommunication | Transaction | Customer Complaint Communications |
| qual | QualityManagement | u_mes_qual_defectGroup | Master | Defect Groups |
| qual | QualityManagement | u_mes_qual_gaugeType | Master | Gauge Types |
| qual | QualityManagement | u_mes_qual_dispositionType | Master | Disposition Types |
| qual | QualityManagement | u_mes_qual_complaintType | Master | Complaint Types |
| qual | QualityManagement | u_mes_qual_characteristicPosition | Master | Characteristic Positions |
| qual | QualityManagement | u_mes_qual_curveEnvelope | Master | Curve Envelopes |
| qual | QualityManagement | u_mes_qual_curveEnvelopeWindow | Master | Curve Envelope Windows |
| qual | QualityManagement | u_mes_qual_measurementCurve | Transaction | Measurement Curves |
| qual | QualityManagement | u_mes_qual_measurementCurvePoint | Telemetry | Measurement Curve Points |
| qual | QualityManagement | u_mes_qual_defectRecord | Transaction | Defect Records |
| qual | QualityManagement | u_mes_qual_auditSchedule | Master | Audit Schedules |
| qual | QualityManagement | u_mes_qual_inspectionPlanProductVariant | Master | Inspection Plan Variants |
| qual | QualityManagement | u_mes_qual_environmentalMonitoringPoint | Master | Environmental Monitoring Points |
| qual | QualityManagement | u_mes_qual_environmentalMonitoringResult | Transaction | Environmental Monitoring Results |
| qual | QualityManagement | u_mes_qual_retentionSample | Transaction | Retention Samples |
| qual | QualityManagement | u_mes_qual_riskAssessment | Transaction | Quality Risk Assessments |
| qual | QualityManagement | u_mes_qual_productQualityReview | Transaction | Product Quality Reviews |
| qual | QualityManagement | u_mes_qual_productRecall | Transaction | Product Recalls |
| qual | QualityManagement | u_mes_qual_productRecallLot | Transaction | Recall Lots |
| qual | QualityManagement | u_mes_qual_processValidation | Transaction | Process Validations |
| perf | PerformanceManagement | u_mes_perf_reasonCode | Master | Reason Codes |
| perf | PerformanceManagement | u_mes_perf_equipmentState | Telemetry | Equipment States |
| perf | PerformanceManagement | u_mes_perf_downtimeEvent | Transaction | Downtime Events |
| perf | PerformanceManagement | u_mes_perf_downtimeEventComment | Transaction | Downtime Event Comments |
| perf | PerformanceManagement | u_mes_perf_productionCount | Reports | Hourly Production Counts |
| perf | PerformanceManagement | u_mes_perf_oeeRecord | Reports | OEE Records |
| perf | PerformanceManagement | u_mes_perf_oeeRecordLoss | Reports | OEE Record Losses |
| perf | PerformanceManagement | u_mes_perf_processTag | Master | Process Tags |
| perf | PerformanceManagement | u_mes_perf_processReading | Telemetry | Process Readings |
| perf | PerformanceManagement | u_mes_perf_alarm | Telemetry | Alarms |
| perf | PerformanceManagement | u_mes_perf_torqueResult | Transaction | Torque Results |
| perf | PerformanceManagement | u_mes_perf_leakTestResult | Transaction | Leak Test Results |
| perf | PerformanceManagement | u_mes_perf_leakTestResultStage | Transaction | Leak Test Result Stages |
| perf | PerformanceManagement | u_mes_perf_energyReading | Telemetry | Energy Readings |
| perf | PerformanceManagement | u_mes_perf_lossCategory | Master | Loss Categories |
| perf | PerformanceManagement | u_mes_perf_reasonCategory | Master | Reason Categories |
| perf | PerformanceManagement | u_mes_perf_energyType | Master | Energy Types |
| perf | PerformanceManagement | u_mes_perf_alarmDefinition | Master | Alarm Definitions |
| perf | PerformanceManagement | u_mes_perf_lossSummary | Reports | Loss Summary |
| perf | PerformanceManagement | u_mes_perf_workCenterPerformance | Reports | Station Performance |
| perf | PerformanceManagement | u_mes_perf_operatorPerformance | Reports | Operator Performance |
| maint | ToolingAndMaintenance | u_mes_maint_maintenancePlan | Master | Maintenance Plans |
| maint | ToolingAndMaintenance | u_mes_maint_maintenancePlanTask | Master | Maintenance Plan Tasks |
| maint | ToolingAndMaintenance | u_mes_maint_maintenancePlanRequiredSkill | Master | Maintenance Plan Required Skills |
| maint | ToolingAndMaintenance | u_mes_maint_maintenancePlanRequiredSparePart | Master | Maintenance Plan Required Spare Parts |
| maint | ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrder | Transaction | Maintenance Work Orders |
| maint | ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrderAssignedToUser | Transaction | Maintenance Work Order Assignees |
| maint | ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrderLabour | Transaction | Maintenance Work Order Labour |
| maint | ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrderUsedSparePart | Transaction | Maintenance Work Order Used Spare Parts |
| maint | ToolingAndMaintenance | u_mes_maint_sparePart | Master | Spare Parts |
| maint | ToolingAndMaintenance | u_mes_maint_sparePartUsedOnEquipment | Master | Spare Part Used on Equipment |
| maint | ToolingAndMaintenance | u_mes_maint_tool | Master | Tools |
| maint | ToolingAndMaintenance | u_mes_maint_toolItem | Master | Tool Applicable Items |
| maint | ToolingAndMaintenance | u_mes_maint_toolLifeRecord | Transaction | Tool Life Records |
| maint | ToolingAndMaintenance | u_mes_maint_toolType | Master | Tool Types |
| maint | ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrderTask | Transaction | Work Order Checklist |
| maint | ToolingAndMaintenance | u_mes_maint_sparePartTransaction | Transaction | Spare Part Transactions |
| maint | ToolingAndMaintenance | u_mes_maint_reliabilitySummary | Reports | Reliability Summary |
| maint | ToolingAndMaintenance | u_mes_maint_equipmentLifecycleEvent | Transaction | Equipment Lifecycle |
| maint | ToolingAndMaintenance | u_mes_maint_logbookEntry | Transaction | Equipment and Area Logbook |
| maint | ToolingAndMaintenance | u_mes_maint_cleaningRecord | Transaction | Cleaning Records |
| maint | ToolingAndMaintenance | u_mes_maint_equipmentQualification | Transaction | Equipment Qualifications |
| syst | SystemAndIntegration | u_mes_syst_erpMessage | Transaction | ERP Messages |
| syst | SystemAndIntegration | u_mes_syst_integrationConnector | Master | Integration Connectors |
| syst | SystemAndIntegration | u_mes_syst_integrationConnectorFunction | Master | Integration Connector Functions |
| syst | SystemAndIntegration | u_mes_syst_iotDevice | Master | IoT Devices |
| syst | SystemAndIntegration | u_mes_syst_operatorApp | Master | Operator Apps |
| syst | SystemAndIntegration | u_mes_syst_operatorAppWorkCenter | Master | Operator App Work Centers |
| syst | SystemAndIntegration | u_mes_syst_operatorAppOperation | Master | Operator App Operations |
| syst | SystemAndIntegration | u_mes_syst_operatorAppStep | Master | Operator App Steps |
| syst | SystemAndIntegration | u_mes_syst_operatorAppStepTrigger | Master | Operator App Step Triggers |
| syst | SystemAndIntegration | u_mes_syst_operatorAppDeviceBinding | Master | Operator App Device Bindings |
| syst | SystemAndIntegration | u_mes_syst_operatorAppLanguage | Master | Operator App Languages |
| syst | SystemAndIntegration | u_mes_syst_businessEvent | Audit Trail | Business Events |
| syst | SystemAndIntegration | u_mes_syst_auditTrail | Audit Trail | Audit Trail |
| syst | SystemAndIntegration | u_mes_syst_auditTrailChange | Audit Trail | Audit Trail Changes |
| syst | SystemAndIntegration | u_mes_syst_electronicSignature | Audit Trail | Electronic Signatures |
| syst | SystemAndIntegration | u_mes_syst_notification | Transaction | Notifications |
| syst | SystemAndIntegration | u_mes_syst_notificationRecipient | Transaction | Notification Recipients |
| syst | SystemAndIntegration | u_mes_syst_controlledDocument | Transaction | Controlled Documents |
| syst | SystemAndIntegration | u_mes_syst_controlledDocumentTag | Transaction | Controlled Document Tags |
| syst | SystemAndIntegration | u_mes_syst_numberRange | Master | Number Ranges |
| syst | SystemAndIntegration | u_mes_syst_systemConfiguration | Master | System Configurations |
| syst | SystemAndIntegration | u_mes_syst_documentType | Master | Document Types |
| syst | SystemAndIntegration | u_mes_syst_deviceType | Master | Device Types |
| syst | SystemAndIntegration | u_mes_syst_notificationType | Master | Notification Types |
| syst | SystemAndIntegration | u_mes_syst_statusDefinition | Master | Status Definitions |
| syst | SystemAndIntegration | u_mes_syst_enumerationValue | Master | Enumeration Values |
| syst | SystemAndIntegration | u_mes_syst_statusTransition | Master | Status Transitions |
| syst | SystemAndIntegration | u_mes_syst_interlockRule | Master | Interlock Rules |
| syst | SystemAndIntegration | u_mes_syst_statusTransitionRole | Master | Status Transition Roles |
| syst | SystemAndIntegration | u_mes_syst_escalationRule | Master | Escalation Rules |
| syst | SystemAndIntegration | u_mes_syst_escalationRuleLevel | Master | Escalation Levels |
| syst | SystemAndIntegration | u_mes_syst_alertRule | Master | Alert Rules |
| syst | SystemAndIntegration | u_mes_syst_analyticsModel | Master | Analytics Models |
| syst | SystemAndIntegration | u_mes_syst_modelPrediction | Transaction | Model Predictions |
| syst | SystemAndIntegration | u_mes_syst_simulationStudy | Transaction | Simulation Studies |
| syst | SystemAndIntegration | u_mes_syst_recordPolicy | Master | Record Policies |
| syst | SystemAndIntegration | u_mes_syst_savedView | Master | Saved Views |
| syst | SystemAndIntegration | u_mes_syst_backupRun | Transaction | Backup and Restore Runs |
| syst | SystemAndIntegration | u_mes_syst_computerisedSystem | Master | Computerised Systems |
| syst | SystemAndIntegration | u_mes_syst_systemValidation | Transaction | System Validations |
| syst | SystemAndIntegration | u_mes_syst_systemPeriodicReview | Transaction | System Periodic Reviews |
| syst | SystemAndIntegration | u_mes_syst_auditTrailReview | Transaction | Audit Trail Reviews |
| syst | SystemAndIntegration | u_mes_syst_userAccessReview | Transaction | User Access Reviews |
| syst | SystemAndIntegration | u_mes_syst_userAccessReviewLine | Transaction | User Access Review Lines |
| syst | SystemAndIntegration | u_mes_syst_unsMessageType | Master | UNS Message Types |
| syst | SystemAndIntegration | u_mes_syst_iotHubIdentity | Master | IoT Hub Identities |
| syst | SystemAndIntegration | u_mes_syst_unsRejectedMessage | Transaction | UNS Rejected Messages |
| ehs | EnvironmentHealthAndSafety | u_mes_ehs_safetyIncident | Transaction | Safety Incidents |
| ehs | EnvironmentHealthAndSafety | u_mes_ehs_safetyIncidentWitnessUser | Transaction | Safety Incident Witnesses |
| ehs | EnvironmentHealthAndSafety | u_mes_ehs_safetyIncidentAction | Transaction | Safety Incident Actions |
| ehs | EnvironmentHealthAndSafety | u_mes_ehs_incidentType | Master | Incident Types |
| ehs | EnvironmentHealthAndSafety | u_mes_ehs_bodyPart | Master | Body Parts |
| ehs | EnvironmentHealthAndSafety | u_mes_ehs_injuryType | Master | Injury Types |
| bmr | BatchManufacturingRecord | u_mes_bmr_batchRecordReview | Transaction | Batch Record Reviews |
| bmr | BatchManufacturingRecord | u_mes_bmr_batchRecordReviewException | Transaction | Batch Record Review Exceptions |
| bmr | BatchManufacturingRecord | u_mes_bmr_batchRelease | Transaction | Batch Releases |
| bmr | BatchManufacturingRecord | u_mes_bmr_yieldReconciliation | Transaction | Yield and Reconciliation |
| bmr | BatchManufacturingRecord | u_mes_bmr_batchManufacturingRecord | Transaction | Batch Manufacturing Records |
| mmr | MasterManufacturingRecord | u_mes_mmr_masterManufacturingRecord | Master | Master Manufacturing Records |
| mmr | MasterManufacturingRecord | u_mes_mmr_masterManufacturingRecordRecipe | Master | Master Record Recipes |
