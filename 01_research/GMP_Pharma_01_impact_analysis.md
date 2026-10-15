# GMP_Pharma_01 - Pharmaceutical Good Manufacturing Practice: impact analysis and implementation

Date: 12 October 2026 | Task: Good Manufacturing Practices For Pharma | Owner decision: analysis and implementation in the same task (12 Oct 2026) | Decisions D047-D053 | Assumptions A019-A022

## 1. Purpose and scope

Note of 12 October 2026 (D055): batch record review, its exceptions, batch release and yield reconciliation were moved to the new module bmr (BatchManufacturingRecord) after this analysis; the names below are the current ones. See `01_research/BMR_MMR_module_designation.md`.

This document lists the requirements of pharmaceutical Good Manufacturing Practice (GMP) that a manufacturing execution system must support. It checks each requirement against the 343 collections of model version 2.6 and records how the gaps were closed in model version 2.7.

The requirements are adopted as **generic MES capabilities** and mapped to the caliper reference process, in the same way MES_ExternalRequirement_01 was adopted (A016). The model gets the record types that a GMP-regulated plant needs: validated systems, batch record review, release by the quality unit, reconciliation, line clearance, cleaning, environmental monitoring, dispensing, retention samples, quality risk management, product quality review, recall, and process and equipment validation. The sample data stays in the caliper universe (Varuna Brake Systems, Chakan Plant, production fortnight 15 to 26 September 2026). No pharmaceutical reference product was added; the owner did not choose that option.

This is a data-model analysis. It is not a regulatory compliance assessment of a plant or a product (A019).

## 2. Sources

| Ref | Source | Status used |
|---|---|---|
| S1 | US 21 CFR Part 210 and Part 211, Current Good Manufacturing Practice for finished pharmaceuticals | In force |
| S2 | US 21 CFR Part 11, Electronic records; electronic signatures | In force |
| S3 | EudraLex Volume 4, EU GMP Part I, chapters 1 (Pharmaceutical Quality System), 3 (Premises and Equipment), 4 (Documentation), 5 (Production), 8 (Complaints and Recalls), 9 (Self-inspection) | In force; a revised chapter 4 was published as a draft for consultation in July 2025 |
| S4 | EU GMP Annex 11, Computerised Systems (2011) | In force; a revised Annex 11 and a new Annex 22 (Artificial Intelligence) were published as drafts in July 2025. The final status in October 2026 must be confirmed by the owner (A019) |
| S5 | EU GMP Annex 15 (Qualification and Validation), Annex 16 (Certification by a Qualified Person and Batch Release), Annex 19 (Reference and Retention Samples), Annex 1 (Manufacture of Sterile Medicinal Products, 2022) | In force |
| S6 | ICH Q7 (GMP for active pharmaceutical ingredients), ICH Q9(R1) (Quality Risk Management, 2023), ICH Q10 (Pharmaceutical Quality System) | In force |
| S7 | PIC/S PI 041-1, Good Practices for Data Management and Integrity in Regulated GMP/GDP Environments (2021) | In force |
| S8 | India, Drugs Rules 1945, revised Schedule M (G.S.R. 922(E), 28 December 2023): in force for large manufacturers from 2024; the extended deadline for MSME manufacturers was 31 December 2025, with enforcement from 2026 | In force |
| S9 | FDA guidance, Computer Software Assurance for Production and Quality System Software (final, September 2025) | In force; risk-based assurance in place of exhaustive scripted testing |
| S10 | FDA guidance, Process Validation: General Principles and Practices (2011) | In force |
| S11 | ISA-88 (batch control) and ISPE GAMP 5 second edition (2022), used for terminology: master and control recipe, review by exception, software categories | Industry standards |

Web references consulted for current status: [EU stakeholder consultation on Chapter 4, Annex 11 and Annex 22](https://health.ec.europa.eu/consultations/stakeholders-consultation-eudralex-volume-4-good-manufacturing-practice-guidelines-chapter-4-annex_en), [ECA news on the drafts of Annex 11, Annex 22 and Chapter 4](https://www.gmp-compliance.org/gmp-news/drafts-of-eu-gmp-guideline-annex-11-annex-22-and-chapter-4-released-for-comment), [FDA guidance on Computer Software Assurance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/computer-software-assurance-production-and-quality-system-software), [India Briefing on the Schedule M deadline extension](https://india-briefing.com/news/india-extends-gmp-compliance-deadline-to-december-2025-35679.html), [Revised Schedule M enforcement overview](https://laafon.com/cdsco-schedule-m-compliance-dashboard/).

## 3. Mapping of pharmaceutical concepts to the caliper reference (A020)

| Pharmaceutical concept | Caliper reference in the model and samples |
|---|---|
| Batch | Production order (`u_mes_plan_productionOrder`) and, where lot-controlled, its output lot (`u_mes_plan_lot`). Assembly orders produce serialised units without a lot and are released by order |
| Master batch record | Released bill of process, recipes and work instructions (`u_mes_prod_billOfProcess`, `u_mes_prod_recipe`, `u_mes_prod_workInstruction`) |
| Executed batch record | Operation executions, step completions, material consumption, as-built record, inspection, torque and leak test results, interlock events, logbook entries |
| Quality unit / Qualified Person | Quality department; in the samples Anita Kulkarni (quality engineer) reviews and releases, and Meera Deshpande (manager) approves product quality reviews |
| Weighing and dispensing | Weighing of A356 ingot charges for casting orders; count-by-weight kitting of piston seals, dust boots and bleed screws for assembly orders |
| Classified room | Assembly clean area (area ASY) classified ISO 8 for technical cleanliness of the brake hydraulic parts; final inspection cell and quality laboratory as controlled, not classified areas |
| Equipment cleaning and hold times | Product changeover cleaning of the piston press (LH to RH), wash and anodising bath changes, die cleaning, leak tester fixture and laser lens cleaning |
| Retention samples | Retained castings, machined bodies and finished calipers by serial number; reserve samples of bought-in pistons, seals and bleed screws |
| Recall | Containment at a customer plant (Class II or III) and field actions (Class I for a brake fluid leak) |

## 4. Requirement catalogue

Coverage before the change: C = covered by the existing model, P = partly covered (keys or allowed values added), G = gap (new collection), O = outside the scope of the MES model.

### 4.1 Computerised systems and data integrity

| No | Source | Requirement | Coverage | Resolution |
|---|---|---|---|---|
| GMP-01 | S2 11.10(a); S4 4.3; S8 | Systems that hold GMP records are validated, and an up-to-date inventory states their GMP functionality and impact | G | `u_mes_syst_computerisedSystem` (GxP impact, GAMP category, data criticality, Part 11 scope, owners, review cycle) |
| GMP-02 | S4 1, 4; S9; S11 | Validation is risk-based and documented; the assurance effort follows the risk | G | `u_mes_syst_systemValidation` (validation type, assurance approach, tests, deviations, approval) linked to `u_mes_qual_riskAssessment` |
| GMP-03 | S4 11 | Computerised systems are periodically evaluated to confirm they stay in a validated state | G | `u_mes_syst_systemPeriodicReview` |
| GMP-04 | S2 11.10(e); S4 9; S7 | A secure, computer-generated, time-stamped audit trail records who, what, when, old and new value and why | P | Already in `u_mes_syst_auditTrail` + `u_mes_syst_auditTrailChange` with hash chain. Added `gxpRelevant` and `auditTrailReviewId` |
| GMP-05 | S4 9; S7 9; S3 ch. 4 draft | Audit trails of GMP-relevant data are reviewed regularly and as part of batch record review | G | `u_mes_syst_auditTrailReview` (by batch record, periodic or for cause) |
| GMP-06 | S2 11.50, 11.70, 11.100, 11.200 | An electronic signature is unique, linked to its record, and shows printed name, date and time and meaning; in a continuous session the first signing uses both components | P | `u_mes_syst_electronicSignature` already holds user, meaning, time, content hash. Added `signatureManifestationText`, `signedRecordVersion`, `isFirstSigningInSession` |
| GMP-07 | S2 11.10(d), (g), 11.300; S4 12 | Access is limited to authorised individuals; identities are unique; access rights are reviewed periodically; passwords are aged | G | `u_mes_syst_userAccessReview` + `u_mes_syst_userAccessReviewLine`; `lastAccessReviewDate`, `passwordExpiryDate` on `u_mes_mast_user` |
| GMP-08 | S2 11.10(f) | Operational system checks enforce the permitted sequence of steps | C | `u_mes_syst_interlockRule`, `u_mes_syst_statusTransition`, `u_mes_syst_statusTransitionRole` (D036, D037) |
| GMP-09 | S2 11.10(h) | Device checks confirm the validity of the source of data input | C | `u_mes_plan_operatorSession`, `u_mes_syst_operatorAppDeviceBinding`, `u_mes_syst_iotDevice` |
| GMP-10 | S2 11.10(b), (c); S4 7, 8, 17 | Accurate and complete copies can be produced; records are protected and retained for the retention period | P | `u_mes_syst_recordPolicy`, `u_mes_syst_backupRun`, `u_mes_syst_controlledDocument` checksum. Added `gxpRelevant` to `u_mes_syst_recordPolicy` |
| GMP-11 | S1 211.101(d); S4 6 | Critical data entered manually is checked by a second person or by a validated system | P | Second-person or system verification in `u_mes_matl_dispenseRecord`; manual entries are listed as exceptions in `u_mes_bmr_batchRecordReviewException` |
| GMP-12 | S4 10 | Changes to computerised systems are made under change control | C | `u_mes_prod_engineeringChange` referenced by `u_mes_syst_systemValidation.engineeringChangeId` |
| GMP-13 | S4 13 | Incidents of computerised systems are recorded and assessed | C | `u_mes_qual_nonconformance`, `u_mes_syst_notification`; counted in `u_mes_syst_systemPeriodicReview` |
| GMP-14 | S4 3 | Suppliers and service providers of computerised systems are assessed and their responsibilities agreed | G | `u_mes_syst_computerisedSystem.supplierId` |
| GMP-15 | S4 7.2, 16 | Backups are made and restore is tested; business continuity is provided | C | `u_mes_syst_backupRun` (Restore Test, Failover Test); `backupRestoreVerified` in the periodic review |
| GMP-16 | S4 draft Annex 22 | AI and machine-learning models used in GMP are validated, version-controlled and monitored | C | `u_mes_syst_analyticsModel`, `u_mes_syst_modelPrediction` (D040) |
| GMP-17 | S7 (ALCOA+) | Records are attributable, legible, contemporaneous, original and accurate; system clocks are synchronised | C | Audit keys, `u_mes_syst_auditTrail`; clock source in `u_mes_syst_systemConfiguration` |

### 4.2 Production and process controls

| No | Source | Requirement | Coverage | Resolution |
|---|---|---|---|---|
| GMP-18 | S1 211.186; S3 4.17 | Master production records are approved and version-controlled | C | Status and version of bill of process, recipes and work instructions; signatures in `u_mes_syst_electronicSignature` |
| GMP-19 | S1 211.188; S3 4.20 | Each batch has a production record of every significant step: who, when, equipment, materials, results | C | Operation executions, material consumption, as-built record, results, logbook entries. Reviewed in `u_mes_bmr_batchRecordReview` |
| GMP-20 | S1 211.192; S3 ch. 4; S8 | Production and quality review and approve the batch record before release | G | `u_mes_bmr_batchRecordReview` (production review, quality review, signature); `batchRecordReviewId` on `u_mes_plan_productionOrder` |
| GMP-21 | S11 (review by exception) | Review concentrates on exceptions found by the system | G | `u_mes_bmr_batchRecordReviewException` (overrides, out-of-specification results, manual entries, corrections, missing signatures, deviations, late entries, holds) |
| GMP-22 | S1 211.22, 211.165; S5 Annex 16; S8 | The quality unit decides on release or rejection of each batch | G | `u_mes_bmr_batchRelease`; `batchReleaseId` on `u_mes_plan_lot`; interlock rule type Batch Release Check before dispatch |
| GMP-23 | S1 211.101(c), (d) | Components are weighed, measured or subdivided as specified and checked by a second person or a validated system | G | `u_mes_matl_dispenseRecord`; interlock rule type Dispense Tolerance Check |
| GMP-24 | S1 211.103, 211.192 | Actual yield is calculated at the end of each phase and compared with limits; differences are investigated | G | `u_mes_bmr_yieldReconciliation` (Product Yield); `yieldWithinLimits` on `u_mes_plan_productionOrder` |
| GMP-25 | S1 211.125, 211.130 | Labels issued, used, destroyed and returned are reconciled; discrepancies are investigated | G | `u_mes_bmr_yieldReconciliation` (Label Reconciliation, Component Reconciliation) |
| GMP-26 | S1 211.130(e); S3 5 | Line clearance before an order starts or a product changes, with independent verification | G | `u_mes_plan_lineClearance`; `lineClearanceId` on `u_mes_plan_productionOrder`; interlock rule type Line Clearance Check |
| GMP-27 | S1 211.111 | Time limits for each phase of production (hold times) are set and enforced | P | `u_mes_matl_exposureTimer` timer types Dirty Equipment Hold, Clean Equipment Hold, Process Hold Time added; `cleanHoldExpiresAt` in cleaning records |
| GMP-28 | S1 211.110 | In-process controls and sampling | C | Control plan, inspection plan, sampling plan, SPC |
| GMP-29 | S1 211.115 | Reprocessing is approved and controlled | C | `u_mes_qual_reworkOrder` |
| GMP-30 | S1 211.192; S3 1.4(xiv); S6 Q10 3.2.2 | Deviations are recorded, classified, investigated, extended to other batches, and approved by quality | P | On `u_mes_qual_nonconformance`: `deviationClass`, `productImpactText`, `investigationDueDate`, `qaApprovedById`, `qaApprovedAt`, `riskAssessmentId` |
| GMP-31 | S3 1 | Planned deviations are approved before use | C | `u_mes_qual_deviationPermit` |
| GMP-32 | S10; S5 Annex 15 5; S8 | Processes are validated through the lifecycle: design, qualification, continued verification | G | `u_mes_qual_processValidation` |
| GMP-33 | S5 Annex 15 3; S1 211.63 | Equipment is qualified (DQ, IQ, OQ, PQ) and requalified periodically or after change | G | `u_mes_maint_equipmentQualification`; `qualificationStatus`, `requalificationDueDate` on `u_mes_mast_equipment`; interlock rule type Qualification Status Check |
| GMP-34 | S1 211.67, 211.182 | Equipment is cleaned by procedure; cleaning and use are recorded in a chronological log | G | `u_mes_maint_cleaningRecord`, `u_mes_maint_logbookEntry` (equipment or area) |
| GMP-35 | S3 3.43; S8 | The status of equipment (clean, dirty, qualified, out of use) is identified | P | `cleanStatus`, `cleanHoldExpiresAt`, `lastCleaningRecordId`, `qualificationStatus` on `u_mes_mast_equipment`; interlock rule type Equipment Clean Status Check |
| GMP-36 | S1 211.68, 211.160(b)(4) | Instruments and balances are calibrated and checked | P | `u_mes_qual_gauge`, `u_mes_qual_gaugeCalibration`; calibration type Daily Performance Check added |

### 4.3 Premises and environment

| No | Source | Requirement | Coverage | Resolution |
|---|---|---|---|---|
| GMP-37 | S1 211.42, 211.46; S5 Annex 1; S8 | Areas are classified and controlled for their use; gowning where required | P | On `u_mes_mast_area`: `cleanlinessClass`, `environmentallyMonitored`, `gowningRequired` |
| GMP-38 | S5 Annex 1 9; S8 | Environmental monitoring with alert and action limits; excursions are investigated | G | `u_mes_qual_environmentalMonitoringPoint` (master) and `u_mes_qual_environmentalMonitoringResult` |

### 4.4 Materials

| No | Source | Requirement | Coverage | Resolution |
|---|---|---|---|---|
| GMP-39 | S1 211.84 | Materials are quarantined until released | C | `qualityStatus` on `u_mes_plan_lot`, `u_mes_matl_stockStatus`, interlock rule type Lot Release Check |
| GMP-40 | S3 5.27; S6 Q10 2.7 | Materials are bought only from approved suppliers | P | `qualificationStatus`, `qualifiedUntilDate` on `u_mes_mast_supplierSuppliedItem` |
| GMP-41 | S1 211.87; S6 Q7 7.5 | Materials are re-tested after a set time; expiry is enforced | P | `retestDate` on `u_mes_plan_lot`; expiry and FEFO already present |
| GMP-42 | S1 211.170; S5 Annex 19 | Reserve and retention samples are kept for the required period | G | `u_mes_qual_retentionSample` |

### 4.5 Pharmaceutical quality system

| No | Source | Requirement | Coverage | Resolution |
|---|---|---|---|---|
| GMP-43 | S6 Q9(R1) | Quality risk management is documented, with risk acceptance and review | G | `u_mes_qual_riskAssessment` (the process FMEA stays in `u_mes_qual_pfmea` and is referenced) |
| GMP-44 | S6 Q10 3.2.3; S3 1 | Change control assesses GMP, validation and regulatory impact | P | On `u_mes_prod_engineeringChange`: `gmpImpact`, `validationRequired`, `regulatoryImpact`, `riskAssessmentId` |
| GMP-45 | S6 Q10 3.2.2 | Corrective and preventive action | C | `u_mes_qual_capa` and its child collections |
| GMP-46 | S1 211.180(e); S3 1.10 | Regular product quality review | G | `u_mes_qual_productQualityReview` |
| GMP-47 | S1 211.198; S3 8 | Complaints are recorded and investigated | C | `u_mes_qual_customerComplaint` and its child collections |
| GMP-48 | S3 8; S8 | Recalls are classified, scoped by traceability, reconciled and checked for effectiveness | G | `u_mes_qual_productRecall` + `u_mes_qual_productRecallLot` |
| GMP-49 | S1 211.25 | Personnel are trained on current procedures | C | `u_mes_mast_skillCertification`, `u_mes_plan_documentAcknowledgement` |
| GMP-50 | S3 9 | Self-inspection | C | `u_mes_qual_audit`, `u_mes_qual_auditSchedule` |
| GMP-51 | S3 4; S1 211.100 | Documents are controlled | C | `u_mes_syst_controlledDocument` |

### 4.6 Outside the MES model

| No | Source | Requirement | Coverage | Reason |
|---|---|---|---|---|
| GMP-52 | S1 211.160-211.166, 211.194 | Laboratory controls, out-of-specification investigations in the laboratory, stability programme | O | Laboratory information management system; the MES receives results through `u_mes_qual_inspectionResult` |
| GMP-53 | India QR codes on active ingredients and on listed brands; EU Falsified Medicines Directive; US DSCSA | Serialisation reporting to regulators | O | Serial numbers, labels and aggregation exist; reporting to national repositories belongs to a serialisation system |
| GMP-54 | S5 Annex 1 | Sterile manufacture: contamination control strategy, aseptic process simulation | O | Not applicable to the caliper process |
| GMP-55 | S1 211.48; S8 | Water, HVAC and utilities qualification and monitoring | O | Building management and energy systems; monitored values can enter through `u_mes_perf_processTag` and environmental monitoring points |

### 4.7 Summary

| Coverage | Requirements |
|---|---|
| C - covered | 18 |
| P - partly covered, keys or values added | 12 |
| G - gap, new collection | 21 |
| O - outside the model | 4 |
| Total | 55 |

## 5. New collections (numbers 1344-1366)

| No | Collection | Kind | Data class | Business key (recordNo) | Status values | Requirements | Embed or reference |
|---|---|---|---|---|---|---|---|
| 1344 | u_mes_syst_computerisedSystem | entity | master | CSY-<system code> | In Validation, Validated, Retired | GMP-01, 02, 03, 14 | Own master: a list quality and IT maintain, referenced by four transaction collections |
| 1345 | u_mes_syst_systemValidation | entity | transaction | CSV-<yyyy>-<nnn> | Planned, In Execution, Executed, Approved, Rejected | GMP-02, 12 | Separate: one per release over the system life (unbounded) |
| 1346 | u_mes_syst_systemPeriodicReview | entity | transaction | SPR-<system code>-<yyyy>-<nn> | Planned, In Review, Completed, Approved | GMP-03, 13, 15 | Separate: one per system and period |
| 1347 | u_mes_syst_auditTrailReview | entity | transaction | ATR-<yyyymmdd>-<nnn> | Open, In Review, Completed, Escalated | GMP-04, 05 | Separate; polymorphic link to the reviewed record (order, periodic review, nonconformance) |
| 1348 | u_mes_syst_userAccessReview | entity | transaction | UAR-<system code>-<yyyy>-<nn> | Open, In Review, Completed | GMP-07 | Separate; reviewed accounts as child |
| 1349 | u_mes_syst_userAccessReviewLine | child | transaction | parent recordNo + -L<nnn> | - | GMP-07 | Child (DATA-001) |
| 1350 | u_mes_bmr_batchRecordReview | entity | transaction | BRR-<order number> | Open, Under Review, Returned For Correction, Approved, Rejected | GMP-19, 20, 21 | One per order (unique index on productionOrderId); exceptions as child |
| 1351 | u_mes_bmr_batchRecordReviewException | child | transaction | parent recordNo + -E<nnn> | - | GMP-11, 21, 30 | Child; polymorphic link to the record behind the exception |
| 1352 | u_mes_bmr_batchRelease | entity | transaction | BRL-<lot or order number> | Pending, Released, Conditionally Released, Rejected | GMP-22 | Separate from `u_mes_qual_qualityHold`: a hold blocks, a release decides |
| 1353 | u_mes_bmr_yieldReconciliation | entity | transaction | YRC-<order number>-<nn> | Calculated, Under Investigation, Approved | GMP-24, 25 | Several per order (product, components, labels) |
| 1354 | u_mes_plan_lineClearance | entity | transaction | LCL-<yyyymmdd>-<nnn> | In Progress, Passed, Failed, Verified | GMP-26 | Separate; checklist answers stay in `u_mes_qual_checkSheetResult` |
| 1355 | u_mes_maint_logbookEntry | entity | transaction | LOG-<equipment or area code>-<nnnnn> | Recorded, Reviewed | GMP-34 | Append-only event data; polymorphic equipment or area |
| 1356 | u_mes_maint_cleaningRecord | entity | transaction | CLN-<yyyymmdd>-<nnn> | In Progress, Completed, Verified, Expired, Rejected | GMP-27, 34, 35 | Separate event; equipment keeps the latest status |
| 1357 | u_mes_qual_environmentalMonitoringPoint | entity | master | EMP-<area code>-<nn> | Active, Inactive | GMP-37, 38 | Own master |
| 1358 | u_mes_qual_environmentalMonitoringResult | entity | transaction | EMR-<yyyymmdd>-<nnnn> | Recorded, Excursion Open, Excursion Closed, Invalidated | GMP-38 | Unbounded results; continuous values stay in `u_mes_perf_processReading` |
| 1359 | u_mes_matl_dispenseRecord | entity | transaction | DSP-<yyyymmdd>-<nnnn> | Dispensed, Verified, Issued, Returned, Rejected | GMP-11, 23 | Unbounded event data |
| 1360 | u_mes_qual_retentionSample | entity | transaction | RSM-<lot or serial number>-<nn> | Stored, Withdrawn, Destroyed | GMP-42 | Separate |
| 1361 | u_mes_qual_riskAssessment | entity | transaction | QRA-<yyyy>-<nnn> | In Preparation, In Review, Approved, Superseded | GMP-02, 43, 44 | Separate; polymorphic subject |
| 1362 | u_mes_qual_productQualityReview | entity | transaction | PQR-<item>-<yyyy>-<period> | In Preparation, In Review, Approved | GMP-46 | One per item and period |
| 1363 | u_mes_qual_productRecall | entity | transaction | RCL-<yyyy>-<nnn> | Initiated, In Progress, Completed, Closed, Cancelled | GMP-48 | Recalled lots as child |
| 1364 | u_mes_qual_productRecallLot | child | transaction | parent recordNo + -L<nnn> | - | GMP-48 | Child (carries quantities, so not a relationship) |
| 1365 | u_mes_qual_processValidation | entity | transaction | PVL-<yyyy>-<nnn> | Planned, In Execution, Completed, Approved, Rejected | GMP-32 | Separate |
| 1366 | u_mes_maint_equipmentQualification | entity | transaction | EQQ-<equipment code>-<phase>-<nn> | Planned, In Execution, Passed, Failed, Approved | GMP-33, 35 | Separate; equipment keeps the latest status |

Field-level detail of every collection: `03_design/<module folder>/specs/<collection name>.md`, `02_architecture/collection_keys.md` and the field lists. Source: `05_generator/gmp01.py`.

## 6. Keys added to existing collections

| Collection | Keys added (display pairs included) | Requirements |
|---|---|---|
| u_mes_mast_equipment | qualificationStatus, requalificationDueDate, cleanStatus, cleanHoldExpiresAt, lastCleaningRecordId, lastCleaningRecordName | GMP-33, 34, 35 |
| u_mes_mast_area | cleanlinessClass, environmentallyMonitored, gowningRequired | GMP-37 |
| u_mes_plan_lot | retestDate, batchReleaseId, batchReleaseName | GMP-22, 41 |
| u_mes_plan_productionOrder | batchRecordReviewId, batchRecordReviewName, lineClearanceId, lineClearanceName, yieldWithinLimits | GMP-20, 24, 26 |
| u_mes_qual_nonconformance | deviationClass, productImpactText, investigationDueDate, qaApprovedById, qaApprovedBy, qaApprovedAt, riskAssessmentId, riskAssessmentName | GMP-30 |
| u_mes_prod_engineeringChange | gmpImpact, validationRequired, regulatoryImpact, riskAssessmentId, riskAssessmentName | GMP-44 |
| u_mes_syst_electronicSignature | signatureManifestationText, signedRecordVersion, isFirstSigningInSession | GMP-06 |
| u_mes_syst_auditTrail | gxpRelevant, auditTrailReviewId, auditTrailReviewName | GMP-04, 05 |
| u_mes_mast_user | lastAccessReviewDate, passwordExpiryDate | GMP-07 |
| u_mes_mast_supplierSuppliedItem | qualificationStatus, qualifiedUntilDate | GMP-40 |
| u_mes_syst_recordPolicy | gxpRelevant | GMP-10 |

33 keys as specified (11 collections), 41 keys after the reference keys are expanded into their display pairs. The other 718 of the 759 new keys belong to the 23 new collections.

## 7. Allowed values added to existing lists

| Collection.key | Values added |
|---|---|
| u_mes_syst_interlockRule.ruleType | Line Clearance Check, Batch Release Check, Equipment Clean Status Check, Qualification Status Check, Dispense Tolerance Check |
| u_mes_matl_exposureTimer.timerType | Dirty Equipment Hold, Clean Equipment Hold, Process Hold Time |
| u_mes_qual_gaugeCalibration.calibrationType | Daily Performance Check |

Classification keys of the new collections are fixed enumerations (DATA-003 rule B), because the software branches on them or they are fixed by a standard (GAMP category, recall class, ISO cleanliness class, qualification phase, validation stage). Their values are in `04_reference_data/code_lists/enumeration_values.md`. The two new master lists that a plant maintains are collections of their own (rule A): computerised systems and environmental monitoring points.

## 8. Enforcement

Under data modeling standard section 12, each rule the application enforces has a configuration record and an evidence record:

| Rule | Configuration | Evidence |
|---|---|---|
| No order start without a verified line clearance | `u_mes_syst_interlockRule` (ruleType Line Clearance Check) | `u_mes_plan_interlockEvent`, `u_mes_plan_lineClearance` |
| No dispatch of a lot or order without release | ruleType Batch Release Check | `u_mes_plan_interlockEvent`, `u_mes_bmr_batchRelease` |
| No use of equipment that is dirty or past its clean hold time | ruleType Equipment Clean Status Check | `u_mes_plan_interlockEvent`, `u_mes_maint_cleaningRecord` |
| No use of equipment that is not qualified | ruleType Qualification Status Check | `u_mes_plan_interlockEvent`, `u_mes_maint_equipmentQualification` |
| No issue of a dispensed quantity outside tolerance | ruleType Dispense Tolerance Check | `u_mes_plan_interlockEvent`, `u_mes_matl_dispenseRecord` |
| Signature and reason for status changes of GMP records | `u_mes_syst_statusTransition` (requiresSignature, requiresReason), `u_mes_syst_statusTransitionRole` | `u_mes_syst_electronicSignature`, `u_mes_syst_auditTrail` |
| Edit, lock and retention of GMP records | `u_mes_syst_recordPolicy` (gxpRelevant) | `u_mes_syst_auditTrail` |

## 9. Sample data

Ten documents per new collection, written collection by collection in `05_generator/gmp01_samples.py`, in the caliper universe:

- **Batch record review and release.** PO-1000412 is reviewed by exception: a tool-life override and a hold are assessed, and the order is released for 474 calipers. Furnace charge L260915-HT-002 is conditionally released under DEV-2026-0007. PO-1000461 is returned for correction because three leak retests were entered manually without a second-person check.
- **Yield and reconciliation.** PO-1000461 has 3 units unaccounted, a yield of 96.63 percent against a lower limit of 98.00 percent, and is under investigation under NCR-2026-000139.
- **Line clearance.** Clearance LCL-20260922-001 fails because two labels of the previous order are found under the leak tester fixture. The repeat clearance is verified.
- **Cleaning.** The cleaning before the LH-to-RH changeover of the piston press is recorded. Its clean hold expired before the next use.
- **Environmental monitoring.** Illuminance at final inspection falls to 760 lux (an action-limit excursion). This links to the Environment Check interlock override of 24 September.
- **Recalls.** There is a Class I field action for seals from lot L260905-SEL-011, scoped by trace TRC-20260919-011.

## 10. Owner decision and implementation notes

Owner decision of 12 October 2026: analysis and implementation in this task (option "Analysis + implement"). The decisions taken under the approved-by-default rule are D047-D053 in `decision_log.md`.

Implementation:

1. `05_generator/gmp01.py` defines the 23 collections, the 33 keys and the allowed-value additions in the format of `ext_req01.py`. `ext_req01.py` appends them to its NEW, ADD and ENUM_ADD lists, so `flatten_model.py`, `spec_rules.py`, `gen_specs.py`, `gen_docs.py` and `gen_samples.py` pick them up unchanged. The catalogue entry of each new collection names its source set (GMP_Pharma_01) and uses the source concept prefix `gmp01:`.
2. `05_generator/gmp01_samples.py` holds the sample rules and is applied in `sample_rules.py` after `ext_req01_samples.py`.
3. Collection numbers continue from 1343. Existing numbers and `_id` values are unchanged (D042).
4. Key types were chosen so that every key name keeps one BSON type (D044). For example, `targetWeight` is used instead of `targetQuantity` (Int32 elsewhere), `releaseQuantity` instead of `releasedQuantity`, and `testCaseCount` / `testFailedCount` are shared by the system validation and equipment qualification collections.
5. Model version 2.7: 366 collections (198 entity, 85 child, 75 relationship, 8 value-list) and 8,142 keys.

## 11. Checks (12 October 2026)

| Check | Result |
|---|---|
| `flatten_model.py`: naming, references, display pairs, flatness, one BSON type per key name (D044) | 0 problems |
| `gen_specs.py` specification check | 0 findings (366 collections, 8,142 keys, 1,471 indexes) |
| `gen_samples.py` sample checks (19 checks, including referential integrity, display values, status values, date order and timeline) | 0 findings, 3,660 documents |
| Independent check of the 3,660 sample documents against the 366 JSON Schema validators (types, required keys, no extra keys, allowed values) | 0 problems |
| `schema_review_checklist.md` A1-A13, B1-B9, C1-C7 for the new collections and keys | Pass; see `08_validation/reports/specification_check.md` and `sample_data_validation.md` |
