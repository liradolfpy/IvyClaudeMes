// Indexes for u_mes_mdm_workCenterOperation
db.getCollection("u_mes_mdm_workCenterOperation").createIndex({ workCenterId: 1, operationId: 1 }, { name: "ux_workCenterId_operationId", unique: true });
db.getCollection("u_mes_mdm_workCenterOperation").createIndex({ operationId: 1, workCenterId: 1 }, { name: "ix_operationId_workCenterId" });
