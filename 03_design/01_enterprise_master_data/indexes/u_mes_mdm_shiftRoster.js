// Indexes for u_mes_mdm_shiftRoster
db.getCollection("u_mes_mdm_shiftRoster").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mdm_shiftRoster").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mdm_shiftRoster").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_mdm_shiftRoster").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_mdm_shiftRoster").createIndex({ supervisorUserId: 1 }, { name: "ix_supervisorUserId" });
db.getCollection("u_mes_mdm_shiftRoster").createIndex({ siteId: 1, productionDate: -1 }, { name: "ix_siteId_productionDate" });
