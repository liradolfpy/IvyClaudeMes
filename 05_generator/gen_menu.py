"""Builds the SideBar menu for every ClaudeMES list screen (one menu item per query page configuration).

Source : 02_architecture/collection_inventory.md (kind, parent), 02_architecture/collection_type_matrix.csv (label)
Output : 04_reference_data/ui_controls/menu/menu.json  (mongo shell / Studio 3T format, like FormatMenu.json.txt)
Levels : 0 = module, 1 = functional section, 2 = query screen (dictName = <collection without u_>Query)
Rules  : skill mes-menu-builder
"""
import csv, os, sys
ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
INV = os.path.join(ROOT, "02_architecture", "collection_inventory.md")
MAT = os.path.join(ROOT, "02_architecture", "collection_type_matrix.csv")
OUT = os.path.join(ROOT, "04_reference_data", "ui_controls", "menu", "menu.json")

MODULES = [  # code, level 0 _id, icon
    ("mast", "2010", "bi/BiData"), ("prod", "2020", "bi/BiCube"), ("plan", "2030", "bi/BiCalendar"),
    ("matl", "2040", "bi/BiPackage"), ("trac", "2050", "bi/BiGitBranch"), ("qual", "2060", "bi/BiCheckShield"),
    ("perf", "2070", "bi/BiTachometer"), ("maint", "2080", "bi/BiWrench"), ("syst", "2090", "bi/BiCog"),
    ("ehs", "2100", "bi/BiFirstAid"), ("bmr", "2110", "bi/BiBook"), ("mmr", "2120", "bi/BiBookOpen"),
]
# Level 1 sections: module -> [(section label, [root entity names in display order])].
# Child, relationship and value-list collections follow their root entity.
SECTIONS = {
 "mast": [
  ("Organisation", ["enterprise", "site", "area", "line", "workCenter", "department", "designation", "employmentType", "costCenter"]),
  ("Equipment", ["equipment", "equipmentType", "manufacturer"]),
  ("Shifts And Calendars", ["shift", "workCalendar", "shiftRoster"]),
  ("People And Skills", ["user", "skill", "skillCategory", "skillCertification"]),
  ("Access Control", ["role", "permission", "signatureMeaning"]),
  ("Business Partners", ["customer", "supplier", "transporter"]),
  ("General Values", ["unitOfMeasure", "currency", "country", "language", "commodity"]),
 ],
 "prod": [
  ("Items And Variants", ["item", "productVariant", "itemGroup", "itemFamily", "vehicleModel", "market", "padCompound", "surfaceFinish", "ppeItem"]),
  ("BOM And Routing", ["billOfMaterial", "operation", "routing", "billOfProcess"]),
  ("Recipes And Instructions", ["recipe", "workInstruction"]),
  ("Engineering Change", ["engineeringChange"]),
 ],
 "plan": [
  ("Orders And Scheduling", ["customerSchedule", "productionOrder", "productionSchedule", "dispatchList"]),
  ("Execution", ["operationExecution", "stepCompletion", "operatorSession", "documentAcknowledgement", "labourBooking", "indirectActivity"]),
  ("WIP, Lots And Containers", ["wipUnit", "lot", "container", "containerType"]),
  ("Setup And Changeover", ["changeover", "setupVerification", "lineClearance", "recipeDownload", "interlockEvent"]),
  ("Andon And Handover", ["andonEvent", "andonType", "shiftHandover"]),
 ],
 "matl": [
  ("Storage And Inventory", ["storageLocation", "inventoryBalance", "stockStatus", "materialMovement", "movementType"]),
  ("Line Supply", ["materialRequest", "kit", "dispenseRecord", "materialConsumption", "exposureTimer", "replenishmentRule", "materialDemandForecast"]),
  ("Packing And Labels", ["packagingSpecification", "packType", "labelTemplate", "label"]),
  ("Receiving And Dispatch", ["goodsReceipt", "shipment"]),
 ],
 "trac": [
  ("Serialisation And Genealogy", ["serialNumber", "genealogyLink", "componentLotLink", "asBuiltRecord"]),
  ("Investigations", ["traceInvestigation"]),
 ],
 "qual": [
  ("Quality Planning", ["characteristic", "controlPlan", "inspectionPlan", "samplingPlan", "pfmea", "riskAssessment"]),
  ("Inspection And Defects", ["checkSheet", "checkSheetResult", "inspectionResult", "defectRecord", "defectCode", "defectGroup"]),
  ("SPC And Curves", ["spcChart", "spcSample", "curveEnvelope", "measurementCurve", "measurementCurvePoint"]),
  ("Nonconformance And CAPA", ["nonconformance", "qualityHold", "reworkOrder", "scrapRecord", "deviationPermit", "dispositionType", "capa"]),
  ("Gauges And MSA", ["gauge", "gaugeType", "gaugeCalibration", "msaStudy"]),
  ("Customer Quality", ["ppapSubmission", "customerComplaint", "complaintType", "productRecall"]),
  ("Audits", ["audit", "auditSchedule"]),
  ("Validation And Review", ["processValidation", "productQualityReview", "retentionSample", "environmentalMonitoringPoint", "environmentalMonitoringResult"]),
 ],
 "perf": [
  ("Production And OEE", ["productionCount", "oeeRecord", "workCenterPerformance", "operatorPerformance"]),
  ("Downtime And Losses", ["downtimeEvent", "reasonCode", "reasonCategory", "lossCategory", "lossSummary"]),
  ("Machine Data", ["equipmentState", "processTag", "processReading", "alarm", "alarmDefinition"]),
  ("Test Results", ["torqueResult", "leakTestResult"]),
  ("Energy", ["energyReading", "energyType"]),
 ],
 "maint": [
  ("Maintenance", ["maintenancePlan", "maintenanceWorkOrder", "reliabilitySummary"]),
  ("Equipment Records", ["equipmentLifecycleEvent", "logbookEntry", "cleaningRecord", "equipmentQualification"]),
  ("Spare Parts", ["sparePart", "sparePartTransaction"]),
  ("Tooling", ["tool", "toolType", "toolLifeRecord"]),
 ],
 "syst": [
  ("Integration", ["integrationConnector", "erpMessage", "businessEvent"]),
  ("Devices And Apps", ["iotDevice", "deviceType", "operatorApp"]),
  ("Rules And Notifications", ["interlockRule", "escalationRule", "alertRule", "notification", "notificationType"]),
  ("Configuration", ["systemConfiguration", "numberRange", "statusDefinition", "statusTransition", "enumerationValue", "recordPolicy", "savedView"]),
  ("Documents", ["controlledDocument", "documentType"]),
  ("Audit Trail And Signatures", ["auditTrail", "electronicSignature"]),
  ("Analytics", ["analyticsModel", "modelPrediction", "simulationStudy"]),
  ("Computerised System Compliance", ["computerisedSystem", "systemValidation", "systemPeriodicReview", "auditTrailReview", "userAccessReview", "backupRun"]),
 ],
 "ehs": [
  ("Safety Incidents", ["safetyIncident"]),
  ("Safety Masters", ["incidentType", "bodyPart", "injuryType"]),
 ],
 "bmr": [
  ("Batch Records", ["batchManufacturingRecord", "batchRecordReview", "batchRelease", "yieldReconciliation"]),
 ],
 "mmr": [
  ("Master Records", ["masterManufacturingRecord"]),
 ],
}
ROLES = ["Hod", "Line", "SiteAdmin", "SuperAdmin", "User", "LiraAdmin"]
STYLE = {"marginTop": "1rem", "marginLeft": "20"}

# ---- read model --------------------------------------------------------------------------
modname, inv = {}, []          # inv: (collection, kind, parent) in inventory order
for l in open(INV, encoding="utf-8"):
    p = [x.strip() for x in l.split("|")]
    if len(p) == 5 and p[1] in dict((m[0], 1) for m in MODULES):
        modname[p[1]] = p[2]
    if len(p) > 8 and p[2].startswith("u_mes_"):
        inv.append((p[2], p[3], p[5] if p[5] != "-" else None))
label = {r["Collection"]: r["Label"] for r in csv.DictReader(open(MAT, encoding="utf-8"))}
parent = {c: pa for c, k, pa in inv}
def root(c):
    while parent[c]:
        c = parent[c]
    return c
def ent(c):
    return c.split("_", 3)[3]

errors = []
assigned = {}
for code, secs in SECTIONS.items():
    for si, (sl, ents) in enumerate(secs):
        for e in ents:
            c = "u_mes_%s_%s" % (code, e)
            if c not in parent:
                errors.append("unknown entity " + c)
            elif parent[c]:
                errors.append("not a root entity " + c)
            elif c in assigned:
                errors.append("entity in two sections " + c)
            assigned[c] = (code, si)
for c, k, pa in inv:
    if pa is None and c not in assigned:
        errors.append("root entity without section " + c)
    if c not in label:
        errors.append("no label in matrix " + c)
if errors:
    sys.exit("\n".join(errors))

# ---- build documents --------------------------------------------------------------------
def doc(_id, seq, level, lab, link, pid, icon, roles, extra):
    d = {"_id": _id, "enable": True, "seq": ("int", seq), "level": ("int", level), "label": lab,
         "cat": "SideBar", "visible": True}
    if link:
        d["link"] = link
    d.update({"parentid": pid, "icon": icon, "typ": "individual", "act": True})
    d.update(roles)
    d["dest"] = "reactV04"
    d.update(extra)
    return d

ALL = {r: True for r in ROLES}
LEAF = dict(ALL, Line=False)
docs = []
for mseq, (code, mid, micon) in enumerate(MODULES, 1):
    mname = modname[code]
    mlabel = "".join(" " + ch if ch.isupper() and i else ch for i, ch in enumerate(mname)).replace("And ", "And ")
    docs.append(doc(mid, mseq, 0, mlabel, "/dashboard", None, micon, ALL, {"childWidth": "75vw"}))
    for si, (sl, ents) in enumerate(SECTIONS[code]):
        sid = "%s_%d" % (mid, (si + 1) * 100)
        docs.append(doc(sid, si + 1, 1, sl, None, mid, "fa/FaBoxes", ALL, {"colSize": ("dbl", "8.0"), "style": STYLE}))
        roots = ["u_mes_%s_%s" % (code, e) for e in ents]
        cols = []
        for r in roots:   # root entity first, then its descendants in inventory order
            cols.append(r)
            cols += [c for c, k, pa in inv if pa is not None and root(c) == r]
        if len(cols) > 900:
            sys.exit("section too large " + sid)
        for li, c in enumerate(cols):
            dn = c[2:] + "Query"
            link = "/dp?op=qy&dictName=%s&moduleName=%s" % (dn, mname)
            docs.append(doc("%s_%d" % (sid, 100 + li), li + 1, 2, label[c], link, sid, "bi/BiInfoCircle", LEAF, {"style": STYLE}))

# parents expose every role a child shows (rule 1.5)
byid = {d["_id"]: d for d in docs}
for d in reversed(docs):
    if d["parentid"]:
        for r in ROLES:
            if d[r]:
                byid[d["parentid"]][r] = True

# ---- write (mongo shell / Studio 3T style, same layout as FormatMenu.json.txt) ------------
def val(v, ind):
    if isinstance(v, tuple):
        return "NumberInt(%d)" % v[1] if v[0] == "int" else v[1]
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, dict):
        pad = " " * (ind + 4)
        inner = ", \n".join('%s"%s" : %s' % (pad, k, val(x, ind + 4)) for k, x in v.items())
        return "{\n" + inner + "\n" + " " * ind + "}"
    return '"%s"' % str(v).replace('"', "'")
out = []
for d in docs:
    out.append("{ \n" + ", \n".join('    "%s" : %s' % (k, val(v, 4)) for k, v in d.items()) + "\n}")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out) + "\n")
n = {lv: sum(1 for d in docs if d["level"][1] == lv) for lv in (0, 1, 2)}
print("menu.json written: %d documents (level 0: %d, level 1: %d, level 2: %d)" % (len(docs), n[0], n[1], n[2]))
