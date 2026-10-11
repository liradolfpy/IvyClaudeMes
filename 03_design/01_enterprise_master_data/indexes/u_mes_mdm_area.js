// Indexes for u_mes_mdm_area
db.getCollection("u_mes_mdm_area").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mdm_area").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mdm_area").createIndex({ parentAreaId: 1 }, { name: "ix_parentAreaId" });
db.getCollection("u_mes_mdm_area").createIndex({ costCenterId: 1 }, { name: "ix_costCenterId" });
db.getCollection("u_mes_mdm_area").createIndex({ supervisorUserId: 1 }, { name: "ix_supervisorUserId" });
