// Indexes for u_mes_plan_lineClearance
db.getCollection("u_mes_plan_lineClearance").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_plan_lineClearance").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_plan_lineClearance").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_plan_lineClearance").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_plan_lineClearance").createIndex({ previousProductionOrderId: 1 }, { name: "ix_previousProductionOrderId" });
db.getCollection("u_mes_plan_lineClearance").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_plan_lineClearance").createIndex({ changeoverId: 1 }, { name: "ix_changeoverId" });
db.getCollection("u_mes_plan_lineClearance").createIndex({ siteId: 1, startedAt: -1 }, { name: "ix_siteId_startedAt" });
