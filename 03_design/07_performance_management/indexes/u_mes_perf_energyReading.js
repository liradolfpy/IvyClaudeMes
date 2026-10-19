// Indexes for u_mes_perf_energyReading
db.getCollection("u_mes_perf_energyReading").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_perf_energyReading").createIndex({ meterIotDeviceId: 1 }, { name: "ix_meterIotDeviceId" });
db.getCollection("u_mes_perf_energyReading").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_perf_energyReading").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_perf_energyReading").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_perf_energyReading").createIndex({ energyTypeId: 1 }, { name: "ix_energyTypeId" });
db.getCollection("u_mes_perf_energyReading").createIndex({ siteId: 1, intervalStartAt: -1 }, { name: "ix_siteId_intervalStartAt" });
db.getCollection("u_mes_perf_energyReading").createIndex({ meterIotDeviceId: 1, intervalStartAt: -1 }, { name: "ix_meterIotDeviceId_intervalStartAt" });
db.getCollection("u_mes_perf_energyReading").createIndex({ sourceMessageUuid: 1 }, { name: "ix_sourceMessageUuid" });
