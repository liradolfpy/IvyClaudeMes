// Indexes for u_mes_perf_workCenterPerformance
db.getCollection("u_mes_perf_workCenterPerformance").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_perf_workCenterPerformance").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_perf_workCenterPerformance").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_perf_workCenterPerformance").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_perf_workCenterPerformance").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_perf_workCenterPerformance").createIndex({ productVariantId: 1 }, { name: "ix_productVariantId" });
db.getCollection("u_mes_perf_workCenterPerformance").createIndex({ siteId: 1, productionDate: -1 }, { name: "ix_siteId_productionDate" });
