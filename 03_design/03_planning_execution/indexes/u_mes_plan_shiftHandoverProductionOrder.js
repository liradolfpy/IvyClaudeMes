// Indexes for u_mes_plan_shiftHandoverProductionOrder
db.getCollection("u_mes_plan_shiftHandoverProductionOrder").createIndex({ shiftHandoverId: 1, productionOrderId: 1 }, { name: "ux_shiftHandoverId_productionOrderId", unique: true });
db.getCollection("u_mes_plan_shiftHandoverProductionOrder").createIndex({ productionOrderId: 1, shiftHandoverId: 1 }, { name: "ix_productionOrderId_shiftHandoverId" });
