# u_mes_mast_user

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
| Purpose | People and system accounts; badge id, role, home work centre |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | fullName |
| Keys | 35 (24 required, 11 may be null) |
| Estimated volume per year | 300-1,500 per site |
| Storage | standard |

## Structure

Flat entity collection: one document per user, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with userId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mast_userRole | Relationship | role |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1029000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"10231"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | userName | String | - | Yes | User name | `"sunil.jadhav"` |  |
| 6 | fullName | String | - | Yes | Full name | `"Sunil Jadhav"` |  |
| 7 | userType | String | - | Yes | User type | `"Employee"` | Employee; Contractor; System |
| 8 | departmentId | String | - | Yes | Reference to u_mes_mast_department._id | `"1256000000000001"` | Reference: u_mes_mast_department._id |
| 9 | departmentName | String | - | Yes | Display value of departmentId, copied from u_mes_mast_department.name | `"Production"` |  |
| 10 | designationId | String | - | Yes | Reference to u_mes_mast_designation._id | `"1257000000000001"` | Reference: u_mes_mast_designation._id |
| 11 | designationName | String | - | Yes | Display value of designationId, copied from u_mes_mast_designation.name | `"Assembly Operator"` |  |
| 12 | badgeNo | String | - | Yes | Number encoded on the operator badge used for station login | `"B-0010231"` |  |
| 13 | email | String | - | No (null allowed) | Email of the user | `"sunil.jadhav@varunabrakes.example"` |  |
| 14 | mobile | String | - | No (null allowed) | Mobile of the user | `"+91-98220-55142"` |  |
| 15 | defaultShiftId | String | - | Yes | Reference to u_mes_mast_shift._id: default shift | `"1015000000000001"` | Reference: u_mes_mast_shift._id |
| 16 | defaultShiftName | String | - | Yes | Display value of defaultShiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 17 | homeWorkCenterId | String | - | No (null allowed) | Reference to u_mes_mast_workCenter._id: home work center | `"1009000000000007"` | Reference: u_mes_mast_workCenter._id |
| 18 | homeWorkCenterName | String | - | No (null allowed) | Display value of homeWorkCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 19 | reportsToUserId | String | - | No (null allowed) | Reference to u_mes_mast_user._id: reports to user | `"1029000000000005"` | Reference: u_mes_mast_user._id |
| 20 | reportsToUserName | String | - | No (null allowed) | Display value of reportsToUserId, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 21 | dateOfJoining | Date | Date | Yes | Date of joining. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix | `ISODate("2019-01-04T00:00:00.000+0000")` |  |
| 22 | employmentTypeId | String | - | Yes | Reference to u_mes_mast_employmentType._id | `"1258000000000001"` | Reference: u_mes_mast_employmentType._id |
| 23 | employmentTypeName | String | - | Yes | Display value of employmentTypeId, copied from u_mes_mast_employmentType.name | `"Permanent"` |  |
| 24 | contractorSupplierId | String | - | No (null allowed) | Reference to u_mes_mast_supplier._id: contractor supplier | `null` | Reference: u_mes_mast_supplier._id |
| 25 | contractorSupplierName | String | - | No (null allowed) | Display value of contractorSupplierId, copied from u_mes_mast_supplier.name | `null` |  |
| 26 | languageId | String | - | Yes | Reference to u_mes_mast_language._id | `"1267000000000002"` | Reference: u_mes_mast_language._id |
| 27 | languageName | String | - | Yes | Display value of languageId, copied from u_mes_mast_language.name | `"Marathi"` |  |
| 28 | lastLoginAt | Date | Datetime | No (null allowed) | Last login date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 29 | failedLoginCount | Int32 | - | Yes | Failed login count | `NumberInt(0)` |  |
| 30 | passwordChangedAt | Date | Datetime | Yes | Password changed date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `ISODate("2026-04-02T00:00:00.000+0000")` |  |
| 31 | isLocked | Boolean | - | Yes | True when the record is locked | `false` |  |
| 32 | lastAccessReviewDate | Date | Date | No (null allowed) | Date of the last access review of the account (GMP-07) | `ISODate("2026-09-16T00:00:00.000+0000")` |  |
| 33 | passwordExpiryDate | Date | Date | No (null allowed) | Date the password expires | `ISODate("2026-06-30T00:00:00.000+0000")` |  |
| 34 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Suspended; Left |
| 35 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Suspended, Left. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ departmentId: 1 }` | No | Look-up of documents by department |
| 4 | `{ designationId: 1 }` | No | Look-up of documents by designation |
| 5 | `{ defaultShiftId: 1 }` | No | Look-up of documents by default shift |
| 6 | `{ homeWorkCenterId: 1 }` | No | Look-up of documents by home work center |
| 7 | `{ reportsToUserId: 1 }` | No | Look-up of documents by reports to user |
| 8 | `{ userName: 1 }` | Yes | Login name is unique |
| 9 | `{ badgeNo: 1 }` | Yes | Badge number is unique |

## Referenced by

u_mes_mast_siteCertificate, u_mes_mast_area, u_mes_mast_shiftRoster, u_mes_mast_shiftRosterAssignment, u_mes_mast_user, u_mes_mast_userRole, u_mes_mast_skillCertification, u_mes_prod_billOfMaterial, u_mes_prod_routing, u_mes_prod_billOfProcess, u_mes_prod_workInstruction, u_mes_prod_recipe, u_mes_prod_engineeringChange, u_mes_prod_engineeringChangeApproval, u_mes_plan_productionOrder, u_mes_plan_productionOrderRelease, u_mes_plan_productionSchedule, u_mes_plan_dispatchList, u_mes_plan_operationExecution, u_mes_plan_stepCompletion, u_mes_plan_container, u_mes_plan_labourBooking, u_mes_plan_changeover, u_mes_plan_changeoverStep, u_mes_plan_changeoverPerformedByUser, u_mes_plan_shiftHandover, u_mes_plan_shiftHandoverOpenItem, u_mes_matl_inventoryBalance, u_mes_matl_materialMovement, u_mes_matl_goodsReceipt, u_mes_matl_kit, u_mes_matl_materialRequest, u_mes_matl_materialConsumption, u_mes_matl_label, u_mes_matl_shipment, u_mes_trac_genealogyLink, u_mes_trac_componentLotLink, u_mes_trac_asBuiltRecord, u_mes_trac_asBuiltRecordOperation, u_mes_qual_controlPlan, u_mes_qual_controlPlanCoreTeamUser, u_mes_qual_inspectionPlan, u_mes_qual_checkSheet, u_mes_qual_checkSheetResult, u_mes_qual_inspectionResult, u_mes_qual_spcChart, u_mes_qual_spcSample, u_mes_qual_nonconformance, u_mes_qual_nonconformanceAffectedObject, u_mes_qual_nonconformanceContainmentAction, u_mes_qual_nonconformanceMrbUser, u_mes_qual_reworkOrder, u_mes_qual_reworkOrderStep, u_mes_qual_scrapRecord, u_mes_qual_qualityHold, u_mes_qual_deviationPermit, u_mes_qual_deviationPermitApproval, u_mes_qual_capa, u_mes_qual_capaTeamMember, u_mes_qual_capaContainmentAction, u_mes_qual_capaCorrectiveAction, u_mes_qual_capaImplementationAction, u_mes_qual_pfmea, u_mes_qual_pfmeaCoreTeamUser, u_mes_qual_pfmeaLine, u_mes_qual_ppapSubmission, u_mes_qual_gauge, u_mes_qual_gaugeCalibration, u_mes_qual_msaStudy, u_mes_qual_msaStudyAppraiserUser, u_mes_qual_msaStudyTrial, u_mes_qual_audit, u_mes_qual_auditAuditorUser, u_mes_qual_auditFinding, u_mes_qual_customerComplaint, u_mes_qual_customerComplaintCommunication, u_mes_perf_downtimeEvent, u_mes_perf_downtimeEventComment, u_mes_perf_alarm, u_mes_perf_torqueResult, u_mes_perf_leakTestResult, u_mes_maint_maintenanceWorkOrder, u_mes_maint_maintenanceWorkOrderAssignedToUser, u_mes_maint_maintenanceWorkOrderLabour, u_mes_maint_toolLifeRecord, u_mes_syst_integrationConnector, u_mes_syst_operatorApp, u_mes_syst_businessEvent, u_mes_syst_auditTrail, u_mes_syst_electronicSignature, u_mes_syst_notification, u_mes_syst_notificationRecipient, u_mes_syst_controlledDocument, u_mes_syst_numberRange, u_mes_plan_andonEvent, u_mes_plan_andonEventEscalation, u_mes_ehs_safetyIncident, u_mes_ehs_safetyIncidentWitnessUser, u_mes_ehs_safetyIncidentAction, u_mes_mast_department, u_mes_plan_operatorSession, u_mes_plan_documentAcknowledgement, u_mes_plan_interlockEvent, u_mes_plan_recipeDownload, u_mes_plan_setupVerification, u_mes_matl_exposureTimer, u_mes_trac_traceInvestigation, u_mes_qual_curveEnvelope, u_mes_qual_defectRecord, u_mes_qual_auditSchedule, u_mes_perf_operatorPerformance, u_mes_maint_maintenanceWorkOrderTask, u_mes_maint_sparePartTransaction, u_mes_maint_equipmentLifecycleEvent, u_mes_syst_analyticsModel, u_mes_syst_modelPrediction, u_mes_syst_simulationStudy, u_mes_syst_savedView, u_mes_syst_backupRun, u_mes_syst_computerisedSystem, u_mes_syst_systemValidation, u_mes_syst_systemPeriodicReview, u_mes_syst_auditTrailReview, u_mes_syst_userAccessReview, u_mes_syst_userAccessReviewLine, u_mes_bmr_batchRecordReview, u_mes_bmr_batchRecordReviewException, u_mes_bmr_batchRelease, u_mes_bmr_yieldReconciliation, u_mes_plan_lineClearance, u_mes_maint_logbookEntry, u_mes_maint_cleaningRecord, u_mes_qual_environmentalMonitoringResult, u_mes_matl_dispenseRecord, u_mes_qual_retentionSample, u_mes_qual_riskAssessment, u_mes_qual_productQualityReview, u_mes_qual_productRecall, u_mes_qual_processValidation, u_mes_maint_equipmentQualification, u_mes_mmr_masterManufacturingRecord, u_mes_bmr_batchManufacturingRecord.

In addition, every collection carries siteId, and every transaction collection carries createdById and updatedById.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_user.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_user.js
- Sample documents (10): 03_design/01_master_data_management/samples/u_mes_mast_user.js
