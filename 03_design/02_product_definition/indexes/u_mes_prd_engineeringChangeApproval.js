// Indexes for u_mes_prd_engineeringChangeApproval
db.getCollection("u_mes_prd_engineeringChangeApproval").createIndex({ engineeringChangeId: 1, stepNo: 1 }, { name: "ux_engineeringChangeId_stepNo", unique: true });
db.getCollection("u_mes_prd_engineeringChangeApproval").createIndex({ userId: 1 }, { name: "ix_userId" });
