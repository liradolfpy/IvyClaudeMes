# Status values per collection

Model version 2.2 | 11 October 2026 | 299 collections (148 entity, 76 child, 67 relationship, 8 value-list), 6058 keys

Each collection with a lifecycle defines its own `status` values. The first value is the initial state. The values are stored as master data in `u_mes_sys_statusDefinition` (one document per collection and value) and the allowed moves in `u_mes_sys_statusTransition`. Collections not listed have no `status` key.

| Module | Collection | Status values (in order) |
|---|---|---|
| Master data | u_mes_mdm_enterprise | Active, Inactive |
| Master data | u_mes_mdm_site | Active, Inactive |
| Master data | u_mes_mdm_area | Active, Inactive |
| Master data | u_mes_mdm_line | Active, Inactive |
| Master data | u_mes_mdm_workCenter | Active, Inactive |
| Master data | u_mes_mdm_equipment | Active, Under Maintenance, Decommissioned |
| Master data | u_mes_mdm_shift | Active, Inactive |
| Master data | u_mes_mdm_workCalendar | Active, Inactive |
| Master data | u_mes_mdm_shiftRoster | Planned, Published, Closed |
| Master data | u_mes_mdm_role | Active, Inactive |
| Master data | u_mes_mdm_user | Active, Suspended, Left |
| Master data | u_mes_mdm_skill | Active, Inactive |
| Master data | u_mes_mdm_skillCertification | Valid, Expiring Soon, Expired, Revoked |
| Master data | u_mes_mdm_customer | Active, Inactive |
| Master data | u_mes_mdm_supplier | Approved, Conditional, Blocked, Inactive |
| Master data | u_mes_mdm_unitOfMeasure | Active, Inactive |
| Master data | u_mes_mdm_department | Active, Inactive |
| Master data | u_mes_mdm_designation | Active, Inactive |
| Master data | u_mes_mdm_employmentType | Active, Inactive |
| Master data | u_mes_mdm_costCenter | Active, Inactive |
| Master data | u_mes_mdm_manufacturer | Active, Inactive |
| Master data | u_mes_mdm_equipmentType | Active, Inactive |
| Master data | u_mes_mdm_skillCategory | Active, Inactive |
| Master data | u_mes_mdm_permission | Active, Inactive |
| Master data | u_mes_mdm_signatureMeaning | Active, Inactive |
| Master data | u_mes_mdm_currency | Active, Inactive |
| Master data | u_mes_mdm_country | Active, Inactive |
| Master data | u_mes_mdm_language | Active, Inactive |
| Master data | u_mes_mdm_transporter | Active, Inactive |
| Master data | u_mes_mdm_commodity | Active, Inactive |
| Product definition | u_mes_prd_item | Active, Phase Out, Obsolete |
| Product definition | u_mes_prd_productVariant | In Preparation, Released, Obsolete |
| Product definition | u_mes_prd_billOfMaterial | In Preparation, Released, Obsolete |
| Product definition | u_mes_prd_operation | Active, Inactive |
| Product definition | u_mes_prd_routing | In Preparation, Released, Obsolete |
| Product definition | u_mes_prd_billOfProcess | In Preparation, Released, Obsolete |
| Product definition | u_mes_prd_workInstruction | In Preparation, Released, Obsolete |
| Product definition | u_mes_prd_recipe | In Preparation, Released, Obsolete |
| Product definition | u_mes_prd_engineeringChange | Raised, Under Evaluation, Approved, Implemented, Closed, Rejected |
| Product definition | u_mes_prd_itemGroup | Active, Inactive |
| Product definition | u_mes_prd_itemFamily | Active, Inactive |
| Product definition | u_mes_prd_ppeItem | Active, Inactive |
| Product definition | u_mes_prd_market | Active, Inactive |
| Product definition | u_mes_prd_padCompound | Active, Inactive |
| Product definition | u_mes_prd_surfaceFinish | Active, Inactive |
| Product definition | u_mes_prd_vehicleModel | Active, Inactive |
| Planning and execution | u_mes_exe_customerSchedule | Received, Confirmed, Partially Shipped, Completed, Replaced |
| Planning and execution | u_mes_exe_productionOrder | Created, Released, In Progress, On Hold, Completed, Closed, Cancelled |
| Planning and execution | u_mes_exe_productionSchedule | Planned, Published, In Progress, Completed |
| Planning and execution | u_mes_exe_dispatchList | Generated, Acknowledged, Closed |
| Planning and execution | u_mes_exe_dispatchListEntry | Queued, Started, Completed, Skipped |
| Planning and execution | u_mes_exe_operationExecution | Started, Completed, Aborted |
| Planning and execution | u_mes_exe_stepCompletion | Completed, Skipped, Overridden |
| Planning and execution | u_mes_exe_wipUnit | Created, In Process, On Hold, In Rework, Completed, Packed, Shipped, Scrapped |
| Planning and execution | u_mes_exe_lot | Created, Available, In Process, On Hold, Consumed, Closed, Rejected |
| Planning and execution | u_mes_exe_container | Empty, Filling, Full, Sealed, Shipped, Returned, Under Repair |
| Planning and execution | u_mes_exe_labourBooking | Open, Closed, Approved |
| Planning and execution | u_mes_exe_changeover | Planned, In Progress, Awaiting First Off Approval, Completed |
| Planning and execution | u_mes_exe_shiftHandover | Open, Handed Over, Acknowledged |
| Planning and execution | u_mes_exe_indirectActivity | Active, Inactive |
| Planning and execution | u_mes_exe_containerType | Active, Inactive |
| Materials | u_mes_mat_storageLocation | Active, Inactive |
| Materials | u_mes_mat_inventoryBalance | Active, Closed |
| Materials | u_mes_mat_materialMovement | Posted, Reversed |
| Materials | u_mes_mat_goodsReceipt | Received, Under Inspection, Accepted, Partially Accepted, Rejected |
| Materials | u_mes_mat_kit | Requested, Picking, Picked, Delivered, Short |
| Materials | u_mes_mat_materialRequest | Raised, Acknowledged, Delivered, Cancelled |
| Materials | u_mes_mat_materialConsumption | Posted, Reversed |
| Materials | u_mes_mat_packagingSpecification | In Preparation, Released, Obsolete |
| Materials | u_mes_mat_labelTemplate | In Preparation, Released, Obsolete |
| Materials | u_mes_mat_label | Printed, Verified, Reprinted, Voided |
| Materials | u_mes_mat_shipment | Planned, Loading, Dispatched, Delivered, Cancelled |
| Materials | u_mes_mat_movementType | Active, Inactive |
| Materials | u_mes_mat_stockStatus | Active, Inactive |
| Materials | u_mes_mat_packType | Active, Inactive |
| Traceability | u_mes_trc_serialNumber | Reserved, Issued, Marked, Shipped, Voided, Scrapped |
| Traceability | u_mes_trc_genealogyLink | Active, Removed |
| Traceability | u_mes_trc_componentLotLink | Active, Removed |
| Traceability | u_mes_trc_asBuiltRecord | Compiling, Released |
| Quality | u_mes_qlt_characteristic | Active, Inactive |
| Quality | u_mes_qlt_controlPlan | In Preparation, Released, Obsolete |
| Quality | u_mes_qlt_inspectionPlan | In Preparation, Released, Obsolete |
| Quality | u_mes_qlt_samplingPlan | Active, Inactive |
| Quality | u_mes_qlt_checkSheet | In Preparation, Released, Obsolete |
| Quality | u_mes_qlt_checkSheetResult | In Progress, Completed, Verified |
| Quality | u_mes_qlt_inspectionResult | Recorded, Voided |
| Quality | u_mes_qlt_spcChart | Active, Suspended, Inactive |
| Quality | u_mes_qlt_spcSample | Recorded, Under Investigation, Closed |
| Quality | u_mes_qlt_defectCode | Active, Inactive |
| Quality | u_mes_qlt_nonconformance | Open, Contained, Dispositioned, Closed, Cancelled |
| Quality | u_mes_qlt_reworkOrder | Issued, In Progress, Awaiting Reinspection, Completed, Scrapped |
| Quality | u_mes_qlt_scrapRecord | Declared, Approved, Disposed |
| Quality | u_mes_qlt_qualityHold | Active, Partially Released, Released |
| Quality | u_mes_qlt_deviationPermit | Requested, Approved, Expired, Closed, Rejected |
| Quality | u_mes_qlt_capa | Open, Containment Done, Root Cause Identified, Actions Implemented, Verified, Closed |
| Quality | u_mes_qlt_pfmea | In Preparation, Released, Obsolete |
| Quality | u_mes_qlt_ppapSubmission | In Preparation, Submitted, Approved, Interim Approved, Rejected |
| Quality | u_mes_qlt_ppapSubmissionElement | Not Started, In Progress, Complete, Not Applicable |
| Quality | u_mes_qlt_gauge | Active, Due For Calibration, Overdue, Under Calibration, Blocked, Retired |
| Quality | u_mes_qlt_gaugeCalibration | Planned, Completed, Failed |
| Quality | u_mes_qlt_msaStudy | Planned, Completed, Accepted, Not Accepted |
| Quality | u_mes_qlt_audit | Planned, In Progress, Completed, Closed |
| Quality | u_mes_qlt_customerComplaint | Received, Containment Sent, Under Analysis, Closed, Rejected |
| Quality | u_mes_qlt_defectGroup | Active, Inactive |
| Quality | u_mes_qlt_gaugeType | Active, Inactive |
| Quality | u_mes_qlt_dispositionType | Active, Inactive |
| Quality | u_mes_qlt_complaintType | Active, Inactive |
| Equipment and performance | u_mes_eqp_reasonCode | Active, Inactive |
| Equipment and performance | u_mes_eqp_equipmentState | Open, Closed |
| Equipment and performance | u_mes_eqp_downtimeEvent | Open, Classified, Closed |
| Equipment and performance | u_mes_eqp_productionCount | Open, Closed |
| Equipment and performance | u_mes_eqp_oeeRecord | Calculated, Recalculated |
| Equipment and performance | u_mes_eqp_processTag | Active, Inactive |
| Equipment and performance | u_mes_eqp_alarm | Raised, Acknowledged, Cleared |
| Equipment and performance | u_mes_eqp_torqueResult | Recorded, Voided |
| Equipment and performance | u_mes_eqp_leakTestResult | Recorded, Voided |
| Equipment and performance | u_mes_eqp_lossCategory | Active, Inactive |
| Equipment and performance | u_mes_eqp_reasonCategory | Active, Inactive |
| Maintenance and tooling | u_mes_mnt_maintenancePlan | Active, Suspended, Inactive |
| Maintenance and tooling | u_mes_mnt_maintenanceWorkOrder | Reported, Planned, In Progress, Completed, Closed, Cancelled |
| Maintenance and tooling | u_mes_mnt_sparePart | Active, Obsolete |
| Maintenance and tooling | u_mes_mnt_tool | Available, Mounted, In Maintenance, Life Expired, Scrapped |
| Maintenance and tooling | u_mes_mnt_toolLifeRecord | Recorded, Voided |
| Maintenance and tooling | u_mes_mnt_toolType | Active, Inactive |
| Integration and system | u_mes_sys_erpMessage | Queued, Sent, Acknowledged, Failed, Dead Letter |
| Integration and system | u_mes_sys_integrationConnector | Active, Disabled |
| Integration and system | u_mes_sys_iotDevice | Active, Inactive, Retired |
| Integration and system | u_mes_sys_operatorApp | In Preparation, Released, Obsolete |
| Integration and system | u_mes_sys_notification | Raised, Sent, Acknowledged, Expired |
| Integration and system | u_mes_sys_controlledDocument | In Preparation, Released, Obsolete |
| Integration and system | u_mes_sys_numberRange | Active, Inactive |
| Integration and system | u_mes_sys_systemConfiguration | Active, Inactive |
| Integration and system | u_mes_sys_documentType | Active, Inactive |
| Integration and system | u_mes_sys_deviceType | Active, Inactive |
| Integration and system | u_mes_sys_notificationType | Active, Inactive |
| Integration and system | u_mes_sys_statusDefinition | Active, Inactive |
| Integration and system | u_mes_sys_enumerationValue | Active, Inactive |
| Integration and system | u_mes_sys_statusTransition | Active, Inactive |
| Energy, safety and andon | u_mes_ehs_andonEvent | Raised, Acknowledged, Resolved, Cancelled |
| Energy, safety and andon | u_mes_ehs_safetyIncident | Reported, Under Investigation, Actions Open, Closed |
| Energy, safety and andon | u_mes_ehs_andonType | Active, Inactive |
| Energy, safety and andon | u_mes_ehs_incidentType | Active, Inactive |
| Energy, safety and andon | u_mes_ehs_energyType | Active, Inactive |
| Energy, safety and andon | u_mes_ehs_bodyPart | Active, Inactive |
| Energy, safety and andon | u_mes_ehs_injuryType | Active, Inactive |

Entity collections without a status key (append-only records): u_mes_eqp_processReading, u_mes_sys_businessEvent, u_mes_sys_auditTrail, u_mes_sys_electronicSignature, u_mes_ehs_energyReading.
