"""Gamp universe (pharma): the 26 GMP-only collections rewritten to the Paracetamol 500 mg story. Merged by pharma_rules.py. D060-D065.
Dates, statuses and most reference positions follow gmp01_samples.py, so the timeline stays inside the production fortnight;
names, business numbers, quantities, texts and the references that carry product meaning are replaced here."""
import datetime, hashlib
import sample_universe as U
import ext_req01_samples as _X
import gmp01_samples as _GM
from pharma_rules import DT, D0, BATCH, LOTS

_poly = _X._poly
def _audited(f): return lambda env: (f(env), _GM._audit(env))
VAL = {}; REFIDX = {}; STATUSOF = {}; RECFMT = {}; PARENTIDX = {}; CTXOF = {}; POST = {}
TITLES_ADD = {}
def _tl(e, k, lst): VAL[(e, k)] = lst
def _r(e, k, lst): REFIDX[(e, k)] = lst
def _mname(ent): return lambda env: U.MASTER[ent][env["i"]].split("|")[1]
def _title(lst): return lambda env: lst[env["i"]]
N10 = [None] * 10

# ---------------------------------------------------------------- syst: computerised systems
E = "computerisedSystem"
VAL[(E, "name")] = _mname(E)
_tl(E, "description", ["Process orders, electronic batch records, dispensing, genealogy, batch record review, release, reconciliation and electronic signatures for all OSD lines",
    "Two-stage vacuum decay test of the hourly blister samples at -300 and -500 mbar, test programs, results and curves",
    "Capping programs, application torque per capping head and removal torque results",
    "Serial number generation, carton coding with batch number and expiry date, code verification and aggregation to shippers",
    "Main compression force, automatic weight control and tablet rejection on the rotary tablet press",
    "Transfer of process orders from ERP and of confirmations and goods movements to ERP",
    "Label templates and printing of dispense, status and shipper labels",
    "Collection and storage of process parameters from all equipment controllers",
    "Sample management, test results, specifications and certificates of analysis of the quality control laboratory",
    "Granulator recipe, impeller and chopper control and batch data (replaced by the new granulator PLC)"])
_r(E, "equipmentId", [None, 7, 6, 8, 4, None, None, None, None, 1])
_r(E, "processOwnerUserId", [6, 4, 4, 4, 4, 7, 7, 6, 3, 4])
_tl(E, "softwareVersion", ["2.7.0", "VLT-FW 4.2", "SC-CTRL 2.8", "SER-L3 6.4", "FE-CTRL 5.1.0", "IF 1.9", "LPS 6.2", "HIST 2.4", "LIMS 11.2", "S7-300 program 3.0"])

E = "systemValidation"
_SVT = ["MES release 2.7.0, review by exception, batch release and reconciliation functions", "Blister vacuum leak tester firmware 4.2 with -500 mbar test program",
    "Capper controller 2.8 with torque monitoring per capping head", "Serialisation line system 6.4, GS1 2D code with batch number and expiry",
    "Tablet press control system 5.1.0 with automatic weight control", "ERP interface 1.9, publication of goods movements", "Label printing server 6.2, dispense and status label templates",
    "Process data historian 2.4, initial validation", "MES patch 2.7.1, audit trail export", "Rapid mixer granulator PLC decommissioning and data archive"]
VAL[(E, "title")] = _title(_SVT); TITLES_ADD[E] = _SVT
_tl(E, "releaseVersion", ["2.7.0", "VLT-FW 4.2", "SC-CTRL 2.8", "SER-L3 6.4", "FE-CTRL 5.1.0", "IF 1.9", "LPS 6.2", "HIST 2.4", "2.7.1", "S7-300 program 3.0"])
_r(E, "engineeringChangeId", [None, 3, 6, 4, None, None, None, None, None, None])
_tl(E, "conclusionText", ["186 test cases executed; 3 failures in report layout corrected and retested; release fit for intended use",
    "Both test stages, limits and curve storage verified at -300 and -500 mbar; fit for intended use",
    "Torque window and rejection per capping head verified on 24 bottles including two challenge bottles; fit for intended use",
    "Code layout with batch number, expiry and serial verified on 31 cartons; all codes grade A; fit for intended use", None,
    "Order download and goods-movement publication verified on 37 messages; fit for intended use", "28 label templates verified against the approved artwork; fit for intended use",
    "Supplier test package reviewed and 19 site tests executed; fit for intended use", None, "Batch data archived and readable from the archive; program retired; decommissioning complete"])

_SYSC = ["MES-RJ1", "LKT-BLS-01", "CAP-BTL-01", "SER-L3", "CMP-01-T1", "ERP-IF-PH", "LBL-RJ1", "HIST-RJ1", "LIMS-QC1", "RMG-01-PLC"]
RECFMT["systemPeriodicReview"] = lambda i, j: "SPR-%s-2026-01" % _SYSC[i]
RECFMT["userAccessReview"] = lambda i, j: "UAR-%s-2026-02" % _SYSC[i]
_tl("systemPeriodicReview", "findingsText", ["Two report templates changed without change record; retrospective change records raised",
    "Local shared account found on the leak tester; replaced by personal badge login", "None", "Code grade below B after print head contamination on 24 September; covered by NCR-2026-000142",
    None, "None", "None", "None", None, "Program and batch data archived before retirement"])
_tl("auditTrailReview", "findingsText", ["Change part life override justified in the interlock event", "None", "Wet massing time limit change and one manual inlet air temperature entry justified",
    None, "Two hourly leak test results entered manually without second-person verification", "Two report template changes without change record",
    "Local shared account used for two logins on the leak tester", "None", "Print parameter changed during print head cleaning; change justified", "None"])
_tl("userAccessReviewLine", "comment", [None, None, "Administrator role no longer needed after go-live of release 2.7.0; validation engineer role kept",
    "Moved from granulation operator to packing operator on 1 September 2026", None, "Shared local account on the leak tester replaced by personal badge login", None, None, None, None])

# ---------------------------------------------------------------- bmr: batch record review, exceptions, release, reconciliation, batch record header
RECFMT["batchRecordReview"] = lambda i, j: "BRR-" + BATCH[i]
_r("batchRecordReview", "lotId", [None, None, 2, 0, None, None, None, None, None, None])
_tl("batchRecordReview", "operationsCount", [486, 212, 344, 298, 96, 0, 301, 190, 0, 0])
_tl("batchRecordReview", "returnReasonText", [None] * 7 + ["Two hourly leak test results entered manually without second-person verification; correct and re-sign", None, None])

E = "batchRecordReviewException"
POST[E] = _audited(_poly([("interlockEvent", 3), ("interlockEvent", 7), ("nonconformance", 4), ("nonconformance", 1), ("auditTrail", 1), ("operationExecution", 0),
    ("auditTrail", 0), ("nonconformance", 2), ("qualityHold", 0), ("nonconformance", 7)]))
_tl(E, "description", ["Capping chuck life limit overridden by the supervisor for the last 300 bottles until the planned chuck change",
    "Carton on quality hold blocked at serialisation and removed from the line",
    "Tablet weight drift on station 17 after lower punch wear; tablets since the last good check rejected under NCR-2026-000130",
    "Wet mass over-granulated after a binder pump fault; batch processed under deviation DEV-2026-0007",
    "Wet massing time limit edited during the batch; change checked against the approved master manufacturing record",
    "Inlet air temperature entered manually for 35 minutes during a sensor fault", "Granule loss on drying result entered three hours after the measurement",
    "Loss on drying 2.9 percent on granules of batch PCM5G26092; NCR-2026-000124 open", "Batch on hold after blister leak test failures",
    "Two hourly leak test results entered manually without second-person verification"])

E = "batchRelease"
RECFMT[E] = lambda i, j: ["BRL-PCM5G26091-S2", "BRL-PCM5G26091-S1", "BRL-PCM5F26091-P1", "BRL-PCM5F26091-P2", "BRL-PCM5B26091", "BRL-PCM5B26093", "BRL-PCM5G26092",
    "BRL-PCM5H26091", "BRL-PCM5B26092", "BRL-PCM5F26091-P1-R"][i]
_r(E, "lotId", [1, 0, 2, 3, None, None, None, None, None, 2])
_r(E, "productionOrderId", [3, 3, 2, 2, 0, 7, 6, 1, 4, 2])
_r(E, "itemId", [3, 3, 2, 2, 0, 0, 3, 1, 0, 2])
_r(E, "batchRecordReviewId", [3, 3, 2, 2, 0, 7, 6, 1, 4, 2])
_tl(E, "releaseQuantity", [150, 150, 236000, 240000, 4741, 1716, 296, 1532, 950, 4000])
_r(E, "unitOfMeasureId", [1, 1, 0, 0, 0, 0, 1, 0, 0, 0])
_tl(E, "decisionText", ["Released to blending under deviation DEV-2026-0007 (binder pump in manual mode); loss on drying and particle size within limits",
    "Granulation sub-lot released to blending after batch record review", "236,000 coated tablets released to packing; 4,000 tablets with twinning excluded",
    "Coating pan load 2 released to packing after weight gain and appearance check", "4,741 cartons certified for sale; certificate of analysis and batch record review complete",
    "Pending closure of NCR-2026-000139", "Pending QA review of the batch manufacturing record", "Batch still in packing", "Batch still in packing",
    "4,000 coated tablets with twinning rejected for destruction (NCR-2026-000133)"])

E = "yieldReconciliation"
RECFMT[E] = lambda i, j: ["YRC-PCM5B26091-01", "YRC-PCM5B26091-02", "YRC-PCM5B26091-03", "YRC-PCM5F26091-01", "YRC-PCM5G26091-01", "YRC-PCM5G26091-02", "YRC-PCM5G26092-01",
    "YRC-PCM5B26093-01", "YRC-PCM5B26093-02", "YRC-PCM5F26091-02"][i]
_r(E, "itemId", [0, 0, 2, 2, 3, 4, 3, 0, 0, 3])
_r(E, "unitOfMeasureId", [0, 0, 0, 0, 1, 1, 1, 0, 0, 1])
_YQ = [("4800", "4800", "4741", "22", "25", "12", "0", "98.77", "98.00", "100.00"), ("4800", "4900", "4741", "0", "47", "112", "0", "100.00", "100.00", "100.00"),
       ("480000", "480000", "474100", "2200", "2500", "1200", "0", "100.00", "99.50", "100.50"), ("480000", "480000", "476000", "4000", "0", "0", "0", "99.17", "98.00", "100.00"),
       ("300.000", "300.000", "296.400", "1.200", "0.900", "0.000", "1.500", "98.80", "97.00", "100.00"), ("250.000", "250.150", "249.250", "0.000", "0.250", "0.650", "0.000", "100.00", "99.50", "100.50"),
       ("300.000", "300.000", "295.800", "1.800", "0.900", "0.000", "1.500", "98.60", "97.00", "100.00"), ("2400", "1800", "1716", "36", "18", "0", "30", "95.33", "98.00", "100.00"),
       ("1800", "1900", "1716", "0", "36", "148", "0", "100.00", "100.00", "100.00"), ("288.000", "290.000", "285.600", "2.400", "0.500", "1.500", "0.000", "100.00", "99.50", "100.50")]
for _n, _k in enumerate(["theoreticalQuantity", "issuedQuantity", "outputQuantity", "rejectedQuantity", "destroyedQuantity", "returnedQuantity", "unaccountedQuantity", "yieldPct",
                         "lowerLimitPct", "upperLimitPct"]): VAL[(E, _k)] = [x[_n] for x in _YQ]

E = "batchManufacturingRecord"
RECFMT[E] = lambda i, j: "BMR-" + BATCH[i]
_r(E, "lotId", [None, None, 2, 0, None, None, None, None, None, None])
_tl(E, "plannedQuantity", [4800, 2400, 480000, 300, 4800, 480000, 300, 4800, 480000, 1200])
_tl(E, "checksumSha256", [hashlib.sha256(("BMR-" + BATCH[i] + "-export").encode()).hexdigest() if i in (0, 2, 3, 9) else None for i in range(10)])
_tl(E, "pageCount", [64, None, 52, 48, None, None, None, None, None, 6])

# ---------------------------------------------------------------- mmr: master manufacturing records
E = "masterManufacturingRecord"
VAL[(E, "title")] = _mname(E)
_r(E, "engineeringChangeId", [3, 8, None, 2, None, 1, 5, 6, 0, None])
_r(E, "processValidationId", [0, 0, 8, 6, None, 9, 4, None, None, None])
_tl(E, "changeReasonText", ["Blister foil supplier changed and leak test program revised (ECN-2026-0030)", "Shipper of 50 cartons for Medicura Healthcare (ECN-2026-0035)", None,
    "Coating weight gain target changed to 3.0 percent (ECN-2026-0029)", None, "Second source of microcrystalline cellulose PH 101 (ECN-2026-0028)",
    "Granulation end-point changed to impeller power (ECN-2026-0032)", "Cap torque window revised to 1.2-2.0 N.m (ECN-2026-0033)",
    "Compression force window aligned with the hardness limit 80-140 N (ECN-2026-0027)", None])
_tl(E, "standardBatchSize", [4800, 4800, 2400, 480000, 300, 4800, 300, 2400, 480000, 4800])
_tl(E, "theoreticalQuantity", ["4800", "4800", "2400", "480000", "300.000", "4800", "300.000", "2400", "480000", "4800"])
_r(E, "unitOfMeasureId", [0, 0, 0, 0, 1, 0, 1, 0, 0, 0])
_tl(E, "lowerLimitPct", ["98.00", "98.00", "98.00", "98.00", "97.00", "98.00", "97.00", "98.00", "98.00", "97.50"])
PARENTIDX["masterManufacturingRecordRecipe"] = [0, 0, 0, 2, 2, 3, 3, 4, 4, 4]
_r("masterManufacturingRecordRecipe", "recipeId", [7, 8, 9, 6, 9, 4, 5, 0, 1, 2])

# ---------------------------------------------------------------- plan: line clearance
E = "lineClearance"
_r(E, "lineId", [5, 4, 2, 1, 5, 1, 5, 5, 2, 2])
_r(E, "previousProductionOrderId", [None, None, None, None, 0, 3, 4, 4, 2, 2])
_tl(E, "clearanceType", ["Before Order Start", "Before Order Start", "Before Order Start", "Before Order Start", "Order Changeover", "Order Changeover", "Order Changeover",
    "Order Changeover", "Order Changeover", "Order Changeover"])
_tl(E, "failureText", [None] * 6 + ["Two printed cartons of batch PCM5B26092 found under the cartoner infeed guide", None, None, None])

# ---------------------------------------------------------------- maint: logbook, cleaning, equipment qualification
E = "logbookEntry"
RECFMT[E] = lambda i, j: ["LOG-BLS-01-P1-00412", "LOG-BLS-01-P1-00413", "LOG-BTL-01-K1-00214", "LOG-RMG-01-G1-00288", "LOG-RMG-01-G1-00289", "LOG-DSP-01-B1-00518",
    "LOG-BLS-01-P1-00414", "LOG-PPK-00096", "LOG-CMP-01-T1-00402", "LOG-SER-01-P1-00233"][i]
POST[E] = _audited(_poly([("equipment", 7), ("equipment", 7), ("equipment", 6), ("equipment", 1), ("equipment", 1), ("equipment", 0), ("equipment", 7), ("area", 4),
    ("equipment", 4), ("equipment", 8)]))
_r(E, "productionOrderId", [0, 4, 1, None, 3, None, None, None, None, None])
_r(E, "lineClearanceId", [None, 4, None, None, None, None, None, None, None, None])
_r(E, "cleaningRecordId", [None, None, None, 0, None, None, None, None, None, 6])
_tl(E, "entryText", ["Blister packing of batch PCM5B26091: 4,741 cartons good, 22 rejected", "Line clearance before batch PCM5B26092, verified by the supervisor",
    "Bottle filling and capping of batch PCM5H26091 started", "Granulator cleaned after batch PCM5G26091, rinse sample taken",
    "Wet granulation of sub-lot PCM5G26091-S1 for batch PCM5G26091", "Balance zero drift corrected and balance recalibrated (MWO-2026-000341)",
    "Periodic leak tester verification with the reference leaking blister at -300 and -500 mbar", "Weekly cleaning of the primary packing area, floor, walls and return air grills",
    "Compression cubicle idle on weekly off; dehumidifier kept on", "Print head of the serialisation unit cleaned after the code grade fell below B"])

E = "cleaningRecord"
_r(E, "equipmentId", [1, 2, 4, 4, 6, 7, 8, 9, 0, 5])
_r(E, "workCenterId", [1, 2, 4, 4, 6, 7, 8, 9, 0, 5])
_tl(E, "cleaningType", ["Major Cleaning", "Minor Cleaning", "Major Cleaning", "Product Changeover Cleaning", "Minor Cleaning", "Minor Cleaning", "Minor Cleaning", "Minor Cleaning",
    "Major Cleaning", "Product Changeover Cleaning"])
_r(E, "procedureControlledDocumentId", [1, 1, 1, 1, 3, 3, 3, 3, 9, 1])
_r(E, "previousProductionOrderId", [3, None, 2, None, None, 4, None, None, 6, 2])
_r(E, "previousItemId", [3, None, 2, None, None, 0, None, None, 3, 2])
_tl(E, "verificationMethod", ["Rinse Sample", "Visual Inspection", "Rinse Sample", "Swab Sample", "Visual Inspection", "Visual Inspection", "Visual Inspection", "Visual Inspection",
    "Visual Inspection", "Swab Sample"])

E = "equipmentQualification"
RECFMT[E] = lambda i, j: ["EQQ-BLS-01-P1-PQ-01", "EQQ-RMG-01-G1-OQ-02", "EQQ-RMG-01-G1-RQ-01", "EQQ-SER-01-P1-IQ-01", "EQQ-SER-01-P1-OQ-01", "EQQ-SER-01-P1-PQ-02",
    "EQQ-BTL-01-K1-RQ-01", "EQQ-CMP-01-T1-RQ-01", "EQQ-FBD-01-D1-RQ-01", "EQQ-COT-01-C1-OQ-01"][i]
_r(E, "equipmentId", [7, 1, 1, 8, 8, 8, 6, 4, 2, 5])
_r(E, "engineeringChangeId", [3, None, None, None, None, None, 6, None, None, None])

# ---------------------------------------------------------------- qual: environmental monitoring
E = "environmentalMonitoringPoint"
VAL[(E, "name")] = _mname(E)
_r(E, "areaId", [1, 1, 1, 3, 2, 4, 4, 6, 6, 1])
_r(E, "workCenterId", [0, 0, 0, 4, 1, None, None, None, None, 0])
_tl(E, "monitoredParameter", ["Airborne Particles 0.5 um", "Temperature", "Relative Humidity", "Differential Pressure", "Surface Microbial Count", "Relative Humidity", "Temperature",
    "Temperature", "Relative Humidity", "Airborne Particles 5.0 um"])
_tl(E, "parameterUnitText", ["particles per m3", "degC", "percent RH", "Pa", "CFU per plate", "percent RH", "degC", "degC", "percent RH", "particles per m3"])
_tl(E, "limitDirection", ["Upper", "Range", "Range", "Lower", "Upper", "Range", "Range", "Range", "Range", "Upper"])
_tl(E, "alertLimit", ["2800000", "24.0", "50.0", "12.0", "25", "50.0", "24.0", "31.5", "68.0", "25000"])
_tl(E, "actionLimit", ["3520000", "25.0", "55.0", "10.0", "50", "55.0", "25.0", "32.0", "70.0", "29300"])
_tl(E, "lowerActionLimit", [None, "18.0", "30.0", None, None, "30.0", "18.0", "28.0", "60.0", None])
_tl(E, "samplingFrequency", ["Weekly", "Continuous", "Continuous", "Every Shift", "Weekly", "Every Shift", "Every Shift", "Continuous", "Continuous", "Weekly"])
E = "environmentalMonitoringResult"
_tl(E, "measuredValue", ["1840000", "22.6", "46.0", "14.0", "32", "58.5", "23.1", "30.1", "70.6", "18400"])
_tl(E, "limitEvaluation", ["Within Limits", "Within Limits", "Within Limits", "Within Limits", "Alert Limit Exceeded", "Action Limit Exceeded", "Within Limits", "Within Limits",
    "Action Limit Exceeded", "Within Limits"])
_r(E, "gaugeId", N10)
_tl(E, "productImpactText", [None, None, None, None, "Alert only; area sanitised with the rotation disinfectant, no product impact",
    "Relative humidity above 55 percent for 25 minutes; blisters packed in that period tested for leaks and water content, all within limits", None, None,
    "Stability samples moved to the backup chamber; excursion assessed under the stability protocol", None])

# ---------------------------------------------------------------- matl: dispensing for the granulation batches
E = "dispenseRecord"
RECFMT[E] = lambda i, j: ["DSP-20260917-0011", "DSP-20260917-0012", "DSP-20260921-0006", "DSP-20260921-0007", "DSP-20260917-0013", "DSP-20260917-0014", "DSP-20260916-0021",
    "DSP-20260921-0008", "DSP-20260921-0009", "DSP-20260921-0010"][i]
_r(E, "productionOrderId", [3, 3, 6, 6, 3, 3, 2, 6, 6, 6])
_r(E, "itemId", [4, 5, 4, 4, 6, 7, 9, 5, 6, 5])
_r(E, "lotId", [4, 9, 4, 4, 6, 7, 8, 9, 6, 5])
_tl(E, "dispenseMethod", ["Gravimetric Weighing"] * 10)
_tl(E, "targetWeight", ["250.000", "27.500", "250.000", "250.000", "10.000", "10.000", "9.000", "27.500", "10.000", "27.500"])
_tl(E, "tareWeight", ["12.400", "2.300", "12.400", "12.400", "1.150", "1.150", "1.150", "2.300", "1.150", "2.300"])
_tl(E, "netWeight", ["250.150", "27.480", "251.600", "249.900", "10.020", "9.990", "9.010", "27.520", "10.010", "27.505"])
_tl(E, "grossWeight", ["262.550", "29.780", "264.000", "262.300", "11.170", "11.140", "10.160", "29.820", "11.160", "29.805"])
_tl(E, "pieceCount", N10)
_tl(E, "withinTolerance", [True, True, False, True, True, True, True, True, True, True])
_r(E, "balanceGaugeId", [0] * 10)
_r(E, "storageLocationId", [3] * 10)
_tl(E, "dispensedAt", [DT(9, 17, 6, 5), DT(9, 17, 6, 14), DT(9, 21, 7, 0), DT(9, 21, 7, 8), DT(9, 17, 6, 22), DT(9, 17, 6, 28), DT(9, 16, 21, 40), DT(9, 21, 7, 15), DT(9, 21, 7, 20),
    DT(9, 21, 7, 25)])
_tl(E, "verificationMethod", ["System Check", "System Check", "System Check", "System Check", "Second Person", "Second Person", "Second Person", "Second Person", "Second Person",
    "System Check"])
_r(E, "verifiedById", [9, 9, 9, 9, 4, 4, 4, 4, 4, None])
_tl(E, "verifiedAt", [DT(9, 17, 6, 5, 20), DT(9, 17, 6, 14, 20), DT(9, 21, 7, 0, 20), DT(9, 21, 7, 8, 20), DT(9, 17, 6, 26), DT(9, 17, 6, 32), DT(9, 16, 21, 45), DT(9, 21, 7, 19),
    DT(9, 21, 7, 24), None])

# ---------------------------------------------------------------- qual: retention and reserve samples
E = "retentionSample"
RECFMT[E] = lambda i, j: ["RSM-PCM5G26091-S1-01", "RSM-PCM5G26091-S2-01", "RSM-PCM5F26091-P1-01", "RSM-PCM5F26091-P2-01", "RSM-PCM5B26091-01", "RSM-PCM5B26091-02",
    "RSM-R260904-API-011-01", "RSM-R260912-MCC-002-01", "RSM-R260830-MCC-007-01", "RSM-R260901-SSG-022-01"][i]
_r(E, "itemId", [3, 3, 2, 2, 0, 0, 4, 5, 5, 7])
_r(E, "lotId", [0, 1, 2, 3, None, None, 4, 9, 5, 7])
_tl(E, "sampleType", ["Retention Sample", "Retention Sample", "Retention Sample", "Retention Sample", "Retention Sample", "Retention Sample", "Reserve Sample", "Reserve Sample",
    "Reserve Sample", "Reserve Sample"])
_tl(E, "sampleQuantity", [1, 1, 200, 200, 4, 4, 1, 1, 1, 1])
_r(E, "unitOfMeasureId", [1, 1, 0, 0, 0, 0, 1, 1, 1, 1])
_r(E, "storageLocationId", [6] * 10)
_tl(E, "withdrawalReason", [None] * 5 + ["Withdrawn for comparison testing against market complaint CMP-2026-0011", None, None,
    "Withdrawn for water content retest of the MCC lot on hold", "Destroyed after the container was found damaged at the annual reserve sample inspection"])

# ---------------------------------------------------------------- qual: quality risk management
E = "riskAssessment"
_RAT = ["MES release 2.7.0, validation risk assessment of GMP functions", "Blister leak tester firmware 4.2 and new test program",
    "Cap torque window 1.2-2.0 N.m with monitoring per capping head", "Loss on drying 2.9 percent on granules of batch PCM5G26092",
    "Blister leak test failures after the foil roll change, batch PCM5B26093", "Tablet press automatic weight control release 5.1.0",
    "Second source of microcrystalline cellulose PH 101", "Paracetamol 500 mg blister pack, product risk review 2026",
    "Paracetamol 500 mg blister pack, product risk review 2026 after the foil supplier change", "Rapid mixer granulator PLC retirement and data archive"]
VAL[(E, "title")] = _title(_RAT); TITLES_ADD[E] = _RAT
POST[E] = _audited(_poly([("computerisedSystem", 0), ("engineeringChange", 3), ("engineeringChange", 6), ("nonconformance", 2), ("nonconformance", 7), ("equipment", 4),
    ("engineeringChange", 1), ("item", 0), ("item", 0), ("computerisedSystem", 9)]))
_tl(E, "scopeText", ["New and changed functions of release 2.7.0: signatures, batch record review by exception, release, reconciliation, reports",
    "Firmware change and new test program at the blister vacuum leak tester, both test stages", "Torque monitoring per capping head and window 1.2-2.0 N.m on the bottle capper",
    "Use of one granulation batch with loss on drying 2.9 percent after re-drying", "Causes of the blister leak test failures after the foil roll change on batch PCM5B26093",
    "Release of automatic weight control 5.1.0 on the rotary tablet press", "Second source for microcrystalline cellulose PH 101",
    "All process steps of Paracetamol 500 mg blister packs", "All process steps of Paracetamol 500 mg blister packs after the foil supplier change",
    "Retirement of the granulator PLC and archiving of its batch data"])
_tl(E, "riskControlsText", ["Scripted testing of signature, release and reconciliation functions; unscripted testing of reports",
    "Reference leaking blister detected at both stages after installation; curve envelope review", "Challenge bottles with loose caps rejected at every head; torque trended by SPC",
    "Re-dry to loss on drying 1.0-2.5 percent; extended dissolution and assay testing of the batch", None, None, None,
    "Balance interlocks at dispensing, recipe-controlled granulation and drying end-points, checkweighing of every carton and leak testing of hourly samples",
    "As before, with a leak test at every foil roll start", "Data archived and read back before retirement"])

# ---------------------------------------------------------------- qual: product quality reviews
E = "productQualityReview"
RECFMT[E] = lambda i, j: ["PQR-FG-PCM500-B10-2026-Q2", "PQR-FG-PCM500-B10-2026-Q3", "PQR-FG-PCM500-H100-2026-Q2", "PQR-FG-PCM500-H100-2026-Q3", "PQR-BLK-PCM500-FCT-2026-Q2",
    "PQR-BLK-PCM500-FCT-2026-Q3", "PQR-BLK-PCM500-GRN-2026-Q2", "PQR-BLK-PCM500-GRN-2026-Q3", "PQR-RM-PCM-API-2026-H1", "PQR-RM-MCC-101-2026-H1"][i]
_r(E, "itemId", [0, 0, 1, 1, 2, 2, 3, 3, 4, 5])
for _k, _v in {"lotsProducedCount": [38, 36, 14, 13, 40, 38, 40, 39, 12, 18], "lotsReleasedCount": [37, 34, 14, 12, 40, 37, 39, 38, 12, 17],
               "lotsRejectedCount": [1, 0, 0, 0, 0, 1, 1, 0, 0, 1], "nonconformanceCount": [5, 7, 1, 2, 3, 4, 4, 5, 1, 3], "deviationPermitCount": [1, 2, 0, 0, 1, 1, 1, 1, 0, 0],
               "customerComplaintCount": [3, 6, 0, 1, 0, 0, 0, 0, 0, 1], "capaCount": [2, 4, 0, 0, 1, 2, 1, 2, 0, 1], "engineeringChangeCount": [2, 3, 1, 1, 1, 1, 1, 1, 0, 1],
               "productRecallCount": [1, 2, 0, 0, 0, 0, 0, 0, 0, 1]}.items(): _tl(E, _k, _v)
_tl(E, "processCapabilityText", ["Tablet weight Cpk 1.92; blister leak test pass rate 99.6 percent", None, "Cap removal torque Cpk 1.88", None,
    "Tablet weight Cpk 1.71; coating weight gain Cpk 1.41", None, "Loss on drying Cpk 1.52; blend uniformity RSD below 3 percent on all batches", None,
    "Assay of API lots 99.4-100.6 percent from supplier certificates", "Loss on drying of MCC Cpk 1.45 from supplier data"])
_tl(E, "conclusionText", ["Process in a state of control; no change to the control strategy", None, "Process in a state of control", None,
    "Process in a state of control; coating weight gain capability to be improved", None, "Granule moisture capability marginal; dryer airflow study brought forward", None,
    "Supplier process in a state of control", "High moisture of MCC lot R260830-MCC-007 traced to the supplier; supplier conditionally approved"])
_tl(E, "actionsText", ["None", None, "None", None, "Coating spray rate study PVL-2026-007", None, "Requalification of the fluid bed dryer", None, "None",
    "Second source qualification PVL-2026-010"])

# ---------------------------------------------------------------- qual: recalls
E = "productRecall"
_RCT = ["Recall of 120 cartons of batch PCM5B26091 with unreadable 2D code at Medicura Healthcare Kenya",
    "Market recall of batch PCM5B26088 after 650 mg strips were found in 500 mg cartons", "Recall of bottles of batch PCM5H26091 with loose caps from hospital stores",
    "Recall of cartons with a foreign particle on the tablet surface from Arogya Distributors", "Recall of blister packs made from granules with high loss on drying",
    "Recall of cartons with smudged expiry print after transit", "Market recall of blister packs with empty pockets, batch PCM5B26087",
    "Recall of cartons with an expiry date mismatch between carton and blister", "Recall of cartons without leaflet from institutional supply",
    "Recall of shippers with short quantity at the Kenya importer"]
VAL[(E, "title")] = _title(_RCT); TITLES_ADD[E] = _RCT
_tl(E, "recallScope", ["Distributor", "Field", "Distributor", "Distributor", "Distributor", "Distributor", "Field", "Distributor", "Distributor", "Distributor"])
_tl(E, "reasonText", ["2D code not readable at the importer scanner", "Product mix-up: 650 mg strips packed in 500 mg cartons", "Bottle caps found loose at the hospital store",
    "Foreign particle on the tablet surface reported by a pharmacist", "Granules with loss on drying 2.9 percent used before the deviation was closed",
    "Expiry date smudged on cartons after transit in a wet truck", "Empty pockets found in blister strips by patients", "Expiry date on the carton differs from the blister",
    "Leaflet missing in cartons at the institutional store", "Shippers with 48 instead of 50 cartons at the Kenya importer"])
_r(E, "customerId", [4, 0, 3, 1, 0, 0, 0, 0, 7, 4])
_tl(E, "quantityShipped", [120, 4800, 2400, 4800, 0, 0, 4800, 3600, 1200, 500])
_tl(E, "quantityRecovered", [120, 4310, 2380, 4790, 0, 0, 0, 2900, 1200, 500])
E = "productRecallLot"
_r(E, "lotId", [3, 2, 3, 2, 3, 0, 2, 3, 2, 3])
_tl(E, "quantityShipped", [120, 2400, 2400, 2400, 4800, 0, 4800, 3600, 1200, 500])
_tl(E, "quantityRecovered", [120, 2155, 2155, 2380, 4790, 0, 0, 2900, 1200, 500])

# ---------------------------------------------------------------- qual: process validation
E = "processValidation"
_PVT = ["Paracetamol 500 mg tablets, process performance qualification, three batches", "Paracetamol 500 mg tablets, continued process verification, third quarter 2026",
    "Bottle capping torque window 1.2-2.0 N.m, process qualification", "Blister vacuum leak test at -500 mbar, process qualification",
    "Wet granulation end-point by impeller power, process design study", "Fluid bed drying after air handling unit repair, process qualification",
    "Film coating weight gain 2.5-3.5 percent, process qualification", "Compression and coating, continued process verification, third quarter 2026",
    "Paracetamol 500 mg bottle pack, process qualification", "Microcrystalline cellulose second source, process qualification"]
VAL[(E, "title")] = _title(_PVT); TITLES_ADD[E] = _PVT
_r(E, "itemId", [0, 0, 1, 0, 3, 3, 2, 2, 1, 3])
_r(E, "lineId", [5, 5, 4, 5, 1, 1, 3, 2, 4, 1])
_r(E, "engineeringChangeId", [None, None, 6, 3, 5, None, 2, None, None, 1])
_tl(E, "acceptanceCriteriaText", ["Assay 95.0-105.0 percent, dissolution not less than 80 percent in 30 minutes and content uniformity acceptance value not more than 15 on three batches",
    "Monthly Cpk >= 1.33 on all critical quality attributes", "Cpk >= 1.67 on cap removal torque; challenge bottle rejected at every head",
    "Reference leaking blister detected in every check; no leaking pocket passed", "Granule bulk density 0.45-0.55 g/ml and loss on drying 1.0-2.5 percent on three batches",
    "Loss on drying 1.0-2.5 percent on three batches; inlet air temperature 60 +/- 5 degC", "Cpk >= 1.33 on coating weight gain 2.5-3.5 percent",
    "Monthly Cpk >= 1.33 on tablet weight and hardness", "Cpk >= 1.67 on removal torque; induction seal intact on three batches",
    "Blend uniformity RSD not more than 5 percent and dissolution within limits on three batches"])
_tl(E, "resultText", ["Assay 99.1-100.4 percent, dissolution 92-97 percent, acceptance value 3.2-5.1; criteria met", None, "Removal torque Cpk 1.84; criteria met",
    "Reference leak detected in all 36 checks; criteria met", "Bulk density 0.58 g/ml on two batches; power end-point not adopted", None, "Weight gain Cpk 1.52; criteria met", None,
    "Removal torque Cpk 1.88, induction seal intact on all samples; criteria met", None])
