"""Gamp universe (pharma): rules for the shared transaction collections (dual Auto / Gamp collections). Merged by pharma_rules.py. D060-D065.
Units: each WIP unit is one serialised saleable unit, a carton of the blister pack or a bottle of the bottle pack.
Units 1-3 are bottles of batch PCM5H26091 (capping and torque results), units 4-7 are cartons of batches PCM5B26092 and PCM5B26093
(blister leak test of the hourly sample), units 0, 8 and 9 are cartons of batch PCM5B26091."""
import datetime
import ext_req01_samples as _X
from pharma_rules import DT, D0, fmt, code, name, BATCH, LOTS, UPO, serial, unit_no, gs1

_poly = _X._poly
VAL = {}; REFIDX = {}; STATUSOF = {}; RECFMT = {}; PARENTIDX = {}; CTXOF = {}; POST = {}; NULLWHEN = {}
def _tl(e, k, lst): VAL[(e, k)] = lst
def _r(e, k, lst): REFIDX[(e, k)] = lst
N10 = [None] * 10

# ---------------------------------------------------------------- production orders (one batch each)
RECFMT["productionOrder"] = lambda i, j: BATCH[i]
CTXOF["productionOrder"] = [7, 6, 5, 1, 7, 5, 1, 7, 5, 7]
_r("productionOrder", "lineId", [5, 4, 2, 1, 5, 2, 1, 5, 2, 5])
_r("productionOrder", "unitOfMeasureId", [0, 0, 0, 1, 0, 0, 1, 0, 0, 0])
_POQ = [(4800, 4800, 4800, 4741, 22, 0), (2400, 2400, 1560, 1532, 8, 0), (480000, 480000, 480000, 476000, 4000, 0), (300, 300, 300, 296, 3, 0), (4800, 4800, 960, 950, 4, 0),
        (480000, 480000, 0, 0, 0, 0), (300, 300, 300, 296, 4, 0), (4800, 2400, 1800, 1716, 36, 0), (480000, 0, 0, 0, 0, 0), (1200, 0, 0, 0, 0, 0)]
for _n, _k in enumerate(["plannedQuantity", "releasedQuantity", "startedQuantity", "goodQuantity", "scrapQuantity", "reworkQuantity"]): VAL[("productionOrder", _k)] = [x[_n] for x in _POQ]

# ---------------------------------------------------------------- lots
RECFMT["lot"] = lambda i, j: LOTS[i]
_r("lot", "productionOrderId", [3, 3, 2, 2, None, None, None, None, None, None])
_r("lot", "unitOfMeasureId", [1, 1, 0, 0, 1, 1, 1, 1, 1, 1])
_tl("lot", "supplierLotNo", [None, None, None, None, "DFC-260904-11", "BEX-260830-07", "SPP-260828-04", "WSD-260901-22", "IFC-260910-03", "BEX-260912-02"])
_tl("lot", "heatNo", N10)
for _k in ("attributesDieNo", "attributesFurnaceChargeNo", "attributesHardnessHbw", "attributesAnodisingLoadNo", "attributesCoatingThicknessUm", "attributesCureDate"): _tl("lot", _k, N10)
_tl("lot", "initialQuantity", ["150.000", "150.000", "240000", "240000", "500.000", "1000.000", "100.000", "200.000", "50.000", "1000.000"])
_tl("lot", "currentQuantity", ["0.000", "0.000", "118400", "240000", "249.850", "1000.000", "90.000", "190.000", "0.000", "972.500"])

# ---------------------------------------------------------------- serialised units
UCTX = [8, 6, 6, 6, 7, 7, 7, 7, 9, 9]
for _e in ("wipUnit", "serialNumber", "asBuiltRecord"): CTXOF[_e] = UCTX
_UITEM = [1 if p == 1 else 0 for p in UPO]
_UPV = [0, 1, 1, 1, 0, 0, 2, 2, 0, 0]
for _e in ("wipUnit", "serialNumber", "asBuiltRecord"):
    _r(_e, "itemId", _UITEM); _r(_e, "productVariantId", _UPV)
_r("wipUnit", "productionOrderId", UPO); _r("serialNumber", "productionOrderId", UPO)
_r("wipUnit", "bodyLotId", N10); _r("asBuiltRecord", "bodyLotId", N10); _r("asBuiltRecord", "castingLotId", N10); _r("asBuiltRecord", "heatTreatmentLotId", N10)
_r("serialNumber", "markedAtEquipmentId", [8, 6, 6, 6, 8, 8, 8, 8, 8, 8])
RECFMT["wipUnit"] = lambda i, j: unit_no(i)
RECFMT["serialNumber"] = lambda i, j: serial(i)
RECFMT["asBuiltRecord"] = lambda i, j: "ABR-" + serial(i)
_tl("wipUnit", "bodyCavityNo", N10); _tl("wipUnit", "castDateCode", N10)
_tl("wipUnit", "itemRevision", ["C", "B", "B", "B", "C", "C", "C", "C", "C", "C"])
_tl("serialNumber", "itemRevision", ["C", "B", "B", "B", "C", "C", "C", "C", "C", "C"])
_tl("asBuiltRecord", "itemRevision", ["C", "B", "B", "B", "C", "C", "C", "C", "C", "C"])
VAL[("serialNumber", "dataMatrixPayload")] = lambda env: gs1(env["i"])
_r("asBuiltRecord", "torqueTorqueResultId", [None, 0, 3, 7, None, None, None, None, None, None])
_tl("asBuiltRecord", "torqueFinalTorqueNm", [None, "1.64", "1.58", "1.12", None, None, None, None, None, None])
_tl("asBuiltRecord", "torqueFinalAngleDeg", [None, "290.0", "284.0", "268.0", None, None, None, None, None, None])
_r("asBuiltRecord", "leakTestLeakTestResultId", [None, None, None, None, 1, 4, 6, 9, None, None])
_tl("asBuiltRecord", "leakTestVerdict", [None, None, None, None, "Pass", "Pass", "Pass", "Fail", None, None])
_tl("asBuiltRecord", "leakTestLeakRate", [None, None, None, None, "0.002", "0.002", "0.002", "0.015", None, None])

# ---------------------------------------------------------------- operation executions (0 = dispensing of sub-lot S1, 1-9 = units 0-8)
CTXOF["operationExecution"] = [0, 8, 6, 6, 6, 7, 7, 7, 7, 9]
_OR = ["OK", "OK", "OK", "OK", "Not OK", "OK", "OK", "OK", "Not OK", "OK"]
_tl("operationExecution", "quantityIn", [6] + [1] * 9)
_tl("operationExecution", "quantityGood", [6] + [1 if r == "OK" else 0 for r in _OR[1:]])
_tl("operationExecution", "quantityReject", [0] + [0 if r == "OK" else 1 for r in _OR[1:]])
_tl("operationExecution", "remarks", ["Six materials dispensed for sub-lot S1, all within +/- 0.5 percent", None, "Cap applied and re-torqued, removal torque 1.52 N.m", None,
    "Cap torque low on two attempts, bottle sent to re-capping", None, "Second leak test after the tester chamber seal was changed, passed", None,
    "Leaking pocket confirmed on three tests, strip rejected", None])
VAL[("operationExecution", "startScanCode")] = lambda env: None if env["i"] == 0 else gs1(env["i"] - 1)

# ---------------------------------------------------------------- bottle capping torque (executions 2-4 = bottles 1-3)
_TQ = [("Cap 38 mm, capping head 2", 1, 1, 1.64, 290.0), ("Cap 38 mm, re-torque station", 2, 1, 1.71, 22.0), ("Cap 38 mm, removal torque check", 3, 1, 1.52, 35.0),
       ("Cap 38 mm, capping head 3", 1, 1, 1.58, 284.0), ("Cap 38 mm, re-torque station", 2, 1, 1.66, 20.0), ("Cap 38 mm, removal torque check", 3, 1, 1.49, 33.0),
       ("Cap 38 mm, capping head 3", 1, 1, 1.08, 262.0), ("Cap 38 mm, capping head 3", 1, 2, 1.12, 268.0), ("Cap 38 mm, re-torque station", 2, 1, 1.63, 21.0),
       ("Cap 38 mm, removal torque check", 3, 1, 1.47, 34.0)]
_ANG = {1: ("290.0", "240.0", "340.0"), 2: ("20.0", "5.0", "40.0"), 3: ("35.0", "10.0", "60.0")}
VAL.update({("torqueResult", "jointName"): [x[0] for x in _TQ], ("torqueResult", "programNo"): ["CAP-38-07"] * 10,
 ("torqueResult", "targetTorqueNm"): ["1.60"] * 10, ("torqueResult", "minTorqueNm"): ["1.20"] * 10, ("torqueResult", "maxTorqueNm"): ["2.00"] * 10,
 ("torqueResult", "tighteningNo"): [x[1] for x in _TQ], ("torqueResult", "attemptNo"): [x[2] for x in _TQ], ("torqueResult", "finalTorqueNm"): ["%.2f" % x[3] for x in _TQ],
 ("torqueResult", "finalAngleDeg"): ["%.1f" % x[4] for x in _TQ], ("torqueResult", "targetAngleDeg"): [_ANG[x[1]][0] for x in _TQ],
 ("torqueResult", "minAngleDeg"): [_ANG[x[1]][1] for x in _TQ], ("torqueResult", "maxAngleDeg"): [_ANG[x[1]][2] for x in _TQ],
 ("torqueResult", "result"): ["Not OK" if x[3] < 1.2 else "OK" for x in _TQ],
 ("torqueResult", "failureReason"): ["Application torque below 1.2 N.m, capping chuck insert worn" if x[3] < 1.2 else None for x in _TQ],
 ("torqueResult", "rundownTimeMs"): [620, 410, 480, 605, 400, 470, 590, 600, 405, 475],
 ("torqueResult", "recipeId"): lambda e: e["identity"](e["byent"]["recipe"], 6)[0], ("torqueResult", "recipeName"): lambda e: e["identity"](e["byent"]["recipe"], 6)[2]})

# ---------------------------------------------------------------- blister vacuum leak test of the hourly sample (executions 5-8 = cartons 4-7)
_T = "Vacuum of -500 mbar not reached, test chamber seal of the tester leaking"
_S = "Pressure rise above limit at -500 mbar, leaking pocket at the knurled seal edge"
VAL.update({("leakTestResult", "failureReason"): [_T, None, _T, _T, None, _T, None, _S, _S, _S], ("leakTestResult", "programNo"): ["BLS-10X10-08"] * 10,
 ("leakTestResult", "ambientTemperatureC"): ["23.4", "23.5", "23.5", "23.8", "23.9", "24.1", "24.2", "22.9", "23.0", "23.1"],
 ("leakTestResult", "partTemperatureC"): ["24.1", "24.2", "24.2", "24.6", "24.6", "25.0", "25.1", "23.5", "23.6", "23.6"],
 ("leakTestResultStage", "stageName"): ["Gross Leak", "Fine Leak"] * 5, ("leakTestResultStage", "testPressureBar"): ["-0.300", "-0.500"] * 5,
 ("leakTestResultStage", "fillTimeSec"): ["2.0", "3.0"] * 5, ("leakTestResultStage", "stabiliseTimeSec"): ["3.0", "5.0"] * 5, ("leakTestResultStage", "testTimeSec"): ["10.0", "30.0"] * 5,
 ("leakTestResultStage", "limitPressureDropPa"): ["300.0", "500.0"] * 5, ("leakTestResultStage", "limitLeakRateSccm"): ["0.005", "0.010"] * 5,
 ("leakTestResultStage", "pressureDropPa"): ["110.0", "780.0", "95.0", "240.0", "120.0", "810.0", "90.0", "760.0", "105.0", "220.0"],
 ("leakTestResultStage", "leakRateSccm"): ["0.002", "0.016", "0.002", "0.005", "0.002", "0.017", "0.002", "0.015", "0.002", "0.004"]})

# ---------------------------------------------------------------- containers, movements, receipts, shipments
RECFMT["container"] = lambda i, j: ["IBC-%05d", "IBC-%05d", "SSD-%05d", "SHP-%06d", "SHP-%06d", "SHP-%06d", "SHP-%06d", "SHP-%06d", "SHP-%06d", "SHP-%06d"][i] % (31 + 17 * i)
_r("container", "containerTypeId", [0, 0, 2, 6, 6, 6, 6, 6, 6, 6])
_r("container", "itemId", [3, 3, 2, 0, 0, 0, 0, 0, 0, 0])
_tl("container", "quantity", [150, 146, 60000, 38, 50, 50, 50, 50, 50, 50])
_tl("container", "capacity", [300, 300, 60000, 50, 50, 50, 50, 50, 50, 50])
_tl("container", "tareWeightKg", ["82.500", "82.500", "6.200", "0.650", "0.650", "0.650", "0.650", "0.650", "0.650", "0.650"])
_tl("container", "grossWeightKg", ["232.500", "228.500", "42.900", "3.390", "4.250", "4.250", "4.250", "4.250", "4.250", "4.250"])
_tl("materialMovement", "quantity", ["500.000", "1000.000", "250.150", "10.000", "240000", "1", "50", "480", "0.500", "1000.000"])
_r("materialMovement", "unitOfMeasureId", [1, 1, 1, 1, 0, 0, 0, 0, 1, 1])
_r("materialMovement", "itemId", [4, 5, 4, 7, 2, 0, 0, 0, 6, 5])
_r("materialMovement", "lotId", [4, 5, 4, 7, 3, None, None, None, 6, 5])
_GQ = ["500.000", "1000.000", "100.000", "200.000", "50.000", "1000.000", "500.000", "25.000", "200.000", "50.000"]
_GS = ["Accepted", "Accepted", "Accepted", "Accepted", "Accepted", "Accepted", "Pending", "Accepted Under Deviation", "Rejected", "Accepted"]
VAL.update({("goodsReceiptLine", "supplierLotNo"): ["DFC-260904-11", "BEX-260830-07", "SPP-260828-04", "WSD-260901-22", "IFC-260910-03", "BEX-260912-02", "DFC-260918-03",
    "KLS-260910-15", "WSD-260915-08", "IFC-260920-07"],
 ("goodsReceiptLine", "orderedQuantity"): _GQ, ("goodsReceiptLine", "receivedQuantity"): _GQ,
 ("goodsReceiptLine", "acceptedQuantity"): [q if s.startswith("Accepted") else "0.000" for q, s in zip(_GQ, _GS)],
 ("goodsReceiptLine", "rejectedQuantity"): [q if s == "Rejected" else "0.000" for q, s in zip(_GQ, _GS)]})
_r("goodsReceiptLine", "unitOfMeasureId", [1] * 10)
VAL[("shipment", "totalContainers")] = lambda e: max(1, int(e["doc"]["totalQuantity"][1] // 50)) if isinstance(e["doc"].get("totalQuantity"), tuple) else 10
VAL[("shipment", "grossWeightKg")] = lambda e: "%.3f" % (max(1, int(e["doc"]["totalQuantity"][1] // 50)) * 4.25) if isinstance(e["doc"].get("totalQuantity"), tuple) else "42.500"
_tl("shipment", "invoiceValueInr", ["18480.00", "9240.00", "18480.00", "36960.00", "4620.00", "18480.00", "9240.00", "27720.00", "18480.00", "13860.00"])

# ---------------------------------------------------------------- execution support
_tl("operatorSession", "clientWorkstation", ["RJ1-COT01-HMI-01", "RJ1-BTL01-HMI-01", "RJ1-BTL01-HMI-01", "RJ1-BTL01-HMI-01", "RJ1-BLS01-HMI-01", "RJ1-BLS01-HMI-01",
    "RJ1-BLS01-HMI-01", "RJ1-BLS01-HMI-01", "RJ1-BLS01-HMI-01", "RJ1-CTN01-HMI-01"])
_IRMSG = ["Unit, lot or batch is on quality hold; operation not allowed", "Previous routing step not completed or bulk lot not released; operation not allowed",
    "No valid certification for the skill required at this station; login refused", "Serial already issued; coding stopped",
    "Lot is on hold, rejected or past its retest date; dispensing not allowed", "Blister sample failed the leak test; serialisation not allowed until the hourly sample passes",
    "Change part has reached its life limit; change the chuck insert and verify", "Balance calibration or daily performance check not valid; weighing not allowed",
    "Foil, carton or leaflet scanned does not match the pack variant of the batch", "Room relative humidity above 55 percent; compression not allowed"]
_tl("interlockRule", "messageText", _IRMSG)
_r("interlockRule", "lineId", [None, 5, None, 5, 0, 5, 4, 0, 5, 2])
_r("interlockRule", "workCenterId", [None, None, None, 8, 0, 8, 6, 0, 7, 4])
_r("interlockRule", "operationId", [None, None, None, 8, 0, 8, 6, 0, 7, 4])
_IR = [8, 1, 2, 6, 4, 5, 3, 0, 9, 7]
VAL[("interlockEvent", "messageText")] = lambda env: _IRMSG[_IR[env["i"]]]
_r("interlockEvent", "workCenterId", [7, 7, 7, 6, 0, 8, 8, 8, 4, 4])
_r("interlockEvent", "equipmentId", [7, 7, 7, 6, 0, 8, 8, 8, 4, 4])
_r("interlockEvent", "productionOrderId", [7, 4, 7, None, None, 7, 0, 0, 5, None])
_r("interlockEvent", "wipUnitId", [None, 4, None, None, None, 7, 8, 0, None, None])
_r("interlockEvent", "lotId", [None, None, None, None, 5, None, None, None, None, None])
POST["interlockEvent"] = _poly([(None, 0), ("wipUnit", 4), ("operatorSession", 8), ("tool", 6), ("lot", 5), ("wipUnit", 7), ("serialNumber", 8), ("wipUnit", 0), ("workCenter", 4), ("gauge", 4)])
_tl("interlockEvent", "foundValueText", ["Foil roll for the domestic pack scanned on a Kenya batch", "Bulk lot PCM5F26091-P2 status In Process", "BLS-OP certification expired on 10 Sep 2026",
    "Chuck insert CHK-38-0002 at 2,000,000 cycles", "Lot R260830-MCC-007 status On Hold", "Leak test verdict Fail on 22 Sep 2026 16:04", serial(8) + " already issued",
    "Unit %s on hold HLD-2026-000021" % unit_no(0), "58 percent RH", "Balance G-BAL-220 daily performance check overdue since 12 Sep 2026"])
_tl("interlockEvent", "expectedValueText", ["Kenya pack foil", "Bulk lot released to packing", "Valid BLS-OP certification, level 3", "Below 2,000,000 cycles", "Available, released lot",
    "Pass", "Unused serial", "No active hold", "30-55 percent RH", "Valid daily performance check"])
_tl("interlockEvent", "overrideComment", [None, None, None, "Last 300 bottles before the planned chuck change at shift end; removal torque checked every 15 minutes", None, None,
    None, None, "Dehumidifier restarted; humidity back to 48 percent within 10 minutes; QA informed", None])
_tl("setupVerificationItem", "scannedCode", ["CHP-BLS-10X10", "RM-PCM-API R260904-API-011", "PCM500-B10-DOM", "BLS-10X10-08", "CHK-38-0002", "PCM500-H100-DOM", "FRM-BLS-10X10",
    "G-VLT-001", None, "SER-CTN-09"])
_tl("setupVerificationItem", "expectedValue", [None] * 8 + ["-500.0", None])
_tl("setupVerificationItem", "actualValue", [None] * 8 + ["-498.0", None])
_r("setupVerificationItem", "unitOfMeasureId", [None] * 8 + [6, None])
_tl("changeover", "lossReason", ["Change parts for the bottle of 100 not at the point of use", "Line clearance waited for QA verification", "Rinse sample result of the granulator awaited",
    "Punch inspection before the tooling change took longer than planned", "Foil roll for the Kenya pack not staged", "Cleaning of the coating pan spray guns",
    "Leaflet stock of the new version not issued", "Carton magazine adjustment for the new carton size", "Batch documents not issued to the line", "Checkweigher limits not downloaded"])

# ---------------------------------------------------------------- quality
_tl("nonconformance", "productImpactText", ["API weighed 0.6 percent above target for one sub-lot; dispensed quantity rejected and re-dispensed",
    "One granulation batch affected; processed under deviation DEV-2026-0007", "One granulation batch affected; granules re-dried and retested",
    "Validation batch affected; blend re-mixed for 2 minutes and resampled", None, "4,000 coated tablets from pan load 1 rejected; pan load 2 not affected",
    "Bottles from head 3 since the last good check re-capped and retested", "Batch on hold; hourly samples since the foil roll change retested", "120 cartons decommissioned and re-coded", None])
_tl("engineeringChange", "description", ["Change request: tablet hardness limit revised to 80-140 N. Affected process step: compression",
    "Change request: second source of microcrystalline cellulose PH 101 approved. Affected process steps: dispensing and granulation",
    "Change request: coating weight gain target changed to 3.0 percent. Affected process step: film coating",
    "Change request: blister foil supplier changed. Affected process step: blister packing and leak test",
    "Change request: carton artwork revised for the new marketing authorisation number. Affected process steps: serialisation and cartoning",
    "Change request: granulation end-point changed from time to impeller power. Affected process step: wet granulation",
    "Change request: bottle cap torque window revised to 1.2-2.0 N.m. Affected process step: bottle filling and capping",
    "Change request: Kenya export pack added. Affected process steps: blister packing and cartoning",
    "Change request: shipper quantity changed from 40 to 50 cartons. Affected process step: cartoning",
    "Change request: dispensing booth balance replaced with a 150 kg model. Affected process step: dispensing"])
VAL[("deviationPermit", "specifiedValue")] = lambda env: env["p"]["usl"]
VAL[("deviationPermit", "requestedValue")] = lambda env: fmt(float(env["p"]["usl"]) + (float(env["p"]["usl"]) - float(env["p"]["lsl"])) * 0.1, env["p"]["dp"])
PARENTIDX["characteristicPosition"] = [4, 4, 4, 4, 4, 2, 2, 2, 2, 2]
_tl("characteristicPosition", "positionName", ["Press station 1", "Press station 12", "Press station 17", "Press station 30", "Press station 45", "Dryer bowl, top layer",
    "Dryer bowl, centre", "Dryer bowl, bottom near the distributor plate", "Dryer bowl, wall side", "Discharge sample at the bin"])
_tl("characteristicPosition", "nominal", ["600.0"] * 5 + ["1.75"] * 5)
_tl("characteristicPosition", "lowerSpecLimit", ["570.0"] * 5 + ["1.00"] * 5)
_tl("characteristicPosition", "upperSpecLimit", ["630.0"] * 5 + ["2.50"] * 5)
_r("characteristicPosition", "unitOfMeasureId", [2] * 5 + [3] * 5)
_tl("inspectionResult", "positionNo", [None, None, 2, None, 3, None, None, None, None, None])
_tl("inspectionResult", "positionName", [None, None, "Dryer bowl, centre", None, "Press station 17", None, None, None, None, None])
_tl("defectRecord", "defectLocationText", ["Cap thread, head 3", "Blister pocket 7, knurled seal edge", "Blister pocket 3", "Tablet surface, upper face", "Granule sample, bowl bottom",
    "Coated tablet edge", "Tablet band", "Blister strip, pocket row 2", "Carton 2D code field", "Carton flap"])
_tl("reworkOrder", "instruction", ["Remove the strips from the rejected cartons, re-check the blisters on the leak tester and repack into new printed cartons",
    "Remove the strips from the rejected cartons, re-check the blisters on the leak tester and repack into new printed cartons",
    "Re-cap the bottle on the capper and check the removal torque", "Remove the strips from the rejected cartons, re-check the blisters on the leak tester and repack into new printed cartons",
    "Re-mill and re-blend the granules under the approved reprocessing protocol", "Remove the strips from the rejected cartons, re-check the blisters on the leak tester and repack into new printed cartons",
    "Re-cap the bottle on the capper and check the removal torque", "Decommission the old serial and re-code the carton on the serialisation unit",
    "Remove the strips from the rejected cartons, re-check the blisters on the leak tester and repack into new printed cartons", "Re-cap the bottle on the capper and check the removal torque"])
_tl("labelTemplate", "standard", ["GS1 General Specifications", "GS1 General Specifications", "Drugs Rules 1945, Rule 96", "Schedule M 2023, dispensing label",
    "Schedule M 2023, status labelling", "GS1 General Specifications", "Schedule M 2023, status labelling", "Schedule M 2023, status labelling", "Schedule M 2023, status labelling",
    "Schedule M 2023, status labelling"])

# ---------------------------------------------------------------- curves
_tl("curveEnvelope", "xUnitText", ["mm", "mm", "deg", "deg", "deg", "ms", "ms", "mm", "mm", "deg"])
_tl("curveEnvelope", "yUnitText", ["kN", "kN", "N.m", "N.m", "N.m", "mbar", "mbar", "kN", "kN", "N.m"])
_tl("curveEnvelope", "goldenSampleSerialNo", ["RS-CMP-PCM500-02", "RS-CMP-PCM500-02", "0890000398012", "0890000398031", "0890000398012", "RS-BLS-LEAK-07", "RS-BLS-LEAK-07",
    "RS-CMP-PCM500-01", "RS-CMP-PCM500-03", "0890000397011"])
_r("curveEnvelope", "characteristicId", [4, 4, 6, 6, 6, 7, 7, 4, 4, 6])
_r("curveEnvelope", "operationId", [4, 4, 6, 6, 6, 7, 7, 4, 4, 6])
_r("curveEnvelope", "itemId", [2, 2, 1, 1, 1, 0, 0, 2, 2, 1])
_r("curveEnvelope", "productVariantId", [None, None, 1, 1, None, 0, 0, None, None, 1])
_r("curveEnvelope", "recipeId", [4, 4, 6, 6, 6, 7, 7, 4, None, 6])
VAL.update({("curveEnvelopeWindow", "xMin"): ["0.0", "2.5", "3.2", "0", "180", "300", "0", "29000", "1.0", "20"],
 ("curveEnvelopeWindow", "xMax"): ["2.5", "3.2", "3.4", "180", "400", "400", "30000", "30000", "1.4", "90"],
 ("curveEnvelopeWindow", "yMin"): ["0.0", "5.0", "15.0", "0.00", "0.60", "1.20", None, "0.0", "1.0", "1.00"],
 ("curveEnvelopeWindow", "yMax"): ["5.0", "22.0", "21.0", "0.60", "2.20", "2.00", "5.0", "5.0", "4.0", "2.20"]})
_r("measurementCurve", "curveEnvelopeId", [4, 2, 2, 2, 2, 4, 5, 5, 5, 5])
_r("measurementCurve", "characteristicId", [6, 6, 6, 6, 6, 6, 7, 7, 7, 7])
_r("measurementCurve", "wipUnitId", [2, 1, 2, 3, 3, 1, 4, 4, 7, 7])
_r("measurementCurve", "serialNumberId", [2, 1, 2, 3, 3, 1, 4, 4, 7, 7])
_r("measurementCurve", "operationExecutionId", [3, 2, 3, 4, 4, 2, 5, 5, 8, 8])
_r("measurementCurve", "equipmentId", [6, 6, 6, 6, 6, 6, 7, 7, 7, 7])
_r("measurementCurve", "inspectionResultId", [6, None, None, None, None, None, 7, None, None, None])
VAL.update({("measurementCurve", "pointCount"): [360, 360, 360, 360, 360, 360, 300, 300, 300, 300],
 ("measurementCurve", "peakX"): ["33", "290", "284", "262", "268", "35", "30000", "30000", "30000", "30000"],
 ("measurementCurve", "peakY"): ["1.49", "1.64", "1.58", "1.08", "1.12", "1.52", "2.0", "2.4", "7.8", "8.1"],
 ("measurementCurve", "finalX"): ["33", "290", "284", "262", "268", "35", "30000", "30000", "30000", "30000"],
 ("measurementCurve", "finalY"): ["1.49", "1.64", "1.58", "1.08", "1.12", "1.52", "2.0", "2.4", "7.8", "8.1"],
 ("measurementCurve", "result"): ["OK", "OK", "OK", "NOK", "NOK", "OK", "OK", "OK", "NOK", "NOK"],
 ("measurementCurve", "failedWindowNo"): [None, None, None, 3, 3, None, None, None, 2, 2]})

# ---------------------------------------------------------------- documents
_DOCS = ["MMR-PCM500-B10-03", "SOP-PRD-014-06", "SPEC-FP-PCM500-04", "SOP-PKG-003-08", "VR-PV-2026-07", "COA-DFC-260904-11", "EBR-PCM5B26091", "CAL-G-BAL-150-260915",
         "ART-CTN-PCM500-B10-05", "SOP-WH-007-09"]
RECFMT["controlledDocument"] = lambda i, j: _DOCS[i]
VAL[("controlledDocument", "fileName")] = lambda env: _DOCS[env["i"]] + ".pdf"
VAL[("controlledDocument", "storageKey")] = lambda env: "rj1/documents/%s.pdf" % _DOCS[env["i"]]
