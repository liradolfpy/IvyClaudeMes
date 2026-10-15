# BMR and MMR modules - designation of collections

Date: 12 October 2026 | Owner instruction of 12 October 2026 | Decisions D054-D059 | Model version 2.9

## 1. Instruction

The owner asked for two new modules:

- **BMR - BatchManufacturingRecord**
- **MMR - MasterManufacturingRecord**

Collections unique to the BMR or the MMR are to be designated to the new modules. Collections shared by BMR or MMR and the rest of the MES are **not** moved. They are listed below so that the owner can decide on them.

## 2. Modules added

| Module code | Module name | Module folder | Collections |
|---|---|---|---|
| bmr | BatchManufacturingRecord | 11_batch_manufacturing_record | 5 (4 moved, 1 added by decision 2) |
| mmr | MasterManufacturingRecord | 12_master_manufacturing_record | 2 (added by decision 1) |

The codes are three letters, like `ehs`. The standard asks for four or five letters (data_modeling_standard section 1), but the owner named the modules BMR and MMR. The standard is amended to allow three-letter codes fixed by the owner (D054).

## 3. Rule used to decide "unique"

A collection is unique to the BMR when it exists only to compile, review, reconcile or release the executed batch record. No execution, material, traceability, quality, maintenance or system function of the MES writes it or depends on it to do its own work.

A collection is unique to the MMR when it exists only to define, approve or version the master manufacturing record. No MES function uses it at execution time.

A collection that is part of a batch record or master record, but is also written or read by another MES function, is **common**.

## 4. Collections moved to the new modules

Collection numbers and `_id` values are unchanged (D042). Only the module code in the name and the module folder change. All four were added by GMP_Pharma_01 on 12 October 2026, so no data outside the samples refers to the old names.

| No | Old name | New name | Why it is unique to the BMR |
|---|---|---|---|
| 1350 | u_mes_qual_batchRecordReview | u_mes_bmr_batchRecordReview | Production and quality review of the executed batch record of one order; exists only for the BMR |
| 1351 | u_mes_qual_batchRecordReviewException | u_mes_bmr_batchRecordReviewException | Exceptions found in that review (child of the review) |
| 1352 | u_mes_qual_batchRelease | u_mes_bmr_batchRelease | Release decision of the quality unit on the reviewed batch record; the closing step of the BMR |
| 1353 | u_mes_plan_yieldReconciliation | u_mes_bmr_yieldReconciliation | Yield, component and label reconciliation of a batch; a mandatory section of the BMR, calculated only for it |

References to these collections from other collections keep working, because references use `_id` values: for example `batchRecordReviewId` on the production order, `batchReleaseId` on the lot, and `yieldReconciliationId` on the batch record review. Only the target collection name in the specifications changed.

## 5. MasterManufacturingRecord: no unique collection found

Every collection that holds master-record content is also used by the MES at execution time: by dispatching, operator guidance, interlocks, recipe download, inspection, packing and labelling. **No collection was moved to `mmr`.** After the owner's decision of 12 October 2026 the module holds the new master record header and its recipe links (section 9).

## 6. Common collections (not moved) - for the owner's decision

### 6.1 Common to the BMR and the MES

| Collection | Current module | BMR content it provides | Other MES use |
|---|---|---|---|
| u_mes_plan_productionOrder | plan | The batch: identity, quantities, dates, links to review, clearance and yield | Planning, dispatching, ERP interface, OEE |
| u_mes_plan_productionOrderRelease | plan | Release of the order to the shop floor | Dispatching |
| u_mes_plan_productionOrderLot | plan | Lots produced by the batch | Planning, traceability |
| u_mes_plan_lot | plan | Batch or lot number, quantity, expiry, retest, release link | Material status, stock, traceability |
| u_mes_plan_lotParentLot | plan | Lot genealogy | Traceability |
| u_mes_plan_operationExecution | plan | Executed steps: who, when, equipment, result, recipe version | Execution, OEE, interlocks |
| u_mes_plan_operationExecutionDefectCode | plan | Defects recorded in a step | Quality statistics |
| u_mes_plan_operationExecutionTool | plan | Tools used in a step | Tool life |
| u_mes_plan_stepCompletion | plan | Confirmation of each instruction step | Operator guidance |
| u_mes_plan_wipUnit | plan | Units of the batch | Execution, traceability |
| u_mes_plan_lineClearance | plan | Line clearance section of the BMR | Interlock before order start; equipment and area logbook |
| u_mes_plan_interlockEvent | plan | Blocks and overrides during the batch (review exceptions) | Execution control for all modules |
| u_mes_plan_operatorSession | plan | Who was logged in at each station | Access control, labour |
| u_mes_plan_documentAcknowledgement | plan | Proof that current instructions were read | Training |
| u_mes_plan_recipeDownload | plan | Program version loaded for the batch | Equipment integration |
| u_mes_plan_setupVerification | plan | Set-up check before the batch | Changeover |
| u_mes_plan_setupVerificationItem | plan | Items of the set-up check | Changeover |
| u_mes_plan_changeover | plan | Changeover and first-off approval | Planning, OEE |
| u_mes_plan_labourBooking | plan | Personnel on the batch | Labour costing |
| u_mes_matl_dispenseRecord | matl | Dispensing section of the BMR | Material issue to the order |
| u_mes_matl_materialConsumption | matl | Materials and lots consumed | Stock, ERP backflush |
| u_mes_matl_kit | matl | Materials staged for the batch | Line supply |
| u_mes_matl_kitLine | matl | Lines of the kit | Line supply |
| u_mes_matl_label | matl | Labels printed for the batch (label reconciliation) | Packing, dispatch |
| u_mes_matl_exposureTimer | matl | Hold times during the batch | Material control |
| u_mes_matl_materialMovement | matl | Issues and returns of the batch | Stock |
| u_mes_trac_serialNumber | trac | Serial numbers of the batch | Traceability, dispatch |
| u_mes_trac_asBuiltRecord | trac | Unit-level executed record | Traceability, complaints |
| u_mes_trac_asBuiltRecordComponent | trac | Components built in | Traceability |
| u_mes_trac_asBuiltRecordOperation | trac | Operations per unit | Traceability |
| u_mes_trac_asBuiltRecordInspectionResult | trac | Results per unit | Traceability |
| u_mes_trac_genealogyLink | trac | Parent-child genealogy of the batch | Traceability |
| u_mes_trac_componentLotLink | trac | Component lots used | Traceability, recall |
| u_mes_qual_inspectionResult | qual | In-process and final results | SPC, nonconformance |
| u_mes_qual_checkSheetResult | qual | Checklists done during the batch | Start-of-shift checks, audits |
| u_mes_qual_checkSheetResultAnswer | qual | Checklist answers | Same |
| u_mes_qual_spcSample | qual | In-process control samples | SPC |
| u_mes_qual_measurementCurve | qual | Press, torque and leak curves of the batch | Process monitoring |
| u_mes_qual_defectRecord | qual | Defects found in the batch | Quality statistics |
| u_mes_qual_nonconformance | qual | Deviations of the batch | Quality management for all sources |
| u_mes_qual_deviationPermit | qual | Planned deviations used | Quality management |
| u_mes_qual_qualityHold | qual | Holds on the batch | Material and order status |
| u_mes_qual_environmentalMonitoringResult | qual | Room conditions during the batch | Environmental monitoring programme |
| u_mes_qual_retentionSample | qual | Retained samples of the batch | Complaint investigation |
| u_mes_perf_torqueResult | perf | Torque results | Process monitoring |
| u_mes_perf_leakTestResult | perf | Leak test results | Process monitoring |
| u_mes_perf_leakTestResultStage | perf | Results per test stage | Process monitoring |
| u_mes_perf_processReading | perf | Critical process parameters during the batch | Historian, alarms (time series) |
| u_mes_maint_cleaningRecord | maint | Cleaning before and after the batch | Equipment status |
| u_mes_maint_logbookEntry | maint | Equipment and area use log | Maintenance, calibration, qualification |
| u_mes_syst_electronicSignature | syst | Signatures on the batch record | Signatures for every module |
| u_mes_syst_auditTrail | syst | Changes to batch data | Audit trail for every module |
| u_mes_syst_auditTrailChange | syst | Changed values | Same |
| u_mes_syst_auditTrailReview | syst | Audit-trail review of the batch | Periodic system reviews |
| u_mes_syst_recordPolicy | syst | Lock and retention of batch records | Record policy for every collection |

### 6.2 Common to the MMR and the MES

| Collection | Current module | MMR content it provides | MES use at execution |
|---|---|---|---|
| u_mes_prod_item | prod | Product and material master | Everywhere |
| u_mes_prod_itemRevision | prod | Drawing and specification revision | Revision control |
| u_mes_prod_productVariant | prod | Variant made under the record | Variant checks |
| u_mes_prod_billOfMaterial | prod | Master formula: components and quantities | Kitting, consumption, genealogy |
| u_mes_prod_billOfMaterialComponent | prod | Component lines | Same |
| u_mes_prod_billOfMaterialComponentProductVariant | prod | Variant-specific components | Same |
| u_mes_prod_billOfMaterialComponentAlternateItem | prod | Approved alternates | Same |
| u_mes_prod_operation | prod | Process steps | Dispatching |
| u_mes_prod_routing | prod | Sequence of steps | Sequence interlock |
| u_mes_prod_routingStep | prod | Steps of the routing | Same |
| u_mes_prod_routingStepAlternateWorkCenter | prod | Approved alternate stations | Dispatching |
| u_mes_prod_routingStepNextStep | prod | Step sequence | Sequence interlock |
| u_mes_prod_billOfProcess | prod | Manufacturing instructions per step | Operator guidance, interlocks |
| u_mes_prod_billOfProcessStep | prod | Steps | Same |
| u_mes_prod_billOfProcessStepEquipment | prod | Equipment per step | Equipment readiness check |
| u_mes_prod_billOfProcessStepTool | prod | Tools per step | Set-up verification |
| u_mes_prod_billOfProcessStepRequiredSkill | prod | Skills per step | Skill check at login |
| u_mes_prod_billOfProcessStepConsumedComponent | prod | Components per step | Component scan |
| u_mes_prod_billOfProcessStepInterlock | prod | Controls per step | Interlocks |
| u_mes_prod_billOfProcessStepProcessParameter | prod | Critical process parameters and limits | Parameter monitoring |
| u_mes_prod_recipe | prod | Approved machine programs | Recipe download |
| u_mes_prod_recipeParameter | prod | Program parameters | Same |
| u_mes_prod_recipeStage | prod | Program stages | Same |
| u_mes_prod_recipeProductVariant | prod | Variants per program | Same |
| u_mes_prod_recipeControlledDocument | prod | Program files and reference curves | Same |
| u_mes_prod_workInstruction | prod | Written instructions | Operator display |
| u_mes_prod_workInstructionStep | prod | Instruction steps | Same |
| u_mes_prod_workInstructionStepMediaControlledDocument | prod | Pictures and media | Same |
| u_mes_prod_workInstructionStepProductVariant | prod | Variant-specific steps | Same |
| u_mes_prod_workInstructionStepTool | prod | Tools per step | Same |
| u_mes_prod_workInstructionStepCharacteristic | prod | Checks per step | Data collection |
| u_mes_prod_workInstructionPpeItem | prod | Protective equipment | Safety |
| u_mes_prod_workInstructionKeyPoint | prod | Key points | Operator display |
| u_mes_prod_workInstructionWorkCenter | prod | Stations | Operator display |
| u_mes_prod_workInstructionProductVariant | prod | Variants | Operator display |
| u_mes_prod_engineeringChange (and its 4 child collections) | prod | Change control of the master record | Change control for every product and process change |
| u_mes_qual_characteristic | qual | Specifications and tolerances | Inspection, SPC |
| u_mes_qual_characteristicPosition | qual | Multi-position characteristics | Inspection |
| u_mes_qual_controlPlan | qual | In-process control strategy | Inspection planning |
| u_mes_qual_controlPlanLine | qual | Control plan lines | Same |
| u_mes_qual_controlPlanCoreTeamUser | qual | Authors | APQP |
| u_mes_qual_inspectionPlan | qual | In-process and final tests | Inspection |
| u_mes_qual_inspectionPlanLine | qual | Test lines | Same |
| u_mes_qual_inspectionPlanProductVariant | qual | Variants | Same |
| u_mes_qual_samplingPlan | qual | Sampling | Inspection |
| u_mes_qual_samplingPlanSizeRow | qual | Sample sizes | Same |
| u_mes_qual_checkSheet | qual | Line clearance and in-process checklists | Start-of-shift checks, audits |
| u_mes_qual_checkSheetItem | qual | Checklist items | Same |
| u_mes_qual_curveEnvelope | qual | Accepted curve windows | Curve evaluation |
| u_mes_qual_curveEnvelopeWindow | qual | Windows | Same |
| u_mes_qual_pfmea | qual | Risk basis of the controls | APQP |
| u_mes_qual_processValidation | qual | Validated state of the process the record describes | Validation lifecycle |
| u_mes_qual_riskAssessment | qual | Risk assessment of the master record | Risk assessments of systems, changes and deviations |
| u_mes_matl_packagingSpecification | matl | Packing instructions | Packing |
| u_mes_matl_packagingSpecificationLevel | matl | Packing levels | Packing |
| u_mes_matl_labelTemplate | matl | Approved label specimen | Label printing |
| u_mes_matl_labelTemplateField | matl | Label fields | Label printing |
| u_mes_syst_controlledDocument | syst | Master record document and attachments | Document control for every module |
| u_mes_syst_electronicSignature | syst | Approval signatures of the master record | Signatures for every module |

## 7. Points for the owner's decision

| No | Question | Options | Recommendation |
|---|---|---|---|
| 1 | Should the MMR module hold a master record of its own? | (a) Keep mmr empty and treat the approved set of prod / qual / matl masters as the master record. (b) Add a header collection `u_mes_mmr_masterManufacturingRecord`: one approved, versioned record per item revision that names the BOM, routing, bill of process, recipes, control plan, packaging specification and label template, with batch size, theoretical yield, yield limits, effective dates, status and approval signatures. Add a child `u_mes_mmr_masterManufacturingRecordApproval` for the author, reviewer and approver steps. (c) Move the prod collections into mmr | (b). The master record becomes one approvable object, and the execution masters stay where the MES uses them. Option (c) would split the product definition the MES runs on |
| 2 | Should the BMR module hold a batch record header? | (a) Keep `u_mes_plan_productionOrder` as the batch record header. (b) Add `u_mes_bmr_batchManufacturingRecord`: one per order or lot, freezing the master record version used, record status (Compiled, Under Review, Approved, Archived), the export or true copy with its checksum, and links to review and release | (b) if a frozen, exportable record per batch is required by the customer or regulator; otherwise (a) |
| 3 | Line clearance and dispensing exist only because of GMP. Should they move to bmr? | Move `u_mes_plan_lineClearance` and `u_mes_matl_dispenseRecord` to bmr, or keep them where execution and material issue use them | Keep. Both are written at execution time and checked by interlocks |
| 4 | Audit-trail review serves both the batch record review and the periodic system review | Keep in syst, or split into a BMR review and a system review | Keep in syst |

## 8. Checks after the change (12 October 2026)

| Check | Result |
|---|---|
| `flatten_model.py` (names, references, display pairs, one type per key) | 0 problems |
| `gen_specs.py` specification check | 0 findings; 366 collections, 8,142 keys, 1,471 indexes |
| `gen_samples.py` 19 sample checks | 0 findings; 3,660 documents |
| Independent check of samples against validators | 0 problems |
| Every generated file lies in the folder of its module code | 1,464 files, 0 misplaced; 16 files left under the old names in qual and plan were deleted |

## 9. Owner decisions of 12 October 2026 and implementation

| No | Decision | Implementation |
|---|---|---|
| 1 | Add the master record header | `u_mes_mmr_masterManufacturingRecord` (1367, master): one versioned record per item revision with references to bill of material, routing, bill of process, control plan, inspection plan, packaging specification, label template, process validation, master document and engineering change; standard batch size, theoretical quantity, yield limits, effective dates, author, reviewer and approver. Status: In Preparation, In Review, Approved, Effective, Superseded. Recipes are linked through the relationship `u_mes_mmr_masterManufacturingRecordRecipe` (1368), because a record uses several recipes and arrays are not allowed (DATA-001). Approval signatures are kept in `u_mes_syst_electronicSignature`, so no separate approval collection was added |
| 2 | Add the batch record header | `u_mes_bmr_batchManufacturingRecord` (1369, transaction): one per production order (unique). It freezes the master record version at opening (`masterManufacturingRecordId` and `masterRecordVersion`) and links line clearance, yield reconciliation, review and release. It holds the exported true copy (`exportControlledDocumentId`, `checksumSha256`, `pageCount`, `exportedById`, `exportedAt`). Status: Open, In Execution, Compiled, Under Review, Approved, Archived |
| 3 | Line clearance and dispensing stay in plan and matl | No change |
| 4 | Audit-trail review stays in syst | No change |

Result: 369 collections (bmr 5, mmr 2), 8,245 keys, 3,690 sample documents, 1,488 indexes. Checks: `flatten_model.py` 0 problems; specification check 0 findings; 19 sample checks 0 findings; independent validator check of 3,690 samples 0 problems; 1,476 generated files all in the folder of their module.
