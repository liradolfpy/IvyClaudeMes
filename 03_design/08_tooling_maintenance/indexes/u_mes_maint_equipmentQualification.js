// Indexes for u_mes_maint_equipmentQualification
db.getCollection("u_mes_maint_equipmentQualification").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_maint_equipmentQualification").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_maint_equipmentQualification").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_maint_equipmentQualification").createIndex({ engineeringChangeId: 1 }, { name: "ix_engineeringChangeId" });
db.getCollection("u_mes_maint_equipmentQualification").createIndex({ protocolControlledDocumentId: 1 }, { name: "ix_protocolControlledDocumentId" });
db.getCollection("u_mes_maint_equipmentQualification").createIndex({ reportControlledDocumentId: 1 }, { name: "ix_reportControlledDocumentId" });
db.getCollection("u_mes_maint_equipmentQualification").createIndex({ electronicSignatureId: 1 }, { name: "ix_electronicSignatureId" });
db.getCollection("u_mes_maint_equipmentQualification").createIndex({ siteId: 1, startedAt: -1 }, { name: "ix_siteId_startedAt" });
