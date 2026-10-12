// Indexes for u_mes_plan_operatorSession
db.getCollection("u_mes_plan_operatorSession").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_plan_operatorSession").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_plan_operatorSession").createIndex({ userId: 1 }, { name: "ix_userId" });
db.getCollection("u_mes_plan_operatorSession").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_plan_operatorSession").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_plan_operatorSession").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_plan_operatorSession").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_plan_operatorSession").createIndex({ siteId: 1, productionDate: -1 }, { name: "ix_siteId_productionDate" });
