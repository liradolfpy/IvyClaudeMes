# Fixed enumeration values

Keys whose values are fixed by the application logic stay coded text (data_modeling_standard.md section 11, rule B). Their allowed values are listed here, enforced by the validators, and stored as data in `u_mes_syst_enumerationValue` (one document per collection, key and value). Status values are in status_values.md.

Keys: 677 | Values: 2514

| Module | Collection | Key | Allowed values |
|---|---|---|---|
| MasterDataManagement | u_mes_mast_enterprise | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_enterprise | scope | Enterprise; Site |
| MasterDataManagement | u_mes_mast_enterpriseContact | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_site | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_site | siteType | Manufacturing Plant; Warehouse; Technical Center; Head Office |
| MasterDataManagement | u_mes_mast_siteCertificate | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_area | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_area | areaType | Production; Storage; Quality; Maintenance; Utility |
| MasterDataManagement | u_mes_mast_area | cleanlinessClass | ISO 7; ISO 8; Controlled Not Classified; Unclassified |
| MasterDataManagement | u_mes_mast_line | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_line | lineType | Casting; Heat Treatment; Machining; Surface Treatment; Assembly; Inspection; Packing; Dispensing; Granulation; Compression; Coating; Primary Packing; Secondary Packing |
| MasterDataManagement | u_mes_mast_lineDefaultShift | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_lineIdealRate | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_workCenter | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_workCenter | workCenterType | Machine Station; Manual Station; Test Station; Inspection Station; Batch Process |
| MasterDataManagement | u_mes_mast_workCenter | trackingGrain | Lot; Unit; Container |
| MasterDataManagement | u_mes_mast_workCenterEquipment | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_workCenterOperation | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_workCenterRequiresSkill | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_equipment | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_equipment | equipmentClass | Production Equipment; Test Equipment; Measuring Equipment; Utility |
| MasterDataManagement | u_mes_mast_equipment | controllerProtocol | OPC UA; Open Protocol; Modbus TCP; Profinet; MQTT; Ethernet/IP |
| MasterDataManagement | u_mes_mast_equipment | criticality | A; B; C |
| MasterDataManagement | u_mes_mast_equipment | currentState | Running; Idle; Setup; Down; Starved; Blocked; Planned Stop |
| MasterDataManagement | u_mes_mast_equipment | safetyCategory | PL a; PL b; PL c; PL d; PL e |
| MasterDataManagement | u_mes_mast_equipment | qualificationStatus | Qualified; Not Qualified; Requalification Due |
| MasterDataManagement | u_mes_mast_equipment | cleanStatus | Clean; Dirty; In Cleaning; Clean Hold Expired; Not Applicable |
| MasterDataManagement | u_mes_mast_equipmentIotDevice | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_shift | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_shiftBreak | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_shiftWorkingDay | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_shiftWorkingDay | workingDay | Monday; Tuesday; Wednesday; Thursday; Friday; Saturday; Sunday |
| MasterDataManagement | u_mes_mast_workCalendar | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_workCalendarLine | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_workCalendarShift | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_workCalendarWeeklyOffDay | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_workCalendarWeeklyOffDay | weeklyOffDay | Monday; Tuesday; Wednesday; Thursday; Friday; Saturday; Sunday |
| MasterDataManagement | u_mes_mast_workCalendarException | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_workCalendarException | exceptionType | Public Holiday; Plant Shutdown; Extra Working Day; Reduced Shift |
| MasterDataManagement | u_mes_mast_workCalendarExceptionShift | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_shiftRoster | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_shiftRosterAssignment | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_shiftRosterAssignment | roleInCrew | Operator; Setter; Line Leader; Quality Inspector; Material Handler |
| MasterDataManagement | u_mes_mast_shiftRosterAssignment | attendance | Present; Absent; Leave; Overtime |
| MasterDataManagement | u_mes_mast_shiftRosterAssignment | assignmentSource | Manual; Rule; Model |
| MasterDataManagement | u_mes_mast_role | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_role | scope | Enterprise; Site |
| MasterDataManagement | u_mes_mast_rolePermission | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_roleSignatureMeaning | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_user | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_user | userType | Employee; Contractor; System |
| MasterDataManagement | u_mes_mast_userRole | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_skill | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_skill | assessmentMethod | Practical Test; Written Test; Observation; On the Job |
| MasterDataManagement | u_mes_mast_skillOperation | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_skillLevelScale | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_skillCertification | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_skillCertification | assessmentMethod | Practical Test; Written Test; Observation; On the Job |
| MasterDataManagement | u_mes_mast_skillCertification | revocationSource | Expiry; Document Revision; Manual; Assessment Failure |
| MasterDataManagement | u_mes_mast_customer | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_customer | customerType | OEM; Tier 1; Aftermarket; Distributor; Hospital; Institutional; Export |
| MasterDataManagement | u_mes_mast_customerShipTo | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_customerContact | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_customerContact | businessFunction | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| MasterDataManagement | u_mes_mast_supplier | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_supplier | supplierType | Direct Material; Indirect Material; Tooling; Service; Calibration Laboratory |
| MasterDataManagement | u_mes_mast_supplierContact | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_supplierContact | businessFunction | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| MasterDataManagement | u_mes_mast_supplierCertificate | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_supplierSuppliedItem | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_supplierSuppliedItem | qualificationStatus | Qualified; Conditionally Approved; Disqualified |
| MasterDataManagement | u_mes_mast_unitOfMeasure | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_unitOfMeasure | scope | Enterprise; Site |
| MasterDataManagement | u_mes_mast_unitOfMeasure | dimension | Count; Mass; Length; Torque; Pressure; Temperature; Time; Energy; Volume; Hardness; Leak Rate; Ratio; Force |
| MasterDataManagement | u_mes_mast_department | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_designation | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_employmentType | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_costCenter | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_manufacturer | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_equipmentType | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_skillCategory | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_permission | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_signatureMeaning | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_currency | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_country | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_language | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_transporter | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_commodity | app | Auto; Gamp; Common |
| MasterDataManagement | u_mes_mast_roleRequiredSkill | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_item | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_item | itemType | Finished Good; Semi Finished; Purchased Component; Raw Material; Consumable; Packaging |
| ProductDefinition | u_mes_prod_item | procurementType | In House; Purchased; Subcontracted |
| ProductDefinition | u_mes_prod_itemRevision | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_itemCustomerPart | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_productVariant | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_productVariant | optionsHand | LH; RH |
| ProductDefinition | u_mes_prod_billOfMaterial | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_billOfMaterial | bomType | Production; Engineering; Rework |
| ProductDefinition | u_mes_prod_billOfMaterialComponent | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_billOfMaterialComponent | traceLevel | None; Lot; Serial |
| ProductDefinition | u_mes_prod_billOfMaterialComponentProductVariant | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_billOfMaterialComponentAlternateItem | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_operation | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_operation | operationType | Casting; Heat Treatment; Machining; Cleaning; Surface Treatment; Assembly; Test; Marking; Inspection; Packing; Dispensing; Granulation; Drying; Blending; Compression; Coating |
| ProductDefinition | u_mes_prod_operation | trackingGrain | Lot; Unit; Container |
| ProductDefinition | u_mes_prod_operationRequiredSkill | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_routing | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_routing | routingType | Standard; Rework; Alternate |
| ProductDefinition | u_mes_prod_routingStep | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_routingStepAlternateWorkCenter | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_routingStepNextStep | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_routingStepNextStep | nextStepCondition | Result OK; Result Not OK; Rework Complete; Always |
| ProductDefinition | u_mes_prod_billOfProcess | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_billOfProcessStep | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_billOfProcessStepEquipment | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_billOfProcessStepTool | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_billOfProcessStepRequiredSkill | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_billOfProcessStepConsumedComponent | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_billOfProcessStepInterlock | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_billOfProcessStepInterlock | interlockType | Skill; Recipe; Tool Life; Gauge Calibration; Previous Step; Component Scan; Maintenance Due |
| ProductDefinition | u_mes_prod_billOfProcessStepProcessParameter | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_workInstruction | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_workInstruction | generationSource | Manual; Generated From Bill Of Process; Generated By Model |
| ProductDefinition | u_mes_prod_workInstructionStep | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_workInstructionStep | inputType | None; Confirmation; Number; Text; Scan; Photo; Device Value |
| ProductDefinition | u_mes_prod_workInstructionStepMediaControlledDocument | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_workInstructionStepProductVariant | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_workInstructionStepTool | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_workInstructionStepCharacteristic | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_workInstructionPpeItem | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_workInstructionKeyPoint | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_recipe | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_recipe | recipeType | Die Casting Parameters; Furnace Profile; CNC Program; Washing Program; Anodising Program; Tightening Program; Leak Test Program; Laser Marking Program; Press Program; Dispensing Program; Vision Job; Granulation Program; Drying Program; Blending Program; Compression Program; Coating Program; Capping Program; Blister Program; Serialisation Program; Cartoning Program |
| ProductDefinition | u_mes_prod_recipe | origin | Engineering; Optimisation Model; Simulation Study |
| ProductDefinition | u_mes_prod_recipeParameter | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_recipeStage | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_engineeringChange | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_engineeringChange | changeType | Design Change; Process Change; Material Change; Supplier Change; Tooling Change; Document Change |
| ProductDefinition | u_mes_prod_engineeringChange | originator | Customer; Internal; Supplier |
| ProductDefinition | u_mes_prod_engineeringChange | effectivityType | Date; Serial Number; Lot; Stock Run Out |
| ProductDefinition | u_mes_prod_engineeringChange | regulatoryImpact | None; Customer Notification; Prior Approval |
| ProductDefinition | u_mes_prod_engineeringChangeAffectedItem | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_engineeringChangeAffectedObject | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_engineeringChangeAffectedObject | changeAction | Create; Update; Obsolete |
| ProductDefinition | u_mes_prod_engineeringChangeApproval | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_engineeringChangeApproval | businessFunction | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| ProductDefinition | u_mes_prod_engineeringChangeApproval | decision | Approved; Rejected; Approved With Conditions |
| ProductDefinition | u_mes_prod_engineeringChangeControlledDocument | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_itemGroup | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_itemFamily | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_ppeItem | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_market | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_padCompound | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_surfaceFinish | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_vehicleModel | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_recipeProductVariant | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_recipeControlledDocument | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_recipeControlledDocument | fileRole | Program File; Golden Image; Reference Curve; Parameter Export; Process Specification; Product Drawing; Verification Record |
| ProductDefinition | u_mes_prod_workInstructionWorkCenter | app | Auto; Gamp; Common |
| ProductDefinition | u_mes_prod_workInstructionProductVariant | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_customerSchedule | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_customerSchedule | scheduleType | Forecast; Delivery Schedule; Just In Time Call Off |
| PlanningAndExecution | u_mes_plan_customerScheduleLine | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_customerScheduleLine | firmness | Firm; Forecast |
| PlanningAndExecution | u_mes_plan_productionOrder | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_productionOrder | orderType | Production; Rework; Trial; PPAP Run; Validation Batch |
| PlanningAndExecution | u_mes_plan_productionOrder | priority | Low; Normal; High; Urgent |
| PlanningAndExecution | u_mes_plan_productionOrderRelease | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_productionOrderLot | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_productionSchedule | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_productionScheduleSlot | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_dispatchList | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_dispatchList | rule | Earliest Due Date; First In First Out; Critical Ratio; Priority |
| PlanningAndExecution | u_mes_plan_dispatchListEntry | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_dispatchListEntry | priority | Low; Normal; High; Urgent |
| PlanningAndExecution | u_mes_plan_operationExecution | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_operationExecution | executionType | Production; Rework; Retest; Setup |
| PlanningAndExecution | u_mes_plan_operationExecution | result | OK; Not OK |
| PlanningAndExecution | u_mes_plan_operationExecution | captureMethod | Scan; PLC Signal; Manual Entry |
| PlanningAndExecution | u_mes_plan_operationExecutionDefectCode | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_operationExecutionTool | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_stepCompletion | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_stepCompletion | inputType | None; Confirmation; Number; Text; Scan; Photo; Device Value |
| PlanningAndExecution | u_mes_plan_stepCompletion | deviceSource | Manual Entry; Scanner; Nutrunner Controller; Leak Tester; Gauge Interface; PLC; AR Headset |
| PlanningAndExecution | u_mes_plan_wipUnit | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_wipUnit | qualityStatus | Released; Under Inspection; On Hold; Rejected |
| PlanningAndExecution | u_mes_plan_wipUnitCompletedStep | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_lot | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_lot | lotType | Supplier Lot; Melt Lot; Casting Lot; Heat Treatment Charge; Machining Lot; Anodising Load; Finished Goods Lot; Granulation Lot; Coated Tablet Lot |
| PlanningAndExecution | u_mes_plan_lot | qualityStatus | Released; Under Inspection; On Hold; Rejected |
| PlanningAndExecution | u_mes_plan_lotParentLot | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_lotAttributesCavityNo | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_container | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_containerLot | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_labourBooking | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_labourBooking | bookingType | Direct; Indirect |
| PlanningAndExecution | u_mes_plan_labourBooking | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| PlanningAndExecution | u_mes_plan_changeover | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_changeover | changeoverType | Variant Change; Item Change; Tool Change; Die Change; Batch Change; Product Change |
| PlanningAndExecution | u_mes_plan_changeoverStep | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_changeoverStep | internalExternal | Internal; External |
| PlanningAndExecution | u_mes_plan_changeoverRemovedTool | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_changeoverInstalledTool | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_changeoverPerformedByUser | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_shiftHandover | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_shiftHandoverProductionOrder | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_shiftHandoverDowntimeEvent | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_shiftHandoverNonconformance | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_shiftHandoverOpenItem | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_andonEvent | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_andonEvent | severityClass | Low; Medium; High; Critical |
| PlanningAndExecution | u_mes_plan_andonEventEscalation | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_andonEventEscalation | channel | Screen; Email; SMS; Mobile Push |
| PlanningAndExecution | u_mes_plan_indirectActivity | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_containerType | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_andonType | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_operatorSession | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_operatorSession | authenticationMethod | Badge; Biometric; Badge And PIN; Password |
| PlanningAndExecution | u_mes_plan_operatorSession | logoutReason | Operator Logout; Shift End; Timeout; Supervisor Logout; Skill Revoked |
| PlanningAndExecution | u_mes_plan_documentAcknowledgement | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_documentAcknowledgement | relatedCollectionName | u_mes_prod_workInstruction; u_mes_prod_recipe; u_mes_syst_controlledDocument |
| PlanningAndExecution | u_mes_plan_documentAcknowledgement | acknowledgementType | First Read; Revision Re-acknowledgement; Shift Start; Periodic Refresh |
| PlanningAndExecution | u_mes_plan_documentAcknowledgement | method | Touch Confirmation; Badge Scan; AR Confirmation; Electronic Signature |
| PlanningAndExecution | u_mes_plan_interlockEvent | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_recipeDownload | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_recipeDownload | trigger | Order Start; Changeover; Operator Request; Revision Release; Controller Reconnect |
| PlanningAndExecution | u_mes_plan_recipeDownload | verificationResult | Match; Mismatch; No Response; Version Not Released |
| PlanningAndExecution | u_mes_plan_setupVerification | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_setupVerification | trigger | Order Start; Changeover; Shift Start; After Maintenance |
| PlanningAndExecution | u_mes_plan_setupVerificationItem | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_setupVerificationItem | checkType | Variant; Fixture; Tool; Program; Parameter; Component; Gauge |
| PlanningAndExecution | u_mes_plan_lineClearance | app | Auto; Gamp; Common |
| PlanningAndExecution | u_mes_plan_lineClearance | clearanceType | Before Order Start; Order Changeover; After Order Completion; After Maintenance |
| MaterialManagement | u_mes_matl_storageLocation | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_storageLocation | locationType | Warehouse Rack; Line Side; Quarantine; Dispatch Bay; Receiving Bay; Tool Crib; Scrap Yard |
| MaterialManagement | u_mes_matl_inventoryBalance | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_materialMovement | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_materialMovement | scanSource | Handheld Scanner; Fixed Scanner; Manual Entry |
| MaterialManagement | u_mes_matl_goodsReceipt | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_goodsReceiptLine | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_goodsReceiptLine | inspectionStatus | Pending; Accepted; Rejected; Accepted Under Deviation |
| MaterialManagement | u_mes_matl_goodsReceiptLineInspectionResult | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_kit | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_kit | kitType | Order Kit; Shift Kit; Rework Kit |
| MaterialManagement | u_mes_matl_kitLine | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_kitLine | verificationResult | Match; Wrong Item; Wrong Revision; Wrong Quantity; Not Scanned |
| MaterialManagement | u_mes_matl_materialRequest | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_materialRequest | requestType | Kanban; Andon Call; Manual |
| MaterialManagement | u_mes_matl_materialRequest | triggerSource | Minimum Level Sensor; Operator; Schedule |
| MaterialManagement | u_mes_matl_materialRequest | priority | Low; Normal; High; Urgent |
| MaterialManagement | u_mes_matl_materialConsumption | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_materialConsumption | consumptionType | Scanned; Backflush; Manual |
| MaterialManagement | u_mes_matl_packagingSpecification | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_packagingSpecificationLevel | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_labelTemplate | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_labelTemplate | labelType | Unit Mark; Container Label; Shipping Label; Hold Tag; Location Label |
| MaterialManagement | u_mes_matl_labelTemplate | printerLanguage | ZPL; EPL; PDF |
| MaterialManagement | u_mes_matl_labelTemplate | symbology | Data Matrix ECC200; QR Code; Code 128; Code 39; PDF417 |
| MaterialManagement | u_mes_matl_labelTemplateField | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_labelTemplateField | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| MaterialManagement | u_mes_matl_label | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_label | labelType | Unit Mark; Container Label; Shipping Label; Hold Tag; Location Label |
| MaterialManagement | u_mes_matl_label | verificationGrade | A; B; C; D; F |
| MaterialManagement | u_mes_matl_shipment | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_shipmentLine | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_shipmentLineContainer | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_shipmentLineLot | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_movementType | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_movementType | stockEffect | Increase; Decrease; Transfer; None |
| MaterialManagement | u_mes_matl_stockStatus | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_packType | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_exposureTimer | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_exposureTimer | timerType | Floor Life; Pot Life; Open Time; Bake; Dirty Equipment Hold; Clean Equipment Hold; Process Hold Time |
| MaterialManagement | u_mes_matl_replenishmentRule | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_replenishmentRule | triggerType | Consumption; Kanban Scan; Min-Max; Order Demand |
| MaterialManagement | u_mes_matl_materialDemandForecast | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_materialDemandForecast | method | Schedule; Consumption Rate; Model |
| MaterialManagement | u_mes_matl_storageLocationAllowedItem | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_dispenseRecord | app | Auto; Gamp; Common |
| MaterialManagement | u_mes_matl_dispenseRecord | dispenseMethod | Gravimetric Weighing; Count By Weight |
| MaterialManagement | u_mes_matl_dispenseRecord | verificationMethod | Second Person; System Check |
| Traceability | u_mes_trac_serialNumber | app | Auto; Gamp; Common |
| Traceability | u_mes_trac_serialNumber | markGrade | A; B; C; D; F |
| Traceability | u_mes_trac_genealogyLink | app | Auto; Gamp; Common |
| Traceability | u_mes_trac_genealogyLink | childType | Lot; Serial |
| Traceability | u_mes_trac_genealogyLink | linkType | Assembled; Replaced; Split; Merge; Transformed |
| Traceability | u_mes_trac_componentLotLink | app | Auto; Gamp; Common |
| Traceability | u_mes_trac_componentLotLink | linkType | Assembled; Replaced; Split; Merge; Transformed |
| Traceability | u_mes_trac_asBuiltRecord | app | Auto; Gamp; Common |
| Traceability | u_mes_trac_asBuiltRecord | leakTestVerdict | Pass; Fail |
| Traceability | u_mes_trac_asBuiltRecordComponent | app | Auto; Gamp; Common |
| Traceability | u_mes_trac_asBuiltRecordOperation | app | Auto; Gamp; Common |
| Traceability | u_mes_trac_asBuiltRecordOperation | result | OK; Not OK |
| Traceability | u_mes_trac_asBuiltRecordInspectionResult | app | Auto; Gamp; Common |
| Traceability | u_mes_trac_traceInvestigation | app | Auto; Gamp; Common |
| Traceability | u_mes_trac_traceInvestigation | direction | Forward; Reverse; Both |
| Traceability | u_mes_trac_traceInvestigation | relatedCollectionName | u_mes_trac_serialNumber; u_mes_plan_lot; u_mes_plan_wipUnit; u_mes_plan_container; u_mes_matl_shipment |
| Traceability | u_mes_trac_traceInvestigationResult | app | Auto; Gamp; Common |
| Traceability | u_mes_trac_traceInvestigationResult | relatedCollectionName | u_mes_trac_serialNumber; u_mes_plan_lot; u_mes_plan_wipUnit; u_mes_plan_container; u_mes_matl_shipment |
| QualityManagement | u_mes_qual_characteristic | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_characteristic | characteristicType | Product; Process |
| QualityManagement | u_mes_qual_characteristic | classification | Critical; Significant; Standard |
| QualityManagement | u_mes_qual_characteristic | dataType | Variable; Attribute |
| QualityManagement | u_mes_qual_characteristic | toleranceType | Bilateral; Unilateral Upper; Unilateral Lower |
| QualityManagement | u_mes_qual_characteristic | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| QualityManagement | u_mes_qual_controlPlan | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_controlPlan | phase | Prototype; Pre Launch; Production |
| QualityManagement | u_mes_qual_controlPlanCoreTeamUser | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_controlPlanLine | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_controlPlanLine | classification | Critical; Significant; Standard |
| QualityManagement | u_mes_qual_inspectionPlan | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_inspectionPlan | planType | Incoming; In Process; First Off; Final; Dock Audit; Layout |
| QualityManagement | u_mes_qual_inspectionPlan | collectionTrigger | Operation Start; Operation Complete; Time Interval; Unit Count; Goods Receipt; Changeover |
| QualityManagement | u_mes_qual_inspectionPlanLine | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_inspectionPlanLine | frequencyType | Every Unit; Every N Units; Every N Minutes; Per Lot; Per Shift; First Off |
| QualityManagement | u_mes_qual_inspectionPlanLine | recordType | Measured Value; Pass Fail; Count |
| QualityManagement | u_mes_qual_samplingPlan | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_samplingPlan | samplingType | Attribute AQL; Fixed Sample; Hundred Percent; Skip Lot |
| QualityManagement | u_mes_qual_samplingPlan | inspectionLevel | S-1; S-2; S-3; S-4; I; II; III |
| QualityManagement | u_mes_qual_samplingPlan | frequencyType | Every Unit; Every N Units; Every N Minutes; Per Lot; Per Shift; First Off |
| QualityManagement | u_mes_qual_samplingPlanSizeRow | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_checkSheet | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_checkSheet | checkSheetType | Start Of Shift; Poka Yoke Verification; First Off Approval; Autonomous Maintenance; Layered Process Audit; Changeover |
| QualityManagement | u_mes_qual_checkSheet | frequency | Per Shift; Daily; Weekly; Per Changeover; Per Lot |
| QualityManagement | u_mes_qual_checkSheetItem | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_checkSheetItem | answerType | Yes No; Number; Text |
| QualityManagement | u_mes_qual_checkSheetResult | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_checkSheetResult | overallResult | Pass; Fail |
| QualityManagement | u_mes_qual_checkSheetResultAnswer | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_inspectionResult | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_inspectionResult | inspectionType | Incoming; In Process; First Off; Final; Audit |
| QualityManagement | u_mes_qual_inspectionResult | attributeResult | Pass; Fail |
| QualityManagement | u_mes_qual_inspectionResult | result | OK; Not OK |
| QualityManagement | u_mes_qual_inspectionResult | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| QualityManagement | u_mes_qual_spcChart | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_spcChart | chartType | X-bar R; X-bar S; I-MR; p; np; c; u |
| QualityManagement | u_mes_qual_spcChartControlLimit | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_spcChartRule | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_spcChartRule | rule | Earliest Due Date; First In First Out; Critical Ratio; Priority |
| QualityManagement | u_mes_qual_spcSample | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_spcSample | reactionType | Alert; Hold; Recheck; Stop Line |
| QualityManagement | u_mes_qual_spcSampleReading | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_spcSampleInspectionResult | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_spcSampleViolation | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_spcSampleViolation | rule | Earliest Due Date; First In First Out; Critical Ratio; Priority |
| QualityManagement | u_mes_qual_defectCode | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_defectCode | scrapCostCategory | Casting Scrap; Machining Scrap; Assembly Scrap; Supplier Chargeable; Manufacturing Scrap; Packing Scrap |
| QualityManagement | u_mes_qual_defectCodeApplicableOperation | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_nonconformance | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_nonconformance | ncType | Internal; Supplier; Customer |
| QualityManagement | u_mes_qual_nonconformance | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| QualityManagement | u_mes_qual_nonconformance | deviationClass | Minor; Major; Critical |
| QualityManagement | u_mes_qual_nonconformanceAffectedObject | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_nonconformanceContainmentAction | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_nonconformanceInspectionResult | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_nonconformanceReworkOrder | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_nonconformanceScrapRecord | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_nonconformancePhotoControlledDocument | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_nonconformanceMrbUser | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_reworkOrder | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_reworkOrder | reworkType | Replace Component; Retighten; Re-machine; Re-anodise; Re-mark; Clean; Repack; Reprocess |
| QualityManagement | u_mes_qual_reworkOrder | reinspectionResult | Pass; Fail |
| QualityManagement | u_mes_qual_reworkOrderWipUnit | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_reworkOrderStep | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_scrapRecord | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_scrapRecord | scrapType | Process Scrap; Setup Scrap; Material Defect; Destructive Test |
| QualityManagement | u_mes_qual_scrapRecord | disposalMethod | Remelt; Sell As Scrap; Return To Supplier; Incineration |
| QualityManagement | u_mes_qual_qualityHold | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_qualityHold | holdType | Quality; Customer; Engineering; Supplier |
| QualityManagement | u_mes_qual_qualityHold | releaseDecision | Released; Rework; Scrap; Return To Supplier |
| QualityManagement | u_mes_qual_qualityHoldHeldObject | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_qualityHoldHeldObject | releaseDecision | Released; Rework; Scrap; Return To Supplier |
| QualityManagement | u_mes_qual_deviationPermit | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_deviationPermit | deviationType | Product; Process; Material |
| QualityManagement | u_mes_qual_deviationPermit | limitType | Quantity; Date |
| QualityManagement | u_mes_qual_deviationPermitApproval | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_deviationPermitApproval | businessFunction | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| QualityManagement | u_mes_qual_deviationPermitApproval | decision | Approved; Rejected; Approved With Conditions |
| QualityManagement | u_mes_qual_capa | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_capa | capaType | Corrective; Preventive |
| QualityManagement | u_mes_qual_capa | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| QualityManagement | u_mes_qual_capa | d4RootCauseMethod | 5 Why; Fishbone; Fault Tree; Is Is Not |
| QualityManagement | u_mes_qual_capa | currentDiscipline | D1; D2; D3; D4; D5; D6; D7; D8 |
| QualityManagement | u_mes_qual_capaNonconformance | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_capaTeamMember | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_capaTeamMember | roleInTeam | Champion; Leader; Member |
| QualityManagement | u_mes_qual_capaContainmentAction | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_capaCorrectiveAction | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_capaImplementationAction | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_capaControlledDocument | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_pfmea | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_pfmea | methodology | AIAG-VDA; AIAG 4th Edition |
| QualityManagement | u_mes_qual_pfmeaCoreTeamUser | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_pfmeaLine | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_pfmeaLine | classification | Critical; Significant; Standard |
| QualityManagement | u_mes_qual_pfmeaLine | actionPriority | High; Medium; Low |
| QualityManagement | u_mes_qual_ppapSubmission | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_ppapSubmission | submissionReason | Initial Submission; Engineering Change; Tooling Transfer; Correction Of Discrepancy; Tooling Inactive Over One Year; Sub Supplier Change |
| QualityManagement | u_mes_qual_ppapSubmission | customerDecision | Approved; Interim Approved; Rejected |
| QualityManagement | u_mes_qual_ppapSubmissionElement | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_ppapSubmissionMsaStudy | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_gauge | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_gauge | calibrationSource | Internal; External |
| QualityManagement | u_mes_qual_gaugeCalibration | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_gaugeCalibration | calibrationType | Initial; Periodic; After Repair; After Shock Or Damage; Automatic Closed Loop; Daily Performance Check |
| QualityManagement | u_mes_qual_gaugeCalibration | asFoundResult | Within Tolerance; Out Of Tolerance |
| QualityManagement | u_mes_qual_gaugeCalibration | asLeftResult | Within Tolerance; Out Of Tolerance |
| QualityManagement | u_mes_qual_gaugeCalibration | overallResult | Pass; Fail |
| QualityManagement | u_mes_qual_gaugeCalibrationReading | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_msaStudy | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_msaStudy | studyType | Gauge R and R; Bias; Linearity; Stability; Attribute Agreement |
| QualityManagement | u_mes_qual_msaStudy | studyMethod | ANOVA; Average And Range; Kappa |
| QualityManagement | u_mes_qual_msaStudy | conclusion | Acceptable; Conditionally Acceptable; Not Acceptable |
| QualityManagement | u_mes_qual_msaStudyAppraiserUser | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_msaStudyTrial | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_audit | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_audit | auditType | Layered Process Audit; Process Audit; Product Audit; System Audit; Customer Audit; Supplier Audit |
| QualityManagement | u_mes_qual_audit | overallRating | A; B; C |
| QualityManagement | u_mes_qual_auditAuditorUser | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_auditFinding | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_auditFinding | grade | Major; Minor; Observation; Opportunity For Improvement |
| QualityManagement | u_mes_qual_customerComplaint | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_customerComplaintSerialNumber | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_customerComplaintShipment | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_customerComplaintSuspectLot | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_customerComplaintCommunication | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_customerComplaintCommunication | direction | Inbound; Outbound |
| QualityManagement | u_mes_qual_defectGroup | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_gaugeType | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_dispositionType | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_complaintType | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_characteristicPosition | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_curveEnvelope | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_curveEnvelope | curveType | Force Displacement; Torque Angle; Pressure Time; Sound Spectrum; Vibration Acceleration |
| QualityManagement | u_mes_qual_curveEnvelopeWindow | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_curveEnvelopeWindow | windowType | Box; Upper Band; Lower Band; Peak; Final Value |
| QualityManagement | u_mes_qual_curveEnvelopeWindow | entrySide | Left; Right; Top; Bottom |
| QualityManagement | u_mes_qual_curveEnvelopeWindow | exitSide | Left; Right; Top; Bottom |
| QualityManagement | u_mes_qual_measurementCurve | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_measurementCurve | result | OK; NOK |
| QualityManagement | u_mes_qual_measurementCurvePoint | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_defectRecord | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_defectRecord | fourMCategory | Man; Machine; Material; Method |
| QualityManagement | u_mes_qual_auditSchedule | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_auditSchedule | auditType | Layered Process Audit; Product Audit; Process Audit; 5S Audit |
| QualityManagement | u_mes_qual_auditSchedule | frequencyType | Shift; Daily; Weekly; Monthly |
| QualityManagement | u_mes_qual_inspectionPlanProductVariant | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_environmentalMonitoringPoint | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_environmentalMonitoringPoint | monitoredParameter | Temperature; Relative Humidity; Differential Pressure; Airborne Particles 0.5 um; Airborne Particles 5.0 um; Surface Particle Count; Illuminance; Surface Microbial Count |
| QualityManagement | u_mes_qual_environmentalMonitoringPoint | limitDirection | Upper; Lower; Range |
| QualityManagement | u_mes_qual_environmentalMonitoringPoint | samplingFrequency | Continuous; Every Shift; Daily; Weekly |
| QualityManagement | u_mes_qual_environmentalMonitoringResult | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_environmentalMonitoringResult | limitEvaluation | Within Limits; Alert Limit Exceeded; Action Limit Exceeded |
| QualityManagement | u_mes_qual_retentionSample | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_retentionSample | sampleType | Reserve Sample; Retention Sample; Master Sample; Boundary Sample |
| QualityManagement | u_mes_qual_riskAssessment | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_riskAssessment | relatedCollectionName | u_mes_prod_engineeringChange; u_mes_syst_computerisedSystem; u_mes_qual_nonconformance; u_mes_mast_equipment; u_mes_prod_item |
| QualityManagement | u_mes_qual_riskAssessment | assessmentMethod | FMEA; Risk Ranking And Filtering; Fault Tree Analysis; HACCP; Preliminary Hazard Analysis |
| QualityManagement | u_mes_qual_riskAssessment | initialRiskLevel | Low; Medium; High |
| QualityManagement | u_mes_qual_riskAssessment | residualRiskLevel | Low; Medium; High |
| QualityManagement | u_mes_qual_riskAssessment | acceptanceDecision | Accepted; Accepted With Controls; Not Accepted |
| QualityManagement | u_mes_qual_productQualityReview | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_productRecall | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_productRecall | recallClass | Class I; Class II; Class III |
| QualityManagement | u_mes_qual_productRecall | recallScope | Customer Plant; Distributor; Field |
| QualityManagement | u_mes_qual_productRecallLot | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_processValidation | app | Auto; Gamp; Common |
| QualityManagement | u_mes_qual_processValidation | validationStage | Stage 1 Process Design; Stage 2 Process Qualification; Stage 3 Continued Process Verification |
| PerformanceManagement | u_mes_perf_reasonCode | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_reasonCode | reasonType | Downtime; Scrap; Hold; Andon; Changeover Loss; Hold Release; Interlock Override; Rework; Root Cause; Alarm Closure; Exposure Reset |
| PerformanceManagement | u_mes_perf_reasonCode | oeeImpact | Availability; Performance; Quality; None |
| PerformanceManagement | u_mes_perf_equipmentState | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_equipmentState | stateCode | Running; Idle; Setup; Down; Starved; Blocked; Planned Stop |
| PerformanceManagement | u_mes_perf_equipmentState | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| PerformanceManagement | u_mes_perf_downtimeEvent | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_downtimeEvent | downtimeType | Planned; Unplanned |
| PerformanceManagement | u_mes_perf_downtimeEvent | captureSource | Equipment Signal; Operator Entry; Andon |
| PerformanceManagement | u_mes_perf_downtimeEventComment | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_productionCount | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_productionCount | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| PerformanceManagement | u_mes_perf_oeeRecord | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_oeeRecordLoss | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_processTag | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_processTag | dataType | Variable; Attribute |
| PerformanceManagement | u_mes_perf_processTag | tagClass | Process Value; Setpoint; Counter; State; Alarm Bit; Energy; Environment |
| PerformanceManagement | u_mes_perf_processTag | aggregation | None; Average; Minimum; Maximum; Last; Sum |
| PerformanceManagement | u_mes_perf_processReading | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_processReading | signalQuality | Good; Uncertain; Bad |
| PerformanceManagement | u_mes_perf_alarm | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_alarm | alarmClass | Process; Machine; Safety; Quality |
| PerformanceManagement | u_mes_perf_torqueResult | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_torqueResult | strategy | Torque Control; Torque Control Angle Monitor; Angle Control Torque Monitor; Yield Control |
| PerformanceManagement | u_mes_perf_torqueResult | result | OK; Not OK |
| PerformanceManagement | u_mes_perf_torqueResult | envelopeResult | OK; NOK |
| PerformanceManagement | u_mes_perf_leakTestResult | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_leakTestResult | testMedium | Dry Air; Nitrogen; Helium |
| PerformanceManagement | u_mes_perf_leakTestResult | verdict | Pass; Fail |
| PerformanceManagement | u_mes_perf_leakTestResultStage | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_leakTestResultStage | stageName | Low Pressure; High Pressure; Gross Leak; Fine Leak |
| PerformanceManagement | u_mes_perf_leakTestResultStage | stageResult | Pass; Fail |
| PerformanceManagement | u_mes_perf_energyReading | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_energyReading | signalQuality | Good; Uncertain; Bad |
| PerformanceManagement | u_mes_perf_lossCategory | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_lossCategory | oeeImpact | Availability; Performance; Quality; None |
| PerformanceManagement | u_mes_perf_reasonCategory | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_energyType | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_alarmDefinition | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_alarmDefinition | alarmClass | Process; Equipment; Safety; Quality; Utility |
| PerformanceManagement | u_mes_perf_alarmDefinition | severityClass | Low; Medium; High; Critical |
| PerformanceManagement | u_mes_perf_lossSummary | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_workCenterPerformance | app | Auto; Gamp; Common |
| PerformanceManagement | u_mes_perf_operatorPerformance | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_maintenancePlan | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_maintenancePlan | planType | Incoming; In Process; First Off; Final; Dock Audit; Layout |
| ToolingAndMaintenance | u_mes_maint_maintenancePlan | strategy | Torque Control; Torque Control Angle Monitor; Angle Control Torque Monitor; Yield Control |
| ToolingAndMaintenance | u_mes_maint_maintenancePlan | intervalType | Calendar; Counter; Condition |
| ToolingAndMaintenance | u_mes_maint_maintenancePlan | intervalUom | Days; Weeks; Months; Cycles; Shots; Run Hours |
| ToolingAndMaintenance | u_mes_maint_maintenancePlanTask | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_maintenancePlanRequiredSkill | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_maintenancePlanRequiredSparePart | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrder | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrder | workOrderType | Breakdown; Preventive; Predictive; Improvement; Calibration |
| ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrder | priority | Low; Normal; High; Urgent |
| ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrder | schedulingSource | Manual; Rule; Model |
| ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrderAssignedToUser | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrderLabour | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrderUsedSparePart | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_sparePart | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_sparePart | category | Mechanical; Electrical; Process; Material; Quality; Organisation; Planned |
| ToolingAndMaintenance | u_mes_maint_sparePart | criticality | A; B; C |
| ToolingAndMaintenance | u_mes_maint_sparePartUsedOnEquipment | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_tool | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_tool | toolClass | Production Tooling; Customer Owned Tooling; Consumable Tooling; Fixture |
| ToolingAndMaintenance | u_mes_maint_tool | lifeUom | Shots; Cycles; Pieces; Run Hours; Batches; Tablets |
| ToolingAndMaintenance | u_mes_maint_toolItem | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_toolLifeRecord | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_toolLifeRecord | eventType | Mounted; Usage; Dismounted; Regrind; Maintenance; Scrapped |
| ToolingAndMaintenance | u_mes_maint_toolType | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_toolType | lifeUom | Shots; Cycles; Pieces; Run Hours; Batches; Tablets |
| ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrderTask | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrderTask | result | Done OK; Done Not OK; Not Applicable; Not Done |
| ToolingAndMaintenance | u_mes_maint_sparePartTransaction | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_sparePartTransaction | transactionType | Issue; Return; Receipt; Adjustment; Scrap |
| ToolingAndMaintenance | u_mes_maint_reliabilitySummary | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_reliabilitySummary | periodType | Shift; Day; Week; Month |
| ToolingAndMaintenance | u_mes_maint_equipmentLifecycleEvent | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_equipmentLifecycleEvent | eventType | Commissioning; Relocation; Overhaul; Refurbishment; Upgrade; Health Assessment; Replacement Recommendation; Decommissioning |
| ToolingAndMaintenance | u_mes_maint_logbookEntry | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_logbookEntry | relatedCollectionName | u_mes_mast_equipment; u_mes_mast_area |
| ToolingAndMaintenance | u_mes_maint_logbookEntry | activityType | Production; Cleaning; Maintenance; Calibration; Line Clearance; Qualification; Idle |
| ToolingAndMaintenance | u_mes_maint_cleaningRecord | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_cleaningRecord | cleaningType | Minor Cleaning; Major Cleaning; Product Changeover Cleaning; Bath Change |
| ToolingAndMaintenance | u_mes_maint_cleaningRecord | verificationMethod | Visual Inspection; Cleanliness Test; Rinse Sample; Swab Sample |
| ToolingAndMaintenance | u_mes_maint_cleaningRecord | verificationResult | Pass; Fail |
| ToolingAndMaintenance | u_mes_maint_equipmentQualification | app | Auto; Gamp; Common |
| ToolingAndMaintenance | u_mes_maint_equipmentQualification | qualificationPhase | Design Qualification; Installation Qualification; Operational Qualification; Performance Qualification; Periodic Requalification |
| SystemAndIntegration | u_mes_syst_erpMessage | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_erpMessage | direction | Inbound; Outbound; Publish |
| SystemAndIntegration | u_mes_syst_erpMessage | messageType | Production Order Download; Operation Confirmation; Goods Movement; Goods Receipt; Shipment Advice; Material Master; Quality Notification |
| SystemAndIntegration | u_mes_syst_erpMessage | payloadFormat | JSON; XML; IDoc |
| SystemAndIntegration | u_mes_syst_integrationConnector | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_integrationConnector | connectorType | ERP; PLM; OPC UA Server; Tool Controller; Label Printer; Leak Tester; Email Gateway; LIMS; Weighing System; Serialisation Server; Track And Trace Portal; Document Management |
| SystemAndIntegration | u_mes_syst_integrationConnector | protocol | HTTPS REST; OPC UA; Open Protocol; Modbus TCP; MQTT; ZPL Over TCP; SMTP; Serial Over TCP |
| SystemAndIntegration | u_mes_syst_integrationConnector | environment | Production; Quality; Development |
| SystemAndIntegration | u_mes_syst_integrationConnector | authMethod | OAuth2 Client Credentials; Certificate; Basic; None |
| SystemAndIntegration | u_mes_syst_integrationConnector | healthStatus | Healthy; Degraded; Down |
| SystemAndIntegration | u_mes_syst_integrationConnectorFunction | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_integrationConnectorFunction | direction | Inbound; Outbound; Publish |
| SystemAndIntegration | u_mes_syst_integrationConnectorFunction | messageType | Production Order Download; Operation Confirmation; Goods Movement; Goods Receipt; Shipment Advice; Material Master; Quality Notification |
| SystemAndIntegration | u_mes_syst_iotDevice | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_iotDevice | protocol | HTTPS REST; OPC UA; Open Protocol; Modbus TCP; MQTT; ZPL Over TCP; SMTP |
| SystemAndIntegration | u_mes_syst_iotDevice | connectionStatus | Online; Offline; Degraded |
| SystemAndIntegration | u_mes_syst_operatorApp | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_operatorApp | appType | Operator Station; Inspection; Material Handling; Maintenance; Andon Board |
| SystemAndIntegration | u_mes_syst_operatorAppWorkCenter | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_operatorAppOperation | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_operatorAppStep | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_operatorAppStep | widgetType | Work Instruction; Data Entry; Device Result; Scan; Checklist; Signature; Summary |
| SystemAndIntegration | u_mes_syst_operatorAppStepTrigger | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_operatorAppStepTrigger | triggerEvent | Step Opened; Button Pressed; Scan Completed; Device Result Received; Value Out Of Limit; Timer Expired |
| SystemAndIntegration | u_mes_syst_operatorAppStepTrigger | triggerAction | Go To Step; Complete Operation; Raise Nonconformance; Raise Andon; Print Label; Block Station |
| SystemAndIntegration | u_mes_syst_operatorAppDeviceBinding | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_operatorAppDeviceBinding | purpose | Tightening result; Leak test result; Component scan; Label print; Measurement |
| SystemAndIntegration | u_mes_syst_operatorAppLanguage | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_businessEvent | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_businessEvent | eventType | Order Released; Operation Started; Operation Completed; Recipe Downloaded; Hold Placed; Hold Released; Label Printed; Unit Scrapped; Shipment Dispatched; User Logged In |
| SystemAndIntegration | u_mes_syst_businessEvent | eventCategory | Execution; Quality; Material; Maintenance; Integration; Security |
| SystemAndIntegration | u_mes_syst_businessEvent | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| SystemAndIntegration | u_mes_syst_auditTrail | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_auditTrail | changeAction | Create; Update; Obsolete |
| SystemAndIntegration | u_mes_syst_auditTrailChange | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_electronicSignature | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_electronicSignature | authenticationMethod | Password; Password And Badge; Single Sign On |
| SystemAndIntegration | u_mes_syst_notification | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_notificationRecipient | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_notificationRecipient | channel | Screen; Email; SMS; Mobile Push |
| SystemAndIntegration | u_mes_syst_controlledDocument | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_controlledDocument | storageProvider | S3; GridFS; File Share |
| SystemAndIntegration | u_mes_syst_controlledDocumentTag | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_numberRange | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_numberRange | rangeType | Serial Number; Lot Number; Order Number; Label Number; Document Number |
| SystemAndIntegration | u_mes_syst_numberRange | resetPolicy | Never; Daily; Monthly; Yearly |
| SystemAndIntegration | u_mes_syst_numberRange | checkDigitMethod | None; Modulo 10; Modulo 43 |
| SystemAndIntegration | u_mes_syst_systemConfiguration | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_systemConfiguration | module | Master Data; ProductDefinition; Execution; Materials; Traceability; Quality; Performance; Maintenance; Integration; Safety |
| SystemAndIntegration | u_mes_syst_systemConfiguration | valueType | Text; Number; Flag; JSON |
| SystemAndIntegration | u_mes_syst_systemConfiguration | scope | Enterprise; Site |
| SystemAndIntegration | u_mes_syst_documentType | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_deviceType | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_notificationType | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_statusDefinition | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_enumerationValue | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_statusTransition | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_interlockRule | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_interlockRule | ruleType | Hold Check; Sequence Check; Mandatory Scan; Duplicate Serial; Wrong Order; Wrong Station; Variant Check; Component Lot Capture; Lot Release Check; Expiry Check; Kit Completeness; Genealogy Completeness; Recipe Release Check; Program Version Check; Work Instruction Release Check; Acknowledgement Check; Mandatory Inspection; NOK Result; Skill Check; Login Check; Equipment Readiness; Tool Life; Calibration Check; Environment Check; Setup Check; Alarm Restart; Line Clearance Check; Batch Release Check; Equipment Clean Status Check; Qualification Status Check; Dispense Tolerance Check |
| SystemAndIntegration | u_mes_syst_interlockRule | transactionPoint | Operation Start; Operation Complete; Material Issue; Kit Release; Pack Out; Dispatch; Order Close; Login; Inspection Accept |
| SystemAndIntegration | u_mes_syst_interlockRule | enforcementMode | Warning; Block |
| SystemAndIntegration | u_mes_syst_statusTransitionRole | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_escalationRule | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_escalationRule | sourceType | Interlock; Andon; Alarm; Alert Rule; Breakdown; Audit; Nonconformance; Customer Complaint |
| SystemAndIntegration | u_mes_syst_escalationRule | severityClass | Low; Medium; High; Critical |
| SystemAndIntegration | u_mes_syst_escalationRuleLevel | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_escalationRuleLevel | basis | Not Acknowledged; Not Resolved |
| SystemAndIntegration | u_mes_syst_escalationRuleLevel | channel | Andon Board; SMS; Email; Mobile App; Public Address |
| SystemAndIntegration | u_mes_syst_alertRule | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_alertRule | metric | OEE; Availability; Downtime Minutes; Reject Rate; Output Gap; Process Deviation; SPC Rule Violation; Line-side Stock Cover; Environment Limit; Model Anomaly Score |
| SystemAndIntegration | u_mes_syst_alertRule | comparison | Less Than; Greater Than; Outside Band |
| SystemAndIntegration | u_mes_syst_alertRule | severityClass | Low; Medium; High; Critical |
| SystemAndIntegration | u_mes_syst_alertRule | actionType | Notify; Hold; Stop Equipment; Block Process; Create Work Order; Create Nonconformance |
| SystemAndIntegration | u_mes_syst_analyticsModel | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_analyticsModel | modelType | Vision Classification; Defect Prediction; OEE Forecast; Anomaly Detection; Maintenance Prediction; Demand Forecast; Recipe Optimisation; Operator Risk; Assignment Recommendation |
| SystemAndIntegration | u_mes_syst_modelPrediction | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_modelPrediction | predictionType | Classification; Forecast; Anomaly; Maintenance Priority; Remaining Useful Life; Recommendation; Operator Risk; Assignment Recommendation |
| SystemAndIntegration | u_mes_syst_modelPrediction | actionStatus | Not Required; Pending; Approved; Applied; Rejected |
| SystemAndIntegration | u_mes_syst_simulationStudy | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_simulationStudy | studyType | Process; Inventory; Equipment; Calibration Baseline |
| SystemAndIntegration | u_mes_syst_simulationStudy | comparisonResult | Better; Equal; Worse |
| SystemAndIntegration | u_mes_syst_recordPolicy | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_recordPolicy | editPolicy | Free Edit; Controlled Edit; No Edit After Lock; Append Only |
| SystemAndIntegration | u_mes_syst_savedView | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_savedView | viewType | Dashboard; Comparison; Pareto; Trend; List |
| SystemAndIntegration | u_mes_syst_backupRun | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_backupRun | runType | Full Backup; Incremental Backup; Restore Test; Failover Test |
| SystemAndIntegration | u_mes_syst_computerisedSystem | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_computerisedSystem | systemCategory | Manufacturing Execution System; Equipment Controller; Laboratory System; ERP Interface; Label Printing; Data Historian; Infrastructure |
| SystemAndIntegration | u_mes_syst_computerisedSystem | gampCategory | Category 1; Category 3; Category 4; Category 5 |
| SystemAndIntegration | u_mes_syst_computerisedSystem | gxpImpact | Direct; Indirect; None |
| SystemAndIntegration | u_mes_syst_computerisedSystem | dataCriticality | High; Medium; Low |
| SystemAndIntegration | u_mes_syst_computerisedSystem | hostingModel | On Premise; Private Cloud; Supplier Hosted; Embedded |
| SystemAndIntegration | u_mes_syst_systemValidation | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_systemValidation | validationType | Initial Validation; Change Revalidation; Retrospective Validation; Decommissioning |
| SystemAndIntegration | u_mes_syst_systemValidation | assuranceApproach | Scripted Testing; Unscripted Testing; Ad Hoc Testing; Supplier Assurance |
| SystemAndIntegration | u_mes_syst_systemPeriodicReview | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_auditTrailReview | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_auditTrailReview | reviewType | Batch Record Review; Periodic System Review; For Cause |
| SystemAndIntegration | u_mes_syst_auditTrailReview | relatedCollectionName | u_mes_plan_productionOrder; u_mes_syst_systemPeriodicReview; u_mes_qual_nonconformance |
| SystemAndIntegration | u_mes_syst_userAccessReview | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_userAccessReviewLine | app | Auto; Gamp; Common |
| SystemAndIntegration | u_mes_syst_userAccessReviewLine | reviewAction | Retain; Remove Role; Change Role; Lock Account |
| EnvironmentHealthAndSafety | u_mes_ehs_safetyIncident | app | Auto; Gamp; Common |
| EnvironmentHealthAndSafety | u_mes_ehs_safetyIncidentWitnessUser | app | Auto; Gamp; Common |
| EnvironmentHealthAndSafety | u_mes_ehs_safetyIncidentAction | app | Auto; Gamp; Common |
| EnvironmentHealthAndSafety | u_mes_ehs_incidentType | app | Auto; Gamp; Common |
| EnvironmentHealthAndSafety | u_mes_ehs_bodyPart | app | Auto; Gamp; Common |
| EnvironmentHealthAndSafety | u_mes_ehs_injuryType | app | Auto; Gamp; Common |
| BatchManufacturingRecord | u_mes_bmr_batchRecordReview | app | Auto; Gamp; Common |
| BatchManufacturingRecord | u_mes_bmr_batchRecordReview | reviewScope | Review By Exception; Full Review |
| BatchManufacturingRecord | u_mes_bmr_batchRecordReviewException | app | Auto; Gamp; Common |
| BatchManufacturingRecord | u_mes_bmr_batchRecordReviewException | exceptionType | Interlock Override; Out Of Specification Result; Manual Data Entry; Data Correction; Missing Signature; Deviation; Late Entry; Hold |
| BatchManufacturingRecord | u_mes_bmr_batchRecordReviewException | relatedCollectionName | u_mes_plan_interlockEvent; u_mes_qual_inspectionResult; u_mes_syst_auditTrail; u_mes_qual_nonconformance; u_mes_qual_qualityHold; u_mes_plan_operationExecution |
| BatchManufacturingRecord | u_mes_bmr_batchRecordReviewException | assessment | No Impact; Impact Assessed Acceptable; Requires Deviation; Requires Correction |
| BatchManufacturingRecord | u_mes_bmr_batchRelease | app | Auto; Gamp; Common |
| BatchManufacturingRecord | u_mes_bmr_yieldReconciliation | app | Auto; Gamp; Common |
| BatchManufacturingRecord | u_mes_bmr_yieldReconciliation | reconciliationType | Product Yield; Component Reconciliation; Label Reconciliation |
| BatchManufacturingRecord | u_mes_bmr_batchManufacturingRecord | app | Auto; Gamp; Common |
| MasterManufacturingRecord | u_mes_mmr_masterManufacturingRecord | app | Auto; Gamp; Common |
| MasterManufacturingRecord | u_mes_mmr_masterManufacturingRecordRecipe | app | Auto; Gamp; Common |
