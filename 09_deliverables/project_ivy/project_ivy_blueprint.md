# Project Ivy - Project Blueprint

Successor to ClaudeMES (ClaudeMes1). Source state: model version 3.0, 19 Oct 2026, last decision D083, last assumption A028.
Authority: this file replaces the conversation history of ClaudeMES. Where it differs from the old project instructions, this file applies.

---

## 1. Core context and objectives

| Item | Value |
|---|---|
| Product | MES application on MongoDB, designed as data model + generated specifications, validators, indexes, sample data and UI configurations |
| Standards basis | ISA-95 / IEC 62264, IATF 16949, APQP, PPAP, FMEA, SPC, MSA; pharma extension: 21 CFR 210/211/Part 11, EU GMP Annex 11/15/16/19, ICH Q9/Q10, PIC/S PI 041, GAMP 5 (2nd ed.), FDA CSA, India Schedule M |
| Role of Claude | Senior MES solution architect and MongoDB data modeller (20 years automotive) |
| Universe "Auto" | Front Brake Caliper Assembly LH; Varuna Brake Systems Pvt. Ltd. (fictional), Chakan Plant, Pune (site PN1); OEM Sahyadri Motors Ltd. (fictional) |
| Auto process | Gravity die casting -> T6 heat treatment -> CNC machining -> washing -> anodising -> piston and seal assembly -> bleed screw torque -> pressure leak test -> laser marking (serial / 2D code) -> final inspection -> packing -> dispatch |
| Universe "Gamp" | Paracetamol Tablets IP 500 mg, film-coated OSD; Indrayani Pharmaceuticals Ltd. (fictional), Ranjangaon OSD Plant, Pune (site RJ1); process table in `pharma_universe.py` (dispensing -> granulation -> drying -> ... -> serialisation -> cartoning) |
| Key `app` | Every document: `Auto`, `Gamp` or `Common` (reference data shared by both) |
| Model size | 372 collections (203 entity, 85 child, 76 relationship, 8 value-list), 8,703 keys, 12 modules |
| Data types by use | Master 189, Transaction 162, Reports 12, Telemetry 5, Audit Trail 4 |
| Sample data | 5,420 documents: 10 per collection, 20 in collections holding both universes |
| UI configurations | 372 query page configs (1,337 controls), 372 IvyConfigs, 372 Stable table configs, 150 dynamic-dropdown registry docs, menu 436 docs |
| Integration | Unified Namespace on Azure IoT Hub only (no third-party broker); ISA-95 topic tree `VBS/PN1/<area>/<line>/<workCenter>/<equipment>` |
| Folders | Project root (Git) + skills library `E:\Ivy\Claude\ClaudeSkills` (UI skills in `MintSkills\UiSkills`) |

Objectives of Project Ivy:
1. Keep the model, generator and UI pipeline running with low token use.
2. Add new modules / requirement sets on the same pattern (section 5).
3. Close the open items (section 3.9).

---

## 2. Master rulebook

### 2.1 Working rules
- One owner. No draft / review / superseded stages. All actions approved by default; Claude proceeds and records choices.
- Ask only when the answer blocks dependent work. Otherwise decide, record in `decision_log.md` (decision) or `assumptions_log.md` (assumption).
- No shortening, summarising or placeholders ("...", "similar to above") in specifications, data or documents Claude writes. Reading through summaries / generator digests is allowed.
- State every assumption.
- One task = one phase or work package = one goal. New task when the goal is done, the subject changes, or the conversation gets long.
- Edit files on the connected computer in place with short `device_bash` scripts. Never read a large file to change one line. Verify container-to-computer copies with `md5sum`.
- Never hand-edit generated files. Change `05_generator` sources and regenerate (D019).
- Files are overwritten in place; history is in Git. No version suffixes.
- `99_Archive` and `100_Self_Notes` are not authority. Claude never writes to `100_Self_Notes`.
- No frontend, backend, cloud or deployment technology is implied by model documents (exception: UNS fixed to Azure IoT Hub, D082).

### 2.2 Order of authority
1. `project_working_rules.md`, `data_modeling_standard.md`, `mongodb_output_rules.md`, this blueprint
2. `data_model_register.md`, `decision_log.md`
3. `02_architecture` documents, `05_generator/model/flat_model.json`
4. `03_design` specifications
5. Everything else

### 2.3 Collection naming
- `u_mes_<moduleCode>_<singularCollectionName>`, collection part lower camelCase singular (`workOrder`). (Replaces "snake_case plural" of the original brief.)
- Module codes (3-5 letters, owner-fixed): `mast` MasterDataManagement, `prod` ProductDefinition, `plan` PlanningAndExecution, `matl` MaterialManagement, `trac` Traceability, `qual` QualityManagement, `perf` PerformanceManagement, `maint` ToolingAndMaintenance, `syst` SystemAndIntegration, `ehs` EnvironmentHealthAndSafety, `bmr` BatchManufacturingRecord, `mmr` MasterManufacturingRecord.
- Module names PascalCase, no spaces, no `&` (write `And`).
- Menu short labels: Master Data, Product, Plan, Mtl Mgt, Trace, Quality, Performance, Maint, System, EHS, BMR, MMR.
- Andon -> `plan`; energy -> `perf`. Spelling `workCenter`, `centerLine`.
- One business concept = one collection. No vague names.

### 2.4 Document structure (DATA-001 flat)
- No embedded documents, no arrays, anywhere.
- Repeats go to separate collections:
  - Child: repeating lines with attributes -> parent ref pair + `lineNo` + line keys (`u_mes_prod_routingStep`).
  - Relationship: many-to-many -> parent ref pair + `sequenceNo` + one ref pair (`u_mes_mast_workCenterEquipment`).
  - Value list: several plain values -> parent ref pair + `sequenceNo` + one value key.
- No keys ending `Ids` / `Names`. One key = one value = one purpose.
- Every key present in every document; `null` when unavailable. "Required" = may not be null.
- Key order: `_id`, `recordNo`, `app`, `siteId`, `siteName`, specific keys, `status`, `schemaVersion`, audit keys.

### 2.5 Keys and identifiers
- Keys lower camelCase, singular, established terms, one name per concept across the model (no `recordNo` / `recordNumber` mix).
- `_id`: String, exactly 16 digits = 4-digit collection number + 12-digit running number (`1090000000000003`). Never ObjectId / UUID / external ID.
- `recordNo`: business identifier in every collection; children/relationships use `<parent recordNo>-<TAG><nnn>`.
- New collections numbered after the last (last = 1372); existing numbers and `_id`s never change (D042).
- External IDs in own keys (`erpOrderNo`). Message IDs end in `Uuid`, not `Id` (generators read `...Id` as a reference).

### 2.6 References
- Pair `<entity>Id` + `<entity>Name`; stem singular, full entity name (`unitOfMeasureId`).
- `<entity>Name` = target's `name`, else `title`, else `description`, else `recordNo`; child/relationship targets use `recordNo`.
- Role prefix allowed: `fromStorageLocationId` + `fromStorageLocationName`.
- User actions: `<action>ById` + `<action>By`.
- Polymorphic: `relatedCollectionName` + `relatedEntityId` + `relatedEntityName`.
- `siteId` + `siteName` everywhere except `u_mes_mast_site`.
- Same entity -> identical display value everywhere. Every reference points to an existing `_id`.

### 2.7 Status
- `status` only where a lifecycle exists. Title Case with spaces (`In Progress`). One spelling.
- Values in `04_reference_data/code_lists/status_values.md`; data in `u_mes_syst_statusDefinition`, moves in `u_mes_syst_statusTransition`, role authorisation in `u_mes_syst_statusTransitionRole`.
- Secondary states keep own keys (`qualityStatus`, `stockStatus`, `cleanStatus`, `qualificationStatus`).

### 2.8 Classification values (DATA-003)
- Rule A, master collection: plant can add/rename/retire values -> own master (`_id`, `recordNo`, `name`, `description`, `sequenceNo`, `status`), referenced by ID pair.
- Rule B, fixed enumeration: software branches on the value -> coded text, values in validator, `enumeration_values.md` and `u_mes_syst_enumerationValue`.
- Free text only for names, descriptions, notes, third-party numbers, technical addresses.

### 2.9 Dates (DATA-004)
- BSON Date only, never strings.
- Stored as local plant time (IST) with `+0000`, no UTC conversion. 06:00 IST -> `T06:00:00.000+0000`. (Replaces "IST stored as UTC".) `T18:30:00` for local midnight is an error.
- Each date key tagged: Date (calendar, `00:00:00`, name ends `Date` or `validFrom/validTo/effectiveFrom/effectiveTo/horizonFrom/horizonTo`) or Datetime (moment, ends `At`). Tag decides format, not the name (`nextDueAt`, `expiryAt`, `masterLeakVerifiedAt` are Date-tagged).
- `validTo` / `effectiveTo` = last valid day.

### 2.10 BSON types (DATA-002)
| Type | Use |
|---|---|
| Int32 | counts, pieces, line/step numbers, durations min/s, versions, `schemaVersion` |
| Int64 | lifetime counters, number ranges, file sizes |
| Decimal128 | measurements, tolerances, fractional quantities, percentages, money |
| Double | only `geoLatitude`, `geoLongitude`, `tagValue`, `powerFactor` |
| String / Boolean / Date | text, IDs, statuses / flags / all dates |
| null | only when genuinely unavailable |
- One key name = one BSON type model-wide (D044). Only exception: `quantity` (Int32 countable, Decimal128 material). Clash -> more specific name (`severityClass`, `targetWeight`).

### 2.11 Audit keys
- `createdAt, createdById, createdBy, updatedAt, updatedById, updatedBy` on Transaction collections only. Masters: history in `u_mes_syst_auditTrail`. Children inherit parent's class.
- `schemaVersion` (Int32) in every collection.

### 2.12 Enforcement pattern (standard section 12)
- Every enforced rule = configuration master + transaction evidence record.
- Interlock `u_mes_syst_interlockRule` -> `u_mes_plan_interlockEvent`; escalation `escalationRule` + `escalationRuleLevel`; alerts `alertRule` -> `notification`.
- Override = reason code (`u_mes_perf_reasonCode`, Interlock Override) + `overrideById/By` + time + e-signature if required.
- Station evidence: `operatorSession`, `documentAcknowledgement`, `recipeDownload`, `setupVerification` + item.
- Curves: `u_mes_qual_measurementCurve` + time-series `measurementCurvePoint` (timeField `sampledAt`, metaField `measurementCurveId`).
- AI/ML: `u_mes_syst_analyticsModel` + `modelPrediction` (+ `simulationStudy`); no algorithm-specific collections.
- Edit / lock / retention: `u_mes_syst_recordPolicy`. Transaction data never physically deleted.
- Target maturity: Level 3 (system-enforced) with Level 4 data links; Level 5 via analytics registry.

### 2.13 Output formats
| Type | Shell (`.js`) | Extended JSON v2 | Validator `bsonType` |
|---|---|---|---|
| Date | `ISODate("2026-09-15T06:00:00.000+0000")` | `$date` | `date` |
| Int32 | `NumberInt(240)` | `$numberInt` | `int` |
| Int64 | `NumberLong("1250000")` | `$numberLong` | `long` |
| Double | `Double(18.5204)`, also whole numbers | `$numberDouble` | `double` |
| Decimal128 | plain number, decimals exact, no constructor, no quotes (`14.20`) | `$numberDecimal` | `decimal` |
| Boolean / String / null | `true` / `"In Progress"` / `null` | native | `bool` / `string` / `null` |
- Constructors never in quotes. A bare number in a shell file always means Decimal128.
- BSON seed: one `<collection>.bson` per collection (mongodump format), `06_seed_data/bson`.
- Validators: all keys `required`, `additionalProperties: false`, null only where allowed. Time-series collections cannot carry validators (file = application rule).

### 2.14 Sample data
- Exactly 10 documents per collection per universe, one `insertMany` per file, `03_design/<module>/samples/<collection>.js`.
- Same keys, order and types as the specification; flat.
- One universe: an ID always has the same display value; every reference exists; registry `04_reference_data/sample_data_registry.md`.
- Period April-September 2026; shop-floor events in production fortnight Tue 15 - Sat 26 Sep 2026; Mon 14 Sep holiday (Ganesh Chaturthi), Sun 20 Sep weekly off.
- Shifts A 06:00-14:00, B 14:00-22:00, C 22:00-06:00, G (general). `shiftId` in transactions holds the shift code.
- Future dates (retention, next review) within 2027 (sample check accepts 2018-2027).
- Representative engineering values, e.g. bleed screw torque 14 +/- 2 N.m, leak limit 50 Pa at 140 bar, T6 at 535 degC, bore 54.000-54.046 mm.
- A missing spec field is reported as "Schema Observation", never added to documents.

### 2.15 Indexes (default, D020 + strategy)
- Unique (`siteId`, `recordNo`); (`siteId`, `status`); up to five reference keys; (`siteId`, main date -1) on transactions; (parent, `lineNo`) on children; both directions on relationships.
- Unique partial index on `siteId` + `sourceMessageUuid` (`$type: "string"`), plain index on time-series collections.
- Tuning by `QueryKeySelectionStrategy.md`: access patterns -> gates -> nullable keys -> ESR compound -> consolidate -> budget per volume tier.

### 2.16 Token rules
- Start-up reads only the handover note + what the task type needs (section 3.1); `grep -n` everything else.
- `log_decision.py next` instead of reading the decision log.
- Use generator digests (`gen_query.py --digest/--propose`, `gen_stable.py --dry-run`) instead of field lists.
- Skills installed as pointers to library files; a rule change = library edit, no review card.
- Keep large generated files out of project knowledge; read them from the folder with `grep`.

---

## 3. Skills and workflows

### 3.1 Task start (every task)
1. Confirm project root connected; else request root-folder access and wait.
2. Read `00_governance/session_handover.md`; continue its open items.
3. Read by task type:

| Task type | Read | Do not read in full |
|---|---|---|
| UI configs | skill core named in brief, `ui_project_profile.md`, generator digests | field lists, collection keys, specs, register, standard |
| Model / sample change | `data_modeling_standard.md`, `mongodb_output_rules.md`, register sections touched, generator sources touched, `assumptions_log.md` | other modules' field lists and specs |
| Governance / skill change | files changed (`grep -n`) + `skill-library-sync` | anything else |
| New requirement set / module | this blueprint section 5, standard, register header, last `ext_req01`-style file as pattern | existing impact analyses (grep only) |

4. `python3 05_generator/log_decision.py next`.
5. First reply, a few lines: documents read, collection + key count, last decision number, plan.

### 3.2 Task end (every task)
1. Save changed files to their `Folder_Guide.md` location (and to project knowledge only if on the knowledge list, section 6).
2. Regenerate and hand over `data_model_register.md` if the model changed; otherwise say "model unchanged".
3. Run checks: `schema_review_checklist.md`, `flatten_model.py` type check, `gen_specs`, `gen_samples` (integrity + timeline), `gen_query --check`, `gen_stable --check`, menu validator. Record results.
4. `python3 05_generator/log_decision.py handover <file>`: date, task, completed, files changed, counts, last decision, checks, open items, next task.
5. End with the next task brief (template 4.9).

### 3.3 Model regeneration pipeline
```
cd 05_generator
python flatten_model.py          # catalogue.py + keys.py + master_refs.py + ext_req01.py -> model/flat_model.json; type-clash report
python gen_docs.py ..            # register, inventory, collection_keys, field_lists, type matrix, status_values, enumeration_values
python gen_specs.py ..           # specs (.md), validators (.json), indexes (.js), samples; findings report
python gen_samples.py ..         # 10 docs/collection/universe, sample_data_registry.md, sample_data_validation.md
python3 gen_query.py <module>|--check|--cropdown|--digest <m>|--propose <m>|--compare <m>
python3 gen_stable.py [--dry-run|--check]
python3 gen_menu.py              # menu.json + validator
```
Target: 0 problems / 0 findings in every step.

### 3.4 Generator source map
| Change | Edit |
|---|---|
| Original concepts (Phase 1) | `catalogue.py` (C), `keys.py` (K) |
| Master collections / DATA-003 conversions | `master_refs.py` |
| Text key examples, allowed values, descriptions | `keydict_text.py` |
| Numeric examples | `keydict_num.py` |
| Entity sample text, overrides | `entity_samples.py` |
| Shared spec/sample rules | `spec_rules.py` |
| Requirement sets (new collections, added keys, enum additions) | `ext_req01.py` (hub), `gmp01.py`, `uns01.py` |
| Their sample rules | `ext_req01_samples.py`, `gmp01_samples.py`, `uns01_samples.py`, merged by `sample_rules.py` |
| Auto universe | `sample_universe.py` (PROC, MASTER, TITLES, KEYPOOL), `sample_rules.py` |
| Gamp universe | `pharma_universe.py` (PROC, DUAL, GMPONLY, COMMONAPP), `pharma_rules*.py`, switch `pharma_profile.py` |
| Query screens | `query_screens.py` (SCREENS) |
| Decisions / handover | `log_decision.py` |

### 3.5 Requirement-set intake (external questionnaire, regulation, design)
1. Read the source workbook/document; build requirement catalogue (ID, source, requirement).
2. Map source terms to the reference universe (mapping table; e.g. switch -> caliper, batch -> production order + lot).
3. Classify each: C covered / P partly (add keys or values) / G gap (new collection) / O outside MES.
4. Apply DATA-001..004, section 12 enforcement pattern, type uniqueness, BMR/MMR uniqueness rule.
5. Write `01_research/<SET>_impact_analysis.md` (template 4.7). Stop for owner review if large.
6. Implement in `05_generator/<tag>.py` (+ `<tag>_samples.py`), merged through `ext_req01.py` (`NEW += ...`, `ADD += ...`, `ENUM_ADD.update`).
7. Number collections after the last; regenerate (3.3); fix to 0 findings.
8. Log decisions (D###) and assumptions (A###); update `Folder_Guide.md` section 3; handover.

### 3.6 UI configuration (skills)
| Output | Skill | Generator | Location |
|---|---|---|---|
| Query page config + IvyConfig + `/dd` registry | `mes-query-control` (0.22) + `mes-ivy-config` | `gen_query.py` | `04_reference_data/ui_controls/query/PageConfigs`, `IvyConfig`, `u_int_dynamicDropdown.json` |
| Table page config (Stable) | `mes-stable-table` (0.10) | `gen_stable.py` | `ui_controls/table/PageConfigs` |
| Sidebar menu (`_id` 1010 / 1010_100 / 1010_100_100) | `mes-menu-builder` | `gen_menu.py` | `ui_controls/menu/menu.json` |
| Skill rule change | `skill-library-sync` | - | `E:\Ivy\Claude\ClaudeSkills` |

Fixed UI rules: every collection (incl. child / relationship / value-list) has a list screen; Stable only if a query screen exists; `colSize` 12, `labelColSpan` 24; `queryLayout: "singleLine"`; child screens start with parent search dropdown; Stable footer `{ "background-color": "#6F7786", "multiCol": [] }`.
Control source: masters <= 200 docs -> `/mdict` (`u_int_mdict`); larger or growing -> `/dd` search (`dn: "<collection>__id_<displayKey>"`); status / enums -> hard-coded `data`; shift -> `/cropdown` `Shift`.
Workflow: `gen_query.py --digest <m>` -> `--propose <m>` -> review -> record in `query_screens.py` -> generate -> `--check`.

### 3.7 Decision and assumption logging
- `python3 05_generator/log_decision.py add "<decision>" "<reason>" "<source>"`; `check` for duplicates.
- Assumptions: next A### row in `assumptions_log.md` (No, Date, Assumption, Impact if wrong).

### 3.8 Folder access and file delivery
- Work via `device_bash` in the connected root. Container only for steps the shell cannot do (PDF building, viewing images); commit back and verify `md5sum`.
- Deletion needs owner permission; otherwise move to `_to_delete/`.

### 3.9 Open items carried into Project Ivy
1. UNS sample findings F1-F11, F13 (device-connector shift, device models, IP/MAC, certificate expiry, tag addresses, connector targets, `shiftId` code vs `_id` (D080), event timing, energy equipment, marking station, OEE calc time, RJ1 line areas).
2. Commissioning data M2, M3, M5 (UNS-PN1 connector, six IoT Edge gateways, config entries).
3. 24 query configs without `query_screens.py` entries (21 maint, perf alarm, downtimeEvent, workCenterPerformance).
4. UNS design open questions Q1, Q3-Q7.
5. `load_cropdown_configs` in `load_mongodb.py`; F6 required date keys; F5; F1 index alignment; loader root.
6. Renumber second D069; slim cores of `mes-stable-table`, `mes-menu-builder`.
7. Not yet produced: BSON / Extended JSON seed files (complete set), ERD (Mermaid), data flows, `07_database_scripts` (create_indexes, validators, time-series, restore).
8. Annex 11 (2025 draft) / Annex 22 (AI) final status check.
9. Document the Auto / Gamp universe rule (`app` key, DUAL / GMPONLY / COMMONAPP) in `data_modeling_standard.md` - currently only in code. Rename Date-tagged `...At` keys to `...Date` (D035 candidates).
10. Git commits in project root and ClaudeSkills.

---

## 4. Essential templates

### 4.1 New collection (requirement-set file, `NEW` entry)
```python
SRC = '<SET_NAME>'      # e.g. 'MES_ExternalRequirement_02'
TAG = '<tag>'           # e.g. 'ext02'
def _c(**kw):
    kw.setdefault('src', SRC); kw.setdefault('tag', TAG); return kw

NEW = [
 _c(no=1373, entity='<camelCaseSingular>', prefix='<ABC>', volume='about 500 per year', storage='standard collection',
  module='<moduleCode>', kind='entity',            # entity | child | relationship | value-list
  type='Transaction',                              # Master | Transaction | Reports | Telemetry | Audit Trail
  label='<Screen Label Plural>',
  purpose='<What the collection holds>',
  why='<Embed vs reference / why separate collection>',
  bk='<recordNo format, e.g. ABC-2026-000001>', status=['Open', 'In Progress', 'Closed'], q='<requirement IDs>',
  idx='unique `recordNo`; (`<refKey>Id`, `status`)',
  fields=[
   # ('PARENT', '<parentKeyStem>', '<parentEntity>'),   # child / relationship / value-list only, first line
   ('name', 'String', False, None, '<description>'),
   ('<target>Id', 'String', False, '<targetEntity>', '<description>'),    # expanded to Id + Name
   ('approvedById', 'String', True, 'user', '<description>'),             # expanded to ById + By
   ('<measure>', 'Decimal128', False, None, '<description, unit>'),
   ('<count>', 'Int32', False, None, '<description>'),
   ('<event>At', 'Date', False, None, '<Datetime>'),
   ('<due>Date', 'Date', True, None, '<Date>'),
   ('<flag>', 'Boolean', False, None, '<description>'),
  ],
  enums={'<enumKey>': ['<Value A>', '<Value B>']}),
]
```
Standard keys (`_id`, `recordNo`, `app`, `siteId/Name`, `status`, `schemaVersion`, audit keys by type) are added by `apply()`.

### 4.2 Added keys and enumeration values
```python
ADD = [
 # (entity, key, BSON type, null allowed, referenced entity or None, enum list or None, description)
 ("<existingEntity>", "<newKey>", "String", True, None, None, "<description>"),
]
ENUM_ADD = {
 ("<existingEntity>", "<enumKey>"): ["<New Value>"],
}
```
Merge in `ext_req01.py`: `import <tag> as _X; NEW += _X.NEW; ADD += _X.ADD; ENUM_ADD.update(...)` (as for `_GMP`, `_UNS`).

### 4.3 Sample rules file (`<tag>_samples.py`)
```python
"""Sample-data rules for <SET>. Merged into sample_rules.py by apply(), after uns01_samples.
Index conventions: <equipment 0-9 order>. Users: <index -> person>. Story: <events tied to the fortnight>."""
import datetime
def DT(m, d, h=0, mi=0, s=0, y=2026): return datetime.datetime(y, m, d, h, mi, s)   # local plant time, no conversion
MASTER_ADD = {"<entity>": """<CODE-01>|<Name 1>
<CODE-02>|<Name 2>"""}          # 10 lines
TITLES_ADD = {}
RECFMT    = {"<entity>": "<PFX>-2026-%06d"}
STATUSOF  = {"<entity>": ["Closed"]*6 + ["In Progress"]*3 + ["Open"]}
# also available: VAL, REFIDX, PARENTIDX, CTXOF, POST, NULLWHEN, GEN, BOOLRULE, ENUMRULE
def apply(S): ...               # merge dicts into sample_rules
```

### 4.4 Flat document (transaction)
```javascript
db.getCollection("u_mes_perf_leakTestResult").insertMany([
  {
    _id: "1214000000000001",
    recordNo: "LKT-2026-000377",
    app: "Auto",
    siteId: "1003000000000001",
    siteName: "Chakan Plant, Pune",
    wipUnitId: "1094000000000005",
    wipUnitName: "U260918B0236",
    equipmentId: "1013000000000008",
    equipmentName: "Pressure Leak Tester 1",
    operatorUserId: "1029000000000003",
    operatorUserName: "Deepak Gaikwad",
    attemptNo: NumberInt(1),
    partTemperatureC: 28.1,
    masterLeakVerifiedAt: ISODate("2026-04-02T00:00:00.000+0000"),
    verdict: "Fail",
    testedAt: ISODate("2026-09-18T15:11:33.000+0000"),
    sourceMessageUuid: "a3354e57-ef7d-5d57-ae79-712cbc4cff69",
    status: "Recorded",
    schemaVersion: NumberInt(1),
    createdAt: ISODate("2026-09-18T15:11:03.000+0000"),
    createdById: "1029000000000010",
    createdBy: "MES System",
    updatedAt: ISODate("2026-09-18T15:11:33.000+0000"),
    updatedById: "1029000000000010",
    updatedBy: "MES System"
  }
]);
```
Master: same without audit keys. Child: after `siteName` -> `<parent>Id`, `<parent>Name`, `lineNo`. Relationship / value list: parent pair, `sequenceNo`, one ref pair / one value.

### 4.5 Validator
```json
{
  "collMod": "<collection>",
  "validator": { "$jsonSchema": {
    "bsonType": "object", "title": "<collection>",
    "required": ["_id", "recordNo", "app", "siteId", "siteName", "<every key>", "status", "schemaVersion"],
    "additionalProperties": false,
    "properties": {
      "_id": { "bsonType": "string", "description": "Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database" },
      "<ref>Id": { "bsonType": ["string", "null"], "description": "Reference to <target collection>._id: <meaning>" },
      "<ref>Name": { "bsonType": ["string", "null"], "description": "Display value of <ref>Id, copied from <target collection>.<display key>" },
      "<measure>": { "bsonType": "decimal", "description": "<meaning, unit>" },
      "status": { "bsonType": "string", "enum": ["<Value>", "<Value>"], "description": "Lifecycle state" }
    } } },
  "validationLevel": "strict", "validationAction": "error"
}
```

### 4.6 Indexes
```javascript
db.getCollection("<c>").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("<c>").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("<c>").createIndex({ <ref>Id: 1 }, { name: "ix_<ref>Id" });
db.getCollection("<c>").createIndex({ siteId: 1, <mainDate>: -1 }, { name: "ix_siteId_<mainDate>" });
db.getCollection("<c>").createIndex({ siteId: 1, sourceMessageUuid: 1 },
  { name: "ux_siteId_sourceMessageUuid", unique: true, partialFilterExpression: { sourceMessageUuid: { $type: "string" } } });
// time-series
db.createCollection("<c>", { timeseries: { timeField: "sampledAt", metaField: "<parent>Id", granularity: "seconds" } });
```

### 4.7 Impact analysis skeleton (`01_research/<SET>_impact_analysis.md`)
```
# <SET> - <title>: impact analysis and implementation
Date | Task | Owner decision | Decisions D### | Assumptions A###
## 1. Purpose and scope            (generic MES capability, mapped to reference universe)
## 2. Sources                      (Ref | Source | Status used)
## 3. Mapping to the reference      (Source concept | Model collection / sample)
## 4. Requirement catalogue         (No | Source | Requirement | C/P/G/O | Resolution) per domain + summary
## 5. New collections (numbers nnnn-nnnn)
## 6. Keys added to existing collections
## 7. Allowed values added
## 8. Enforcement                   (Rule | Configuration | Evidence)
## 9. Sample data                   (story tied to the production fortnight)
## 10. Owner decision and implementation notes
## 11. Checks                       (generator results, 0 findings)
```

### 4.8 Decision / assumption rows
```
| D084 | 20 Oct 2026 | <decision> | <reason> | Owner / Claude |
| A029 | 20 Oct 2026 | <assumption> | <impact if wrong> |
```

### 4.9 Task brief
```
Task: <phase or work package>. Goal: <one outcome>. Inputs: <exact file names>.
Must not change: <files / numbers / conventions>.
Connect E:\Ivy\Claude\ClaudeProjects\ProjectIvy (and E:\Ivy\Claude\ClaudeSkills for UI work).
Follow section 3.1 of project_ivy_blueprint.md.
```

### 4.10 Handover note
```
# Session handover note
- Date:
- Task:
- Completed:
- Files changed:
- Counts: <n> collections (<entity/child/relationship/value-list>), <n> keys, <n> sample documents; UI <n>/<n>/<n>
- Last decision number: D###. Last assumption: A###.
- Checks run: <generator> <result>
- Open items:
- Recommended next task brief: "<4.9>"
```

### 4.11 Project Ivy instructions (paste into project settings)
```
ROLE: Senior MES solution architect and MongoDB data modeller, 20 years automotive (IATF 16949, ISA-95, APQP, PPAP, FMEA, SPC, MSA) and GMP / GAMP 5 computerised systems.
PROJECT: Project Ivy - MES on MongoDB. Successor of ClaudeMES (model 3.0).
AUTHORITY: project_ivy_blueprint.md, then 00_governance files in the folder E:\Ivy\Claude\ClaudeProjects\ProjectIvy.
CONVENTIONS: u_mes_<module>_<singularCamelCase>; flat documents; 16-digit string _id; recordNo; <entity>Id + <entity>Name;
IST stored with +0000 (no UTC conversion); Decimal128 for measures and money; audit keys on transactions only; 10 samples per collection.
WORK: no placeholders or shortening in outputs; state assumptions; read session_handover.md first; change generator sources, never generated files;
end every task with checks, register update (if model changed), handover note and next brief.
```

---

## 5. MES and GAMP knowledge base for collection design

### 5.1 Module boundaries (ISA-95 Level 3 functions)
| Code | Scope | Typical collections |
|---|---|---|
| mast | ISA-95 hierarchy (enterprise, site, area, line, work center, equipment), calendars, shifts, people, roles, skills, partners, UoM, classification masters | site, line, workCenter, equipment, shift, user, role, skill, customer, supplier, department |
| prod | Product definition: item, variant, BOM, operation, routing, bill of process, work instruction, recipe, engineering change, packaging | item, billOfMaterial, routing, routingStep, recipe, workInstruction |
| plan | Demand-to-execution: schedules, orders, dispatch, execution, WIP, lots, containers, labour, changeover, andon, interlocks, line clearance, yield | productionOrder, operationExecution, wipUnit, lot, andonEvent, interlockEvent |
| matl | Receipts, storage, stock, movements, kitting, consumption, dispensing, exposure timers, replenishment | goodsReceipt, inventoryBalance, materialMovement, dispenseRecord |
| trac | Serials, genealogy, as-built, trace investigations, recalls (reports) | serialNumber, genealogyLink, asBuiltRecord, traceInvestigation |
| qual | Characteristics, control/inspection/sampling plans, SPC, results, NC, CAPA, holds, deviations, PPAP, gauges / MSA, audits, risk, complaints | characteristic, controlPlan, inspectionResult, nonconformance, capa, gauge |
| perf | Process data, equipment states, downtime, OEE, alarms, test results, energy | equipmentState, downtimeEvent, processReading (TS), torqueResult, leakTestResult, energyReading (TS) |
| maint | Tools, dies, maintenance plans/work orders, spares, cleaning, logbooks, equipment qualification | tool, maintenanceWorkOrder, cleaningRecord, equipmentQualification |
| syst | Integration (ERP, IoT, UNS), configuration, number ranges, status/enum tables, audit trail, e-signature, computerised-system governance, rules, analytics | integrationConnector, iotDevice, auditTrail, electronicSignature, interlockRule, computerisedSystem |
| ehs | Safety incidents, environment and health records | safetyIncident |
| bmr | Unique to the executed batch record: header, review by exception, exceptions, release, yield reconciliation | batchManufacturingRecord, batchRecordReview, batchRelease |
| mmr | Unique to the master record: versioned MMR per item revision + recipe links | masterManufacturingRecord |

Uniqueness rule (bmr / mmr): a collection moves there only if no other MES function writes it or depends on it; shared collections stay functional (55 shared with BMR, 63 with MMR - `BMR_MMR_module_designation.md` section 6).

### 5.2 Collection design decision tree
1. Is it a business concept not yet held? (C2) -> else extend existing collection with keys.
2. Single value per parent? -> key on parent. Repeating lines with attributes -> Child. Many-to-many -> Relationship. Repeated plain values -> Value list.
3. Data class: plant-maintained reference -> Master (no audit keys); created by daily operations -> Transaction; pre-aggregated -> Reports; machine time-ordered signals -> Telemetry (time-series, no validator); append-only who-did-what -> Audit Trail.
4. Unbounded data (results, events, readings, curve points, messages) -> own collection, never on the parent. High-rate signals -> time-series (`timeField` + `metaField`).
5. Classification key -> DATA-003 rule A or B.
6. Lifecycle -> `status` values + transitions + role authorisation; requiresReason / requiresSignature where regulated.
7. Enforced rule -> configuration + evidence (2.12).
8. External identifier -> own key; UNS / message id -> `...Uuid` + unique partial index.
9. Every key: B1-B9 checklist; every collection: C1-C7.

Embed vs reference (justification line in `why`): flat model forbids embedding, so the justification states which repeat-collection kind was chosen and why (bounded lines -> child; shared master -> reference pair; unbounded -> separate transaction / time-series).

### 5.3 Volume tiers and storage
- T1 small masters (< 1,000): default indexes only.
- T2 transactions (10^4-10^6 / year): access-pattern indexes, ESR compound, archive by `recordPolicy`.
- T3 telemetry (> 10^6 / year): time-series (`processReading`, `energyReading`, `measurementCurvePoint`); no unique index; no validator.
- Basis: 2,400 calipers/day, 300 days, ~720,000 units/year.

### 5.4 Traceability model (Auto)
- Lot tracking from casting to anodising; unit identifier created at piston and seal assembly; customer serial at laser marking.
- Genealogy as parent/child links (`genealogyLink`), as-built per serial with `recipeVersion` + `recipeChecksum`.

### 5.5 GMP / GAMP pattern (GMP_Pharma_01, 55 requirements, collections 1344-1369)
| Requirement area | Collections / keys |
|---|---|
| Computerised system inventory (GxP impact, GAMP 5 category, data criticality, Part 11 scope, owners, review cycle) | `u_mes_syst_computerisedSystem` (master) |
| Risk-based validation (FDA CSA, GAMP 5 2nd ed.) | `u_mes_syst_systemValidation` -> `u_mes_qual_riskAssessment` |
| Periodic review / access review | `systemPeriodicReview`, `userAccessReview` + line |
| Audit trail (who, what, when, old/new, why; hash chain) + review | `auditTrail` + `auditTrailChange` (`gxpRelevant`, `auditTrailReviewId`), `auditTrailReview` |
| Part 11 e-signature (unique, linked, meaning, first signing in session) | `electronicSignature` (`signatureManifestationText`, `signedRecordVersion`, `isFirstSigningInSession`), `signatureMeaning`, `roleSignatureMeaning` |
| Master batch record | `u_mes_mmr_masterManufacturingRecord` (per item revision, refs to BOM, routing, BOP, control / inspection / packaging plans) |
| Executed batch record | `u_mes_bmr_batchManufacturingRecord` (per order; freezes MMR version; links clearance, reconciliation, review, release, true copy) |
| Review by exception / release by quality unit | `bmr_batchRecordReview` + `batchRecordReviewException`, `bmr_batchRelease` (separate from quality hold) |
| Yield, component, label reconciliation | `bmr_yieldReconciliation` (`reconciliationType`) |
| Line clearance (second-person verification) | `u_mes_plan_lineClearance` |
| Dispensing / count-by-weight | `u_mes_matl_dispenseRecord` |
| Cleaning, use logbook, clean hold time | `maint_cleaningRecord`, `maint_logbookEntry` (polymorphic), equipment `cleanStatus` |
| Equipment / process qualification | `maint_equipmentQualification` (`qualificationStatus`), process validation |
| Environmental monitoring, classified areas | EM collections in `qual` / `ehs`, area classification |
| Retention samples, recall, PQR, complaints, CAPA, change control, training, self-inspection | existing `qual` / `trac` collections + keys |
| Deviations | `qual_nonconformance` (`deviationClass`, investigation keys) - no new collection |
| Enforcement | interlock rule types: Line Clearance Check, Batch Release Check, Equipment Clean Status Check, Qualification Status Check, Dispense Tolerance Check; `statusTransition.requiresSignature/Reason`; `recordPolicy.gxpRelevant` |

Pharma-to-Auto mapping (A020): batch = production order + lot; quality unit = quality department; dispensing = ingot charge weighing / seal kitting; classified room = assembly clean area ISO 8; recall = customer containment / field action.

GAMP 5 software categories (key `gampCategory`): 1 infrastructure, 3 non-configured, 4 configured, 5 custom. Assurance effort follows risk (CSA): unscripted / scripted testing by risk.

Sources to cite: 21 CFR 210/211, Part 11; EudraLex Vol 4 Part I ch. 1, 3, 4, 5, 8, 9; Annex 1, 11 (2011 in force; 2025 drafts), 15, 16, 19, 22 (draft AI); ICH Q7, Q9(R1), Q10; PIC/S PI 041-1; Schedule M (revised 2023); FDA CSA (Sep 2025); FDA Process Validation (2011); ISA-88; GAMP 5 2nd ed. Re-check draft status before use.

### 5.6 Automotive quality pattern
- Characteristic -> control plan -> inspection plan / sampling plan -> check sheet -> inspection result -> SPC chart; multi-position via `characteristicPosition`.
- Curves: `curveEnvelope` + `curveEnvelopeWindow` -> `measurementCurve` (verdict) -> TS points.
- NC -> containment / quality hold -> disposition -> rework / scrap -> CAPA (8D); deviation permit; PPAP submission; gauge calibration + MSA.
- Defect codes, downtime reason tree (`reasonCode`, `reasonType`), PFMEA linked to process rows.

### 5.7 Unified Namespace pattern (UNS_01, 1370-1372)
- Azure IoT Hub only; IoT Edge gateways per area; MES publisher identity.
- Topic tree from master data: `VBS/PN1/<area>/<line>/<workCenter>/<equipment>`; namespaces Edge, MES, KPI; message classes State, Event, Measurement.
- `u_mes_syst_unsMessageType` (catalogue, target collection, twin path), `iotHubIdentity`, `unsRejectedMessage`; `sourceMessageUuid` on ingested collections (idempotency); `edgeGatewayIotDeviceId` on `iotDevice`.

### 5.8 Research baseline
- Ten products benchmarked: Siemens Opcenter, Rockwell Plex, GE Proficy, Tulip, Critical Manufacturing, Aegis FactoryLogix, Eyelit, Infor MES, SAP DM, NoMuda VisualFactory (`phase1_research_feature_matrix_catalogue.md`, `module_comparison_matrix.md`).
- Requirement sets already absorbed: MES_ExternalRequirement_01 (Q1-Q129, 44 collections 1300-1343, 212 keys), GMP_Pharma_01 (GMP-01..55, 1344-1369), UNS_01 (1370-1372).

### 5.9 Adding a new module (checklist)
1. Owner fixes module code (3-5 letters), PascalCase name, menu short label, folder `NN_<snake_name>`.
2. Apply uniqueness rule: only collections no other module writes / depends on; shared ones stay.
3. Add code to `MOD_NAMES` / `ORDER_ALL` / `DOMF` in generators; `Folder_Guide.md` section 4; standard section 1.
4. Requirement-set intake (3.5) with `module='<code>'`; collection numbers continue from last.
5. Sample rules per universe (Auto, and Gamp if relevant: add to DUAL / GMPONLY).
6. Regenerate (3.3); UI: `query_screens.py` entries, `gen_query`, `gen_stable`, `gen_menu` (new level-0 menu node).
7. Log decisions; update register; handover.

---

## 6. Migration method (ClaudeMES -> Project Ivy)

### 6.1 Step by step
1. **Freeze ClaudeMES.** Commit the folder to Git (`git add -A && git commit -m "ClaudeMES final, model 3.0, D083"`); tag `claudemes-final`.
2. **Clean the old root** (move to `_to_delete/` or archive, see 6.2).
3. **Create the new root** `E:\Ivy\Claude\ClaudeProjects\ProjectIvy`: copy the cleaned ClaudeMES tree (or `git clone` it, keeping history). Do not start an empty model - Ivy continues model 3.0.
4. **Add this blueprint** as `00_governance/project_ivy_blueprint.md`; update `README.md`, `Folder_Guide.md` (root path), `project_working_rules.md` section 7 (root path, brief template = 4.9), `ui_project_profile.md` (root path).
5. **Consolidate logs:** move `decision_log.md` and `assumptions_log.md` to `99_Archive/2026-10-19_claudemes_logs/`; start new logs with one row "D084 Project Ivy started from ClaudeMES model 3.0; decisions D001-D083 consolidated in the blueprint" and continue numbering (D084+, A029+) so references stay valid. Keep `log_decision.py`.
6. **Run the baseline** in the new root: section 3.3 pipeline; expect 372 collections, 8,703 keys, 0 findings. Record in `08_validation/reports`.
7. **Create the claude.ai project "Project Ivy"**; paste instructions 4.11.
8. **Upload only the knowledge set** (6.3). Everything else is read from the folder with `device_bash` + `grep`.
9. **Skills:** keep `E:\Ivy\Claude\ClaudeSkills` unchanged (account skills are shared across projects); update the root path inside `ui_project_profile.md` only.
10. **First task brief** (example): "Task: UNS sample data corrections. Goal: correct findings F1-F11, F13 in the sample generator and add commissioning data M2, M3; regenerate with 0 findings. Inputs: none. Must not change: collection numbers, _id values. Connect E:\Ivy\Claude\ClaudeProjects\ProjectIvy and E:\Ivy\Claude\ClaudeSkills. Follow section 3.1 of project_ivy_blueprint.md."
11. Keep ClaudeMes1 read-only for reference; delete it only after the first two Ivy tasks succeed.

### 6.2 Folder clean-up (old root)
| Item | Action | Reason |
|---|---|---|
| `_gamp_dump_review.txt` (459 KB) | delete / archive | debug dump |
| `Claude outputs/` | delete | duplicates of governance / research files |
| root `load_mongodb.py` | delete (keep `07_database_scripts/MongoDocUpload/load_mongodb.py`) | duplicate |
| `07_database_scripts/MongoDocUpload.zip` | delete | packaged copy |
| `00_governance/decision_log-1.md` | delete | stale copy (open item) |
| all `__pycache__/` | delete; add to `.gitignore` | build artefacts |
| `_to_delete/` | empty after review | holding folder |
| `01_research/MES_ExternalRequirement_01_impact_analysis.md` (266 KB) | keep in folder, remove from project knowledge | implemented; grep when needed |
| `100_Self_Notes/ClaudeInstructions.md` | keep (owner notes) | not authority |

### 6.3 Folder structure for Project Ivy
```
ProjectIvy/                                  (Git; .gitignore: __pycache__/, *.pyc, _to_delete/)
  README.md  Folder_Guide.md
  00_governance/
    project_ivy_blueprint.md                 NEW - level-1 authority, replaces conversation history
    project_working_rules.md  data_modeling_standard.md  mongodb_output_rules.md  schema_review_checklist.md
    data_model_register.md                   (generated)
    decision_log.md  assumptions_log.md      (restarted at D084 / A029)
    session_handover.md
    decisions/
  01_research/
    requirement_sets/<SET>/                  NEW - workbook + impact analysis per set (ext_req01, gmp01, uns01, ...)
    benchmark/                               phase1 catalogue, module comparison matrix
  02_architecture/  (unchanged; generated + hand)
  03_design/<NN_module>/{specs,validators,indexes,samples}   (generated)
  04_reference_data/{code_lists,product,process_values,timeline,ui_controls}
  05_generator/
    core/        catalogue.py keys.py master_refs.py flatten_model.py spec_rules.py keydict_*.py entity_samples.py
    reqsets/     ext_req01*.py gmp01*.py uns01*.py   (one pair per requirement set)
    universes/   sample_universe.py sample_rules.py pharma_*.py
    builders/    gen_docs.py gen_specs.py gen_samples.py gen_query.py query_screens.py gen_stable.py gen_menu.py
    tools/       log_decision.py
    model/flat_model.json
    run_all.py                               NEW - runs the 3.3 pipeline and prints a 1-line result per step
  06_seed_data/  07_database_scripts/  08_validation/  09_deliverables/  99_Archive/  100_Self_Notes/
```
Note: the `05_generator` sub-folders need import-path changes (`sys.path` in each entry script); do this as its own task with a baseline comparison, or keep the flat folder if not worth the risk.

### 6.4 Project knowledge set (upload to Project Ivy)
| File | Approx. size |
|---|---|
| `project_ivy_blueprint.md` | 30 KB |
| `session_handover.md` | 4 KB |
| `project_working_rules.md` | 9 KB |
| `data_modeling_standard.md` | 14 KB |
| `mongodb_output_rules.md` | 3 KB |
| `schema_review_checklist.md` | 3 KB |
| `Folder_Guide.md` | 10 KB |
| `data_model_register.md` | 58 KB (optional; grep from folder instead) |

About 75-135 KB, against 726 KB today. Do not upload generator sources, impact analyses, collection_keys, sample registry or UI configs; read them from the folder.
