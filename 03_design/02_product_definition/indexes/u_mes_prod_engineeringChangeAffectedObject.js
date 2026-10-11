// Indexes for u_mes_prod_engineeringChangeAffectedObject
db.getCollection("u_mes_prod_engineeringChangeAffectedObject").createIndex({ engineeringChangeId: 1, sequenceNo: 1 }, { name: "ux_engineeringChangeId_sequenceNo", unique: true });
