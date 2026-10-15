# Status values per collection

Model version 2.9 | 12 October 2026 | 369 collections (200 entity, 85 child, 76 relationship, 8 value-list), 8614 keys

Each collection with a lifecycle defines its own `status` values. The first value is the initial state. The values are stored as master data in `u_mes_syst_statusDefinition` (one document per collection and value) and the allowed moves in `u_mes_syst_statusTransition`. Collections not listed have no `status` key.

| Module | Collection | Status values (in order) |
|---|---|---|
| MasterDataManagement | u_mes_mast_enterprise | Active, Inactive |
| MasterDataManagement | u_mes_mast_site | Active, Inactive |
| MasterDataManagement | u_mes_mast_area | Active, Inactive |
| MasterDataManagement | u_mes_mast_line | Active, Inactive |
| MasterDataManagement | u_mes_mast_workCenter | Active, Inactive |
| MasterDataManagement | u_mes_mast_equipment | Active, Under Maintenance, Decommissioned |
| MasterDataManagement | u_mes_mast_shift | Active, Inactive |
| MasterDataManagement | u_mes_mast_workCalendar | Active, Inactive |
| MasterDataManagement | u_mes_mast_shiftRoster | Planned, Published, Closed |
| MasterDataManagement | u_mes_mast_role | Active, Inactive |
| MasterDataManagement | u_mes_mast_user | Active, Suspended, Left |
| MasterDataManagement | u_mes_mast_skill | Active, Inactive |
| MasterDataManagement | u_mes_mast_skillCertification | Valid, Expiring Soon, Expired, Revoked |
| MasterDataManagement | u_mes_mast_customer | Active, Inactive |
| MasterDataManagement | u_mes_mast_supplier | Approved, Conditional, Blocked, Inactive |
| MasterDataManagement | u_mes_mast_unitOfMeasure | Active, Inactive |
| MasterDataManagement | u_mes_mast_department | Active, Inactive |
| MasterDataManagement | u_mes_mast_designation | Active, Inactive |
| MasterDataManagement | u_mes_mast_employmentType | Active, Inactive |
| MasterDataManagement | u_mes_mast_costCenter | Active, Inactive |
| MasterDataManagement | u_mes_mast_manufacturer | Active, Inactive |
| MasterDataManagement | u_mes_mast_equipmentType | Active, Inactive |
| MasterDataManagement | u_mes_mast_skillCategory | Active, Inactive |
| MasterDataManagement | u_mes_mast_permission | Active, Inactive |
| MasterDataManagement | u_mes_mast_signatureMeaning | Active, Inactive |
| MasterDataManagement | u_mes_mast_currency | Active, Inactive |
| MasterDataManagement | u_mes_mast_country | Active, Inactive |
| MasterDataManagement | u_mes_mast_language | Active, Inactive |
| MasterDataManagement | u_mes_mast_transporter | Active, Inactive |
| MasterDataManagement | u_mes_mast_commodity | Active, Inactive |
| ProductDefinition | u_mes_prod_item | Active, Phase Out, Obsolete |
| ProductDefinition | u_mes_prod_productVariant | In Preparation, Released, Obsolete |
| ProductDefinition | u_mes_prod_billOfMaterial | In Preparation, Released, Obsolete |
| ProductDefinition | u_mes_prod_operation | Active, Inactive |
| ProductDefinition | u_mes_prod_routing | In Preparation, Released, Obsolete |
| ProductDefinition | u_mes_prod_billOfProcess | In Preparation, Released, Obsolete |
| ProductDefinition | u_mes_prod_workInstruction | In Preparation, Released, Obsolete |
| ProductDefinition | u_mes_prod_recipe | In Preparation, Released, Obsolete |
| ProductDefinition | u_mes_prod_engineeringChange | Raised, Under Evaluation, Approved, Implemented, Closed, Rejected |
| ProductDefinition | u_mes_prod_itemGroup | Active, Inactive |
| ProductDefinition | u_mes_prod_itemFamily | Active, Inactive |
| ProductDefinition | u_mes_prod_ppeItem | Active, Inactive |
| ProductDefinition | u_mes_prod_market | Active, Inactive |
| ProductDefinition | u_mes_prod_padCompound | Active, Inactive |
| ProductDefinition | u_mes_prod_surfaceFinish | Active, Inactive |
| ProductDefinition | u_mes_prod_vehicleModel | Active, Inactive |
| PlanningAndExecution | u_mes_plan_customerSchedule | Received, Confirmed, Partially Shipped, Completed, Replaced |
| PlanningAndExecution | u_mes_plan_productionOrder | Created, Released, In Progress, On Hold, Completed, Closed, Cancelled |
| PlanningAndExecution | u_mes_plan_productionSchedule | Planned, Published, In Progress, Completed |
| PlanningAndExecution | u_mes_plan_dispatchList | Generated, Acknowledged, Closed |
| PlanningAndExecution | u_mes_plan_dispatchListEntry | Queued, Started, Completed, Skipped |
| PlanningAndExecution | u_mes_plan_operationExecution | Started, Completed, Aborted |
| PlanningAndExecution | u_mes_plan_stepCompletion | Completed, Skipped, Overridden |
| PlanningAndExecution | u_mes_plan_wipUnit | Created, In Process, On Hold, In Rework, Completed, Packed, Shipped, Scrapped |
| PlanningAndExecution | u_mes_plan_lot | Created, Available, In Process, On Hold, Consumed, Closed, Rejected |
| PlanningAndExecution | u_mes_plan_container | Empty, Filling, Full, Sealed, Shipped, Returned, Under Repair |
| PlanningAndExecution | u_mes_plan_labourBooking | Open, Closed, Approved |
| PlanningAndExecution | u_mes_plan_changeover | Planned, In Progress, Awaiting First Off Approval, Completed |
| PlanningAndExecution | u_mes_plan_shiftHandover | Open, Handed Over, Acknowledged |
| PlanningAndExecution | u_mes_plan_andonEvent | Raised, Acknowledged, Resolved, Cancelled |
| PlanningAndExecution | u_mes_plan_indirectActivity | Active, Inactive |
| PlanningAndExecution | u_mes_plan_containerType | Active, Inactive |
| PlanningAndExecution | u_mes_plan_andonType | Active, Inactive |
| PlanningAndExecution | u_mes_plan_operatorSession | Active, Closed, Rejected |
| PlanningAndExecution | u_mes_plan_documentAcknowledgement | Acknowledged, Superseded |
| PlanningAndExecution | u_mes_plan_interlockEvent | Blocked, Overridden, Cleared, Cancelled |
| PlanningAndExecution | u_mes_plan_recipeDownload | Requested, Verified, Rejected |
| PlanningAndExecution | u_mes_plan_setupVerification | In Progress, Passed, Failed, Overridden |
| PlanningAndExecution | u_mes_plan_lineClearance | In Progress, Passed, Failed, Verified |
| MaterialManagement | u_mes_matl_storageLocation | Active, Inactive |
| MaterialManagement | u_mes_matl_inventoryBalance | Active, Closed |
| MaterialManagement | u_mes_matl_materialMovement | Posted, Reversed |
| MaterialManagement | u_mes_matl_goodsReceipt | Received, Under Inspection, Accepted, Partially Accepted, Rejected |
| MaterialManagement | u_mes_matl_kit | Requested, Picking, Picked, Delivered, Short |
| MaterialManagement | u_mes_matl_materialRequest | Raised, Acknowledged, Delivered, Cancelled |
| MaterialManagement | u_mes_matl_materialConsumption | Posted, Reversed |
| MaterialManagement | u_mes_matl_packagingSpecification | In Preparation, Released, Obsolete |
| MaterialManagement | u_mes_matl_labelTemplate | In Preparation, Released, Obsolete |
| MaterialManagement | u_mes_matl_label | Printed, Verified, Reprinted, Voided |
| MaterialManagement | u_mes_matl_shipment | Planned, Loading, Dispatched, Delivered, Cancelled |
| MaterialManagement | u_mes_matl_movementType | Active, Inactive |
| MaterialManagement | u_mes_matl_stockStatus | Active, Inactive |
| MaterialManagement | u_mes_matl_packType | Active, Inactive |
| MaterialManagement | u_mes_matl_exposureTimer | Running, Paused, Expired, Reset, Consumed |
| MaterialManagement | u_mes_matl_replenishmentRule | Active, Inactive |
| MaterialManagement | u_mes_matl_materialDemandForecast | Calculated, Superseded |
| MaterialManagement | u_mes_matl_dispenseRecord | Dispensed, Verified, Issued, Returned, Rejected |
| Traceability | u_mes_trac_serialNumber | Reserved, Issued, Marked, Shipped, Voided, Scrapped |
| Traceability | u_mes_trac_genealogyLink | Active, Removed |
| Traceability | u_mes_trac_componentLotLink | Active, Removed |
| Traceability | u_mes_trac_asBuiltRecord | Compiling, Released |
| Traceability | u_mes_trac_traceInvestigation | Running, Completed, Closed |
| QualityManagement | u_mes_qual_characteristic | Active, Inactive |
| QualityManagement | u_mes_qual_controlPlan | In Preparation, Released, Obsolete |
| QualityManagement | u_mes_qual_inspectionPlan | In Preparation, Released, Obsolete |
| QualityManagement | u_mes_qual_samplingPlan | Active, Inactive |
| QualityManagement | u_mes_qual_checkSheet | In Preparation, Released, Obsolete |
| QualityManagement | u_mes_qual_checkSheetResult | In Progress, Completed, Verified |
| QualityManagement | u_mes_qual_inspectionResult | Recorded, Voided |
| QualityManagement | u_mes_qual_spcChart | Active, Suspended, Inactive |
| QualityManagement | u_mes_qual_spcSample | Recorded, Under Investigation, Closed |
| QualityManagement | u_mes_qual_defectCode | Active, Inactive |
| QualityManagement | u_mes_qual_nonconformance | Open, Contained, Dispositioned, Closed, Cancelled |
| QualityManagement | u_mes_qual_reworkOrder | Issued, In Progress, Awaiting Reinspection, Completed, Scrapped |
| QualityManagement | u_mes_qual_scrapRecord | Declared, Approved, Disposed |
| QualityManagement | u_mes_qual_qualityHold | Active, Partially Released, Released |
| QualityManagement | u_mes_qual_deviationPermit | Requested, Approved, Expired, Closed, Rejected |
| QualityManagement | u_mes_qual_capa | Open, Containment Done, Root Cause Identified, Actions Implemented, Verified, Closed |
| QualityManagement | u_mes_qual_pfmea | In Preparation, Released, Obsolete |
| QualityManagement | u_mes_qual_ppapSubmission | In Preparation, Submitted, Approved, Interim Approved, Rejected |
| QualityManagement | u_mes_qual_ppapSubmissionElement | Not Started, In Progress, Complete, Not Applicable |
| QualityManagement | u_mes_qual_gauge | Active, Due For Calibration, Overdue, Under Calibration, Blocked, Retired |
| QualityManagement | u_mes_qual_gaugeCalibration | Planned, Completed, Failed |
| QualityManagement | u_mes_qual_msaStudy | Planned, Completed, Accepted, Not Accepted |
| QualityManagement | u_mes_qual_audit | Planned, In Progress, Completed, Closed |
| QualityManagement | u_mes_qual_customerComplaint | Received, Containment Sent, Under Analysis, Closed, Rejected |
| QualityManagement | u_mes_qual_defectGroup | Active, Inactive |
| QualityManagement | u_mes_qual_gaugeType | Active, Inactive |
| QualityManagement | u_mes_qual_dispositionType | Active, Inactive |
| QualityManagement | u_mes_qual_complaintType | Active, Inactive |
| QualityManagement | u_mes_qual_curveEnvelope | In Preparation, Released, Obsolete |
| QualityManagement | u_mes_qual_measurementCurve | Recorded, Voided |
| QualityManagement | u_mes_qual_defectRecord | Open, Reworked, Scrapped, Accepted, Closed |
| QualityManagement | u_mes_qual_auditSchedule | Active, Inactive |
| QualityManagement | u_mes_qual_environmentalMonitoringPoint | Active, Inactive |
| QualityManagement | u_mes_qual_environmentalMonitoringResult | Recorded, Excursion Open, Excursion Closed, Invalidated |
| QualityManagement | u_mes_qual_retentionSample | Stored, Withdrawn, Destroyed |
| QualityManagement | u_mes_qual_riskAssessment | In Preparation, In Review, Approved, Superseded |
| QualityManagement | u_mes_qual_productQualityReview | In Preparation, In Review, Approved |
| QualityManagement | u_mes_qual_productRecall | Initiated, In Progress, Completed, Closed, Cancelled |
| QualityManagement | u_mes_qual_processValidation | Planned, In Execution, Completed, Approved, Rejected |
| PerformanceManagement | u_mes_perf_reasonCode | Active, Inactive |
| PerformanceManagement | u_mes_perf_equipmentState | Open, Closed |
| PerformanceManagement | u_mes_perf_downtimeEvent | Open, Classified, Closed |
| PerformanceManagement | u_mes_perf_productionCount | Open, Closed |
| PerformanceManagement | u_mes_perf_oeeRecord | Calculated, Recalculated |
| PerformanceManagement | u_mes_perf_processTag | Active, Inactive |
| PerformanceManagement | u_mes_perf_alarm | Raised, Acknowledged, Cleared |
| PerformanceManagement | u_mes_perf_torqueResult | Recorded, Voided |
| PerformanceManagement | u_mes_perf_leakTestResult | Recorded, Voided |
| PerformanceManagement | u_mes_perf_lossCategory | Active, Inactive |
| PerformanceManagement | u_mes_perf_reasonCategory | Active, Inactive |
| PerformanceManagement | u_mes_perf_energyType | Active, Inactive |
| PerformanceManagement | u_mes_perf_alarmDefinition | Active, Inactive |
| PerformanceManagement | u_mes_perf_lossSummary | Calculated, Recalculated |
| PerformanceManagement | u_mes_perf_workCenterPerformance | Calculated, Recalculated |
| PerformanceManagement | u_mes_perf_operatorPerformance | Calculated, Recalculated |
| ToolingAndMaintenance | u_mes_maint_maintenancePlan | Active, Suspended, Inactive |
| ToolingAndMaintenance | u_mes_maint_maintenanceWorkOrder | Reported, Planned, In Progress, Completed, Closed, Cancelled |
| ToolingAndMaintenance | u_mes_maint_sparePart | Active, Obsolete |
| ToolingAndMaintenance | u_mes_maint_tool | Available, Mounted, In Maintenance, Life Expired, Scrapped |
| ToolingAndMaintenance | u_mes_maint_toolLifeRecord | Recorded, Voided |
| ToolingAndMaintenance | u_mes_maint_toolType | Active, Inactive |
| ToolingAndMaintenance | u_mes_maint_sparePartTransaction | Posted, Reversed |
| ToolingAndMaintenance | u_mes_maint_reliabilitySummary | Calculated, Recalculated |
| ToolingAndMaintenance | u_mes_maint_equipmentLifecycleEvent | Recorded, Approved, Cancelled |
| ToolingAndMaintenance | u_mes_maint_logbookEntry | Recorded, Reviewed |
| ToolingAndMaintenance | u_mes_maint_cleaningRecord | In Progress, Completed, Verified, Expired, Rejected |
| ToolingAndMaintenance | u_mes_maint_equipmentQualification | Planned, In Execution, Passed, Failed, Approved |
| SystemAndIntegration | u_mes_syst_erpMessage | Queued, Sent, Acknowledged, Failed, Dead Letter |
| SystemAndIntegration | u_mes_syst_integrationConnector | Active, Disabled |
| SystemAndIntegration | u_mes_syst_iotDevice | Active, Inactive, Retired |
| SystemAndIntegration | u_mes_syst_operatorApp | In Preparation, Released, Obsolete |
| SystemAndIntegration | u_mes_syst_notification | Raised, Sent, Acknowledged, Expired |
| SystemAndIntegration | u_mes_syst_controlledDocument | In Preparation, Released, Obsolete |
| SystemAndIntegration | u_mes_syst_numberRange | Active, Inactive |
| SystemAndIntegration | u_mes_syst_systemConfiguration | Active, Inactive |
| SystemAndIntegration | u_mes_syst_documentType | Active, Inactive |
| SystemAndIntegration | u_mes_syst_deviceType | Active, Inactive |
| SystemAndIntegration | u_mes_syst_notificationType | Active, Inactive |
| SystemAndIntegration | u_mes_syst_statusDefinition | Active, Inactive |
| SystemAndIntegration | u_mes_syst_enumerationValue | Active, Inactive |
| SystemAndIntegration | u_mes_syst_statusTransition | Active, Inactive |
| SystemAndIntegration | u_mes_syst_interlockRule | Active, Inactive |
| SystemAndIntegration | u_mes_syst_escalationRule | Active, Inactive |
| SystemAndIntegration | u_mes_syst_alertRule | Active, Inactive |
| SystemAndIntegration | u_mes_syst_analyticsModel | In Preparation, Released, Retired |
| SystemAndIntegration | u_mes_syst_modelPrediction | Open, Actioned, Dismissed, Verified |
| SystemAndIntegration | u_mes_syst_simulationStudy | Planned, Completed, Approved, Rolled Out, Rejected |
| SystemAndIntegration | u_mes_syst_recordPolicy | Active, Inactive |
| SystemAndIntegration | u_mes_syst_savedView | Active, Inactive |
| SystemAndIntegration | u_mes_syst_backupRun | Running, Succeeded, Failed |
| SystemAndIntegration | u_mes_syst_computerisedSystem | In Validation, Validated, Retired |
| SystemAndIntegration | u_mes_syst_systemValidation | Planned, In Execution, Executed, Approved, Rejected |
| SystemAndIntegration | u_mes_syst_systemPeriodicReview | Planned, In Review, Completed, Approved |
| SystemAndIntegration | u_mes_syst_auditTrailReview | Open, In Review, Completed, Escalated |
| SystemAndIntegration | u_mes_syst_userAccessReview | Open, In Review, Completed |
| EnvironmentHealthAndSafety | u_mes_ehs_safetyIncident | Reported, Under Investigation, Actions Open, Closed |
| EnvironmentHealthAndSafety | u_mes_ehs_incidentType | Active, Inactive |
| EnvironmentHealthAndSafety | u_mes_ehs_bodyPart | Active, Inactive |
| EnvironmentHealthAndSafety | u_mes_ehs_injuryType | Active, Inactive |
| BatchManufacturingRecord | u_mes_bmr_batchRecordReview | Open, Under Review, Returned For Correction, Approved, Rejected |
| BatchManufacturingRecord | u_mes_bmr_batchRelease | Pending, Released, Conditionally Released, Rejected |
| BatchManufacturingRecord | u_mes_bmr_yieldReconciliation | Calculated, Under Investigation, Approved |
| BatchManufacturingRecord | u_mes_bmr_batchManufacturingRecord | Open, In Execution, Compiled, Under Review, Approved, Archived |
| MasterManufacturingRecord | u_mes_mmr_masterManufacturingRecord | In Preparation, In Review, Approved, Effective, Superseded |

Entity collections without a status key (append-only records): u_mes_perf_processReading, u_mes_syst_businessEvent, u_mes_syst_auditTrail, u_mes_syst_electronicSignature, u_mes_perf_energyReading, u_mes_qual_measurementCurvePoint.
