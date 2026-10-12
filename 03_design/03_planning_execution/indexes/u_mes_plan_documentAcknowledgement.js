// Indexes for u_mes_plan_documentAcknowledgement
db.getCollection("u_mes_plan_documentAcknowledgement").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_plan_documentAcknowledgement").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_plan_documentAcknowledgement").createIndex({ userId: 1 }, { name: "ix_userId" });
db.getCollection("u_mes_plan_documentAcknowledgement").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_plan_documentAcknowledgement").createIndex({ productVariantId: 1 }, { name: "ix_productVariantId" });
db.getCollection("u_mes_plan_documentAcknowledgement").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_plan_documentAcknowledgement").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_plan_documentAcknowledgement").createIndex({ relatedCollectionName: 1, relatedEntityId: 1 }, { name: "ix_relatedCollectionName_relatedEntityId" });
db.getCollection("u_mes_plan_documentAcknowledgement").createIndex({ siteId: 1, acknowledgedAt: -1 }, { name: "ix_siteId_acknowledgedAt" });
