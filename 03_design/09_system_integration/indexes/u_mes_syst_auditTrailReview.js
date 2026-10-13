// Indexes for u_mes_syst_auditTrailReview
db.getCollection("u_mes_syst_auditTrailReview").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_auditTrailReview").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_auditTrailReview").createIndex({ computerisedSystemId: 1 }, { name: "ix_computerisedSystemId" });
db.getCollection("u_mes_syst_auditTrailReview").createIndex({ nonconformanceId: 1 }, { name: "ix_nonconformanceId" });
db.getCollection("u_mes_syst_auditTrailReview").createIndex({ electronicSignatureId: 1 }, { name: "ix_electronicSignatureId" });
db.getCollection("u_mes_syst_auditTrailReview").createIndex({ relatedCollectionName: 1, relatedEntityId: 1 }, { name: "ix_relatedCollectionName_relatedEntityId" });
db.getCollection("u_mes_syst_auditTrailReview").createIndex({ siteId: 1, reviewFromAt: -1 }, { name: "ix_siteId_reviewFromAt" });
