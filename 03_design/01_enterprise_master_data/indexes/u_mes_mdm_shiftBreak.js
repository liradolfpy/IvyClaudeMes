// Indexes for u_mes_mdm_shiftBreak
db.getCollection("u_mes_mdm_shiftBreak").createIndex({ shiftId: 1, sequenceNo: 1 }, { name: "ux_shiftId_sequenceNo", unique: true });
