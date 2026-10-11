// Indexes for u_mes_plan_andonEventEscalation
db.getCollection("u_mes_plan_andonEventEscalation").createIndex({ andonEventId: 1, level: 1 }, { name: "ux_andonEventId_level", unique: true });
db.getCollection("u_mes_plan_andonEventEscalation").createIndex({ toUserId: 1 }, { name: "ix_toUserId" });
