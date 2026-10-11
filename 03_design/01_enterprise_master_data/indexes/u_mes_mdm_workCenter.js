// Indexes for u_mes_mdm_workCenter
db.getCollection("u_mes_mdm_workCenter").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mdm_workCenter").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mdm_workCenter").createIndex({ areaId: 1 }, { name: "ix_areaId" });
db.getCollection("u_mes_mdm_workCenter").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_mdm_workCenter").createIndex({ costCenterId: 1 }, { name: "ix_costCenterId" });
db.getCollection("u_mes_mdm_workCenter").createIndex({ inputLocationId: 1 }, { name: "ix_inputLocationId" });
db.getCollection("u_mes_mdm_workCenter").createIndex({ outputLocationId: 1 }, { name: "ix_outputLocationId" });
