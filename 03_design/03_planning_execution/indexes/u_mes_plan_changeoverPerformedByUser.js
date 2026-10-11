// Indexes for u_mes_plan_changeoverPerformedByUser
db.getCollection("u_mes_plan_changeoverPerformedByUser").createIndex({ changeoverId: 1, performedByUserId: 1 }, { name: "ux_changeoverId_performedByUserId", unique: true });
db.getCollection("u_mes_plan_changeoverPerformedByUser").createIndex({ performedByUserId: 1, changeoverId: 1 }, { name: "ix_performedByUserId_changeoverId" });
