// Indexes for u_mes_perf_lossSummary
db.getCollection("u_mes_perf_lossSummary").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_perf_lossSummary").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_perf_lossSummary").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_perf_lossSummary").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_perf_lossSummary").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_perf_lossSummary").createIndex({ lossCategoryId: 1 }, { name: "ix_lossCategoryId" });
db.getCollection("u_mes_perf_lossSummary").createIndex({ reasonCodeId: 1 }, { name: "ix_reasonCodeId" });
db.getCollection("u_mes_perf_lossSummary").createIndex({ siteId: 1, productionDate: -1 }, { name: "ix_siteId_productionDate" });
