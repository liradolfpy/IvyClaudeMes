# UI project profile - ClaudeMES

Project-specific values for the UI skills `mes-query-control`, `mes-ivy-config`, `mes-stable-table` and `mes-menu-builder` (skills library `E:\Ivy\Claude\ClaudeSkills\MintSkills\UiSkills`). The skills hold the method; this file holds what is particular to ClaudeMES. Created 17 October 2026 from the project-specific sections of `query_control_instruction.md` v0.16 and `menu_skill.md`.

## 1. Project facts

| Item | Value |
|---|---|
| Project root | `E:\Ivy\Claude\ClaudeProjects\ClaudeMES` |
| Application code | `mes`; collections `u_mes_<moduleCode>_<entity>`; MasterDict `u_int_mdict` |
| Model version | 2.9 (369 collections, 8,614 keys including `app`) plus `u_int_mdict`; current counts in `00_governance/data_model_register.md` |
| Module codes, names and menu labels | Module table of `02_architecture/collection_inventory.md` |
| Folder layout | `Folder_Guide.md`; the standard paths named in the skills apply without change |
| Reference samples (owner-maintained) | `04_reference_data/ui_controls/query/FormatQuery.json`, `query/cropdown.md`, `table/FormatTableNewDesign.json` (Stable reference since skill 0.7, 18 Oct 2026; `table/FormatTable.json` is the previous design), `menu/FormatMenu.json.txt` (starting copies in the skill folders' `assets/`) |
| Generators | `05_generator/gen_stable.py` (Stable), `05_generator/gen_menu.py` (Menu); starting copies in the skill folders' `templates/`. `05_generator/gen_query.py` (query page configurations, IvyConfigs and dynamic dropdown registry; screen decisions in its `SCREENS` table, PlanningAndExecution from 17 Oct 2026; `--check` runs the query and IvyConfig checklists on every file, D066) |
| Outputs | `04_reference_data/ui_controls/query/PageConfigs/<collection>.json`, `query/IvyConfig/<collection>Ivy.json`, `query/u_int_dynamicDropdown.json` (dynamic dropdown registry, one combined file), `table/PageConfigs/<collection>.json`, `menu/menu.json` |

## 2. Query

### 2.1 Placement of model collections used in query controls:

| Model collection | Expected documents per site | Source | `params` |
|---|---|---|---|
| Masters listed in section 11.3 | 200 or fewer | `/mdict` | `{ typ: "<dictName>", subTyp: "idame" }` |
| `u_mes_mast_user` (operators, supervisors, any `...ById` or `...UserId` key) | about 600 | `/dd` search | `{ dn: "u_mes_mast_user__id_fullName" }` |
| `u_mes_matl_storageLocation` | more than 200 bins | `/dd` search | `{ dn: "u_mes_matl_storageLocation__id_name" }` |
| `u_mes_maint_tool` | about 300 | `/dd` search | `{ dn: "u_mes_maint_tool__id_name" }` |
| `u_mes_qual_gauge` | about 250 | `/dd` search | `{ dn: "u_mes_qual_gauge__id_name" }` |
| `u_mes_qual_characteristic` | more than 200, grows with each item | `/dd` search | `{ dn: "u_mes_qual_characteristic__id_name" }` |
| `u_mes_maint_sparePart`, `u_mes_perf_processTag` | more than 500 | `/dd` search | `{ dn: "<collection>__id_<display key>" }` (registry document in `u_int_dynamicDropdown`) |
| `u_mes_prod_recipe`, `u_mes_syst_iotDevice`, `u_mes_prod_routing`, `u_mes_qual_controlPlan`, `u_mes_qual_inspectionPlan`, `u_mes_qual_checkSheet`, `u_mes_maint_maintenancePlan` | 500 or fewer, not frequently used as a filter | `/dd` | `{ dn: "<collection>__id_<display key>" }` (registry document in `u_int_dynamicDropdown`) |
| Transaction collections searched by business number or used as a parent: `u_mes_plan_customerSchedule`, `u_mes_plan_productionOrder`, `u_mes_plan_productionSchedule`, `u_mes_plan_dispatchList`, `u_mes_plan_operationExecution`, `u_mes_plan_wipUnit`, `u_mes_plan_lot`, `u_mes_plan_container`, `u_mes_plan_changeover`, `u_mes_plan_shiftHandover`, `u_mes_plan_setupVerification`, `u_mes_perf_downtimeEvent` | grow without limit (T1 / T2) | `/dd` search | `{ dn: "<collection>__id_recordNo" }` |
| `u_mes_plan_andonEvent` (display key `description`), `u_mes_qual_nonconformance` (display key `title`), `u_mes_maint_maintenanceWorkOrder` (display key `title`) | grow without limit | `/dd` search | `{ dn: "<collection>__id_<display key>" }` |
| `u_mes_prod_workInstruction` (`title`), `u_mes_syst_interlockRule`, `u_mes_mast_costCenter`, `u_mes_mast_department`, `u_mes_mast_skill`, `u_mes_mast_manufacturer`, `u_mes_maint_toolType` (`name`) | 500 or fewer, not in `u_int_mdict` | `/dd` | `{ dn: "<collection>__id_<display key>" }` |
| Status of any collection | 3 to 8 values | `data` | values from `status_values.md` |
| Shift | 4 values (A, B, C, G) | `/cropdown` | `{ name: "Shift" }`. The cropdown keys are the shift codes (`A`, `B`, `C`, `G`), and `shiftId` in transaction, report and telemetry collections stores the same code, so the filter is a direct match. The mdict `Shift` dictionary is not used in query controls. |

### 2.2 MasterDict dictionaries (`u_int_mdict`)

Reference counts were taken from `02_architecture/field_lists` (references from non-master collections, `siteId` excluded).

| dictName | Source collection | Display key | References from non-master collections | Expected documents per site |
|---|---|---|---|---|
| Area | `u_mes_mast_area` | name | 3 | 10 |
| Line | `u_mes_mast_line` | name | 18 | 12 |
| WorkCenter | `u_mes_mast_workCenter` | name | 37 | 60 |
| Equipment | `u_mes_mast_equipment` | name | 29 | 150 |
| Shift | `u_mes_mast_shift` | name | 27 | 4 (kept in `u_int_mdict` for other uses; query controls use cropdown `Shift`) |
| Customer | `u_mes_mast_customer` | name | 14 | 15 |
| Supplier | `u_mes_mast_supplier` | name | 4 | 60 |
| Item | `u_mes_prod_item` | description | 52 | 180 (review at go-live; above 200 it moves to `/dd` search) |
| ProductVariant | `u_mes_prod_productVariant` | name | 14 | 20 |
| Operation | `u_mes_prod_operation` | name | 16 | 40 |
| AndonType | `u_mes_plan_andonType` | name | 1 (category of Andon Events) | 6 |
| ContainerType | `u_mes_plan_containerType` | name | 1 (category of Containers) | 15 |
| IndirectActivity | `u_mes_plan_indirectActivity` | name | 1 (category of Labour Bookings) | 15 |
| StockStatus | `u_mes_matl_stockStatus` | name | 3 | 6 |
| MovementType | `u_mes_matl_movementType` | name | 1 (category of Material Movements) | 25 |
| DefectCode | `u_mes_qual_defectCode` | name | 5 | 80 |
| DispositionType | `u_mes_qual_dispositionType` | name | 3 | 6 |
| ComplaintType | `u_mes_qual_complaintType` | name | 1 (category of Customer Complaints) | 8 |
| ReasonCode | `u_mes_perf_reasonCode` | name | 14 | 150 |
| LossCategory | `u_mes_perf_lossCategory` | name | 2 | 8 |
| EnergyType | `u_mes_perf_energyType` | name | 1 (category of Energy Readings) | 5 |
| DocumentType | `u_mes_syst_documentType` | name | 1 (category of Controlled Documents) | 30 |
| NotificationType | `u_mes_syst_notificationType` | name | 1 (category of Notifications) | 15 |
| IncidentType | `u_mes_ehs_incidentType` | name | 1 (category of Safety Incidents) | 8 |

Not given a dictionary:

| Collection | Reason | Source used instead |
|---|---|---|
| `u_mes_mast_user` (518 references) | About 600 documents per site | `/dd` search |
| `u_mes_matl_storageLocation`, `u_mes_maint_tool`, `u_mes_qual_gauge`, `u_mes_qual_characteristic`, `u_mes_maint_sparePart`, `u_mes_perf_processTag` | More than 200 documents, or growing | `/dd` search |
| `u_mes_prod_recipe`, `u_mes_syst_iotDevice`, `u_mes_prod_routing`, `u_mes_qual_controlPlan`, `u_mes_qual_pfmea`, `u_mes_prod_billOfMaterial` and other definition masters | Versioned or rarely used as a filter | `/dd` |
| `u_mes_mast_unitOfMeasure` (20 references) | Displayed only, never a query control | – |
| Value-list masters without transaction references (country, currency, language, item group, defect group and similar) | Not used in query controls of transaction screens | `/dd` on their own admin screen |

### 2.3 Sample file

`04_reference_data/ui_controls/query/u_int_mdict.json`: 43 documents in MongoDB shell style, one per dictionary per site, built from the sample documents in `03_design/<module>/samples`. The sample universe holds two sites: Chakan Plant, Pune (`PN1`, `1003000000000001`) and Ranjangaon OSD Plant, Pune (`RJ1`, `1003000000000011`). Dictionaries whose source has samples for one site only (AndonType, IndirectActivity, EnergyType, NotificationType, IncidentType) exist for that site only. Every `idame` key is an `_id` present in the source sample file.

### 2.4 Open questions and deferred items


None at version 0.10. New questions are added here with the next free number (Q24 onwards).

Q20 resolved on 17 Oct 2026 (skill `mes-query-control` 0.18, section 14): `/dd` reads the registry document `u_int_dynamicDropdown._id = params.dn`, which names `coln`, `key` (`_id`) and `val` (display key).

FormatQuery.json review (17 Oct 2026, skill `mes-query-control` 0.19, decision D065): the owner's reviewed `query/FormatQuery.json` sets the key names `p_data_index`, `data_index_from` / `data_index_to`, `"source" : "dynamic"` and `"sourceParams" : {}` on `/dd` controls, `Please Select <label>`, and search length 4 with placeholder `Type min 4 characters`. Its frame (`typ` PageConfig, `_id` F_1019, `api` /stdtools/phantomzen, extra fields lid, countList, q, resp, origId), its `required: false` on `/dd` and its `multiSelect: true` example are not the rule for MES pages. All 24 page configurations in `query/PageConfigs/` were updated (27 `/dd` controls, 23 search dropdowns); at that point no MES query screen used `multiSelect: true`, and no master or plan screen carried a range picker, so the new `-30` default changed no file. IvyConfigs are unchanged (range entry keeps `dinFrom` / `dinTo`).

PlanningAndExecution (17 Oct 2026, D066, D067): 43 page configurations and IvyConfigs generated by `05_generator/gen_query.py`; 18 registry documents added (29 in total); no new `u_int_mdict` dictionary. Range default `-30` / `0` on customer schedules, production orders and production schedules, `-7` / `0` on the other transaction screens. Andon Events keep the multi-select status of the skill's worked example (default `[]`), the only multi-select control. Child and relationship screens may carry search dropdowns on their own transaction references after the parent control.

Layout standard (18 Oct 2026, skill `mes-query-control` 0.20, D071): new configurations use `colSize` 12 and `labelColSpan` 24. The 67 existing page configurations, `FormatQuery.json` and the constants of `05_generator/gen_query.py` stay at 8 / 8 until the owner asks for them to be regenerated.

#### Deferred items (to be worked later)

| No. | Item | Note |
|---|---|---|
| Q21 | Registering the `u_int_` prefix (`u_int_mdict`; page configurations stay in the application collection `PageConfig`) in the data model register and generator | Deferred by the owner on 13 Oct 2026 |
| Q22 | Whether `/mdict` reads the extra keys of `u_int_mdict` (`siteId`, `recordNo`, audit keys), and how it treats the per-site dictionaries now that site is not used in queries | Deferred by the owner on 13 Oct 2026 |
| F1 | Index alignment: the query key strategy (`02_architecture/QueryKeySelectionStrategy.md`) and the generated index scripts put `siteId` first in several indexes (`{ siteId, recordNo }`, `{ siteId, status }`, `{ siteId, <date> }`). UI queries never carry `siteId`, so those indexes need `siteId` removed from the front, or a version without it, for list screens. Not changed by this instruction. | Follow-up on the query key strategy |
| F2 | `shiftId` now stores the shift code (`A`, `B`, `C`) in the sample documents (owner instruction, 13 Oct 2026; applied in `05_generator/gen_samples.py`). The model (`05_generator/model/flat_model.json`), `02_architecture/field_lists`, the collection specifications and their examples still describe `shiftId` as a reference to `u_mes_mast_shift._id`. They need the reference changed to the shift code (`u_mes_mast_shift.recordNo`) and a decision log entry. Child collections of the shift master (`shiftBreak`, `shiftWorkingDay`) keep the parent `_id`. | Follow-up on the model and specifications |
| F4 | Maintenance module check (15 Oct 2026): the allowed values of `u_mes_maint_maintenancePlan.planType` (Incoming, In Process, First Off ...) and `strategy` (Torque Control ...) belong to inspection plans and tightening, not maintenance plans; they are not used as query controls until corrected in the model. `u_mes_maint_equipmentQualification` has no required date key; its period control uses `startedAt`, so records in status Planned (no start yet) are found only after they start. | Follow-up on the model |
| F5 | PlanningAndExecution check (17 Oct 2026): `u_mes_plan_container` has no required date key. Its period control uses `packedAt`, which is null for empty and returned containers, so those are not listed by a date range. The model needs a required date key on containers (for example `registeredAt` or `lastMovedAt`), or the owner accepts that the Containers screen lists only packed containers by date. `u_mes_plan_customerSchedule.receivedAt` may be null; the period uses the required `horizonFrom` instead. | Follow-up on the model |

### 2.5 Observations on the sample files (not changed)


| File | Observation |
|---|---|
| `FormatQuery.json` | Corrected by the owner on 13 Oct 2026 and reviewed again the same day: parses (9 controls) once read as MongoDB shell style (`NumberInt`); labels, placeholders and error messages match their controls; every hard-coded default is one of its values; no double or trailing spaces. Cosmetic only: one error message reads "Please Select Direction" (capital S) and indentation mixes tabs and spaces. |
| `FormatQuery.json` | `config.api` (`/stdtools/phantomzen`) and `config.params` (`op`) are the page's submit endpoint, hard-coded per page as needed; they are outside the scope of this instruction. |
| `cropdown.md` | 16 documents (after `ShiftZone` was deleted by the owner on 13 Oct 2026), each with 10 values or fewer. Shift and financial year are master-type data; MES pages use `/mdict` `Shift` instead. Document `X016` has a space in its name (`Task Status`). |
| `mdict.json` | Legacy content of another application (watch dials, two-wheeler customers, other plants); kept as a format reference only. |

## 3. IvyConfig

No project-specific values beyond section 1. `moduleName` comes from the module table of `02_architecture/collection_inventory.md`.

## 4. Stable

No project-specific values beyond section 1. Run from the project root: `python3 05_generator/gen_stable.py --all` (every query screen; or `--module <code>`, `--modules <a>,<b>`, named collections; `--dry-run` first after a rule change), then `python3 05_generator/gen_stable.py --check`. Scope: collections with a file in `query/PageConfigs` (skill 0.8, D069).

## 5. Menu

| Item | Value |
|---|---|
| Module order | `mast, prod, plan, matl, trac, qual, perf, maint, syst, ehs, bmr, mmr` |
| Level 0 `_id` block | `2010, 2020, ... 2120`, `seq` 1..12 |
| Level 0 labels | Menu column of the module table in `02_architecture/collection_inventory.md` (owner short forms, 18 Oct 2026, D069): Master Data, Product, Plan, Mtl Mgt, Trace, Quality, Performance, Maint, System, EHS, BMR, MMR |
| Icons and sections | `MODULES` and `SECTIONS` tables in `05_generator/gen_menu.py` |
| Inputs | `02_architecture/collection_inventory.md`, `02_architecture/collection_type_matrix.csv`, `query/PageConfigs`, `query/IvyConfig` |
| Output | `04_reference_data/ui_controls/menu/menu.json` (never edited by hand; rerun `python3 05_generator/gen_menu.py`) |
