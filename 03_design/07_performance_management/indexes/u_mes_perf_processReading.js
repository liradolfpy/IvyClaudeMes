// Indexes for u_mes_perf_processReading
db.getCollection("u_mes_perf_processReading").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_perf_processReading").createIndex({ processTagId: 1 }, { name: "ix_processTagId" });
db.getCollection("u_mes_perf_processReading").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_perf_processReading").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_perf_processReading").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_perf_processReading").createIndex({ areaId: 1 }, { name: "ix_areaId" });
db.getCollection("u_mes_perf_processReading").createIndex({ siteId: 1, timestamp: -1 }, { name: "ix_siteId_timestamp" });
db.getCollection("u_mes_perf_processReading").createIndex({ processTagId: 1, timestamp: -1 }, { name: "ix_processTagId_timestamp" });
db.getCollection("u_mes_perf_processReading").createIndex({ sourceMessageUuid: 1 }, { name: "ix_sourceMessageUuid" });
