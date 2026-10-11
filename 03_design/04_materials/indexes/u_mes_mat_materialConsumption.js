// Indexes for u_mes_mat_materialConsumption
db.getCollection("u_mes_mat_materialConsumption").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mat_materialConsumption").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mat_materialConsumption").createIndex({ operationExecutionId: 1 }, { name: "ix_operationExecutionId" });
db.getCollection("u_mes_mat_materialConsumption").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_mat_materialConsumption").createIndex({ wipUnitId: 1 }, { name: "ix_wipUnitId" });
db.getCollection("u_mes_mat_materialConsumption").createIndex({ parentLotId: 1 }, { name: "ix_parentLotId" });
db.getCollection("u_mes_mat_materialConsumption").createIndex({ componentItemId: 1 }, { name: "ix_componentItemId" });
db.getCollection("u_mes_mat_materialConsumption").createIndex({ siteId: 1, consumedAt: -1 }, { name: "ix_siteId_consumedAt" });
