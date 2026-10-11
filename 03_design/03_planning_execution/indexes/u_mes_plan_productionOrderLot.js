// Indexes for u_mes_plan_productionOrderLot
db.getCollection("u_mes_plan_productionOrderLot").createIndex({ productionOrderId: 1, lotId: 1 }, { name: "ux_productionOrderId_lotId", unique: true });
db.getCollection("u_mes_plan_productionOrderLot").createIndex({ lotId: 1, productionOrderId: 1 }, { name: "ix_lotId_productionOrderId" });
