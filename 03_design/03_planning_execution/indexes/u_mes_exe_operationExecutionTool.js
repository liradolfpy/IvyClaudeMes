// Indexes for u_mes_exe_operationExecutionTool
db.getCollection("u_mes_exe_operationExecutionTool").createIndex({ operationExecutionId: 1, toolId: 1 }, { name: "ux_operationExecutionId_toolId", unique: true });
db.getCollection("u_mes_exe_operationExecutionTool").createIndex({ toolId: 1, operationExecutionId: 1 }, { name: "ix_toolId_operationExecutionId" });
