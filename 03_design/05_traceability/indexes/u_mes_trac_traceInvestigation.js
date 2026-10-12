// Indexes for u_mes_trac_traceInvestigation
db.getCollection("u_mes_trac_traceInvestigation").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_trac_traceInvestigation").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_trac_traceInvestigation").createIndex({ qualityHoldId: 1 }, { name: "ix_qualityHoldId" });
db.getCollection("u_mes_trac_traceInvestigation").createIndex({ nonconformanceId: 1 }, { name: "ix_nonconformanceId" });
db.getCollection("u_mes_trac_traceInvestigation").createIndex({ customerComplaintId: 1 }, { name: "ix_customerComplaintId" });
db.getCollection("u_mes_trac_traceInvestigation").createIndex({ exportControlledDocumentId: 1 }, { name: "ix_exportControlledDocumentId" });
db.getCollection("u_mes_trac_traceInvestigation").createIndex({ relatedCollectionName: 1, relatedEntityId: 1 }, { name: "ix_relatedCollectionName_relatedEntityId" });
db.getCollection("u_mes_trac_traceInvestigation").createIndex({ siteId: 1, requestedAt: -1 }, { name: "ix_siteId_requestedAt" });
