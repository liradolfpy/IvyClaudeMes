# ClaudeMES - MES on MongoDB (Front Brake Caliper Assembly LH, Pune)

Start here:

1. `Folder_Guide.md` - where every file belongs.
2. `00_governance/project_working_rules.md` - how the project is run.
3. `00_governance/data_modeling_standard.md` - naming, flat documents, references, status, audit keys, BSON types.
4. `00_governance/data_model_register.md` - the collection register and master IDs.
5. `02_architecture/collection_inventory.md` and `collection_keys.md` - the model.

Rebuild the model documents from source:

    cd 05_generator
    python flatten_model.py
    python gen_docs.py ..
    python gen_specs.py ..
    python gen_samples.py ..

Restore seed data (after Phase 3): `mongorestore --db mes 06_seed_data/bson`

Position on 12 Oct 2026: research, model inventory, collection specifications and sample documents complete (369 flat collections, 8,245 keys, 3,690 sample documents: exactly 10 per collection under 03_design/<module>/samples). Includes the 44 collections and 212 keys of MES_ExternalRequirement_01 (01_research/MES_ExternalRequirement_01_impact_analysis.md) and the 23 collections and 33 keys of GMP_Pharma_01, pharmaceutical Good Manufacturing Practice (01_research/GMP_Pharma_01_impact_analysis.md). Twelve modules: the ten functional modules plus bmr (Batch Manufacturing Record, 5 collections) and mmr (Master Manufacturing Record, 2 collections; 01_research/BMR_MMR_module_designation.md). BSON seed files (06_seed_data), diagrams and data flows are not yet produced.
