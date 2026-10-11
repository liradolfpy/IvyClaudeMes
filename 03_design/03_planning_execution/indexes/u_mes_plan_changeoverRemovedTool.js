// Indexes for u_mes_plan_changeoverRemovedTool
db.getCollection("u_mes_plan_changeoverRemovedTool").createIndex({ changeoverId: 1, removedToolId: 1 }, { name: "ux_changeoverId_removedToolId", unique: true });
db.getCollection("u_mes_plan_changeoverRemovedTool").createIndex({ removedToolId: 1, changeoverId: 1 }, { name: "ix_removedToolId_changeoverId" });
