// Indexes for u_mes_sys_electronicSignature
db.getCollection("u_mes_sys_electronicSignature").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_sys_electronicSignature").createIndex({ userId: 1 }, { name: "ix_userId" });
db.getCollection("u_mes_sys_electronicSignature").createIndex({ roleId: 1 }, { name: "ix_roleId" });
db.getCollection("u_mes_sys_electronicSignature").createIndex({ signatureMeaningId: 1 }, { name: "ix_signatureMeaningId" });
db.getCollection("u_mes_sys_electronicSignature").createIndex({ witnessUserId: 1 }, { name: "ix_witnessUserId" });
db.getCollection("u_mes_sys_electronicSignature").createIndex({ relatedCollectionName: 1, relatedEntityId: 1 }, { name: "ix_relatedCollectionName_relatedEntityId" });
db.getCollection("u_mes_sys_electronicSignature").createIndex({ siteId: 1, signedAt: -1 }, { name: "ix_siteId_signedAt" });
