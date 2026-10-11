# u_mes_mdm_user

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | People and system accounts; badge id, role, home work centre |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | USR-<recordNo> |
| Display value used by references | fullName |
| Keys | 33 (24 required, 9 may be null) |
| Estimated volume per year | 300-1,500 per site |
| Storage | standard |

## Structure

Flat entity collection: one document per user, all keys top-level and scalar.

Repeating data of this entity is held in separate collections, one document per occurrence, each pointing back with userId:

| Collection | Kind | Holds |
|---|---|---|
| u_mes_mdm_userRole | Relationship | role |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: USR-<recordNo> | `"USR-10231"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"10231"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | userName | String | Yes | User name | `"sunil.jadhav"` |  |
| 6 | fullName | String | Yes | Full name | `"Sunil Jadhav"` |  |
| 7 | userType | String | Yes | User type | `"Employee"` | Employee; Contractor; System |
| 8 | departmentId | String | Yes | Reference to u_mes_mdm_department._id | `"DEPT-PROD"` | Reference: u_mes_mdm_department._id |
| 9 | departmentName | String | Yes | Display value of departmentId, copied from u_mes_mdm_department.name | `"Production"` |  |
| 10 | designationId | String | Yes | Reference to u_mes_mdm_designation._id | `"DSG-ASM-OPR"` | Reference: u_mes_mdm_designation._id |
| 11 | designationName | String | Yes | Display value of designationId, copied from u_mes_mdm_designation.name | `"Assembly Operator"` |  |
| 12 | badgeNo | String | Yes | Number encoded on the operator badge used for station login | `"B-0010231"` |  |
| 13 | email | String | No (null allowed) | Email of the user | `"sunil.jadhav@varunabrakes.example"` |  |
| 14 | mobile | String | No (null allowed) | Mobile of the user | `"+91-98220-55142"` |  |
| 15 | defaultShiftId | String | Yes | Reference to u_mes_mdm_shift._id: default shift | `"SH-A"` | Reference: u_mes_mdm_shift._id |
| 16 | defaultShiftName | String | Yes | Display value of defaultShiftId, copied from u_mes_mdm_shift.name | `"Shift A"` |  |
| 17 | homeWorkCenterId | String | No (null allowed) | Reference to u_mes_mdm_workCenter._id: home work center | `"WC-TRQ-01"` | Reference: u_mes_mdm_workCenter._id |
| 18 | homeWorkCenterName | String | No (null allowed) | Display value of homeWorkCenterId, copied from u_mes_mdm_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 19 | reportsToUserId | String | No (null allowed) | Reference to u_mes_mdm_user._id: reports to user | `"USR-10045"` | Reference: u_mes_mdm_user._id |
| 20 | reportsToUserName | String | No (null allowed) | Display value of reportsToUserId, copied from u_mes_mdm_user.fullName | `"Rajesh Patil"` |  |
| 21 | dateOfJoining | Date | Yes | Date of joining (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 22 | employmentTypeId | String | Yes | Reference to u_mes_mdm_employmentType._id | `"EMT-PERM"` | Reference: u_mes_mdm_employmentType._id |
| 23 | employmentTypeName | String | Yes | Display value of employmentTypeId, copied from u_mes_mdm_employmentType.name | `"Permanent"` |  |
| 24 | contractorSupplierId | String | No (null allowed) | Reference to u_mes_mdm_supplier._id: contractor supplier | `null` | Reference: u_mes_mdm_supplier._id |
| 25 | contractorSupplierName | String | No (null allowed) | Display value of contractorSupplierId, copied from u_mes_mdm_supplier.name | `null` |  |
| 26 | languageId | String | Yes | Reference to u_mes_mdm_language._id | `"LNG-en"` | Reference: u_mes_mdm_language._id |
| 27 | languageName | String | Yes | Display value of languageId, copied from u_mes_mdm_language.name | `"English"` |  |
| 28 | lastLoginAt | Date | No (null allowed) | Last login date and time | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 29 | failedLoginCount | Int32 | Yes | Failed login count | `NumberInt(0)` |  |
| 30 | passwordChangedAt | Date | Yes | Password changed date and time | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 31 | isLocked | Boolean | Yes | True when the record is locked | `false` |  |
| 32 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Suspended; Left |
| 33 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Suspended, Left. Initial state: Active. The values are maintained in u_mes_sys_statusDefinition.

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

u_mes_mdm_siteCertificate, u_mes_mdm_area, u_mes_mdm_shiftRoster, u_mes_mdm_shiftRosterAssignment, u_mes_mdm_user, u_mes_mdm_userRole, u_mes_mdm_skillCertification, u_mes_prd_billOfMaterial, u_mes_prd_routing, u_mes_prd_billOfProcess, u_mes_prd_workInstruction, u_mes_prd_recipe, u_mes_prd_engineeringChange, u_mes_prd_engineeringChangeApproval, u_mes_exe_productionOrder, u_mes_exe_productionOrderRelease, u_mes_exe_productionSchedule, u_mes_exe_dispatchList, u_mes_exe_operationExecution, u_mes_exe_stepCompletion, u_mes_exe_container, u_mes_exe_labourBooking, u_mes_exe_changeover, u_mes_exe_changeoverStep, u_mes_exe_changeoverPerformedByUser, u_mes_exe_shiftHandover, u_mes_exe_shiftHandoverOpenItem, u_mes_mat_inventoryBalance, u_mes_mat_materialMovement, u_mes_mat_goodsReceipt, u_mes_mat_kit, u_mes_mat_materialRequest, u_mes_mat_materialConsumption, u_mes_mat_label, u_mes_mat_shipment, u_mes_trc_genealogyLink, u_mes_trc_componentLotLink, u_mes_trc_asBuiltRecord, u_mes_trc_asBuiltRecordOperation, u_mes_qlt_controlPlan, u_mes_qlt_controlPlanCoreTeamUser, u_mes_qlt_inspectionPlan, u_mes_qlt_checkSheet, u_mes_qlt_checkSheetResult, u_mes_qlt_inspectionResult, u_mes_qlt_spcChart, u_mes_qlt_spcSample, u_mes_qlt_nonconformance, u_mes_qlt_nonconformanceAffectedObject, u_mes_qlt_nonconformanceContainmentAction, u_mes_qlt_nonconformanceMrbUser, u_mes_qlt_reworkOrder, u_mes_qlt_reworkOrderStep, u_mes_qlt_scrapRecord, u_mes_qlt_qualityHold, u_mes_qlt_deviationPermit, u_mes_qlt_deviationPermitApproval, u_mes_qlt_capa, u_mes_qlt_capaTeamMember, u_mes_qlt_capaContainmentAction, u_mes_qlt_capaCorrectiveAction, u_mes_qlt_capaImplementationAction, u_mes_qlt_pfmea, u_mes_qlt_pfmeaCoreTeamUser, u_mes_qlt_pfmeaLine, u_mes_qlt_ppapSubmission, u_mes_qlt_gauge, u_mes_qlt_gaugeCalibration, u_mes_qlt_msaStudy, u_mes_qlt_msaStudyAppraiserUser, u_mes_qlt_msaStudyTrial, u_mes_qlt_audit, u_mes_qlt_auditAuditorUser, u_mes_qlt_auditFinding, u_mes_qlt_customerComplaint, u_mes_qlt_customerComplaintCommunication, u_mes_eqp_downtimeEvent, u_mes_eqp_downtimeEventComment, u_mes_eqp_alarm, u_mes_eqp_torqueResult, u_mes_eqp_leakTestResult, u_mes_mnt_maintenanceWorkOrder, u_mes_mnt_maintenanceWorkOrderAssignedToUser, u_mes_mnt_maintenanceWorkOrderLabour, u_mes_mnt_toolLifeRecord, u_mes_sys_integrationConnector, u_mes_sys_operatorApp, u_mes_sys_businessEvent, u_mes_sys_auditTrail, u_mes_sys_electronicSignature, u_mes_sys_notification, u_mes_sys_notificationRecipient, u_mes_sys_controlledDocument, u_mes_sys_numberRange, u_mes_ehs_andonEvent, u_mes_ehs_andonEventEscalation, u_mes_ehs_safetyIncident, u_mes_ehs_safetyIncidentWitnessUser, u_mes_ehs_safetyIncidentAction, u_mes_mdm_department.

In addition, every collection carries siteId, and every transaction collection carries createdById and updatedById.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_user.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_user.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_user.js
