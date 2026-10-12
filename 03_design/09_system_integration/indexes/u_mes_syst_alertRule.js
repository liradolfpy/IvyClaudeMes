// Indexes for u_mes_syst_alertRule
db.getCollection("u_mes_syst_alertRule").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_alertRule").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_alertRule").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_syst_alertRule").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_syst_alertRule").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_syst_alertRule").createIndex({ processTagId: 1 }, { name: "ix_processTagId" });
db.getCollection("u_mes_syst_alertRule").createIndex({ itemId: 1 }, { name: "ix_itemId" });
