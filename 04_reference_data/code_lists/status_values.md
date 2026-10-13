# Status values per collection

Model version 2.9 | 12 October 2026 | 369 collections (200 entity, 85 child, 76 relationship, 8 value-list), 8614 keys

Each collection with a lifecycle defines its own `status` values. The first value is the initial state. The values are stored as master data in `u_mes_syst_statusDefinition` (one document per collection and value) and the allowed moves in `u_mes_syst_statusTransition`. Collections not listed have no `status` key.

| Module | Collection | Status values (in order) |
|---|---|---|
| Master Data Management | u_mes_mast_enterprise | Active, Inactive |
| Master Data Management | u_mes_mast_site | Active, Inactive |
| Master Data Management | u_mes_mast_area | Active, Inactive |
| Master Data Management | u_mes_mast_line | Active, Inactive |
| Master Data Management | u_mes_mast_workCenter | Active, Inactive |
| Master Data Management | u_mes_mast_equipment | Active, Under Maintenance, Decommissioned |
| Master Data Management | u_mes_mast_shift | Active, Inactive |
| Master Data Management | u_mes_mast_workCalendar | Active, Inactive |
| Master Data Management | u_mes_mast_shiftRoster | Planned, Published, Closed |
| Master Data Management | u_mes_mast_role | Active, Inactive |
| Master Data Management | u_mes_mast_user | Active, Suspended, Left |
| Master Data Management | u_mes_mast_skill | Active, Inactive |
| Master Data Management | u_mes_mast_skillCertification | Valid, Expiring Soon, Expired, Revoked |
| Master Data Management | u_mes_mast_customer | Active, Inactive |
| Master Data Management | u_mes_mast_supplier | Approved, Conditional, Blocked, Inactive |
| Master Data Management | u_mes_mast_unitOfMeasure | Active, Inactive |
| Master Data Management | u_mes_mast_department | Active, Inactive |
| Master Data Management | u_mes_mast_designation | Active, Inactive |
| Master Data Management | u_mes_mast_employmentType | Active, Inactive |
| Master Data Management | u_mes_mast_costCenter | Active, Inactive |
| Master Data Management | u_mes_mast_manufacturer | Active, Inactive |
| Master Data Management | u_mes_mast_equipmentType | Active, Inactive |
| Master Data Management | u_mes_mast_skillCategory | Active, Inactive |
| Master Data Management | u_mes_mast_permission | Active, Inactive |
| Master Data Management | u_mes_mast_signatureMeaning | Active, Inactive |
| Master Data Management | u_mes_mast_currency | Active, Inactive |
| Master Data Management | u_mes_mast_country | Active, Inactive |
| Master Data Management | u_mes_mast_language | Active, Inactive |
| Master Data Management | u_mes_mast_transporter | Active, Inactive |
| Master Data Management | u_mes_mast_commodity | Active, Inactive |
| Product Definition | u_mes_prod_item | Active, Phase Out, Obsolete |
| Product Definition | u_mes_prod_productVariant | In Preparation, Released, Obsolete |
| Product Definition | u_mes_prod_billOfMaterial | In Preparation, Released, Obsolete |
| Product Definition | u_mes_prod_operation | Active, Inactive |
| Product Definition | u_mes_prod_routing | In Preparation, Released, Obsolete |
| Product Definition | u_mes_prod_billOfProcess | In Preparation, Released, Obsolete |
| Product Definition | u_mes_prod_workInstruction | In Preparation, Released, Obsolete |
| Product Definition | u_mes_prod_recipe | In Preparation, Released, Obsolete |
| Product Definition | u_mes_prod_engineeringChange | Raised, Under Evaluation, Approved, Implemented, Closed, Rejected |
| Product Definition | u_mes_prod_itemGroup | Active, Inactive |
| Product Definition | u_mes_prod_itemFamily | Active, Inactive |
| Product Definition | u_mes_prod_ppeItem | Active, Inactive |
| Product Definition | u_mes_prod_market | Active, Inactive |
| Product Definition | u_mes_prod_padCompound | Active, Inactive |
| Product Definition | u_mes_prod_surfaceFinish | Active, Inactive |
| Product Definition | u_mes_prod_vehicleModel | Active, Inactive |
| Planning and Execution | u_mes_plan_customerSchedule | Received, Confirmed, Partially Shipped, Completed, Replaced |
| Planning and Execution | u_mes_plan_productionOrder | Created, Released, In Progress, On Hold, Completed, Closed, Cancelled |
| Planning and Execution | u_mes_plan_productionSchedule | Planned, Published, In Progress, Completed |
| Planning and Execution | u_mes_plan_dispatchList | Generated, Acknowledged, Closed |
| Planning and Execution | u_mes_plan_dispatchListEntry | Queued, Started, Completed, Skipped |
| Planning and Execution | u_mes_plan_operationExecution | Started, Completed, Aborted |
| Planning and Execution | u_mes_plan_stepCompletion | Completed, Skipped, Overridden |
| Planning and Execution | u_mes_plan_wipUnit | Created, In Process, On Hold, In Rework, Completed, Packed, Shipped, Scrapped |
| Planning and Execution | u_mes_plan_lot | Created, Available, In Process, On Hold, Consumed, Closed, Rejected |
| Planning and Execution | u_mes_plan_container | Empty, Filling, Full, Sealed, Shipped, Returned, Under Repair |
| Planning and Execution | u_mes_plan_labourBooking | Open, Closed, Approved |
| Planning and Execution | u_mes_plan_changeover | Planned, In Progress, Awaiting First Off Approval, Completed |
| Planning and Execution | u_mes_plan_shiftHandover | Open, Handed Over, Acknowledged |
| Planning and Execution | u_mes_plan_andonEvent | Raised, Acknowledged, Resolved, Cancelled |
| Planning and Execution | u_mes_plan_indirectActivity | Active, Inactive |
| Planning and Execution | u_mes_plan_containerType | Active, Inactive |
| Planning and Execution | u_mes_plan_andonType | Active, Inactive |
| Planning and Execution | u_mes_plan_operatorSession | Active, Closed, Rejected |
| Planning and Execution | u_mes_plan_documentAcknowledgement | Acknowledged, Superseded |
| Planning and Execution | u_mes_plan_interlockEvent | Blocked, Overridden, Cleared, Cancelled |
| Planning and Execution | u_mes_plan_recipeDownload | Requested, Verified, Rejected |
| Planning and Execution | u_mes_plan_setupVerification | In Progress, Passed, Failed, Overridden |
| Planning and Execution | u_mes_plan_lineClearance | In Progress, Passed, Failed, Verified |
| Material Management | u_mes_matl_storageLocation | Active, Inactive |
| Material Management | u_mes_matl_inventoryBalance | Active, Closed |
| Material Management | u_mes_matl_materialMovement | Posted, Reversed |
| Material Management | u_mes_matl_goodsReceipt | Received, Under Inspection, Accepted, Partially Accepted, Rejected |
| Material Management | u_mes_matl_kit | Requested, Picking, Picked, Delivered, Short |
| Material Management | u_mes_matl_materialRequest | Raised, Acknowledged, Delivered, Cancelled |
| Material Management | u_mes_matl_materialConsumption | Posted, Reversed |
| Material Management | u_mes_matl_packagingSpecification | In Preparation, Released, Obsolete |
| Material Management | u_mes_matl_labelTemplate | In Preparation, Released, Obsolete |
| Material Management | u_mes_matl_label | Printed, Verified, Reprinted, Voided |
| Material Management | u_mes_matl_shipment | Planned, Loading, Dispatched, Delivered, Cancelled |
| Material Management | u_mes_matl_movementType | Active, Inactive |
| Material Management | u_mes_matl_stockStatus | Active, Inactive |
| Material Management | u_mes_matl_packType | Active, Inactive |
| Material Management | u_mes_matl_exposureTimer | Running, Paused, Expired, Reset, Consumed |
| Material Management | u_mes_matl_replenishmentRule | Active, Inactive |
| Material Management | u_mes_matl_materialDemandForecast | Calculated, Superseded |
| Material Management | u_mes_matl_dispenseRecord | Dispensed, Verified, Issued, Returned, Rejected |
| Traceability | u_mes_trac_serialNumber | Reserved, Issued, Marked, Shipped, Voided, Scrapped |
| Traceability | u_mes_trac_genealogyLink | Active, Removed |
| Traceability | u_mes_trac_componentLotLink | Active, Removed |
| Traceability | u_mes_trac_asBuiltRecord | Compiling, Released |
| Traceability | u_mes_trac_traceInvestigation | Running, Completed, Closed |
| Quality Management | u_mes_qual_characteristic | Active, Inactive |
| Quality Management | u_mes_qual_controlPlan | In Preparation, Released, Obsolete |
| Quality Management | u_mes_qual_inspectionPlan | In Preparation, Released, Obsolete |
| Quality Management | u_mes_qual_samplingPlan | Active, Inactive |
| Quality Management | u_mes_qual_checkSheet | In Preparation, Released, Obsolete |
| Quality Management | u_mes_qual_checkSheetResult | In Progress, Completed, Verified |
| Quality Management | u_mes_qual_inspectionResult | Recorded, Voided |
| Quality Management | u_mes_qual_spcChart | Active, Suspended, Inactive |
| Quality Management | u_mes_qual_spcSample | Recorded, Under Investigation, Closed |
| Quality Management | u_mes_qual_defectCode | Active, Inactive |
| Quality Management | u_mes_qual_nonconformance | Open, Contained, Dispositioned, Closed, Cancelled |
| Quality Management | u_mes_qual_reworkOrder | Issued, In Progress, Awaiting Reinspection, Completed, Scrapped |
| Quality Management | u_mes_qual_scrapRecord | Declared, Approved, Disposed |
| Quality Management | u_mes_qual_qualityHold | Active, Partially Released, Released |
| Quality Management | u_mes_qual_deviationPermit | Requested, Approved, Expired, Closed, Rejected |
| Quality Management | u_mes_qual_capa | Open, Containment Done, Root Cause Identified, Actions Implemented, Verified, Closed |
| Quality Management | u_mes_qual_pfmea | In Preparation, Released, Obsolete |
| Quality Management | u_mes_qual_ppapSubmission | In Preparation, Submitted, Approved, Interim Approved, Rejected |
| Quality Management | u_mes_qual_ppapSubmissionElement | Not Started, In Progress, Complete, Not Applicable |
| Quality Management | u_mes_qual_gauge | Active, Due For Calibration, Overdue, Under Calibration, Blocked, Retired |
| Quality Management | u_mes_qual_gaugeCalibration | Planned, Completed, Failed |
| Quality Management | u_mes_qual_msaStudy | Planned, Completed, Accepted, Not Accepted |
| Quality Management | u_mes_qual_audit | Planned, In Progress, Completed, Closed |
| Quality Management | u_mes_qual_customerComplaint | Received, Containment Sent, Under Analysis, Closed, Rejected |
| Quality Management | u_mes_qual_defectGroup | Active, Inactive |
| Quality Management | u_mes_qual_gaugeType | Active, Inactive |
| Quality Management | u_mes_qual_dispositionType | Active, Inactive |
| Quality Management | u_mes_qual_complaintType | Active, Inactive |
| Quality Management | u_mes_qual_curveEnvelope | In Preparation, Released, Obsolete |
| Quality Management | u_mes_qual_measurementCurve | Recorded, Voided |
| Quality Management | u_mes_qual_defectRecord | Open, Reworked, Scrapped, Accepted, Closed |
| Quality Management | u_mes_qual_auditSchedule | Active, Inactive |
| Quality Management | u_mes_qual_environmentalMonitoringPoint | Active, Inactive |
| Quality Management | u_mes_qual_environmentalMonitoringResult | Recorded, Excursion Open, Excursion Closed, Invalidated |
| Quality Management | u_mes_qual_retentionSample | Stored, Withdrawn, Destroyed |
| Quality Management | u_mes_qual_riskAssessment | In Preparation, In Review, Approved, Superseded |
| Quality Management | u_mes_qual_productQualityReview | In Preparation, In Review, Approved |
| Quality Management | u_mes_qual_productRecall | Initiated, In Progress, Completed, Closed, Cancelled |
| Quality Management | u_mes_qual_processValidation | Planned, In Execution, Completed, Approved, Rejected |
| Performance Management | u_mes_perf_reasonCode | Active, Inactive |
| Performance Management | u_mes_perf_equipmentState | Open, Closed |
| Performance Management | u_mes_perf_downtimeEvent | Open, Classified, Closed |
| Performance Management | u_mes_perf_productionCount | Open, Closed |
| Performance Management | u_mes_perf_oeeRecord | Calculated, Recalculated |
| Performance Management | u_mes_perf_processTag | Active, Inactive |
| Performance Management | u_mes_perf_alarm | Raised, Acknowledged, Cleared |
| Performance Management | u_mes_perf_torqueResult | Recorded, Voided |
| Performance Management | u_mes_perf_leakTestResult | Recorded, Voided |
| Performance Management | u_mes_perf_lossCategory | Active, Inactive |
| Performance Management | u_mes_perf_reasonCategory | Active, Inactive |
| Performance Management | u_mes_perf_energyType | Active, Inactive |
| Performance Management | u_mes_perf_alarmDefinition | Active, Inactive |
| Performance Management | u_mes_perf_lossSummary | Calculated, Recalculated |
| Performance Management | u_mes_perf_workCenterPerformance | Calculated, Recalculated |
| Performance Management | u_mes_perf_operatorPerformance | Calculated, Recalculated |
| Tooling & Maintenance | u_mes_maint_maintenancePlan | Active, Suspended, Inactive |
| Tooling & Maintenance | u_mes_maint_maintenanceWorkOrder | Reported, Planned, In Progress, Completed, Closed, Cancelled |
| Tooling & Maintenance | u_mes_maint_sparePart | Active, Obsolete |
| Tooling & Maintenance | u_mes_maint_tool | Available, Mounted, In Maintenance, Life Expired, Scrapped |
| Tooling & Maintenance | u_mes_maint_toolLifeRecord | Recorded, Voided |
| Tooling & Maintenance | u_mes_maint_toolType | Active, Inactive |
| Tooling & Maintenance | u_mes_maint_sparePartTransaction | Posted, Reversed |
| Tooling & Maintenance | u_mes_maint_reliabilitySummary | Calculated, Recalculated |
| Tooling & Maintenance | u_mes_maint_equipmentLifecycleEvent | Recorded, Approved, Cancelled |
| Tooling & Maintenance | u_mes_maint_logbookEntry | Recorded, Reviewed |
| Tooling & Maintenance | u_mes_maint_cleaningRecord | In Progress, Completed, Verified, Expired, Rejected |
| Tooling & Maintenance | u_mes_maint_equipmentQualification | Planned, In Execution, Passed, Failed, Approved |
| System and Integration | u_mes_syst_erpMessage | Queued, Sent, Acknowledged, Failed, Dead Letter |
| System and Integration | u_mes_syst_integrationConnector | Active, Disabled |
| System and Integration | u_mes_syst_iotDevice | Active, Inactive, Retired |
| System and Integration | u_mes_syst_operatorApp | In Preparation, Released, Obsolete |
| System and Integration | u_mes_syst_notification | Raised, Sent, Acknowledged, Expired |
| System and Integration | u_mes_syst_controlledDocument | In Preparation, Released, Obsolete |
| System and Integration | u_mes_syst_numberRange | Active, Inactive |
| System and Integration | u_mes_syst_systemConfiguration | Active, Inactive |
| System and Integration | u_mes_syst_documentType | Active, Inactive |
| System and Integration | u_mes_syst_deviceType | Active, Inactive |
| System and Integration | u_mes_syst_notificationType | Active, Inactive |
| System and Integration | u_mes_syst_statusDefinition | Active, Inactive |
| System and Integration | u_mes_syst_enumerationValue | Active, Inactive |
| System and Integration | u_mes_syst_statusTransition | Active, Inactive |
| System and Integration | u_mes_syst_interlockRule | Active, Inactive |
| System and Integration | u_mes_syst_escalationRule | Active, Inactive |
| System and Integration | u_mes_syst_alertRule | Active, Inactive |
| System and Integration | u_mes_syst_analyticsModel | In Preparation, Released, Retired |
| System and Integration | u_mes_syst_modelPrediction | Open, Actioned, Dismissed, Verified |
| System and Integration | u_mes_syst_simulationStudy | Planned, Completed, Approved, Rolled Out, Rejected |
| System and Integration | u_mes_syst_recordPolicy | Active, Inactive |
| System and Integration | u_mes_syst_savedView | Active, Inactive |
| System and Integration | u_mes_syst_backupRun | Running, Succeeded, Failed |
| System and Integration | u_mes_syst_computerisedSystem | In Validation, Validated, Retired |
| System and Integration | u_mes_syst_systemValidation | Planned, In Execution, Executed, Approved, Rejected |
| System and Integration | u_mes_syst_systemPeriodicReview | Planned, In Review, Completed, Approved |
| System and Integration | u_mes_syst_auditTrailReview | Open, In Review, Completed, Escalated |
| System and Integration | u_mes_syst_userAccessReview | Open, In Review, Completed |
| Environment Health and Safety | u_mes_ehs_safetyIncident | Reported, Under Investigation, Actions Open, Closed |
| Environment Health and Safety | u_mes_ehs_incidentType | Active, Inactive |
| Environment Health and Safety | u_mes_ehs_bodyPart | Active, Inactive |
| Environment Health and Safety | u_mes_ehs_injuryType | Active, Inactive |
| Batch Manufacturing Record | u_mes_bmr_batchRecordReview | Open, Under Review, Returned For Correction, Approved, Rejected |
| Batch Manufacturing Record | u_mes_bmr_batchRelease | Pending, Released, Conditionally Released, Rejected |
| Batch Manufacturing Record | u_mes_bmr_yieldReconciliation | Calculated, Under Investigation, Approved |
| Batch Manufacturing Record | u_mes_bmr_batchManufacturingRecord | Open, In Execution, Compiled, Under Review, Approved, Archived |
| Master Manufacturing Record | u_mes_mmr_masterManufacturingRecord | In Preparation, In Review, Approved, Effective, Superseded |

Entity collections without a status key (append-only records): u_mes_perf_processReading, u_mes_syst_businessEvent, u_mes_syst_auditTrail, u_mes_syst_electronicSignature, u_mes_perf_energyReading, u_mes_qual_measurementCurvePoint.
