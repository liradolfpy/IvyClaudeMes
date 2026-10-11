// Indexes for u_mes_sys_operatorAppDeviceBinding
db.getCollection("u_mes_sys_operatorAppDeviceBinding").createIndex({ operatorAppId: 1, sequenceNo: 1 }, { name: "ux_operatorAppId_sequenceNo", unique: true });
db.getCollection("u_mes_sys_operatorAppDeviceBinding").createIndex({ iotDeviceId: 1 }, { name: "ix_iotDeviceId" });
