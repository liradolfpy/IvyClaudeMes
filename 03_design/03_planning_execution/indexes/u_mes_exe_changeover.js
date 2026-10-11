// Indexes for u_mes_exe_changeover
db.getCollection("u_mes_exe_changeover").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_exe_changeover").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_exe_changeover").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_exe_changeover").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_exe_changeover").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_exe_changeover").createIndex({ fromProductionOrderId: 1 }, { name: "ix_fromProductionOrderId" });
db.getCollection("u_mes_exe_changeover").createIndex({ toProductionOrderId: 1 }, { name: "ix_toProductionOrderId" });
db.getCollection("u_mes_exe_changeover").createIndex({ siteId: 1, plannedStartAt: -1 }, { name: "ix_siteId_plannedStartAt" });
