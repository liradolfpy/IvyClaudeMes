// Indexes for u_mes_mast_skillCertification
db.getCollection("u_mes_mast_skillCertification").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mast_skillCertification").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mast_skillCertification").createIndex({ userId: 1 }, { name: "ix_userId" });
db.getCollection("u_mes_mast_skillCertification").createIndex({ skillId: 1 }, { name: "ix_skillId" });
db.getCollection("u_mes_mast_skillCertification").createIndex({ assessorUserId: 1 }, { name: "ix_assessorUserId" });
db.getCollection("u_mes_mast_skillCertification").createIndex({ evidenceControlledDocumentId: 1 }, { name: "ix_evidenceControlledDocumentId" });
db.getCollection("u_mes_mast_skillCertification").createIndex({ siteId: 1, awardedAt: -1 }, { name: "ix_siteId_awardedAt" });
db.getCollection("u_mes_mast_skillCertification").createIndex({ userId: 1, skillId: 1, validTo: -1 }, { name: "ix_userId_skillId_validTo" });
