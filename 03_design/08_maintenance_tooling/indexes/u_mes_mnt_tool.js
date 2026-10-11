// Indexes for u_mes_mnt_tool
db.getCollection("u_mes_mnt_tool").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mnt_tool").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mnt_tool").createIndex({ toolTypeId: 1 }, { name: "ix_toolTypeId" });
db.getCollection("u_mes_mnt_tool").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_mnt_tool").createIndex({ supplierId: 1 }, { name: "ix_supplierId" });
db.getCollection("u_mes_mnt_tool").createIndex({ storageLocationId: 1 }, { name: "ix_storageLocationId" });
db.getCollection("u_mes_mnt_tool").createIndex({ ownedByCustomerId: 1 }, { name: "ix_ownedByCustomerId" });
