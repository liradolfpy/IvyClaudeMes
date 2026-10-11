// Indexes for u_mes_sys_auditTrail
db.getCollection("u_mes_sys_auditTrail").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_sys_auditTrail").createIndex({ electronicSignatureId: 1 }, { name: "ix_electronicSignatureId" });
db.getCollection("u_mes_sys_auditTrail").createIndex({ relatedCollectionName: 1, relatedEntityId: 1 }, { name: "ix_relatedCollectionName_relatedEntityId" });
db.getCollection("u_mes_sys_auditTrail").createIndex({ siteId: 1, changedAt: -1 }, { name: "ix_siteId_changedAt" });
db.getCollection("u_mes_sys_auditTrail").createIndex({ relatedCollectionName: 1, relatedEntityId: 1, changedAt: -1 }, { name: "ix_relatedCollectionName_relatedEntityId_changedAt" });
