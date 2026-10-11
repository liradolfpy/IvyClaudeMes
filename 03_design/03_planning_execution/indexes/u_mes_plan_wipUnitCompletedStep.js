// Indexes for u_mes_plan_wipUnitCompletedStep
db.getCollection("u_mes_plan_wipUnitCompletedStep").createIndex({ wipUnitId: 1, sequenceNo: 1 }, { name: "ux_wipUnitId_sequenceNo", unique: true });
