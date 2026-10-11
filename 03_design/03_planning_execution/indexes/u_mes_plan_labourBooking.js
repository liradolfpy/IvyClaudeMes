// Indexes for u_mes_plan_labourBooking
db.getCollection("u_mes_plan_labourBooking").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_plan_labourBooking").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_plan_labourBooking").createIndex({ userId: 1 }, { name: "ix_userId" });
db.getCollection("u_mes_plan_labourBooking").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_plan_labourBooking").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_plan_labourBooking").createIndex({ operationId: 1 }, { name: "ix_operationId" });
db.getCollection("u_mes_plan_labourBooking").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_plan_labourBooking").createIndex({ siteId: 1, productionDate: -1 }, { name: "ix_siteId_productionDate" });
