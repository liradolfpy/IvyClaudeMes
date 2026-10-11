// Indexes for u_mes_maint_maintenancePlanTask
db.getCollection("u_mes_maint_maintenancePlanTask").createIndex({ maintenancePlanId: 1, taskNo: 1 }, { name: "ux_maintenancePlanId_taskNo", unique: true });
