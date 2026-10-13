"""Sample rules of the Gamp universe (pharma, app = "Gamp"): overrides applied by pharma_profile.activate("Gamp"). D060-D065.
Story: Paracetamol Tablets IP 500 mg, film-coated, Indrayani Pharmaceuticals Ltd., Ranjangaon OSD Plant (RJ1), production fortnight 15-24 September 2026.
Index conventions of the Gamp universe (same positions as the caliper universe, so the generic rules keep their meaning):
  process rows 0-9   = OP010 dispensing, OP020 granulation, OP030 drying, OP040 blending, OP050 compression, OP060 coating,
                       OP070 bottle filling and capping, OP080 blister packing and leak test, OP090 serialisation, OP100 cartoning and final inspection
  items 0-9          = FG blister 10 x 10, FG bottle of 100, bulk film-coated tablets, granules, Paracetamol API, MCC PH 101, povidone K30, SSG, magnesium stearate, coating system
  production orders  = batches PCM5B26091 (blister), PCM5H26091 (bottle), PCM5F26091 (bulk tablets), PCM5G26091 (granules), PCM5B26092, PCM5F26092, PCM5G26092,
                       PCM5B26093 (on hold), PCM5F26093 (created), PCM5B26094 (cancelled)
  lots 0-9           = granulation sub-lots PCM5G26091-S1 and -S2, coating pan loads PCM5F26091-P1 and -P2, supplier lots API, MCC (on hold), PVP, SSG, coating system, MCC
  users 0-9          = Amol Shinde, Pooja Kadam, Rahul Waghmare (operators), Shalini Rao (QA officer), Nilesh Sawant (production executive), Farhan Qureshi (engineering),
                       Vandana Iyer (head QA), Prakash Jagtap (warehouse), Tejas Bapat (CSV engineer), MES system
The rule dictionaries are split over three files: this one (masters and key-level rules), pharma_rules_trans.py (shared transactions)
and pharma_rules_gmp.py (the 26 GMP-only collections)."""
import datetime
import sample_universe as U

def DT(m, d, h=0, mi=0, s=0, y=2026): return datetime.datetime(y, m, d, h, mi, s)
def D0(y, m, d): return datetime.datetime(y, m, d)
def rows(t): return t.strip().split("\n")
def code(s): return s.split("|")[0]
def name(s): return s.split("|")[1]
def fmt(x, dp): return "%.*f" % (dp, x)

PERSONS = ["Sudhir Kulkarni", "Anjali Menon", "Harish Bhat", "Leena Desai", "Ketan Shah", "Rekha Pillai", "Omkar Joshi", "Neha Sathe", "Pradeep Rane", "Smita Gokhale"]
BATCH = ["PCM5B26091", "PCM5H26091", "PCM5F26091", "PCM5G26091", "PCM5B26092", "PCM5F26092", "PCM5G26092", "PCM5B26093", "PCM5F26093", "PCM5B26094"]
LOTS = ["PCM5G26091-S1", "PCM5G26091-S2", "PCM5F26091-P1", "PCM5F26091-P2", "R260904-API-011", "R260830-MCC-007", "R260828-PVP-004", "R260901-SSG-022",
        "R260910-COT-003", "R260912-MCC-002"]
# WIP units: one serialised saleable unit each (carton of the blister pack, bottle of the bottle pack); unit k belongs to order UPO[k]
UPO = [0, 1, 1, 1, 4, 4, 7, 7, 0, 0]
UDAY = [15, 15, 15, 15, 18, 18, 22, 22, 16, 16]
def serial(i): return "08900004%05d" % (184 + 13 * i)
def unit_no(i): return "%s-%s-%05d" % ("BTL" if UPO[i] == 1 else "CTN", BATCH[UPO[i]], 184 + 13 * i)
GTIN = {0: "08904101500017", 1: "08904101500024"}
def gs1(i): return "(01)%s(21)%s(17)280831(10)%s" % (GTIN[0 if UPO[i] != 1 else 1], serial(i), BATCH[UPO[i]])

MASTER_ADD = {
"computerisedSystem": rows("""CSY-MES-RJ1|Manufacturing execution system, Ranjangaon OSD plant
CSY-LKT-BLS-01|Blister vacuum leak tester controller, blister line 1
CSY-CAP-BTL-01|Capper torque controller, bottle line 1
CSY-SER-L3|Serialisation line system, blister line 1
CSY-CMP-01-T1|Tablet press control system, compression cubicle 1
CSY-ERP-IF-PH|ERP interface for process orders and goods movements
CSY-LBL-RJ1|Label printing server, Ranjangaon plant
CSY-HIST-RJ1|Process data historian, Ranjangaon plant
CSY-LIMS-QC1|Laboratory information management system, quality control
CSY-RMG-01-PLC|Rapid mixer granulator PLC (legacy)"""),
"environmentalMonitoringPoint": rows("""EMP-DSP-01|Dispensing booth, airborne particles 0.5 um
EMP-DSP-02|Dispensing booth, temperature
EMP-DSP-03|Dispensing booth, relative humidity
EMP-CMP-01|Compression cubicle to corridor, differential pressure
EMP-GRN-01|Granulation suite, surface microbial count by contact plate
EMP-PPK-01|Primary packing area, relative humidity
EMP-PPK-02|Primary packing area, temperature
EMP-QCL-01|Stability chamber 30 degC / 65 percent RH, temperature
EMP-QCL-02|Stability chamber 30 degC / 65 percent RH, relative humidity
EMP-DSP-04|Dispensing booth, airborne particles 5.0 um"""),
"masterManufacturingRecord": rows("""MMR-PCM500-B10-03|Paracetamol Tablets IP 500 mg blister 10 x 10, master manufacturing record version 3
MMR-PCM500-B10-02|Paracetamol Tablets IP 500 mg blister 10 x 10, master manufacturing record version 2
MMR-PCM500-H100-02|Paracetamol Tablets IP 500 mg bottle of 100, master manufacturing record version 2
MMR-PCM500-FCT-04|Paracetamol 500 mg film-coated tablets bulk, master manufacturing record version 4
MMR-PCM500-GRN-03|Paracetamol 500 mg granules, master manufacturing record version 3
MMR-PCM500-B10-04|Paracetamol Tablets IP 500 mg blister 10 x 10, master manufacturing record version 4
MMR-PCM500-GRN-04|Paracetamol 500 mg granules, master manufacturing record version 4
MMR-PCM500-H100-03|Paracetamol Tablets IP 500 mg bottle of 100, master manufacturing record version 3
MMR-PCM500-FCT-03|Paracetamol 500 mg film-coated tablets bulk, master manufacturing record version 3
MMR-PCM500-B10-01|Paracetamol Tablets IP 500 mg blister 10 x 10, master manufacturing record version 1"""),
"interlockRule": rows("""ILR-HOLD-001|Hold check at operation start
ILR-SEQ-001|Routing sequence check, blister packing line 1
ILR-SKL-001|Skill check at station login
ILR-DUP-001|Duplicate serial check at carton serialisation
ILR-LOT-001|Lot release and retest date check at dispensing
ILR-NOK-001|Failed blister leak test blocks serialisation
ILR-TQL-001|Change part life check, capping chuck
ILR-CAL-001|Balance calibration and daily performance check
ILR-VAR-001|Pack variant check at blister line start
ILR-ENV-001|Room humidity check, compression cubicle"""),
"curveEnvelope": rows("""ENV-OP050-CMP-FD-02|Main compression force-displacement, Paracetamol 500 mg cores
ENV-OP050-PRE-FD-01|Pre-compression force-displacement, Paracetamol 500 mg cores
ENV-OP070-CAP-TA-04|Cap application torque-angle, 38 mm cap, bottle of 100
ENV-OP070-CAP-TA-04B|Cap application torque-angle, 38 mm cap, bottle of 100, chuck set B
ENV-OP070-CAP-RT-01|Cap removal torque-angle, 38 mm cap
ENV-OP080-VAC-500-02|Vacuum decay at -500 mbar, blister 10 x 10
ENV-OP080-VAC-300-02|Vacuum decay at -300 mbar, blister 10 x 10
ENV-OP050-CMP-FD-01|Main compression force-displacement, Paracetamol 500 mg cores
ENV-OP050-CMP-FD-02B|Main compression force-displacement, Paracetamol 500 mg cores, tooling set B
ENV-OP070-CAP-TA-03|Cap application torque-angle, 38 mm cap, bottle of 100"""),
}
TITLES_ADD = {}

TD_EXAMPLE = {
 "addressLine1": "Plot D-3, MIDC Ranjangaon Industrial Area", "addressLine2": "Karegaon, Taluka Shirur", "addressCity": "Pune", "addressPostalCode": "412220", "addressState": "Maharashtra",
 "registeredAddressLine1": "Indrayani House, 21 Senapati Bapat Road", "registeredAddressLine2": "Shivajinagar", "registeredAddressCity": "Pune", "registeredAddressPostalCode": "411016",
 "registeredAddressState": "Maharashtra", "billingAddressLine1": "Medicura House, Plot 44, Bhosari MIDC", "billingAddressCity": "Pune", "billingAddressPostalCode": "411026",
 "billingAddressState": "Maharashtra", "website": "https://www.indrayanipharma.example", "email": "dispatch@pharmacoldcargo.example", "gstin": "27AABCI7321M1Z4",
 "cin": "U24230PN1998PLC112345", "pan": "AABCI7321M", "industryCode": "21002", "factoryLicenceNo": "MH/PUN/2(m)(i)/21002/2008/1144", "portalUrl": "https://partners.medicura.example",
 "endpoint": "https://erp-prd.indrayanipharma.example/api/mes", "credentialRef": "vault://mes/rj1/erp-prd", "workstation": "RJ1-QA-WS-07", "assetNo": "FA-RJ1-007311",
 "barcode": "LOC-PKG-STG-01", "attributeAcceptance": "No black specks, chipping, capping or broken tablets", "caution": "Do not open more than one material container in the booth at a time",
 "certificateNo": "PCVS/CAL/2026/04128", "controlMethod": "In-process check record in the electronic batch record", "controllerResultNo": "SC-000418871",
 "customerApprovalRef": "QA/DEV/2026/044", "customerChangeRef": "MCH-CCR-2026-118", "customerDefectCode": "MCH-Q-0417", "customerLocation": "Medicura Healthcare, Nagpur distribution depot",
 "customerRefNo": "MCH-QC-2026-0932", "cutInSerialNo": "0890000400001",
 "d4RootCauseEscape": "Spray rate excursion not alarmed on the coater HMI; weight gain checked only at the end of the batch",
 "d7PreventionHorizontalDeployment": "Apply to coating suite 2 and compression suite 2",
 "d7PreventionLessonsLearned": "Recipe limits to be enforced as alarms on all coating and granulation equipment",
 "dunnage": "Corrugated partition, 2 layers of 25 cartons", "drawingNo": "TD-PNC-19X9-02", "drawingZone": "SPEC-FP-PCM500 clause 4.3", "enteredText": "Cap seated, no tilt",
 "equipmentText": "Rotary tablet press CMP-01-T1", "erpCostCenterCode": "RJ017040", "erpWorkCenterCode": "RJ01-BLS01", "exampleValue": "PCM5B26091", "formatMask": "PCM5{FORM}{YY}{M}{N}",
 "prefix": "PCM5", "hsnCode": "30049099", "humanReadable": "PARACETAMOL 500MG  QTY 50 CTN  B.NO PCM5B26091", "payload": "(01)18904101500014(37)50(10)PCM5B26091(17)280831",
 "payloadPattern": "(01){gtin}(37){quantity}(10){batchNo}(17){expiry}", "labelSuffix": "B", "instruction": "Remove the strips from the rejected cartons, re-check the blisters on the leak tester and repack into new printed cartons",
 "invoiceNo": "IPL/26-27/004128", "markingRequirement": "Yellow deviation label on each shipper", "masterStandardRef": "Reference weight set E2, 1 mg to 200 g, certificate NABL-CC-4471",
 "mountedPosition": "Turret", "opcNodeAddress": "ns=3;s=\"PLC_RMG01\"", "optionsColour": "White", "parentCustomerCode": "MCH", "pathText": "Unplanned > Equipment > Balance > Zero drift",
 "reactionOnFail": "Stop the operation and inform the production supervisor and QA", "reactionPlan": "Stop, quarantine material since the last good check, inform QA, raise a deviation",
 "referenceDesignator": "F1", "releaseComment": "Leak retest of all hourly samples completed, 2 strips rejected", "safetyNotes": "Wear the powered air-purifying respirator when handling open API",
 "sampleFrequency": "Every 30 minutes", "scannedCode": "RM-PCM-API/R260904-API-011", "serialNo": "SC120-2231907", "sourceAddress": "ns=3;s=\"DB_Process\".\"ProductTemp\"",
 "specification": "600.0 +/- 30.0 mg", "standard": "ISO 2859-1:1999", "storageKey": "rj1/documents/MMR-PCM500-B10-03.pdf", "fileName": "MMR-PCM500-B10-03.pdf",
 "subgroupFrequency": "Every 30 minutes", "supplierCodeAtCustomer": "IPL0487", "supplierInvoiceNo": "DFC/26-27/1842", "unitText": "mg", "newValue": "140", "oldValue": "130",
 "reasonCodeText": "Annual product quality review finding", "erpBomNo": "00061050-01", "erpRoutingNo": "50006105-01", "legalName": "Indrayani Pharmaceuticals Limited", "application": "MES Operator Client 1.4.2",
}
ND_EXAMPLE = {"geoLatitude": "18.7556", "geoLongitude": "74.2414", "quantityPerContainer": "50", "layersPerContainer": "2", "unitsPerLayer": "25", "containersPerPallet": "40",
 "maxGrossWeightKg": "12.0", "tareWeightKg": "0.650", "grossWeightKg": "4.250", "weightKg": "0.245", "ppmTarget": "10"}

VAL = {}; REFIDX = {}; STATUSOF = {}; RECFMT = {}; PARENTIDX = {}; CTXOF = {}; POST = {}; NULLWHEN = {}; SPECIALIDENT = {}
GEN = {}; BOOLRULE = {}; ENUMRULE = {}; PKEY = {}
def _tl(e, k, lst): VAL[(e, k)] = lst
def _r(e, k, lst): REFIDX[(e, k)] = lst
N10 = [None] * 10

# ---------------------------------------------------------------- key-level rules (apply to every Gamp document that has the key)
def _ev(lst): return lambda env, en: lst[env["i"]] if lst[env["i"]] in en else en[0]
ENUMRULE.update({
 "lineType": _ev(["Dispensing", "Granulation", "Compression", "Coating", "Primary Packing", "Primary Packing", "Secondary Packing", "Granulation", "Compression", "Primary Packing"]),
 "lotType": _ev(["Granulation Lot", "Granulation Lot", "Coated Tablet Lot", "Coated Tablet Lot"] + ["Supplier Lot"] * 6),
 "customerType": _ev(["Distributor", "Distributor", "Distributor", "Hospital", "Export", "Distributor", "Distributor", "Institutional", "Distributor", "Export"]),
 "supplierType": _ev(["Direct Material"] * 6 + ["Calibration Laboratory", "Direct Material", "Direct Material", "Service"]),
 "itemType": _ev(["Finished Good", "Finished Good", "Semi Finished", "Semi Finished"] + ["Raw Material"] * 6),
 "siteType": _ev(["Manufacturing Plant"] * 6 + ["Technical Center", "Warehouse", "Technical Center", "Head Office"]),
 "orderType": _ev(["Production"] * 8 + ["Validation Batch", "Production"]),
 "changeType": _ev(["Process Change", "Supplier Change", "Process Change", "Supplier Change", "Document Change", "Process Change", "Process Change", "Design Change", "Document Change", "Tooling Change"]),
 "originator": _ev(["Internal", "Internal", "Internal", "Supplier", "Internal", "Internal", "Internal", "Customer", "Customer", "Internal"]),
 "reworkType": _ev(["Repack", "Repack", "Retighten", "Repack", "Reprocess", "Repack", "Retighten", "Re-mark", "Repack", "Retighten"]),
 "connectorType": _ev(["ERP", "LIMS", "OPC UA Server", "OPC UA Server", "Weighing System", "Leak Tester", "Serialisation Server", "Track And Trace Portal", "Email Gateway", "Document Management"]),
 "protocol": _ev(["HTTPS REST", "HTTPS REST", "OPC UA", "OPC UA", "Serial Over TCP", "Modbus TCP", "HTTPS REST", "HTTPS REST", "SMTP", "HTTPS REST"]),
 "workCenterType": _ev(["Manual Station", "Batch Process", "Batch Process", "Batch Process", "Machine Station", "Batch Process", "Machine Station", "Test Station", "Machine Station", "Inspection Station"]),
 "stageName": _ev(["Gross Leak", "Fine Leak"] * 5),
 "changeoverType": _ev(["Batch Change", "Product Change", "Batch Change", "Batch Change", "Product Change", "Batch Change", "Batch Change", "Product Change", "Batch Change", "Batch Change"]),
 "disposalMethod": lambda env, en: "Incineration" if "Incineration" in en else en[0],
 "scrapCostCategory": lambda env, en: "Packing Scrap" if env["p"]["optype"] in ("Packing", "Inspection") else "Manufacturing Scrap",
 "optionsHand": lambda env, en: None,
 "lifeUom": lambda env, en: env["p"]["lifeuom"] if env["p"]["lifeuom"] in en else en[0],
 "auditType": _ev(["Self Inspection", "Process Audit", "Process Audit", "Self Inspection", "Process Audit", "Self Inspection", "Product Audit", "Self Inspection", "Customer Audit", "System Audit"]),
})
def _dp(s): return len(s.split(".")[1]) if "." in s else 0
GEN.update({
 "highHighLimit": lambda e: fmt(float(e["p"]["hi"]) + (float(e["p"]["hi"]) - float(e["p"]["lo"])) * 0.5, _dp(e["p"]["hi"])),
 "lowLowLimit": lambda e: fmt(float(e["p"]["lo"]) - (float(e["p"]["hi"]) - float(e["p"]["lo"])) * 0.5, _dp(e["p"]["lo"])),
 "engineeringMax": lambda e: fmt(float(e["p"]["hi"]) * 1.5, _dp(e["p"]["hi"])),
 "tagValue": lambda e: round(float(e["p"]["sp"]) + [0.4, -1.2, 0.9, 2.6, -0.7, 0.1, 1.5, -2.0, 0.6, -0.3][e["i"]] * (float(e["p"]["hi"]) - float(e["p"]["lo"])) / 10.0, 4),
 "taktTimeSec": lambda e: "0.8",
})

# ---------------------------------------------------------------- organisation and people
_tl("site", "addressCity", ["Pune", "Pune", "Pune", "Baddi", "Rangpo", "Verna", "Hyderabad", "Pune", "Pune", "Pune"])
_tl("site", "addressDistrict", ["Pune", "Pune", "Pune", "Solan", "Pakyong", "South Goa", "Medchal-Malkajgiri", "Pune", "Pune", "Pune"])
_tl("site", "addressState", ["Maharashtra", "Maharashtra", "Maharashtra", "Himachal Pradesh", "Sikkim", "Goa", "Telangana", "Maharashtra", "Maharashtra", "Maharashtra"])
_tl("site", "addressPostalCode", ["412220", "412220", "413802", "173205", "737132", "403722", "500078", "410507", "411057", "411016"])
_tl("site", "addressLine1", ["Plot D-3, MIDC Ranjangaon Industrial Area", "Plot D-5, MIDC Ranjangaon Industrial Area", "Plot B-22, MIDC Kurkumbh", "Village Katha, Baddi-Barotiwala Road",
    "Majhitar Industrial Area", "Plot L-41, Verna Industrial Estate", "Plot 8, Genome Valley, Shamirpet", "Gat No. 312, Talegaon Dabhade Road", "Plot 17, Rajiv Gandhi Infotech Park, Hinjewadi",
    "Indrayani House, 21 Senapati Bapat Road"])
_tl("site", "addressLine2", ["Karegaon, Taluka Shirur", "Karegaon, Taluka Shirur", "Taluka Daund", "Tehsil Nalagarh", "Rangpo", "Verna, Salcete", "Turkapally", "Talegaon Dabhade, Taluka Maval",
    "Phase 1, Hinjewadi", "Shivajinagar"])
_tl("site", "erpPlantCode", ["RJ01", "RJ02", "KR01", "BD01", "SK01", "GA01", "HY01", "WH02", "QC01", "HO02"])
_tl("site", "headcount", [620, 180, 410, 350, 290, 330, 140, 45, 85, 160])
VAL[("enterprise", "legalName")] = lambda env: env["disp"].replace("Ltd.", "Limited").replace("Pvt.", "Private")
VAL[("manufacturer", "website")] = lambda env: "https://www.%s.example" % name(U.MASTER["manufacturer"][env["i"]] if "manufacturer" in U.MASTER else U.PROC[env["i"]]["mfr"]).split(" ")[0].lower()
_tl("supplier", "addressLine1", ["Plot 14, MIDC Chemical Zone, Kurkumbh", "Survey 211, Vasai Industrial Estate", "Plot 7, MIDC Taloja", "Plot 33, GIDC Ankleshwar", "Plot 52, MIDC Tarapur",
    "Plot 9, Pirangut Industrial Area", "Office 401, Baner Business Bay", "Plot 61, MIDC Shendra", "Gat 118, Kharabwadi, Talegaon Road", "Office 12, Wakad Commercial Square"])
_tl("supplier", "addressCity", ["Daund", "Vasai", "Navi Mumbai", "Ankleshwar", "Palghar", "Pune", "Pune", "Aurangabad", "Pune", "Pune"])
_tl("supplier", "addressState", ["Maharashtra", "Maharashtra", "Maharashtra", "Gujarat", "Maharashtra", "Maharashtra", "Maharashtra", "Maharashtra", "Maharashtra", "Maharashtra"])
_tl("supplier", "addressPostalCode", ["413802", "401208", "410208", "393002", "401506", "412115", "411045", "431154", "410501", "411057"])
_tl("user", "userName", ["amol.shinde", "pooja.kadam", "rahul.waghmare", "shalini.rao", "nilesh.sawant", "farhan.qureshi", "vandana.iyer", "prakash.jagtap", "tejas.bapat", "mes.system.ph"])
_tl("user", "email", ["amol.shinde@indrayanipharma.example", "pooja.kadam@indrayanipharma.example", "rahul.waghmare@indrayanipharma.example", "shalini.rao@indrayanipharma.example",
    "nilesh.sawant@indrayanipharma.example", "farhan.qureshi@indrayanipharma.example", "vandana.iyer@indrayanipharma.example", "prakash.jagtap@indrayanipharma.example",
    "tejas.bapat@indrayanipharma.example", None])
_tl("user", "mobile", ["+91-98500-31142", "+91-98500-31377", "+91-98500-31419", None, "+91-98500-31061", "+91-98500-31208", "+91-98500-31013", "+91-98500-31290", None, None])
_tl("role", "description", ["Runs process steps in the granulation, compression and coating suites and records results in the electronic batch record",
    "Runs the blister, bottle and cartoning lines and records in-process checks", "Leads the shift crew, verifies line clearance and signs critical steps",
    "Reviews executed batch records and exceptions before release", "Certifies batches for sale and approves deviations, CAPA and changes",
    "Tests samples in the quality control laboratory and records results", "Carries out breakdown and preventive maintenance and calibration of process equipment",
    "Receives, samples, dispenses and issues material", "Validates computerised systems and maintains master data and recipes", "Administers users, roles and system settings"])
_tl("customer", "ppapLevelDefault", N10)

# ---------------------------------------------------------------- product definition
_tl("item", "drawingNo", ["SPEC-FP-PCM500-B10", "SPEC-FP-PCM500-H100", "SPEC-IP-PCM500-FCT", "SPEC-IP-PCM500-GRN", "SPEC-RM-PCM-API", "SPEC-RM-MCC-101", "SPEC-RM-PVP-K30",
    "SPEC-RM-SSG", "SPEC-RM-MGST", "SPEC-RM-COAT-WHT"])
_tl("item", "erpMaterialNo", ["0000000000610%05d" % k for k in (50010, 50020, 40010, 30010, 10010, 20101, 20130, 20140, 20150, 20160)])
_tl("item", "netWeightKg", ["0.072", "0.086", "0.001", "1.000", "1.000", "1.000", "1.000", "1.000", "1.000", "1.000"])
_tl("item", "grossWeightKg", ["0.074", "0.089", "0.001", "1.000", "1.000", "1.000", "1.000", "1.000", "1.000", "1.000"])
_tl("item", "standardCostInr", ["38.50", "41.20", "0.28", "260.00", "420.00", "185.00", "960.00", "410.00", "330.00", "1450.00"])
_tl("item", "isSerialised", [True, True] + [False] * 8)
_tl("item", "isLotControlled", [True] * 10)
_tl("item", "materialSpecification", ["Indian Pharmacopoeia 2022, Paracetamol Tablets", "Indian Pharmacopoeia 2022, Paracetamol Tablets", "In-house specification SPEC-IP-PCM500-FCT",
    "In-house specification SPEC-IP-PCM500-GRN", "Indian Pharmacopoeia 2022, Paracetamol", "Ph. Eur. Microcrystalline Cellulose", "Ph. Eur. Povidone", "Ph. Eur. Sodium Starch Glycolate",
    "Ph. Eur. Magnesium Stearate", "Supplier specification IFC-WHT-01"])
_tl("item", "materialGrade", [None, None, None, None, "Dense powder", "PH 101", "K30", "Type A", "Vegetable grade", "White, PVA based"])
_tl("item", "shelfLifeDays", [1095, 1095, 180, 90, 1825, 1825, 1095, 1095, 1095, 730])
_tl("item", "openLifeMinutes", [None, None, None, None, None, 720, 480, None, None, None])
_tl("item", "safetyCharacteristic", [True, True, True, True, True, False, False, False, False, False])
_r("item", "baseUnitOfMeasureId", [0, 0, 0, 1, 1, 1, 1, 1, 1, 1])
_r("item", "defaultStorageLocationId", [8, 8, 4, 4, 1, 1, 2, 2, 2, 1])
_r("item", "lotNumberRangeId", [0, 0, 0, 3, 2, 2, 2, 2, 2, 2])
_tl("unitOfMeasure", "symbol", ["ea", "kg", "mg", "%", "N", "N.m", "mbar", "degC", "min", "mm"])
_tl("unitOfMeasure", "isoCode", ["C62", "KGM", "MGM", "P1", "NEW", "NU", "MBR", "CEL", "MIN", "MMT"])
_tl("unitOfMeasure", "dimension", ["Count", "Mass", "Mass", "Ratio", "Force", "Torque", "Pressure", "Temperature", "Time", "Length"])
_tl("unitOfMeasure", "decimalPlaces", [0, 3, 1, 2, 0, 2, 1, 1, 1, 2])
_tl("productVariant", "optionsPistonDiameterMm", N10)
_tl("productVariant", "optionsColour", ["White"] * 10)
# bill of material: granulation formula per kg of granules, coating per tablet, packs per carton or bottle of 100 tablets
PARENTIDX["billOfMaterialComponent"] = [3, 3, 3, 3, 3, 2, 2, 0, 1, 7]
_r("billOfMaterialComponent", "componentItemId", [4, 5, 6, 7, 8, 3, 9, 2, 2, 4])
_r("billOfMaterialComponent", "operationId", [1, 1, 1, 1, 3, 4, 5, 7, 6, 1])
CTXOF["billOfMaterialComponent"] = [1, 1, 1, 1, 3, 4, 5, 7, 6, 1]
_r("billOfMaterialComponent", "unitOfMeasureId", [1, 1, 1, 1, 1, 1, 1, 0, 0, 1])
_tl("billOfMaterialComponent", "quantity", ["0.8333", "0.0917", "0.0333", "0.0333", "0.0083", "0.000600", "0.000018", "100", "100", "0.8333"])
_tl("billOfMaterialComponent", "scrapPct", ["0.5", "1.0", "1.0", "1.0", "2.0", "0.5", "8.0", "0.5", "0.5", "0.5"])
CTXOF["recipe"] = list(range(10))
VAL[("recipe", "programNo")] = lambda env: env["p"]["prog"]
_tl("recipe", "changeReasonText", [None, "Wet massing end-point changed to impeller power (ECN-2026-0032)", "Inlet air temperature raised from 55 to 60 degC to shorten drying", None,
    "Main compression force window 15-21 kN after hardness limit change (ECN-2026-0027)", None, "Cap torque window 1.2-2.0 N.m (ECN-2026-0033)",
    "Leak test hold time 30 s after study SIM-2026-014", None, "Kenya pack code layout added (ECN-2026-0034)"])
_tl("characteristic", "positionCount", [1, 1, 5, 1, 5, 1, 1, 1, 1, 1])
VAL[("controlPlanLine", "equipmentText")] = lambda env: "%s %s" % (name(env["p"]["eq"]), code(env["p"]["eq"]))

# ---------------------------------------------------------------- equipment, tools and gauges
_tl("equipment", "serialNo", ["ESC-DFB-19-0457", "SAM-RMG-18-0221", "GLT-WSG-20-3318", "SAM-OCB-21-0074", "FET-FE35-17-0012", "GAC-48-22-1187", "ACG-SC120-22-1907",
    "ACG-BMAX-21-5540", "OPT-CSM-23-0931", "MT-C3570-22-4416"])
_tl("equipment", "controllerMake", ["Mettler Toledo", "Siemens", "Siemens", "Siemens", "Fette", "Rockwell Automation", "ACG", "ACG", "Optel", "Mettler Toledo"])
_tl("equipment", "controllerModel", ["IND570", "S7-1500", "S7-1500", "S7-1200", "FE Control 5", "CompactLogix 5380", "SC-CTRL 2.8", "BMAX PLC", "Vision Station 6", "C35 controller"])
_tl("equipment", "readinessReasonText", [None, "Under maintenance: impeller seal replacement (MWO-2026-000347)", None, None, None, None, None, None, None, None])
_tl("equipment", "acquisitionCostInr", ["3200000.00", "18500000.00", "24000000.00", "6500000.00", "42000000.00", "15500000.00", "9800000.00", "36000000.00", "12500000.00", "7400000.00"])
_tl("tool", "cavities", [0, 0, 0, 0, 45, 0, 0, 10, 0, 0])
_tl("tool", "regrindCount", [0, 0, 0, 0, 2, 0, 0, 0, 0, 0])
_tl("tool", "maxRegrinds", [0, 0, 0, 0, 5, 0, 0, 0, 0, 0])
_tl("gauge", "model", ["IND570 with PFA579", "SW-100", "HC103", "Alliance e2695", "XPR226", "ML6002T", "TT02", "VLT-500", "LVS-9585", "8M"])
_tl("gauge", "serialNo", ["MT-IND-21-0457", "SW-19-1132", "MT-HC-22-0771", "WAT-20-0098", "MT-XPR-21-4410", "MT-ML-23-0261", "TT-22-1904", "VLT-21-3327", "LVS-23-0882", "DT-18-0044"])
_GR = [("0.000", "150.000", "0.010", "0.020"), ("0.0", "600.0", "0.1", "0.2"), ("0.00", "100.00", "0.01", "0.05"), ("0.0", "200.0", "0.1", "0.5"), ("0.0", "220000.0", "0.1", "0.2"),
       ("0.0", "6200000.0", "10.0", "50.0"), ("0.00", "5.00", "0.01", "0.03"), ("-1000.0", "0.0", "1.0", "2.0"), ("0.00", "4.00", "0.01", "0.05"), ("0.0", "500.0", "1.0", "2.0")]
for _n, _k in enumerate(["rangeMin", "rangeMax", "resolution", "accuracy"]): VAL[("gauge", _k)] = [x[_n] for x in _GR]
_r("gauge", "rangeUnitOfMeasureId", [1, 8, 3, 3, 2, 2, 5, 6, 9, 4])
_r("gauge", "manufacturerId", [9, None, 9, None, 9, 9, None, 7, 8, None])
_tl("gaugeCalibrationReading", "asFound", lambda env: fmt(float(env["p"]["nom"]), env["p"]["dp"]))
_tl("gaugeCalibrationReading", "asLeft", lambda env: fmt(float(env["p"]["nom"]), env["p"]["dp"]))
_tl("gaugeCalibrationReading", "tolerance", lambda env: fmt((float(env["p"]["usl"]) - float(env["p"]["lsl"])) / 10.0, env["p"]["dp"]))

# ---------------------------------------------------------------- reference data that is product specific in the Gamp universe
_ENUMV = [("operationExecution", "result", "OK"), ("operationExecution", "result", "Not OK"), ("leakTestResult", "verdict", "Pass"), ("leakTestResult", "verdict", "Fail"),
          ("lot", "lotType", "Supplier Lot"), ("lot", "lotType", "Granulation Lot"), ("lot", "lotType", "Coated Tablet Lot"), ("lot", "lotType", "Finished Goods Lot"),
          ("productionOrder", "orderType", "Production"), ("productionOrder", "orderType", "Validation Batch")]
def _scode(s): return s.upper().replace(" ", "_")
import spec_rules as _R
SPECIALIDENT["enumerationValue"] = lambda i: ("%s.%s.%s" % (_ENUMV[i][0], _ENUMV[i][1], _scode(_ENUMV[i][2])), _ENUMV[i][2])
VAL.update({("enumerationValue", "collectionName"): [_R.byent[x[0]]["collection"] for x in _ENUMV], ("enumerationValue", "fieldName"): [x[1] for x in _ENUMV],
 ("enumerationValue", "valueCode"): [_scode(x[2]) for x in _ENUMV], ("enumerationValue", "valueName"): [x[2] for x in _ENUMV],
 ("enumerationValue", "description"): ["Operation finished within all limits", "Operation finished with at least one result outside limits", "Both vacuum test stages within limits",
    "At least one vacuum test stage outside limits", "Material lot received from a supplier", "Granules from one granulation and drying sub-lot",
    "Coated tablets from one coating pan load", "Packed batch of finished goods", "Commercial batch made to the effective master manufacturing record",
    "Process performance qualification batch made under an approved protocol"],
 ("enumerationValue", "sequenceNo"): [1, 2, 1, 2, 1, 2, 3, 4, 1, 2], ("enumerationValue", "isDefault"): [True, False, True, False, True, False, False, False, True, False]})

# ---------------------------------------------------------------- merge the other two files
import pharma_rules_trans as _T
import pharma_rules_gmp as _G
for _m in (_T, _G):
    for _n in ("VAL", "REFIDX", "STATUSOF", "RECFMT", "PARENTIDX", "CTXOF", "POST", "NULLWHEN", "SPECIALIDENT", "GEN", "BOOLRULE", "ENUMRULE", "PKEY", "MASTER_ADD", "TITLES_ADD"):
        if hasattr(_m, _n): globals()[_n].update(getattr(_m, _n))
