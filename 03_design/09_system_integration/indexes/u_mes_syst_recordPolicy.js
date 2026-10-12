// Indexes for u_mes_syst_recordPolicy
db.getCollection("u_mes_syst_recordPolicy").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_recordPolicy").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_recordPolicy").createIndex({ lockOnStatusDefinitionId: 1 }, { name: "ix_lockOnStatusDefinitionId" });
db.getCollection("u_mes_syst_recordPolicy").createIndex({ editRoleId: 1 }, { name: "ix_editRoleId" });
