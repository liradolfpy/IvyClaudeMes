// Indexes for u_mes_qual_riskAssessment
db.getCollection("u_mes_qual_riskAssessment").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_riskAssessment").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_riskAssessment").createIndex({ pfmeaId: 1 }, { name: "ix_pfmeaId" });
db.getCollection("u_mes_qual_riskAssessment").createIndex({ relatedCollectionName: 1, relatedEntityId: 1 }, { name: "ix_relatedCollectionName_relatedEntityId" });
db.getCollection("u_mes_qual_riskAssessment").createIndex({ siteId: 1, approvedAt: -1 }, { name: "ix_siteId_approvedAt" });
