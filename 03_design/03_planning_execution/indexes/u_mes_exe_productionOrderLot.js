// Indexes for u_mes_exe_productionOrderLot
db.getCollection("u_mes_exe_productionOrderLot").createIndex({ productionOrderId: 1, lotId: 1 }, { name: "ux_productionOrderId_lotId", unique: true });
db.getCollection("u_mes_exe_productionOrderLot").createIndex({ lotId: 1, productionOrderId: 1 }, { name: "ix_lotId_productionOrderId" });
