// Indexes for u_mes_perf_operatorPerformance
db.getCollection("u_mes_perf_operatorPerformance").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_perf_operatorPerformance").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_perf_operatorPerformance").createIndex({ userId: 1 }, { name: "ix_userId" });
db.getCollection("u_mes_perf_operatorPerformance").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_perf_operatorPerformance").createIndex({ productVariantId: 1 }, { name: "ix_productVariantId" });
db.getCollection("u_mes_perf_operatorPerformance").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_perf_operatorPerformance").createIndex({ siteId: 1, productionDate: -1 }, { name: "ix_siteId_productionDate" });
