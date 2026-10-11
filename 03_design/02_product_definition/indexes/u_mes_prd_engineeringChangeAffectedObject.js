// Indexes for u_mes_prd_engineeringChangeAffectedObject
db.getCollection("u_mes_prd_engineeringChangeAffectedObject").createIndex({ engineeringChangeId: 1, sequenceNo: 1 }, { name: "ux_engineeringChangeId_sequenceNo", unique: true });
