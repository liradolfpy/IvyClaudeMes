// Indexes for u_mes_prod_engineeringChangeControlledDocument
db.getCollection("u_mes_prod_engineeringChangeControlledDocument").createIndex({ engineeringChangeId: 1, controlledDocumentId: 1 }, { name: "ux_engineeringChangeId_controlledDocumentId", unique: true });
db.getCollection("u_mes_prod_engineeringChangeControlledDocument").createIndex({ controlledDocumentId: 1, engineeringChangeId: 1 }, { name: "ix_controlledDocumentId_engineeringChangeId" });
