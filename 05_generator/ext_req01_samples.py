"""Sample-data rules for the collections and keys added by MES_ExternalRequirement_01 (D036-D042).
Merged into sample_rules.py by apply(); the same 10-documents-per-collection universe, same IDs and names.
Index conventions (see sample_universe.PROC): process rows 0-9 = OP010 casting ... OP100 final inspection.
Users: 0 Sunil Jadhav, 1 Kavita Bhosale, 2 Deepak Gaikwad (operators), 3 Anita Kulkarni (quality), 4 Rajesh Patil (supervisor),
5 Imran Shaikh (maintenance), 6 Meera Deshpande (manager), 7 Vikram Pawar (stores), 8 Sneha Joshi, 9 MES System."""
import datetime
from sample_universe import MASTER, TITLES

def DT(m, d, h, mi, s=0): return datetime.datetime(2026, m, d, h, mi, s)
def M(minutes): return datetime.timedelta(minutes=minutes)
def raw(env, ent, idx, key):
    """value of key in document idx of entity ent (dates as datetime, numbers as text/number)"""
    v = env["docs_of"](ent)[idx][key]
    return v[1] if isinstance(v, tuple) else v
def cur(env, key):
    """value of an earlier key of the document being built"""
    v = env["doc"][key]
    if v is None or not isinstance(v, (tuple, str, bool, int, float)): return None
    return v[1] if isinstance(v, tuple) else v
def plus(t, minutes): return None if t is None else t + M(minutes)
def by_i(lst): return lambda env: lst[env["i"]]

MASTER_ADD = {
"interlockRule": """ILR-HOLD-001|Hold check at operation start
ILR-SEQ-001|Routing sequence check, front caliper assembly line
ILR-SKL-001|Skill check at station login
ILR-DUP-001|Duplicate serial check at laser marking
ILR-LOT-001|Lot release and expiry check at material issue
ILR-NOK-001|Previous NOK result blocks laser marking
ILR-TQL-001|Tool life check, nutrunner socket
ILR-CAL-001|Gauge calibration check at inspection accept
ILR-VAR-001|Variant check at piston and seal assembly start
ILR-ENV-001|Ambient light check, final inspection vision""",
"escalationRule": """ESC-BRKDN-CRIT|Critical breakdown, assembly line
ESC-BRKDN-STD|Breakdown, all lines
ESC-QUAL-ANDON|Quality andon not acknowledged
ESC-INTERLOCK|Interlock block not cleared
ESC-ALARM-SAFE|Safety alarm restart authorisation
ESC-LPA-MISSED|Missed layered process audit
ESC-OUTPUT-GAP|Output behind plan
ESC-KPI-ALERT|KPI alert on OEE and rejects
ESC-MAT-SHORT|Line-side material shortage
ESC-NCR-OPEN|Nonconformance open beyond 24 hours""",
"alertRule": """ALR-OEE-ASY01|OEE below 75 percent on assembly line 1
ALR-GAP-ASY01|Output more than 30 units behind plan
ALR-REJ-LKT01|Leak test reject rate above 1.5 percent
ALR-DT-GDC01|Downtime above 20 minutes in one hour, casting
ALR-PRESS-LKT01|High-pressure stage test pressure drift
ALR-TORQ-TRQ01|Final torque mean drifting towards lower limit
ALR-SPC-CNC01|SPC rule violation, piston bore diameter
ALR-STOCK-SEAL|Piston seal line-side cover below 45 minutes
ALR-LUX-FIN01|Ambient light outside 800-1200 lux at final inspection
ALR-ANOM-NR1|Nutrunner anomaly score above 0.8""",
"analyticsModel": """AIM-VIS-BOOT-1.3|Dust boot seating and cap presence classifier
AIM-VIS-BOOT-1.2|Dust boot seating and cap presence classifier
AIM-LKT-PRED-0.9|Leak test failure predictor
AIM-OEE-FC-2.1|Assembly line OEE forecast
AIM-NR-ANOM-1.0|Nutrunner rundown anomaly detector
AIM-MNT-RUL-1.4|Leak tester test seal remaining life
AIM-DEM-FC-1.1|Line-side component demand forecast
AIM-RCP-OPT-0.7|Anodising current density optimiser
AIM-OPR-RISK-0.5|Operator error risk indicator
AIM-ASG-REC-0.6|Station assignment recommender""",
"curveEnvelope": """ENV-OP060-PST-PRESS-02|Piston press-in force, front caliper LH
ENV-OP060-BOOT-SEAT-01|Dust boot seating force, front caliper
ENV-OP070-BLEED-TA-04|Bleed screw M10 torque-angle, LH
ENV-OP070-BLEED-TA-04R|Bleed screw M10 torque-angle, RH
ENV-OP070-GPIN-TA-01|Guide pin bolt M8 torque-angle
ENV-OP080-DECAY-140-02|Pressure decay at 140 bar
ENV-OP080-DECAY-5-02|Pressure decay at 5 bar
ENV-OP060-PST-PRESS-01|Piston press-in force, front caliper LH
ENV-OP060-PST-PRESS-02R|Piston press-in force, front caliper RH
ENV-OP070-BLEED-TA-03|Bleed screw M10 torque-angle, LH""",
"auditSchedule": """LPA-L1-ASY-01|LPA layer 1, piston and seal assembly, every shift
LPA-L1-TRQ-01|LPA layer 1, bleed screw torque, every shift
LPA-L1-LKT-01|LPA layer 1, leak test, every shift
LPA-L2-ASY-01|LPA layer 2, front caliper assembly line, daily
LPA-L2-MC-01|LPA layer 2, machining line, daily
LPA-L2-GDC-01|LPA layer 2, casting line, daily
LPA-L3-ASY-01|LPA layer 3, front caliper assembly line, weekly
LPA-L3-FDY|LPA layer 3, foundry, weekly
LPA-L3-SF|LPA layer 3, surface treatment, weekly
PRD-AUD-FBC|Product audit, front caliper LH, monthly""",
"alarmDefinition": """ALD-GDC-A2031|Die temperature upper half above high limit
ALD-HTF-A2031|Solution furnace zone temperature below low limit
ALD-HMC-A2031|Through-spindle coolant pressure below low limit
ALD-WSH-A2031|Wash bath temperature below low limit
ALD-ANO-A2031|Anodising bath temperature above high limit
ALD-PRS-A2031|Press stroke end position below low limit
ALD-NR-A2031|Final torque below low limit on three consecutive cycles
ALD-LKT-A2031|High-pressure stage test pressure below low limit
ALD-LSR-A2031|Marking head temperature above high limit
ALD-VIS-A2031|Inspection cell air pressure below low limit""",
"recordPolicy": """RPO-u_mes_plan_operationExecution|Operation executions
RPO-u_mes_qual_inspectionResult|Inspection results
RPO-u_mes_trac_asBuiltRecord|As-built records
RPO-u_mes_perf_torqueResult|Torque results
RPO-u_mes_perf_leakTestResult|Leak test results
RPO-u_mes_plan_interlockEvent|Interlock events
RPO-u_mes_prod_recipe|Recipes
RPO-u_mes_qual_nonconformance|Nonconformances
RPO-u_mes_mast_user|Users
RPO-u_mes_perf_processReading|Process readings""",
"savedView": """VIEW-10045-001|OEE by shift, assembly line 1, last 7 days
VIEW-10045-002|Downtime Pareto, assembly line 1, this week
VIEW-10019-001|Best and worst lines by OEE, this month
VIEW-10087-001|Leak test rejects by variant
VIEW-10087-002|Open nonconformances older than 24 hours
VIEW-10112-001|MTBF and MTTR by equipment, this quarter
VIEW-10150-001|Line-side stock cover, assembly line 1
VIEW-QUAL-001|Defects by first-fail station and 4M category
VIEW-PROD-001|Hourly output against plan, all lines
VIEW-MAINT-001|Overdue preventive maintenance""",
"replenishmentRule": """RPL-5110-30-0010-LS-ASY-01|Piston to assembly line side
RPL-5110-30-0020-LS-ASY-01|Piston seal to assembly line side
RPL-5110-30-0030-LS-ASY-01|Dust boot to assembly line side
RPL-5110-30-0040-LS-ASY-01|Bleed screw to assembly line side
RPL-5110-30-0050-LS-ASY-01|Guide pin to assembly line side
RPL-5110-20-0110-LS-ASY-01|Machined caliper body to assembly line side
RPL-5110-20-0105-LS-MC-01|Caliper body casting to machining line side
RPL-RM-A356-LS-FDY-01|Aluminium ingot to foundry line side
RPL-5110-10-0100-DSP-BAY-01|Front caliper LH to dispatch bay
RPL-5110-10-0200-DSP-BAY-01|Front caliper RH to dispatch bay""",
}
TITLES_ADD = {
"traceInvestigation": """Forward trace, seal lot L260905-SEL-011 after seal cut at assembly
Reverse trace, serial VB26267A00301 for missing bleed screw cap complaint
Forward trace, bleed screw lot L260901-BLS-022 after low torque
Reverse trace, scrapped unit U260922B0275 with leak at piston seal
Forward trace, casting lot L260915-GDC-014 after shrinkage porosity
Forward trace, furnace charge L260915-HT-002 after low hardness
Reverse trace, unit U260915A0184 on quality hold
Forward trace, piston lot L260905-PST-007, supplier audit sample
Reverse trace, serial VB26258B00210 for customer audit
Forward trace, anodising load L260917-ANO-001 after low coating thickness""",
"simulationStudy": """Leak test stabilisation time 5.0 s to 4.0 s, what-if on cycle time and escape risk
Anodising current density by rack count, recipe A12 optimisation
Bleed screw torque window 14 +/- 2 N.m, angle monitoring study
Line-side supermarket size for piston seals after e-Kanban
Assembly line 1 balancing with second leak tester
Casting die temperature setpoint 400 to 395 degC, porosity risk
Finished goods buffer for Sahyadri Motors weekly schedule
Laser marking speed increase for grade A codes
Leak tester auto-calibration baseline propagation to tester 2
Press force window review after seal supplier change""",
"equipmentLifecycleEvent": """Commissioning of DC nutrunner station 1
Overhaul of gravity die casting machine 1 tilt hydraulics
Health assessment, solution furnace after zone 2 heater failure
Refurbishment of horizontal machining center 1 spindle
Upgrade of leak tester 1 with 160 bar booster
Health assessment, pressure leak tester 1
Replacement recommendation, aqueous spray washer 1 pump
Relocation of laser marker 1 to assembly line 1
Commissioning of final inspection vision station
Health assessment, anodising line rectifier""",
}

RECFMT = {}
def _fmt(prefix, days, start):
    return lambda i, j: "%s-202609%02d-%05d" % (prefix, days[i], start + 7 * i)
RECFMT["operatorSession"] = _fmt("OSN", [15, 15, 15, 15, 18, 18, 22, 22, 22, 24], 41)
RECFMT["documentAcknowledgement"] = _fmt("ACK", [15, 15, 15, 15, 18, 18, 22, 22, 24, 24], 118)
RECFMT["interlockEvent"] = _fmt("ILK", [15, 15, 22, 21, 19, 22, 24, 19, 24, 18], 207)
RECFMT["recipeDownload"] = _fmt("RDL", [17, 16, 15, 15, 18, 22, 22, 24, 15, 18], 31)
RECFMT["setupVerification"] = _fmt("SUV", [15, 15, 15, 18, 22, 22, 16, 17, 19, 24], 12)
RECFMT["exposureTimer"] = _fmt("EXT", [15, 15, 16, 19, 18, 21, 22, 23, 24, 24], 3)
RECFMT["traceInvestigation"] = lambda i, j: "TRC-202609%02d-%03d" % ([19, 24, 21, 22, 17, 15, 19, 23, 24, 18][i], 11 + i)
RECFMT["measurementCurve"] = _fmt("CRV", [15, 15, 15, 15, 15, 15, 18, 18, 22, 22], 1840)
RECFMT["measurementCurvePoint"] = lambda i, j: "CRV-20260915-01840-%04d" % (1 + i)
RECFMT["defectRecord"] = _fmt("DFR", [15, 22, 15, 16, 17, 15, 17, 18, 24, 24], 230)
RECFMT["lossSummary"] = lambda i, j: ["LSS-20260915-ASY-01-A-MATL-ASY-01", "LSS-20260915-ASY-01-B-TOOL-TRQ-01", "LSS-20260915-ASY-01-B-MATL-ASY-01", "LSS-20260917-GDC-01-A-MECH-GDC-01",
    "LSS-20260917-GDC-01-A-ELEC-HT-01", "LSS-20260918-ASY-01-B-TOOL-LKT-01", "LSS-20260922-ASY-01-B-TOOL-LKT-01", "LSS-20260922-ASY-01-B-MATL-ASY-01", "LSS-20260924-MC-01-C-TOOL-CNC-01", "LSS-20260924-FIP-01-A-ELEC-FIN-01"][i]
RECFMT["workCenterPerformance"] = lambda i, j: ["WCP-2026091506-ASY-01", "WCP-2026091506-TRQ-01", "WCP-2026091506-LKT-01", "WCP-2026091514-TRQ-01", "WCP-2026091514-LKT-01",
    "WCP-2026091815-LKT-01", "WCP-2026092216-LKT-01", "WCP-2026092216-TRQ-01", "WCP-2026092408-FIN-01", "WCP-2026092408-LSR-01"][i]
RECFMT["operatorPerformance"] = lambda i, j: ["OPF-20260915-10344-ASY-01", "OPF-20260915-10402-TRQ-01", "OPF-20260915-10231-TRQ-01", "OPF-20260915-10344-TRQ-01", "OPF-20260918-10402-LKT-01",
    "OPF-20260918-10231-LKT-01", "OPF-20260922-10344-LKT-01", "OPF-20260922-10402-LKT-01", "OPF-20260924-10231-FIN-01", "OPF-20260917-10231-GDC-01"][i]
RECFMT["materialDemandForecast"] = lambda i, j: ["MDF-20260924-ASY-01-5110-30-0020-08", "MDF-20260924-ASY-01-5110-30-0020-09", "MDF-20260924-ASY-01-5110-30-0010-08", "MDF-20260924-ASY-01-5110-30-0030-08",
    "MDF-20260924-ASY-01-5110-30-0040-08", "MDF-20260924-ASY-01-5110-30-0050-08", "MDF-20260924-ASY-01-5110-20-0110-08", "MDF-20260922-ASY-01-5110-30-0020-16", "MDF-20260922-ASY-01-5110-30-0030-16", "MDF-20260922-ASY-01-5110-30-0010-16"][i]
RECFMT["sparePartTransaction"] = _fmt("SPT", [15, 15, 16, 17, 18, 19, 21, 22, 23, 24], 88)
RECFMT["reliabilitySummary"] = lambda i, j: ["REL-202609-" + x for x in ["GDC-01-M1", "HT-01-F1", "CNC-01-H1", "WSH-01-W1", "ANO-01-L1", "ASY-01-P1", "TRQ-01-N1", "LKT-01-T1", "LSR-01-L1", "FIN-01-V1"]][i]
RECFMT["equipmentLifecycleEvent"] = lambda i, j: ["ELE-TRQ-01-N1-001", "ELE-GDC-01-M1-004", "ELE-HT-01-F1-006", "ELE-CNC-01-H1-003", "ELE-LKT-01-T1-002", "ELE-LKT-01-T1-003", "ELE-WSH-01-W1-005", "ELE-LSR-01-L1-002", "ELE-FIN-01-V1-001", "ELE-ANO-01-L1-007"][i]
RECFMT["modelPrediction"] = _fmt("PRD", [15, 15, 18, 18, 21, 22, 22, 24, 24, 24], 5112)
RECFMT["simulationStudy"] = lambda i, j: "SIM-2026-%03d" % (14 + i)
RECFMT["backupRun"] = lambda i, j: ["BKP-20260915-01", "BKP-20260916-01", "BKP-20260917-01", "BKP-20260918-01", "BKP-20260919-01", "BKP-20260920-01", "BKP-20260920-02", "BKP-20260921-01", "BKP-20260922-01", "BKP-20260927-01"][i]

STATUSOF = {
 "operatorSession": ["Closed"] * 8 + ["Rejected", "Active"],
 "documentAcknowledgement": ["Acknowledged", "Acknowledged", "Acknowledged", "Superseded", "Acknowledged", "Acknowledged", "Acknowledged", "Acknowledged", "Acknowledged", "Acknowledged"],
 "interlockEvent": ["Cleared", "Blocked", "Blocked", "Overridden", "Blocked", "Blocked", "Cleared", "Blocked", "Overridden", "Blocked"],
 "recipeDownload": ["Verified"] * 5 + ["Rejected"] + ["Verified"] * 4,
 "setupVerification": ["Passed", "Passed", "Failed", "Passed", "Passed", "Passed", "Passed", "Passed", "In Progress", "Overridden"],
 "exposureTimer": ["Consumed", "Consumed", "Expired", "Reset", "Consumed", "Paused", "Consumed", "Running", "Running", "Paused"],
 "traceInvestigation": ["Closed", "Completed", "Closed", "Completed", "Closed", "Closed", "Completed", "Completed", "Running", "Closed"],
 "curveEnvelope": ["Released"] * 7 + ["Obsolete", "Released", "Obsolete"],
 "measurementCurve": ["Recorded"] * 9 + ["Voided"],
 "defectRecord": ["Open", "Scrapped", "Open", "Scrapped", "Scrapped", "Accepted", "Closed", "Accepted", "Reworked", "Reworked"],
 "auditSchedule": ["Active"] * 9 + ["Inactive"],
 "alarmDefinition": ["Active"] * 10,
 "lossSummary": ["Calculated"] * 9 + ["Recalculated"],
 "workCenterPerformance": ["Calculated"] * 10,
 "operatorPerformance": ["Calculated"] * 9 + ["Recalculated"],
 "sparePartTransaction": ["Posted"] * 8 + ["Reversed", "Posted"],
 "reliabilitySummary": ["Calculated"] * 10,
 "equipmentLifecycleEvent": ["Approved", "Approved", "Recorded", "Approved", "Approved", "Recorded", "Recorded", "Approved", "Approved", "Recorded"],
 "interlockRule": ["Active"] * 10,
 "escalationRule": ["Active"] * 10,
 "alertRule": ["Active"] * 9 + ["Inactive"],
 "analyticsModel": ["Released", "Retired", "Released", "Released", "Released", "Released", "Released", "In Preparation", "In Preparation", "In Preparation"],
 "modelPrediction": ["Verified", "Actioned", "Verified", "Open", "Actioned", "Open", "Verified", "Open", "Actioned", "Open"],
 "simulationStudy": ["Rolled Out", "Approved", "Completed", "Rolled Out", "Completed", "Rejected", "Completed", "Planned", "Approved", "Completed"],
 "recordPolicy": ["Active"] * 10,
 "savedView": ["Active"] * 10,
 "backupRun": ["Succeeded"] * 4 + ["Failed"] + ["Succeeded"] * 5,
 "replenishmentRule": ["Active"] * 9 + ["Inactive"],
 "materialDemandForecast": ["Calculated", "Calculated", "Calculated", "Calculated", "Calculated", "Calculated", "Calculated", "Superseded", "Superseded", "Superseded"],
}

PARENTIDX = {
 "roleRequiredSkill": [0, 0, 0, 1, 1, 2, 2, 4, 6, 8],
 "recipeProductVariant": [6, 6, 6, 7, 7, 8, 8, 8, 9, 9],
 "recipeControlledDocument": [0, 1, 2, 3, 4, 6, 6, 7, 8, 9],
 "workInstructionProductVariant": [5, 5, 6, 6, 7, 7, 8, 8, 9, 9],
 "setupVerificationItem": [0, 0, 0, 1, 1, 2, 2, 3, 4, 5],
 "traceInvestigationResult": [0, 0, 0, 1, 1, 2, 2, 3, 4, 9],
 "characteristicPosition": [4, 4, 4, 4, 4, 2, 2, 2, 0, 0],
 "curveEnvelopeWindow": [0, 0, 0, 2, 2, 2, 5, 5, 1, 4],
 "inspectionPlanProductVariant": [5, 5, 6, 6, 7, 7, 8, 8, 9, 9],
 "maintenanceWorkOrderTask": [7, 7, 7, 0, 0, 3, 3, 6, 6, 9],
 "escalationRuleLevel": [0, 0, 0, 1, 1, 2, 2, 3, 5, 6],
 "statusTransitionRole": [0, 1, 2, 3, 3, 4, 5, 5, 6, 9],
 "storageLocationAllowedItem": [5, 5, 5, 5, 5, 4, 3, 0, 7, 6],
}
REFIDX = {}
VAL = {}
POST = {}
CTXOF = {}

# ---------------------------------------------------------------- mast
REFIDX[("roleRequiredSkill", "requiredSkillId")] = [5, 6, 7, 2, 0, 5, 7, 9, 6, 8]
VAL[("roleRequiredSkill", "minimumLevel")] = [2, 2, 3, 3, 3, 3, 4, 3, 2, 3]

# ---------------------------------------------------------------- prod
REFIDX[("recipeProductVariant", "productVariantId")] = [0, 1, 2, 0, 1, 0, 2, 4, 1, 3]
REFIDX[("recipeControlledDocument", "controlledDocumentId")] = [0, 1, 2, 3, 4, 6, 8, 7, 9, 8]
VAL[("recipeControlledDocument", "fileRole")] = ["Product Drawing", "Process Specification", "Product Drawing", "Process Specification", "Process Specification",
    "Reference Curve", "Process Specification", "Verification Record", "Product Drawing", "Process Specification"]
REFIDX[("workInstructionProductVariant", "productVariantId")] = [0, 2, 0, 1, 0, 2, 0, 2, 0, 4]

# ---------------------------------------------------------------- plan: operator sessions (session k belongs to operation execution _OX[k])
_OX = [1, 2, 3, 4, 5, 6, 7, 8, None, 9]
_SWC = [5, 6, 6, 6, 7, 7, 7, 7, 7, 9]
_SPO = [0, 0, 1, 1, 4, 4, 7, 7, 7, 9]
_SUSER = [1, 2, 0, 1, 2, 0, 1, 2, 5, 0]
_SSHIFT = [1, 2, 0, 1, 2, 0, 1, 2, 1, 0]
def _login(env):
    k = _OX[env["i"]]
    if k is None: return DT(9, 22, 15, 48)
    return raw(env, "operationExecution", k, "startedAt") - M(25)
def _logout(env):
    k = _OX[env["i"]]
    if env["status"] != "Closed": return None
    return raw(env, "operationExecution", k, "completedAt") + M([175, 160, 170, 165, 180, 172, 150, 155, 0, 0][env["i"]])
REFIDX.update({("operatorSession", "userId"): _SUSER, ("operatorSession", "workCenterId"): _SWC, ("operatorSession", "equipmentId"): _SWC,
    ("operatorSession", "shiftId"): _SSHIFT, ("operatorSession", "productionOrderId"): _SPO, ("operatorSession", "interlockEventId"): [None] * 8 + [2, None]})
VAL.update({("operatorSession", "loginAt"): _login, ("operatorSession", "logoutAt"): _logout,
    ("operatorSession", "productionDate"): lambda env: datetime.datetime(_login(env).year, _login(env).month, _login(env).day),
    ("operatorSession", "authenticationMethod"): ["Badge", "Badge", "Biometric", "Badge", "Badge", "Badge", "Badge", "Badge", "Badge", "Badge And PIN"],
    ("operatorSession", "logoutReason"): ["Shift End", "Operator Logout", "Shift End", "Shift End", "Operator Logout", "Shift End", "Timeout", "Shift End", None, None],
    ("operatorSession", "skillVerified"): [True] * 8 + [False, True], ("operatorSession", "trainingVerified"): [True] * 10,
    ("operatorSession", "clientWorkstation"): ["PN1-ASY01-HMI-01", "PN1-TRQ01-HMI-01", "PN1-TRQ01-HMI-01", "PN1-TRQ01-HMI-01", "PN1-LKT01-HMI-01", "PN1-LKT01-HMI-01", "PN1-LKT01-HMI-01", "PN1-LKT01-HMI-01", "PN1-LKT01-HMI-01", "PN1-FIN01-HMI-01"]})
REFIDX[("operationExecution", "operatorSessionId")] = [None, 0, 1, 2, 3, 4, 5, 6, 7, 9]

# ---------------------------------------------------------------- plan: document acknowledgements
_ADOC = [("workInstruction", 5), ("workInstruction", 6), ("workInstruction", 6), ("workInstruction", 6), ("workInstruction", 7), ("workInstruction", 7), ("recipe", 7), ("workInstruction", 7), ("workInstruction", 8), ("workInstruction", 9)]
_ASESS = [0, 1, 2, 3, 4, 5, 6, 7, None, 9]
def _ackat(env):
    s = _ASESS[env["i"]]
    if s is None: return DT(9, 24, 0, 22)
    k = _OX[s]; return raw(env, "operationExecution", k, "startedAt") - M(22)
REFIDX.update({("documentAcknowledgement", "userId"): [1, 2, 0, 1, 2, 0, 1, 2, 2, 0], ("documentAcknowledgement", "workCenterId"): [5, 6, 6, 6, 7, 7, 7, 7, 8, 9],
    ("documentAcknowledgement", "productVariantId"): [0, 0, 1, 1, 0, 0, 2, 2, None, 0], ("documentAcknowledgement", "productionOrderId"): [0, 0, 1, 1, 4, 4, 7, 7, None, 9],
    ("documentAcknowledgement", "shiftId"): [1, 2, 0, 1, 2, 0, 1, 2, 2, 0], ("documentAcknowledgement", "operatorSessionId"): _ASESS,
    ("documentAcknowledgement", "electronicSignatureId"): [None] * 6 + [7, None, None, None]})
VAL.update({("documentAcknowledgement", "acknowledgedAt"): _ackat,
    ("documentAcknowledgement", "documentVersion"): lambda env: str(raw(env, _ADOC[env["i"]][0], _ADOC[env["i"]][1], "version")),
    ("documentAcknowledgement", "acknowledgementType"): ["Shift Start", "Shift Start", "Revision Re-acknowledgement", "First Read", "Shift Start", "Revision Re-acknowledgement", "Revision Re-acknowledgement", "Shift Start", "First Read", "Shift Start"],
    ("documentAcknowledgement", "method"): ["Badge Scan", "Touch Confirmation", "Touch Confirmation", "Touch Confirmation", "Badge Scan", "Touch Confirmation", "Electronic Signature", "Badge Scan", "AR Confirmation", "Badge Scan"]})
def _poly(entity_list):
    def post(env):
        ent, idx = entity_list[env["i"]]
        d = env["doc"]
        if ent is None:
            d["relatedCollectionName"] = None; d["relatedEntityId"] = None; d["relatedEntityName"] = None; return
        t = env["identity"](env["byent"][ent], idx)
        d["relatedCollectionName"] = env["byent"][ent]["collection"]; d["relatedEntityId"] = t[0]; d["relatedEntityName"] = t[2]
    return post
POST["documentAcknowledgement"] = _poly(_ADOC)

# ---------------------------------------------------------------- syst: interlock rules
_RTYPE = ["Hold Check", "Sequence Check", "Skill Check", "Duplicate Serial", "Lot Release Check", "NOK Result", "Tool Life", "Calibration Check", "Variant Check", "Environment Check"]
VAL.update({("interlockRule", "name"): lambda env: MASTER["interlockRule"][env["i"]].split("|")[1], ("interlockRule", "ruleType"): _RTYPE,
    ("interlockRule", "transactionPoint"): ["Operation Start", "Operation Start", "Login", "Operation Complete", "Material Issue", "Operation Start", "Operation Start", "Inspection Accept", "Operation Start", "Inspection Accept"],
    ("interlockRule", "enforcementMode"): ["Block"] * 9 + ["Warning"],
    ("interlockRule", "overrideAllowed"): [False, True, False, False, False, False, True, False, True, True],
    ("interlockRule", "overrideRequiresSignature"): [False, True, False, False, False, False, False, False, True, False],
    ("interlockRule", "overrideRequiresReasonCode"): [False, True, False, False, False, False, True, False, True, True],
    ("interlockRule", "messageText"): ["Unit, lot or order is on quality hold; operation not allowed",
        "Previous routing step not completed; scan the unit at the missing station first",
        "No valid certification for the skill required at this station; login refused",
        "Serial already issued; marking stopped",
        "Lot is on hold, rejected or expired; issue not allowed",
        "Unit has a NOK result at an earlier test; marking not allowed",
        "Tool has reached its life limit; change the tool and verify",
        "Gauge calibration overdue or failed; result cannot be accepted",
        "Scanned body or component does not match the variant of the order",
        "Ambient light outside 800-1200 lux; vision result needs confirmation"],
    ("interlockRule", "validFrom"): [DT(4, 1, 0, 0)] * 6 + [DT(6, 1, 0, 0), DT(4, 1, 0, 0), DT(7, 15, 0, 0), DT(9, 1, 0, 0)], ("interlockRule", "validTo"): [None] * 10})
REFIDX.update({("interlockRule", "lineId"): [None, 5, None, None, None, 5, 5, None, 5, 6], ("interlockRule", "workCenterId"): [None, None, None, 8, None, 8, 6, None, 5, 9],
    ("interlockRule", "operationId"): [None, None, None, 8, None, 8, 6, None, 5, 9], ("interlockRule", "itemId"): [None] * 8 + [0, None],
    ("interlockRule", "overrideRoleId"): [None, 3, None, None, None, None, 3, None, 3, 4], ("interlockRule", "escalationRuleId"): [3, 3, 3, 3, 8, 3, 0, 3, 3, 2]})

# ---------------------------------------------------------------- plan: interlock events
_IR = [8, 1, 2, 6, 4, 5, 3, 0, 9, 7]
_ITIME = [DT(9, 15, 14, 9), DT(9, 15, 14, 41), DT(9, 22, 15, 48), DT(9, 21, 7, 38), DT(9, 19, 23, 40), DT(9, 22, 16, 12), DT(9, 24, 0, 31), DT(9, 19, 23, 52), DT(9, 24, 8, 29), DT(9, 18, 15, 21)]
REFIDX.update({("interlockEvent", "interlockRuleId"): _IR, ("interlockEvent", "workCenterId"): [5, 7, 7, 6, 5, 8, 8, 6, 9, 4], ("interlockEvent", "equipmentId"): [5, 7, 7, 6, 5, 8, 8, 6, 9, 4],
    ("interlockEvent", "productionOrderId"): [1, 1, 7, None, None, 7, 9, 0, 9, None], ("interlockEvent", "wipUnitId"): [2, 3, None, None, None, 7, 8, 0, 8, None],
    ("interlockEvent", "lotId"): [None, None, None, None, 5, None, None, None, None, 3], ("interlockEvent", "operationExecutionId"): [None] * 10,
    ("interlockEvent", "shiftId"): [1, 1, 1, 0, 2, 1, 2, 2, 0, 1], ("interlockEvent", "operatorUserId"): [1, 0, 5, 0, 7, 1, 2, 2, 0, 3],
    ("interlockEvent", "overrideReasonCodeId"): [None, None, None, 6, None, None, None, None, 9, None], ("interlockEvent", "overrideById"): [None, None, None, 4, None, None, None, None, 3, None],
    ("interlockEvent", "electronicSignatureId"): [None] * 10, ("interlockEvent", "notificationId"): [None, None, None, None, 5, None, None, None, None, 4]})
VAL.update({("interlockEvent", "ruleType"): [_RTYPE[r] for r in _IR], ("interlockEvent", "raisedAt"): _ITIME,
    ("interlockEvent", "productionDate"): [DT(9, 15, 0, 0), DT(9, 15, 0, 0), DT(9, 22, 0, 0), DT(9, 21, 0, 0), DT(9, 19, 0, 0), DT(9, 22, 0, 0), DT(9, 23, 0, 0), DT(9, 19, 0, 0), DT(9, 24, 0, 0), DT(9, 18, 0, 0)],
    ("interlockEvent", "foundValueText"): ["FBC-LH-STD body 5110-20-0110 scanned", "Last completed step 60", "LEAK-TEST-OP certification expired on 10 Sep 2026", "Socket SKT-10-0007 at 100,000 cycles",
        "Lot L260905-SEL-011 status On Hold", "Leak test verdict Fail on 22 Sep 2026 16:04", "VB26267A00288 already issued", "Unit U260915A0184 on hold HLD-2026-000021", "780 lux", "Gauge G-CT-002 calibration overdue since 12 Sep 2026"],
    ("interlockEvent", "expectedValueText"): ["FBC-RH-STD body", "Step 70 completed", "Valid LEAK-TEST-OP certification, level 3", "Below 100,000 cycles", "Available, released lot", "Pass", "Unused serial", "No active hold", "800-1200 lux", "Valid calibration"],
    ("interlockEvent", "messageText"): lambda env: MASTER_ROWS_MSG[_IR[env["i"]]],
    ("interlockEvent", "overrideComment"): [None, None, None, "Last 40 units before planned socket change at shift end; torque verified with analyser", None, None, None, None, "Overhead lamp replaced at break; vision results reviewed by quality", None],
    ("interlockEvent", "overrideAt"): [None, None, None, DT(9, 21, 7, 44), None, None, None, None, DT(9, 24, 8, 33), None],
    ("interlockEvent", "clearedAt"): [DT(9, 15, 14, 16), None, None, None, None, None, DT(9, 24, 0, 37), None, None, None]})
MASTER_ROWS_MSG = VAL[("interlockRule", "messageText")]
POST["interlockEvent"] = _poly([(None, 0), ("wipUnit", 3), ("operatorSession", 8), ("tool", 6), ("lot", 5), ("wipUnit", 7), ("serialNumber", 8), ("wipUnit", 0), ("workCenter", 9), ("gauge", 4)])
VAL[("operationExecution", "interlockEventCount")] = [0] * 10

# ---------------------------------------------------------------- plan: recipe downloads
_RD = [0, 2, 6, 6, 7, 7, 7, 8, 9, 4]
_RDT = [DT(9, 17, 6, 40), DT(9, 16, 22, 20), DT(9, 15, 5, 52), DT(9, 15, 14, 8), DT(9, 18, 14, 58), DT(9, 22, 15, 50), DT(9, 22, 15, 56), DT(9, 24, 8, 21), DT(9, 15, 14, 11), DT(9, 18, 14, 47)]
REFIDX.update({("recipeDownload", "recipeId"): _RD, ("recipeDownload", "equipmentId"): [0, 2, 6, 6, 7, 7, 7, 8, 8, 4], ("recipeDownload", "workCenterId"): [0, 2, 6, 6, 7, 7, 7, 8, 8, 4],
    ("recipeDownload", "productionOrderId"): [3, 2, 0, 1, 4, 7, 7, 9, 1, None], ("recipeDownload", "productVariantId"): [None, None, 0, 1, 0, 2, 2, 0, 1, None],
    ("recipeDownload", "requestedById"): [9, 9, 9, 4, 9, 9, 1, 9, 4, 6], ("recipeDownload", "interlockEventId"): [None] * 10})
VAL.update({("recipeDownload", "recipeVersion"): lambda env: str(raw(env, "recipe", _RD[env["i"]], "version")),
    ("recipeDownload", "checksumExpected"): lambda env: raw(env, "recipe", _RD[env["i"]], "checksum"),
    ("recipeDownload", "checksumReported"): lambda env: None if env["i"] == 5 and False else (raw(env, "recipe", _RD[env["i"]], "checksum") if env["i"] != 5 else "9f2c4a1be07d51a2"),
    ("recipeDownload", "trigger"): ["Order Start", "Order Start", "Order Start", "Changeover", "Order Start", "Controller Reconnect", "Operator Request", "Order Start", "Changeover", "Revision Release"],
    ("recipeDownload", "verificationResult"): ["Match"] * 5 + ["Mismatch"] + ["Match"] * 4,
    ("recipeDownload", "downloadedAt"): _RDT, ("recipeDownload", "verifiedAt"): [t + datetime.timedelta(seconds=40) for t in _RDT]})

# ---------------------------------------------------------------- plan: set-up verification
_SVT = [DT(9, 15, 5, 48), DT(9, 15, 14, 4), DT(9, 15, 13, 58), DT(9, 18, 14, 55), DT(9, 22, 15, 45), DT(9, 22, 15, 53), DT(9, 16, 22, 14), DT(9, 17, 6, 34), DT(9, 19, 23, 14), DT(9, 24, 8, 18)]
REFIDX.update({("setupVerification", "workCenterId"): [5, 6, 5, 7, 7, 8, 2, 0, 2, 9], ("setupVerification", "equipmentId"): [5, 6, 5, 7, 7, 8, 2, 0, 2, 9],
    ("setupVerification", "productionOrderId"): [0, 1, 1, 4, 7, 7, 2, 3, 5, 9], ("setupVerification", "productVariantId"): [0, 1, 1, 0, 2, 2, None, None, None, 0],
    ("setupVerification", "changeoverId"): [None, None, None, None, None, None, None, None, None, None], ("setupVerification", "billOfProcessId"): [0, 1, 1, 0, 0, 0, 2, 3, 2, 0],
    ("setupVerification", "verifiedById"): [1, 0, 1, 2, 4, 1, 2, 0, 2, 3], ("setupVerification", "interlockEventId"): [None] * 10})
VAL.update({("setupVerification", "trigger"): ["Order Start", "Changeover", "Changeover", "Shift Start", "After Maintenance", "Order Start", "Order Start", "Order Start", "Shift Start", "Order Start"],
    ("setupVerification", "itemCount"): [3, 2, 2, 1, 1, 1, 3, 2, 2, 2], ("setupVerification", "failedCount"): [0, 0, 1, 0, 0, 0, 0, 0, 0, 1], ("setupVerification", "verifiedAt"): _SVT})
_SVI = [("tool", 5), ("item", 4), ("productVariant", 0), ("recipe", 6), ("tool", 6), ("productVariant", 1), ("tool", 5), ("gauge", 7), ("recipe", 7), ("recipe", 8)]
POST["setupVerificationItem"] = _poly(_SVI)
VAL.update({("setupVerificationItem", "checkType"): ["Fixture", "Component", "Variant", "Program", "Tool", "Variant", "Fixture", "Gauge", "Parameter", "Program"],
    ("setupVerificationItem", "scannedCode"): ["SLV-54-0008", "5110-30-0010 L260905-PST-007", "FBC-LH-STD", "PSET-07", "SKT-10-0007", "FBC-RH-STD", "SLV-57-0002", "G-PC-001", None, "DM-5110"],
    ("setupVerificationItem", "expectedValue"): [None] * 8 + ["140.0", None], ("setupVerificationItem", "actualValue"): [None] * 8 + ["140.2", None],
    ("setupVerificationItem", "passed"): [True] * 6 + [False, True, True, True],
    ("setupVerificationItem", "checkedAt"): [_SVT[p] - M(3 - k) for p, k in zip(PARENTIDX["setupVerificationItem"], [0, 1, 2, 0, 1, 0, 1, 0, 0, 0])]})
REFIDX[("setupVerificationItem", "unitOfMeasureId")] = [None] * 8 + [5, None]

# ---------------------------------------------------------------- matl: exposure timers (EPDM seals and dust boots, open-bag time)
_EL = [9, 6, 9, 5, 9, 6, 9, 6, 9, 6]
_EST = [DT(9, 15, 5, 40), DT(9, 15, 5, 45), DT(9, 16, 6, 5), DT(9, 19, 22, 30), DT(9, 18, 15, 0), DT(9, 21, 7, 30), DT(9, 22, 15, 40), DT(9, 23, 6, 10), DT(9, 24, 6, 5), DT(9, 24, 6, 12)]
_ELIM = [480 if l in (5, 9) else 720 for l in _EL]
_EACC = [455, 610, 480, 120, 470, 300, 430, 360, 150, 95]
REFIDX.update({("exposureTimer", "itemId"): [5 if l in (5, 9) else 6 for l in _EL], ("exposureTimer", "lotId"): _EL, ("exposureTimer", "containerId"): [None] * 10,
    ("exposureTimer", "storageLocationId"): [5] * 10, ("exposureTimer", "resetReasonCodeId"): [None, None, None, 5, None, None, None, None, None, None], ("exposureTimer", "resetById"): [None, None, None, 3] + [None] * 6})
VAL.update({("exposureTimer", "timerType"): ["Open Time"] * 10, ("exposureTimer", "limitMinutes"): _ELIM, ("exposureTimer", "startedAt"): _EST,
    ("exposureTimer", "pausedAt"): [None, None, None, DT(9, 19, 23, 26), None, DT(9, 21, 12, 30), None, None, None, DT(9, 24, 7, 47)],
    ("exposureTimer", "accumulatedMinutes"): _EACC, ("exposureTimer", "expiresAt"): [s + M(l) for s, l in zip(_EST, _ELIM)],
    ("exposureTimer", "resetAt"): [None, None, None, DT(9, 19, 23, 35), None, None, None, None, None, None]})
VAL.update({("item", "exposureControlled"): [False] * 5 + [True, True] + [False] * 3, ("item", "openLifeMinutes"): [None] * 5 + [480, 720] + [None] * 3,
    ("item", "fefoRequired"): [False, False, False, False, False, True, True, False, False, False]})

# ---------------------------------------------------------------- matl: replenishment rules and demand forecast
_RPI = [4, 5, 6, 7, 8, 2, 3, 9, 0, 1]
REFIDX.update({("replenishmentRule", "itemId"): _RPI, ("replenishmentRule", "toLocationId"): [5, 5, 5, 5, 5, 5, 4, 3, 8, 8], ("replenishmentRule", "fromLocationId"): [1, 2, 2, 1, 1, 2, 2, 0, 7, 7],
    ("replenishmentRule", "workCenterId"): [5, 5, 5, 6, 6, 5, 2, 0, None, None], ("replenishmentRule", "containerTypeId"): [1, 1, 1, 1, 1, 0, 2, None, 0, 0], ("replenishmentRule", "unitOfMeasureId"): [0] * 7 + [1, 0, 0]})
VAL.update({("replenishmentRule", "triggerType"): ["Kanban Scan", "Consumption", "Consumption", "Kanban Scan", "Kanban Scan", "Min-Max", "Min-Max", "Min-Max", "Order Demand", "Order Demand"],
    ("replenishmentRule", "minQuantity"): ["96", "200", "200", "100", "100", "48", "120", "1000", "0", "0"], ("replenishmentRule", "maxQuantity"): ["480", "800", "800", "500", "500", "240", "480", "4000", "480", "480"],
    ("replenishmentRule", "reorderPointQuantity"): ["192", "300", "300", "200", "200", "96", "240", "1500", "24", "24"], ("replenishmentRule", "kanbanQuantity"): ["96", None, None, "100", "100", None, None, None, None, None],
    ("replenishmentRule", "kanbanCount"): [5, None, None, 5, 5, None, None, None, None, None], ("replenishmentRule", "leadTimeMinutes"): [45, 30, 30, 45, 45, 60, 90, 240, 30, 30],
    ("replenishmentRule", "validFrom"): [DT(4, 1, 0, 0)] * 5 + [DT(5, 1, 0, 0)] * 3 + [DT(6, 1, 0, 0)] * 2, ("replenishmentRule", "validTo"): [None] * 9 + [DT(9, 30, 0, 0)]})
REFIDX[("materialRequest", "replenishmentRuleId")] = [None, None, None, None, None, 1, 3, None, None, 1]
_MDI = [5, 5, 4, 6, 7, 8, 2, 5, 6, 4]
_MDB = [DT(9, 24, 8, 0), DT(9, 24, 9, 0), DT(9, 24, 8, 0), DT(9, 24, 8, 0), DT(9, 24, 8, 0), DT(9, 24, 8, 0), DT(9, 24, 8, 0), DT(9, 22, 16, 0), DT(9, 22, 16, 0), DT(9, 22, 16, 0)]
REFIDX.update({("materialDemandForecast", "itemId"): _MDI, ("materialDemandForecast", "lineId"): [5] * 10, ("materialDemandForecast", "unitOfMeasureId"): [0] * 10,
    ("materialDemandForecast", "analyticsModelId"): [6, 6, None, None, None, None, None, None, None, None]})
VAL.update({("materialDemandForecast", "productionDate"): [DT(9, 24, 0, 0)] * 7 + [DT(9, 22, 0, 0)] * 3, ("materialDemandForecast", "bucketStartAt"): _MDB,
    ("materialDemandForecast", "bucketEndAt"): [b + M(60) for b in _MDB], ("materialDemandForecast", "scheduledDemand"): ["100", "100", "100", "100", "100", "200", "100", "60", "60", "60"],
    ("materialDemandForecast", "consumptionRatePerHour"): ["96", "98", "95", "96", "96", "192", "96", "58", "57", "58"],
    ("materialDemandForecast", "onHandQuantity"): ["150", "54", "310", "260", "420", "380", "130", "210", "190", "240"],
    ("materialDemandForecast", "projectedOnHand"): ["54", "-44", "215", "164", "324", "188", "34", "152", "133", "182"],
    ("materialDemandForecast", "projectedShortageAt"): [None, DT(9, 24, 9, 33), None, None, None, None, None, None, None, None],
    ("materialDemandForecast", "method"): ["Model", "Model", "Consumption Rate", "Consumption Rate", "Schedule", "Schedule", "Consumption Rate", "Schedule", "Schedule", "Schedule"],
    ("materialDemandForecast", "calculatedAt"): [b - M(5) for b in _MDB]})

# ---------------------------------------------------------------- trac: trace investigations
_TRS = [("lot", 5), ("serialNumber", 9), ("lot", 7), ("wipUnit", 7), ("lot", 0), ("lot", 1), ("wipUnit", 0), ("lot", 4), ("serialNumber", 2), ("lot", 3)]
_TRT = [DT(9, 19, 23, 50), DT(9, 24, 15, 10), DT(9, 21, 8, 5), DT(9, 22, 17, 0), DT(9, 17, 9, 15), DT(9, 15, 15, 0), DT(9, 19, 23, 58), DT(9, 23, 10, 30), DT(9, 24, 11, 0), DT(9, 18, 16, 0)]
POST["traceInvestigation"] = _poly(_TRS)
REFIDX.update({("traceInvestigation", "qualityHoldId"): [0, None, 7, None, 4, 2, 0, None, None, 3], ("traceInvestigation", "nonconformanceId"): [5, 9, 6, 7, 0, 1, 5, None, None, 4],
    ("traceInvestigation", "customerComplaintId"): [None, 9, None, None, None, None, None, None, None, None], ("traceInvestigation", "requestedById"): [3, 3, 3, 3, 3, 3, 4, 3, 6, 3],
    ("traceInvestigation", "exportControlledDocumentId"): [None] * 10})
VAL.update({("traceInvestigation", "title"): lambda env: TITLES["traceInvestigation"][env["i"]],
    ("traceInvestigation", "direction"): ["Forward", "Reverse", "Forward", "Reverse", "Forward", "Forward", "Reverse", "Forward", "Reverse", "Forward"],
    ("traceInvestigation", "depthLimit"): [3, 5, 3, 5, 4, 4, 5, 3, 5, 3], ("traceInvestigation", "resultCount"): [3, 2, 2, 1, 1, 0, 6, 0, 4, 1],
    ("traceInvestigation", "shippedCount"): [0, 1, 0, 0, 0, 0, 0, 0, 0, 1], ("traceInvestigation", "requestedAt"): _TRT,
    ("traceInvestigation", "completedAt"): [t + M(2) if s != "Running" else None for t, s in zip(_TRT, STATUSOF["traceInvestigation"])]})
_TRR = [("wipUnit", 0), ("wipUnit", 1), ("wipUnit", 4), ("lot", 3), ("lot", 7), ("wipUnit", 2), ("wipUnit", 3), ("lot", 4), ("lot", 1), ("wipUnit", 9)]
POST["traceInvestigationResult"] = _poly(_TRR)
REFIDX.update({("traceInvestigationResult", "itemId"): [0, 0, 0, 2, 7, 1, 1, 4, 3, 0], ("traceInvestigationResult", "storageLocationId"): [6, 5, 5, 5, 5, 5, 6, 5, None, None],
    ("traceInvestigationResult", "shipmentId"): [None] * 9 + [0], ("traceInvestigationResult", "customerId"): [None] * 9 + [0]})
VAL.update({("traceInvestigationResult", "genealogyDepth"): [1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    ("traceInvestigationResult", "statusAtRun"): ["On Hold", "In Process", "In Process", "Available", "Available", "In Process", "In Rework", "Available", "Consumed", "Shipped"],
    ("traceInvestigationResult", "quantity"): ["1", "1", "1", "960", "4800", "1", "1", "4000", "480", "1"]})

# ---------------------------------------------------------------- qual: positions, envelopes, curves
VAL.update({("characteristicPosition", "positionName"): ["Outer face, inboard", "Outer face, outboard", "Bridge top", "Mounting ear, upper", "Mounting ear, lower", "Bore depth 5 mm", "Bore depth 20 mm", "Bore depth 35 mm", "Bridge, left of centre", "Bridge, right of centre"],
    ("characteristicPosition", "nominal"): ["12.0"] * 5 + ["54.023"] * 3 + ["8.00"] * 2, ("characteristicPosition", "lowerSpecLimit"): ["8.0"] * 5 + ["54.000"] * 3 + ["7.50"] * 2,
    ("characteristicPosition", "upperSpecLimit"): ["16.0"] * 5 + ["54.046"] * 3 + ["8.50"] * 2})
REFIDX.update({("characteristicPosition", "unitOfMeasureId"): [3] * 5 + [2] * 5, ("characteristicPosition", "curveEnvelopeId"): [None] * 10})
VAL[("characteristic", "positionCount")] = [2, 1, 3, 1, 5, 1, 1, 1, 1, 1]
VAL.update({("curveEnvelope", "name"): lambda env: MASTER["curveEnvelope"][env["i"]].split("|")[1],
    ("curveEnvelope", "curveType"): ["Force Displacement", "Force Displacement", "Torque Angle", "Torque Angle", "Torque Angle", "Pressure Time", "Pressure Time", "Force Displacement", "Force Displacement", "Torque Angle"],
    ("curveEnvelope", "xQuantity"): ["Displacement", "Displacement", "Angle", "Angle", "Angle", "Time", "Time", "Displacement", "Displacement", "Angle"],
    ("curveEnvelope", "xUnitText"): ["mm", "mm", "deg", "deg", "deg", "ms", "ms", "mm", "mm", "deg"],
    ("curveEnvelope", "yQuantity"): ["Force", "Force", "Torque", "Torque", "Torque", "Pressure drop", "Pressure drop", "Force", "Force", "Torque"],
    ("curveEnvelope", "yUnitText"): ["N", "N", "N.m", "N.m", "N.m", "Pa", "Pa", "N", "N", "N.m"],
    ("curveEnvelope", "version"): [2, 1, 4, 4, 1, 2, 2, 1, 2, 3],
    ("curveEnvelope", "goldenSampleSerialNo"): ["VB26240A00012", "VB26240A00012", "VB26241A00031", "VB26241B00044", "VB26241A00031", "VB26238A00007", "VB26238A00007", "VB26205A00003", "VB26242B00019", "VB26201A00011"],
    ("curveEnvelope", "effectiveFrom"): [DT(8, 28, 0, 0), DT(6, 2, 0, 0), DT(9, 1, 0, 0), DT(9, 1, 0, 0), DT(6, 2, 0, 0), DT(8, 26, 0, 0), DT(8, 26, 0, 0), DT(4, 6, 0, 0), DT(8, 31, 0, 0), DT(4, 6, 0, 0)],
    ("curveEnvelope", "effectiveTo"): [None] * 7 + [DT(8, 27, 0, 0), None, DT(8, 31, 0, 0)],
    ("curveEnvelope", "approvedAt"): [DT(8, 27, 11, 10), DT(6, 1, 15, 20), DT(8, 31, 10, 5), DT(8, 31, 10, 12), DT(6, 1, 15, 40), DT(8, 25, 12, 0), DT(8, 25, 12, 4), DT(4, 4, 10, 0), DT(8, 30, 16, 15), DT(4, 4, 10, 20)]})
REFIDX.update({("curveEnvelope", "characteristicId"): [5, 5, 6, 6, 6, 7, 7, 5, 5, 6], ("curveEnvelope", "itemId"): [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    ("curveEnvelope", "productVariantId"): [0, None, 0, 1, None, None, None, 0, 1, 0], ("curveEnvelope", "operationId"): [5, 5, 6, 6, 6, 7, 7, 5, 5, 6],
    ("curveEnvelope", "recipeId"): [None, None, 6, 6, 5, 7, 7, None, None, 6], ("curveEnvelope", "referenceControlledDocumentId"): [None, None, 6, None, None, None, None, None, None, None],
    ("curveEnvelope", "approvedById"): [6] * 10})
VAL.update({("curveEnvelopeWindow", "windowType"): ["Box", "Box", "Final Value", "Box", "Box", "Final Value", "Upper Band", "Final Value", "Peak", "Final Value"],
    ("curveEnvelopeWindow", "xMin"): ["0.0", "30.0", "41.5", "0", "15", "20", "0", "4900", "2.7", "20"], ("curveEnvelopeWindow", "xMax"): ["30.0", "41.5", "42.5", "15", "70", "70", "5000", "5000", "3.3", "70"],
    ("curveEnvelopeWindow", "yMin"): ["0", "250", "800", "0.0", "4.0", "12.0", None, "0", "50", "25.0"], ("curveEnvelopeWindow", "yMax"): ["400", "900", "1500", "6.0", "16.0", "16.0", "50", "50", "200", "31.0"],
    ("curveEnvelopeWindow", "entrySide"): ["Left", "Left", None, "Left", "Left", None, None, None, None, None], ("curveEnvelopeWindow", "exitSide"): ["Right", "Right", None, "Right", "Right", None, None, None, None, None]})
# measurement curves: 0 = piston press-in (unit U260915A0184), 1-5 = torque results 0, 3, 6, 7 and 1, 6-9 = leak test results 0, 1, 7, 8
_CRV = [("press", None), ("trq", 0), ("trq", 3), ("trq", 6), ("trq", 7), ("trq", 1), ("lkt", 0), ("lkt", 1), ("lkt", 7), ("lkt", 8)]
REFIDX.update({("measurementCurve", "curveEnvelopeId"): [0, 2, 3, 3, 3, 4, 5, 5, 5, 5], ("measurementCurve", "characteristicId"): [5, 6, 6, 6, 6, 6, 7, 7, 7, 7],
    ("measurementCurve", "wipUnitId"): [0, 1, 2, 3, 3, 1, 4, 4, 7, 7], ("measurementCurve", "serialNumberId"): [0, 1, 2, 3, 3, 1, 4, 4, 7, 7],
    ("measurementCurve", "operationExecutionId"): [1, 2, 3, 4, 4, 2, 5, 5, 8, 8], ("measurementCurve", "equipmentId"): [5, 6, 6, 6, 6, 6, 7, 7, 7, 7],
    ("measurementCurve", "rawControlledDocumentId"): [None, None, 6, None, None, None, None, None, None, None], ("measurementCurve", "inspectionResultId"): [5, 6, None, None, None, None, 7, None, None, None]})
def _cap(env):
    kind, k = _CRV[env["i"]]
    if kind == "press": return raw(env, "operationExecution", 1, "startedAt") + datetime.timedelta(seconds=12)
    if kind == "trq": return raw(env, "torqueResult", k, "tightenedAt")
    return raw(env, "leakTestResult", k, "testedAt")
VAL.update({("measurementCurve", "capturedAt"): _cap, ("measurementCurve", "positionNo"): [1, None, None, None, None, None, None, None, None, None],
    ("measurementCurve", "recipeVersion"): [None, "4", "4", "4", "4", "1", "2", "2", "2", "2"], ("measurementCurve", "pointCount"): [400, 512, 498, 530, 534, 620, 250, 250, 250, 250],
    ("measurementCurve", "peakX"): ["41.9", "38.5", "36.0", "31.0", "33.5", "44.0", "5000", "5000", "5000", "5000"], ("measurementCurve", "peakY"): ["1180", "14.2", "13.8", "11.4", "11.8", "28.6", "8", "9", "412", "402"],
    ("measurementCurve", "finalX"): ["41.9", "38.5", "36.0", "31.0", "33.5", "44.0", "5000", "5000", "5000", "5000"], ("measurementCurve", "finalY"): ["1150", "14.2", "13.8", "11.4", "11.8", "28.6", "8", "9", "412", "402"],
    ("measurementCurve", "result"): ["OK", "OK", "OK", "NOK", "NOK", "OK", "OK", "OK", "NOK", "NOK"], ("measurementCurve", "failedWindowNo"): [None, None, None, 3, 3, None, None, None, 1, 1]})
REFIDX.update({("torqueResult", "measurementCurveId"): [1, 5, None, 2, None, None, 3, 4, None, None], ("torqueResult", "curveEnvelopeId"): [2, 4, 4, 3, 4, 4, 3, 3, 4, 4]})
VAL[("torqueResult", "envelopeResult")] = ["OK", "OK", None, "OK", None, None, "NOK", "NOK", None, None]
REFIDX[("leakTestResult", "measurementCurveId")] = [6, 7, None, None, None, None, None, 8, 9, None]
REFIDX[("inspectionResult", "measurementCurveId")] = [None, None, None, None, None, 0, 1, 6, None, None]
_PX = ["0.0", "5.0", "10.0", "15.0", "20.0", "25.0", "30.0", "35.0", "40.0", "41.9"]
_PY = ["0", "38", "85", "118", "142", "160", "355", "640", "905", "1150"]
REFIDX[("measurementCurvePoint", "measurementCurveId")] = [0] * 10
VAL.update({("measurementCurvePoint", "pointNo"): [1 + 40 * k for k in range(9)] + [400], ("measurementCurvePoint", "xValue"): _PX, ("measurementCurvePoint", "yValue"): _PY,
    ("measurementCurvePoint", "sampledAt"): lambda env: _cap(dict(env, i=0)) - datetime.timedelta(seconds=9) + datetime.timedelta(seconds=env["i"])})

# ---------------------------------------------------------------- qual: defect records
_DC = [6, 7, 5, 2, 0, 1, 3, 4, 8, 9]
_DT = [DT(9, 15, 14, 21), DT(9, 22, 16, 4), DT(9, 15, 6, 2), DT(9, 16, 23, 10), DT(9, 17, 9, 5), DT(9, 15, 14, 50), DT(9, 17, 7, 40), DT(9, 18, 15, 30), DT(9, 24, 0, 40), DT(9, 24, 8, 36)]
REFIDX.update({("defectRecord", "defectCodeId"): _DC, ("defectRecord", "wipUnitId"): [3, 7, 0, None, None, None, None, None, 8, 9], ("defectRecord", "serialNumberId"): [3, 7, 0, None, None, None, None, None, 8, 9],
    ("defectRecord", "lotId"): [None, None, None, 2, 0, 1, 2, 3, None, None], ("defectRecord", "itemId"): [1, 0, 0, 2, 3, 3, 2, 2, 0, 0], ("defectRecord", "productVariantId"): [1, 2, 0, None, None, None, None, None, 0, 0],
    ("defectRecord", "productionOrderId"): [1, 7, 0, 2, 3, None, 2, None, 9, 9], ("defectRecord", "detectedAtOperationId"): [6, 7, 5, 2, 2, 1, 3, 4, 8, 9], ("defectRecord", "detectedAtWorkCenterId"): [6, 7, 5, 2, 2, 1, 3, 4, 8, 9],
    ("defectRecord", "originOperationId"): [6, 5, 5, 2, 0, 1, 2, 4, 8, 9], ("defectRecord", "operatorUserId"): [1, 2, 1, 2, 0, 1, 0, 1, 2, 0], ("defectRecord", "equipmentId"): [6, 5, 5, 2, 0, 1, 3, 4, 8, 9],
    ("defectRecord", "componentLotId"): [7, 9, 5, None, 8, None, None, None, None, None], ("defectRecord", "operationExecutionId"): [4, 8, 1, None, None, None, None, None, None, 9],
    ("defectRecord", "inspectionResultId"): [None, 7, None, 2, None, 1, 3, 4, None, None], ("defectRecord", "shiftId"): [1, 2, 1, 2, 0, 1, 0, 1, 2, 0], ("defectRecord", "detectedById"): [1, 2, 1, 3, 3, 3, 3, 3, 2, 0],
    ("defectRecord", "imageControlledDocumentId"): [None] * 10, ("defectRecord", "nonconformanceId"): [6, 7, 5, 2, 0, 1, 3, 4, 8, 9],
    ("defectRecord", "reworkOrderId"): [2, None, None, None, None, None, None, None, 7, None], ("defectRecord", "scrapRecordId"): [None, 7, None, 2, 0, None, None, None, None, None]})
VAL.update({("defectRecord", "isFirstFail"): [True, True, True, True, False, True, True, True, True, True], ("defectRecord", "positionNo"): [None, 1, 1, 2, None, None, None, 3, None, None],
    ("defectRecord", "defectLocationText"): ["Bleed screw seat", "Piston seal, inboard", "Piston seal groove", "Piston bore, depth 20 mm", "Bridge section", "Test pad", "Piston bore, bottom", "Bridge top", "2D code field", "Bleed port"],
    ("defectRecord", "quantity"): [1, 1, 1, 3, 9, 6, 2, 24, 1, 1], ("defectRecord", "fourMCategory"): ["Machine", "Material", "Material", "Machine", "Method", "Machine", "Method", "Machine", "Machine", "Man"],
    ("defectRecord", "productionDate"): [datetime.datetime(t.year, t.month, t.day) for t in _DT], ("defectRecord", "detectedAt"): _DT})

# ---------------------------------------------------------------- qual: audit schedules
REFIDX.update({("auditSchedule", "areaId"): [4, 4, 4, 4, 2, 0, 4, 0, 3, 5], ("auditSchedule", "lineId"): [5, 5, 5, 5, 2, 0, 5, None, None, 6],
    ("auditSchedule", "workCenterId"): [5, 6, 7, None, None, None, None, None, None, None], ("auditSchedule", "checkSheetId"): [5, 6, 7, 5, 2, 0, 5, 0, 4, 9],
    ("auditSchedule", "auditorRoleId"): [2, 2, 2, 3, 3, 3, 5, 5, 5, 5], ("auditSchedule", "auditorUserId"): [None, None, None, 4, 4, 4, 3, 3, 3, 3], ("auditSchedule", "escalationRuleId"): [5] * 10})
VAL.update({("auditSchedule", "name"): lambda env: MASTER["auditSchedule"][env["i"]].split("|")[1],
    ("auditSchedule", "auditType"): ["Layered Process Audit"] * 9 + ["Product Audit"], ("auditSchedule", "layer"): [1, 1, 1, 2, 2, 2, 3, 3, 3, None],
    ("auditSchedule", "frequencyType"): ["Shift", "Shift", "Shift", "Daily", "Daily", "Daily", "Weekly", "Weekly", "Weekly", "Monthly"], ("auditSchedule", "frequencyValue"): ["1"] * 10,
    ("auditSchedule", "toleranceHours"): [4, 4, 4, 12, 12, 12, 48, 48, 48, 168],
    ("auditSchedule", "nextDueDate"): [DT(9, 28, 0, 0)] * 3 + [DT(9, 28, 0, 0)] * 3 + [DT(10, 3, 0, 0)] * 3 + [DT(10, 31, 0, 0)],
    ("auditSchedule", "validFrom"): [DT(4, 1, 0, 0)] * 10, ("auditSchedule", "validTo"): [None] * 9 + [DT(9, 30, 0, 0)]})
REFIDX[("audit", "auditScheduleId")] = [7, None, None, None, None, 6, 9, 2, None, None]
VAL.update({("audit", "dueDate"): [DT(9, 19, 0, 0), None, None, None, None, DT(9, 26, 0, 0), DT(9, 30, 0, 0), DT(9, 22, 0, 0), None, None],
    ("audit", "isMissed"): [True] + [False] * 9, ("audit", "escalationLevel"): [1] + [0] * 9})
REFIDX[("inspectionPlanProductVariant", "productVariantId")] = [0, 2, 0, 1, 0, 2, 0, 2, 0, 4]
VAL[("inspectionPlan", "itemRevision")] = [None, None, "C", "C", "C", "D", "D", "D", "D", "D"]

# ---------------------------------------------------------------- perf: alarm definitions
REFIDX.update({("alarmDefinition", "equipmentTypeId"): list(range(10)), ("alarmDefinition", "authorizingRoleId"): [3, 3, 1, None, 3, 3, 3, 4, None, None],
    ("alarmDefinition", "defaultReasonCodeId"): list(range(10)), ("alarmDefinition", "escalationRuleId"): [1, 1, 1, None, 4, 0, 0, 0, None, None]})
VAL.update({("alarmDefinition", "alarmCode"): ["A2031"] * 10, ("alarmDefinition", "alarmText"): lambda env: MASTER["alarmDefinition"][env["i"]].split("|")[1],
    ("alarmDefinition", "alarmClass"): ["Process"] * 10, ("alarmDefinition", "severityClass"): ["High", "Critical", "High", "Medium", "Medium", "Critical", "High", "Critical", "Medium", "Low"],
    ("alarmDefinition", "blocksRestart"): [True, True, True, False, True, True, True, True, False, False], ("alarmDefinition", "createsDowntime"): [True, False, True, False, True, False, True, False, True, False],
    ("alarmDefinition", "responseInstruction"): ["Stop pouring, check die heater zones and thermocouple; restart after supervisor approval",
        "Hold the charge in the furnace; maintenance to check heater current; quality to decide on the charge",
        "Stop the spindle; check coolant filter and pump; setter restarts after first-off check",
        "Check bath heater and level; continue after temperature is back in range",
        "Stop current; check rectifier cooling; restart after supervisor approval",
        "Stop the press; remove the part to the red bin; check seal feed and press position sensor",
        "Stop the station; change the socket and verify with the torque analyser before restart",
        "Stop testing; verify the tester with the master leak part before restart",
        "Pause marking; let the head cool and check extraction",
        "Check the air supply regulator; continue when pressure is back in range"]})
REFIDX.update({("alarm", "alarmDefinitionId"): list(range(10)), ("alarm", "lineId"): [0, 1, 2, 3, 4, 5, 5, 5, 5, 6], ("alarm", "workCenterId"): list(range(10)), ("alarm", "shiftId"): [0, 1, 2, 0, 1, 2, 0, 1, 2, 0],
    ("alarm", "wipUnitId"): [None] * 10, ("alarm", "restartAuthorizedById"): [None, None, 4, None, None, 4, None, None, None, None],
    ("alarm", "closureReasonCodeId"): [None, None, 2, None, None, 5, None, None, 8, None]})
VAL.update({("alarm", "blocksRestart"): [True, True, True, False, True, True, True, True, False, False],
    ("alarm", "restartAuthorizedAt"): lambda env: (cur(env, "raisedAt") + M(2)) if env["i"] in (2, 5) else None,
    ("alarm", "escalationLevel"): [1, 0, 0, 0, 0, 0, 1, 0, 0, 0], ("alarm", "productionDate"): lambda env: (lambda t: datetime.datetime(t.year, t.month, t.day))(cur(env, "raisedAt"))})

# ---------------------------------------------------------------- perf: reports
_LS = [(5, 5, 0, DT(9, 15, 0, 0), 5), (5, 6, 1, DT(9, 15, 0, 0), 6), (5, 5, 1, DT(9, 15, 0, 0), 5), (0, 0, 0, DT(9, 17, 0, 0), 0), (0, 0, 0, DT(9, 17, 0, 0), 1),
       (5, 7, 1, DT(9, 18, 0, 0), 7), (5, 7, 1, DT(9, 22, 0, 0), 7), (5, 5, 1, DT(9, 22, 0, 0), 5), (2, 2, 2, DT(9, 24, 0, 0), 2), (6, 9, 0, DT(9, 24, 0, 0), 9)]
REFIDX.update({("lossSummary", "lineId"): [x[0] for x in _LS], ("lossSummary", "workCenterId"): [x[1] for x in _LS], ("lossSummary", "shiftId"): [x[2] for x in _LS],
    ("lossSummary", "reasonCodeId"): [x[4] for x in _LS], ("lossSummary", "lossCategoryId"): [3, 0, 9, 0, 0, 0, 0, 2, 0, 0]})
VAL.update({("lossSummary", "productionDate"): [x[3] for x in _LS], ("lossSummary", "isPlanned"): [False] * 10,
    ("lossSummary", "occurrenceCount"): [6, 3, 2, 1, 1, 4, 2, 1, 1, 2], ("lossSummary", "lossMinutes"): [14, 35, 9, 95, 150, 48, 30, 12, 42, 22],
    ("lossSummary", "lossUnits"): [23, 58, 15, 57, 0, 120, 50, 20, 12, 66], ("lossSummary", "lossPctOfPlannedTime"): ["3.3", "8.1", "2.1", "22.1", "34.9", "11.2", "7.0", "2.8", "9.8", "5.1"],
    ("lossSummary", "paretoRank"): [2, 1, 3, 1, 1, 1, 1, 2, 1, 1], ("lossSummary", "cumulativePct"): ["79.5", "60.3", "100.0", "38.8", "100.0", "84.2", "71.4", "100.0", "100.0", "100.0"],
    ("lossSummary", "maintenanceWorkOrderCount"): [0, 1, 0, 1, 1, 1, 1, 0, 1, 1], ("lossSummary", "capaCount"): [1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    ("lossSummary", "calculatedAt"): [x[3] + M(24 * 60 + 15) for x in _LS]})
_WP = [(5, 1, DT(9, 15, 6, 0)), (6, 2, DT(9, 15, 6, 0)), (7, 2, DT(9, 15, 6, 0)), (6, 0, DT(9, 15, 14, 0)), (7, 0, DT(9, 15, 14, 0)), (7, 2, DT(9, 18, 15, 0)), (7, 1, DT(9, 22, 16, 0)), (6, 1, DT(9, 22, 16, 0)), (9, 0, DT(9, 24, 8, 0)), (8, 0, DT(9, 24, 8, 0))]
REFIDX.update({("workCenterPerformance", "workCenterId"): [x[0] for x in _WP], ("workCenterPerformance", "lineId"): [6 if x[0] == 9 else 5 for x in _WP], ("workCenterPerformance", "shiftId"): [x[1] for x in _WP],
    ("workCenterPerformance", "productVariantId"): [0, 0, 0, 1, 1, 0, 2, 2, 0, 0]})
VAL.update({("workCenterPerformance", "productionDate"): [datetime.datetime(x[2].year, x[2].month, x[2].day) for x in _WP], ("workCenterPerformance", "periodStartAt"): [x[2] for x in _WP],
    ("workCenterPerformance", "periodEndAt"): [x[2] + M(60) for x in _WP], ("workCenterPerformance", "unitsCompleted"): [98, 96, 94, 92, 89, 88, 71, 90, 99, 101],
    ("workCenterPerformance", "throughputPerHour"): ["98", "96", "94", "92", "89", "88", "71", "90", "99", "101"],
    ("workCenterPerformance", "averageCycleTimeSec"): ["33.9", "20.0", "24.5", "17.5", "25.8", "24.5", "31.9", "19.2", "20.0", "14.4"],
    ("workCenterPerformance", "taktTimeSec"): ["36.0"] * 10, ("workCenterPerformance", "taktBreachCount"): [6, 1, 2, 0, 4, 3, 19, 1, 0, 0],
    ("workCenterPerformance", "wipQuantity"): [4, 6, 12, 3, 9, 8, 24, 2, 3, 1], ("workCenterPerformance", "blockedMinutes"): ["2.5", "4.0", "0.0", "1.0", "0.0", "0.0", "0.0", "11.0", "0.0", "0.0"],
    ("workCenterPerformance", "starvedMinutes"): ["0.0", "0.5", "1.5", "2.0", "0.5", "3.0", "0.0", "6.5", "4.0", "5.0"], ("workCenterPerformance", "isConstraint"): [False, False, True, False, True, True, True, False, False, False],
    ("workCenterPerformance", "rankInLine"): [3, 2, 1, 2, 1, 1, 1, 2, 1, 2], ("workCenterPerformance", "calculatedAt"): [x[2] + M(65) for x in _WP]})
_OP = [(1, 5, 0, 1, DT(9, 15, 0, 0)), (2, 6, 0, 2, DT(9, 15, 0, 0)), (0, 6, 1, 0, DT(9, 15, 0, 0)), (1, 6, 1, 1, DT(9, 15, 0, 0)), (2, 7, 0, 2, DT(9, 18, 0, 0)),
       (0, 7, 0, 0, DT(9, 18, 0, 0)), (1, 7, 2, 1, DT(9, 22, 0, 0)), (2, 7, 2, 2, DT(9, 22, 0, 0)), (0, 9, 0, 0, DT(9, 24, 0, 0)), (0, 0, None, 0, DT(9, 17, 0, 0))]
REFIDX.update({("operatorPerformance", "userId"): [x[0] for x in _OP], ("operatorPerformance", "workCenterId"): [x[1] for x in _OP], ("operatorPerformance", "productVariantId"): [x[2] for x in _OP],
    ("operatorPerformance", "shiftId"): [x[3] for x in _OP]})
VAL.update({("operatorPerformance", "productionDate"): [x[4] for x in _OP], ("operatorPerformance", "attendedMinutes"): ["455", "460", "450", "455", "448", "452", "440", "445", "430", "460"],
    ("operatorPerformance", "earnedMinutes"): ["421", "430", "441", "398", "409", "418", "322", "401", "418", "448"],
    ("operatorPerformance", "efficiencyPct"): ["92.5", "93.5", "98.0", "87.5", "91.3", "92.5", "73.2", "90.1", "97.2", "97.4"],
    ("operatorPerformance", "goodQuantity"): [742, 1290, 1508, 1226, 980, 1012, 610, 958, 1250, 231], ("operatorPerformance", "rejectQuantity"): [2, 0, 1, 2, 3, 2, 6, 1, 0, 9],
    ("operatorPerformance", "errorCount"): [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], ("operatorPerformance", "interlockCount"): [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
    ("operatorPerformance", "calculatedAt"): [x[4] + M(24 * 60 + 20) for x in _OP]})

# ---------------------------------------------------------------- maint
_MT = ["Remove and inspect the inlet test seal set", "Fit the new test seal set and tighten the adaptor", "Verify the tester with the 0.5 sccm master leak part",
       "Remove die 2 ejector pin and inspect for galling", "Polish the pin, check the bush and refit", "Change the bag filter", "Record differential pressure after the change",
       "Replace the nutrunner socket", "Verify torque with the analyser on the check joint", "Replace camera 2 cable and route it in the drag chain"]
REFIDX.update({("maintenanceWorkOrderTask", "maintenancePlanTaskId"): [None] * 10, ("maintenanceWorkOrderTask", "unitOfMeasureId"): [None, None, None, None, None, None, 5, None, 4, None],
    ("maintenanceWorkOrderTask", "completedById"): [None, None, None, 5, 5, 5, 5, 5, 5, 5]})
VAL.update({("maintenanceWorkOrderTask", "description"): _MT, ("maintenanceWorkOrderTask", "result"): ["Not Done", "Not Done", "Not Done", "Done OK", "Done OK", "Done OK", "Done OK", "Done OK", "Done OK", "Done OK"],
    ("maintenanceWorkOrderTask", "measuredValue"): [None] * 6 + ["0.25", None, "14.1", None],
    ("maintenanceWorkOrderTask", "comment"): [None, None, None, "Galling on 30 mm of the pin", None, None, "Was 0.92 bar before the change", None, "Analyser 14.1 N.m against controller 14.0 N.m", None],
    ("maintenanceWorkOrderTask", "completedAt"): lambda env: None if env["i"] < 3 else raw(env, "maintenanceWorkOrder", PARENTIDX["maintenanceWorkOrderTask"][env["i"]], "startedAt") + M(10 + 8 * env["line"])})
_SPI = [0, 0, 2, 3, 4, 5, 0, 5, 5, 7]
_SPW = [6, None, 2, 3, 4, None, 6, 7, 7, 9]
_SPT = [DT(9, 15, 6, 20), DT(9, 15, 11, 0), DT(9, 16, 23, 5), DT(9, 17, 7, 10), DT(9, 18, 15, 20), DT(9, 19, 10, 30), DT(9, 21, 7, 50), DT(9, 22, 16, 15), DT(9, 23, 9, 40), DT(9, 24, 8, 50)]
def _spt_at(env):
    """an issue or return happens at the work order: 5 minutes after its start (return: one day later)"""
    i = env["i"]; w = _SPW[i]
    if w is None: return _SPT[i]
    t = raw(env, "maintenanceWorkOrder", w, "startedAt") or raw(env, "maintenanceWorkOrder", w, "reportedAt")
    return t + M(5) + (datetime.timedelta(days=1) if i == 8 else datetime.timedelta(0))
REFIDX.update({("sparePartTransaction", "sparePartId"): _SPI, ("sparePartTransaction", "unitOfMeasureId"): [0] * 10, ("sparePartTransaction", "maintenanceWorkOrderId"): [6, None, 2, 3, 4, None, 6, 7, 7, 9],
    ("sparePartTransaction", "equipmentId"): [6, None, 2, 3, 4, None, 6, 7, 7, 9], ("sparePartTransaction", "storageLocationId"): [2] * 10, ("sparePartTransaction", "transactedById"): [7] * 10})
VAL.update({("sparePartTransaction", "transactionType"): ["Issue", "Receipt", "Issue", "Issue", "Issue", "Receipt", "Issue", "Issue", "Return", "Issue"],
    ("sparePartTransaction", "quantity"): ["1", "10", "2", "1", "1", "4", "1", "1", "1", "1"], ("sparePartTransaction", "scanVerified"): [True, True, True, True, False, True, True, True, True, True],
    ("sparePartTransaction", "unitCostInr"): lambda env: raw(env, "sparePart", _SPI[env["i"]], "unitCostInr"),
    ("sparePartTransaction", "transactedAt"): lambda env: _spt_at(env),
    ("sparePartTransaction", "erpDocumentNo"): ["4900127731", "5000331204", "4900127802", "4900127845", "4900127913", "5000331287", "4900128001", "4900128066", "4900128104", "4900128150"]})
REFIDX.update({("reliabilitySummary", "equipmentId"): list(range(10)), ("reliabilitySummary", "lineId"): [0, 1, 2, 3, 4, 5, 5, 5, 5, 6], ("reliabilitySummary", "shiftId"): [None] * 10})
VAL.update({("reliabilitySummary", "periodType"): ["Month"] * 10, ("reliabilitySummary", "periodStartAt"): [DT(9, 1, 0, 0)] * 10, ("reliabilitySummary", "periodEndAt"): [DT(9, 30, 23, 59)] * 10,
    ("reliabilitySummary", "operatingHours"): ["498.5", "612.0", "455.0", "380.5", "402.0", "441.5", "438.0", "436.5", "420.0", "415.5"], ("reliabilitySummary", "failureCount"): [2, 1, 3, 1, 1, 2, 3, 2, 1, 1],
    ("reliabilitySummary", "repairMinutes"): [190, 150, 126, 25, 60, 36, 105, 96, 30, 22],
    ("reliabilitySummary", "mtbfHours"): ["249.3", "612.0", "151.7", "380.5", "402.0", "220.8", "146.0", "218.3", "420.0", "415.5"],
    ("reliabilitySummary", "mttrMinutes"): ["95.0", "150.0", "42.0", "25.0", "60.0", "18.0", "35.0", "48.0", "30.0", "22.0"],
    ("reliabilitySummary", "availabilityPct"): ["99.4", "99.6", "99.5", "99.9", "99.8", "99.9", "99.6", "99.6", "99.9", "99.9"], ("reliabilitySummary", "calculatedAt"): [DT(9, 30, 23, 59)] * 10})
REFIDX.update({("equipmentLifecycleEvent", "equipmentId"): [6, 0, 1, 2, 7, 7, 3, 8, 9, 4], ("equipmentLifecycleEvent", "maintenanceWorkOrderId"): [None, None, 1, None, None, 7, 3, None, None, 4],
    ("equipmentLifecycleEvent", "engineeringChangeId"): [None, None, None, None, 6, None, None, None, None, None], ("equipmentLifecycleEvent", "modelPredictionId"): [None, None, None, None, None, 5, None, None, None, None],
    ("equipmentLifecycleEvent", "approvedById"): [6, 6, None, 6, 6, None, None, 6, 6, None]})
_ELT = [DT(4, 20, 10, 0), DT(5, 30, 9, 0), DT(9, 15, 16, 30), DT(6, 21, 8, 0), DT(8, 22, 9, 0), DT(9, 22, 18, 0), DT(9, 23, 11, 0), DT(7, 11, 9, 0), DT(7, 25, 9, 0), DT(9, 19, 10, 0)]
VAL.update({("equipmentLifecycleEvent", "eventType"): ["Commissioning", "Overhaul", "Health Assessment", "Refurbishment", "Upgrade", "Health Assessment", "Replacement Recommendation", "Relocation", "Commissioning", "Health Assessment"],
    ("equipmentLifecycleEvent", "eventAt"): _ELT, ("equipmentLifecycleEvent", "description"): lambda env: TITLES["equipmentLifecycleEvent"][env["i"]],
    ("equipmentLifecycleEvent", "costInr"): ["1850000.00", "640000.00", None, "1125000.00", "780000.00", None, "245000.00", "48000.00", "2300000.00", None],
    ("equipmentLifecycleEvent", "healthScore"): ["98", "86", "61", "90", "95", "72", "54", "93", "99", "68"],
    ("equipmentLifecycleEvent", "lifetimeCyclesAtEvent"): [0, 412000, None, 1580000, 1120000, 1265000, 2040000, 3100000, 0, None],
    ("equipmentLifecycleEvent", "lifetimeRunHoursAtEvent"): ["0.0", "38150.0", "51210.5", "29870.0", "22410.0", "23880.5", "31205.0", "18760.0", "0.0", "40115.0"],
    ("equipmentLifecycleEvent", "approvedAt"): [t + M(240) if a else None for t, a in zip(_ELT, [1, 1, 0, 1, 1, 0, 0, 1, 1, 0])]})
VAL.update({("equipment", "isProductionReady"): [True, False, True, True, True, True, True, True, True, True],
    ("equipment", "readinessReasonText"): [None, "Under maintenance: zone 2 heater replacement (MWO-2026-000347)"] + [None] * 8,
    ("equipment", "healthScore"): ["84", "61", "88", "54", "68", "92", "90", "72", "93", "99"],
    ("equipment", "healthScoreAt"): [DT(9, 24, 23, 0)] * 10,
    ("equipment", "acquisitionCostInr"): ["14500000.00", "21800000.00", "18750000.00", "4200000.00", "16400000.00", "3850000.00", "1850000.00", "2650000.00", "1950000.00", "2300000.00"],
    ("equipment", "plannedReplacementDate"): [DT(11, 30, 0, 0).replace(year=2027), DT(3, 31, 0, 0).replace(year=2027), None, DT(6, 30, 0, 0).replace(year=2027), DT(9, 30, 0, 0).replace(year=2027), None, None, None, None, None]})

# ---------------------------------------------------------------- syst: escalation and alert rules
VAL.update({("escalationRule", "name"): lambda env: MASTER["escalationRule"][env["i"]].split("|")[1],
    ("escalationRule", "sourceType"): ["Breakdown", "Breakdown", "Andon", "Interlock", "Alarm", "Audit", "Alert Rule", "Alert Rule", "Alert Rule", "Nonconformance"],
    ("escalationRule", "severityClass"): ["Critical", None, None, None, "Critical", None, "High", None, "High", None],
    ("escalationRule", "responseTargetMinutes"): [5, 10, 5, 10, 5, 240, 15, 15, 10, 60], ("escalationRule", "resolutionTargetMinutes"): [60, 120, 30, 30, 30, 1440, 60, 120, 45, 1440]})
REFIDX.update({("escalationRule", "lineId"): [5, None, None, None, None, None, 5, None, 5, None], ("escalationRule", "firstResponderRoleId"): [6, 6, 4, 3, 3, 3, 3, 3, 7, 5],
    ("escalationRule", "requiredSkillId"): [None, None, None, None, None, None, None, None, None, None]})
VAL.update({("escalationRuleLevel", "delayMinutes"): [5, 15, 45, 10, 30, 5, 15, 10, 240, 15], ("escalationRuleLevel", "basis"): ["Not Acknowledged", "Not Resolved", "Not Resolved", "Not Acknowledged", "Not Resolved", "Not Acknowledged", "Not Resolved", "Not Acknowledged", "Not Acknowledged", "Not Resolved"],
    ("escalationRuleLevel", "channel"): ["Andon Board", "Mobile App", "SMS", "Mobile App", "Email", "Andon Board", "Mobile App", "Mobile App", "Email", "Mobile App"]})
REFIDX.update({("escalationRuleLevel", "roleId"): [3, 3, 8, 3, 8, 3, 5, 3, 3, 3], ("escalationRuleLevel", "notificationTypeId"): [0, 0, 0, 0, 0, 1, 1, 0, 1, 4]})
VAL.update({("alertRule", "name"): lambda env: MASTER["alertRule"][env["i"]].split("|")[1],
    ("alertRule", "metric"): ["OEE", "Output Gap", "Reject Rate", "Downtime Minutes", "Process Deviation", "Process Deviation", "SPC Rule Violation", "Line-side Stock Cover", "Environment Limit", "Model Anomaly Score"],
    ("alertRule", "comparison"): ["Less Than", "Greater Than", "Greater Than", "Greater Than", "Outside Band", "Less Than", "Greater Than", "Less Than", "Outside Band", "Greater Than"],
    ("alertRule", "thresholdValue"): ["75.0", "30", "1.5", "20", "138.0", "12.8", "0", "45", "800", "0.8"], ("alertRule", "thresholdUpperValue"): [None, None, None, None, "142.0", None, None, None, "1200", None],
    ("alertRule", "evaluationWindowMinutes"): [60, 60, 120, 60, 5, 30, 1, 15, 5, 10], ("alertRule", "severityClass"): ["Medium", "High", "High", "Medium", "High", "Medium", "Medium", "High", "Low", "Medium"],
    ("alertRule", "actionType"): ["Notify", "Notify", "Create Nonconformance", "Notify", "Stop Equipment", "Notify", "Hold", "Notify", "Block Process", "Create Work Order"],
    ("alertRule", "falseAlertCount"): [3, 1, 0, 2, 0, 4, 1, 0, 2, 5]})
REFIDX.update({("alertRule", "lineId"): [5, 5, 5, 0, 5, 5, 2, 5, 6, 5], ("alertRule", "workCenterId"): [None, None, 7, None, 7, 6, 2, None, 9, 6], ("alertRule", "equipmentId"): [None, None, None, 0, 7, 6, 2, None, None, 6],
    ("alertRule", "processTagId"): [None, None, None, None, 7, 6, None, None, None, None], ("alertRule", "itemId"): [None] * 7 + [5, None, None],
    ("alertRule", "notificationTypeId"): [4, 4, 1, 0, 1, 1, 9, 4, 1, 2], ("alertRule", "escalationRuleId"): [7, 6, 9, None, None, None, None, 8, None, None]})
REFIDX.update({("notification", "alertRuleId"): [None, None, None, None, None, None, None, 6, None, None], ("notification", "escalationRuleId"): [1, None, None, None, None, None, 2, None, None, None],
    ("notification", "interlockEventId"): [None, None, None, None, 9, 4, None, None, None, None], ("notification", "resolvedById"): [None] * 10})
VAL.update({("notification", "responseDueAt"): lambda env: cur(env, "raisedAt") + M([5, 15, 30, 60, 15, 15, 5, 10, 60, 1440][env["i"]]),
    ("notification", "resolvedAt"): [None] * 10})

# ---------------------------------------------------------------- syst: analytics models and predictions
VAL.update({("analyticsModel", "name"): lambda env: MASTER["analyticsModel"][env["i"]].split("|")[1],
    ("analyticsModel", "modelType"): ["Vision Classification", "Vision Classification", "Defect Prediction", "OEE Forecast", "Anomaly Detection", "Maintenance Prediction", "Demand Forecast", "Recipe Optimisation", "Operator Risk", "Assignment Recommendation"],
    ("analyticsModel", "modelVersion"): ["1.3", "1.2", "0.9", "2.1", "1.0", "1.4", "1.1", "0.7", "0.5", "0.6"],
    ("analyticsModel", "framework"): ["Keyence XG-X deep learning tool", "Keyence XG-X deep learning tool", "Python scikit-learn gradient boosting", "Python Prophet", "Python isolation forest", "Python survival regression", "Python LightGBM", "Python Bayesian optimisation", "Python logistic regression", "Python linear programming"],
    ("analyticsModel", "trainingDatasetRef"): ["DS-VIS-BOOT-2026-08 (18,400 labelled images)", "DS-VIS-BOOT-2026-05 (9,200 labelled images)", "DS-LKT-2026-Q2 (212,000 tests)", "DS-OEE-ASY01-2025-2026", "DS-NR1-CURVES-2026-07", "DS-LKT-SEAL-LIFE-2025-2026", "DS-CONS-ASY01-2026", "DS-ANO-LOADS-2026", "DS-OPR-2026-H1", "DS-ROSTER-2026-H1"],
    ("analyticsModel", "validationMetricName"): ["Recall NOK", "Recall NOK", "AUC", "MAPE percent", "Precision", "MAE cycles", "MAPE percent", "Coating thickness Cpk", "AUC", "Coverage percent"],
    ("analyticsModel", "validationMetricValue"): ["0.995", "0.981", "0.82", "6.4", "0.88", "1450", "8.1", "1.67", "0.71", "96.0"],
    ("analyticsModel", "effectiveFrom"): [DT(9, 1, 0, 0), DT(5, 20, 0, 0), DT(9, 1, 0, 0), DT(7, 1, 0, 0), DT(8, 1, 0, 0), DT(6, 15, 0, 0), DT(8, 15, 0, 0), DT(11, 1, 0, 0), DT(12, 1, 0, 0), DT(12, 1, 0, 0)],
    ("analyticsModel", "effectiveTo"): [None, DT(8, 31, 0, 0)] + [None] * 8,
    ("analyticsModel", "approvedAt"): [DT(8, 29, 15, 0), DT(5, 18, 11, 0), DT(8, 28, 12, 0), DT(6, 28, 10, 0), DT(7, 30, 16, 0), DT(6, 12, 9, 30), DT(8, 13, 14, 0), DT(9, 25, 11, 0), DT(9, 25, 11, 30), DT(9, 25, 12, 0)]})
REFIDX.update({("analyticsModel", "equipmentId"): [9, 9, None, None, 6, 7, None, 4, None, None], ("analyticsModel", "modelControlledDocumentId"): [None] * 10, ("analyticsModel", "approvedById"): [6] * 10})
_PM = [0, 4, 2, 3, 4, 5, 4, 6, 0, 3]
_PT = [DT(9, 24, 8, 35), DT(9, 15, 14, 21), DT(9, 18, 15, 9), DT(9, 18, 22, 0), DT(9, 21, 7, 35), DT(9, 22, 17, 30), DT(9, 22, 16, 1), DT(9, 24, 7, 55), DT(9, 24, 8, 36), DT(9, 24, 14, 0)]
POST["modelPrediction"] = _poly([("wipUnit", 8), ("equipment", 6), ("wipUnit", 4), ("line", 5), ("equipment", 6), ("tool", 7), ("equipment", 7), ("item", 5), ("wipUnit", 9), ("line", 5)])
REFIDX.update({("modelPrediction", "analyticsModelId"): _PM, ("modelPrediction", "workCenterId"): [9, 6, 7, None, 6, 7, 7, 5, 9, None], ("modelPrediction", "productVariantId"): [0, None, 0, None, None, None, None, None, 0, None],
    ("modelPrediction", "shiftId"): [0, 1, 1, 2, 0, 1, 1, 0, 0, 1], ("modelPrediction", "actionTakenById"): [None, 4, None, None, 4, None, None, None, 3, None], ("modelPrediction", "notificationId"): [None] * 10})
VAL.update({("modelPrediction", "modelVersion"): lambda env: ["1.3", "1.0", "0.9", "2.1", "1.0", "1.4", "1.0", "1.1", "1.3", "2.1"][env["i"]],
    ("modelPrediction", "predictionType"): ["Classification", "Anomaly", "Classification", "Forecast", "Anomaly", "Remaining Useful Life", "Anomaly", "Forecast", "Classification", "Forecast"],
    ("modelPrediction", "predictedAt"): _PT, ("modelPrediction", "horizonMinutes"): [None, None, None, 480, None, None, None, 60, None, 480],
    ("modelPrediction", "predictedClass"): ["OK", "Anomalous rundown", "Pass", None, "Anomalous rundown", None, "Normal", None, "NOK", None],
    ("modelPrediction", "predictedValue"): [None, None, None, "78.5", None, "3200", None, "-44", None, "81.0"],
    ("modelPrediction", "confidence"): ["0.993", "0.86", "0.88", "0.80", "0.91", "0.75", "0.97", "0.83", "0.98", "0.79"],
    ("modelPrediction", "recommendedAction"): [None, "Check the nutrunner socket drive for wear", None, None, "Inspect socket drive for wear", "Plan test seal replacement within 3,200 cycles", None, "Call seal replenishment before 09:30", "Reject: bleed screw cap missing", None],
    ("modelPrediction", "actionStatus"): ["Not Required", "Applied", "Not Required", "Not Required", "Applied", "Pending", "Not Required", "Pending", "Applied", "Not Required"],
    ("modelPrediction", "actionTakenAt"): [None, DT(9, 15, 14, 30), None, None, DT(9, 21, 7, 44), None, None, None, DT(9, 24, 8, 37), None],
    ("modelPrediction", "actualValue"): [None, None, None, "76.9", None, None, None, None, None, None],
    ("modelPrediction", "actualClass"): ["OK", "Socket worn", "Pass", None, "Socket worn", None, "Normal", None, "NOK", None]})
REFIDX.update({("inspectionResult", "analyticsModelId"): [None] * 10})
VAL.update({("inspectionResult", "modelVersion"): [None] * 10, ("inspectionResult", "modelClass"): [None] * 10, ("inspectionResult", "modelConfidence"): [None] * 10,
    ("inspectionResult", "positionNo"): [1, None, 2, None, 3, None, None, None, None, None], ("inspectionResult", "positionName"): ["Bridge, left of centre", None, "Bore depth 20 mm", None, "Bridge top", None, None, None, None, None]})
REFIDX[("inspectionResult", "imageControlledDocumentId")] = [None] * 10

# ---------------------------------------------------------------- syst: simulation studies, record policies, saved views, backups
POST["simulationStudy"] = _poly([("recipe", 7), ("recipe", 4), ("recipe", 6), ("storageLocation", 5), ("line", 5), ("recipe", 0), ("storageLocation", 7), ("recipe", 8), ("equipment", 7), (None, 0)])
REFIDX.update({("simulationStudy", "recommendedRecipeId"): [7, 4, None, None, None, None, None, 8, None, None], ("simulationStudy", "rolloutProductionOrderId"): [7, None, None, None, None, None, None, None, None, None],
    ("simulationStudy", "resultControlledDocumentId"): [None] * 10, ("simulationStudy", "approvedById"): [6, 6, None, 6, None, None, None, None, 6, None]})
_SIM = [DT(9, 16, 10, 0), DT(9, 17, 11, 0), DT(9, 18, 14, 0), DT(9, 19, 10, 0), DT(9, 21, 11, 0), DT(9, 21, 15, 0), DT(9, 22, 10, 0), DT(9, 23, 10, 0), DT(9, 23, 15, 0), DT(9, 24, 11, 0)]
VAL.update({("simulationStudy", "title"): lambda env: TITLES["simulationStudy"][env["i"]],
    ("simulationStudy", "studyType"): ["Process", "Process", "Process", "Inventory", "Process", "Process", "Inventory", "Process", "Calibration Baseline", "Process"],
    ("simulationStudy", "scenarioText"): ["Stabilisation time of both stages reduced by 1.0 s on 5,000 historical curves", "Current density set by number of racks loaded, 12 to 24 racks", "Angle window 20-70 deg added as second criterion",
        "Seal supermarket from 800 to 500 pieces with 45 minute e-Kanban loop", "Second leak tester in parallel at OP080", "Die temperature setpoint lowered by 5 degC with current pour rate",
        "Finished goods buffer from 3 days to 2 days of customer demand", "Marking speed from 800 to 1,000 mm/s at constant power", "Auto-calibration offsets of tester 1 applied to tester 2 of the same model",
        "Press force window 250-900 N recalculated on seals from the second supplier"],
    ("simulationStudy", "inputSnapshotAt"): _SIM, ("simulationStudy", "resultText"): ["Cycle time 24.0 s to 22.0 s; no additional escapes on the 5,000-curve replay", "Coating thickness Cpk from 1.33 to 1.67 predicted", "Angle criterion would have caught both slipping-socket rejects",
        "Stock-out risk below 1 percent at current consumption", "Leak test stops being the constraint; line output +11 percent", "Porosity risk increases; study rejected", "Service level 99.2 percent maintained", None,
        "Baseline transfer valid for testers of the same firmware", "Window 280-900 N recommended"],
    ("simulationStudy", "predictedValue"): ["22.0", "1.67", None, "0.8", "11.0", None, "99.2", None, None, None], ("simulationStudy", "predictedKpi"): ["Cycle time (s)", "Coating thickness Cpk", None, "Stock-out risk (percent)", "Line output increase (percent)", None, "Service level (percent)", None, None, None],
    ("simulationStudy", "actualValue"): ["22.3", None, None, "0.0", None, None, None, None, None, None], ("simulationStudy", "comparisonResult"): ["Equal", None, None, "Better", None, None, None, None, None, None],
    ("simulationStudy", "approvedAt"): [DT(9, 17, 9, 0), DT(9, 18, 10, 0), None, DT(9, 20, 9, 0), None, None, None, None, DT(9, 24, 9, 0), None]})
VAL.update({("recordPolicy", "collectionName"): lambda env: MASTER["recordPolicy"][env["i"]].split("|")[0][4:],
    ("recordPolicy", "editPolicy"): ["No Edit After Lock", "Controlled Edit", "No Edit After Lock", "Append Only", "Append Only", "Append Only", "Controlled Edit", "Controlled Edit", "Controlled Edit", "Append Only"],
    ("recordPolicy", "requiresReasonForEdit"): [True, True, True, False, False, False, True, True, True, False], ("recordPolicy", "requiresSignatureForEdit"): [True, True, True, False, False, False, True, False, False, False],
    ("recordPolicy", "deleteAllowed"): [False] * 8 + [False, False], ("recordPolicy", "retentionYears"): [15, 15, 15, 15, 15, 10, 15, 15, 10, 3], ("recordPolicy", "archiveAfterMonths"): [24, 24, 36, 12, 12, 24, None, 36, None, 6]})
REFIDX.update({("recordPolicy", "lockOnStatusDefinitionId"): [None] * 10, ("recordPolicy", "editRoleId"): [None, 5, None, None, None, None, 8, 5, 9, None]})
VAL.update({("savedView", "name"): lambda env: MASTER["savedView"][env["i"]].split("|")[1],
    ("savedView", "viewType"): ["Comparison", "Pareto", "Comparison", "Pareto", "List", "Trend", "List", "Pareto", "Trend", "List"],
    ("savedView", "collectionName"): ["u_mes_perf_oeeRecord", "u_mes_perf_lossSummary", "u_mes_perf_oeeRecord", "u_mes_perf_leakTestResult", "u_mes_qual_nonconformance", "u_mes_maint_reliabilitySummary", "u_mes_matl_materialDemandForecast", "u_mes_qual_defectRecord", "u_mes_perf_productionCount", "u_mes_maint_maintenancePlan"],
    ("savedView", "filterJson"): ['{"lineName":"Front Caliper Assembly Line 1","periodStartAt":{"$gte":"-7d"}}', '{"lineName":"Front Caliper Assembly Line 1","productionDate":{"$gte":"thisWeek"}}', '{"periodStartAt":{"$gte":"thisMonth"}}',
        '{"verdict":"Fail"}', '{"status":{"$in":["Open","Contained"]},"detectedAt":{"$lt":"-24h"}}', '{"periodType":"Month"}', '{"lineName":"Front Caliper Assembly Line 1","status":"Calculated"}', '{"isFirstFail":true}', '{"productionDate":"today"}', '{"nextDueAt":{"$lt":"today"}}'],
    ("savedView", "sortJson"): ['{"oeePct":-1}', '{"lossMinutes":-1}', '{"oeePct":-1}', '{"testedAt":-1}', '{"detectedAt":1}', '{"mtbfHours":1}', '{"projectedShortageAt":1}', '{"quantity":-1}', '{"hourStartAt":1}', '{"nextDueAt":1}'],
    ("savedView", "isShared"): [True, True, True, False, True, True, False, True, True, True]})
REFIDX.update({("savedView", "ownerUserId"): [4, 4, 6, 3, 3, 5, 7, 3, 4, 5], ("savedView", "roleId"): [3, 3, None, None, 5, 6, None, 5, 3, 6]})
_BK = [DT(9, 15, 1, 0), DT(9, 16, 1, 0), DT(9, 17, 1, 0), DT(9, 18, 1, 0), DT(9, 19, 1, 0), DT(9, 20, 1, 0), DT(9, 20, 10, 0), DT(9, 21, 1, 0), DT(9, 22, 1, 0), DT(9, 27, 10, 0)]
VAL.update({("backupRun", "runType"): ["Incremental Backup", "Incremental Backup", "Incremental Backup", "Incremental Backup", "Incremental Backup", "Full Backup", "Restore Test", "Incremental Backup", "Incremental Backup", "Failover Test"],
    ("backupRun", "startedAt"): _BK, ("backupRun", "completedAt"): [b + M(m) for b, m in zip(_BK, [18, 17, 19, 18, 6, 142, 64, 18, 19, 9])],
    ("backupRun", "sizeBytes"): [6.1e9, 5.9e9, 6.4e9, 6.2e9, 0.8e9, 186.4e9, 186.4e9, 6.0e9, 6.3e9, None], ("backupRun", "storageTarget"): ["NAS-PN1-BK01"] * 5 + ["NAS-PN1-BK01 and offsite copy, Pune data centre", "Restore server PN1-MES-RST01", "NAS-PN1-BK01", "NAS-PN1-BK01", "Standby cluster PN1-MES-DR"],
    ("backupRun", "recoveryTimeMinutes"): [None] * 6 + [64, None, None, 9], ("backupRun", "recoveryPointMinutes"): [None] * 6 + [60, None, None, 1]})
VAL[("backupRun", "sizeBytes")] = [None if v is None else int(v) for v in VAL[("backupRun", "sizeBytes")]]
REFIDX.update({("backupRun", "evidenceControlledDocumentId"): [None] * 10, ("backupRun", "performedById"): [9] * 6 + [8, 9, 9, 8]})

# ---------------------------------------------------------------- relationship and child collections of existing masters
REFIDX[("statusTransitionRole", "roleId")] = [3, 3, 3, 3, 4, 3, 3, 5, 3, 3]
REFIDX.update({("storageLocationAllowedItem", "itemId"): [4, 5, 6, 7, 8, 3, 9, 9, 0, None], ("storageLocationAllowedItem", "itemGroupId"): [None] * 9 + [0]})
REFIDX.update({("maintenanceWorkOrder", "shiftId"): [0, 1, 2, 0, 1, 2, 0, 1, 2, 0], ("maintenanceWorkOrder", "rootCauseCodeId"): [0, 1, 2, 3, 4, 5, 6, None, None, 9],
    ("maintenanceWorkOrder", "closureApprovedById"): [None, None, 6, None, 6, 6, None, None, None, None], ("maintenanceWorkOrder", "andonEventId"): [0, 1, None, None, None, None, 6, None, None, None]})
VAL.update({("maintenanceWorkOrder", "closureApprovedAt"): lambda env: (cur(env, "completedAt") + M(90)) if env["status"] == "Closed" else None,
    ("maintenanceWorkOrder", "priorityScore"): ["72", "88", "65", "30", "58", "70", "84", "77", "45", "52"], ("maintenanceWorkOrder", "schedulingSource"): ["Manual", "Rule", "Manual", "Rule", "Manual", "Manual", "Rule", "Model", "Rule", "Manual"],
    ("maintenanceWorkOrder", "slaResponseDueAt"): lambda env: cur(env, "reportedAt") + M(10),
    ("maintenanceWorkOrder", "slaRepairDueAt"): lambda env: cur(env, "reportedAt") + M(120)})
REFIDX.update({("andonEvent", "equipmentId"): [0, 1, None, None, 4, None, 6, 7, None, None], ("andonEvent", "maintenanceWorkOrderId"): [0, 1, None, None, None, None, 6, None, None, None],
    ("andonEvent", "escalationRuleId"): [1, 1, 2, None, 2, 8, 2, 2, None, 8]})
VAL[("andonEvent", "severityClass")] = ["High", "Medium", "Medium", "Low", "Medium", "Medium", "High", "High", "Low", "Medium"]
VAL[("andonType", "targetRepairSec")] = [1800, 1200, 3600, 600, 900, 1800, 2700, 1800, 600, 1200]
REFIDX[("andonType", "escalationRuleId")] = [2, 8, 1, None, None, None, None, None, None, None]
REFIDX.update({("toolLifeRecord", "workCenterId"): list(range(10)), ("toolLifeRecord", "itemId"): [3, 3, 2, 2, 2, 0, 0, 0, 0, 0], ("toolLifeRecord", "operationExecutionId"): [None] * 10})
VAL.update({("tool", "blockAtLifeLimit"): [True, False, True, False, False, True, True, True, False, False],
    ("tool", "lastCertifiedAt"): [None, None, None, None, None, None, None, DT(9, 1, 10, 0), DT(8, 4, 10, 0), DT(8, 18, 10, 0)],
    ("tool", "certificationDueDate"): [None, None, None, None, None, None, None, DT(12, 1, 0, 0), DT(11, 4, 0, 0), DT(9, 18, 0, 0)]})
REFIDX[("tool", "certificateControlledDocumentId")] = [None] * 10
REFIDX[("gauge", "equipmentId")] = [None, None, None, None, None, None, 6, 7, None, None]
REFIDX.update({("processTag", "areaId"): [0, 1, 2, 3, 3, 4, 4, 4, 4, 5], ("processTag", "lineId"): [0, 1, 2, 3, 4, 5, 5, 5, 5, 6], ("processTag", "workCenterId"): list(range(10))})
REFIDX.update({("processReading", "areaId"): [0] * 10, ("processReading", "shiftId"): None})
REFIDX.update({("productionOrder", "qualityHoldId"): [None] * 7 + [0, None, None], ("productionOrder", "holdReasonCodeId"): [None] * 7 + [5, None, None]})
VAL.update({("productionOrder", "onHold"): [False] * 7 + [True, False, False], ("productionOrder", "genealogyComplete"): [True, False, True, True, False, False, True, False, False, False]})
VAL.update({("operationExecution", "recipeVersion"): lambda env: (lambda r: None if r is None else str(env["docs_of"]("recipe")[[d["_id"] for d in env["docs_of"]("recipe")].index(r)]["version"][1]))(env["doc"].get("recipeId")),
    ("operationExecution", "recipeChecksum"): lambda env: (lambda r: None if r is None else env["docs_of"]("recipe")[[d["_id"] for d in env["docs_of"]("recipe")].index(r)]["checksum"])(env["doc"].get("recipeId")),
    ("operationExecution", "taktTimeSec"): [None, "36.0", "36.0", "36.0", "36.0", "36.0", "36.0", "36.0", "36.0", "36.0"],
    ("operationExecution", "taktBreached"): [False, False, False, False, True, False, True, False, True, False],
    ("operationExecution", "captureMethod"): ["PLC Signal", "Scan", "Scan", "Scan", "Scan", "Scan", "Scan", "Scan", "Scan", "Scan"],
    ("operationExecution", "startScanCode"): lambda env: None if env["i"] == 0 else raw(env, "serialNumber", [None, 0, 1, 2, 3, 4, 5, 6, 7, 8][env["i"]], "dataMatrixPayload"),
    ("operationExecution", "checksVariantVerified"): [True] * 10, ("operationExecution", "checksDocumentAcknowledged"): [True] * 10, ("operationExecution", "checksEquipmentReady"): [True] * 10,
    ("operationExecution", "checksMaterialReleased"): [True] * 10, ("operationExecution", "checksSetupVerified"): [True] * 10, ("operationExecution", "checksEnvironmentOk"): [True] * 10})
REFIDX[("operationExecution", "productVariantId")] = [None, 0, 0, 1, 1, 0, 0, 2, 2, 0]
REFIDX.update({("stepCompletion", "overrideReasonCodeId"): [None, None, 6, None, None, 7, None, None, 9, None]})
VAL[("stepCompletion", "arSessionRef")] = [None] * 10
REFIDX.update({("labourBooking", "operationExecutionId"): [None, 1, 2, None, 4, 5, None, None, None, None], ("labourBooking", "productVariantId"): [None, 0, 0, None, 1, 0, None, None, None, None],
    ("labourBooking", "operatorSessionId"): [None, 0, 1, None, 3, 4, None, None, None, None]})
VAL.update({("kitLine", "itemRevision"): ["C", "B", "A", "B", "A", "C", "B", "A", "B", "A"], ("kitLine", "isMandatory"): [True] * 8 + [False, True],
    ("kitLine", "verificationResult"): ["Match", "Match", "Match", "Match", "Wrong Revision", "Match", "Match", "Not Scanned", "Match", "Match"]})
VAL[("kitLine", "scannedItemRevision")] = lambda env: None if env["i"] == 7 else ("A" if env["i"] == 4 else VAL[("kitLine", "itemRevision")][env["i"]])
REFIDX.update({("trac_unused", "x"): None})
VAL.update({("serialNumber", "markingRecipeVersion"): [None] * 8 + ["1", "1"]})
REFIDX[("serialNumber", "markingRecipeId")] = [None] * 8 + [8, 8]
def _rcp(key):
    def f(env):
        r = env["doc"].get("recipeId")
        if not isinstance(r, str): return None
        for d in env["docs_of"]("recipe"):
            if d["_id"] == r:
                v = d[key]; return str(v[1]) if isinstance(v, tuple) else v
        return None
    return f
VAL.update({("asBuiltRecordOperation", "recipeVersion"): _rcp("version"), ("asBuiltRecordOperation", "recipeChecksum"): _rcp("checksum")})
REFIDX.update({("genealogyLink", "childSerialNumberId"): [None] * 10, ("genealogyLink", "childWipUnitId"): [None] * 10})
VAL.update({("asBuiltRecord", "genealogyComplete"): [False, True, True, True, True, True, True, False, True, True], ("asBuiltRecord", "missingComponentCount"): [1, 0, 0, 0, 0, 0, 0, 1, 0, 0]})
VAL.update({("spcSample", "reactionType"): lambda env: None if cur(env, "inControl") else ["Alert", "Hold", "Recheck"][env["i"] % 3]})
REFIDX.update({("spcSample", "qualityHoldId"): [None] * 10, ("spcSample", "notificationId"): [None] * 7 + [7, None, None]})
REFIDX.update({("reworkOrder", "reasonCodeId"): [7, 7, 6, 7, 9, 7, 6, 8, 7, 6], ("reworkOrder", "releasedById"): [None, None, None, 3, None, None, None, None, 3, None]})
VAL[("reworkOrder", "releasedAt")] = lambda env: (cur(env, "reinspectedAt") + M(10)) if env["status"] == "Completed" and cur(env, "reinspectedAt") else None
REFIDX.update({("scrapRecord", "serialNumberId"): [None] * 7 + [7, None, None], ("scrapRecord", "dispositionTypeId"): [2] * 10})
REFIDX.update({("qualityHold", "releaseReasonCodeId"): [None, 7, 1, 4, 0, 2, None, 6, 8, 9], ("qualityHold", "releaseElectronicSignatureId"): [None] * 10})
VAL.update({("workInstruction", "reacknowledgeOnRevision"): [False, False, True, False, False, True, True, True, True, True],
    ("workInstruction", "generationSource"): ["Manual"] * 9 + ["Generated From Bill Of Process"]})
REFIDX[("workInstruction", "sourceBillOfProcessId")] = [None] * 9 + [0]
REFIDX[("workInstructionStep", "arContentControlledDocumentId")] = [None] * 10
VAL[("workInstructionStep", "arAnchorRef")] = [None] * 10
VAL.update({("recipe", "isGoldenRecipe"): [False, True, True, False, True, False, True, True, False, False], ("recipe", "origin"): ["Engineering", "Engineering", "Engineering", "Engineering", "Optimisation Model", "Engineering", "Engineering", "Simulation Study", "Engineering", "Engineering"],
    ("recipe", "changeReasonText"): [None, "Ageing time extended from 6 to 7 hours", "Finish boring feed reduced for bore Cpk", None, "Current density by rack count", None, "Torque window 14 +/- 2 N.m per drawing revision D", "Stabilisation time 4.0 s after study SIM-2026-014", None, "RH layout added plant code"],
    ("recipe", "goldenDesignatedAt"): [None, DT(7, 2, 11, 0), DT(8, 12, 15, 0), None, DT(9, 10, 10, 0), None, DT(9, 2, 10, 0), DT(9, 17, 9, 30), None, None]})
REFIDX.update({("recipe", "previousVersionRecipeId"): [None] * 10, ("recipe", "goldenDesignatedById"): [None, 6, 6, None, 6, None, 6, 6, None, None], ("recipe", "analyticsModelId"): [None, None, None, None, 7, None, None, None, None, None]})
VAL[("recipe", "releasedAt")] = lambda env: cur(env, "effectiveFrom")
VAL.update({("shiftRosterAssignment", "assignmentSource"): ["Manual", "Manual", "Rule", "Manual", "Manual", "Rule", "Manual", "Model", "Manual", "Manual"],
    ("shiftRosterAssignment", "suggestionScore"): [None, None, "0.82", None, None, "0.77", None, "0.91", None, None]})
VAL.update({("skillCertification", "trainedDocumentRevision"): ["1", "4", "1", "3", "2", "1", "2", "3", "1", "3"], ("skillCertification", "requalificationRequired"): [False, False, False, False, False, False, False, False, True, False],
    ("skillCertification", "revocationSource"): lambda env: {"Expired": "Expiry", "Revoked": "Assessment Failure"}.get(env["status"])})

def apply(ns):
    """merge into the namespace of sample_rules.py"""
    from sample_universe import MASTER as _M, TITLES as _T
    def rows(t): return [l for l in t.strip().split("\n")]
    for k, v in MASTER_ADD.items(): _M[k] = rows(v)
    for k, v in TITLES_ADD.items(): _T[k] = rows(v)
    ns["RECFMT"].update(RECFMT); ns["STATUSOF"].update(STATUSOF); ns["PARENTIDX"].update(PARENTIDX); ns["POST"].update(POST)
    for k, v in REFIDX.items():
        if v is None: ns["REFIDX"].pop(k, None)
        elif k[0] != "trac_unused": ns["REFIDX"][k] = v
    ns["VAL"].update(VAL)
    ns["CTXOF"].update(CTXOF)
    ns["OBS"] = obs(ns["OBS"])
    for e in AUDITFIX:
        old = ns["POST"].get(e)
        ns["POST"][e] = (lambda o: (lambda env: (o(env) if o else None, _audit_fix(env))))(old)

REFIDX[("downtimeEvent", "capaId")] = [None] * 6 + [6, 7, None, None]
# two mid-shift re-allocations: the operator joins the station at 18:00 / 10:00 and stays to shift end
VAL.update({("shiftRosterAssignment", "assignedFromAt"): [None, None, None, DT(9, 15, 18, 0), None, None, None, DT(9, 17, 10, 0), None, None],
    ("shiftRosterAssignment", "assignedToAt"): [None, None, None, DT(9, 15, 22, 0), None, None, None, DT(9, 17, 14, 0), None, None]})

OBS_ROW1_OLD = "| 1 | u_mes_prod_recipe | recipeType has no allowed value for an assembly press program or a vision job | The recipes at those two positions are a second tightening program and a second laser marking layout; executions at the press and at final inspection carry no recipe |"
OBS_ROW1_NEW = "| 1 | u_mes_prod_recipe | Resolved on 12 Oct 2026 (MES_ExternalRequirement_01): recipeType now allows Press Program, Dispensing Program and Vision Job | The ten sample recipes are unchanged; executions at the press and at final inspection still carry no recipe |"
OBS_ADD = """| 7 | u_mes_perf_reasonCode | The reason types added on 12 Oct 2026 (Hold Release, Interlock Override, Rework, Root Cause, Alarm Closure, Exposure Reset) have no sample reason code, because the ten sample codes are downtime causes | Hold, override, rework, root-cause, alarm-closure and reset references point to the downtime cause that fits the story |
| 8 | u_mes_qual_inspectionResult | positionNo, model and image keys are filled only where a sample result fits; no sample result was classified by a vision model | Model classifications are shown in u_mes_syst_modelPrediction |
| 9 | u_mes_mast_unitOfMeasure | The ten sample units have no newton, degree or millisecond | Curve envelope axis units are held as text (xUnitText, yUnitText), as delivered by the controller |
| 10 | u_mes_qual_measurementCurvePoint | A time-series collection; ten points of one press-in curve are shown, one second apart because the shell format carries whole seconds | Real curves carry 250 to 620 points each |
| 11 | u_mes_trac_genealogyLink | childSerialNumberId and childWipUnitId are empty, because all sample components are bought-in lots | Sub-assemblies serialised by the MES would use them |
"""
def obs(text):
    text = text.replace("Nothing was added to or removed from any collection. These points were noticed while filling the documents and are reported only.",
        "These points were noticed while filling the documents and are reported only. On 12 Oct 2026 the 44 collections and 212 keys of MES_ExternalRequirement_01 were added (D036-D042).")
    text = text.replace(OBS_ROW1_OLD, OBS_ROW1_NEW)
    marker = "\n## How realistic the documents are"
    text = text.replace(marker, OBS_ADD + marker, 1) if OBS_ADD not in text else text
    text = text.replace("- Built by the same rules but not read line by line: the remaining collections.",
        "- Written collection by collection for MES_ExternalRequirement_01: the 44 new collections and the 212 added keys (05_generator/ext_req01_samples.py).\n- Built by the same rules but not read line by line: the remaining collections.")
    return text

# keep the existing tool classes; the three fixtures get the new value Fixture
VAL[("tool", "toolClass")] = ["Production Tooling", "Customer Owned Tooling", "Consumable Tooling", "Fixture", "Customer Owned Tooling", "Consumable Tooling", "Production Tooling", "Customer Owned Tooling", "Fixture", "Fixture"]
# new due-date and calendar-date keys must not move the audit timestamps of existing documents
_EXCL = {"productionDate", "dueDate", "responseDueAt", "slaResponseDueAt", "slaRepairDueAt", "assignedFromAt", "assignedToAt", "nextDueDate", "certificationDueDate", "plannedReplacementDate"}
def _audit_fix(env):
    d = env["doc"]
    if not d.get("createdAt"): return
    lo, hi = datetime.datetime(2026, 9, 14), datetime.datetime(2026, 10, 1)
    ev = [v[1] for k, v in d.items() if isinstance(v, tuple) and v[0] == "date" and k not in ("createdAt", "updatedAt") and k not in _EXCL and lo <= v[1] < hi]
    base = env["base"]
    c = min([x for x in ev if x >= base - datetime.timedelta(days=1)] + [base])
    d["createdAt"] = ("date", c); d["updatedAt"] = ("date", max(ev + [c]))
AUDITFIX = {"processReading", "alarm", "audit", "notification", "maintenanceWorkOrder", "shiftRosterAssignment"}
