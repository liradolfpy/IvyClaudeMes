# Fixed enumeration values

Keys whose values are fixed by the application logic stay coded text (data_modeling_standard.md section 11, rule B). Their allowed values are listed here, enforced by the validators, and stored as data in `u_mes_sys_enumerationValue` (one document per collection, key and value). Status values are in status_values.md.

Keys: 205 | Values: 878

| Module | Collection | Key | Allowed values |
|---|---|---|---|
| Master data | u_mes_mdm_enterprise | scope | Enterprise; Site |
| Master data | u_mes_mdm_site | siteType | Manufacturing Plant; Warehouse; Technical Center; Head Office |
| Master data | u_mes_mdm_area | areaType | Production; Storage; Quality; Maintenance; Utility |
| Master data | u_mes_mdm_line | lineType | Casting; Heat Treatment; Machining; Surface Treatment; Assembly; Inspection; Packing |
| Master data | u_mes_mdm_workCenter | workCenterType | Machine Station; Manual Station; Test Station; Inspection Station; Batch Process |
| Master data | u_mes_mdm_workCenter | trackingGrain | Lot; Unit; Container |
| Master data | u_mes_mdm_equipment | equipmentClass | Production Equipment; Test Equipment; Measuring Equipment; Utility |
| Master data | u_mes_mdm_equipment | controllerProtocol | OPC UA; Open Protocol; Modbus TCP; Profinet; MQTT; Ethernet/IP |
| Master data | u_mes_mdm_equipment | criticality | A; B; C |
| Master data | u_mes_mdm_equipment | currentState | Running; Idle; Setup; Down; Starved; Blocked; Planned Stop |
| Master data | u_mes_mdm_equipment | safetyCategory | PL a; PL b; PL c; PL d; PL e |
| Master data | u_mes_mdm_shiftWorkingDay | workingDay | Monday; Tuesday; Wednesday; Thursday; Friday; Saturday; Sunday |
| Master data | u_mes_mdm_workCalendarWeeklyOffDay | weeklyOffDay | Monday; Tuesday; Wednesday; Thursday; Friday; Saturday; Sunday |
| Master data | u_mes_mdm_workCalendarException | exceptionType | Public Holiday; Plant Shutdown; Extra Working Day; Reduced Shift |
| Master data | u_mes_mdm_shiftRosterAssignment | roleInCrew | Operator; Setter; Line Leader; Quality Inspector; Material Handler |
| Master data | u_mes_mdm_shiftRosterAssignment | attendance | Present; Absent; Leave; Overtime |
| Master data | u_mes_mdm_role | scope | Enterprise; Site |
| Master data | u_mes_mdm_user | userType | Employee; Contractor; System |
| Master data | u_mes_mdm_skill | assessmentMethod | Practical Test; Written Test; Observation; On the Job |
| Master data | u_mes_mdm_skillCertification | assessmentMethod | Practical Test; Written Test; Observation; On the Job |
| Master data | u_mes_mdm_customer | customerType | OEM; Tier 1; Aftermarket |
| Master data | u_mes_mdm_customerContact | businessFunction | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| Master data | u_mes_mdm_supplier | supplierType | Direct Material; Indirect Material; Tooling; Service; Calibration Laboratory |
| Master data | u_mes_mdm_supplierContact | businessFunction | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| Master data | u_mes_mdm_unitOfMeasure | scope | Enterprise; Site |
| Master data | u_mes_mdm_unitOfMeasure | dimension | Count; Mass; Length; Torque; Pressure; Temperature; Time; Energy; Volume; Hardness; Leak Rate |
| Product definition | u_mes_prd_item | itemType | Finished Good; Semi Finished; Purchased Component; Raw Material; Consumable; Packaging |
| Product definition | u_mes_prd_item | procurementType | In House; Purchased; Subcontracted |
| Product definition | u_mes_prd_productVariant | optionsHand | LH; RH |
| Product definition | u_mes_prd_billOfMaterial | bomType | Production; Engineering; Rework |
| Product definition | u_mes_prd_billOfMaterialComponent | traceLevel | None; Lot; Serial |
| Product definition | u_mes_prd_operation | operationType | Casting; Heat Treatment; Machining; Cleaning; Surface Treatment; Assembly; Test; Marking; Inspection; Packing |
| Product definition | u_mes_prd_operation | trackingGrain | Lot; Unit; Container |
| Product definition | u_mes_prd_routing | routingType | Standard; Rework; Alternate |
| Product definition | u_mes_prd_routingStepNextStep | nextStepCondition | Result OK; Result Not OK; Rework Complete; Always |
| Product definition | u_mes_prd_billOfProcessStepInterlock | interlockType | Skill; Recipe; Tool Life; Gauge Calibration; Previous Step; Component Scan; Maintenance Due |
| Product definition | u_mes_prd_workInstructionStep | inputType | None; Confirmation; Number; Text; Scan; Photo; Device Value |
| Product definition | u_mes_prd_recipe | recipeType | Die Casting Parameters; Furnace Profile; CNC Program; Washing Program; Anodising Program; Tightening Program; Leak Test Program; Laser Marking Program |
| Product definition | u_mes_prd_engineeringChange | changeType | Design Change; Process Change; Material Change; Supplier Change; Tooling Change; Document Change |
| Product definition | u_mes_prd_engineeringChange | originator | Customer; Internal; Supplier |
| Product definition | u_mes_prd_engineeringChange | effectivityType | Date; Serial Number; Lot; Stock Run Out |
| Product definition | u_mes_prd_engineeringChangeAffectedObject | changeAction | Create; Update; Obsolete |
| Product definition | u_mes_prd_engineeringChangeApproval | businessFunction | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| Product definition | u_mes_prd_engineeringChangeApproval | decision | Approved; Rejected; Approved With Conditions |
| Planning and execution | u_mes_exe_customerSchedule | scheduleType | Forecast; Delivery Schedule; Just In Time Call Off |
| Planning and execution | u_mes_exe_customerScheduleLine | firmness | Firm; Forecast |
| Planning and execution | u_mes_exe_productionOrder | orderType | Production; Rework; Trial; PPAP Run |
| Planning and execution | u_mes_exe_productionOrder | priority | Low; Normal; High; Urgent |
| Planning and execution | u_mes_exe_dispatchList | rule | Earliest Due Date; First In First Out; Critical Ratio; Priority |
| Planning and execution | u_mes_exe_dispatchListEntry | priority | Low; Normal; High; Urgent |
| Planning and execution | u_mes_exe_operationExecution | executionType | Production; Rework; Retest; Setup |
| Planning and execution | u_mes_exe_operationExecution | result | OK; Not OK |
| Planning and execution | u_mes_exe_stepCompletion | inputType | None; Confirmation; Number; Text; Scan; Photo; Device Value |
| Planning and execution | u_mes_exe_stepCompletion | deviceSource | Manual Entry; Scanner; Nutrunner Controller; Leak Tester; Gauge Interface; PLC |
| Planning and execution | u_mes_exe_wipUnit | qualityStatus | Released; Under Inspection; On Hold; Rejected |
| Planning and execution | u_mes_exe_lot | lotType | Supplier Lot; Melt Lot; Casting Lot; Heat Treatment Charge; Machining Lot; Anodising Load; Finished Goods Lot |
| Planning and execution | u_mes_exe_lot | qualityStatus | Released; Under Inspection; On Hold; Rejected |
| Planning and execution | u_mes_exe_labourBooking | bookingType | Direct; Indirect |
| Planning and execution | u_mes_exe_labourBooking | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Planning and execution | u_mes_exe_changeover | changeoverType | Variant Change; Item Change; Tool Change; Die Change |
| Planning and execution | u_mes_exe_changeoverStep | internalExternal | Internal; External |
| Materials | u_mes_mat_storageLocation | locationType | Warehouse Rack; Line Side; Quarantine; Dispatch Bay; Receiving Bay; Tool Crib; Scrap Yard |
| Materials | u_mes_mat_materialMovement | scanSource | Handheld Scanner; Fixed Scanner; Manual Entry |
| Materials | u_mes_mat_goodsReceiptLine | inspectionStatus | Pending; Accepted; Rejected; Accepted Under Deviation |
| Materials | u_mes_mat_kit | kitType | Order Kit; Shift Kit; Rework Kit |
| Materials | u_mes_mat_materialRequest | requestType | Kanban; Andon Call; Manual |
| Materials | u_mes_mat_materialRequest | triggerSource | Minimum Level Sensor; Operator; Schedule |
| Materials | u_mes_mat_materialRequest | priority | Low; Normal; High; Urgent |
| Materials | u_mes_mat_materialConsumption | consumptionType | Scanned; Backflush; Manual |
| Materials | u_mes_mat_labelTemplate | labelType | Unit Mark; Container Label; Shipping Label; Hold Tag; Location Label |
| Materials | u_mes_mat_labelTemplate | printerLanguage | ZPL; EPL; PDF |
| Materials | u_mes_mat_labelTemplate | symbology | Data Matrix ECC200; QR Code; Code 128; Code 39; PDF417 |
| Materials | u_mes_mat_labelTemplateField | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Materials | u_mes_mat_label | labelType | Unit Mark; Container Label; Shipping Label; Hold Tag; Location Label |
| Materials | u_mes_mat_label | verificationGrade | A; B; C; D; F |
| Materials | u_mes_mat_movementType | stockEffect | Increase; Decrease; Transfer; None |
| Traceability | u_mes_trc_serialNumber | markGrade | A; B; C; D; F |
| Traceability | u_mes_trc_genealogyLink | childType | Lot; Serial |
| Traceability | u_mes_trc_genealogyLink | linkType | Assembled; Replaced; Split; Merge; Transformed |
| Traceability | u_mes_trc_componentLotLink | linkType | Assembled; Replaced; Split; Merge; Transformed |
| Traceability | u_mes_trc_asBuiltRecord | leakTestVerdict | Pass; Fail |
| Traceability | u_mes_trc_asBuiltRecordOperation | result | OK; Not OK |
| Quality | u_mes_qlt_characteristic | characteristicType | Product; Process |
| Quality | u_mes_qlt_characteristic | classification | Critical; Significant; Standard |
| Quality | u_mes_qlt_characteristic | dataType | Variable; Attribute |
| Quality | u_mes_qlt_characteristic | toleranceType | Bilateral; Unilateral Upper; Unilateral Lower |
| Quality | u_mes_qlt_characteristic | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Quality | u_mes_qlt_controlPlan | phase | Prototype; Pre Launch; Production |
| Quality | u_mes_qlt_controlPlanLine | classification | Critical; Significant; Standard |
| Quality | u_mes_qlt_inspectionPlan | planType | Incoming; In Process; First Off; Final; Dock Audit; Layout |
| Quality | u_mes_qlt_inspectionPlan | collectionTrigger | Operation Start; Operation Complete; Time Interval; Unit Count; Goods Receipt; Changeover |
| Quality | u_mes_qlt_inspectionPlanLine | frequencyType | Every Unit; Every N Units; Every N Minutes; Per Lot; Per Shift; First Off |
| Quality | u_mes_qlt_inspectionPlanLine | recordType | Measured Value; Pass Fail; Count |
| Quality | u_mes_qlt_samplingPlan | samplingType | Attribute AQL; Fixed Sample; Hundred Percent; Skip Lot |
| Quality | u_mes_qlt_samplingPlan | inspectionLevel | S-1; S-2; S-3; S-4; I; II; III |
| Quality | u_mes_qlt_samplingPlan | frequencyType | Every Unit; Every N Units; Every N Minutes; Per Lot; Per Shift; First Off |
| Quality | u_mes_qlt_checkSheet | checkSheetType | Start Of Shift; Poka Yoke Verification; First Off Approval; Autonomous Maintenance; Layered Process Audit; Changeover |
| Quality | u_mes_qlt_checkSheet | frequency | Per Shift; Daily; Weekly; Per Changeover; Per Lot |
| Quality | u_mes_qlt_checkSheetItem | answerType | Yes No; Number; Text |
| Quality | u_mes_qlt_checkSheetResult | overallResult | Pass; Fail |
| Quality | u_mes_qlt_inspectionResult | inspectionType | Incoming; In Process; First Off; Final; Audit |
| Quality | u_mes_qlt_inspectionResult | attributeResult | Pass; Fail |
| Quality | u_mes_qlt_inspectionResult | result | OK; Not OK |
| Quality | u_mes_qlt_inspectionResult | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Quality | u_mes_qlt_spcChart | chartType | X-bar R; X-bar S; I-MR; p; np; c; u |
| Quality | u_mes_qlt_spcChartRule | rule | Earliest Due Date; First In First Out; Critical Ratio; Priority |
| Quality | u_mes_qlt_spcSampleViolation | rule | Earliest Due Date; First In First Out; Critical Ratio; Priority |
| Quality | u_mes_qlt_defectCode | scrapCostCategory | Casting Scrap; Machining Scrap; Assembly Scrap; Supplier Chargeable |
| Quality | u_mes_qlt_nonconformance | ncType | Internal; Supplier; Customer |
| Quality | u_mes_qlt_nonconformance | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Quality | u_mes_qlt_reworkOrder | reworkType | Replace Component; Retighten; Re-machine; Re-anodise; Re-mark; Clean |
| Quality | u_mes_qlt_reworkOrder | reinspectionResult | Pass; Fail |
| Quality | u_mes_qlt_scrapRecord | scrapType | Process Scrap; Setup Scrap; Material Defect; Destructive Test |
| Quality | u_mes_qlt_scrapRecord | disposalMethod | Remelt; Sell As Scrap; Return To Supplier |
| Quality | u_mes_qlt_qualityHold | holdType | Quality; Customer; Engineering; Supplier |
| Quality | u_mes_qlt_qualityHold | releaseDecision | Released; Rework; Scrap; Return To Supplier |
| Quality | u_mes_qlt_qualityHoldHeldObject | releaseDecision | Released; Rework; Scrap; Return To Supplier |
| Quality | u_mes_qlt_deviationPermit | deviationType | Product; Process; Material |
| Quality | u_mes_qlt_deviationPermit | limitType | Quantity; Date |
| Quality | u_mes_qlt_deviationPermitApproval | businessFunction | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| Quality | u_mes_qlt_deviationPermitApproval | decision | Approved; Rejected; Approved With Conditions |
| Quality | u_mes_qlt_capa | capaType | Corrective; Preventive |
| Quality | u_mes_qlt_capa | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Quality | u_mes_qlt_capa | d4RootCauseMethod | 5 Why; Fishbone; Fault Tree; Is Is Not |
| Quality | u_mes_qlt_capa | currentDiscipline | D1; D2; D3; D4; D5; D6; D7; D8 |
| Quality | u_mes_qlt_capaTeamMember | roleInTeam | Champion; Leader; Member |
| Quality | u_mes_qlt_pfmea | methodology | AIAG-VDA; AIAG 4th Edition |
| Quality | u_mes_qlt_pfmeaLine | classification | Critical; Significant; Standard |
| Quality | u_mes_qlt_pfmeaLine | actionPriority | High; Medium; Low |
| Quality | u_mes_qlt_ppapSubmission | submissionReason | Initial Submission; Engineering Change; Tooling Transfer; Correction Of Discrepancy; Tooling Inactive Over One Year; Sub Supplier Change |
| Quality | u_mes_qlt_ppapSubmission | customerDecision | Approved; Interim Approved; Rejected |
| Quality | u_mes_qlt_gauge | calibrationSource | Internal; External |
| Quality | u_mes_qlt_gaugeCalibration | calibrationType | Initial; Periodic; After Repair; After Shock Or Damage |
| Quality | u_mes_qlt_gaugeCalibration | asFoundResult | Within Tolerance; Out Of Tolerance |
| Quality | u_mes_qlt_gaugeCalibration | asLeftResult | Within Tolerance; Out Of Tolerance |
| Quality | u_mes_qlt_gaugeCalibration | overallResult | Pass; Fail |
| Quality | u_mes_qlt_msaStudy | studyType | Gauge R and R; Bias; Linearity; Stability; Attribute Agreement |
| Quality | u_mes_qlt_msaStudy | studyMethod | ANOVA; Average And Range; Kappa |
| Quality | u_mes_qlt_msaStudy | conclusion | Acceptable; Conditionally Acceptable; Not Acceptable |
| Quality | u_mes_qlt_audit | auditType | Layered Process Audit; Process Audit; Product Audit; System Audit; Customer Audit; Supplier Audit |
| Quality | u_mes_qlt_audit | overallRating | A; B; C |
| Quality | u_mes_qlt_auditFinding | grade | Major; Minor; Observation; Opportunity For Improvement |
| Quality | u_mes_qlt_customerComplaintCommunication | direction | Inbound; Outbound |
| Equipment and performance | u_mes_eqp_reasonCode | reasonType | Downtime; Scrap; Hold; Andon; Changeover Loss |
| Equipment and performance | u_mes_eqp_reasonCode | oeeImpact | Availability; Performance; Quality; None |
| Equipment and performance | u_mes_eqp_equipmentState | stateCode | Running; Idle; Setup; Down; Starved; Blocked; Planned Stop |
| Equipment and performance | u_mes_eqp_equipmentState | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Equipment and performance | u_mes_eqp_downtimeEvent | downtimeType | Planned; Unplanned |
| Equipment and performance | u_mes_eqp_productionCount | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Equipment and performance | u_mes_eqp_processTag | dataType | Variable; Attribute |
| Equipment and performance | u_mes_eqp_processTag | tagClass | Process Value; Setpoint; Counter; State; Alarm Bit; Energy |
| Equipment and performance | u_mes_eqp_processTag | aggregation | None; Average; Minimum; Maximum; Last; Sum |
| Equipment and performance | u_mes_eqp_processReading | signalQuality | Good; Uncertain; Bad |
| Equipment and performance | u_mes_eqp_alarm | alarmClass | Process; Machine; Safety; Quality |
| Equipment and performance | u_mes_eqp_torqueResult | strategy | Torque Control; Torque Control Angle Monitor; Angle Control Torque Monitor; Yield Control |
| Equipment and performance | u_mes_eqp_torqueResult | result | OK; Not OK |
| Equipment and performance | u_mes_eqp_leakTestResult | testMedium | Dry Air; Nitrogen; Helium |
| Equipment and performance | u_mes_eqp_leakTestResult | verdict | Pass; Fail |
| Equipment and performance | u_mes_eqp_leakTestResultStage | stageName | Low Pressure; High Pressure |
| Equipment and performance | u_mes_eqp_leakTestResultStage | stageResult | Pass; Fail |
| Equipment and performance | u_mes_eqp_lossCategory | oeeImpact | Availability; Performance; Quality; None |
| Maintenance and tooling | u_mes_mnt_maintenancePlan | planType | Incoming; In Process; First Off; Final; Dock Audit; Layout |
| Maintenance and tooling | u_mes_mnt_maintenancePlan | strategy | Torque Control; Torque Control Angle Monitor; Angle Control Torque Monitor; Yield Control |
| Maintenance and tooling | u_mes_mnt_maintenancePlan | intervalType | Calendar; Counter; Condition |
| Maintenance and tooling | u_mes_mnt_maintenancePlan | intervalUom | Days; Weeks; Months; Cycles; Shots; Run Hours |
| Maintenance and tooling | u_mes_mnt_maintenanceWorkOrder | workOrderType | Breakdown; Preventive; Predictive; Improvement; Calibration |
| Maintenance and tooling | u_mes_mnt_maintenanceWorkOrder | priority | Low; Normal; High; Urgent |
| Maintenance and tooling | u_mes_mnt_sparePart | category | Mechanical; Electrical; Process; Material; Quality; Organisation; Planned |
| Maintenance and tooling | u_mes_mnt_sparePart | criticality | A; B; C |
| Maintenance and tooling | u_mes_mnt_tool | toolClass | Production Tooling; Customer Owned Tooling; Consumable Tooling |
| Maintenance and tooling | u_mes_mnt_tool | lifeUom | Shots; Cycles; Pieces; Run Hours |
| Maintenance and tooling | u_mes_mnt_toolLifeRecord | eventType | Mounted; Usage; Dismounted; Regrind; Maintenance; Scrapped |
| Maintenance and tooling | u_mes_mnt_toolType | lifeUom | Shots; Cycles; Pieces; Run Hours |
| Integration and system | u_mes_sys_erpMessage | direction | Inbound; Outbound |
| Integration and system | u_mes_sys_erpMessage | messageType | Production Order Download; Operation Confirmation; Goods Movement; Goods Receipt; Shipment Advice; Material Master; Quality Notification |
| Integration and system | u_mes_sys_erpMessage | payloadFormat | JSON; XML; IDoc |
| Integration and system | u_mes_sys_integrationConnector | connectorType | ERP; PLM; OPC UA Server; Tool Controller; Label Printer; Leak Tester; Email Gateway |
| Integration and system | u_mes_sys_integrationConnector | protocol | HTTPS REST; OPC UA; Open Protocol; Modbus TCP; MQTT; ZPL Over TCP; SMTP |
| Integration and system | u_mes_sys_integrationConnector | environment | Production; Quality; Development |
| Integration and system | u_mes_sys_integrationConnector | authMethod | OAuth2 Client Credentials; Certificate; Basic; None |
| Integration and system | u_mes_sys_integrationConnector | healthStatus | Healthy; Degraded; Down |
| Integration and system | u_mes_sys_integrationConnectorFunction | direction | Inbound; Outbound |
| Integration and system | u_mes_sys_integrationConnectorFunction | messageType | Production Order Download; Operation Confirmation; Goods Movement; Goods Receipt; Shipment Advice; Material Master; Quality Notification |
| Integration and system | u_mes_sys_iotDevice | protocol | HTTPS REST; OPC UA; Open Protocol; Modbus TCP; MQTT; ZPL Over TCP; SMTP |
| Integration and system | u_mes_sys_iotDevice | connectionStatus | Online; Offline; Degraded |
| Integration and system | u_mes_sys_operatorApp | appType | Operator Station; Inspection; Material Handling; Maintenance; Andon Board |
| Integration and system | u_mes_sys_operatorAppStep | widgetType | Work Instruction; Data Entry; Device Result; Scan; Checklist; Signature; Summary |
| Integration and system | u_mes_sys_operatorAppStepTrigger | triggerEvent | Step Opened; Button Pressed; Scan Completed; Device Result Received; Value Out Of Limit; Timer Expired |
| Integration and system | u_mes_sys_operatorAppStepTrigger | triggerAction | Go To Step; Complete Operation; Raise Nonconformance; Raise Andon; Print Label; Block Station |
| Integration and system | u_mes_sys_operatorAppDeviceBinding | purpose | Tightening result; Leak test result; Component scan; Label print; Measurement |
| Integration and system | u_mes_sys_businessEvent | eventType | Order Released; Operation Started; Operation Completed; Recipe Downloaded; Hold Placed; Hold Released; Label Printed; Unit Scrapped; Shipment Dispatched; User Logged In |
| Integration and system | u_mes_sys_businessEvent | eventCategory | Execution; Quality; Material; Maintenance; Integration; Security |
| Integration and system | u_mes_sys_businessEvent | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Integration and system | u_mes_sys_auditTrail | changeAction | Create; Update; Obsolete |
| Integration and system | u_mes_sys_electronicSignature | authenticationMethod | Password; Password And Badge; Single Sign On |
| Integration and system | u_mes_sys_notificationRecipient | channel | Screen; Email; SMS; Mobile Push |
| Integration and system | u_mes_sys_controlledDocument | storageProvider | S3; GridFS; File Share |
| Integration and system | u_mes_sys_numberRange | rangeType | Serial Number; Lot Number; Order Number; Label Number; Document Number |
| Integration and system | u_mes_sys_numberRange | resetPolicy | Never; Daily; Monthly; Yearly |
| Integration and system | u_mes_sys_numberRange | checkDigitMethod | None; Modulo 10; Modulo 43 |
| Integration and system | u_mes_sys_systemConfiguration | module | Master Data; Product Definition; Execution; Materials; Traceability; Quality; Performance; Maintenance; Integration; Safety |
| Integration and system | u_mes_sys_systemConfiguration | valueType | Text; Number; Flag; JSON |
| Integration and system | u_mes_sys_systemConfiguration | scope | Enterprise; Site |
| Energy, safety and andon | u_mes_ehs_energyReading | signalQuality | Good; Uncertain; Bad |
| Energy, safety and andon | u_mes_ehs_andonEventEscalation | channel | Screen; Email; SMS; Mobile Push |
