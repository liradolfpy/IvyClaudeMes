// Indexes for u_mes_plan_operationExecution
db.getCollection("u_mes_plan_operationExecution").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_plan_operationExecution").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_plan_operationExecution").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_plan_operationExecution").createIndex({ wipUnitId: 1 }, { name: "ix_wipUnitId" });
db.getCollection("u_mes_plan_operationExecution").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_plan_operationExecution").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_plan_operationExecution").createIndex({ routingId: 1 }, { name: "ix_routingId" });
db.getCollection("u_mes_plan_operationExecution").createIndex({ siteId: 1, startedAt: -1 }, { name: "ix_siteId_startedAt" });
db.getCollection("u_mes_plan_operationExecution").createIndex({ wipUnitId: 1, stepNo: 1, attemptNo: 1 }, { name: "ix_wipUnitId_stepNo_attemptNo" });
db.getCollection("u_mes_plan_operationExecution").createIndex({ workCenterId: 1, startedAt: -1 }, { name: "ix_workCenterId_startedAt" });
db.getCollection("u_mes_plan_operationExecution").createIndex({ siteId: 1, sourceMessageUuid: 1 }, { name: "ux_siteId_sourceMessageUuid", unique: true, partialFilterExpression: { sourceMessageUuid: { $type: "string" } } });
