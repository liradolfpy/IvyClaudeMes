# Folder_Guide.md

Project root: E:\Ivy\Claude\ClaudeProjects\ClaudeMES (Git repository; earlier versions of any file are retrieved from Git, not from copies).
This guide is the authority for where a file belongs. Paths in all other documents are relative to the project root.

## 1. Rules

1. One kind of file per folder. Supplied originals, requirements, designs and generated outputs each stay in their assigned folder.
2. Files carry no stage labels (no draft, current, superseded or review markers). The file in its assigned folder is the one in force. History is in Git.
3. `99_Archive` and `100_Self_Notes` are reference-only. Nothing in them is project authority. Material taken from them into current documentation is reviewed first and the adoption is recorded in `00_governance/decision_log.md`.
4. Generated folders (`06_seed_data`, `08_validation/reports`, `09_deliverables`, and the generated files listed in section 3) are never edited by hand. Change the source in `05_generator` and regenerate.
5. Optional folders are created only when the first file for them exists. The empty folders already present are placeholders for planned files and may stay empty.
6. The same module sub-folders (section 4) are used wherever files are grouped by module.

## 2. Folder map

| Folder | Holds | Authority | Written by |
|---|---|---|---|
| (root) | Folder_Guide.md, README.md | Yes | Hand |
| 00_governance | Requirements and rules that every other file must follow: working rules, data modeling standard, MongoDB output rules, schema review checklist, data model register, decision log, assumptions log | Yes, highest | Hand, except data_model_register.md (generated) |
| 00_governance/decisions | Longer write-ups for a single decision, when the log entry is not enough (optional) | Yes | Hand |
| 01_research | Phase 1 research, feature matrix, source notes per product, external requirement workbooks and their impact analyses | Background | Hand |
| 01_research/sources | One notes file per product studied (optional) | Background | Hand |
| 02_architecture | Whole-model view: collection inventory, collection keys, field lists, diagrams, data flows, storage strategy | Yes | Generated: collection_inventory.md, collection_keys.md, field_lists/*. Hand: the rest |
| 02_architecture/field_lists | Key, BSON type and reference target per collection, one file per module | Yes | Generated |
| 02_architecture/diagrams | Mermaid ER diagrams, overall and per module | Yes | Hand |
| 02_architecture/data_flows | Order-to-dispatch and other flows | Yes | Hand |
| 02_architecture/storage | Time-series, archiving and volume notes | Yes | Hand |
| 03_design/<module folder>/specs | Collection specification: field dictionary with requiredness, description, example, allowed values | Yes | Generated; corrections are made in the dictionaries in 05_generator |
| 03_design/<module folder>/validators | JSON Schema validator per collection | Yes | Generated |
| 03_design/<module folder>/indexes | Index definitions per collection | Yes | Generated |
| 03_design/<module folder>/samples | Exactly 10 sample documents per collection in MongoDB shell style, one consistent sample-data universe | Yes | Generated |
| 04_reference_data | The caliper reference story the seed data must follow | Yes | Hand, except code_lists/status_values.md (generated) |
| 04_reference_data/product | BOM, routing, characteristics and tolerances | Yes | Hand |
| 04_reference_data/process_values | Torque, leak test and heat treatment values | Yes | Hand |
| 04_reference_data/code_lists | Status values, defect codes, downtime reason tree | Yes | Mixed |
| 04_reference_data/timeline | Production calendar and scenario script for the two-week period | Yes | Hand |
| 04_reference_data/ui_controls | UI configurations: query page configurations and IvyConfigs (`query/`), table page configurations (`table/`), menu (`menu/`), owner-maintained reference samples, and `ui_project_profile.md` (ClaudeMES values for the UI skills in the skills library `E:\Ivy\Claude\ClaudeSkills\MintSkills\UiSkills`) | Yes | Generated, except the reference samples and ui_project_profile.md (hand) |
| 05_generator | Python source that builds the model, the documents and the seed data | Yes (source) | Hand |
| 05_generator/model | flat_model.json, the machine-readable model | Yes | Generated |
| 05_generator/common, domains, builders | Shared helpers, one seed module per domain, document builders | Yes (source) | Hand |
| 06_seed_data/bson | One .bson file per collection, flat folder for mongorestore | Output | Generated |
| 06_seed_data/shell | One .js file per collection with shell-style insert statements | Output | Generated (folder created with the first file) |
| 06_seed_data/extended_json/<module folder> | Readable copy of the seed documents | Output | Generated |
| 07_database_scripts | create_indexes.js, validators, time-series creation, restore script | Yes | Generated and hand |
| 07_database_scripts/queries | Worked example queries | Yes | Hand |
| 08_validation/reports | Model consistency, reference integrity, timeline checks | Output | Generated |
| 08_validation/tests | Test scripts | Yes (source) | Hand |
| 09_deliverables/phase1, phase2, phase3 | What is handed over, copied from the folders above | Output | Copied |
| 99_Archive | Files taken out of use, in a dated sub-folder | No, reference-only | Moved |
| 100_Self_Notes | The owner's personal notes | No, reference-only | Owner only; Claude does not write here |

## 3. Where each existing file lives

| File | Folder |
|---|---|
| Folder_Guide.md, README.md | root |
| project_working_rules.md | 00_governance |
| data_modeling_standard.md | 00_governance |
| mongodb_output_rules.md | 00_governance |
| schema_review_checklist.md | 00_governance |
| data_model_register.md | 00_governance |
| decision_log.md, assumptions_log.md | 00_governance |
| phase1_research_feature_matrix_catalogue.md | 01_research (copy in 09_deliverables/phase1) |
| MES_ExternalRequirement_01.xlsx (owner's requirement workbook), MES_ExternalRequirement_01_impact_analysis.md | 01_research |
| GMP_Pharma_01_impact_analysis.md (pharmaceutical GMP requirements GMP-01 to GMP-55) | 01_research |
| BMR_MMR_module_designation.md (collections designated to bmr and mmr, common collections for decision) | 01_research |
| collection_inventory.md, collection_keys.md | 02_architecture |
| <module folder>_field_list.md (10 files) | 02_architecture/field_lists |
| status_values.md | 04_reference_data/code_lists |
| catalogue.py, keys.py, flatten_model.py, gen_docs.py, gen_specs.py | 05_generator |
| keydict_text.py, keydict_num.py, entity_samples.py (dictionaries behind the specifications) | 05_generator |
| master_refs.py (master collections and key conversions under DATA-003) | 05_generator |
| ext_req01.py (44 collections and 212 keys of MES_ExternalRequirement_01), ext_req01_samples.py (their sample rules) | 05_generator |
| gmp01.py (23 collections and 33 keys of GMP_Pharma_01, merged through ext_req01.py), gmp01_samples.py (their sample rules) | 05_generator |
| spec_rules.py (rules shared by the specification and sample generators) | 05_generator |
| gen_samples.py, sample_rules.py, sample_universe.py (sample documents) | 05_generator |
| gen_stable.py, gen_menu.py, gen_query.py (UI configurations: Stable table pages, menu, query page configurations with IvyConfigs and the dynamic dropdown registry; `gen_query.py --digest / --propose` for token-saving module work), query_screens.py (query screen decisions) | 05_generator |
| log_decision.py (next decision number, new decision rows, session handover note) | 05_generator |
| session_handover.md (latest session handover note only) | 00_governance |
| token_optimization_review.md (D073) | 00_governance/decisions |
| sample_data_registry.md (every sample _id, business number and display value) | 04_reference_data |
| sample_data_validation.md | 08_validation/reports |
| enumeration_values.md | 04_reference_data/code_lists |
| master_data_review.md | 08_validation/reports |
| module_summary.md (one per module) | 03_design/<module folder> |
| <collection name>.md / .json / .js / .js (369 each) | 03_design/<module folder>/specs, validators, indexes, samples |
| specification_check.md | 08_validation/reports |
| flat_model.json | 05_generator/model |
| model_consistency_check.md | 08_validation/reports |
| build_phase1.py, build_keys.py (nested-model builders) | 99_Archive/2026-10-11_nested_model |

## 4. Module folders and module codes

| Module folder | Module code | Module name |
|---|---|---|
| 01_master_data_management | mast | MasterDataManagement |
| 02_product_definition | prod | ProductDefinition |
| 03_planning_execution | plan | PlanningAndExecution |
| 04_material_management | matl | MaterialManagement |
| 05_traceability | trac | Traceability |
| 06_quality_management | qual | QualityManagement |
| 07_performance_management | perf | PerformanceManagement |
| 08_tooling_maintenance | maint | ToolingAndMaintenance |
| 09_system_integration | syst | SystemAndIntegration |
| 10_environment_health_safety | ehs | EnvironmentHealthAndSafety |
| 11_batch_manufacturing_record | bmr | BatchManufacturingRecord |
| 12_master_manufacturing_record | mmr | MasterManufacturingRecord |

Andon collections belong to PlanningAndExecution; energy collections belong to PerformanceManagement. The batch manufacturing record header, batch record review, its exceptions, batch release and yield reconciliation belong to BatchManufacturingRecord; the master manufacturing record and its recipe links belong to MasterManufacturingRecord; collections shared by the batch or master record and other MES functions stay in their functional module (01_research/BMR_MMR_module_designation.md).

## 5. File naming

- Governance and architecture documents: lower snake_case with .md, except Folder_Guide.md and README.md.
- Per-collection files use the full collection name: `u_mes_plan_productionOrder.md`, `.json`, `.js`, `.bson`.
- Archive sub-folders: `YYYY-MM-DD_short_reason`.
