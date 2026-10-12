// Indexes for u_mes_syst_backupRun
db.getCollection("u_mes_syst_backupRun").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_backupRun").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_backupRun").createIndex({ evidenceControlledDocumentId: 1 }, { name: "ix_evidenceControlledDocumentId" });
db.getCollection("u_mes_syst_backupRun").createIndex({ siteId: 1, startedAt: -1 }, { name: "ix_siteId_startedAt" });
