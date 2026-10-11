// Indexes for u_mes_qual_spcSample
db.getCollection("u_mes_qual_spcSample").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_spcSample").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_spcSample").createIndex({ spcChartId: 1 }, { name: "ix_spcChartId" });
db.getCollection("u_mes_qual_spcSample").createIndex({ characteristicId: 1 }, { name: "ix_characteristicId" });
db.getCollection("u_mes_qual_spcSample").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_qual_spcSample").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_qual_spcSample").createIndex({ nonconformanceId: 1 }, { name: "ix_nonconformanceId" });
db.getCollection("u_mes_qual_spcSample").createIndex({ siteId: 1, sampledAt: -1 }, { name: "ix_siteId_sampledAt" });
