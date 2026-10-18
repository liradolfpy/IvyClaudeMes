#!/usr/bin/env python3
"""
gen_query.py - query page configuration (PageConfigQuery), IvyConfig and dynamic
dropdown registry generator for MES list screens.

For every collection listed in SCREENS it writes, in the same step:

  04_reference_data/ui_controls/query/PageConfigs/<collection>.json   (skill mes-query-control 0.19)
  04_reference_data/ui_controls/query/IvyConfig/<collection>Ivy.json  (skill mes-ivy-config 1.0)

and adds every registry document its /dd controls need to

  04_reference_data/ui_controls/query/u_int_dynamicDropdown.json      (skill mes-query-control 0.19, section 14)

keeping the existing registry documents (with their dt and rel) unchanged.
All files are written in MongoDB shell style (NumberInt, ISODate), like the
files already in those folders.

Inputs read from the repository:
  02_architecture/field_lists/*_field_list.md     key, BSON type, reference (data_index, p_data_index, Ivy types)
  02_architecture/collection_type_matrix.csv      screen label (pageTitle)
  02_architecture/collection_inventory.md         module names, display key of each collection (/dd val)
  04_reference_data/code_lists/status_values.md   status dropdown values
  04_reference_data/code_lists/enumeration_values.md  allowed values of category keys
  04_reference_data/ui_controls/query/u_int_mdict.json  dictionaries available to /mdict

The control decisions (which keys become controls, type, source, default range)
are made with the skill's procedure and recorded in SCREENS below, one entry per
collection, in display order. To change a screen, change its entry here and rerun.
SCREENS covers the PlanningAndExecution module (43 collections, 17 Oct 2026).
The 24 PerformanceManagement and ToolingAndMaintenance configurations were built
before this generator existed; they are not regenerated, but --check verifies them.

Usage (from the repository root or anywhere):
  python3 05_generator/gen_query.py plan                 generate every SCREENS entry of module plan
  python3 05_generator/gen_query.py u_mes_plan_lot ...   generate the named collections
  python3 05_generator/gen_query.py --check              run the checklist on every file in PageConfigs
  python3 05_generator/gen_query.py --root <repo> ...    explicit repository root

Rules are documented in the skills mes-query-control 0.19 and mes-ivy-config 1.0
(library E:/Ivy/Claude/ClaudeSkills/MintSkills/UiSkills). Change a rule there and
here together.
"""
import csv
import datetime
import glob
import json
import os
import re
import sys

# ---------------------------------------------------------------------------
# Rule constants (skill mes-query-control 0.19, mes-ivy-config 1.0)
# ---------------------------------------------------------------------------
COL_SIZE = 8
LABEL_COL_SPAN = 8
SEARCH_LENGTH = 4
SEARCH_PLACEHOLDER = "Type min 4 characters"
DATE_FORMAT = "YYYY-MM-DD"
MAX_CONTROLS = 8
MAX_DATA_VALUES = 10
MAX_LABEL = 25
AUDIT_KEYS = ["createdAt", "createdById", "createdBy", "updatedAt", "updatedById", "updatedBy"]
IVY_TYPES = {"String": "string", "Boolean": "bool", "Int32": "int", "Int64": "int",
             "Decimal128": "decimal", "Double": "double", "Date": "Date"}
BOOL_DATA = {"true": "Yes", "false": "No"}

# Registry ids of the shared sources (profile section 2.1)
USER = ("u_mes_mast_user", "fullName")
TOOL = ("u_mes_maint_tool", "name")
STORAGE = ("u_mes_matl_storageLocation", "name")
PO = ("u_mes_plan_productionOrder", "recordNo")
LOT = ("u_mes_plan_lot", "recordNo")
WIP = ("u_mes_plan_wipUnit", "recordNo")
OPEX = ("u_mes_plan_operationExecution", "recordNo")
CHANGEOVER = ("u_mes_plan_changeover", "recordNo")
HANDOVER = ("u_mes_plan_shiftHandover", "recordNo")

# Display text of data maps whose stored values are not readable words
DATA_TEXT = {
    ("u_mes_plan_documentAcknowledgement", "relatedCollectionName"): {
        "u_mes_prod_workInstruction": "Work Instruction",
        "u_mes_prod_recipe": "Recipe",
        "u_mes_syst_controlledDocument": "Controlled Document",
    },
}

# Label overrides (default: key without Id / ById, camelCase split, Title Case)
LABELS = {
    "currentWorkCenterId": "Current Work Center",
    "ownerCustomerId": "Owner Customer",
    "ownerUserId": "Owner",
    "toUserId": "Escalated To",
    "performedByUserId": "Performed By",
    "userId": "User",
    "rule": "Sequencing Rule",
    "internalExternal": "Internal or External",
    "isReturnable": "Returnable",
    "isPaid": "Paid",
    "relatedCollectionName": "Document Source",
    "closed": "Closed",
    "passed": "Passed",
    "frozen": "Frozen",
}
ACRONYMS = {"Wip": "WIP", "Erp": "ERP", "Plc": "PLC"}


# ---------------------------------------------------------------------------
# Control decisions per collection (display order = modalElements order)
# R  = range picker on the time key (defaultFrom, defaultTo)
# MD = dropdown from /mdict (dictName)
# SH = Shift dropdown from cropdown "Shift"
# D  = hard-coded data dropdown (status, enumeration or Boolean)
# DD = /dd dynamic dropdown (coln, val); DS = /dd search dropdown (coln, val)
# ---------------------------------------------------------------------------
def R(key, frm, to):
    return {"kind": "range", "key": key, "from": frm, "to": to}


def MD(key, dict_name):
    return {"kind": "mdict", "key": key, "dict": dict_name}


def SH():
    return {"kind": "shift", "key": "shiftId"}


def D(key, multi=False):
    return {"kind": "data", "key": key, "multi": multi}


def DD(key, source):
    return {"kind": "dd", "key": key, "coln": source[0], "val": source[1], "search": False}


def DS(key, source):
    return {"kind": "dd", "key": key, "coln": source[0], "val": source[1], "search": True}


SCREENS = {
    # Plan and schedule screens: range -30 / 0 (skill 0.19, Q10)
    "u_mes_plan_customerSchedule": [
        R("horizonFrom", -30, 0), D("status"), MD("customerId", "Customer"), D("scheduleType")],
    "u_mes_plan_customerScheduleLine": [
        DS("customerScheduleId", ("u_mes_plan_customerSchedule", "recordNo")), MD("itemId", "Item"),
        D("firmness")],
    "u_mes_plan_productionOrder": [
        R("plannedStartAt", -30, 0), MD("lineId", "Line"), D("status"),
        MD("productVariantId", "ProductVariant"), D("orderType"), D("priority"), D("onHold")],
    "u_mes_plan_productionOrderRelease": [
        DS("productionOrderId", PO), DS("releasedById", USER)],
    "u_mes_plan_productionOrderLot": [
        DS("productionOrderId", PO), DS("lotId", LOT)],
    "u_mes_plan_productionSchedule": [
        R("productionDate", -30, 0), MD("lineId", "Line"), SH(), D("status"), D("frozen")],
    "u_mes_plan_productionScheduleSlot": [
        DS("productionScheduleId", ("u_mes_plan_productionSchedule", "recordNo")),
        DS("productionOrderId", PO), MD("itemId", "Item")],
    # Operational screens: range -7 / 0
    "u_mes_plan_dispatchList": [
        R("productionDate", -7, 0), MD("workCenterId", "WorkCenter"), SH(), D("status"), D("rule")],
    "u_mes_plan_dispatchListEntry": [
        DS("dispatchListId", ("u_mes_plan_dispatchList", "recordNo")), DS("productionOrderId", PO),
        D("status"), MD("itemId", "Item"), D("priority"), D("materialAvailable"), D("toolAvailable")],
    "u_mes_plan_operationExecution": [
        R("startedAt", -7, 0), DS("productionOrderId", PO), MD("workCenterId", "WorkCenter"),
        MD("equipmentId", "Equipment"), SH(), D("status"), MD("operationId", "Operation"), D("result")],
    "u_mes_plan_operationExecutionDefectCode": [
        DS("operationExecutionId", OPEX), MD("defectCodeId", "DefectCode")],
    "u_mes_plan_operationExecutionTool": [
        DS("operationExecutionId", OPEX), DS("toolId", TOOL)],
    "u_mes_plan_stepCompletion": [
        R("startedAt", -7, 0), DS("wipUnitId", WIP), MD("workCenterId", "WorkCenter"), D("status"),
        DD("workInstructionId", ("u_mes_prod_workInstruction", "title")), D("withinLimits"),
        D("overridden")],
    "u_mes_plan_wipUnit": [
        R("startedAt", -7, 0), DS("productionOrderId", PO), MD("currentWorkCenterId", "WorkCenter"),
        D("status"), MD("productVariantId", "ProductVariant"), D("qualityStatus"), D("onHold")],
    "u_mes_plan_wipUnitCompletedStep": [
        DS("wipUnitId", WIP)],
    "u_mes_plan_lot": [
        R("manufacturedAt", -7, 0), DS("productionOrderId", PO), DS("storageLocationId", STORAGE),
        D("status"), D("lotType"), MD("itemId", "Item"), D("qualityStatus"), D("onHold")],
    "u_mes_plan_lotParentLot": [
        DS("lotId", LOT), DS("parentLotId", LOT)],
    "u_mes_plan_lotAttributesCavityNo": [
        DS("lotId", LOT)],
    "u_mes_plan_container": [
        R("packedAt", -7, 0), DS("storageLocationId", STORAGE), D("status"),
        MD("containerTypeId", "ContainerType"), MD("ownerCustomerId", "Customer"), D("isReturnable"),
        D("onHold")],
    "u_mes_plan_containerLot": [
        DS("containerId", ("u_mes_plan_container", "recordNo")), DS("lotId", LOT)],
    "u_mes_plan_labourBooking": [
        R("productionDate", -7, 0), DS("productionOrderId", PO), MD("workCenterId", "WorkCenter"), SH(),
        D("status"), DS("userId", USER), D("bookingType"), MD("indirectActivityId", "IndirectActivity")],
    "u_mes_plan_changeover": [
        R("startedAt", -7, 0), MD("lineId", "Line"), MD("workCenterId", "WorkCenter"), D("status"),
        D("changeoverType")],
    "u_mes_plan_changeoverStep": [
        DS("changeoverId", CHANGEOVER), D("internalExternal"), DS("completedById", USER)],
    "u_mes_plan_changeoverRemovedTool": [
        DS("changeoverId", CHANGEOVER), DS("removedToolId", TOOL)],
    "u_mes_plan_changeoverInstalledTool": [
        DS("changeoverId", CHANGEOVER), DS("installedToolId", TOOL)],
    "u_mes_plan_changeoverPerformedByUser": [
        DS("changeoverId", CHANGEOVER), DS("performedByUserId", USER)],
    "u_mes_plan_shiftHandover": [
        R("productionDate", -7, 0), MD("lineId", "Line"), SH(), D("status")],
    "u_mes_plan_shiftHandoverProductionOrder": [
        DS("shiftHandoverId", HANDOVER), DS("productionOrderId", PO)],
    "u_mes_plan_shiftHandoverDowntimeEvent": [
        DS("shiftHandoverId", HANDOVER), DS("downtimeEventId", ("u_mes_perf_downtimeEvent", "recordNo"))],
    "u_mes_plan_shiftHandoverNonconformance": [
        DS("shiftHandoverId", HANDOVER), DS("nonconformanceId", ("u_mes_qual_nonconformance", "title"))],
    "u_mes_plan_shiftHandoverOpenItem": [
        DS("shiftHandoverId", HANDOVER), DS("ownerUserId", USER), D("closed")],
    # Worked example of the skill (section 12): multi-select status, compelling reason:
    # the open-calls board must show Raised and Acknowledged together
    "u_mes_plan_andonEvent": [
        R("raisedAt", -7, 0), MD("lineId", "Line"), MD("workCenterId", "WorkCenter"), SH(),
        D("status", multi=True), MD("andonTypeId", "AndonType"), D("lineStopped")],
    "u_mes_plan_andonEventEscalation": [
        DS("andonEventId", ("u_mes_plan_andonEvent", "description")), DS("toUserId", USER), D("channel")],
    # Master screens: no period control
    "u_mes_plan_indirectActivity": [
        D("status"), DD("costCenterId", ("u_mes_mast_costCenter", "name")), D("isPaid")],
    "u_mes_plan_containerType": [
        D("status"), D("isReturnable")],
    "u_mes_plan_andonType": [
        D("status"), DD("responsibleDepartmentId", ("u_mes_mast_department", "name"))],
    # Station evidence (D036 - D041)
    "u_mes_plan_operatorSession": [
        R("loginAt", -7, 0), MD("workCenterId", "WorkCenter"), MD("equipmentId", "Equipment"), SH(),
        D("status"), DS("userId", USER), D("authenticationMethod")],
    "u_mes_plan_documentAcknowledgement": [
        R("acknowledgedAt", -7, 0), MD("workCenterId", "WorkCenter"), SH(), D("status"),
        D("relatedCollectionName"), D("acknowledgementType"), DS("userId", USER)],
    "u_mes_plan_interlockEvent": [
        R("raisedAt", -7, 0), DS("productionOrderId", PO), MD("workCenterId", "WorkCenter"),
        MD("equipmentId", "Equipment"), SH(), D("status"),
        DD("interlockRuleId", ("u_mes_syst_interlockRule", "name"))],
    "u_mes_plan_recipeDownload": [
        R("downloadedAt", -7, 0), MD("workCenterId", "WorkCenter"), MD("equipmentId", "Equipment"),
        D("status"), DD("recipeId", ("u_mes_prod_recipe", "name")), D("verificationResult"), D("trigger")],
    "u_mes_plan_setupVerification": [
        R("verifiedAt", -7, 0), DS("productionOrderId", PO), MD("workCenterId", "WorkCenter"),
        MD("equipmentId", "Equipment"), D("status"), MD("productVariantId", "ProductVariant"),
        D("trigger")],
    "u_mes_plan_setupVerificationItem": [
        DS("setupVerificationId", ("u_mes_plan_setupVerification", "recordNo")), D("checkType"),
        D("passed")],
    "u_mes_plan_lineClearance": [
        R("startedAt", -7, 0), DS("productionOrderId", PO), MD("lineId", "Line"),
        MD("workCenterId", "WorkCenter"), D("status"), D("clearanceType")],
}


# ---------------------------------------------------------------------------
# Shell-style serialiser (layout of the existing files)
# ---------------------------------------------------------------------------
class ISODate(str):
    pass


INLINE_EMPTY = {"default", "sourceParams"}


def dump(value, ind="", key=None):
    step = "    "
    if isinstance(value, ISODate):
        return 'ISODate("%s")' % value
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return "NumberInt(%d)" % value
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, dict):
        if not value:
            return "{}" if key in INLINE_EMPTY else "{\n\n" + ind + "}"
        items = [ind + step + json.dumps(k) + " : " + dump(v, ind + step, k) for k, v in value.items()]
        return "{\n" + ",\n".join(items) + "\n" + ind + "}"
    if isinstance(value, list):
        if not value:
            return "[]" if key in INLINE_EMPTY else "[\n\n" + ind + "]"
        items = [ind + step + dump(v, ind + step) for v in value]
        return "[\n" + ",\n".join(items) + "\n" + ind + "]"
    raise TypeError(value)


def parse_shell(text):
    """Read a shell-style JSON document or insertMany array."""
    text = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("//"))
    text = re.sub(r"NumberInt\((-?\d+)\)", r"\1", text)
    text = re.sub(r'ISODate\("([^"]+)"\)', r'{"$isodate": "\1"}', text)
    m = re.search(r"insertMany\(\s*(\[.*\])\s*\)\s*;?\s*$", text, re.S)
    if m:
        text = m.group(1)
    # unquoted keys (u_int_mdict.json style)
    text = re.sub(r'(?m)^(\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:', r'\1"\2":', text)

    def hook(d):
        if list(d.keys()) == ["$isodate"]:
            return ISODate(d["$isodate"])
        return d
    return json.loads(text, object_hook=hook)


# ---------------------------------------------------------------------------
# Model readers
# ---------------------------------------------------------------------------
def find_root(argv):
    if "--root" in argv:
        i = argv.index("--root")
        return argv[i + 1], argv[:i] + argv[i + 2:]
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(here), argv


def read_field_lists(root):
    """{collection: {"kind": ..., "parent": ..., "keys": [(key, bson, ref)]}}"""
    out = {}
    for path in sorted(glob.glob(os.path.join(root, "02_architecture", "field_lists", "*_field_list.md"))):
        coll = None
        for line in open(path, encoding="utf-8"):
            m = re.match(r"^## (u_mes_\w+)", line)
            if m:
                coll = m.group(1)
                out[coll] = {"keys": []}
                continue
            m = re.match(r"^Kind: (\w+) \| Data class: (\w+) \| Parent: (\S+)", line)
            if m and coll:
                out[coll].update(kind=m.group(1), dataClass=m.group(2), parent=m.group(3))
                continue
            m = re.match(r"^\| \d+ \| (\w+) \| (\w+) \| [^|]* \|(.*)\|\s*$", line)
            if m and coll:
                out[coll]["keys"].append((m.group(1), m.group(2), m.group(3).strip()))
    return out


def read_matrix(root):
    out = {}
    with open(os.path.join(root, "02_architecture", "collection_type_matrix.csv"), encoding="utf-8") as f:
        for row in csv.reader(f):
            if len(row) >= 5 and row[2].startswith("u_mes_"):
                out[row[2]] = {"type": row[3], "label": row[4]}
    return out


def read_inventory(root):
    modules, display = {}, {}
    for line in open(os.path.join(root, "02_architecture", "collection_inventory.md"), encoding="utf-8"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) in (3, 4) and re.fullmatch(r"[a-z]{3,5}", cells[0]) and cells[-1].isdigit():  # 4 cells since the Menu column (18 Oct 2026)
            modules[cells[0]] = cells[1]
        elif len(cells) >= 7 and cells[1].startswith("u_mes_"):
            display[cells[1]] = cells[-1]
    return modules, display


def read_status(root):
    out = {}
    for line in open(os.path.join(root, "04_reference_data", "code_lists", "status_values.md"), encoding="utf-8"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 3 and cells[1].startswith("u_mes_"):
            out[cells[1]] = [v.strip() for v in cells[2].split(",")]
    return out


def read_enums(root):
    out = {}
    for line in open(os.path.join(root, "04_reference_data", "code_lists", "enumeration_values.md"), encoding="utf-8"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 4 and cells[1].startswith("u_mes_"):
            out[(cells[1], cells[2])] = [v.strip() for v in cells[3].split(";")]
    return out


def read_mdict(root):
    path = os.path.join(root, "04_reference_data", "ui_controls", "query", "u_int_mdict.json")
    return {d["dictName"]: d for d in parse_shell(open(path, encoding="utf-8").read())}


def registry_path(root):
    return os.path.join(root, "04_reference_data", "ui_controls", "query", "u_int_dynamicDropdown.json")


def read_registry(root):
    path = registry_path(root)
    if not os.path.exists(path):
        return []
    return parse_shell(open(path, encoding="utf-8").read())


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------
def words(key):
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", key)
    return " ".join(ACRONYMS.get(w.capitalize(), w[0].upper() + w[1:]) for w in s.split())


def label_of(ctl):
    key = ctl["key"]
    if ctl["kind"] == "range":
        base = key[:-2] + "Date" if key.endswith("At") else key
        return words(base) + " Range"
    if key in LABELS:
        return LABELS[key]
    if key.endswith("ById"):
        return words(key[:-2])
    if key.endswith("Id"):
        return words(key[:-2])
    return words(key)


def name_key(key, keyset):
    if key.endswith("ById"):
        cand = key[:-2]
    elif key.endswith("Id"):
        cand = key[:-2] + "Name"
    else:
        return key + "Text"
    if cand not in keyset:
        raise ValueError("no display key for %s" % key)
    return cand


def registry_id(coln, val):
    return "%s__id_%s" % (coln, val)


def build_control(coll, ctl, model, status, enums):
    keys = {k: (t, r) for k, t, r in model["keys"]}
    key = ctl["key"]
    if key not in keys:
        raise ValueError("%s: key %s not in field list" % (coll, key))
    label = label_of(ctl)
    if ctl["kind"] == "range":
        return {
            "typ": "rangePicker", "label": label,
            "defaultFrom": ctl["from"], "defaultTo": ctl["to"],
            "required": True, "placeHolder": "Select " + label, "errorMessage": "Please Select " + label,
            "readOnly": False, "visible": True, "colSize": COL_SIZE, "labelColSpan": LABEL_COL_SPAN,
            "format": DATE_FORMAT, "data_index_from": "from", "data_index_to": "to", "data_index": key,
        }
    multi = ctl.get("multi", False)
    c = {"typ": "dropDown", "label": label, "default": [] if multi else "all", "includeAll": True,
         "multiSelect": multi, "required": True}
    search = ctl["kind"] == "dd" and ctl["search"]
    c["placeHolder"] = SEARCH_PLACEHOLDER if search else "Select " + label
    c["errorMessage"] = "Please Select " + label
    c.update({"readOnly": False, "visible": True, "isSearchable": True,
              "colSize": COL_SIZE, "labelColSpan": LABEL_COL_SPAN})
    if search:
        c["minSearchLength"] = SEARCH_LENGTH
        c["maxSearchLength"] = SEARCH_LENGTH
    c["data_index"] = key
    c["p_data_index"] = name_key(key, keys)
    if ctl["kind"] == "mdict":
        c.update({"api": "/mdict", "params": {"typ": ctl["dict"], "subTyp": "idame"}, "src": "api"})
    elif ctl["kind"] == "shift":
        c.update({"api": "/cropdown", "params": {"name": "Shift"}, "src": "api"})
    elif ctl["kind"] == "dd":
        dn = registry_id(ctl["coln"], ctl["val"])
        c.update({"api": "/dd", "params": {"dn": dn}, "src": "api", "source": "dynamic",
                  "sourceParams_dynamic": dn, "sourceParams": {}})
    elif ctl["kind"] == "data":
        bson = keys[key][0]
        if bson == "Boolean":
            data = dict(BOOL_DATA)
        else:
            values = status[coll] if key == "status" else enums.get((coll, key))
            if not values:
                raise ValueError("%s: no allowed values for %s" % (coll, key))
            text = DATA_TEXT.get((coll, key), {})
            data = {v: text.get(v, v) for v in values}
        c.update({"data": data, "src": "data"})
    return c


def build_page(coll, controls, matrix, ver):
    return {
        "_id": coll[2:] + "Query", "dictName": coll[2:] + "Query", "typ": "PageConfigQuery", "page": "Phantom",
        "dictData": {"config": {
            "method": "GET", "pageTitle": matrix[coll]["label"], "api": "/ivy/mes",
            "params": {"op": "st"}, "footerButtons": {}, "modalElements": controls}},
        "ver": ver, "unq": False, "subTyp": "PhantomQuery", "act": False,
        "approve": [], "delete": [], "dynamicModal": [], "edit": [], "mint": "1", "view": [],
        "rel": ver, "projid": "",
    }


def build_ivy(coll, page, model, modules):
    keys = {k: t for k, t, r in model["keys"]}
    code = coll.split("_")[2]
    get = []
    for e in page["dictData"]["config"]["modalElements"]:
        if e["typ"] == "rangePicker":
            get.append({"dinFrom": "from", "dinTo": "to", "din": e["data_index"], "typ": "range",
                        "format": DATE_FORMAT})
        else:
            get.append({"din": e["data_index"], "typ": IVY_TYPES[keys[e["data_index"]]]})
    post = [{"din": k, "typ": IVY_TYPES[t]} for k, t, r in model["keys"]
            if k != "_id" and k not in AUDIT_KEYS]
    return {
        "_id": coll[2:] + "Ivy", "code": code, "moduleName": modules[code], "collection": coll,
        "stableName": coll[2:] + "Stable", "typ": "IvyConfig", "label": "EnterpriseIvy",
        "dn": coll[2:] + "Ivy", "proj": [], "get": get, "post": post, "staticPost": {"act": True},
        "patch": [],
    }


def registry_doc(coln, val, now):
    return {
        "_id": registry_id(coln, val), "coln": coln, "query": {}, "key": "_id", "val": val, "act": True,
        "data": {}, "dt": ISODate(now.strftime("%Y-%m-%dT00:00:00.000+0000")),
        "projid": "mes_" + coln.split("_")[2], "rel": now.strftime("CL%Y%m%d-%H:%M"), "resp": "CL",
    }


def write_registry(root, docs):
    docs = sorted(docs, key=lambda d: d["_id"])
    body = ",\n".join("  " + dump(d, "  ") for d in docs)
    text = ("// Dynamic dropdown registry: one document per /dd source (coln, key, val); "
            "rules in skill mes-query-control, section 14\n"
            'db.getCollection("u_int_dynamicDropdown").insertMany([\n' + body + "\n]);\n")
    open(registry_path(root), "w", encoding="utf-8", newline="\n").write(text)


# ---------------------------------------------------------------------------
# Checklist (skill mes-query-control 0.19 section 13, mes-ivy-config 1.0 section 4)
# ---------------------------------------------------------------------------
def check(root, fields, matrix, inventory_display, mdict):
    qdir = os.path.join(root, "04_reference_data", "ui_controls", "query")
    registry = {d["_id"]: d for d in read_registry(root)}
    findings, n_files, n_controls = [], 0, 0
    order_rank = {"range": 0, "search": 1, "scope": 2, "shift": 3, "status": 4, "category": 5, "bool": 6}
    for path in sorted(glob.glob(os.path.join(qdir, "PageConfigs", "*.json"))):
        coll = os.path.basename(path)[:-5]
        n_files += 1
        f = lambda msg: findings.append("%s: %s" % (coll, msg))
        try:
            page = parse_shell(open(path, encoding="utf-8").read())
        except Exception as exc:
            f("does not parse (%s)" % exc)
            continue
        model = fields.get(coll)
        if not model:
            f("not in field lists")
            continue
        keys = {k: t for k, t, r in model["keys"]}
        cfg = page.get("dictData", {}).get("config", {})
        els = cfg.get("modalElements", [])
        n_controls += len(els)
        # 16, 20 frame
        if page.get("_id") != coll[2:] + "Query" or page.get("dictName") != page.get("_id"):
            f("frame _id / dictName")
        if page.get("typ") != "PageConfigQuery" or list(page.get("dictData", {}).keys()) != ["config"]:
            f("frame typ / dictData")
        if cfg.get("api") != "/ivy/mes" or cfg.get("params") != {"op": "st"} or cfg.get("footerButtons") != {} \
                or cfg.get("method") != "GET" or cfg.get("pageTitle") != matrix.get(coll, {}).get("label"):
            f("frame config")
        if page.get("ver") != page.get("rel") or not re.fullmatch(r"\d{8}-\d{4}", page.get("ver", "")):
            f("ver / rel")
        for k, v in (("unq", False), ("subTyp", "PhantomQuery"), ("act", False), ("mint", "1"), ("projid", "")):
            if page.get(k) != v:
                f("fixed field %s" % k)
        for k in ("approve", "delete", "dynamicModal", "edit", "view"):
            if page.get(k) != []:
                f("fixed field %s" % k)
        # 1, 2 period and count
        ranges = [e for e in els if e.get("typ") == "rangePicker"]
        ctype = matrix.get(coll, {}).get("type")
        if model.get("kind") == "entity" and ctype in ("Transaction", "Reports", "Telemetry", "Audit Trail"):
            if len(ranges) != 1:
                f("needs exactly one range picker")
        if len(ranges) > 1:
            f("more than one range picker")
        if len(els) > MAX_CONTROLS:
            f("more than %d controls" % MAX_CONTROLS)
        for i, e in enumerate(els):
            di = e.get("data_index")
            g = lambda msg: f("control %d (%s): %s" % (i + 1, di, msg))
            if di not in keys:                                          # 3
                g("data_index not a key")
                continue
            if e.get("required") is not True:                            # 15
                g("required is not true")
            lab = e.get("label", "")
            if len(lab) > MAX_LABEL:                                     # 11
                g("label longer than %d" % MAX_LABEL)
            if e.get("colSize") != COL_SIZE or e.get("labelColSpan") != LABEL_COL_SPAN:   # 10
                g("colSize / labelColSpan")
            display_key = (di.endswith("Name") and di[:-4] + "Id" in keys) or \
                          (di.endswith("By") and di + "Id" in keys)
            if di == "siteId" or di == "_id" or display_key:            # 9
                g("forbidden control key")
            if e.get("typ") == "rangePicker":
                if keys[di] != "Date" or e.get("data_index_from") != "from" or e.get("data_index_to") != "to" \
                        or e.get("format") != DATE_FORMAT or not lab.endswith(" Range") or i != 0:
                    g("range picker attributes")
                if e.get("placeHolder") != "Select " + lab or e.get("errorMessage") != "Please Select " + lab:
                    g("placeholder / error message")
                continue
            if e.get("typ") == "radio":
                if not 2 <= len(e.get("data", {})) <= 4 or e.get("default") not in e.get("data", {}):
                    g("radio options / default")
                continue
            if e.get("typ") != "dropDown":
                g("unknown typ")
                continue
            # 4 p_data_index
            pdi = e.get("p_data_index")
            try:
                expect = name_key(di, keys)
            except ValueError:
                expect = None
            if pdi != expect:
                g("p_data_index %s, expected %s" % (pdi, expect))
            # 7 includeAll, default, multiSelect
            if e.get("includeAll") is not True:
                g("includeAll not true")
            if e.get("multiSelect") is True:
                if e.get("default") != []:
                    g("multi-select default must be []")
            elif e.get("default") != "all":
                g("default must be all")
            # 20 isSearchable after visible
            ks = list(e.keys())
            if e.get("isSearchable") is not True or ks.index("isSearchable") != ks.index("visible") + 1:
                g("isSearchable")
            src, api = e.get("src"), e.get("api")
            is_search = "minSearchLength" in e
            # 11 placeholder / error
            if e.get("errorMessage") != "Please Select " + lab:
                g("error message")
            if e.get("placeHolder") != (SEARCH_PLACEHOLDER if is_search else "Select " + lab):
                g("placeholder")
            if is_search and (e.get("minSearchLength") != SEARCH_LENGTH or e.get("maxSearchLength") != SEARCH_LENGTH):
                g("search length")
            # 21 source / sourceParams only on /dd
            if (api == "/dd") != ("source" in e) or (api == "/dd") != ("sourceParams" in e):
                g("source / sourceParams only on /dd")
            if src == "data":                                            # 5, 6
                data = e.get("data", {})
                if len(data) > MAX_DATA_VALUES:
                    g("more than %d data values" % MAX_DATA_VALUES)
                if keys[di] == "Boolean" and data != BOOL_DATA:
                    g("Boolean data map")
                if di.endswith("Id"):
                    g("reference key from data")
            elif api == "/mdict":
                typ = e.get("params", {}).get("typ")
                if typ not in mdict or e["params"].get("subTyp") != "idame":
                    g("mdict dictionary %s missing" % typ)
                elif mdict[typ]["sourceCollection"] != refs_target(model, di):
                    g("mdict %s does not list %s" % (typ, refs_target(model, di)))
            elif api == "/cropdown":
                if di != "shiftId" or e.get("params") != {"name": "Shift"}:  # 17
                    g("cropdown")
            elif api == "/dd":
                dn = e.get("params", {}).get("dn")
                if dn != e.get("sourceParams_dynamic") or e.get("source") != "dynamic" or e.get("sourceParams") != {}:
                    g("/dd params")
                doc = registry.get(dn)
                if not doc:
                    g("registry document %s missing" % dn)
                else:
                    if dn.endswith("_All"):
                        g("registry id with _All")
                    target = refs_target(model, di)
                    if doc["coln"] != target or doc["key"] != "_id" or doc["val"] != inventory_display.get(target):
                        g("registry %s does not match %s.%s" % (dn, target, inventory_display.get(target)))
            else:
                g("unknown source")
            if di == "shiftId" and api != "/cropdown":
                g("shift must use cropdown Shift")
        # 18, 19 IvyConfig
        ipath = os.path.join(qdir, "IvyConfig", coll + "Ivy.json")
        if not os.path.exists(ipath):
            f("IvyConfig missing")
            continue
        ivy = parse_shell(open(ipath, encoding="utf-8").read())
        code = coll.split("_")[2]
        if ivy.get("_id") != coll[2:] + "Ivy" or ivy.get("dn") != ivy.get("_id") or ivy.get("code") != code \
                or ivy.get("collection") != coll or ivy.get("stableName") != coll[2:] + "Stable" \
                or ivy.get("typ") != "IvyConfig" or ivy.get("label") != "EnterpriseIvy" \
                or ivy.get("proj") != [] or ivy.get("patch") != [] or ivy.get("staticPost") != {"act": True}:
            f("IvyConfig frame")
        exp_get = []
        for e in els:
            if e.get("typ") == "rangePicker":
                exp_get.append({"dinFrom": "from", "dinTo": "to", "din": e["data_index"], "typ": "range",
                                "format": DATE_FORMAT})
            elif e.get("data_index") in keys:
                exp_get.append({"din": e["data_index"], "typ": IVY_TYPES[keys[e["data_index"]]]})
        if ivy.get("get") != exp_get:
            f("IvyConfig get list does not mirror modalElements")
        exp_post = [{"din": k, "typ": IVY_TYPES[t]} for k, t, r in model["keys"]
                    if k != "_id" and k not in AUDIT_KEYS]
        if ivy.get("post") != exp_post:
            f("IvyConfig post list does not match the field list")
    # registry integrity
    for dn, doc in registry.items():
        if dn != registry_id(doc["coln"], doc["val"]) or doc["coln"] not in fields \
                or doc["val"] not in {k for k, t, r in fields[doc["coln"]]["keys"]}:
            findings.append("registry %s: id or val does not match its collection" % dn)
    return n_files, n_controls, len(registry), findings


def refs_target(model, key):
    for k, t, r in model["keys"]:
        if k == key:
            return r.split(".")[0] if r.startswith("u_mes_") else None
    return None


# ---------------------------------------------------------------------------
def main(argv):
    root, argv = find_root(argv[1:])
    fields = read_field_lists(root)
    matrix = read_matrix(root)
    modules, display = read_inventory(root)
    status, enums = read_status(root), read_enums(root)
    mdict = read_mdict(root)
    if argv == ["--check"]:
        n, c, r, findings = check(root, fields, matrix, display, mdict)
        print("Checked %d page configurations (%d controls), their IvyConfigs and %d registry documents: "
              "%d findings" % (n, c, r, len(findings)))
        for line in findings:
            print("  " + line)
        return 1 if findings else 0
    targets = []
    for a in argv:
        if a in SCREENS:
            targets.append(a)
        elif re.fullmatch(r"[a-z]{3,5}", a):
            targets += [c for c in SCREENS if c.split("_")[2] == a]
        else:
            raise SystemExit("unknown collection or module: %s" % a)
    if not targets:
        raise SystemExit(__doc__)
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)   # IST
    ver = now.strftime("%Y%m%d-%H%M")
    qdir = os.path.join(root, "04_reference_data", "ui_controls", "query")
    registry = {d["_id"]: d for d in read_registry(root)}
    added = []
    for coll in targets:
        model = fields[coll]
        controls = [build_control(coll, ctl, model, status, enums) for ctl in SCREENS[coll]]
        page = build_page(coll, controls, matrix, ver)
        ivy = build_ivy(coll, page, model, modules)
        for ctl in SCREENS[coll]:
            if ctl["kind"] == "dd":
                dn = registry_id(ctl["coln"], ctl["val"])
                if dn not in registry:
                    registry[dn] = registry_doc(ctl["coln"], ctl["val"], now)
                    added.append(dn)
        with open(os.path.join(qdir, "PageConfigs", coll + ".json"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(dump(page) + "\n")
        with open(os.path.join(qdir, "IvyConfig", coll + "Ivy.json"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(dump(ivy) + "\n")
        print("%-45s %d controls  %s" % (coll, len(controls),
                                          ", ".join(c["data_index"] for c in controls)))
    write_registry(root, list(registry.values()))
    print("Generated %d page configurations and %d IvyConfigs (ver %s); registry: %d documents, %d added%s"
          % (len(targets), len(targets), ver, len(registry), len(added),
             (": " + ", ".join(sorted(added))) if added else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
