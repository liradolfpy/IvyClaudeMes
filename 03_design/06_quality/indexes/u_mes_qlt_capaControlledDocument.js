// Indexes for u_mes_qlt_capaControlledDocument
db.getCollection("u_mes_qlt_capaControlledDocument").createIndex({ capaId: 1, controlledDocumentId: 1 }, { name: "ux_capaId_controlledDocumentId", unique: true });
db.getCollection("u_mes_qlt_capaControlledDocument").createIndex({ controlledDocumentId: 1, capaId: 1 }, { name: "ix_controlledDocumentId_capaId" });
