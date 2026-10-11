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

Restore seed data (after Phase 3): `mongorestore --db mes 06_seed_data/bson`

Position on 11 Oct 2026: research and model inventory complete (257 flat collections, 5,553 keys). Collection specifications (03_design) and seed data (06_seed_data) are not yet produced.
