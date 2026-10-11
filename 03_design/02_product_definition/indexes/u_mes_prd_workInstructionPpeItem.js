// Indexes for u_mes_prd_workInstructionPpeItem
db.getCollection("u_mes_prd_workInstructionPpeItem").createIndex({ workInstructionId: 1, ppeItemId: 1 }, { name: "ux_workInstructionId_ppeItemId", unique: true });
db.getCollection("u_mes_prd_workInstructionPpeItem").createIndex({ ppeItemId: 1, workInstructionId: 1 }, { name: "ix_ppeItemId_workInstructionId" });
