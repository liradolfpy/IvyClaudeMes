# u_mes_mast_user

| Property | Value |
|---|---|
| Module | Master Data Management (mast) |
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
| u_mes_mast_userRole | Relationship | role |

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: USR-<recordNo> | `"USR-10231"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"10231"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | userName | String | Yes | User name | `"sunil.jadhav"` |  |
| 6 | fullName | String | Yes | Full name | `"Sunil Jadhav"` |  |
| 7 | userType | String | Yes | User type | `"Employee"` | Employee; Contractor; System |
| 8 | departmentId | String | Yes | Reference to u_mes_mast_department._id | `"DEPT-PROD"` | Reference: u_mes_mast_department._id |
| 9 | departmentName | String | Yes | Display value of departmentId, copied from u_mes_mast_department.name | `"Production"` |  |
| 10 | designationId | String | Yes | Reference to u_mes_mast_designation._id | `"DSG-ASM-OPR"` | Reference: u_mes_mast_designation._id |
| 11 | designationName | String | Yes | Display value of designationId, copied from u_mes_mast_designation.name | `"Assembly Operator"` |  |
| 12 | badgeNo | String | Yes | Number encoded on the operator badge used for station login | `"B-0010231"` |  |
| 13 | email | String | No (null allowed) | Email of the user | `"sunil.jadhav@varunabrakes.example"` |  |
| 14 | mobile | String | No (null allowed) | Mobile of the user | `"+91-98220-55142"` |  |
| 15 | defaultShiftId | String | Yes | Reference to u_mes_mast_shift._id: default shift | `"SH-A"` | Reference: u_mes_mast_shift._id |
| 16 | defaultShiftName | String | Yes | Display value of defaultShiftId, copied from u_mes_mast_shift.name | `"Shift A"` |  |
| 17 | homeWorkCenterId | String | No (null allowed) | Reference to u_mes_mast_workCenter._id: home work center | `"WC-TRQ-01"` | Reference: u_mes_mast_workCenter._id |
| 18 | homeWorkCenterName | String | No (null allowed) | Display value of homeWorkCenterId, copied from u_mes_mast_workCenter.name | `"Bleed Screw Torque Station"` |  |
| 19 | reportsToUserId | String | No (null allowed) | Reference to u_mes_mast_user._id: reports to user | `"USR-10045"` | Reference: u_mes_mast_user._id |
| 20 | reportsToUserName | String | No (null allowed) | Display value of reportsToUserId, copied from u_mes_mast_user.fullName | `"Rajesh Patil"` |  |
| 21 | dateOfJoining | Date | Yes | Date of joining (calendar date, stored as the start of that day in IST converted to UTC) | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 22 | employmentTypeId | String | Yes | Reference to u_mes_mast_employmentType._id | `"EMT-PERM"` | Reference: u_mes_mast_employmentType._id |
| 23 | employmentTypeName | String | Yes | Display value of employmentTypeId, copied from u_mes_mast_employmentType.name | `"Permanent"` |  |
| 24 | contractorSupplierId | String | No (null allowed) | Reference to u_mes_mast_supplier._id: contractor supplier | `null` | Reference: u_mes_mast_supplier._id |
| 25 | contractorSupplierName | String | No (null allowed) | Display value of contractorSupplierId, copied from u_mes_mast_supplier.name | `null` |  |
| 26 | languageId | String | Yes | Reference to u_mes_mast_language._id | `"LNG-en"` | Reference: u_mes_mast_language._id |
| 27 | languageName | String | Yes | Display value of languageId, copied from u_mes_mast_language.name | `"English"` |  |
| 28 | lastLoginAt | Date | No (null allowed) | Last login date and time | `ISODate("2026-09-29T00:35:00.000+0000")` |  |
| 29 | failedLoginCount | Int32 | Yes | Failed login count | `NumberInt(0)` |  |
| 30 | passwordChangedAt | Date | Yes | Password changed date and time | `ISODate("2026-03-31T18:30:00.000+0000")` |  |
| 31 | isLocked | Boolean | Yes | True when the record is locked | `false` |  |
| 32 | status | String | Yes | Primary lifecycle state of the document | `"Active"` | Active; Suspended; Left |
| 33 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

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

u_mes_mast_siteCertificate, u_mes_mast_area, u_mes_mast_shiftRoster, u_mes_mast_shiftRosterAssignment, u_mes_mast_user, u_mes_mast_userRole, u_mes_mast_skillCertification, u_mes_prod_billOfMaterial, u_mes_prod_routing, u_mes_prod_billOfProcess, u_mes_prod_workInstruction, u_mes_prod_recipe, u_mes_prod_engineeringChange, u_mes_prod_engineeringChangeApproval, u_mes_plan_productionOrder, u_mes_plan_productionOrderRelease, u_mes_plan_productionSchedule, u_mes_plan_dispatchList, u_mes_plan_operationExecution, u_mes_plan_stepCompletion, u_mes_plan_container, u_mes_plan_labourBooking, u_mes_plan_changeover, u_mes_plan_changeoverStep, u_mes_plan_changeoverPerformedByUser, u_mes_plan_shiftHandover, u_mes_plan_shiftHandoverOpenItem, u_mes_matl_inventoryBalance, u_mes_matl_materialMovement, u_mes_matl_goodsReceipt, u_mes_matl_kit, u_mes_matl_materialRequest, u_mes_matl_materialConsumption, u_mes_matl_label, u_mes_matl_shipment, u_mes_trac_genealogyLink, u_mes_trac_componentLotLink, u_mes_trac_asBuiltRecord, u_mes_trac_asBuiltRecordOperation, u_mes_qual_controlPlan, u_mes_qual_controlPlanCoreTeamUser, u_mes_qual_inspectionPlan, u_mes_qual_checkSheet, u_mes_qual_checkSheetResult, u_mes_qual_inspectionResult, u_mes_qual_spcChart, u_mes_qual_spcSample, u_mes_qual_nonconformance, u_mes_qual_nonconformanceAffectedObject, u_mes_qual_nonconformanceContainmentAction, u_mes_qual_nonconformanceMrbUser, u_mes_qual_reworkOrder, u_mes_qual_reworkOrderStep, u_mes_qual_scrapRecord, u_mes_qual_qualityHold, u_mes_qual_deviationPermit, u_mes_qual_deviationPermitApproval, u_mes_qual_capa, u_mes_qual_capaTeamMember, u_mes_qual_capaContainmentAction, u_mes_qual_capaCorrectiveAction, u_mes_qual_capaImplementationAction, u_mes_qual_pfmea, u_mes_qual_pfmeaCoreTeamUser, u_mes_qual_pfmeaLine, u_mes_qual_ppapSubmission, u_mes_qual_gauge, u_mes_qual_gaugeCalibration, u_mes_qual_msaStudy, u_mes_qual_msaStudyAppraiserUser, u_mes_qual_msaStudyTrial, u_mes_qual_audit, u_mes_qual_auditAuditorUser, u_mes_qual_auditFinding, u_mes_qual_customerComplaint, u_mes_qual_customerComplaintCommunication, u_mes_perf_downtimeEvent, u_mes_perf_downtimeEventComment, u_mes_perf_alarm, u_mes_perf_torqueResult, u_mes_perf_leakTestResult, u_mes_maint_maintenanceWorkOrder, u_mes_maint_maintenanceWorkOrderAssignedToUser, u_mes_maint_maintenanceWorkOrderLabour, u_mes_maint_toolLifeRecord, u_mes_syst_integrationConnector, u_mes_syst_operatorApp, u_mes_syst_businessEvent, u_mes_syst_auditTrail, u_mes_syst_electronicSignature, u_mes_syst_notification, u_mes_syst_notificationRecipient, u_mes_syst_controlledDocument, u_mes_syst_numberRange, u_mes_plan_andonEvent, u_mes_plan_andonEventEscalation, u_mes_ehs_safetyIncident, u_mes_ehs_safetyIncidentWitnessUser, u_mes_ehs_safetyIncidentAction, u_mes_mast_department.

In addition, every collection carries siteId, and every transaction collection carries createdById and updatedById.

## Files

- Validator: 03_design/01_master_data_management/validators/u_mes_mast_user.json
- Indexes: 03_design/01_master_data_management/indexes/u_mes_mast_user.js
- Sample document: 03_design/01_master_data_management/samples/u_mes_mast_user.js
