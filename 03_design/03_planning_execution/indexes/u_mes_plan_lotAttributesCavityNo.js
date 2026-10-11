// Indexes for u_mes_plan_lotAttributesCavityNo
db.getCollection("u_mes_plan_lotAttributesCavityNo").createIndex({ lotId: 1, sequenceNo: 1 }, { name: "ux_lotId_sequenceNo", unique: true });
