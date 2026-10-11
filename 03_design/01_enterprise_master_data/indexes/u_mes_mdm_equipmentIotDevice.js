// Indexes for u_mes_mdm_equipmentIotDevice
db.getCollection("u_mes_mdm_equipmentIotDevice").createIndex({ equipmentId: 1, iotDeviceId: 1 }, { name: "ux_equipmentId_iotDeviceId", unique: true });
db.getCollection("u_mes_mdm_equipmentIotDevice").createIndex({ iotDeviceId: 1, equipmentId: 1 }, { name: "ix_iotDeviceId_equipmentId" });
