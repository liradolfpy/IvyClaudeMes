// Indexes for u_mes_matl_storageLocation
db.getCollection("u_mes_matl_storageLocation").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_matl_storageLocation").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_matl_storageLocation").createIndex({ areaId: 1 }, { name: "ix_areaId" });
db.getCollection("u_mes_matl_storageLocation").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_matl_storageLocation").createIndex({ parentLocationId: 1 }, { name: "ix_parentLocationId" });
