// Indexes for u_mes_plan_setupVerification
db.getCollection("u_mes_plan_setupVerification").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_plan_setupVerification").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_plan_setupVerification").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_plan_setupVerification").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_plan_setupVerification").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_plan_setupVerification").createIndex({ productVariantId: 1 }, { name: "ix_productVariantId" });
db.getCollection("u_mes_plan_setupVerification").createIndex({ changeoverId: 1 }, { name: "ix_changeoverId" });
db.getCollection("u_mes_plan_setupVerification").createIndex({ siteId: 1, verifiedAt: -1 }, { name: "ix_siteId_verifiedAt" });
