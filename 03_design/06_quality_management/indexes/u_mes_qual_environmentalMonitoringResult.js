// Indexes for u_mes_qual_environmentalMonitoringResult
db.getCollection("u_mes_qual_environmentalMonitoringResult").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_environmentalMonitoringResult").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_environmentalMonitoringResult").createIndex({ environmentalMonitoringPointId: 1 }, { name: "ix_environmentalMonitoringPointId" });
db.getCollection("u_mes_qual_environmentalMonitoringResult").createIndex({ gaugeId: 1 }, { name: "ix_gaugeId" });
db.getCollection("u_mes_qual_environmentalMonitoringResult").createIndex({ nonconformanceId: 1 }, { name: "ix_nonconformanceId" });
db.getCollection("u_mes_qual_environmentalMonitoringResult").createIndex({ siteId: 1, sampledAt: -1 }, { name: "ix_siteId_sampledAt" });
