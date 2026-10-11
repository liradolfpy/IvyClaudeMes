# ClaudeMES - MES on MongoDB (Front Brake Caliper Assembly LH, Pune)

Folder guide. Numbered folders are in the order the work flows.

| Folder | Holds | Edited by hand? |
|---|---|---|
| 00_governance | data_model_register.md (single source of truth), decisions, assumptions, change log | Yes |
| 01_research | Phase 1 research, feature matrix, per-product source notes | Yes |
| 02_architecture | Collection catalogue, key list, conventions, ER diagrams, data flows, storage strategy | Yes |
| 03_design | Phase 2: per domain, per collection - specs, validators, indexes, samples | Generated from 05_generator, reviewed by hand |
| 04_reference_data | The caliper story: master IDs, BOM, routing, process values, code lists, timeline, scenario script | Yes |
| 05_generator | Python source: catalogue.py, keys.py, builders, seed generator, validator, packager | Yes |
| 06_seed_data | bson/ (flat, for mongorestore), manifest.json, extended_json/ by domain | No - generated |
| 07_database_scripts | create_indexes.js, validators, time-series creation, restore script, example queries | Yes |
| 08_validation | Validation reports and tests | Reports generated, tests by hand |
| 09_deliverables | What is handed over, by phase | No - copied from above |
| 99_archive | Superseded versions, dated | - |

Domain sub-folders (same names in 03_design and 06_seed_data/extended_json):
01_enterprise_master_data, 02_product_definition, 03_planning_execution, 04_materials, 05_traceability,
06_quality, 07_equipment_performance, 08_maintenance_tooling, 09_integration_system, 10_energy_safety_andon.

Rules
- The register in 00_governance wins over every other file.
- Never edit files in 06_seed_data; change 05_generator and regenerate.
- Restore: mongorestore --db mes 06_seed_data/bson

Status on 11 Oct 2026: Phase 1 complete (104 collections, 3,174 keys). Phase 2 and 3 folders are empty until those phases run.
