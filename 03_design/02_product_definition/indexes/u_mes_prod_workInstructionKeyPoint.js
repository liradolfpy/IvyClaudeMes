// Indexes for u_mes_prod_workInstructionKeyPoint
db.getCollection("u_mes_prod_workInstructionKeyPoint").createIndex({ workInstructionId: 1, sequenceNo: 1 }, { name: "ux_workInstructionId_sequenceNo", unique: true });
