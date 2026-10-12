// Indexes for u_mes_syst_interlockRule
db.getCollection("u_mes_syst_interlockRule").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_interlockRule").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_interlockRule").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_syst_interlockRule").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_syst_interlockRule").createIndex({ operationId: 1 }, { name: "ix_operationId" });
db.getCollection("u_mes_syst_interlockRule").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_syst_interlockRule").createIndex({ overrideRoleId: 1 }, { name: "ix_overrideRoleId" });
