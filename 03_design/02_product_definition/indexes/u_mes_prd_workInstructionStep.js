// Indexes for u_mes_prd_workInstructionStep
db.getCollection("u_mes_prd_workInstructionStep").createIndex({ workInstructionId: 1, stepNo: 1 }, { name: "ux_workInstructionId_stepNo", unique: true });
