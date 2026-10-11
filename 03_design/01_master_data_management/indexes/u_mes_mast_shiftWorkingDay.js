// Indexes for u_mes_mast_shiftWorkingDay
db.getCollection("u_mes_mast_shiftWorkingDay").createIndex({ shiftId: 1, sequenceNo: 1 }, { name: "ux_shiftId_sequenceNo", unique: true });
