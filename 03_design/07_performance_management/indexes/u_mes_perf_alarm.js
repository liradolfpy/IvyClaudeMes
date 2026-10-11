// Indexes for u_mes_perf_alarm
db.getCollection("u_mes_perf_alarm").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_perf_alarm").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_perf_alarm").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_perf_alarm").createIndex({ processTagId: 1 }, { name: "ix_processTagId" });
db.getCollection("u_mes_perf_alarm").createIndex({ iotDeviceId: 1 }, { name: "ix_iotDeviceId" });
db.getCollection("u_mes_perf_alarm").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_perf_alarm").createIndex({ downtimeEventId: 1 }, { name: "ix_downtimeEventId" });
db.getCollection("u_mes_perf_alarm").createIndex({ siteId: 1, raisedAt: -1 }, { name: "ix_siteId_raisedAt" });
