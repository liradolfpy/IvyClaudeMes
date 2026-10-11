// Indexes for u_mes_syst_statusTransition
db.getCollection("u_mes_syst_statusTransition").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_statusTransition").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_statusTransition").createIndex({ fromStatusDefinitionId: 1 }, { name: "ix_fromStatusDefinitionId" });
db.getCollection("u_mes_syst_statusTransition").createIndex({ toStatusDefinitionId: 1 }, { name: "ix_toStatusDefinitionId" });
