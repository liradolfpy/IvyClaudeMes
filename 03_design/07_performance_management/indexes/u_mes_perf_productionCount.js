// Indexes for u_mes_perf_productionCount
db.getCollection("u_mes_perf_productionCount").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_perf_productionCount").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_perf_productionCount").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_perf_productionCount").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_perf_productionCount").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_perf_productionCount").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_perf_productionCount").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_perf_productionCount").createIndex({ siteId: 1, productionDate: -1 }, { name: "ix_siteId_productionDate" });
