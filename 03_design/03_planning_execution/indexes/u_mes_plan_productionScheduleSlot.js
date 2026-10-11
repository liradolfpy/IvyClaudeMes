// Indexes for u_mes_plan_productionScheduleSlot
db.getCollection("u_mes_plan_productionScheduleSlot").createIndex({ productionScheduleId: 1, sequenceNo: 1 }, { name: "ux_productionScheduleId_sequenceNo", unique: true });
db.getCollection("u_mes_plan_productionScheduleSlot").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_plan_productionScheduleSlot").createIndex({ itemId: 1 }, { name: "ix_itemId" });
