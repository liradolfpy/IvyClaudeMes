// Indexes for u_mes_mnt_maintenanceWorkOrder
db.getCollection("u_mes_mnt_maintenanceWorkOrder").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mnt_maintenanceWorkOrder").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mnt_maintenanceWorkOrder").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_mnt_maintenanceWorkOrder").createIndex({ toolId: 1 }, { name: "ix_toolId" });
db.getCollection("u_mes_mnt_maintenanceWorkOrder").createIndex({ maintenancePlanId: 1 }, { name: "ix_maintenancePlanId" });
db.getCollection("u_mes_mnt_maintenanceWorkOrder").createIndex({ downtimeEventId: 1 }, { name: "ix_downtimeEventId" });
db.getCollection("u_mes_mnt_maintenanceWorkOrder").createIndex({ reasonCodeId: 1 }, { name: "ix_reasonCodeId" });
db.getCollection("u_mes_mnt_maintenanceWorkOrder").createIndex({ siteId: 1, reportedAt: -1 }, { name: "ix_siteId_reportedAt" });
