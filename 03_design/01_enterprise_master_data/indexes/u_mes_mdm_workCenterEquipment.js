// Indexes for u_mes_mdm_workCenterEquipment
db.getCollection("u_mes_mdm_workCenterEquipment").createIndex({ workCenterId: 1, equipmentId: 1 }, { name: "ux_workCenterId_equipmentId", unique: true });
db.getCollection("u_mes_mdm_workCenterEquipment").createIndex({ equipmentId: 1, workCenterId: 1 }, { name: "ix_equipmentId_workCenterId" });
