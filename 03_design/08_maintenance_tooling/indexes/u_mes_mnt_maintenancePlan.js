// Indexes for u_mes_mnt_maintenancePlan
db.getCollection("u_mes_mnt_maintenancePlan").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mnt_maintenancePlan").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mnt_maintenancePlan").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_mnt_maintenancePlan").createIndex({ toolId: 1 }, { name: "ix_toolId" });
db.getCollection("u_mes_mnt_maintenancePlan").createIndex({ ownerDepartmentId: 1 }, { name: "ix_ownerDepartmentId" });
