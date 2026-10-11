// Indexes for u_mes_mnt_maintenanceWorkOrderAssignedToUser
db.getCollection("u_mes_mnt_maintenanceWorkOrderAssignedToUser").createIndex({ maintenanceWorkOrderId: 1, assignedToUserId: 1 }, { name: "ux_maintenanceWorkOrderId_assignedToUserId", unique: true });
db.getCollection("u_mes_mnt_maintenanceWorkOrderAssignedToUser").createIndex({ assignedToUserId: 1, maintenanceWorkOrderId: 1 }, { name: "ix_assignedToUserId_maintenanceWorkOrderId" });
