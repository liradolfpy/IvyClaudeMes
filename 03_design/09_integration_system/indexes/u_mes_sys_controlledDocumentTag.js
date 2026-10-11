// Indexes for u_mes_sys_controlledDocumentTag
db.getCollection("u_mes_sys_controlledDocumentTag").createIndex({ controlledDocumentId: 1, sequenceNo: 1 }, { name: "ux_controlledDocumentId_sequenceNo", unique: true });
