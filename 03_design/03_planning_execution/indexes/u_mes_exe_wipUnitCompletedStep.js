// Indexes for u_mes_exe_wipUnitCompletedStep
db.getCollection("u_mes_exe_wipUnitCompletedStep").createIndex({ wipUnitId: 1, sequenceNo: 1 }, { name: "ux_wipUnitId_sequenceNo", unique: true });
