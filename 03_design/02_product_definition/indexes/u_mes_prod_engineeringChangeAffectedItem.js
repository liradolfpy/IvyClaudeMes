// Indexes for u_mes_prod_engineeringChangeAffectedItem
db.getCollection("u_mes_prod_engineeringChangeAffectedItem").createIndex({ engineeringChangeId: 1, sequenceNo: 1 }, { name: "ux_engineeringChangeId_sequenceNo", unique: true });
db.getCollection("u_mes_prod_engineeringChangeAffectedItem").createIndex({ itemId: 1 }, { name: "ix_itemId" });
