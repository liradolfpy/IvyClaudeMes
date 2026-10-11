// Indexes for u_mes_plan_changeoverStep
db.getCollection("u_mes_plan_changeoverStep").createIndex({ changeoverId: 1, stepNo: 1 }, { name: "ux_changeoverId_stepNo", unique: true });
