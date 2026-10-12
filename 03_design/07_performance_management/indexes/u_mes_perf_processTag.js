// Indexes for u_mes_perf_processTag
db.getCollection("u_mes_perf_processTag").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_perf_processTag").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_perf_processTag").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_perf_processTag").createIndex({ iotDeviceId: 1 }, { name: "ix_iotDeviceId" });
db.getCollection("u_mes_perf_processTag").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_perf_processTag").createIndex({ areaId: 1 }, { name: "ix_areaId" });
db.getCollection("u_mes_perf_processTag").createIndex({ lineId: 1 }, { name: "ix_lineId" });
