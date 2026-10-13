"""Sample-data rules for the collections and keys added by GMP_Pharma_01 (D047-D053).
Merged into sample_rules.py by apply(), after ext_req01_samples; same universe, same IDs and names.
Index conventions: process rows 0-9 = OP010 casting ... OP100 final inspection; equipment, work centers and lines as in sample_universe.PROC.
Users: 0 Sunil Jadhav, 1 Kavita Bhosale, 2 Deepak Gaikwad (operators), 3 Anita Kulkarni (quality), 4 Rajesh Patil (supervisor),
5 Imran Shaikh (maintenance), 6 Meera Deshpande (manager), 7 Vikram Pawar (stores), 8 Sneha Joshi (process engineering and MES), 9 MES System.
Production orders: 0 PO-1000412 LH, 1 PO-1000419 RH, 2 PO-1000426 body, 3 PO-1000433 casting, 4 PO-1000440 LH, 5 PO-1000447 body,
6 PO-1000454 casting, 7 PO-1000461 LH (on hold), 8 PO-1000468 body, 9 PO-1000475 LH (cancelled).
Lots: 0 L260915-GDC-014, 1 L260915-HT-002, 2 L260916-CNC-007, 3 L260917-ANO-001, 4 piston, 5 seal SEL-011 (hold), 6 boot, 7 bleed screw, 8 ingot, 9 seal SEL-002."""
import datetime
import ext_req01_samples as _X

def DT(m, d, h=0, mi=0, s=0, y=2026): return datetime.datetime(y, m, d, h, mi, s)
def D0(y, m, d): return datetime.datetime(y, m, d)
def M(minutes): return datetime.timedelta(minutes=minutes)
cur = _X.cur
raw = _X.raw
_poly = _X._poly

MASTER_ADD = {
"computerisedSystem": """CSY-MES-PN1|Manufacturing execution system, Chakan plant
CSY-LKT-01-T1|Pressure leak tester 1 controller
CSY-TRQ-01-N1|DC nutrunner station 1 controller
CSY-LSR-01-L1|Laser marker 1 marking software
CSY-FIN-01-V1|Final inspection vision system
CSY-ERP-IF|ERP interface for orders and goods movements
CSY-LBL-PN1|Label printing server, Chakan plant
CSY-HIST-PN1|Process data historian, Chakan plant
CSY-LAB-QL|Quality laboratory measurement system
CSY-ANO-01-PLC|Anodising line PLC (legacy)""",
"environmentalMonitoringPoint": """EMP-ASY-01|Assembly clean area, airborne particles 0.5 um
EMP-ASY-02|Assembly clean area, temperature
EMP-ASY-03|Assembly clean area, relative humidity
EMP-ASY-04|Assembly clean area to machining, differential pressure
EMP-WSH-01|Washed caliper bodies, surface particle count
EMP-FIP-01|Final inspection cell, illuminance
EMP-FIP-02|Final inspection cell, temperature
EMP-QL-01|Quality laboratory, CMM room temperature
EMP-QL-02|Quality laboratory, CMM room relative humidity
EMP-ASY-05|Assembly clean area, airborne particles 5.0 um""",
}

TITLES_ADD = {
"systemValidation": """MES release 2.7.0, batch record review, release and reconciliation functions
Leak tester 1 firmware 5.12 with 160 bar booster
Nutrunner controller 3.4.2 with angle monitoring
Laser marking software 8.1, plant code in layout
Final inspection vision system 4.3.1 with boot classifier 1.3
ERP interface 1.9, publication of goods movements
Label printing server 6.2, customer label templates
Process data historian 2.4, initial validation
MES patch 2.7.1, audit trail export
Anodising line PLC decommissioning and data archive""",
"riskAssessment": """MES release 2.7.0, validation risk assessment of GMP functions
Leak tester firmware 5.12 and 160 bar booster
Nutrunner angle monitoring and torque window 14 +/- 2 N.m
Hardness below 85 HBW on furnace charge HT-260915-02
Leak test failures at 140 bar stage, PO-1000461
Final inspection vision station, boot classifier release
Piston seal second source, EPDM grade E70
Front caliper LH, product risk review 2026
Front caliper LH, product risk review 2026 after torque window change
Anodising line PLC retirement and data archive""",
"productRecall": """Containment of 12 calipers with unreadable 2D code at Sahyadri Motors Exports
Field action on calipers with piston seals from lot L260905-SEL-011
Containment of calipers with loose bleed screws at Deccan Motor Company
Containment of calipers for metallic particles in brake fluid at Konkan Automotive
Recall of calipers from casting lot L260915-GDC-014, shrinkage porosity
Containment of calipers with white corrosion spots after transit
Field action on calipers with piston not retracting
Containment of calipers for seepage at piston seal, zero-kilometre vehicle
Containment of calipers for body deflection above limit
Containment of calipers with missing bleed screw cap""",
"processValidation": """Front caliper LH, assembly line 1, process qualification
Front caliper LH, continued process verification, third quarter 2026
Bleed screw torque window 14 +/- 2 N.m, process qualification
Leak test 140 bar stage, process qualification
Caliper body casting LH, die 2 gate geometry, process design study
T6 heat treatment after furnace zone 2 repair, process qualification
Anodising thickness window 8-16 micrometres, process qualification
Caliper body machining line 1, continued process verification, third quarter 2026
Front caliper RH, assembly line 1, process qualification
Piston seal second source EPDM E70, process qualification""",
}

RECFMT = {}
RECFMT["systemValidation"] = lambda i, j: "CSV-2026-%03d" % (11 + i)
_SYSC = ["MES-PN1", "LKT-01-T1", "TRQ-01-N1", "LSR-01-L1", "FIN-01-V1", "ERP-IF", "LBL-PN1", "HIST-PN1", "LAB-QL", "ANO-01-PLC"]
RECFMT["systemPeriodicReview"] = lambda i, j: "SPR-%s-2026-01" % _SYSC[i]
RECFMT["auditTrailReview"] = lambda i, j: ["ATR-20260916-001", "ATR-20260917-002", "ATR-20260918-003", "ATR-20260922-004", "ATR-20260923-005",
    "ATR-20260918-006", "ATR-20260919-007", "ATR-20260921-008", "ATR-20260924-009", "ATR-20260924-010"][i]
RECFMT["userAccessReview"] = lambda i, j: "UAR-%s-2026-02" % _SYSC[i]
_PO = ["PO-1000412", "PO-1000419", "PO-1000426", "PO-1000433", "PO-1000440", "PO-1000447", "PO-1000454", "PO-1000461", "PO-1000468", "PO-1000475"]
RECFMT["batchRecordReview"] = lambda i, j: "BRR-" + _PO[i]
RECFMT["batchRelease"] = lambda i, j: ["BRL-L260915-HT-002", "BRL-L260915-GDC-014", "BRL-L260916-CNC-007", "BRL-L260917-ANO-001", "BRL-PO-1000412",
    "BRL-PO-1000461", "BRL-PO-1000454", "BRL-PO-1000419", "BRL-PO-1000440", "BRL-L260916-CNC-007-R"][i]
RECFMT["yieldReconciliation"] = lambda i, j: ["YRC-PO-1000412-01", "YRC-PO-1000412-02", "YRC-PO-1000412-03", "YRC-PO-1000426-01", "YRC-PO-1000433-01",
    "YRC-PO-1000433-02", "YRC-PO-1000454-01", "YRC-PO-1000461-01", "YRC-PO-1000461-02", "YRC-PO-1000426-02"][i]
RECFMT["lineClearance"] = lambda i, j: ["LCL-20260915-001", "LCL-20260915-002", "LCL-20260916-001", "LCL-20260917-001", "LCL-20260918-001",
    "LCL-20260921-001", "LCL-20260922-001", "LCL-20260922-002", "LCL-20260924-001", "LCL-20260919-001"][i]
RECFMT["logbookEntry"] = lambda i, j: ["LOG-ASY-01-P1-00412", "LOG-ASY-01-P1-00413", "LOG-ASY-01-P1-00414", "LOG-WSH-01-W1-00288", "LOG-GDC-01-M1-00517",
    "LOG-GDC-01-M1-00518", "LOG-LKT-01-T1-00351", "LOG-ASY-00096", "LOG-ANO-01-L1-00402", "LOG-LSR-01-L1-00233"][i]
RECFMT["cleaningRecord"] = lambda i, j: ["CLN-20260915-001", "CLN-20260917-001", "CLN-20260919-001", "CLN-20260918-001", "CLN-20260921-001",
    "CLN-20260922-001", "CLN-20260924-001", "CLN-20260924-002", "CLN-20260921-002", "CLN-20260916-001"][i]
RECFMT["environmentalMonitoringResult"] = lambda i, j: ["EMR-20260915-0004", "EMR-20260915-0006", "EMR-20260915-0011", "EMR-20260916-0002", "EMR-20260917-0005",
    "EMR-20260924-0003", "EMR-20260922-0008", "EMR-20260918-0001", "EMR-20260921-0001", "EMR-20260915-0005"][i]
RECFMT["dispenseRecord"] = lambda i, j: ["DSP-20260917-0011", "DSP-20260917-0014", "DSP-20260921-0006", "DSP-20260921-0007", "DSP-20260915-0003",
    "DSP-20260915-0004", "DSP-20260915-0005", "DSP-20260922-0009", "DSP-20260918-0008", "DSP-20260915-0012"][i]
RECFMT["retentionSample"] = lambda i, j: ["RSM-L260915-GDC-014-01", "RSM-L260915-HT-002-01", "RSM-L260916-CNC-007-01", "RSM-L260917-ANO-001-01", "RSM-VB26258A00184",
    "RSM-VB26258A00197", "RSM-L260905-PST-007-01", "RSM-L260912-SEL-002-01", "RSM-L260905-SEL-011-01", "RSM-L260901-BLS-022-01"][i]
RECFMT["riskAssessment"] = lambda i, j: "QRA-2026-%03d" % (21 + i)
RECFMT["productQualityReview"] = lambda i, j: ["PQR-5110-10-0100-2026-Q2", "PQR-5110-10-0100-2026-Q3", "PQR-5110-10-0200-2026-Q2", "PQR-5110-10-0200-2026-Q3",
    "PQR-5110-20-0110-2026-Q2", "PQR-5110-20-0110-2026-Q3", "PQR-5110-20-0105-2026-Q2", "PQR-5110-20-0105-2026-Q3", "PQR-5110-30-0010-2026-H1", "PQR-5110-30-0020-2026-H1"][i]
RECFMT["productRecall"] = lambda i, j: "RCL-2026-%03d" % (1 + i)
RECFMT["processValidation"] = lambda i, j: "PVL-2026-%03d" % (1 + i)
RECFMT["equipmentQualification"] = lambda i, j: ["EQQ-LKT-01-T1-PQ-01", "EQQ-HT-01-F1-OQ-02", "EQQ-HT-01-F1-RQ-01", "EQQ-FIN-01-V1-IQ-01", "EQQ-FIN-01-V1-OQ-01",
    "EQQ-FIN-01-V1-PQ-02", "EQQ-TRQ-01-N1-RQ-01", "EQQ-ASY-01-P1-RQ-01", "EQQ-GDC-01-M1-RQ-01", "EQQ-ANO-01-L1-OQ-01"][i]

STATUSOF = {
 "computerisedSystem": ["Validated", "Validated", "Validated", "Validated", "In Validation", "Validated", "Validated", "Validated", "Validated", "Retired"],
 "systemValidation": ["Approved", "Approved", "Approved", "Approved", "In Execution", "Approved", "Approved", "Approved", "Planned", "Approved"],
 "systemPeriodicReview": ["Approved", "Approved", "Completed", "Approved", "In Review", "Approved", "Completed", "Approved", "Planned", "Approved"],
 "auditTrailReview": ["Completed", "Completed", "Completed", "In Review", "Escalated", "Completed", "Completed", "Completed", "Completed", "Completed"],
 "userAccessReview": ["Completed", "Completed", "Completed", "Completed", "In Review", "Completed", "Completed", "Completed", "Open", "Completed"],
 "batchRecordReview": ["Approved", "Open", "Approved", "Approved", "Open", "Open", "Under Review", "Returned For Correction", "Open", "Approved"],
 "batchRelease": ["Conditionally Released", "Released", "Released", "Released", "Released", "Pending", "Pending", "Pending", "Pending", "Rejected"],
 "yieldReconciliation": ["Approved", "Approved", "Approved", "Approved", "Approved", "Approved", "Calculated", "Under Investigation", "Calculated", "Approved"],
 "lineClearance": ["Verified", "Verified", "Verified", "Verified", "Verified", "Verified", "Failed", "Verified", "In Progress", "Passed"],
 "logbookEntry": ["Reviewed", "Reviewed", "Recorded", "Reviewed", "Reviewed", "Reviewed", "Reviewed", "Reviewed", "Reviewed", "Recorded"],
 "cleaningRecord": ["Verified", "Verified", "Verified", "Verified", "Verified", "Verified", "Verified", "In Progress", "Completed", "Expired"],
 "environmentalMonitoringPoint": ["Active"] * 10,
 "environmentalMonitoringResult": ["Recorded", "Recorded", "Recorded", "Recorded", "Recorded", "Excursion Closed", "Recorded", "Recorded", "Excursion Open", "Recorded"],
 "dispenseRecord": ["Issued", "Issued", "Rejected", "Issued", "Issued", "Issued", "Issued", "Returned", "Issued", "Rejected"],
 "retentionSample": ["Stored", "Stored", "Stored", "Stored", "Stored", "Withdrawn", "Stored", "Stored", "Withdrawn", "Destroyed"],
 "riskAssessment": ["Approved", "Approved", "Approved", "Approved", "In Review", "In Preparation", "In Review", "Superseded", "Approved", "Approved"],
 "productQualityReview": ["Approved", "In Preparation", "Approved", "In Preparation", "Approved", "In Preparation", "Approved", "In Review", "Approved", "Approved"],
 "productRecall": ["Closed", "In Progress", "Completed", "Closed", "Cancelled", "Cancelled", "Initiated", "In Progress", "Completed", "Completed"],
 "processValidation": ["Approved", "In Execution", "Completed", "Approved", "Rejected", "Planned", "Approved", "In Execution", "Approved", "In Execution"],
 "equipmentQualification": ["Approved", "In Execution", "Planned", "Approved", "Approved", "Failed", "Approved", "Approved", "Approved", "Approved"],
}

PARENTIDX = {
 "userAccessReviewLine": [0, 0, 0, 0, 1, 1, 2, 3, 5, 6],
 "batchRecordReviewException": [0, 0, 2, 3, 3, 3, 6, 6, 7, 7],
 "productRecallLot": [0, 1, 1, 2, 3, 4, 6, 7, 8, 9],
}
REFIDX = {}
VAL = {}
POST = {}
CTXOF = {}

def _tl(e, k, lst): VAL[(e, k)] = lst
def _r(e, k, lst): REFIDX[(e, k)] = lst
N10 = [None] * 10

# ---------------------------------------------------------------- syst: computerised systems
E = "computerisedSystem"
VAL[(E, "name")] = lambda env: MASTER_ADD["computerisedSystem"].split("\n")[env["i"]].split("|")[1]
_tl(E, "description", ["Production orders, operation executions, genealogy, batch record review, release, reconciliation and electronic signatures for all lines",
    "Two-stage pressure decay test at 5 bar and 140 bar, test programs, results and curves",
    "Tightening programs, torque and angle results and curves for bleed screw and guide pin bolts",
    "Serial number and 2D code layouts, marking parameters and code grading",
    "Image capture and classification of dust boot seating and bleed screw cap presence",
    "Transfer of production orders from ERP and of confirmations and goods movements to ERP",
    "Label templates and printing of container, shipping and hold labels",
    "Collection and storage of process parameters from all equipment controllers",
    "Hardness, coordinate measuring machine and coating thickness results of the quality laboratory",
    "Anodising bath, rectifier and rack sequence control (replaced by the new rectifier controller)"])
_tl(E, "systemCategory", ["Manufacturing Execution System", "Equipment Controller", "Equipment Controller", "Equipment Controller", "Equipment Controller",
    "ERP Interface", "Label Printing", "Data Historian", "Laboratory System", "Equipment Controller"])
_tl(E, "gampCategory", ["Category 4", "Category 4", "Category 4", "Category 4", "Category 4", "Category 4", "Category 4", "Category 4", "Category 4", "Category 5"])
_tl(E, "gxpImpact", ["Direct", "Direct", "Direct", "Direct", "Direct", "Indirect", "Direct", "Indirect", "Direct", "Direct"])
_tl(E, "dataCriticality", ["High", "High", "High", "Medium", "High", "Medium", "Medium", "Medium", "High", "Medium"])
_tl(E, "holdsElectronicRecords", [True] * 10)
_tl(E, "usesElectronicSignatures", [True, False, False, False, False, False, False, False, True, False])
_r(E, "systemOwnerUserId", [8, 5, 5, 5, 8, 8, 8, 8, 3, 5])
_r(E, "processOwnerUserId", [6, 4, 4, 4, 3, 7, 7, 6, 3, 4])
_r(E, "supplierId", N10)
_r(E, "equipmentId", [None, 7, 6, 8, 9, None, None, None, None, 4])
_tl(E, "softwareVersion", ["2.7.0", "LT-FW 5.12", "NR-CTRL 3.4.2", "LMS 8.1", "VIS 4.3.0", "IF 1.9", "LPS 6.2", "HIST 2.4", "QLAB 3.0", "S7-300 program 2.1"])
_tl(E, "hostingModel", ["Private Cloud", "Embedded", "Embedded", "Embedded", "Embedded", "Private Cloud", "On Premise", "On Premise", "On Premise", "Embedded"])
_tl(E, "lastValidatedDate", [D0(2026, 9, 5), D0(2026, 6, 18), D0(2026, 5, 20), D0(2026, 7, 2), D0(2026, 4, 22), D0(2026, 8, 12), D0(2026, 6, 30), D0(2026, 5, 11), D0(2026, 4, 28), D0(2026, 4, 15)])
_tl(E, "periodicReviewIntervalMonths", [12] * 10)
_tl(E, "nextPeriodicReviewDate", [D0(2027, 9, 15), D0(2027, 9, 15), D0(2027, 9, 15), D0(2027, 9, 15), D0(2027, 4, 22), D0(2027, 9, 15), D0(2027, 9, 15), D0(2027, 9, 15), D0(2027, 4, 28), None])

E = "systemValidation"
VAL[(E, "title")] = lambda env: TITLES_ADD["systemValidation"].split("\n")[env["i"]]
_r(E, "computerisedSystemId", [0, 1, 2, 3, 4, 5, 6, 7, 0, 9])
_tl(E, "validationType", ["Change Revalidation", "Change Revalidation", "Change Revalidation", "Change Revalidation", "Change Revalidation",
    "Change Revalidation", "Change Revalidation", "Initial Validation", "Change Revalidation", "Decommissioning"])
_tl(E, "assuranceApproach", ["Scripted Testing", "Scripted Testing", "Unscripted Testing", "Scripted Testing", "Scripted Testing",
    "Unscripted Testing", "Scripted Testing", "Supplier Assurance", "Ad Hoc Testing", "Scripted Testing"])
_tl(E, "releaseVersion", ["2.7.0", "LT-FW 5.12", "NR-CTRL 3.4.2", "LMS 8.1", "VIS 4.3.1", "IF 1.9", "LPS 6.2", "HIST 2.4", "2.7.1", "S7-300 program 2.1"])
_r(E, "engineeringChangeId", [None, 6, 0, 4, None, None, None, None, None, None])
_r(E, "riskAssessmentId", [0, 1, 2, None, 5, None, None, None, None, 9])
_r(E, "protocolControlledDocumentId", N10)
_r(E, "reportControlledDocumentId", N10)
_tl(E, "testCaseCount", [186, 42, 24, 31, 58, 37, 28, 19, 0, 12])
_tl(E, "testFailedCount", [3, 0, 1, 0, 4, 0, 0, 0, 0, 0])
_tl(E, "openDeviationCount", [0, 0, 0, 0, 2, 0, 0, 0, 0, 0])
_tl(E, "plannedStartDate", [D0(2026, 8, 17), D0(2026, 6, 8), D0(2026, 5, 11), D0(2026, 6, 22), D0(2026, 9, 14), D0(2026, 8, 3), D0(2026, 6, 22), D0(2026, 4, 27), D0(2026, 9, 25), D0(2026, 4, 13)])
_tl(E, "startedAt", [DT(8, 18, 9, 0), DT(6, 9, 10, 0), DT(5, 12, 9, 30), DT(6, 23, 10, 0), DT(9, 15, 10, 0), DT(8, 4, 9, 0), DT(6, 23, 14, 0), DT(4, 28, 9, 0), None, DT(4, 13, 9, 0)])
_tl(E, "completedAt", [DT(9, 3, 18, 0), DT(6, 16, 17, 0), DT(5, 18, 16, 0), DT(6, 30, 17, 30), None, DT(8, 10, 18, 0), DT(6, 29, 16, 0), DT(5, 8, 17, 0), None, DT(4, 14, 16, 0)])
_r(E, "approvedById", [3, 3, 3, 3, None, 3, 3, 3, None, 3])
_tl(E, "approvedAt", [DT(9, 5, 11, 0), DT(6, 18, 10, 30), DT(5, 20, 11, 0), DT(7, 2, 10, 0), None, DT(8, 12, 11, 0), DT(6, 30, 15, 0), DT(5, 11, 10, 0), None, DT(4, 15, 12, 0)])
_r(E, "electronicSignatureId", N10)
_tl(E, "conclusionText", ["186 test cases executed; 3 failures in report layout corrected and retested; release fit for intended use",
    "Both test stages, limits and curve storage verified at 5 bar and 140 bar; fit for intended use",
    "Angle window and torque window verified on 24 rundowns including two forced failures; fit for intended use",
    "Layout with plant code verified on 31 parts; all codes grade A; fit for intended use", None,
    "Order download and goods-movement publication verified on 37 messages; fit for intended use",
    "28 customer label templates verified against customer specification SM-ES-3501; fit for intended use",
    "Supplier test package reviewed and 19 site tests executed; fit for intended use", None,
    "Data archived and readable from the archive; program retired; decommissioning complete"])

E = "systemPeriodicReview"
_r(E, "computerisedSystemId", list(range(10)))
_tl(E, "reviewPeriodFromDate", [D0(2026, 4, 1)] * 9 + [D0(2026, 4, 1)])
_tl(E, "reviewPeriodToDate", [D0(2026, 9, 15)] * 8 + [D0(2026, 9, 30), D0(2026, 4, 14)])
_tl(E, "changesReviewedCount", [6, 2, 1, 1, 2, 1, 1, 1, 0, 1])
_tl(E, "incidentsReviewedCount", [4, 1, 0, 2, 3, 1, 0, 1, 0, 0])
_tl(E, "deviationsReviewedCount", [2, 1, 1, 1, 1, 0, 0, 0, 0, 0])
_tl(E, "auditTrailReviewed", [True, True, True, True, False, True, True, True, False, True])
_tl(E, "accessReviewed", [True, True, True, True, False, True, True, True, False, True])
_tl(E, "backupRestoreVerified", [True, True, True, True, False, True, True, True, False, True])
_tl(E, "validatedStateConfirmed", [True, True, True, True, None, True, True, True, None, True])
_tl(E, "findingsText", ["Two report templates changed without change record; retrospective change records raised",
    "Local shared account found on tester; replaced by personal badge login", "None", "Code grading below A after lens contamination on 24 September; covered by NCR-2026-000142",
    None, "None", "None", "None", None, "Program and data archived before retirement"])
_r(E, "reviewedById", [8, 5, 5, 5, 8, 8, 8, 8, 3, 5])
_tl(E, "reviewedAt", [DT(9, 18, 16, 0), DT(9, 19, 11, 0), DT(9, 21, 15, 0), DT(9, 21, 16, 30), None, DT(9, 22, 12, 0), DT(9, 22, 15, 0), DT(9, 23, 11, 0), None, DT(4, 14, 17, 0)])
_r(E, "approvedById", [3, 3, None, 3, None, 3, None, 3, None, 3])
_tl(E, "approvedAt", [DT(9, 21, 10, 0), DT(9, 21, 11, 0), None, DT(9, 22, 10, 0), None, DT(9, 23, 10, 0), None, DT(9, 24, 10, 0), None, DT(4, 15, 11, 0)])
_tl(E, "nextReviewDate", [D0(2027, 9, 15), D0(2027, 9, 15), D0(2027, 9, 15), D0(2027, 9, 15), D0(2027, 4, 22), D0(2027, 9, 15), D0(2027, 9, 15), D0(2027, 9, 15), D0(2027, 4, 28), D0(2026, 4, 15)])

E = "auditTrailReview"
_tl(E, "reviewType", ["Batch Record Review", "Batch Record Review", "Batch Record Review", "Batch Record Review", "For Cause",
    "Periodic System Review", "Periodic System Review", "Periodic System Review", "For Cause", "Batch Record Review"])
_r(E, "computerisedSystemId", [0, 0, 0, 0, 0, 0, 1, 3, 3, 0])
POST[E] = _poly([("productionOrder", 0), ("productionOrder", 2), ("productionOrder", 3), ("productionOrder", 6), ("nonconformance", 7),
    ("systemPeriodicReview", 0), ("systemPeriodicReview", 1), ("systemPeriodicReview", 3), ("nonconformance", 8), ("productionOrder", 9)])
_tl(E, "reviewFromAt", [DT(9, 15, 6, 0), DT(9, 16, 22, 34), DT(9, 17, 6, 51), DT(9, 21, 7, 42), DT(9, 22, 15, 59), DT(4, 1, 0, 0), DT(4, 1, 0, 0), DT(4, 1, 0, 0), DT(9, 24, 0, 0), DT(9, 23, 9, 0)])
_tl(E, "reviewToAt", [DT(9, 15, 13, 40), DT(9, 17, 6, 14), DT(9, 17, 14, 31), DT(9, 21, 15, 22), DT(9, 23, 9, 0), DT(9, 15, 0, 0), DT(9, 15, 0, 0), DT(9, 15, 0, 0), DT(9, 24, 8, 30), DT(9, 24, 14, 0)])
_tl(E, "entriesReviewedCount", [38, 21, 44, 29, 17, 1264, 86, 41, 12, 4])
_tl(E, "criticalEntriesCount", [5, 2, 9, 4, 6, 212, 14, 6, 5, 1])
_tl(E, "anomalyCount", [1, 0, 2, 1, 3, 2, 1, 0, 1, 0])
_tl(E, "findingsText", ["Tool life override justified in the interlock event", "None", "Hardness limit change and one manual die temperature entry justified",
    None, "Three retest results entered manually without second-person verification", "Two report template changes without change record",
    "Local shared account used for two logins", "None", "Marking parameter changed during lens cleaning; change justified", "None"])
_r(E, "nonconformanceId", [None, None, None, None, 7, None, None, None, None, None])
_r(E, "reviewedById", [3, 3, 3, 3, 3, 8, 5, 5, 3, 3])
_tl(E, "reviewedAt", [DT(9, 16, 10, 0), DT(9, 17, 14, 30), DT(9, 18, 10, 45), None, DT(9, 23, 15, 0), DT(9, 18, 15, 0), DT(9, 19, 10, 30), DT(9, 21, 16, 0), DT(9, 24, 11, 0), DT(9, 24, 15, 30)])
_r(E, "electronicSignatureId", N10)

E = "userAccessReview"
_r(E, "computerisedSystemId", list(range(10)))
_tl(E, "reviewPeriodFromDate", [D0(2026, 4, 1)] * 9 + [D0(2026, 4, 1)])
_tl(E, "reviewPeriodToDate", [D0(2026, 9, 15)] * 9 + [D0(2026, 4, 14)])
_tl(E, "usersReviewedCount", [146, 12, 14, 9, 7, 6, 18, 11, 8, 6])
_tl(E, "accessRemovedCount", [1, 1, 0, 0, 0, 0, 0, 0, 0, 6])
_tl(E, "accessChangedCount", [1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
_r(E, "reviewedById", [8, 5, 5, 5, 8, 8, 8, 8, 3, 5])
_tl(E, "reviewedAt", [DT(9, 16, 15, 0), DT(9, 17, 11, 0), DT(9, 17, 12, 0), DT(9, 17, 14, 0), None, DT(9, 18, 11, 0), DT(9, 18, 12, 0), DT(9, 18, 14, 0), None, DT(4, 14, 15, 0)])
_r(E, "approvedById", [3, 3, 3, 3, None, 3, 3, 3, None, 3])
_tl(E, "approvedAt", [DT(9, 17, 10, 0), DT(9, 18, 10, 0), DT(9, 18, 10, 10), DT(9, 18, 10, 20), None, DT(9, 19, 10, 0), DT(9, 19, 10, 10), DT(9, 19, 10, 20), None, DT(4, 15, 10, 0)])

E = "userAccessReviewLine"
_r(E, "userId", [0, 4, 8, 2, 5, 1, 0, 2, 7, 7])
_r(E, "roleId", [0, 3, 9, 1, 6, 1, 1, 0, 7, 7])
_tl(E, "accessStillRequired", [True, True, False, False, True, False, True, True, True, True])
_tl(E, "reviewAction", ["Retain", "Retain", "Remove Role", "Change Role", "Retain", "Lock Account", "Retain", "Retain", "Retain", "Retain"])
_tl(E, "actionCompletedAt", [None, None, DT(9, 16, 16, 30), DT(9, 16, 16, 40), None, DT(9, 17, 11, 30), None, None, None, None])
_tl(E, "comment", [None, None, "Administrator role no longer needed after go-live of release 2.7.0; process engineer role kept",
    "Moved from machine setter to production operator on 1 September 2026", None,
    "Shared local account on the tester replaced by personal badge login", None, None, None, None])

# ---------------------------------------------------------------- qual: batch record review and release
E = "batchRecordReview"
_r(E, "productionOrderId", list(range(10)))
_r(E, "itemId", [0, 1, 2, 3, 0, 2, 3, 0, 2, 0])
_r(E, "lotId", [None, None, 3, 1, None, None, None, None, None, None])
_tl(E, "reviewScope", ["Review By Exception", "Review By Exception", "Review By Exception", "Review By Exception", "Review By Exception",
    "Review By Exception", "Review By Exception", "Full Review", "Review By Exception", "Full Review"])
_tl(E, "operationsCount", [2385, 1530, 1440, 720, 478, 0, 720, 866, 0, 0])
_tl(E, "exceptionCount", [2, 0, 1, 3, 0, 0, 2, 2, 0, 0])
_tl(E, "openExceptionCount", [0, 0, 0, 0, 0, 0, 1, 1, 0, 0])
_tl(E, "genealogyComplete", [True, False, True, True, False, False, True, False, False, True])
_r(E, "yieldReconciliationId", [0, None, 3, 4, None, None, 6, 7, None, None])
_r(E, "auditTrailReviewId", [0, None, 1, 2, None, None, 3, 4, None, 9])
_r(E, "productionReviewedById", [4, None, 4, 4, None, None, 4, 4, None, 4])
_tl(E, "productionReviewedAt", [DT(9, 15, 15, 10), None, DT(9, 17, 9, 30), DT(9, 17, 16, 0), None, None, DT(9, 22, 10, 0), DT(9, 23, 9, 40), None, DT(9, 24, 14, 30)])
_r(E, "qaReviewedById", [3, None, 3, 3, None, None, None, 3, None, 3])
_tl(E, "qaReviewedAt", [DT(9, 16, 10, 20), None, DT(9, 17, 14, 45), DT(9, 18, 11, 5), None, None, None, DT(9, 23, 15, 20), None, DT(9, 24, 16, 0)])
_r(E, "electronicSignatureId", N10)
_tl(E, "returnReasonText", [None] * 7 + ["Retest results of three units entered manually without second-person verification; correct and re-sign", None, None])

E = "batchRecordReviewException"
_tl(E, "exceptionType", ["Interlock Override", "Hold", "Out Of Specification Result", "Deviation", "Data Correction", "Manual Data Entry",
    "Late Entry", "Out Of Specification Result", "Hold", "Manual Data Entry"])
POST[E] = _poly([("interlockEvent", 3), ("interlockEvent", 7), ("nonconformance", 2), ("nonconformance", 1), ("auditTrail", 1), ("operationExecution", 0),
    ("auditTrail", 0), ("nonconformance", 0), ("qualityHold", 0), ("nonconformance", 7)])
_tl(E, "description", ["Tool life limit of the nutrunner socket overridden by the supervisor for 40 rundowns until the socket change",
    "Unit on quality hold blocked at operation start and removed from the line",
    "Piston bore oversize on two bodies after insert breakage; bodies scrapped under NCR-2026-000124",
    "Hardness 83-85 HBW on the furnace charge; used under deviation permit DEV-2026-0007",
    "Hardness limit of the characteristic edited during the order; change checked against the released specification",
    "Die temperature entered manually for 35 minutes during a thermocouple fault",
    "Wall thickness result entered three hours after measurement",
    "Shrinkage porosity found on castings of die 2; NCR-2026-000118 open",
    "Order on hold after leak test failures at the 140 bar stage",
    "Retest results of three units entered manually without second-person verification"])
_tl(E, "assessment", ["Impact Assessed Acceptable", "No Impact", "Impact Assessed Acceptable", "Requires Deviation", "Impact Assessed Acceptable", "No Impact",
    "Impact Assessed Acceptable", None, None, "Requires Correction"])
_r(E, "assessedById", [3, 3, 3, 3, 3, 3, 3, None, None, 3])
_tl(E, "assessedAt", [DT(9, 16, 9, 50), DT(9, 16, 10, 5), DT(9, 17, 14, 20), DT(9, 18, 10, 20), DT(9, 18, 10, 35), DT(9, 18, 10, 50),
    DT(9, 22, 10, 30), None, None, DT(9, 23, 15, 10)])

E = "batchRelease"
_r(E, "lotId", [1, 0, 2, 3, None, None, None, None, None, 2])
_r(E, "productionOrderId", [3, 3, 2, 2, 0, 7, 6, 1, 4, 2])
_r(E, "itemId", [3, 3, 2, 2, 0, 0, 3, 1, 0, 2])
_r(E, "batchRecordReviewId", [3, 3, 2, 2, 0, 7, 6, 1, 4, 2])
_tl(E, "releaseQuantity", [231, 231, 234, 232, 474, 172, 236, 305, 95, 2])
_r(E, "unitOfMeasureId", [0] * 10)
_r(E, "deviationPermitId", [1, None, None, None, None, None, None, None, None, None])
_r(E, "qualityHoldId", [None, None, None, None, None, 0, None, None, None, None])
_r(E, "certificateControlledDocumentId", N10)
_r(E, "releasedById", [3, 3, 3, 3, 3, None, None, None, None, 3])
_tl(E, "releasedAt", [DT(9, 18, 11, 30), DT(9, 17, 15, 10), DT(9, 17, 15, 0), DT(9, 17, 15, 5), DT(9, 16, 10, 40), None, None, None, None, DT(9, 17, 14, 55)])
_r(E, "electronicSignatureId", N10)
_tl(E, "decisionText", ["Released under deviation permit DEV-2026-0007 for hardness 83-85 HBW; customer approval on file",
    "Casting lot released to heat treatment after record review", "234 machined bodies released; 2 rejected bodies excluded",
    "Anodising load released after coating thickness check", "474 calipers released for dispatch", "Pending closure of NCR-2026-000139",
    "Pending quality review of the production record", "Order still in production", "Order still in production",
    "Two bodies with piston bore oversize rejected (NCR-2026-000124)"])

# ---------------------------------------------------------------- plan: yield and reconciliation, line clearance
E = "yieldReconciliation"
_r(E, "productionOrderId", [0, 0, 0, 2, 3, 3, 6, 7, 7, 2])
_tl(E, "reconciliationType", ["Product Yield", "Label Reconciliation", "Component Reconciliation", "Product Yield", "Product Yield",
    "Component Reconciliation", "Product Yield", "Product Yield", "Label Reconciliation", "Component Reconciliation"])
_r(E, "itemId", [0, 0, 5, 2, 3, 9, 3, 0, 0, 3])
_r(E, "unitOfMeasureId", [0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
_tl(E, "theoreticalQuantity", ["480", "480", "480", "240", "240", "552.000", "240", "480", "200", "240"])
_tl(E, "issuedQuantity", ["480", "500", "500", "240", "240", "560.000", "240", "178", "200", "240"])
_tl(E, "outputQuantity", ["474", "476", "476", "238", "231", "547.200", "236", "172", "172", "238"])
_tl(E, "rejectedQuantity", ["2", "0", "3", "2", "9", "0.000", "4", "3", "0", "2"])
_tl(E, "destroyedQuantity", ["0", "2", "0", "0", "0", "6.300", "0", "0", "1", "0"])
_tl(E, "returnedQuantity", ["4", "22", "21", "0", "0", "6.500", "0", "0", "27", "0"])
_tl(E, "unaccountedQuantity", ["0", "0", "0", "0", "0", "0.000", "0", "3", "0", "0"])
_tl(E, "yieldPct", ["98.75", "100.00", "100.00", "99.17", "96.25", "97.71", "98.33", "96.63", "100.00", "100.00"])
_tl(E, "lowerLimitPct", ["98.00", "100.00", "99.50", "98.00", "95.00", "96.00", "95.00", "98.00", "100.00", "99.50"])
_tl(E, "upperLimitPct", ["100.00", "100.00", "100.50", "100.00", "100.00", "100.00", "100.00", "100.00", "100.00", "100.50"])
_tl(E, "withinLimits", [True, True, True, True, True, True, True, False, True, True])
_r(E, "nonconformanceId", [None] * 7 + [7, None, None])
_tl(E, "calculatedAt", [DT(9, 15, 14, 5), DT(9, 15, 14, 6), DT(9, 15, 14, 7), DT(9, 17, 6, 40), DT(9, 17, 14, 55), DT(9, 17, 14, 56), DT(9, 21, 15, 45),
    DT(9, 23, 9, 30), DT(9, 23, 9, 31), DT(9, 17, 6, 41)])
_r(E, "approvedById", [3, 3, 3, 3, 3, 3, None, None, None, 3])
_tl(E, "approvedAt", [DT(9, 16, 10, 15), DT(9, 16, 10, 16), DT(9, 16, 10, 17), DT(9, 17, 14, 40), DT(9, 18, 11, 0), DT(9, 18, 11, 1), None, None, None, DT(9, 17, 14, 41)])

E = "lineClearance"
_r(E, "lineId", [5, 5, 2, 0, 5, 0, 5, 5, 2, 2])
_r(E, "workCenterId", N10)
_tl(E, "clearanceType", ["Before Order Start", "Order Changeover", "Before Order Start", "Before Order Start", "Order Changeover",
    "Before Order Start", "Order Changeover", "Order Changeover", "Before Order Start", "Before Order Start"])
_r(E, "previousProductionOrderId", [None, 0, None, None, 1, 3, 4, 4, 2, 2])
_r(E, "productionOrderId", [0, 1, 2, 3, 4, 6, 7, 7, 8, 5])
_r(E, "changeoverId", [None, None, None, 0, None, None, 7, 7, None, None])
_r(E, "checkSheetResultId", [5, None, None, None, None, None, None, None, None, None])
_tl(E, "materialsRemoved", [True] * 10)
_tl(E, "labelsRemoved", [True] * 6 + [False, True, True, True])
_tl(E, "documentsRemoved", [True] * 10)
_tl(E, "equipmentClean", [True] * 10)
_r(E, "performedById", [0, 1, 2, 0, 1, 1, 2, 2, 2, 1])
_tl(E, "startedAt", [DT(9, 15, 5, 40), DT(9, 15, 13, 45), DT(9, 16, 22, 5), DT(9, 17, 6, 20), DT(9, 18, 14, 40), DT(9, 21, 7, 10), DT(9, 22, 15, 25), DT(9, 22, 15, 40), DT(9, 24, 23, 40), DT(9, 19, 22, 10)])
_tl(E, "completedAt", [DT(9, 15, 5, 52), DT(9, 15, 14, 2), DT(9, 16, 22, 20), DT(9, 17, 6, 35), DT(9, 18, 14, 58), DT(9, 21, 7, 24), DT(9, 22, 15, 38), DT(9, 22, 15, 52), None, DT(9, 19, 22, 24)])
_r(E, "verifiedById", [4, 4, 4, 4, 4, 4, None, 4, None, None])
_tl(E, "verifiedAt", [DT(9, 15, 5, 55), DT(9, 15, 14, 6), DT(9, 16, 22, 25), DT(9, 17, 6, 38), DT(9, 18, 15, 2), DT(9, 21, 7, 28), None, DT(9, 22, 15, 55), None, None])
_r(E, "electronicSignatureId", N10)
_tl(E, "failureText", [None] * 6 + ["Two LH caliper labels of PO-1000440 found under the leak tester fixture", None, None, None])

# ---------------------------------------------------------------- maint: logbook and cleaning
E = "logbookEntry"
POST[E] = _poly([("equipment", 5), ("equipment", 5), ("equipment", 5), ("equipment", 3), ("equipment", 0), ("equipment", 0), ("equipment", 7),
    ("area", 4), ("equipment", 4), ("equipment", 8)])
_tl(E, "activityType", ["Production", "Line Clearance", "Production", "Cleaning", "Production", "Maintenance", "Qualification", "Cleaning", "Idle", "Cleaning"])
_r(E, "productionOrderId", [0, 1, 1, None, 3, None, None, None, None, None])
_r(E, "lotId", [None, None, None, None, 0, None, None, None, None, None])
_r(E, "cleaningRecordId", [None, None, None, 1, None, None, None, None, None, 6])
_r(E, "maintenanceWorkOrderId", [None, None, None, None, None, 0, None, None, None, None])
_r(E, "lineClearanceId", [None, 1, None, None, None, None, None, None, None, None])
_tl(E, "entryText", ["Piston press-in for PO-1000412: 474 good, 2 rejected", "Line clearance LH to RH before PO-1000419, verified",
    "Piston press-in for PO-1000419 (RH) started", "Wash bath change and filter replacement, cleanliness test passed",
    "Casting of lot L260915-GDC-014 for PO-1000433", "Die ejector pin freed and ejector plate inspected (MWO-2026-000341)",
    "Periodic leak tester verification with master leak, 5 bar and 140 bar", "Weekly cleaning of the assembly clean area, floor and benches",
    "Line idle on weekly off; bath circulation and heating kept on", "Marking lens cleaned after code grade fell below A"])
_r(E, "performedById", [0, 1, 1, 5, 0, 5, 5, 4, 9, 2])
_tl(E, "startedAt", [DT(9, 15, 6, 0), DT(9, 15, 13, 45), DT(9, 15, 14, 17), DT(9, 17, 5, 0), DT(9, 17, 6, 51),
    lambda env: raw(env, "maintenanceWorkOrder", 0, "startedAt") or raw(env, "maintenanceWorkOrder", 0, "reportedAt"),
    DT(9, 16, 8, 0), DT(9, 19, 22, 0), DT(9, 20, 0, 0), DT(9, 24, 0, 30)])
_tl(E, "completedAt", [DT(9, 15, 13, 40), DT(9, 15, 14, 2), None, DT(9, 17, 6, 30), DT(9, 17, 14, 31),
    lambda env: raw(env, "maintenanceWorkOrder", 0, "completedAt"), DT(9, 16, 9, 10), DT(9, 19, 23, 0), DT(9, 21, 6, 0), DT(9, 24, 0, 45)])
_r(E, "reviewedById", [4, 4, None, 3, 4, 4, 3, 3, 4, None])
_tl(E, "reviewedAt", [DT(9, 15, 14, 10), DT(9, 15, 14, 12), None, DT(9, 17, 7, 0), DT(9, 17, 15, 0), DT(9, 18, 9, 0), DT(9, 16, 10, 0), DT(9, 21, 6, 30), DT(9, 21, 6, 45), None])
for _k in ("startedAt", "completedAt"):
    _lst = VAL[(E, _k)]
    VAL[(E, _k)] = (lambda lst: (lambda env: lst[env["i"]](env) if callable(lst[env["i"]]) else lst[env["i"]]))(_lst)

E = "cleaningRecord"
_r(E, "equipmentId", [5, 3, 4, 5, 6, 7, 8, 9, 0, 5])
_r(E, "workCenterId", [5, 3, 4, 5, 6, 7, 8, 9, 0, 5])
_tl(E, "cleaningType", ["Product Changeover Cleaning", "Bath Change", "Bath Change", "Product Changeover Cleaning", "Minor Cleaning", "Minor Cleaning",
    "Minor Cleaning", "Minor Cleaning", "Major Cleaning", "Product Changeover Cleaning"])
_r(E, "procedureControlledDocumentId", [3, 3, 4, 3, 3, 3, 3, 3, 3, 3])
_r(E, "previousProductionOrderId", [0, None, None, 1, None, 4, None, None, 6, 1])
_r(E, "previousItemId", [0, None, None, 1, None, 0, None, None, 3, 1])
_tl(E, "dirtyHoldStartAt", [DT(9, 15, 13, 40), None, None, DT(9, 18, 14, 20), None, DT(9, 22, 15, 5), None, None, DT(9, 21, 15, 22), DT(9, 16, 21, 50)])
_tl(E, "startedAt", [DT(9, 15, 13, 41), DT(9, 17, 5, 0), DT(9, 19, 6, 10), DT(9, 18, 14, 25), DT(9, 21, 6, 40), DT(9, 22, 15, 10), DT(9, 24, 0, 30), DT(9, 24, 8, 10), DT(9, 21, 15, 40), DT(9, 16, 22, 0)])
_tl(E, "completedAt", [DT(9, 15, 13, 44), DT(9, 17, 6, 30), DT(9, 19, 12, 30), DT(9, 18, 14, 36), DT(9, 21, 6, 50), DT(9, 22, 15, 22), DT(9, 24, 0, 45), None, DT(9, 21, 19, 10), DT(9, 16, 22, 12)])
_r(E, "cleanedById", [0, 5, 5, 1, 0, 2, 2, 1, 5, 2])
_tl(E, "verificationMethod", ["Visual Inspection", "Cleanliness Test", "Rinse Sample", "Visual Inspection", "Visual Inspection", "Visual Inspection",
    "Visual Inspection", "Visual Inspection", "Visual Inspection", "Visual Inspection"])
_tl(E, "verificationResult", ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass", None, None, "Pass"])
_r(E, "verifiedById", [4, 3, 3, 4, 4, 4, 3, None, None, 4])
_tl(E, "verifiedAt", [DT(9, 15, 13, 45), DT(9, 17, 6, 40), DT(9, 19, 13, 0), DT(9, 18, 14, 38), DT(9, 21, 6, 55), DT(9, 22, 15, 24), DT(9, 24, 0, 50), None, None, DT(9, 16, 22, 15)])
_tl(E, "cleanHoldExpiresAt", [DT(9, 16, 13, 45), DT(9, 24, 6, 40), None, DT(9, 19, 14, 38), DT(9, 22, 6, 55), DT(9, 23, 15, 24), DT(9, 25, 0, 50), None, None, DT(9, 17, 22, 15)])
_r(E, "electronicSignatureId", N10)

# ---------------------------------------------------------------- qual: environmental monitoring
E = "environmentalMonitoringPoint"
VAL[(E, "name")] = lambda env: MASTER_ADD["environmentalMonitoringPoint"].split("\n")[env["i"]].split("|")[1]
_r(E, "areaId", [4, 4, 4, 4, 3, 5, 5, 7, 7, 4])
_r(E, "workCenterId", [5, 5, 5, None, 3, 9, 9, None, None, 5])
_tl(E, "monitoredParameter", ["Airborne Particles 0.5 um", "Temperature", "Relative Humidity", "Differential Pressure", "Surface Particle Count", "Illuminance",
    "Temperature", "Temperature", "Relative Humidity", "Airborne Particles 5.0 um"])
_tl(E, "parameterUnitText", ["particles per m3", "degC", "percent RH", "Pa", "particles above 200 um per part", "lux", "degC", "degC", "percent RH", "particles per m3"])
_tl(E, "limitDirection", ["Upper", "Range", "Range", "Lower", "Upper", "Range", "Range", "Range", "Range", "Upper"])
_tl(E, "alertLimit", ["2800000", "26.0", "60.0", "8.0", "15", None, "28.0", "20.5", "58.0", "25000"])
_tl(E, "actionLimit", ["3520000", "28.0", "65.0", "5.0", "20", "1200", "30.0", "21.0", "60.0", "29300"])
_tl(E, "lowerActionLimit", [None, "18.0", "30.0", None, None, "800", "18.0", "19.0", "40.0", None])
_tl(E, "samplingFrequency", ["Weekly", "Continuous", "Every Shift", "Every Shift", "Every Shift", "Every Shift", "Every Shift", "Continuous", "Continuous", "Weekly"])
_r(E, "processTagId", N10)

E = "environmentalMonitoringResult"
_r(E, "environmentalMonitoringPointId", list(range(10)))
_tl(E, "sampledAt", [DT(9, 15, 7, 10), DT(9, 15, 10, 0), DT(9, 15, 14, 30), DT(9, 16, 6, 20), DT(9, 17, 7, 30), DT(9, 24, 8, 5), DT(9, 22, 14, 30), DT(9, 18, 9, 0), DT(9, 21, 9, 0), DT(9, 15, 7, 15)])
_tl(E, "measuredValue", ["1840000", "24.6", "52.0", "12.0", "17", "760", "27.1", "20.4", "63.5", "18400"])
_tl(E, "limitEvaluation", ["Within Limits", "Within Limits", "Within Limits", "Within Limits", "Alert Limit Exceeded", "Action Limit Exceeded",
    "Within Limits", "Within Limits", "Action Limit Exceeded", "Within Limits"])
_r(E, "sampledById", [3, 0, 1, 0, 3, 1, 1, 3, 3, 3])
_r(E, "gaugeId", [None, None, None, None, 3, None, None, None, None, None])
_r(E, "nonconformanceId", N10)
_tl(E, "productImpactText", [None, None, None, None, "Alert only; washer filter checked, no action on product",
    "Lighting below 800 lux for 25 minutes; 18 calipers inspected in that period re-inspected under restored lighting, all OK",
    None, None, "CMM measurements suspended until humidity is back in range; no product measured during the excursion", None])

# ---------------------------------------------------------------- matl: dispensing
E = "dispenseRecord"
_r(E, "productionOrderId", [3, 3, 6, 6, 0, 0, 0, 7, 4, 1])
_r(E, "itemId", [9, 9, 9, 9, 5, 6, 7, 5, 5, 5])
_r(E, "lotId", [8, 8, 8, 8, 9, 6, 7, 9, 9, 5])
_tl(E, "dispenseMethod", ["Gravimetric Weighing"] * 4 + ["Count By Weight"] * 6)
_tl(E, "targetWeight", ["280.000", "280.000", "280.000", "280.000", "2.100", "3.250", "4.200", "2.100", "2.100", "2.100"])
_tl(E, "tolerancePct", ["0.50"] * 10)
_tl(E, "tareWeight", ["42.300", "42.300", "42.300", "42.300", "0.850", "0.850", "0.850", "0.850", "0.850", "0.850"])
_tl(E, "grossWeight", ["322.450", "321.900", "323.900", "322.200", "2.952", "4.108", "5.046", "2.946", "2.953", "2.949"])
_tl(E, "netWeight", ["280.150", "279.600", "281.600", "279.900", "2.102", "3.258", "4.196", "2.096", "2.103", "2.099"])
_r(E, "unitOfMeasureId", [1] * 10)
_tl(E, "pieceCount", [None, None, None, None, 500, 501, 499, 499, 500, 500])
_tl(E, "withinTolerance", [True, True, False, True, True, True, True, True, True, True])
_r(E, "balanceGaugeId", N10)
_r(E, "storageLocationId", [0, 0, 0, 0, 2, 2, 2, 2, 2, 2])
_r(E, "dispensedById", [7] * 10)
_tl(E, "dispensedAt", [DT(9, 17, 6, 5), DT(9, 17, 10, 20), DT(9, 21, 7, 0), DT(9, 21, 7, 8), DT(9, 15, 5, 20), DT(9, 15, 5, 22), DT(9, 15, 5, 24), DT(9, 22, 15, 10), DT(9, 18, 14, 30), DT(9, 15, 13, 30)])
_tl(E, "verificationMethod", ["System Check", "System Check", "System Check", "System Check", "Second Person", "Second Person", "Second Person", "Second Person", "Second Person", "System Check"])
_r(E, "verifiedById", [9, 9, 9, 9, 4, 4, 4, 4, 4, None])
_tl(E, "verifiedAt", [DT(9, 17, 6, 5, 20), DT(9, 17, 10, 20, 20), DT(9, 21, 7, 0, 20), DT(9, 21, 7, 8, 20), DT(9, 15, 5, 30), DT(9, 15, 5, 31), DT(9, 15, 5, 32), DT(9, 22, 15, 15), DT(9, 18, 14, 35), None])
_r(E, "labelId", N10)

# ---------------------------------------------------------------- qual: retention samples
E = "retentionSample"
_r(E, "itemId", [3, 3, 2, 2, 0, 0, 4, 5, 5, 7])
_r(E, "lotId", [0, 1, 2, 3, None, None, 4, 9, 5, 7])
_r(E, "productionOrderId", [3, 3, 2, 2, 0, 0, None, None, None, None])
_r(E, "serialNumberId", [None, None, None, None, 0, 1, None, None, None, None])
_tl(E, "sampleType", ["Retention Sample", "Retention Sample", "Retention Sample", "Retention Sample", "Retention Sample", "Retention Sample",
    "Reserve Sample", "Reserve Sample", "Reserve Sample", "Reserve Sample"])
_tl(E, "sampleQuantity", [2, 2, 1, 2, 1, 1, 5, 20, 20, 10])
_r(E, "unitOfMeasureId", [0] * 10)
_r(E, "storageLocationId", [2] * 10)
_r(E, "collectedById", [3] * 10)
_tl(E, "collectedAt", [DT(9, 17, 14, 40), DT(9, 17, 14, 45), DT(9, 17, 6, 30), DT(9, 17, 6, 35), DT(9, 15, 13, 30), DT(9, 15, 13, 32),
    DT(8, 5, 11, 0), DT(9, 12, 10, 0), DT(9, 6, 11, 0), DT(9, 2, 10, 30)])
_tl(E, "retainUntilDate", [D0(2027, 12, 31), D0(2027, 12, 31), D0(2027, 12, 31), D0(2027, 12, 31), D0(2027, 12, 31), D0(2027, 12, 31),
    D0(2027, 8, 31), D0(2027, 9, 30), D0(2027, 9, 30), D0(2027, 9, 30)])
_tl(E, "withdrawnAt", [None] * 5 + [DT(9, 23, 11, 0), None, None, DT(9, 19, 14, 0), DT(9, 21, 10, 0)])
_tl(E, "withdrawalReason", [None] * 5 + ["Withdrawn for comparison test against warranty return CMP-2026-0011", None, None,
    "Withdrawn for seal cut investigation NCR-2026-000133", "Destroyed in torque-to-failure test for NCR-2026-000136"])
_r(E, "customerComplaintId", [None] * 5 + [7, None, None, None, None])

# ---------------------------------------------------------------- qual: risk assessments
E = "riskAssessment"
VAL[(E, "title")] = lambda env: TITLES_ADD["riskAssessment"].split("\n")[env["i"]]
POST[E] = _poly([("computerisedSystem", 0), ("engineeringChange", 6), ("engineeringChange", 0), ("nonconformance", 1), ("nonconformance", 7),
    ("equipment", 9), ("engineeringChange", 1), ("item", 0), ("item", 0), ("computerisedSystem", 9)])
_tl(E, "assessmentMethod", ["Risk Ranking And Filtering", "FMEA", "FMEA", "Risk Ranking And Filtering", "Fault Tree Analysis", "Preliminary Hazard Analysis",
    "FMEA", "FMEA", "FMEA", "Risk Ranking And Filtering"])
_tl(E, "scopeText", ["New and changed functions of release 2.7.0: signatures, batch record review, release, reconciliation, reports",
    "Firmware change and booster at the leak test station, both test stages", "Angle window added to the bleed screw tightening program",
    "Use of one furnace charge with hardness 83-85 HBW", "Causes of failures at the 140 bar stage on PO-1000461",
    "Release of the boot classifier version 1.3 at final inspection", "Second source for piston seals",
    "All process steps of the front caliper LH", "All process steps of the front caliper LH after the torque window change",
    "Retirement of the anodising line PLC and archiving of its data"])
_tl(E, "initialRiskLevel", ["High", "High", "Medium", "Medium", "High", "Medium", "Medium", "High", "High", "Medium"])
_tl(E, "residualRiskLevel", ["Low", "Low", "Low", "Low", None, None, None, "Low", "Low", "Low"])
_tl(E, "riskControlsText", ["Scripted testing of signature, release and reconciliation functions; unscripted testing of reports",
    "Master leak verification at both stages after installation; curve envelope review", "Two forced failures in validation; angle window monitored by SPC",
    "Use only under deviation permit; 100 percent hardness check of the charge", None, None, None,
    "Error-proofing at piston press, torque and leak test; 100 percent leak test", "As before, with angle monitoring on bleed screw tightening",
    "Data archived and read back before retirement"])
_r(E, "pfmeaId", [None, 0, 0, 3, 0, None, 0, 0, 0, None])
_tl(E, "acceptanceDecision", ["Accepted With Controls", "Accepted With Controls", "Accepted", "Accepted With Controls", None, None, None, "Accepted With Controls", "Accepted With Controls", "Accepted"])
_r(E, "approvedById", [3, 3, 3, 3, None, None, None, 6, 6, 3])
_tl(E, "approvedAt", [DT(8, 14, 10, 0), DT(6, 5, 11, 0), DT(5, 8, 15, 0), DT(9, 16, 12, 0), None, None, None, DT(4, 20, 11, 0), DT(5, 25, 11, 0), DT(4, 10, 15, 0)])
_tl(E, "nextReviewDate", [D0(2027, 8, 14), D0(2027, 6, 5), D0(2027, 5, 8), None, None, None, None, None, D0(2027, 5, 25), None])

# ---------------------------------------------------------------- qual: product quality reviews
E = "productQualityReview"
_r(E, "itemId", [0, 0, 1, 1, 2, 2, 3, 3, 4, 5])
_tl(E, "reviewPeriodFromDate", [D0(2026, 4, 1), D0(2026, 7, 1), D0(2026, 4, 1), D0(2026, 7, 1), D0(2026, 4, 1), D0(2026, 7, 1), D0(2026, 4, 1), D0(2026, 7, 1), D0(2026, 4, 1), D0(2026, 4, 1)])
_tl(E, "reviewPeriodToDate", [D0(2026, 6, 30), D0(2026, 9, 30), D0(2026, 6, 30), D0(2026, 9, 30), D0(2026, 6, 30), D0(2026, 9, 30), D0(2026, 6, 30), D0(2026, 9, 30), D0(2026, 9, 30), D0(2026, 9, 30)])
_tl(E, "lotsProducedCount", [118, 112, 41, 39, 236, 228, 238, 231, 14, 22])
_tl(E, "lotsReleasedCount", [117, 108, 41, 38, 234, 225, 236, 228, 14, 21])
_tl(E, "lotsRejectedCount", [1, 0, 0, 0, 2, 1, 2, 1, 0, 1])
_tl(E, "nonconformanceCount", [6, 9, 1, 2, 5, 4, 7, 6, 1, 3])
_tl(E, "deviationPermitCount", [1, 2, 0, 0, 1, 1, 1, 1, 0, 0])
_tl(E, "customerComplaintCount", [3, 7, 0, 0, 1, 1, 0, 1, 0, 2])
_tl(E, "capaCount", [2, 5, 0, 0, 1, 2, 1, 2, 0, 2])
_tl(E, "engineeringChangeCount", [2, 3, 1, 1, 1, 1, 0, 1, 0, 1])
_tl(E, "productRecallCount", [1, 7, 0, 0, 0, 0, 0, 1, 0, 1])
_tl(E, "processCapabilityText", ["Bleed screw torque Cpk 1.92; pressure drop at 140 bar Cpk 2.10", None, "Bleed screw torque Cpk 1.88", None,
    "Piston bore diameter Cpk 1.71; coating thickness Cpk 1.41", None, "Wall thickness at bridge Cpk 1.52; hardness Cpk 1.38", None,
    "Piston diameter Cpk 2.05 from supplier data", "Seal section Cpk 1.45 from supplier data"])
_tl(E, "conclusionText", ["Process in a state of control; no change to the control strategy", None, "Process in a state of control", None,
    "Process in a state of control; coating thickness capability to be improved", None, "Hardness capability marginal; furnace uniformity survey brought forward", None,
    "Supplier process in a state of control", "Seal cut complaints traced to supplier lot SEL-011; supplier conditionally approved"])
_tl(E, "actionsText", ["None", None, "None", None, "Anodising thickness study PVL-2026-007", None, "Requalification of the T6 furnace", None, "None", "Second source qualification PVL-2026-010"])
_r(E, "reportControlledDocumentId", N10)
_r(E, "approvedById", [6, None, 6, None, 6, None, 6, None, 6, 6])
_tl(E, "approvedAt", [DT(7, 15, 11, 0), None, DT(7, 15, 11, 30), None, DT(7, 16, 11, 0), None, DT(7, 16, 11, 30), None, DT(9, 24, 11, 0), DT(9, 24, 11, 30)])

# ---------------------------------------------------------------- qual: recalls
E = "productRecall"
VAL[(E, "title")] = lambda env: TITLES_ADD["productRecall"].split("\n")[env["i"]]
_tl(E, "recallClass", ["Class III", "Class I", "Class II", "Class II", "Class II", "Class III", "Class II", "Class II", "Class III", "Class III"])
_tl(E, "recallScope", ["Customer Plant", "Field", "Customer Plant", "Customer Plant", "Customer Plant", "Customer Plant", "Field", "Customer Plant", "Customer Plant", "Customer Plant"])
_tl(E, "reasonText", ["2D code not readable at the customer scanner", "Brake fluid leak at warranty traced to piston seals from lot L260905-SEL-011",
    "Bleed screw found loose at the customer line", "Metallic particle found in brake fluid at the customer fill station",
    "Shrinkage porosity found on castings from die 2", "White corrosion spots on anodised surface after transit",
    "Piston does not retract fully on two vehicles", "Fluid seepage at piston seal on a zero-kilometre vehicle",
    "Caliper body deflection above limit in the customer bench test", "Bleed screw cap missing on three calipers"])
_r(E, "customerId", [7, 0, 2, 1, 0, 0, 0, 0, 0, 0])
_r(E, "customerComplaintId", [8, 7, 6, 3, 0, 4, 2, 5, 1, 9])
_r(E, "nonconformanceId", [8, 5, 6, 3, 0, None, None, 5, None, 9])
_r(E, "traceInvestigationId", [None, 0, 2, None, 4, None, None, 0, None, 1])
_r(E, "capaId", [8, 7, 6, 3, 0, None, None, 7, None, 9])
_r(E, "initiatedById", [3, 6, 3, 3, 3, 3, 6, 3, 3, 3])
_tl(E, "initiatedAt", [DT(9, 24, 13, 0), DT(9, 23, 18, 0), DT(9, 21, 12, 0), DT(9, 19, 10, 0), DT(9, 18, 9, 0), DT(9, 16, 10, 0), DT(9, 24, 16, 0), DT(9, 22, 11, 0), DT(9, 17, 10, 0), DT(9, 24, 12, 0)])
_tl(E, "authorityNotified", [False, True, False, False, False, False, False, False, False, False])
_tl(E, "authorityNotifiedAt", [None, DT(9, 24, 10, 0), None, None, None, None, None, None, None, None])
_tl(E, "quantityShipped", [12, 1180, 480, 240, 0, 0, 960, 420, 240, 96])
_tl(E, "quantityRecovered", [12, 640, 480, 236, 0, 0, 0, 300, 240, 96])
_tl(E, "effectivenessCheckCompleted", [True, False, True, True, False, False, False, False, True, True])
_r(E, "closedById", [6, None, None, 6, 3, 3, None, None, None, None])
_tl(E, "closedAt", [DT(9, 24, 18, 30), None, None, DT(9, 24, 15, 0), DT(9, 18, 16, 0), DT(9, 17, 12, 0), None, None, None, None])

E = "productRecallLot"
_r(E, "lotId", [3, 5, 5, 7, 2, 0, 4, 5, 1, 7])
_r(E, "shipmentId", [8, 5, 7, 6, 3, None, 7, 4, 2, 5])
_tl(E, "quantityShipped", [12, 700, 480, 480, 240, 0, 960, 420, 240, 96])
_tl(E, "quantityRecovered", [12, 410, 230, 480, 236, 0, 0, 300, 240, 96])

# ---------------------------------------------------------------- qual: process validation
E = "processValidation"
VAL[(E, "title")] = lambda env: TITLES_ADD["processValidation"].split("\n")[env["i"]]
_r(E, "itemId", [0, 0, 0, 0, 3, 3, 2, 2, 1, 0])
_r(E, "lineId", [5, 5, 5, 5, 0, 1, 4, 2, 5, 5])
_tl(E, "validationStage", ["Stage 2 Process Qualification", "Stage 3 Continued Process Verification", "Stage 2 Process Qualification", "Stage 2 Process Qualification",
    "Stage 1 Process Design", "Stage 2 Process Qualification", "Stage 2 Process Qualification", "Stage 3 Continued Process Verification",
    "Stage 2 Process Qualification", "Stage 2 Process Qualification"])
_r(E, "engineeringChangeId", [None, None, 0, 6, 5, None, 2, None, None, 1])
_r(E, "protocolControlledDocumentId", N10)
_r(E, "reportControlledDocumentId", N10)
_tl(E, "plannedLotCount", [3, 12, 3, 3, 3, 3, 3, 12, 3, 3])
_tl(E, "executedLotCount", [3, 9, 3, 3, 3, 0, 3, 10, 3, 1])
_tl(E, "acceptanceCriteriaText", ["Cpk >= 1.67 on bleed screw torque and pressure drop; no leak escapes", "Monthly Cpk >= 1.33 on all critical characteristics",
    "Cpk >= 1.67 on torque and angle; no loose bleed screw in 100 percent check", "Cpk >= 1.67 on pressure drop at 140 bar; master leak detected in every check",
    "Porosity rate below 1 percent on three die-2 lots", "Hardness 85-105 HBW on three charges; temperature uniformity +/- 5 degC",
    "Cpk >= 1.33 on coating thickness 8-16 micrometres", "Monthly Cpk >= 1.33 on bore diameter and mounting hole pitch",
    "Cpk >= 1.67 on bleed screw torque and pressure drop; no leak escapes", "No seal cut; pressure drop Cpk >= 1.67 on three lots"])
_tl(E, "resultText", ["Torque Cpk 1.92, pressure drop Cpk 2.10; criteria met", None, "Torque Cpk 1.84, angle Cpk 1.79; criteria met",
    "Pressure drop Cpk 2.04; master leak detected in all 36 checks; criteria met", "Porosity rate 2.4 percent; gate change not adopted", None,
    "Coating thickness Cpk 1.52; criteria met", None, "Torque Cpk 1.88, pressure drop Cpk 2.02; criteria met", None])
_tl(E, "plannedStartDate", [D0(2026, 4, 6), D0(2026, 7, 1), D0(2026, 9, 15), D0(2026, 6, 15), D0(2026, 5, 4), D0(2026, 9, 28), D0(2026, 7, 13), D0(2026, 7, 1), D0(2026, 5, 18), D0(2026, 9, 15)])
_tl(E, "completedAt", [DT(4, 24, 17, 0), None, DT(9, 18, 16, 0), DT(6, 19, 17, 0), DT(6, 12, 16, 0), None, DT(7, 20, 17, 0), None, DT(5, 27, 17, 0), None])
_r(E, "approvedById", [3, None, None, 3, None, None, 3, None, 3, None])
_tl(E, "approvedAt", [DT(4, 28, 11, 0), None, None, DT(6, 20, 11, 0), None, None, DT(7, 22, 11, 0), None, DT(5, 29, 11, 0), None])
_tl(E, "nextReviewDate", [D0(2027, 4, 28), None, None, D0(2027, 6, 20), None, None, D0(2027, 7, 22), None, D0(2027, 5, 29), None])

# ---------------------------------------------------------------- maint: equipment qualification
E = "equipmentQualification"
_r(E, "equipmentId", [7, 1, 1, 9, 9, 9, 6, 5, 0, 4])
_tl(E, "qualificationPhase", ["Performance Qualification", "Operational Qualification", "Periodic Requalification", "Installation Qualification", "Operational Qualification",
    "Performance Qualification", "Periodic Requalification", "Periodic Requalification", "Periodic Requalification", "Operational Qualification"])
_r(E, "engineeringChangeId", [6, None, None, None, None, None, 0, None, None, None])
_r(E, "protocolControlledDocumentId", N10)
_r(E, "reportControlledDocumentId", N10)
_tl(E, "testCaseCount", [18, 9, 0, 22, 31, 24, 12, 10, 14, 16])
_tl(E, "testFailedCount", [0, 0, 0, 0, 1, 2, 0, 0, 0, 0])
_tl(E, "openDeviationCount", [0, 0, 0, 0, 0, 2, 0, 0, 0, 0])
_r(E, "executedById", [5, 5, 5, 8, 8, 8, 5, 5, 5, 5])
_tl(E, "startedAt", [DT(6, 10, 8, 0), DT(9, 19, 10, 0), None, DT(4, 20, 9, 0), DT(4, 24, 9, 0), DT(9, 15, 10, 0), DT(5, 18, 9, 0), DT(8, 4, 9, 0), DT(7, 13, 9, 0), DT(4, 14, 9, 0)])
_tl(E, "completedAt", [DT(6, 12, 17, 0), None, None, DT(4, 21, 17, 0), DT(4, 28, 17, 0), DT(9, 18, 16, 0), DT(5, 19, 16, 0), DT(8, 5, 16, 0), DT(7, 15, 17, 0), DT(4, 16, 17, 0)])
_r(E, "approvedById", [3, None, None, 3, 3, None, 3, 3, 3, 3])
_tl(E, "approvedAt", [DT(6, 15, 11, 0), None, None, DT(4, 22, 11, 0), DT(4, 30, 11, 0), None, DT(5, 20, 11, 0), DT(8, 7, 11, 0), DT(7, 17, 11, 0), DT(4, 17, 11, 0)])
_r(E, "electronicSignatureId", N10)
_tl(E, "requalificationDueDate", [D0(2027, 6, 15), None, None, None, D0(2027, 4, 30), None, D0(2027, 5, 20), D0(2027, 8, 7), D0(2027, 7, 17), D0(2027, 4, 17)])

# ---------------------------------------------------------------- keys added to existing collections
VAL.update({
 ("equipment", "qualificationStatus"): ["Qualified", "Requalification Due", "Qualified", "Qualified", "Qualified", "Qualified", "Qualified", "Qualified", "Qualified", "Qualified"],
 ("equipment", "requalificationDueDate"): [D0(2027, 7, 17), D0(2026, 9, 20), D0(2027, 3, 12), D0(2027, 2, 8), D0(2027, 4, 17), D0(2027, 8, 7), D0(2027, 5, 20), D0(2027, 6, 15), D0(2027, 1, 25), D0(2027, 4, 30)],
 ("equipment", "cleanStatus"): ["Dirty", "Not Applicable", "Not Applicable", "Clean", "Clean", "Clean Hold Expired", "Clean", "Clean", "Clean", "In Cleaning"],
 ("equipment", "cleanHoldExpiresAt"): [None, None, None, DT(9, 24, 6, 40), None, DT(9, 19, 14, 38), DT(9, 22, 6, 55), DT(9, 23, 15, 24), DT(9, 25, 0, 50), None],
 ("area", "cleanlinessClass"): ["Unclassified", "Unclassified", "Controlled Not Classified", "Controlled Not Classified", "ISO 8", "Controlled Not Classified",
    "Unclassified", "Controlled Not Classified", "Unclassified", "Unclassified"],
 ("area", "environmentallyMonitored"): [False, False, False, True, True, True, False, True, False, False],
 ("area", "gowningRequired"): [False, False, False, False, True, False, False, False, False, False],
 ("lot", "retestDate"): [None, None, None, None, None, D0(2027, 3, 5), D0(2027, 2, 26), None, None, D0(2027, 3, 12)],
 ("productionOrder", "yieldWithinLimits"): [True, None, True, True, None, None, True, False, None, None],
 ("nonconformance", "deviationClass"): ["Major", "Major", "Minor", "Minor", None, "Major", "Critical", "Critical", "Minor", None],
 ("nonconformance", "productImpactText"): ["Castings of die 2 from the lot quarantined; other dies not affected", "One furnace charge affected; used under deviation permit DEV-2026-0007",
    "Two bodies affected and scrapped", "One wash batch affected; re-washed and re-tested", None, "All calipers with seals from lot SEL-011 traced; field action RCL-2026-002",
    "Three units affected; containment at Deccan Motor Company", "Order on hold; units tested at 140 bar since last master check retested", "Twelve calipers affected; re-marked", None],
 ("engineeringChange", "gmpImpact"): [True, True, True, True, True, True, True, True, False, False],
 ("engineeringChange", "validationRequired"): [True, True, True, False, True, True, True, False, False, False],
 ("engineeringChange", "regulatoryImpact"): ["Customer Notification", "Prior Approval", "Prior Approval", "Prior Approval", "Customer Notification", "Prior Approval",
    "Customer Notification", "Prior Approval", "None", "None"],
 ("electronicSignature", "signedRecordVersion"): [3, 2, 5, 1, 4, 2, 3, 2, 6, 1],
 ("electronicSignature", "isFirstSigningInSession"): [True, True, True, False, True, True, False, True, True, False],
 ("auditTrail", "gxpRelevant"): [True] * 10,
 ("user", "lastAccessReviewDate"): [D0(2026, 9, 16)] * 9 + [None],
 ("supplierSuppliedItem", "qualificationStatus"): ["Qualified", "Conditionally Approved", "Qualified", "Qualified", "Qualified", "Qualified", "Qualified", "Qualified", "Qualified", "Qualified"],
 ("supplierSuppliedItem", "qualifiedUntilDate"): [D0(2027, 3, 31), D0(2026, 12, 31), D0(2027, 3, 31), D0(2027, 3, 31), D0(2027, 3, 31), D0(2027, 3, 31), D0(2027, 3, 31), D0(2027, 3, 31), D0(2027, 3, 31), D0(2027, 3, 31)],
 ("recordPolicy", "gxpRelevant"): [True] * 10,
})
REFIDX.update({
 ("equipment", "lastCleaningRecordId"): [8, None, None, 1, 2, 3, 4, 5, 6, 7],
 ("lot", "batchReleaseId"): [1, 0, 2, 3, None, None, None, None, None, None],
 ("productionOrder", "batchRecordReviewId"): list(range(10)),
 ("productionOrder", "lineClearanceId"): [0, 1, 2, 3, 4, 9, 5, 7, 8, None],
 ("nonconformance", "qaApprovedById"): [None, 3, 3, 3, None, None, 3, 3, 3, None],
 ("nonconformance", "riskAssessmentId"): [None, 3, None, None, None, None, None, 4, None, None],
 ("engineeringChange", "riskAssessmentId"): [2, 6, None, None, None, None, 1, None, None, None],
 ("auditTrail", "auditTrailReviewId"): [0, None, 1, 2, None, None, 3, 4, 8, None],
})
def _nc_due(env):
    t = cur(env, "detectedAt")
    return None if t is None else datetime.datetime(t.year, t.month, t.day) + datetime.timedelta(days=30)
def _nc_qa(env):
    if env["i"] not in (1, 2, 3, 6, 7, 8): return None
    t = cur(env, "detectedAt")
    return None if t is None else t + datetime.timedelta(hours=26)
VAL[("nonconformance", "investigationDueDate")] = lambda env: None if env["i"] in (4, 9) else _nc_due(env)
VAL[("nonconformance", "qaApprovedAt")] = _nc_qa
def _manif(env):
    d = env["doc"]
    def g(k):
        v = d.get(k); return v[1] if isinstance(v, tuple) else v
    t = g("signedAt")
    return "%s, %s IST, %s" % (g("userName"), t.strftime("%d %b %Y %H:%M") if t else "", g("signatureMeaningName"))
VAL[("electronicSignature", "signatureManifestationText")] = _manif
def _pwd(env):
    t = cur(env, "passwordChangedAt")
    return None if t is None else datetime.datetime(t.year, t.month, t.day) + datetime.timedelta(days=90)
VAL[("user", "passwordExpiryDate")] = _pwd

AUDIT = {"systemValidation", "systemPeriodicReview", "auditTrailReview", "userAccessReview", "userAccessReviewLine", "batchRecordReview", "batchRecordReviewException",
    "batchRelease", "yieldReconciliation", "lineClearance", "logbookEntry", "cleaningRecord", "environmentalMonitoringResult", "dispenseRecord", "retentionSample",
    "riskAssessment", "productQualityReview", "productRecall", "productRecallLot", "processValidation", "equipmentQualification"}

def _audit(env):
    """createdAt = earliest event date of the document (not before 1 April 2026), updatedAt = latest event date; due and validity dates excluded."""
    d = env["doc"]
    if not d.get("createdAt"): return
    lo, hi = datetime.datetime(2026, 4, 1), datetime.datetime(2026, 10, 1)
    skip = ("createdAt", "updatedAt")
    ev = [v[1] for k, v in d.items() if isinstance(v, tuple) and v[0] == "date" and k not in skip and not k.endswith("Date") and k != "cleanHoldExpiresAt" and lo <= v[1] < hi]
    if not ev: return
    d["createdAt"] = ("date", min(ev)); d["updatedAt"] = ("date", max(ev))

OBS_ADD = """| 12 | GMP_Pharma_01 collections | The ten sample electronic signatures all sign recipes, and no validation protocol, certificate of conformance or review report is among the ten controlled documents | electronicSignatureId and the protocol, report and certificate references of the GMP collections are null in the samples |
| 13 | u_mes_matl_dispenseRecord | No balance or scale is among the ten sample gauges | balanceGaugeId is null in the samples |
| 14 | u_mes_syst_computerisedSystem | No software supplier is among the ten sample suppliers | supplierId is null in the samples |
| 15 | u_mes_bmr_batchRelease, u_mes_qual_retentionSample | Assembly orders produce serialised units without a lot; release and retention of those units refer to the order or the serial number | lotId is null for assembly orders |
"""
def obs(text):
    marker = "\n## How realistic the documents are"
    if OBS_ADD not in text: text = text.replace(marker, OBS_ADD + marker, 1)
    text = text.replace("- Built by the same rules but not read line by line: the remaining collections.",
        "- Written collection by collection for GMP_Pharma_01: the 23 new collections and the 33 added keys (05_generator/gmp01_samples.py).\n- Built by the same rules but not read line by line: the remaining collections.")
    return text

def apply(ns):
    """merge into the namespace of sample_rules.py (after ext_req01_samples.apply)"""
    from sample_universe import MASTER as _M, TITLES as _T
    for k, v in MASTER_ADD.items(): _M[k] = v.strip().split("\n")
    for k, v in TITLES_ADD.items(): _T[k] = v.strip().split("\n")
    ns["RECFMT"].update(RECFMT); ns["STATUSOF"].update(STATUSOF); ns["PARENTIDX"].update(PARENTIDX)
    ns["REFIDX"].update(REFIDX); ns["VAL"].update(VAL); ns["CTXOF"].update(CTXOF)
    for e, f in POST.items():
        ns["POST"][e] = f
    for e in AUDIT:
        old = ns["POST"].get(e)
        ns["POST"][e] = (lambda o: (lambda env: (o(env) if o else None, _audit(env))))(old)
    ns["OBS"] = obs(ns["OBS"])

# ---------------------------------------------------------------- BMR / MMR header records (owner decision of 12 Oct 2026, D057-D059)
import hashlib
MASTER_ADD["masterManufacturingRecord"] = """MMR-5110-10-0100-03|Front brake caliper assembly LH, master manufacturing record version 3
MMR-5110-10-0100-02|Front brake caliper assembly LH, master manufacturing record version 2
MMR-5110-10-0200-02|Front brake caliper assembly RH, master manufacturing record version 2
MMR-5110-20-0110-04|Caliper body LH machined and anodised, master manufacturing record version 4
MMR-5110-20-0105-03|Caliper body casting LH T6, master manufacturing record version 3
MMR-5110-10-0100-04|Front brake caliper assembly LH, master manufacturing record version 4
MMR-5110-20-0105-04|Caliper body casting LH T6, master manufacturing record version 4
MMR-5110-10-0200-03|Front brake caliper assembly RH, master manufacturing record version 3
MMR-5110-20-0110-03|Caliper body LH machined and anodised, master manufacturing record version 3
MMR-5110-10-0100-01|Front brake caliper assembly LH, master manufacturing record version 1"""
STATUSOF["masterManufacturingRecord"] = ["Effective", "Superseded", "Effective", "Effective", "Effective", "In Review", "In Preparation", "Approved", "Superseded", "Superseded"]
E = "masterManufacturingRecord"
VAL[(E, "title")] = lambda env: MASTER_ADD["masterManufacturingRecord"].split("\n")[env["i"]].split("|")[1]
_r(E, "itemId", [0, 0, 1, 2, 3, 0, 3, 1, 2, 0])
_r(E, "itemRevisionId", [1, 1, 3, 5, 7, 1, 7, 3, 4, 0])
_r(E, "productVariantId", [0, 0, 1, None, None, 0, None, 1, None, 0])
_tl(E, "version", [3, 2, 2, 4, 3, 4, 4, 3, 3, 1])
_r(E, "previousMasterManufacturingRecordId", [1, 9, None, 8, None, 0, 4, 2, None, None])
_r(E, "billOfMaterialId", [8, 4, 5, 6, 7, 9, 7, 5, 2, 0])
_r(E, "routingId", [0, 0, 1, 2, 3, 0, 3, 1, 2, 0])
_r(E, "billOfProcessId", [0, 0, 1, 2, 3, 0, 3, 1, 2, 0])
_r(E, "controlPlanId", [0, 0, 1, 2, 3, 9, 3, 1, 2, 4])
_r(E, "inspectionPlanId", [9, 9, 9, 2, 0, 9, 0, 9, 2, 9])
_r(E, "packagingSpecificationId", [4, 2, 5, None, None, 4, None, 7, None, 0])
_r(E, "labelTemplateId", [0, 0, 0, 3, 3, 0, 3, 0, 3, 0])
_r(E, "processValidationId", [0, 0, 8, 6, None, 9, 5, None, None, None])
_r(E, "controlledDocumentId", [9, 9, None, 2, 0, 9, 0, None, 2, 9])
_r(E, "engineeringChangeId", [0, None, None, 2, None, 1, None, 9, None, None])
_tl(E, "changeReasonText", ["Bleed screw torque window revised to 14 +/- 2 N.m with angle monitoring (ECN-2026-0027)",
    "Leak test limits and packing specification revised for Sahyadri Motors", None,
    "Anodising thickness window 8-16 micrometres (ECN-2026-0029)", None,
    "Second source piston seal EPDM grade E70 (ECN-2026-0028)", "T6 profile confirmed after furnace zone 2 repair",
    "Work instruction pictures updated for the RH variant (ECN-2026-0036)", "Machining program and wash cycle aligned with drawing revision C", None])
_tl(E, "standardBatchSize", [480, 480, 480, 240, 240, 480, 240, 480, 240, 480])
_r(E, "unitOfMeasureId", [0] * 10)
_tl(E, "theoreticalQuantity", ["480", "480", "480", "240", "240", "480", "240", "480", "240", "480"])
_tl(E, "lowerLimitPct", ["98.00", "98.00", "98.00", "98.00", "95.00", "98.00", "95.00", "98.00", "98.00", "97.50"])
_tl(E, "upperLimitPct", ["100.00"] * 10)
_tl(E, "effectiveFrom", [D0(2026, 5, 25), D0(2026, 4, 15), D0(2026, 5, 29), D0(2026, 7, 22), D0(2026, 5, 4), None, None, D0(2026, 10, 1), D0(2026, 4, 1), D0(2026, 4, 1)])
_tl(E, "effectiveTo", [None, D0(2026, 5, 24), None, None, None, None, None, None, D0(2026, 7, 21), D0(2026, 4, 14)])
_r(E, "authoredById", [8] * 10)
_r(E, "reviewedById", [3, 3, 3, 3, 3, None, None, 3, 3, 3])
_tl(E, "reviewedAt", [DT(5, 22, 15, 0), DT(4, 13, 15, 0), DT(5, 28, 11, 0), DT(7, 21, 11, 0), DT(4, 30, 15, 0), None, None, DT(9, 23, 15, 0), DT(4, 1, 9, 0), DT(4, 1, 9, 30)])
_r(E, "approvedById", [6, 6, 6, 6, 6, None, None, 6, 6, 6])
_tl(E, "approvedAt", [DT(5, 23, 11, 0), DT(4, 14, 11, 0), DT(5, 28, 16, 0), DT(7, 21, 16, 0), DT(5, 2, 11, 0), None, None, DT(9, 24, 11, 0), DT(4, 1, 11, 0), DT(4, 1, 11, 30)])

PARENTIDX["masterManufacturingRecordRecipe"] = [0, 0, 0, 0, 2, 2, 2, 3, 3, 4]
_r("masterManufacturingRecordRecipe", "recipeId", [5, 6, 7, 8, 6, 7, 9, 2, 4, 0])

_PON = ["PO-1000412", "PO-1000419", "PO-1000426", "PO-1000433", "PO-1000440", "PO-1000447", "PO-1000454", "PO-1000461", "PO-1000468", "PO-1000475"]
RECFMT["batchManufacturingRecord"] = lambda i, j: "BMR-" + _PON[i]
STATUSOF["batchManufacturingRecord"] = ["Approved", "In Execution", "Approved", "Approved", "In Execution", "Open", "Under Review", "Under Review", "Open", "Archived"]
E = "batchManufacturingRecord"
_r(E, "productionOrderId", list(range(10)))
_r(E, "itemId", [0, 1, 2, 3, 0, 2, 3, 0, 2, 0])
_r(E, "lotId", [None, None, 3, 1, None, None, None, None, None, None])
_r(E, "masterManufacturingRecordId", [0, 2, 3, 4, 0, 3, 4, 0, 3, 0])
_tl(E, "masterRecordVersion", [3, 2, 4, 3, 3, 4, 3, 3, 4, 3])
_tl(E, "plannedQuantity", [480, 480, 240, 240, 480, 240, 240, 480, 480, 120])
_r(E, "lineClearanceId", [0, 1, 2, 3, 4, 9, 5, 7, 8, None])
_r(E, "yieldReconciliationId", [0, None, 3, 4, None, None, 6, 7, None, None])
_r(E, "batchRecordReviewId", list(range(10)))
_r(E, "batchReleaseId", [4, 7, 3, 0, 8, None, 6, 5, None, None])
_tl(E, "openedAt", [DT(9, 15, 5, 30), DT(9, 15, 13, 40), DT(9, 16, 22, 0), DT(9, 17, 6, 15), DT(9, 18, 14, 35), DT(9, 19, 22, 5), DT(9, 21, 7, 5), DT(9, 22, 15, 20), DT(9, 24, 23, 35), DT(9, 24, 8, 0)])
_tl(E, "compiledAt", [DT(9, 15, 13, 45), None, DT(9, 17, 6, 20), DT(9, 17, 14, 40), None, None, DT(9, 21, 15, 30), DT(9, 23, 9, 0), None, DT(9, 24, 14, 0)])
_r(E, "exportControlledDocumentId", N10)
_tl(E, "checksumSha256", [hashlib.sha256(("BMR-" + _PON[i] + "-export").encode()).hexdigest() if i in (0, 2, 3, 9) else None for i in range(10)])
_tl(E, "pageCount", [46, None, 38, 52, None, None, None, None, None, 6])
_r(E, "exportedById", [3, None, 3, 3, None, None, None, None, None, 3])
_tl(E, "exportedAt", [DT(9, 16, 10, 45), None, DT(9, 17, 15, 20), DT(9, 18, 11, 40), None, None, None, None, None, DT(9, 24, 16, 10)])
_tl(E, "archivedAt", [None] * 9 + [DT(9, 24, 16, 15)])
AUDIT.add("batchManufacturingRecord")

OBS_ADD = OBS_ADD + """| 16 | u_mes_bmr_batchManufacturingRecord | No exported batch record is among the ten sample controlled documents | exportControlledDocumentId is null; the checksum, page count and export time of the four exported records are filled |
| 17 | u_mes_mmr_masterManufacturingRecord | Packaging specifications in the samples all carry the LH assembly as item | RH and body records reference the nearest specification or none |
"""
