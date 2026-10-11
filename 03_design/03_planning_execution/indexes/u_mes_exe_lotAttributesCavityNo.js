// Indexes for u_mes_exe_lotAttributesCavityNo
db.getCollection("u_mes_exe_lotAttributesCavityNo").createIndex({ lotId: 1, sequenceNo: 1 }, { name: "ux_lotId_sequenceNo", unique: true });
