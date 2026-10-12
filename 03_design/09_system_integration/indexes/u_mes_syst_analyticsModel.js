// Indexes for u_mes_syst_analyticsModel
db.getCollection("u_mes_syst_analyticsModel").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_analyticsModel").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_analyticsModel").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_syst_analyticsModel").createIndex({ modelControlledDocumentId: 1 }, { name: "ix_modelControlledDocumentId" });
