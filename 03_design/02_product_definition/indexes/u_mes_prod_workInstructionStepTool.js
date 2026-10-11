// Indexes for u_mes_prod_workInstructionStepTool
db.getCollection("u_mes_prod_workInstructionStepTool").createIndex({ workInstructionStepId: 1, toolId: 1 }, { name: "ux_workInstructionStepId_toolId", unique: true });
db.getCollection("u_mes_prod_workInstructionStepTool").createIndex({ toolId: 1, workInstructionStepId: 1 }, { name: "ix_toolId_workInstructionStepId" });
