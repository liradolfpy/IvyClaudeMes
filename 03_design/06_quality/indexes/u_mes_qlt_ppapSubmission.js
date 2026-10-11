// Indexes for u_mes_qlt_ppapSubmission
db.getCollection("u_mes_qlt_ppapSubmission").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qlt_ppapSubmission").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qlt_ppapSubmission").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qlt_ppapSubmission").createIndex({ customerId: 1 }, { name: "ix_customerId" });
db.getCollection("u_mes_qlt_ppapSubmission").createIndex({ engineeringChangeId: 1 }, { name: "ix_engineeringChangeId" });
db.getCollection("u_mes_qlt_ppapSubmission").createIndex({ controlPlanId: 1 }, { name: "ix_controlPlanId" });
db.getCollection("u_mes_qlt_ppapSubmission").createIndex({ pfmeaId: 1 }, { name: "ix_pfmeaId" });
db.getCollection("u_mes_qlt_ppapSubmission").createIndex({ siteId: 1, pswSignedAt: -1 }, { name: "ix_siteId_pswSignedAt" });
