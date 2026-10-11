// Indexes for u_mes_prd_workInstructionKeyPoint
db.getCollection("u_mes_prd_workInstructionKeyPoint").createIndex({ workInstructionId: 1, sequenceNo: 1 }, { name: "ux_workInstructionId_sequenceNo", unique: true });
