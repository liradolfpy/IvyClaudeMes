#!/usr/bin/env python3
"""
gen_stable.py - Stable (StandardTable) page configuration generator.

Builds the table page configuration (typ "PageConfigStable") of one or more
MES collections from the data model files of this repository:

  02_architecture/field_lists/*_field_list.md   key, BSON type, date tag, reference
  02_architecture/collection_type_matrix.md     screen label (page title)
  03_design/<module>/samples/<collection>.js    sample documents (column widths)

Output, one file per collection:
  04_reference_data/ui_controls/table/PageConfigs/PageConfig_<collection>.json
written in MongoDB shell style (NumberInt), like the query page configurations.

A column report (key, title, type, longest sample text, width) is printed to
stdout for review.

Usage (from the repository root or anywhere):
  python3 05_generator/gen_stable.py u_mes_perf_downtimeEvent [u_mes_perf_alarm ...]
  python3 05_generator/gen_stable.py --root <repo root> <collection> ...

Rules are documented in the Stable skill (SKILL.md). Change a rule there and
here together.
"""
import glob
import json
import math
import os
import re
import sys

# ---------------------------------------------------------------------------
# Rule constants
# ---------------------------------------------------------------------------
EXCLUDED_KEYS = {"_id", "app", "siteId", "siteName", "schemaVersion",
                 "createdById", "updatedById"}
AUDIT_TAIL = ["createdBy", "createdAt", "updatedBy", "updatedAt"]

DATE_FORMAT = "YYYY-MM-DD"
DATETIME_FORMAT = "YYYY-MM-DD HH:mm:ss"
DATE_DISPLAY_LEN = 10        # 2026-09-17
DATETIME_DISPLAY_LEN = 19    # 2026-09-17 06:51:40
BOOL_DISPLAY_LEN = 3         # Yes / No

ROW_CHAR_PX = 7              # row font: Roboto Condensed 12px, average glyph incl. digits
HEAD_CHAR_PX = 8             # header font: Roboto Condensed 14px
SORT_ICON_PX = 20            # tableConfig.isSortable is true
CELL_PADDING_PX = 20         # row-padding 5px left plus cell padding
WIDTH_MIN = 80
WIDTH_MAX = 300              # current standard maximum
WIDTH_STEP = 10

NUMERIC_TYPES = {"Int32", "Int64", "Decimal128", "Double"}

ACRONYMS = {"oee": "OEE", "capa": "CAPA", "ppm": "PPM", "rpn": "RPN", "spc": "SPC",
            "id": "ID", "kwh": "kWh", "uom": "UoM", "ncr": "NCR", "po": "PO",
            "bom": "BOM", "fai": "FAI", "msa": "MSA", "grr": "GRR", "iot": "IoT",
            "plc": "PLC", "erp": "ERP", "qr": "QR", "rfid": "RFID", "ip": "IP",
            "bmr": "BMR", "mmr": "MMR", "gmp": "GMP", "ehs": "EHS", "ppe": "PPE",
            "wip": "WIP", "pfmea": "PFMEA", "sla": "SLA", "cpk": "Cpk", "ppk": "Ppk", "fpy": "FPY", "mtbf": "MTBF", "mttr": "MTTR"}
UNIT_SUFFIXES = [("Minutes", "(min)"), ("Seconds", "(s)"), ("Sec", "(s)"), ("Hours", "(h)"), ("Days", "(days)"), ("Inr", "(INR)"), ("Mm", "(mm)"),
                 ("Percent", "(%)"), ("Pct", "(%)")]


SMALL_WORDS = {"of", "on", "in", "per", "and", "or", "to", "for"}


class NumberInt:
    def __init__(self, v):
        self.v = int(v)


# ---------------------------------------------------------------------------
# Readers
# ---------------------------------------------------------------------------
def read_field_list(root, collection):
    for path in sorted(glob.glob(os.path.join(root, "02_architecture", "field_lists", "*_field_list.md"))):
        lines = open(path, encoding="utf-8").read().splitlines()
        try:
            start = lines.index("## " + collection)
        except ValueError:
            continue
        fields = []
        for line in lines[start + 1:]:
            if line.startswith("## "):
                break
            m = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*$", line)
            if m:
                fields.append({"no": int(m.group(1)), "key": m.group(2), "type": m.group(3),
                               "tag": m.group(4), "ref": m.group(5)})
        return fields, path
    raise SystemExit("Collection %s not found in any field list" % collection)


def read_page_title(root, collection):
    path = os.path.join(root, "02_architecture", "collection_type_matrix.md")
    for line in open(path, encoding="utf-8"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and cells[2] == collection:
            return cells[4], cells[3], cells[0]
    raise SystemExit("Collection %s not found in collection_type_matrix.md" % collection)


def read_samples(root, collection):
    paths = glob.glob(os.path.join(root, "03_design", "*", "samples", collection + ".js"))
    if not paths:
        return [], None
    txt = open(paths[0], encoding="utf-8").read()
    body = txt[txt.index("insertMany(") + len("insertMany("):txt.rindex(")")]
    body = re.sub(r'ISODate\("([^"]*)"\)', r'"\1"', body)
    body = re.sub(r'NumberInt\((-?\d+)\)', r'\1', body)
    body = re.sub(r'NumberLong\("?(-?\d+)"?\)', r'\1', body)
    body = re.sub(r'NumberDecimal\("([^"]*)"\)', r'"\1"', body)
    body = re.sub(r'Double\(([^)]*)\)', r'\1', body)
    body = re.sub(r'^(\s*)([A-Za-z_$][\w$]*)\s*:', r'\1"\2":', body, flags=re.M)
    body = re.sub(r',(\s*[}\]])', r'\1', body)
    return json.loads(body), paths[0]


# ---------------------------------------------------------------------------
# Column rules
# ---------------------------------------------------------------------------
def display_pair(key, keyset):
    """Display key of a reference key: xId -> xName, or reportedById -> reportedBy."""
    if not key.endswith("Id") or len(key) <= 2:
        return None
    base = key[:-2]
    for cand in (base + "Name", base):
        if cand in keyset:
            return cand
    return None


def select_columns(fields):
    keyset = {f["key"] for f in fields}
    by_key = {f["key"]: f for f in fields}
    chosen, dropped = [], []
    for f in fields:
        k = f["key"]
        if k in EXCLUDED_KEYS:
            dropped.append((k, "excluded key (identifier, site, app or schema)"))
            continue
        if k in AUDIT_TAIL:
            continue
        pair = display_pair(k, keyset)
        if pair:
            dropped.append((k, "reference key, shown through %s" % pair))
            continue
        if k.endswith("Id") and f["ref"]:
            dropped.append((k, "reference key without a display key"))
            continue
        chosen.append(f)
    # business key first, fixed left
    first = by_key.get("recordNo")
    if first is None:
        first = next((f for f in chosen if f["type"] == "String"), chosen[0])
    chosen = [first] + [f for f in chosen if f is not first]
    chosen += [by_key[k] for k in AUDIT_TAIL if k in by_key]
    return chosen, dropped


def title_of(key, keyset):
    if key == "recordNo":
        return "Record No"
    base = key
    if key.endswith("Name") and (key[:-4] + "Id") in keyset:
        base = key[:-4]
    if re.match(r"^is[A-Z]", base):
        base = base[2:]
    unit = ""
    for suffix, label in UNIT_SUFFIXES:
        if base.endswith(suffix) and len(base) > len(suffix):
            base, unit = base[:-len(suffix)], label
            break
    words = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", base)
    words = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", words).split()
    out = []
    for i, w in enumerate(words):
        lw = w.lower()
        if i > 0 and lw in SMALL_WORDS:
            out.append(lw)
        else:
            out.append(ACRONYMS.get(lw, w[:1].upper() + w[1:]))
    if unit:
        out.append(unit)
    return " ".join(out)


def sample_len(field, samples):
    best = 0
    for doc in samples:
        v = doc.get(field["key"])
        if v is None:
            continue
        if field["type"] == "Date":
            n = DATE_DISPLAY_LEN if field["tag"] == "Date" else DATETIME_DISPLAY_LEN
        elif field["type"] == "Boolean":
            n = BOOL_DISPLAY_LEN
        else:
            n = len(str(v))
        best = max(best, n)
    return best


def width_of(title, max_len):
    content = max_len * ROW_CHAR_PX + CELL_PADDING_PX
    header = len(title) * HEAD_CHAR_PX + SORT_ICON_PX + CELL_PADDING_PX
    w = max(content, header, WIDTH_MIN)
    w = int(math.ceil(w / float(WIDTH_STEP)) * WIDTH_STEP)
    return min(w, WIDTH_MAX)


def build_column(field, keyset, samples, is_first):
    title = title_of(field["key"], keyset)
    max_len = sample_len(field, samples)
    col = {"title": title}
    if is_first:
        col["fixed"] = "left"
    col["width"] = "%dpx" % width_of(title, max_len)
    t = field["type"]
    if t == "Date":
        col["align"] = "center"
        col["DtFormat"] = DATE_FORMAT if field["tag"] == "Date" else DATETIME_FORMAT
        col["isIST"] = True
    elif t == "Boolean":
        col["align"] = "center"
        col["isBool"] = True
    elif t in NUMERIC_TYPES:
        col["align"] = "right"
    else:
        col["align"] = "left"
    col["data_index"] = field["key"]
    return col, max_len


# ---------------------------------------------------------------------------
# Document frame (fixed values copied from FormatTable.json)
# ---------------------------------------------------------------------------
def text_style(weight):
    return {"fontFamily": "Roboto Condensed", "fontWeight": weight, "fontSize": "18px",
            "color": "#ecf0f1", "textAlign": "left", "margin": "1px 1px 1px 1px"}


GRADIENT = "linear-gradient(90deg, hsla(211, 100%, 28%, 1) 30%, hsla(236, 100%, 8%, 1) 100%)"


def build_document(collection, page_title, module_code, columns):
    suffix = re.sub(r"^u_[a-z]+_[a-z]+_", "", collection)
    name = suffix + "Stable"
    config = {
        "headerRoute": None,
        "headerMultiline": None,
        "footerMultiline": {
            "background-color": "#B9C6DF",
            "multiCol": [[
                {"typ": "dataElement", "colSize": 6.0,
                 "key": {"text": "From", "style": text_style("300")},
                 "val": {"text": "", "style": text_style("600")}},
                {"typ": "blankSpace", "colSize": 1.0},
            ]],
        },
        "tableTitle": {"title-label": "", "font-family": "Roboto Condensed", "font-weight": "600",
                       "font-size": "30px", "font-color": "#B1B1B5", "visible": False},
        "tableSubTitle": {"visible": True, "title-label": page_title, "font-family": "Roboto Condensed",
                          "font-weight": "400", "font-size": "16px", "font-color": "#FFFFFF",
                          "background": GRADIENT, "display-download-icon": True,
                          "download-icon-color": "#0F62FE", "display-search-control": True,
                          "search-border-color": "0px solid #0d3070", "search-inner-color": "#B9C6DF",
                          "title-icon": "fa-list", "title-icon-size": "16px", "title-icon-color": "#FFFFFF"},
        "tableConfig": {"visible": True, "tableWidth": "80%", "divBackgroundColor": ["transparent", "transparent"],
                        "divAlignment": "left", "leftMargin": "0px", "innerLeftPadding": "15px",
                        "innerRightPadding": "15px", "line-color": "#2ECC71", "isSearchable": True,
                        "isSortable": True, "pagination": NumberInt(8), "exportToPdf": False,
                        "exportToCsv": True, "noOfRows": 10.0, "interval": NumberInt(3000000)},
        "header": {"background-color": "#4a4f59", "font-family": "Roboto Condensed", "font-weight": "100",
                   "font-size": "14px", "font-color": "#125FCC", "row-padding": "0px 0px 0px 2px",
                   "visible": True},
        "footer": {"background-color": GRADIENT, "font-family": "Roboto Condensed", "font-weight": "bold",
                   "font-size": "12px", "font-color": "#D0E2FF", "row-padding": "0px",
                   "display-pagination-control": True, "pagination-color": "#E5F6FF",
                   "pagination-visible": True, "visible": True, "noOfRows-visible": True,
                   "pageNo-visible": True, "pagination-background-color": "#0d3070",
                   "pagination-border": "1px solid #314f85"},
        "row": {"background-color": "#FFFFFF", "row-padding": "0px 0px 0px 5px", "font-family": "Roboto Condensed",
                "font-weight": "400", "font-size": "12px", "font-color": "#000000",
                "border-bottom-color": "#DCD5D5", "border-top-color": "#E74C3C", "border-bottom": "none",
                "alternateRows": ["stable-row-1", "stable-row-2"]},
        "column": columns,
        "rat": [],
        "ratConfig": [],
        "zenPop": {},
        "zenFuncs": {"headerRoute": False, "footerMultiline": True, "headerMultiline": False,
                     "footerButtons": True},
        "footerButtons": {},
    }
    return {
        "_id": name,
        "lid": "lid_999",
        "dictName": name,
        "typ": "PageConfigStable",
        "page": name,
        "app": "mes",
        "module": module_code,
        "dictData": {"config": config},
        "subTyp": "PhantomStable",
        "act": True,
    }


# ---------------------------------------------------------------------------
# MongoDB shell style writer
# ---------------------------------------------------------------------------
def shell(v, ind=0):
    pad = " " * ind
    if isinstance(v, NumberInt):
        return "NumberInt(%d)" % v.v
    if v is None:
        return "null"
    if v is True:
        return "true"
    if v is False:
        return "false"
    if isinstance(v, float):
        return repr(v)
    if isinstance(v, int):
        return str(v)
    if isinstance(v, str):
        return json.dumps(v, ensure_ascii=False)
    if isinstance(v, list):
        if not v:
            return "[]"
        inner = (",\n").join(" " * (ind + 4) + shell(x, ind + 4) for x in v)
        return "[\n" + inner + "\n" + pad + "]"
    if isinstance(v, dict):
        if not v:
            return "{}"
        inner = (",\n").join(" " * (ind + 4) + json.dumps(k) + " : " + shell(x, ind + 4) for k, x in v.items())
        return "{\n" + inner + "\n" + pad + "}"
    raise TypeError(type(v))


def check_parse(text):
    """The written file must parse once NumberInt is read as a number."""
    json.loads(re.sub(r"NumberInt\((-?\d+)\)", r"\1", text))


# ---------------------------------------------------------------------------
def generate(root, collection):
    fields, fl_path = read_field_list(root, collection)
    page_title, screen_type, module_code = read_page_title(root, collection)
    samples, sp_path = read_samples(root, collection)
    keyset = {f["key"] for f in fields}
    chosen, dropped = select_columns(fields)
    columns, report = [], []
    for i, f in enumerate(chosen):
        col, max_len = build_column(f, keyset, samples, i == 0)
        columns.append(col)
        report.append((i + 1, f["key"], col["title"], f["type"] + ("/" + f["tag"] if f["tag"] != "-" else ""),
                       max_len, col["width"], col["align"]))
    doc = build_document(collection, page_title, module_code, columns)
    text = shell(doc) + "\n"
    check_parse(text)
    out_dir = os.path.join(root, "04_reference_data", "ui_controls", "table", "PageConfigs")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "PageConfig_%s.json" % collection)
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)

    print("## %s - %s (%s)" % (collection, page_title, screen_type))
    print("")
    print("File: %s | _id: %s | samples: %d | columns: %d | total width: %dpx"
          % (os.path.relpath(out, root).replace(os.sep, "/"), doc["_id"], len(samples), len(columns),
             sum(int(c["width"][:-2]) for c in columns)))
    print("")
    print("| # | data_index | title | type | longest sample | width | align |")
    print("|---|---|---|---|---|---|---|")
    for r in report:
        print("| %d | %s | %s | %s | %d | %s | %s |" % r)
    print("")
    print("Left out: " + "; ".join("%s (%s)" % d for d in dropped))
    no_sample = [r[1] for r in report if r[4] == 0]
    if no_sample:
        print("")
        print("No non-null sample value (width from title only): " + ", ".join(no_sample))
    print("")


def main(argv):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    args = list(argv)
    if args[:1] == ["--root"]:
        root, args = args[1], args[2:]
    if not args:
        raise SystemExit(__doc__)
    for c in args:
        generate(root, c)


if __name__ == "__main__":
    main(sys.argv[1:])
