// Indexes for u_mes_sys_operatorAppOperation
db.getCollection("u_mes_sys_operatorAppOperation").createIndex({ operatorAppId: 1, operationId: 1 }, { name: "ux_operatorAppId_operationId", unique: true });
db.getCollection("u_mes_sys_operatorAppOperation").createIndex({ operationId: 1, operatorAppId: 1 }, { name: "ix_operationId_operatorAppId" });
