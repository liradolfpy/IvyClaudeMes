// Indexes for u_mes_eqp_leakTestResultStage
db.getCollection("u_mes_eqp_leakTestResultStage").createIndex({ leakTestResultId: 1, stageNo: 1 }, { name: "ux_leakTestResultId_stageNo", unique: true });
