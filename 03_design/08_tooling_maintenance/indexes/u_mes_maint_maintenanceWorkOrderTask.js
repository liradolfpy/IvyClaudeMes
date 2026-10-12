// Indexes for u_mes_maint_maintenanceWorkOrderTask
db.getCollection("u_mes_maint_maintenanceWorkOrderTask").createIndex({ maintenanceWorkOrderId: 1, taskNo: 1 }, { name: "ux_maintenanceWorkOrderId_taskNo", unique: true });
db.getCollection("u_mes_maint_maintenanceWorkOrderTask").createIndex({ maintenancePlanTaskId: 1 }, { name: "ix_maintenancePlanTaskId" });
db.getCollection("u_mes_maint_maintenanceWorkOrderTask").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
