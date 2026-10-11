// Indexes for u_mes_prod_itemRevision
db.getCollection("u_mes_prod_itemRevision").createIndex({ itemId: 1, sequenceNo: 1 }, { name: "ux_itemId_sequenceNo", unique: true });
db.getCollection("u_mes_prod_itemRevision").createIndex({ engineeringChangeId: 1 }, { name: "ix_engineeringChangeId" });
