// Indexes for u_mes_exe_productionOrderRelease
db.getCollection("u_mes_exe_productionOrderRelease").createIndex({ productionOrderId: 1, releaseNo: 1 }, { name: "ux_productionOrderId_releaseNo", unique: true });
