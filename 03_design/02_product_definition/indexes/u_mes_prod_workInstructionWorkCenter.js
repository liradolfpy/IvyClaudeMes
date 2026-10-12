// Indexes for u_mes_prod_workInstructionWorkCenter
db.getCollection("u_mes_prod_workInstructionWorkCenter").createIndex({ workInstructionId: 1, workCenterId: 1 }, { name: "ux_workInstructionId_workCenterId", unique: true });
db.getCollection("u_mes_prod_workInstructionWorkCenter").createIndex({ workCenterId: 1, workInstructionId: 1 }, { name: "ix_workCenterId_workInstructionId" });
