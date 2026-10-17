---
name: mes-menu-builder
description: Build or extend the React sidebar menu (cat SideBar, dest reactV04) in the 3-level _id format 1010 / 1010_100 / 1010_100_100, including the ClaudeMES menu.json with one item per query screen.
---

# Menu builder (SideBar menu documents)

Use this skill whenever the user asks to create, extend, reorder, re-permission or check menu entries for the React front end (dest `reactV04`), or to generate the menu for ClaudeMES modules.

The output is a set of MongoDB documents, one per menu node, in the exact format below. An existing front end reads this format, so do not rename keys, add keys or change BSON types unless the user asks. The project audit fields (`createdAt`, `createdBy`, `schemaVersion`, site reference, status) are not used in menu documents (owner decision, 16 Oct 2026).

## 1. Document format

The menu is a three-level tree. Every node is one document. The tree is held by `parentid`, and the `_id` encodes the path.

### 1.1 Keys on every level

| Key | BSON type | Value | Notes |
|---|---|---|---|
| `_id` | String | see section 2 | never an ObjectId |
| `enable` | Boolean | `true` | `false` disables the node without deleting it |
| `seq` | Int32 (`NumberInt`) | 1..n | display order among siblings |
| `level` | Int32 (`NumberInt`) | 0, 1 or 2 | equals the number of `_` in `_id` |
| `label` | String | text shown in the menu | Title Case, no leading or trailing spaces |
| `cat` | String | `"SideBar"` | |
| `visible` | Boolean | `true` | `false` hides the node but keeps the route reachable |
| `parentid` | String or null | `null` at level 0, otherwise the parent `_id` | |
| `icon` | String | `"<lib>/<ReactIconName>"` | lib is the react-icons folder in lower case: `bi`, `fa`, `bs`, `md`, `ai`, `tb`, `hi`; the name keeps its prefix, for example `bi/BiInfoCircle`, `fa/FaBoxes`, `bs/Bs2SquareFill` |
| `typ` | String | `"individual"` | |
| `act` | Boolean | `true` | |
| `Hod` | Boolean | role flag | |
| `Line` | Boolean | role flag | |
| `SiteAdmin` | Boolean | role flag | |
| `SuperAdmin` | Boolean | role flag | |
| `User` | Boolean | role flag | |
| `LiraAdmin` | Boolean | role flag | |
| `dest` | String | `"reactV04"` | |

### 1.2 Keys that depend on the level

| Key | Level 0 (module) | Level 1 (section) | Level 2 (screen) |
|---|---|---|---|
| `link` | `"/dashboard"`; omit when the module has no landing dashboard | omitted | required (section 3) |
| `childWidth` | String, `"75vw"` by default, `"50vw"` for a small module | omitted | omitted |
| `colSize` | omitted | Double `8.0` | omitted |
| `style` | omitted | `{ "marginTop": "1rem", "marginLeft": "20" }` | `{ "marginTop": "1rem", "marginLeft": "20" }` |

Note: `marginLeft` is the String `"20"` (no unit) in the existing data. Keep it exactly so.

### 1.3 Key order

Write keys in this order so new documents look like the existing ones:
`_id, enable, seq, level, label, cat, visible, link, parentid, icon, typ, act, Hod, Line, SiteAdmin, SuperAdmin, User, LiraAdmin, dest, childWidth | colSize, style`.

### 1.4 Default icons

| Level | Default icon |
|---|---|
| 0 | `bi/BiClipboardData`; ClaudeMES modules each have their own (see `gen_menu.py`) |
| 1 | `fa/FaBoxes` for a section, `fa/FaHeading` for a legacy report group |
| 2 query or report | `bi/BiInfoCircle` |
| 2 entry form | `bi/BiListOl` |
| 2 dashboard | `bi/BiBarChartAlt2` |
| 2 checklist or layout | `bs/Bs2SquareFill` |

Use a more specific react-icons name when the user gives one. Only use icon names that exist in react-icons; if unsure, use the default.

### 1.5 Default role flags (confirmed by the owner, 16 Oct 2026)

| Level | Hod | Line | SiteAdmin | SuperAdmin | User | LiraAdmin |
|---|---|---|---|---|---|---|
| 0 | true | true | true | true | true | true |
| 1 | true | true | true | true | true | true |
| 2 | true | false | true | true | true | true |

Rules:
- A parent must be visible to every role that can see at least one of its children. After applying user-requested permissions, set each role flag on a level 0 or level 1 node to true if any child has it true.
- If the user restricts a screen (for example "admins only"), set the other role flags to false on that leaf only.

## 2. `_id` scheme

| Level | Pattern | Example | How the next number is chosen |
|---|---|---|---|
| 0 | 4 digits | `1010` | next free 4-digit number in the block the user names; ClaudeMES uses `2010, 2020, ... 2120` |
| 1 | `<L0>_<NNN>` | `1010_100` | 100, 200, 300, ... (steps of 100) |
| 2 | `<L1>_<NNN>` | `1010_100_100` | 100, 101, 102, ... (steps of 1) |

Rules:
- `parentid` is always the `_id` with its last `_NNN` removed.
- `level` equals the count of `_` in `_id`.
- Never reuse or renumber an existing `_id`; screens may be bookmarked by it. To move a node, create a new `_id` and disable (`enable: false`) the old one only if the user asks.
- Legacy ids in use (from `04_reference_data/ui_controls/menu/FormatMenu.json.txt`): `1010` Visitor Management System, `1011` Safety, `1040` Test Level 0, `1125` TKM SPM. Ask the user for the current list before allocating new level 0 ids outside the 2010-2120 block.

## 3. Link patterns (level 2)

| Screen kind | Link | Dictionary name convention |
|---|---|---|
| Query, list or report | `/dp?op=qy&dictName=<Name>Query` | `VmsVisitorMovementQuery`, `SafetyIncidentQuery` |
| New-entry form | `/dp?op=sn&dictName=<Name>Entry` | `VmsDirectEntry`; optional `&type=<code>` when one dictionary serves several form types, for example `&type=D`, `&type=R`, `&type=I` |
| Layout or checklist form | `/dp?op=ly&dictName=<Name>` | `SampleChecklistForIncidentInvestigationSheet` |
| Dashboard | `/dc?dn=<dashboardName>` | `vms_SafetyDash_00` |
| Module landing page | `/dashboard` | level 0 only |

Legacy (non-MES) dictionary names are PascalCase with no spaces or underscores. Dashboard names are `<module>_<Name>Dash_<NN>`.
Never invent a dictionary name that the user says already exists under another name; ask for the real name when the user refers to an existing screen.

### 3.1 ClaudeMES query links (owner rules, 16 and 17 Oct 2026)

Every ClaudeMES query screen link is:

`/dp?op=qy&dictName=<dictName>&moduleName=<ModuleName>&dn=<dn>`

- `dictName` = the page configuration `_id` = the collection name without the leading `u_`, plus `Query`. `u_mes_maint_sparePart` gives `mes_maint_sparePartQuery`. This is the rule of `04_reference_data/ui_controls/query_control_instruction.md` (step 8); follow that file if it changes.
- `moduleName` = the module name from the module table of `02_architecture/collection_inventory.md`, with no spaces: `perf` gives `PerformanceManagement`, `maint` gives `ToolingAndMaintenance`.
- `dn` = the `dn` of the collection's IvyConfig (`04_reference_data/ui_controls/query/IvyConfig/<collection>Ivy.json`, matched by its `collection` key). Where no IvyConfig is written yet, use the IvyConfig rule (instruction step 9): the collection name without `u_`, plus `Ivy`. `u_mes_perf_alarm` gives `mes_perf_alarmIvy`. An IvyConfig whose `dn` breaks the rule, or whose `collection` is not in the inventory, is an error to report.

## 4. ClaudeMES module menus

Every query gets a menu item. Every collection of the model has a list screen (child and relationship collections too: their first query control is the parent), so every collection gets exactly one level 2 item, including the ones whose page configuration or IvyConfig is not written yet.

Inputs, on the user's computer under `E:/Ivy/Claude/ClaudeProjects/ClaudeMES` (or from the project with `project_read` when the computer is not linked):
- `02_architecture/collection_inventory.md`: module table, kind (entity, child, relationship, valueList) and parent collection of each collection;
- `02_architecture/collection_type_matrix.csv`: UI label of each collection;
- `04_reference_data/ui_controls/query/PageConfigs/*.json`: page configurations already written (their `_id` must each appear as a `dictName` in the menu);
- `04_reference_data/ui_controls/query/IvyConfig/*.json`: IvyConfigs already written (their `dn` goes into the link; each must appear as a `dn` in the menu).

Structure:
- Level 0 = one main menu per module, in the order `mast, prod, plan, matl, trac, qual, perf, maint, syst, ehs, bmr, mmr`, with `_id` `2010, 2020, ... 2120` and `seq` 1..12. Label = the module name split into words (`MasterDataManagement` becomes `Master Data Management`). `link` = `/dashboard`. Each module has its own icon.
- Level 1 = functional sections of the module (for example Quality Management: Quality Planning, Inspection And Defects, SPC And Curves, Nonconformance And CAPA, Gauges And MSA, Customer Quality, Audits, Validation And Review). A section holds a handful of related root entities; aim for 2 to 8 sections per module and no section with more than about 30 items.
- Level 2 = one query screen per collection, label from the matrix. A section lists each of its root entities followed by that entity's child, relationship and value-list collections (all descendants, in inventory order), so a header and its lines sit together.
- Every root entity is assigned to exactly one section; a new entity in the model that is in no section is an error the generator reports.

Generator: `05_generator/gen_menu.py` holds the section table (`SECTIONS`), reads the IvyConfig folder for `dn`, and builds the file. To change sections, labels or ids, change the table and rerun `python3 05_generator/gen_menu.py`; never edit `menu.json` by hand. Rerun it whenever IvyConfigs are added. When the model gains collections, add each new root entity to a section and rerun. Keep existing `_id`s stable: append new sections and new items at the end of their parent where possible, because inserting in the middle shifts the `_id`s of the items after it.

Output: one file, `04_reference_data/ui_controls/menu/menu.json`, holding all menu documents in the mongo shell / Studio 3T layout of `FormatMenu.json.txt` (documents one after another, 4-space indent, `"key" : value`, `NumberInt(...)`, `colSize : 8.0`).

## 5. Working steps

1. Collect the input: module or menu name, sections, screens (label, kind, dictionary or dashboard name), the level 0 id block, role restrictions. Ask in one question only for what cannot be inferred; when unattended, use the defaults in this skill and list every assumption.
2. If the user supplied existing menu documents, load them and treat their `_id`s as taken.
3. Build the tree in Python as plain dicts in key order (section 1.3), applying sections 1 to 4. For ClaudeMES, run or update `05_generator/gen_menu.py`.
4. Run the validator (section 6). Fix every error before delivering. For ClaudeMES, also check that every page configuration `_id` in `query/PageConfigs` appears as a `dictName`, every IvyConfig `dn` in `query/IvyConfig` appears as a `dn`, and the level 2 count equals the collection count of the inventory.
5. For ClaudeMES, the deliverable is the single file `04_reference_data/ui_controls/menu/menu.json` (section 4), written on the user's computer. For any other menu, deliver three things:
   - `menu_<name>.js`: a mongosh script that upserts every document (one `updateOne` with `upsert: true` and `$set` of all keys except `_id`, inside a `bulkWrite`), with `NumberInt(...)` for `seq` and `level`, and `8.0` written as a Double for `colSize`. Upserting makes the script safe to rerun.
   - `menu_<name>.json`: the same documents in Extended JSON (`{"$numberInt": "1"}` for Int32, `{"$numberDouble": "8.0"}` for `colSize`), one array, for import with mongoimport `--jsonArray`.
   - A short table in the reply: `_id`, level, seq, label, link, roles that are false.
6. State the assumptions made.

## 6. Validator

Write this to `validate_menu.py` and run `python3 validate_menu.py menu_<name>.json [existing.json]`. It reads Extended JSON or plain JSON.

```python
import json, sys

ROLES = ["Hod", "Line", "SiteAdmin", "SuperAdmin", "User", "LiraAdmin"]
COMMON = ["_id", "enable", "seq", "level", "label", "cat", "visible", "parentid", "icon",
          "typ", "act"] + ROLES + ["dest"]
ICON_LIBS = {"bi", "fa", "bs", "md", "ai", "tb", "hi", "io", "io5", "ri", "gi", "fi", "lu", "pi"}
LINK_STARTS = ["/dashboard", "/dp?op=qy&dictName=", "/dp?op=sn&dictName=",
               "/dp?op=ly&dictName=", "/dc?dn="]

def num(v):
    if isinstance(v, dict):
        for k in ("$numberInt", "$numberLong", "$numberDouble"):
            if k in v:
                return float(v[k]) if k == "$numberDouble" else int(v[k])
    return v

def is_digits(s, n):
    return len(s) == n and s.isdigit()

def load(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data if isinstance(data, list) else [data]

docs = load(sys.argv[1])
existing = load(sys.argv[2]) if len(sys.argv) > 2 else []
errors = []
ids = {}
for d in docs:
    i = d.get("_id")
    if not isinstance(i, str):
        errors.append("_id must be a string: %r" % (i,))
        continue
    if i in ids:
        errors.append("duplicate _id " + i)
    ids[i] = d
existing_ids = {e.get("_id") for e in existing}
all_ids = set(ids) | existing_ids

for i, d in ids.items():
    parts = i.split("_")
    lvl = num(d.get("level"))
    for k in COMMON:
        if k not in d:
            errors.append(i + ": missing key " + k)
    if lvl != len(parts) - 1:
        errors.append(i + ": level %r does not match _id depth %d" % (lvl, len(parts) - 1))
    if not is_digits(parts[0], 4) or any(not is_digits(p, 3) for p in parts[1:]):
        errors.append(i + ": _id segments must be 4 digits then 3-digit groups")
    for k in ["enable", "visible", "act"] + ROLES:
        if k in d and not isinstance(d[k], bool):
            errors.append(i + ": " + k + " must be Boolean")
    if not isinstance(num(d.get("seq")), int) or num(d.get("seq")) < 1:
        errors.append(i + ": seq must be a positive Int32")
    if d.get("cat") != "SideBar":
        errors.append(i + ": cat must be SideBar")
    if d.get("typ") != "individual":
        errors.append(i + ": typ must be individual")
    if d.get("dest") != "reactV04":
        errors.append(i + ": dest must be reactV04")
    icon = d.get("icon", "")
    if "/" not in icon or icon.split("/")[0] not in ICON_LIBS:
        errors.append(i + ": icon must be <lib>/<Name>, got " + repr(icon))
    elif not icon.split("/")[1].lower().startswith(icon.split("/")[0][:2]):
        errors.append(i + ": icon name prefix does not match library: " + icon)
    expected_parent = None if len(parts) == 1 else "_".join(parts[:-1])
    if d.get("parentid") != expected_parent:
        errors.append(i + ": parentid must be %r" % (expected_parent,))
    if expected_parent and expected_parent not in all_ids:
        errors.append(i + ": parent " + expected_parent + " does not exist")
    link = d.get("link")
    if lvl == 0:
        if "childWidth" not in d:
            errors.append(i + ": level 0 needs childWidth")
        if link not in (None, "/dashboard"):
            errors.append(i + ": level 0 link must be /dashboard or absent")
    if lvl == 1:
        if link is not None:
            errors.append(i + ": level 1 must not have a link")
        if num(d.get("colSize")) != 8.0:
            errors.append(i + ": level 1 colSize must be 8.0")
    if lvl == 2:
        if not link or not any(link.startswith(s) for s in LINK_STARTS):
            errors.append(i + ": level 2 link missing or not a known pattern: %r" % (link,))
        elif " " in link:
            errors.append(i + ": link contains a space")
        elif "dictName=mes_" in link:
            q = dict(x.split("=", 1) for x in link.split("?", 1)[1].split("&"))
            dn = q.get("dictName", "")
            base = dn[:-len("Query")] if dn.endswith("Query") else None
            if base is None or not q.get("moduleName") or q.get("dn") != base + "Ivy":
                errors.append(i + ": MES link must be /dp?op=qy&dictName=<c>Query&moduleName=<ModuleName>&dn=<c>Ivy")
    if lvl in (1, 2):
        st = d.get("style")
        if st != {"marginTop": "1rem", "marginLeft": "20"}:
            errors.append(i + ": style must be marginTop 1rem, marginLeft '20'")
    if lvl == 2:
        children = [c for c in ids if c.startswith(i + "_")]
        if children:
            errors.append(i + ": level 2 node has children")

# siblings: unique, contiguous seq; parents expose roles of their children
groups = {}
for i, d in ids.items():
    groups.setdefault(d.get("parentid"), []).append(d)
for p, kids in groups.items():
    seqs = sorted(num(k.get("seq")) for k in kids)
    if p is not None and seqs != list(range(1, len(seqs) + 1)):
        errors.append("children of %s: seq %r is not 1..%d without gaps or duplicates" % (p, seqs, len(seqs)))
    if p in ids:
        for r in ROLES:
            if any(k.get(r) for k in kids) and not ids[p].get(r):
                errors.append(p + ": role " + r + " is false but a child shows it")
    labels = [k.get("label") for k in kids]
    for lab in set(labels):
        if labels.count(lab) > 1:
            errors.append("children of %s: duplicate label %r" % (p, lab))

clash = set(ids) & existing_ids
for c in sorted(clash):
    errors.append(c + ": _id already exists in the existing menu")

if errors:
    print("FAILED: %d error(s)" % len(errors))
    for e in errors:
        print(" - " + e)
    sys.exit(1)
print("OK: %d menu documents valid" % len(ids))
```

Level 0 nodes are not checked for contiguous `seq` because the legacy menu gives every module `seq` 1. ClaudeMES modules are numbered 1..12.

The validator reads JSON. To check a file in the mongo shell layout, convert it first: replace `NumberInt(n)` with `{"$numberInt": "n"}`, put a comma between consecutive documents and wrap the whole in `[` `]`.

## 7. Known issues in the legacy data

Report these when the user supplies existing documents that show them; do not silently change existing documents:
- Siblings sharing a `seq` (in the sample: `1010_200` and `1010_300` both seq 2; all children of `1011_100` and of `1125_100` have seq 1). The display order is then undefined.
- Level 2 suffixes mixing steps of 1 (`_100, _101`) and steps of 100 (`_100, _200, _300`).
- Level 0 `seq` is 1 for every module.
- A group label equal to its module label (`1011` Safety / `1011_100` Safety, `1125` TKM SPM / `1125_100` TKM SPM).

## 8. Examples

ClaudeMES query item (generated):

```javascript
{ "_id": "2080_100_100", "enable": true, "seq": NumberInt(1), "level": NumberInt(2), "label": "Maintenance Plans", "cat": "SideBar", "visible": true, "link": "/dp?op=qy&dictName=mes_maint_maintenancePlanQuery&moduleName=ToolingAndMaintenance&dn=mes_maint_maintenancePlanIvy", "parentid": "2080_100", "icon": "bi/BiInfoCircle", "typ": "individual", "act": true, "Hod": true, "Line": false, "SiteAdmin": true, "SuperAdmin": true, "User": true, "LiraAdmin": true, "dest": "reactV04", "style": { "marginTop": "1rem", "marginLeft": "20" } }
```

Hand-specified legacy menu with an entry form. Input: "Add an Inspection module, id 1200, with a Reports group holding Inspection Report (dictionary InspectionResultQuery) and an Entry group holding Defect Entry (dictionary DefectEntry, type N), Line role can see the entry form."

```javascript
[
{ "_id": "1200", "enable": true, "seq": NumberInt(1), "level": NumberInt(0), "label": "Inspection", "cat": "SideBar", "visible": true, "link": "/dashboard", "parentid": null, "icon": "bi/BiClipboardData", "typ": "individual", "act": true, "Hod": true, "Line": true, "SiteAdmin": true, "SuperAdmin": true, "User": true, "LiraAdmin": true, "dest": "reactV04", "childWidth": "75vw" },
{ "_id": "1200_100", "enable": true, "seq": NumberInt(1), "level": NumberInt(1), "label": "Reports", "cat": "SideBar", "visible": true, "parentid": "1200", "icon": "fa/FaHeading", "typ": "individual", "act": true, "Hod": true, "Line": true, "SiteAdmin": true, "SuperAdmin": true, "User": true, "LiraAdmin": true, "dest": "reactV04", "colSize": 8.0, "style": { "marginTop": "1rem", "marginLeft": "20" } },
{ "_id": "1200_100_100", "enable": true, "seq": NumberInt(1), "level": NumberInt(2), "label": "Inspection Report", "cat": "SideBar", "visible": true, "link": "/dp?op=qy&dictName=InspectionResultQuery", "parentid": "1200_100", "icon": "bi/BiInfoCircle", "typ": "individual", "act": true, "Hod": true, "Line": false, "SiteAdmin": true, "SuperAdmin": true, "User": true, "LiraAdmin": true, "dest": "reactV04", "style": { "marginTop": "1rem", "marginLeft": "20" } },
{ "_id": "1200_200", "enable": true, "seq": NumberInt(2), "level": NumberInt(1), "label": "Entry Forms", "cat": "SideBar", "visible": true, "parentid": "1200", "icon": "fa/FaBoxes", "typ": "individual", "act": true, "Hod": true, "Line": true, "SiteAdmin": true, "SuperAdmin": true, "User": true, "LiraAdmin": true, "dest": "reactV04", "colSize": 8.0, "style": { "marginTop": "1rem", "marginLeft": "20" } },
{ "_id": "1200_200_100", "enable": true, "seq": NumberInt(1), "level": NumberInt(2), "label": "Defect Entry", "cat": "SideBar", "visible": true, "link": "/dp?op=sn&dictName=DefectEntry&type=N", "parentid": "1200_200", "icon": "bi/BiListOl", "typ": "individual", "act": true, "Hod": true, "Line": true, "SiteAdmin": true, "SuperAdmin": true, "User": true, "LiraAdmin": true, "dest": "reactV04", "style": { "marginTop": "1rem", "marginLeft": "20" } }
]
```
