// Indexes for u_mes_prod_engineeringChange
db.getCollection("u_mes_prod_engineeringChange").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_prod_engineeringChange").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_prod_engineeringChange").createIndex({ customerId: 1 }, { name: "ix_customerId" });
db.getCollection("u_mes_prod_engineeringChange").createIndex({ stockDispositionTypeId: 1 }, { name: "ix_stockDispositionTypeId" });
db.getCollection("u_mes_prod_engineeringChange").createIndex({ riskAssessmentId: 1 }, { name: "ix_riskAssessmentId" });
db.getCollection("u_mes_prod_engineeringChange").createIndex({ siteId: 1, raisedAt: -1 }, { name: "ix_siteId_raisedAt" });
