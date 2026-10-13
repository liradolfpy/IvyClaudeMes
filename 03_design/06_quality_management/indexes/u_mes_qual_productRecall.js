// Indexes for u_mes_qual_productRecall
db.getCollection("u_mes_qual_productRecall").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_productRecall").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_productRecall").createIndex({ customerId: 1 }, { name: "ix_customerId" });
db.getCollection("u_mes_qual_productRecall").createIndex({ customerComplaintId: 1 }, { name: "ix_customerComplaintId" });
db.getCollection("u_mes_qual_productRecall").createIndex({ nonconformanceId: 1 }, { name: "ix_nonconformanceId" });
db.getCollection("u_mes_qual_productRecall").createIndex({ traceInvestigationId: 1 }, { name: "ix_traceInvestigationId" });
db.getCollection("u_mes_qual_productRecall").createIndex({ capaId: 1 }, { name: "ix_capaId" });
db.getCollection("u_mes_qual_productRecall").createIndex({ siteId: 1, initiatedAt: -1 }, { name: "ix_siteId_initiatedAt" });
