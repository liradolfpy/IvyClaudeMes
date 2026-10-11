# Assumptions log

| No | Date | Assumption | Effect if wrong |
|---|---|---|---|
| A001 | 11 Oct 2026 | Company and customer names are fictional: Varuna Brake Systems Pvt. Ltd., Chakan Plant, Pune (PN1); OEM Sahyadri Motors Ltd. | Names change in seed data only |
| A002 | 11 Oct 2026 | Volume basis 2,400 calipers per day, 300 days, about 720,000 units per year | Volume estimates and index advice change |
| A003 | 11 Oct 2026 | Lot tracking from casting to anodising; unit identifier created at piston and seal assembly; customer serial marked at laser marking | wipUnit and serialNumber relationship changes |
| A004 | 11 Oct 2026 | Seed timeline Mon 28 Sep to Sat 10 Oct 2026; 2 Oct holiday; 4 Oct weekly off; shifts A 06:00, B 14:00, C 22:00 IST | All seed dates shift |
| A005 | 11 Oct 2026 | Final inspection and packing share work center WC-FIP-01 but remain two operations | One more work center document |
| A006 | 11 Oct 2026 | Process values (torque, leak limits, T6 profile) will be representative engineering values, not an OEM specification | Values replaced when real ones are supplied |
| A007 | 11 Oct 2026 | No functional baseline document exists in the project, so the module codes were first derived by Claude (D001) and then set by the owner (D026) | Collection names change if a baseline with other codes is supplied |
| A008 | 11 Oct 2026 | DATA-001 and DATA-002 mean exactly what the requirements text of 11 Oct states (flat scalar documents; a concrete BSON type for every numeric key); no separate rule document exists | Standard sections 2 and 8 are revised |
| A009 | 11 Oct 2026 | BSON types in the field lists were assigned by naming rules and are confirmed collection by collection when each specification is written | Individual key types change |
| A010 | 11 Oct 2026 | The "exactly 10 documents" rule applies to each of the 299 collections, including child, relationship and value-list collections | Seed volume changes |
| A011 | 11 Oct 2026 | MongoDB time-series collections remain a storage recommendation for processReading and energyReading; validators cannot be attached to time-series collections | Storage notes change |
| A012 | 11 Oct 2026 | The Phase 1 research document keeps the collection names in use when it was written; `collection_inventory.md` is the authority for names | None |
| A013 | 11 Oct 2026 | The split between master collection (rule A) and fixed enumeration (rule B) was made by Claude key by key; a key can be moved from B to A by adding it to 05_generator/master_refs.py | Individual keys change from coded text to a reference |
