# Fixed enumeration values

Keys whose values are fixed by the application logic stay coded text (data_modeling_standard.md section 11, rule B). Their allowed values are listed here, enforced by the validators, and stored as data in `u_mes_syst_enumerationValue` (one document per collection, key and value). Status values are in status_values.md.

Keys: 308 | Values: 1357

| Module | Collection | Key | Allowed values |
|---|---|---|---|
| Master Data Management | u_mes_mast_enterprise | scope | Enterprise; Site |
| Master Data Management | u_mes_mast_site | siteType | Manufacturing Plant; Warehouse; Technical Center; Head Office |
| Master Data Management | u_mes_mast_area | areaType | Production; Storage; Quality; Maintenance; Utility |
| Master Data Management | u_mes_mast_area | cleanlinessClass | ISO 7; ISO 8; Controlled Not Classified; Unclassified |
| Master Data Management | u_mes_mast_line | lineType | Casting; Heat Treatment; Machining; Surface Treatment; Assembly; Inspection; Packing |
| Master Data Management | u_mes_mast_workCenter | workCenterType | Machine Station; Manual Station; Test Station; Inspection Station; Batch Process |
| Master Data Management | u_mes_mast_workCenter | trackingGrain | Lot; Unit; Container |
| Master Data Management | u_mes_mast_equipment | equipmentClass | Production Equipment; Test Equipment; Measuring Equipment; Utility |
| Master Data Management | u_mes_mast_equipment | controllerProtocol | OPC UA; Open Protocol; Modbus TCP; Profinet; MQTT; Ethernet/IP |
| Master Data Management | u_mes_mast_equipment | criticality | A; B; C |
| Master Data Management | u_mes_mast_equipment | currentState | Running; Idle; Setup; Down; Starved; Blocked; Planned Stop |
| Master Data Management | u_mes_mast_equipment | safetyCategory | PL a; PL b; PL c; PL d; PL e |
| Master Data Management | u_mes_mast_equipment | qualificationStatus | Qualified; Not Qualified; Requalification Due |
| Master Data Management | u_mes_mast_equipment | cleanStatus | Clean; Dirty; In Cleaning; Clean Hold Expired; Not Applicable |
| Master Data Management | u_mes_mast_shiftWorkingDay | workingDay | Monday; Tuesday; Wednesday; Thursday; Friday; Saturday; Sunday |
| Master Data Management | u_mes_mast_workCalendarWeeklyOffDay | weeklyOffDay | Monday; Tuesday; Wednesday; Thursday; Friday; Saturday; Sunday |
| Master Data Management | u_mes_mast_workCalendarException | exceptionType | Public Holiday; Plant Shutdown; Extra Working Day; Reduced Shift |
| Master Data Management | u_mes_mast_shiftRosterAssignment | roleInCrew | Operator; Setter; Line Leader; Quality Inspector; Material Handler |
| Master Data Management | u_mes_mast_shiftRosterAssignment | attendance | Present; Absent; Leave; Overtime |
| Master Data Management | u_mes_mast_shiftRosterAssignment | assignmentSource | Manual; Rule; Model |
| Master Data Management | u_mes_mast_role | scope | Enterprise; Site |
| Master Data Management | u_mes_mast_user | userType | Employee; Contractor; System |
| Master Data Management | u_mes_mast_skill | assessmentMethod | Practical Test; Written Test; Observation; On the Job |
| Master Data Management | u_mes_mast_skillCertification | assessmentMethod | Practical Test; Written Test; Observation; On the Job |
| Master Data Management | u_mes_mast_skillCertification | revocationSource | Expiry; Document Revision; Manual; Assessment Failure |
| Master Data Management | u_mes_mast_customer | customerType | OEM; Tier 1; Aftermarket |
| Master Data Management | u_mes_mast_customerContact | businessFunction | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| Master Data Management | u_mes_mast_supplier | supplierType | Direct Material; Indirect Material; Tooling; Service; Calibration Laboratory |
| Master Data Management | u_mes_mast_supplierContact | businessFunction | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| Master Data Management | u_mes_mast_supplierSuppliedItem | qualificationStatus | Qualified; Conditionally Approved; Disqualified |
| Master Data Management | u_mes_mast_unitOfMeasure | scope | Enterprise; Site |
| Master Data Management | u_mes_mast_unitOfMeasure | dimension | Count; Mass; Length; Torque; Pressure; Temperature; Time; Energy; Volume; Hardness; Leak Rate |
| Product Definition | u_mes_prod_item | itemType | Finished Good; Semi Finished; Purchased Component; Raw Material; Consumable; Packaging |
| Product Definition | u_mes_prod_item | procurementType | In House; Purchased; Subcontracted |
| Product Definition | u_mes_prod_productVariant | optionsHand | LH; RH |
| Product Definition | u_mes_prod_billOfMaterial | bomType | Production; Engineering; Rework |
| Product Definition | u_mes_prod_billOfMaterialComponent | traceLevel | None; Lot; Serial |
| Product Definition | u_mes_prod_operation | operationType | Casting; Heat Treatment; Machining; Cleaning; Surface Treatment; Assembly; Test; Marking; Inspection; Packing |
| Product Definition | u_mes_prod_operation | trackingGrain | Lot; Unit; Container |
| Product Definition | u_mes_prod_routing | routingType | Standard; Rework; Alternate |
| Product Definition | u_mes_prod_routingStepNextStep | nextStepCondition | Result OK; Result Not OK; Rework Complete; Always |
| Product Definition | u_mes_prod_billOfProcessStepInterlock | interlockType | Skill; Recipe; Tool Life; Gauge Calibration; Previous Step; Component Scan; Maintenance Due |
| Product Definition | u_mes_prod_workInstruction | generationSource | Manual; Generated From Bill Of Process; Generated By Model |
| Product Definition | u_mes_prod_workInstructionStep | inputType | None; Confirmation; Number; Text; Scan; Photo; Device Value |
| Product Definition | u_mes_prod_recipe | recipeType | Die Casting Parameters; Furnace Profile; CNC Program; Washing Program; Anodising Program; Tightening Program; Leak Test Program; Laser Marking Program; Press Program; Dispensing Program; Vision Job |
| Product Definition | u_mes_prod_recipe | origin | Engineering; Optimisation Model; Simulation Study |
| Product Definition | u_mes_prod_engineeringChange | changeType | Design Change; Process Change; Material Change; Supplier Change; Tooling Change; Document Change |
| Product Definition | u_mes_prod_engineeringChange | originator | Customer; Internal; Supplier |
| Product Definition | u_mes_prod_engineeringChange | effectivityType | Date; Serial Number; Lot; Stock Run Out |
| Product Definition | u_mes_prod_engineeringChange | regulatoryImpact | None; Customer Notification; Prior Approval |
| Product Definition | u_mes_prod_engineeringChangeAffectedObject | changeAction | Create; Update; Obsolete |
| Product Definition | u_mes_prod_engineeringChangeApproval | businessFunction | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| Product Definition | u_mes_prod_engineeringChangeApproval | decision | Approved; Rejected; Approved With Conditions |
| Product Definition | u_mes_prod_recipeControlledDocument | fileRole | Program File; Golden Image; Reference Curve; Parameter Export; Process Specification; Product Drawing; Verification Record |
| Planning and Execution | u_mes_plan_customerSchedule | scheduleType | Forecast; Delivery Schedule; Just In Time Call Off |
| Planning and Execution | u_mes_plan_customerScheduleLine | firmness | Firm; Forecast |
| Planning and Execution | u_mes_plan_productionOrder | orderType | Production; Rework; Trial; PPAP Run |
| Planning and Execution | u_mes_plan_productionOrder | priority | Low; Normal; High; Urgent |
| Planning and Execution | u_mes_plan_dispatchList | rule | Earliest Due Date; First In First Out; Critical Ratio; Priority |
| Planning and Execution | u_mes_plan_dispatchListEntry | priority | Low; Normal; High; Urgent |
| Planning and Execution | u_mes_plan_operationExecution | executionType | Production; Rework; Retest; Setup |
| Planning and Execution | u_mes_plan_operationExecution | result | OK; Not OK |
| Planning and Execution | u_mes_plan_operationExecution | captureMethod | Scan; PLC Signal; Manual Entry |
| Planning and Execution | u_mes_plan_stepCompletion | inputType | None; Confirmation; Number; Text; Scan; Photo; Device Value |
| Planning and Execution | u_mes_plan_stepCompletion | deviceSource | Manual Entry; Scanner; Nutrunner Controller; Leak Tester; Gauge Interface; PLC; AR Headset |
| Planning and Execution | u_mes_plan_wipUnit | qualityStatus | Released; Under Inspection; On Hold; Rejected |
| Planning and Execution | u_mes_plan_lot | lotType | Supplier Lot; Melt Lot; Casting Lot; Heat Treatment Charge; Machining Lot; Anodising Load; Finished Goods Lot |
| Planning and Execution | u_mes_plan_lot | qualityStatus | Released; Under Inspection; On Hold; Rejected |
| Planning and Execution | u_mes_plan_labourBooking | bookingType | Direct; Indirect |
| Planning and Execution | u_mes_plan_labourBooking | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Planning and Execution | u_mes_plan_changeover | changeoverType | Variant Change; Item Change; Tool Change; Die Change |
| Planning and Execution | u_mes_plan_changeoverStep | internalExternal | Internal; External |
| Planning and Execution | u_mes_plan_andonEvent | severityClass | Low; Medium; High; Critical |
| Planning and Execution | u_mes_plan_andonEventEscalation | channel | Screen; Email; SMS; Mobile Push |
| Planning and Execution | u_mes_plan_operatorSession | authenticationMethod | Badge; Biometric; Badge And PIN; Password |
| Planning and Execution | u_mes_plan_operatorSession | logoutReason | Operator Logout; Shift End; Timeout; Supervisor Logout; Skill Revoked |
| Planning and Execution | u_mes_plan_documentAcknowledgement | relatedCollectionName | u_mes_prod_workInstruction; u_mes_prod_recipe; u_mes_syst_controlledDocument |
| Planning and Execution | u_mes_plan_documentAcknowledgement | acknowledgementType | First Read; Revision Re-acknowledgement; Shift Start; Periodic Refresh |
| Planning and Execution | u_mes_plan_documentAcknowledgement | method | Touch Confirmation; Badge Scan; AR Confirmation; Electronic Signature |
| Planning and Execution | u_mes_plan_recipeDownload | trigger | Order Start; Changeover; Operator Request; Revision Release; Controller Reconnect |
| Planning and Execution | u_mes_plan_recipeDownload | verificationResult | Match; Mismatch; No Response; Version Not Released |
| Planning and Execution | u_mes_plan_setupVerification | trigger | Order Start; Changeover; Shift Start; After Maintenance |
| Planning and Execution | u_mes_plan_setupVerificationItem | checkType | Variant; Fixture; Tool; Program; Parameter; Component; Gauge |
| Planning and Execution | u_mes_plan_lineClearance | clearanceType | Before Order Start; Order Changeover; After Order Completion; After Maintenance |
| Material Management | u_mes_matl_storageLocation | locationType | Warehouse Rack; Line Side; Quarantine; Dispatch Bay; Receiving Bay; Tool Crib; Scrap Yard |
| Material Management | u_mes_matl_materialMovement | scanSource | Handheld Scanner; Fixed Scanner; Manual Entry |
| Material Management | u_mes_matl_goodsReceiptLine | inspectionStatus | Pending; Accepted; Rejected; Accepted Under Deviation |
| Material Management | u_mes_matl_kit | kitType | Order Kit; Shift Kit; Rework Kit |
| Material Management | u_mes_matl_kitLine | verificationResult | Match; Wrong Item; Wrong Revision; Wrong Quantity; Not Scanned |
| Material Management | u_mes_matl_materialRequest | requestType | Kanban; Andon Call; Manual |
| Material Management | u_mes_matl_materialRequest | triggerSource | Minimum Level Sensor; Operator; Schedule |
| Material Management | u_mes_matl_materialRequest | priority | Low; Normal; High; Urgent |
| Material Management | u_mes_matl_materialConsumption | consumptionType | Scanned; Backflush; Manual |
| Material Management | u_mes_matl_labelTemplate | labelType | Unit Mark; Container Label; Shipping Label; Hold Tag; Location Label |
| Material Management | u_mes_matl_labelTemplate | printerLanguage | ZPL; EPL; PDF |
| Material Management | u_mes_matl_labelTemplate | symbology | Data Matrix ECC200; QR Code; Code 128; Code 39; PDF417 |
| Material Management | u_mes_matl_labelTemplateField | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Material Management | u_mes_matl_label | labelType | Unit Mark; Container Label; Shipping Label; Hold Tag; Location Label |
| Material Management | u_mes_matl_label | verificationGrade | A; B; C; D; F |
| Material Management | u_mes_matl_movementType | stockEffect | Increase; Decrease; Transfer; None |
| Material Management | u_mes_matl_exposureTimer | timerType | Floor Life; Pot Life; Open Time; Bake; Dirty Equipment Hold; Clean Equipment Hold; Process Hold Time |
| Material Management | u_mes_matl_replenishmentRule | triggerType | Consumption; Kanban Scan; Min-Max; Order Demand |
| Material Management | u_mes_matl_materialDemandForecast | method | Schedule; Consumption Rate; Model |
| Material Management | u_mes_matl_dispenseRecord | dispenseMethod | Gravimetric Weighing; Count By Weight |
| Material Management | u_mes_matl_dispenseRecord | verificationMethod | Second Person; System Check |
| Traceability | u_mes_trac_serialNumber | markGrade | A; B; C; D; F |
| Traceability | u_mes_trac_genealogyLink | childType | Lot; Serial |
| Traceability | u_mes_trac_genealogyLink | linkType | Assembled; Replaced; Split; Merge; Transformed |
| Traceability | u_mes_trac_componentLotLink | linkType | Assembled; Replaced; Split; Merge; Transformed |
| Traceability | u_mes_trac_asBuiltRecord | leakTestVerdict | Pass; Fail |
| Traceability | u_mes_trac_asBuiltRecordOperation | result | OK; Not OK |
| Traceability | u_mes_trac_traceInvestigation | direction | Forward; Reverse; Both |
| Traceability | u_mes_trac_traceInvestigation | relatedCollectionName | u_mes_trac_serialNumber; u_mes_plan_lot; u_mes_plan_wipUnit; u_mes_plan_container; u_mes_matl_shipment |
| Traceability | u_mes_trac_traceInvestigationResult | relatedCollectionName | u_mes_trac_serialNumber; u_mes_plan_lot; u_mes_plan_wipUnit; u_mes_plan_container; u_mes_matl_shipment |
| Quality Management | u_mes_qual_characteristic | characteristicType | Product; Process |
| Quality Management | u_mes_qual_characteristic | classification | Critical; Significant; Standard |
| Quality Management | u_mes_qual_characteristic | dataType | Variable; Attribute |
| Quality Management | u_mes_qual_characteristic | toleranceType | Bilateral; Unilateral Upper; Unilateral Lower |
| Quality Management | u_mes_qual_characteristic | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Quality Management | u_mes_qual_controlPlan | phase | Prototype; Pre Launch; Production |
| Quality Management | u_mes_qual_controlPlanLine | classification | Critical; Significant; Standard |
| Quality Management | u_mes_qual_inspectionPlan | planType | Incoming; In Process; First Off; Final; Dock Audit; Layout |
| Quality Management | u_mes_qual_inspectionPlan | collectionTrigger | Operation Start; Operation Complete; Time Interval; Unit Count; Goods Receipt; Changeover |
| Quality Management | u_mes_qual_inspectionPlanLine | frequencyType | Every Unit; Every N Units; Every N Minutes; Per Lot; Per Shift; First Off |
| Quality Management | u_mes_qual_inspectionPlanLine | recordType | Measured Value; Pass Fail; Count |
| Quality Management | u_mes_qual_samplingPlan | samplingType | Attribute AQL; Fixed Sample; Hundred Percent; Skip Lot |
| Quality Management | u_mes_qual_samplingPlan | inspectionLevel | S-1; S-2; S-3; S-4; I; II; III |
| Quality Management | u_mes_qual_samplingPlan | frequencyType | Every Unit; Every N Units; Every N Minutes; Per Lot; Per Shift; First Off |
| Quality Management | u_mes_qual_checkSheet | checkSheetType | Start Of Shift; Poka Yoke Verification; First Off Approval; Autonomous Maintenance; Layered Process Audit; Changeover |
| Quality Management | u_mes_qual_checkSheet | frequency | Per Shift; Daily; Weekly; Per Changeover; Per Lot |
| Quality Management | u_mes_qual_checkSheetItem | answerType | Yes No; Number; Text |
| Quality Management | u_mes_qual_checkSheetResult | overallResult | Pass; Fail |
| Quality Management | u_mes_qual_inspectionResult | inspectionType | Incoming; In Process; First Off; Final; Audit |
| Quality Management | u_mes_qual_inspectionResult | attributeResult | Pass; Fail |
| Quality Management | u_mes_qual_inspectionResult | result | OK; Not OK |
| Quality Management | u_mes_qual_inspectionResult | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Quality Management | u_mes_qual_spcChart | chartType | X-bar R; X-bar S; I-MR; p; np; c; u |
| Quality Management | u_mes_qual_spcChartRule | rule | Earliest Due Date; First In First Out; Critical Ratio; Priority |
| Quality Management | u_mes_qual_spcSample | reactionType | Alert; Hold; Recheck; Stop Line |
| Quality Management | u_mes_qual_spcSampleViolation | rule | Earliest Due Date; First In First Out; Critical Ratio; Priority |
| Quality Management | u_mes_qual_defectCode | scrapCostCategory | Casting Scrap; Machining Scrap; Assembly Scrap; Supplier Chargeable |
| Quality Management | u_mes_qual_nonconformance | ncType | Internal; Supplier; Customer |
| Quality Management | u_mes_qual_nonconformance | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Quality Management | u_mes_qual_nonconformance | deviationClass | Minor; Major; Critical |
| Quality Management | u_mes_qual_reworkOrder | reworkType | Replace Component; Retighten; Re-machine; Re-anodise; Re-mark; Clean |
| Quality Management | u_mes_qual_reworkOrder | reinspectionResult | Pass; Fail |
| Quality Management | u_mes_qual_scrapRecord | scrapType | Process Scrap; Setup Scrap; Material Defect; Destructive Test |
| Quality Management | u_mes_qual_scrapRecord | disposalMethod | Remelt; Sell As Scrap; Return To Supplier |
| Quality Management | u_mes_qual_qualityHold | holdType | Quality; Customer; Engineering; Supplier |
| Quality Management | u_mes_qual_qualityHold | releaseDecision | Released; Rework; Scrap; Return To Supplier |
| Quality Management | u_mes_qual_qualityHoldHeldObject | releaseDecision | Released; Rework; Scrap; Return To Supplier |
| Quality Management | u_mes_qual_deviationPermit | deviationType | Product; Process; Material |
| Quality Management | u_mes_qual_deviationPermit | limitType | Quantity; Date |
| Quality Management | u_mes_qual_deviationPermitApproval | businessFunction | Quality; Purchasing; Logistics; Engineering; Production; Finance |
| Quality Management | u_mes_qual_deviationPermitApproval | decision | Approved; Rejected; Approved With Conditions |
| Quality Management | u_mes_qual_capa | capaType | Corrective; Preventive |
| Quality Management | u_mes_qual_capa | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Quality Management | u_mes_qual_capa | d4RootCauseMethod | 5 Why; Fishbone; Fault Tree; Is Is Not |
| Quality Management | u_mes_qual_capa | currentDiscipline | D1; D2; D3; D4; D5; D6; D7; D8 |
| Quality Management | u_mes_qual_capaTeamMember | roleInTeam | Champion; Leader; Member |
| Quality Management | u_mes_qual_pfmea | methodology | AIAG-VDA; AIAG 4th Edition |
| Quality Management | u_mes_qual_pfmeaLine | classification | Critical; Significant; Standard |
| Quality Management | u_mes_qual_pfmeaLine | actionPriority | High; Medium; Low |
| Quality Management | u_mes_qual_ppapSubmission | submissionReason | Initial Submission; Engineering Change; Tooling Transfer; Correction Of Discrepancy; Tooling Inactive Over One Year; Sub Supplier Change |
| Quality Management | u_mes_qual_ppapSubmission | customerDecision | Approved; Interim Approved; Rejected |
| Quality Management | u_mes_qual_gauge | calibrationSource | Internal; External |
| Quality Management | u_mes_qual_gaugeCalibration | calibrationType | Initial; Periodic; After Repair; After Shock Or Damage; Automatic Closed Loop; Daily Performance Check |
| Quality Management | u_mes_qual_gaugeCalibration | asFoundResult | Within Tolerance; Out Of Tolerance |
| Quality Management | u_mes_qual_gaugeCalibration | asLeftResult | Within Tolerance; Out Of Tolerance |
| Quality Management | u_mes_qual_gaugeCalibration | overallResult | Pass; Fail |
| Quality Management | u_mes_qual_msaStudy | studyType | Gauge R and R; Bias; Linearity; Stability; Attribute Agreement |
| Quality Management | u_mes_qual_msaStudy | studyMethod | ANOVA; Average And Range; Kappa |
| Quality Management | u_mes_qual_msaStudy | conclusion | Acceptable; Conditionally Acceptable; Not Acceptable |
| Quality Management | u_mes_qual_audit | auditType | Layered Process Audit; Process Audit; Product Audit; System Audit; Customer Audit; Supplier Audit |
| Quality Management | u_mes_qual_audit | overallRating | A; B; C |
| Quality Management | u_mes_qual_auditFinding | grade | Major; Minor; Observation; Opportunity For Improvement |
| Quality Management | u_mes_qual_customerComplaintCommunication | direction | Inbound; Outbound |
| Quality Management | u_mes_qual_curveEnvelope | curveType | Force Displacement; Torque Angle; Pressure Time; Sound Spectrum; Vibration Acceleration |
| Quality Management | u_mes_qual_curveEnvelopeWindow | windowType | Box; Upper Band; Lower Band; Peak; Final Value |
| Quality Management | u_mes_qual_curveEnvelopeWindow | entrySide | Left; Right; Top; Bottom |
| Quality Management | u_mes_qual_curveEnvelopeWindow | exitSide | Left; Right; Top; Bottom |
| Quality Management | u_mes_qual_measurementCurve | result | OK; NOK |
| Quality Management | u_mes_qual_defectRecord | fourMCategory | Man; Machine; Material; Method |
| Quality Management | u_mes_qual_auditSchedule | auditType | Layered Process Audit; Product Audit; Process Audit; 5S Audit |
| Quality Management | u_mes_qual_auditSchedule | frequencyType | Shift; Daily; Weekly; Monthly |
| Quality Management | u_mes_qual_environmentalMonitoringPoint | monitoredParameter | Temperature; Relative Humidity; Differential Pressure; Airborne Particles 0.5 um; Airborne Particles 5.0 um; Surface Particle Count; Illuminance |
| Quality Management | u_mes_qual_environmentalMonitoringPoint | limitDirection | Upper; Lower; Range |
| Quality Management | u_mes_qual_environmentalMonitoringPoint | samplingFrequency | Continuous; Every Shift; Daily; Weekly |
| Quality Management | u_mes_qual_environmentalMonitoringResult | limitEvaluation | Within Limits; Alert Limit Exceeded; Action Limit Exceeded |
| Quality Management | u_mes_qual_retentionSample | sampleType | Reserve Sample; Retention Sample; Master Sample; Boundary Sample |
| Quality Management | u_mes_qual_riskAssessment | relatedCollectionName | u_mes_prod_engineeringChange; u_mes_syst_computerisedSystem; u_mes_qual_nonconformance; u_mes_mast_equipment; u_mes_prod_item |
| Quality Management | u_mes_qual_riskAssessment | assessmentMethod | FMEA; Risk Ranking And Filtering; Fault Tree Analysis; HACCP; Preliminary Hazard Analysis |
| Quality Management | u_mes_qual_riskAssessment | initialRiskLevel | Low; Medium; High |
| Quality Management | u_mes_qual_riskAssessment | residualRiskLevel | Low; Medium; High |
| Quality Management | u_mes_qual_riskAssessment | acceptanceDecision | Accepted; Accepted With Controls; Not Accepted |
| Quality Management | u_mes_qual_productRecall | recallClass | Class I; Class II; Class III |
| Quality Management | u_mes_qual_productRecall | recallScope | Customer Plant; Distributor; Field |
| Quality Management | u_mes_qual_processValidation | validationStage | Stage 1 Process Design; Stage 2 Process Qualification; Stage 3 Continued Process Verification |
| Performance Management | u_mes_perf_reasonCode | reasonType | Downtime; Scrap; Hold; Andon; Changeover Loss; Hold Release; Interlock Override; Rework; Root Cause; Alarm Closure; Exposure Reset |
| Performance Management | u_mes_perf_reasonCode | oeeImpact | Availability; Performance; Quality; None |
| Performance Management | u_mes_perf_equipmentState | stateCode | Running; Idle; Setup; Down; Starved; Blocked; Planned Stop |
| Performance Management | u_mes_perf_equipmentState | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Performance Management | u_mes_perf_downtimeEvent | downtimeType | Planned; Unplanned |
| Performance Management | u_mes_perf_downtimeEvent | captureSource | Equipment Signal; Operator Entry; Andon |
| Performance Management | u_mes_perf_productionCount | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| Performance Management | u_mes_perf_processTag | dataType | Variable; Attribute |
| Performance Management | u_mes_perf_processTag | tagClass | Process Value; Setpoint; Counter; State; Alarm Bit; Energy; Environment |
| Performance Management | u_mes_perf_processTag | aggregation | None; Average; Minimum; Maximum; Last; Sum |
| Performance Management | u_mes_perf_processReading | signalQuality | Good; Uncertain; Bad |
| Performance Management | u_mes_perf_alarm | alarmClass | Process; Machine; Safety; Quality |
| Performance Management | u_mes_perf_torqueResult | strategy | Torque Control; Torque Control Angle Monitor; Angle Control Torque Monitor; Yield Control |
| Performance Management | u_mes_perf_torqueResult | result | OK; Not OK |
| Performance Management | u_mes_perf_torqueResult | envelopeResult | OK; NOK |
| Performance Management | u_mes_perf_leakTestResult | testMedium | Dry Air; Nitrogen; Helium |
| Performance Management | u_mes_perf_leakTestResult | verdict | Pass; Fail |
| Performance Management | u_mes_perf_leakTestResultStage | stageName | Low Pressure; High Pressure |
| Performance Management | u_mes_perf_leakTestResultStage | stageResult | Pass; Fail |
| Performance Management | u_mes_perf_energyReading | signalQuality | Good; Uncertain; Bad |
| Performance Management | u_mes_perf_lossCategory | oeeImpact | Availability; Performance; Quality; None |
| Performance Management | u_mes_perf_alarmDefinition | alarmClass | Process; Equipment; Safety; Quality; Utility |
| Performance Management | u_mes_perf_alarmDefinition | severityClass | Low; Medium; High; Critical |
| Tooling & Maintenance | u_mes_maint_maintenancePlan | planType | Incoming; In Process; First Off; Final; Dock Audit; Layout |
| Tooling & Maintenance | u_mes_maint_maintenancePlan | strategy | Torque Control; Torque Control Angle Monitor; Angle Control Torque Monitor; Yield Control |
| Tooling & Maintenance | u_mes_maint_maintenancePlan | intervalType | Calendar; Counter; Condition |
| Tooling & Maintenance | u_mes_maint_maintenancePlan | intervalUom | Days; Weeks; Months; Cycles; Shots; Run Hours |
| Tooling & Maintenance | u_mes_maint_maintenanceWorkOrder | workOrderType | Breakdown; Preventive; Predictive; Improvement; Calibration |
| Tooling & Maintenance | u_mes_maint_maintenanceWorkOrder | priority | Low; Normal; High; Urgent |
| Tooling & Maintenance | u_mes_maint_maintenanceWorkOrder | schedulingSource | Manual; Rule; Model |
| Tooling & Maintenance | u_mes_maint_sparePart | category | Mechanical; Electrical; Process; Material; Quality; Organisation; Planned |
| Tooling & Maintenance | u_mes_maint_sparePart | criticality | A; B; C |
| Tooling & Maintenance | u_mes_maint_tool | toolClass | Production Tooling; Customer Owned Tooling; Consumable Tooling; Fixture |
| Tooling & Maintenance | u_mes_maint_tool | lifeUom | Shots; Cycles; Pieces; Run Hours |
| Tooling & Maintenance | u_mes_maint_toolLifeRecord | eventType | Mounted; Usage; Dismounted; Regrind; Maintenance; Scrapped |
| Tooling & Maintenance | u_mes_maint_toolType | lifeUom | Shots; Cycles; Pieces; Run Hours |
| Tooling & Maintenance | u_mes_maint_maintenanceWorkOrderTask | result | Done OK; Done Not OK; Not Applicable; Not Done |
| Tooling & Maintenance | u_mes_maint_sparePartTransaction | transactionType | Issue; Return; Receipt; Adjustment; Scrap |
| Tooling & Maintenance | u_mes_maint_reliabilitySummary | periodType | Shift; Day; Week; Month |
| Tooling & Maintenance | u_mes_maint_equipmentLifecycleEvent | eventType | Commissioning; Relocation; Overhaul; Refurbishment; Upgrade; Health Assessment; Replacement Recommendation; Decommissioning |
| Tooling & Maintenance | u_mes_maint_logbookEntry | relatedCollectionName | u_mes_mast_equipment; u_mes_mast_area |
| Tooling & Maintenance | u_mes_maint_logbookEntry | activityType | Production; Cleaning; Maintenance; Calibration; Line Clearance; Qualification; Idle |
| Tooling & Maintenance | u_mes_maint_cleaningRecord | cleaningType | Minor Cleaning; Major Cleaning; Product Changeover Cleaning; Bath Change |
| Tooling & Maintenance | u_mes_maint_cleaningRecord | verificationMethod | Visual Inspection; Cleanliness Test; Rinse Sample; Swab Sample |
| Tooling & Maintenance | u_mes_maint_cleaningRecord | verificationResult | Pass; Fail |
| Tooling & Maintenance | u_mes_maint_equipmentQualification | qualificationPhase | Design Qualification; Installation Qualification; Operational Qualification; Performance Qualification; Periodic Requalification |
| System and Integration | u_mes_syst_erpMessage | direction | Inbound; Outbound; Publish |
| System and Integration | u_mes_syst_erpMessage | messageType | Production Order Download; Operation Confirmation; Goods Movement; Goods Receipt; Shipment Advice; Material Master; Quality Notification |
| System and Integration | u_mes_syst_erpMessage | payloadFormat | JSON; XML; IDoc |
| System and Integration | u_mes_syst_integrationConnector | connectorType | ERP; PLM; OPC UA Server; Tool Controller; Label Printer; Leak Tester; Email Gateway |
| System and Integration | u_mes_syst_integrationConnector | protocol | HTTPS REST; OPC UA; Open Protocol; Modbus TCP; MQTT; ZPL Over TCP; SMTP |
| System and Integration | u_mes_syst_integrationConnector | environment | Production; Quality; Development |
| System and Integration | u_mes_syst_integrationConnector | authMethod | OAuth2 Client Credentials; Certificate; Basic; None |
| System and Integration | u_mes_syst_integrationConnector | healthStatus | Healthy; Degraded; Down |
| System and Integration | u_mes_syst_integrationConnectorFunction | direction | Inbound; Outbound; Publish |
| System and Integration | u_mes_syst_integrationConnectorFunction | messageType | Production Order Download; Operation Confirmation; Goods Movement; Goods Receipt; Shipment Advice; Material Master; Quality Notification |
| System and Integration | u_mes_syst_iotDevice | protocol | HTTPS REST; OPC UA; Open Protocol; Modbus TCP; MQTT; ZPL Over TCP; SMTP |
| System and Integration | u_mes_syst_iotDevice | connectionStatus | Online; Offline; Degraded |
| System and Integration | u_mes_syst_operatorApp | appType | Operator Station; Inspection; Material Handling; Maintenance; Andon Board |
| System and Integration | u_mes_syst_operatorAppStep | widgetType | Work Instruction; Data Entry; Device Result; Scan; Checklist; Signature; Summary |
| System and Integration | u_mes_syst_operatorAppStepTrigger | triggerEvent | Step Opened; Button Pressed; Scan Completed; Device Result Received; Value Out Of Limit; Timer Expired |
| System and Integration | u_mes_syst_operatorAppStepTrigger | triggerAction | Go To Step; Complete Operation; Raise Nonconformance; Raise Andon; Print Label; Block Station |
| System and Integration | u_mes_syst_operatorAppDeviceBinding | purpose | Tightening result; Leak test result; Component scan; Label print; Measurement |
| System and Integration | u_mes_syst_businessEvent | eventType | Order Released; Operation Started; Operation Completed; Recipe Downloaded; Hold Placed; Hold Released; Label Printed; Unit Scrapped; Shipment Dispatched; User Logged In |
| System and Integration | u_mes_syst_businessEvent | eventCategory | Execution; Quality; Material; Maintenance; Integration; Security |
| System and Integration | u_mes_syst_businessEvent | source | MES Terminal; PLC; Scanner; ERP; Device; Manual Entry |
| System and Integration | u_mes_syst_auditTrail | changeAction | Create; Update; Obsolete |
| System and Integration | u_mes_syst_electronicSignature | authenticationMethod | Password; Password And Badge; Single Sign On |
| System and Integration | u_mes_syst_notificationRecipient | channel | Screen; Email; SMS; Mobile Push |
| System and Integration | u_mes_syst_controlledDocument | storageProvider | S3; GridFS; File Share |
| System and Integration | u_mes_syst_numberRange | rangeType | Serial Number; Lot Number; Order Number; Label Number; Document Number |
| System and Integration | u_mes_syst_numberRange | resetPolicy | Never; Daily; Monthly; Yearly |
| System and Integration | u_mes_syst_numberRange | checkDigitMethod | None; Modulo 10; Modulo 43 |
| System and Integration | u_mes_syst_systemConfiguration | module | Master Data; Product Definition; Execution; Materials; Traceability; Quality; Performance; Maintenance; Integration; Safety |
| System and Integration | u_mes_syst_systemConfiguration | valueType | Text; Number; Flag; JSON |
| System and Integration | u_mes_syst_systemConfiguration | scope | Enterprise; Site |
| System and Integration | u_mes_syst_interlockRule | ruleType | Hold Check; Sequence Check; Mandatory Scan; Duplicate Serial; Wrong Order; Wrong Station; Variant Check; Component Lot Capture; Lot Release Check; Expiry Check; Kit Completeness; Genealogy Completeness; Recipe Release Check; Program Version Check; Work Instruction Release Check; Acknowledgement Check; Mandatory Inspection; NOK Result; Skill Check; Login Check; Equipment Readiness; Tool Life; Calibration Check; Environment Check; Setup Check; Alarm Restart; Line Clearance Check; Batch Release Check; Equipment Clean Status Check; Qualification Status Check; Dispense Tolerance Check |
| System and Integration | u_mes_syst_interlockRule | transactionPoint | Operation Start; Operation Complete; Material Issue; Kit Release; Pack Out; Dispatch; Order Close; Login; Inspection Accept |
| System and Integration | u_mes_syst_interlockRule | enforcementMode | Warning; Block |
| System and Integration | u_mes_syst_escalationRule | sourceType | Interlock; Andon; Alarm; Alert Rule; Breakdown; Audit; Nonconformance; Customer Complaint |
| System and Integration | u_mes_syst_escalationRule | severityClass | Low; Medium; High; Critical |
| System and Integration | u_mes_syst_escalationRuleLevel | basis | Not Acknowledged; Not Resolved |
| System and Integration | u_mes_syst_escalationRuleLevel | channel | Andon Board; SMS; Email; Mobile App; Public Address |
| System and Integration | u_mes_syst_alertRule | metric | OEE; Availability; Downtime Minutes; Reject Rate; Output Gap; Process Deviation; SPC Rule Violation; Line-side Stock Cover; Environment Limit; Model Anomaly Score |
| System and Integration | u_mes_syst_alertRule | comparison | Less Than; Greater Than; Outside Band |
| System and Integration | u_mes_syst_alertRule | severityClass | Low; Medium; High; Critical |
| System and Integration | u_mes_syst_alertRule | actionType | Notify; Hold; Stop Equipment; Block Process; Create Work Order; Create Nonconformance |
| System and Integration | u_mes_syst_analyticsModel | modelType | Vision Classification; Defect Prediction; OEE Forecast; Anomaly Detection; Maintenance Prediction; Demand Forecast; Recipe Optimisation; Operator Risk; Assignment Recommendation |
| System and Integration | u_mes_syst_modelPrediction | predictionType | Classification; Forecast; Anomaly; Maintenance Priority; Remaining Useful Life; Recommendation; Operator Risk; Assignment Recommendation |
| System and Integration | u_mes_syst_modelPrediction | actionStatus | Not Required; Pending; Approved; Applied; Rejected |
| System and Integration | u_mes_syst_simulationStudy | studyType | Process; Inventory; Equipment; Calibration Baseline |
| System and Integration | u_mes_syst_simulationStudy | comparisonResult | Better; Equal; Worse |
| System and Integration | u_mes_syst_recordPolicy | editPolicy | Free Edit; Controlled Edit; No Edit After Lock; Append Only |
| System and Integration | u_mes_syst_savedView | viewType | Dashboard; Comparison; Pareto; Trend; List |
| System and Integration | u_mes_syst_backupRun | runType | Full Backup; Incremental Backup; Restore Test; Failover Test |
| System and Integration | u_mes_syst_computerisedSystem | systemCategory | Manufacturing Execution System; Equipment Controller; Laboratory System; ERP Interface; Label Printing; Data Historian; Infrastructure |
| System and Integration | u_mes_syst_computerisedSystem | gampCategory | Category 1; Category 3; Category 4; Category 5 |
| System and Integration | u_mes_syst_computerisedSystem | gxpImpact | Direct; Indirect; None |
| System and Integration | u_mes_syst_computerisedSystem | dataCriticality | High; Medium; Low |
| System and Integration | u_mes_syst_computerisedSystem | hostingModel | On Premise; Private Cloud; Supplier Hosted; Embedded |
| System and Integration | u_mes_syst_systemValidation | validationType | Initial Validation; Change Revalidation; Retrospective Validation; Decommissioning |
| System and Integration | u_mes_syst_systemValidation | assuranceApproach | Scripted Testing; Unscripted Testing; Ad Hoc Testing; Supplier Assurance |
| System and Integration | u_mes_syst_auditTrailReview | reviewType | Batch Record Review; Periodic System Review; For Cause |
| System and Integration | u_mes_syst_auditTrailReview | relatedCollectionName | u_mes_plan_productionOrder; u_mes_syst_systemPeriodicReview; u_mes_qual_nonconformance |
| System and Integration | u_mes_syst_userAccessReviewLine | reviewAction | Retain; Remove Role; Change Role; Lock Account |
| Batch Manufacturing Record | u_mes_bmr_batchRecordReview | reviewScope | Review By Exception; Full Review |
| Batch Manufacturing Record | u_mes_bmr_batchRecordReviewException | exceptionType | Interlock Override; Out Of Specification Result; Manual Data Entry; Data Correction; Missing Signature; Deviation; Late Entry; Hold |
| Batch Manufacturing Record | u_mes_bmr_batchRecordReviewException | relatedCollectionName | u_mes_plan_interlockEvent; u_mes_qual_inspectionResult; u_mes_syst_auditTrail; u_mes_qual_nonconformance; u_mes_qual_qualityHold; u_mes_plan_operationExecution |
| Batch Manufacturing Record | u_mes_bmr_batchRecordReviewException | assessment | No Impact; Impact Assessed Acceptable; Requires Deviation; Requires Correction |
| Batch Manufacturing Record | u_mes_bmr_yieldReconciliation | reconciliationType | Product Yield; Component Reconciliation; Label Reconciliation |
