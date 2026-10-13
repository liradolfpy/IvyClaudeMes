// Indexes for u_mes_qual_environmentalMonitoringPoint
db.getCollection("u_mes_qual_environmentalMonitoringPoint").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_environmentalMonitoringPoint").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_environmentalMonitoringPoint").createIndex({ areaId: 1 }, { name: "ix_areaId" });
db.getCollection("u_mes_qual_environmentalMonitoringPoint").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_qual_environmentalMonitoringPoint").createIndex({ processTagId: 1 }, { name: "ix_processTagId" });
