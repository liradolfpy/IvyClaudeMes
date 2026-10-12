// Indexes for u_mes_plan_interlockEvent
db.getCollection("u_mes_plan_interlockEvent").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_plan_interlockEvent").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_plan_interlockEvent").createIndex({ interlockRuleId: 1 }, { name: "ix_interlockRuleId" });
db.getCollection("u_mes_plan_interlockEvent").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_plan_interlockEvent").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_plan_interlockEvent").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_plan_interlockEvent").createIndex({ wipUnitId: 1 }, { name: "ix_wipUnitId" });
db.getCollection("u_mes_plan_interlockEvent").createIndex({ relatedCollectionName: 1, relatedEntityId: 1 }, { name: "ix_relatedCollectionName_relatedEntityId" });
db.getCollection("u_mes_plan_interlockEvent").createIndex({ siteId: 1, productionDate: -1 }, { name: "ix_siteId_productionDate" });
