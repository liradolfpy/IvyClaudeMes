"""Sample-data rules for the collections and keys added by UNS_01 (Unified Namespace on Azure IoT Hub, D083).
Merged into sample_rules.py by apply(), after gmp01_samples; same universe, same IDs and names (Auto universe only; the new collections
are not part of the Gamp universe, because the pharma site RJ1 is outside the UNS scope).
Index conventions: equipment and IoT devices 0-9 = GDC-01-M1, HT-01-F1, CNC-01-H1, WSH-01-W1, ANO-01-L1, ASY-01-P1, TRQ-01-N1, LKT-01-T1, LSR-01-L1, FIN-01-V1.
Users: 3 Anita Kulkarni (quality), 5 Imran Shaikh (maintenance), 8 Sneha Joshi (process engineering and MES), 9 MES System.
Story: identities provisioned on 14 September 2026, the evening before the production fortnight; ten rejected messages over the fortnight,
each tied to a real event of the samples (alarm A2031 on 17 September, leak test LKT-2026-000377 on 18 September) or to a commissioning issue."""
import datetime, hashlib, json, uuid
from gmp01_samples import _audit

def DT(m, d, h=0, mi=0, s=0, y=2026): return datetime.datetime(y, m, d, h, mi, s)
NS = uuid.UUID("6f1d2c3b-8a47-4e59-9b0c-7d2e1f4a5b6c")      # namespace of the deterministic sample message ids
def muuid(text): return str(uuid.uuid5(NS, text))
def iso(dt): return dt.strftime("%Y-%m-%dT%H:%M:%S.000+05:30")

MASTER_ADD = {
"unsMessageType": """edge.state|Equipment state
edge.tag|Process tag value
edge.alarm|Alarm
edge.count|Cycle count
edge.result.tightening|Tightening result
edge.result.curve|Measurement curve
edge.result.leakTest|Leak test result
edge.energy|Energy interval
mes.context.workCenter|Work center context
kpi.oee|Equipment OEE""",
"iotHubIdentity": """PN1-EGW-FDY-01|IoT Edge gateway, foundry
PN1-EGW-ASY-01|IoT Edge gateway, assembly and test
PN1-EGW-FIP-01|IoT Edge gateway, final inspection and packing
PN1-GDC-01-M1|Gravity Die Casting Machine 1
PN1-ASY-01-P1|Piston Assembly Press 1
PN1-TRQ-01-N1|DC Nutrunner Station 1
PN1-LKT-01-T1|Pressure Leak Tester 1
PN1-LSR-01-L1|Fibre Laser Marker 1
PN1-FIN-01-V1|Final Inspection Vision Station
PN1-MES|MES publisher, Chakan plant""",
}
TITLES_ADD = {}
RECFMT = {}
STATUSOF = {"unsMessageType": ["Active"] * 10, "iotHubIdentity": ["Active"] * 10,
            "unsRejectedMessage": ["Resent", "Discarded", "Resent", "Resent", "Open", "Discarded", "Discarded", "Open", "Resent", "Open"]}
PARENTIDX = {}
REFIDX = {}
VAL = {}
POST = {}
CTXOF = {}
def _tl(e, k, lst): VAL[(e, k)] = lst
def _r(e, k, lst): REFIDX[(e, k)] = lst

# ---------------------------------------------------------------- unsMessageType
E = "unsMessageType"
VAL[(E, "name")] = lambda env, E=E: MASTER_ADD[E].split("\n")[env["i"]].split("|")[1]
_tl(E, "description", [
    "Running, idle, setup, down, starved, blocked or planned stop of one piece of equipment, sent on every change of state",
    "Value of one process tag, sent when it moves by more than the tag deadband or when the scan interval has passed",
    "Raised, acknowledged and cleared states of one equipment alarm",
    "Increment of the cycle or shot counter with good and reject counts and cycle time",
    "Result of one tightening: program, joint, torque and angle with their limits, rundown time and verdict",
    "All points of one measurement curve (torque-angle, press force-displacement, pressure decay)",
    "Result of one two-stage pressure leak test with both stages and the verdict",
    "Consumption of one energy meter over a 15-minute interval with demand and power factor",
    "Current order, item, operation, recipe, unit, operator and shift of one work center, sent on every change",
    "Availability, performance, quality and OEE of one piece of equipment for the shift"])
_tl(E, "unsNamespace", ["Edge"] * 8 + ["MES", "KPI"])
_tl(E, "messageTypeCode", ["state", "tag", "alarm", "count", "result.tightening", "result.curve", "result.leakTest", "energy", "context.workCenter", "oee"])
VAL[(E, "payloadSchemaName")] = lambda env: "uns." + env["rec"]
_tl(E, "payloadSchemaVersion", [1] * 10)
_tl(E, "messageClass", ["State", "Measurement", "State", "Event", "Event", "Event", "Event", "Event", "State", "State"])
_tl(E, "hierarchyLevel", ["Equipment"] * 8 + ["Work Center", "Equipment"])
_tl(E, "senderType", ["IoT Edge Gateway"] * 8 + ["MES Publisher"] * 2)
_tl(E, "targetCollectionName", ["u_mes_perf_equipmentState", "u_mes_perf_processReading", "u_mes_perf_alarm", "u_mes_perf_productionCount",
    "u_mes_perf_torqueResult", "u_mes_qual_measurementCurve", "u_mes_perf_leakTestResult", "u_mes_perf_energyReading", None, None])
_tl(E, "twinPropertyPath", ["properties.reported.state", "properties.reported.tags", "properties.reported.activeAlarms", None, None, None, None, None,
    "properties.desired.mesContext", "properties.reported.kpi.oee"])
_tl(E, "ingestedByMes", [True] * 8 + [False, False])
_tl(E, "routedToDataLake", [True] * 10)

# ---------------------------------------------------------------- iotHubIdentity
E = "iotHubIdentity"
VAL[(E, "name")] = lambda env, E=E: MASTER_ADD[E].split("\n")[env["i"]].split("|")[1]
_tl(E, "identityType", ["IoT Edge Gateway"] * 3 + ["Equipment"] * 6 + ["MES Publisher"])
_tl(E, "iotHubName", ["iothub-vbs-pn1"] * 10)
_r(E, "equipmentId", [None, None, None, 0, 5, 6, 7, 8, 9, None])
_r(E, "iotDeviceId", [None, None, None, 0, 5, 6, 7, 8, None, None])
_r(E, "parentIotHubIdentityId", [None, None, None, 0, 1, 1, 1, 1, 2, None])
_tl(E, "authenticationMethod", ["X.509 CA Signed"] * 10)
VAL[(E, "certificateThumbprint")] = lambda env: hashlib.sha1(("plant-ca/" + env["rec"]).encode()).hexdigest().upper()
_tl(E, "certificateExpiresAt", [DT(12, 31, 23, 59, 59, y=2027)] * 3 + [DT(8, 31, 23, 59, 59, y=2027)] * 6 + [DT(6, 30, 23, 59, 59, y=2027)])
_tl(E, "provisioningStatus", ["Provisioned"] * 8 + ["Sync Failed", "Provisioned"])
_tl(E, "lastRegistrySyncAt", [DT(9, 14, 18, 0), DT(9, 14, 18, 1), DT(9, 14, 18, 2), DT(9, 14, 18, 5), DT(9, 14, 18, 6), DT(9, 14, 18, 6),
    DT(9, 14, 18, 7), DT(9, 14, 18, 7), None, DT(9, 14, 17, 55)])
_tl(E, "twinTagsVersion", [1, 1, 1, 1, 1, 1, 1, 1, 0, 1])
_tl(E, "lastSyncErrorText", [None] * 8 + ["23 Sep 2026 08:10: twin tags not written; no controller device is registered for FIN-01-V1 in u_mes_syst_iotDevice, so equipmentId and the device link cannot be set", None])
_tl(E, "connectionState", ["Connected", "Connected", "Connected", "Connected", "Connected", "Connected", "Disconnected", "Connected", "Connected", "Connected"])
_tl(E, "connectionStateAt", [DT(9, 14, 18, 20), DT(9, 14, 18, 21), DT(9, 14, 18, 22), DT(9, 14, 18, 30), DT(9, 14, 18, 31), DT(9, 14, 18, 31),
    DT(9, 25, 14, 2, 31), DT(9, 14, 18, 32), DT(9, 23, 8, 11, 40), DT(9, 14, 18, 15)])

# ---------------------------------------------------------------- unsRejectedMessage
E = "unsRejectedMessage"
_PATH = {3: "VBS/PN1/FDY/GDC-01/GDC-01/GDC-01-M1", 4: "VBS/PN1/ASY/ASY-01/ASY-01/ASY-01-P1", 5: "VBS/PN1/ASY/ASY-01/TRQ-01/TRQ-01-N1",
         6: "VBS/PN1/ASY/ASY-01/LKT-01/LKT-01-T1", 8: None}
_PROD = {3: "PLC-GDC-01", 4: "PR-CTRL-01", 5: "NR-CTRL-01", 6: "LKT-CTRL-01", 8: "PRN-FIN-01"}
# identity, message type, equipment, schema in the envelope, envelope ts, received, reason, detail, data, resolver, resolved, resolution text
_RM = [
 (5, 4, 6, "uns.edge.result.tightening/1", DT(9, 15, 6, 4, 8), DT(9, 15, 6, 4, 9), "Unresolved Master Reference",
  "data.unitId U260915A0198 not found among the WIP units; the unit label was printed but the WIP unit was not created at piston and seal assembly",
  {"controllerResultNo": "PF6-000418874", "unitId": "U260915A0198", "programNo": "PSET-07", "jointName": "Bleed screw M10x1.0", "tighteningNo": 1,
   "strategy": "Torque Control", "targetTorqueNm": 14.0, "minTorqueNm": 12.0, "maxTorqueNm": 16.0, "finalTorqueNm": 14.1, "targetAngleDeg": 40.0,
   "minAngleDeg": 20.0, "maxAngleDeg": 70.0, "finalAngleDeg": 39.2, "rundownTimeMs": 1810, "result": "OK"},
  8, DT(9, 15, 9, 40), "WIP unit U260915A0198 created by the supervisor after checking the unit at the station; message sent again and stored"),
 (3, 1, 0, "uns.edge.tag/1", DT(9, 16, 3, 58, 12), DT(9, 15, 22, 14, 5), "Clock Skew",
  "ts 2026-09-16T03:58:12.000+05:30 is 5 h 44 min ahead of the time of receipt; the PLC clock was not synchronised after the power interruption at 21:50",
  {"tag": "PN1.GDC01.DIE_TEMP_UPPER", "value": 398.2, "unit": "Degree Celsius", "quality": "Good"},
  5, DT(9, 15, 23, 5), "PLC clock synchronised again to the NTP source of the gateway; the 37 readings sent between 22:14 and 22:51 discarded and the gap recorded in the shift handover"),
 (6, 6, 7, "uns.edge.result.leakTest/1", DT(9, 16, 10, 31, 2), DT(9, 16, 10, 31, 3), "Validator Failure",
  "stages[0].leakRateSccm missing; u_mes_perf_leakTestResultStage requires leakRateSccm",
  {"unitId": "U260916A0221", "programNo": "LT-03", "testMedium": "Dry Air", "ambientTemperatureC": 26.9, "partTemperatureC": 27.5, "verdict": "Pass",
   "failureReason": None, "stages": [{"stageNo": 1, "stageName": "Low Pressure", "testPressureBar": 5.0, "pressureDropPa": 0.0, "stageResult": "Pass"}]},
  8, DT(9, 16, 11, 20), "The leak tester protocol module dropped the leak rate when the pressure decay was below the resolution of the tester; module corrected to send 0.00 and the message sent again"),
 (3, 2, 0, "uns.edge.alarm/2", DT(9, 17, 6, 51, 40), DT(9, 17, 6, 51, 41), "Unknown Schema",
  "schema uns.edge.alarm/2 is not in u_mes_syst_unsMessageType; the gateway module of the foundry was updated overnight to version 2 of the alarm payload",
  {"alarmCode": "A2031", "alarmText": "Die temperature upper half above high limit", "alarmClass": "Process", "severity": 8, "alarmState": "Raised",
   "tag": "PN1.GDC01.DIE_TEMP_UPPER", "triggerValue": 421.0, "limitValue": 420.0, "operatorHint": "Check die coat thickness"},
  8, DT(9, 17, 8, 15), "Gateway module rolled back to schema version 1 until version 2 is approved; alarm A2031 sent again in version 1 and stored as ALM-2026-000176"),
 (6, 5, 7, "uns.edge.result.curve/1", DT(9, 18, 15, 11, 33), DT(9, 18, 15, 11, 35), "Unresolved Master Reference",
  "data.resultRef LT-03-000377 matches no leak test result of unit U260918B0236; the curve arrived before its result message",
  {"resultRef": "LT-03-000377", "unitId": "U260918B0236", "xQuantity": "Time", "xUnit": "Millisecond", "yQuantity": "Pressure drop", "yUnit": "Pascal",
   "sampleIntervalMs": 20, "points": [[0, 0.0], [1000, 81.0], [2000, 166.0], [3000, 248.0], [4000, 331.0], [5000, 412.0]]},
  None, None, None),
 (4, 5, 5, "uns.edge.result.curve/1", DT(9, 21, 11, 2, 10), DT(9, 21, 11, 2, 11), "Invalid Envelope",
  "envelope fields seq and producer missing; the message was sent by the press supplier's test tool during commissioning of press program PR-12",
  {"resultRef": "TEST-PR-12-001", "unitId": "TEST", "xQuantity": "Displacement", "xUnit": "Millimetre", "yQuantity": "Force", "yUnit": "Newton",
   "sampleIntervalMs": 5, "points": [[0.0, 0.0], [20.0, 310.0], [41.9, 1180.0]]},
  5, DT(9, 21, 11, 30), "Test message of the supplier tool; the tool's access to the gateway removed and the message discarded"),
 (5, 3, 6, "uns.edge.count/1", DT(9, 22, 14, 0, 6), DT(9, 22, 14, 0, 7), "Validator Failure",
  "data.increment -418871 is negative; the controller counter restarted from zero after a firmware restart",
  {"counter": "TighteningCounter", "counterValue": 0, "increment": -418871, "good": 0, "reject": 0, "cycleTimeSec": 0.0},
  5, DT(9, 22, 14, 30), "Counter reset after the controller restart; message discarded and the counter baseline reset in the gateway"),
 (8, 0, 9, "uns.edge.state/1", DT(9, 23, 8, 12, 0), DT(9, 23, 8, 12, 1), "Unresolved Master Reference",
  "enrichment properties isa95Path and equipmentId missing; the twin tags of PN1-FIN-01-V1 were never written because the registry sync failed",
  {"stateCode": "Running", "subStateCode": "Auto Cycle", "plcStateCode": "1", "faultCode": None},
  None, None, None),
 (3, 3, 0, "uns.edge.count/1", DT(9, 24, 10, 5, 15), DT(9, 24, 10, 5, 16), "Validator Failure",
  "data.good 3 exceeds data.increment 2; the good count was read from the wrong PLC address",
  {"counter": "ShotCounter", "counterValue": 1291514, "increment": 2, "good": 3, "reject": 0, "cycleTimeSec": 96.0},
  8, DT(9, 24, 11, 0), "Good count mapping corrected in the gateway (cavity good counter); message sent again with good 2"),
 (6, 0, 7, None, None, DT(9, 25, 14, 2, 30), "Invalid Envelope",
  "body is not valid JSON: truncated after 96 bytes when the connection of PN1-LKT-01-T1 dropped at 14:02",
  None, None, None, None),
]
RECFMT[E] = lambda i, j: ["URM-20260915-00001", "URM-20260915-00002", "URM-20260916-00003", "URM-20260917-00004", "URM-20260918-00005",
    "URM-20260921-00006", "URM-20260922-00007", "URM-20260923-00008", "URM-20260924-00009", "URM-20260925-00010"][i]
def _msg(env): return muuid("rejected/" + env["rec"])
def _payload(env):
    r = _RM[env["i"]]
    if r[8] is None:   # truncated body of row 9
        full = json.dumps({"schema": "uns.edge.state/1", "msgId": _msg(env), "ts": iso(DT(9, 25, 14, 2, 29)), "tsSource": "Device", "producer": _PROD[r[0]],
            "seq": 77120, "data": {"stateCode": "Down", "subStateCode": "Fault", "plcStateCode": "7", "faultCode": "F112"}}, ensure_ascii=False)
        return full[:96]
    env_ = {"schema": r[3], "msgId": _msg(env), "ts": iso(r[4]), "tsSource": "Device"}
    if env["i"] != 5:
        env_["producer"] = _PROD[r[0]]; env_["seq"] = 1000 + 37 * env["i"]
    env_["data"] = r[8]
    return json.dumps(env_, ensure_ascii=False)
VAL[(E, "messageUuid")] = _msg
_r(E, "iotHubIdentityId", [x[0] for x in _RM])
_r(E, "unsMessageTypeId", [x[1] for x in _RM])
_r(E, "equipmentId", [x[2] for x in _RM])
_tl(E, "isa95Path", [_PATH[x[0]] for x in _RM])
_tl(E, "payloadSchemaName", [x[3] for x in _RM])
_tl(E, "messageTimestamp", [x[4] for x in _RM])
_tl(E, "receivedAt", [x[5] for x in _RM])
_tl(E, "rejectionReason", [x[6] for x in _RM])
_tl(E, "rejectionDetailText", [x[7] for x in _RM])
VAL[(E, "payloadText")] = _payload
VAL[(E, "deadLetterBlobPath")] = lambda env: "uns-deadletter/%s/%s.json" % (_RM[env["i"]][5].strftime("%Y/%m/%d"), _msg(env))
_r(E, "resolvedById", [x[9] for x in _RM])
_tl(E, "resolvedAt", [x[10] for x in _RM])
_tl(E, "resolutionText", [x[11] for x in _RM])
_r(E, "createdById", [9] * 10)
_r(E, "updatedById", [x[9] if x[9] is not None else 9 for x in _RM])
VAL[(E, "resentMessageUuid")] = lambda env: muuid("resent/" + env["rec"]) if STATUSOF[E][env["i"]] == "Resent" else None

# ---------------------------------------------------------------- keys added to existing collections
def _smu(env):
    """UNS message id for documents that came from the UNS: Auto universe only (RJ1 is outside the UNS scope)."""
    d = env["doc"]; e = env["e"]
    if d.get("app") == "Gamp": return None
    if e == "operationExecution" and d.get("captureMethod") != "PLC Signal": return None
    if e == "inspectionResult" and d.get("source") != "Device": return None
    return muuid("%s/%s" % (env["c"]["collection"], env["rec"]))
for _e in ("equipmentState", "processReading", "alarm", "torqueResult", "leakTestResult", "energyReading", "measurementCurve", "inspectionResult", "operationExecution"):
    VAL[(_e, "sourceMessageUuid")] = _smu
REFIDX[("iotDevice", "edgeGatewayIotDeviceId")] = [None] * 10
# finding F12 of the UNS design: machine states are captured from the PLC, not entered at an MES terminal
VAL[("equipmentState", "source")] = lambda env: "PLC"

AUDIT = set()
def _audit_rm(env):
    """createdAt = receipt of the message (the record is created by the ingestion service); updatedAt = resolution, else receipt.
    The envelope ts is not used: it can be wrong (clock skew is one of the rejection reasons)."""
    d = env["doc"]; i = env["i"]
    d["createdAt"] = ("date", _RM[i][5]); d["updatedAt"] = ("date", _RM[i][10] or _RM[i][5])
POST["unsRejectedMessage"] = _audit_rm

OBS_ADD = """| 18 | u_mes_syst_iotHubIdentity | The six IoT Edge gateway devices are not among the ten sample IoT devices | iotDeviceId is null for the three gateway identities and for the vision station, whose controller is not registered |
| 19 | UNS_01 keys | Only documents that came from the UNS carry sourceMessageUuid: machine states, readings, alarms, tightening and leak test results, energy readings and curves of the caliper universe, and operation executions captured by PLC signal | Documents of the pharma universe and documents entered in the MES have sourceMessageUuid null |
"""

def obs(text):
    marker = "\n## How realistic the documents are"
    if OBS_ADD not in text: text = text.replace(marker, OBS_ADD + marker, 1)
    line = "- Written collection by collection for UNS_01: the 3 new collections and the 10 added keys (05_generator/uns01_samples.py)."
    if line not in text:
        text = text.replace("- Built by the same rules but not read line by line:", line + "\n- Built by the same rules but not read line by line:", 1)
    return text

def apply(ns):
    """merge into the namespace of sample_rules.py (after gmp01_samples.apply)"""
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
    # a rejected message is resolved by sending it again or by discarding it (only this collection uses these statuses)
    ns["STATUSDATE"]["resolved"] = set(ns["STATUSDATE"]["resolved"]) | {"Resent", "Discarded"}
    ns["OBS"] = obs(ns["OBS"])
