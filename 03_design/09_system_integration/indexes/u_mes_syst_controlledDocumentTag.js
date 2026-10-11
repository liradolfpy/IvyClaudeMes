// Indexes for u_mes_syst_controlledDocumentTag
db.getCollection("u_mes_syst_controlledDocumentTag").createIndex({ controlledDocumentId: 1, sequenceNo: 1 }, { name: "ux_controlledDocumentId_sequenceNo", unique: true });
