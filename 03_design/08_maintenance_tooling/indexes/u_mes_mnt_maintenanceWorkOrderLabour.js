// Indexes for u_mes_mnt_maintenanceWorkOrderLabour
db.getCollection("u_mes_mnt_maintenanceWorkOrderLabour").createIndex({ maintenanceWorkOrderId: 1, sequenceNo: 1 }, { name: "ux_maintenanceWorkOrderId_sequenceNo", unique: true });
db.getCollection("u_mes_mnt_maintenanceWorkOrderLabour").createIndex({ userId: 1 }, { name: "ix_userId" });
