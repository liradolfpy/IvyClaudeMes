// Indexes for u_mes_mnt_maintenancePlanTask
db.getCollection("u_mes_mnt_maintenancePlanTask").createIndex({ maintenancePlanId: 1, taskNo: 1 }, { name: "ux_maintenancePlanId_taskNo", unique: true });
