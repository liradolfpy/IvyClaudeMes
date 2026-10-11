// Indexes for u_mes_prod_workInstructionStep
db.getCollection("u_mes_prod_workInstructionStep").createIndex({ workInstructionId: 1, stepNo: 1 }, { name: "ux_workInstructionId_stepNo", unique: true });
