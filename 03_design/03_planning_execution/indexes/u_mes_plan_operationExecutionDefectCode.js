// Indexes for u_mes_plan_operationExecutionDefectCode
db.getCollection("u_mes_plan_operationExecutionDefectCode").createIndex({ operationExecutionId: 1, defectCodeId: 1 }, { name: "ux_operationExecutionId_defectCodeId", unique: true });
db.getCollection("u_mes_plan_operationExecutionDefectCode").createIndex({ defectCodeId: 1, operationExecutionId: 1 }, { name: "ix_defectCodeId_operationExecutionId" });
