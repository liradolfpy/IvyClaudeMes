// Indexes for u_mes_sys_erpMessage
db.getCollection("u_mes_sys_erpMessage").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_sys_erpMessage").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_sys_erpMessage").createIndex({ integrationConnectorId: 1 }, { name: "ix_integrationConnectorId" });
db.getCollection("u_mes_sys_erpMessage").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_sys_erpMessage").createIndex({ goodsReceiptId: 1 }, { name: "ix_goodsReceiptId" });
db.getCollection("u_mes_sys_erpMessage").createIndex({ shipmentId: 1 }, { name: "ix_shipmentId" });
db.getCollection("u_mes_sys_erpMessage").createIndex({ relatedCollectionName: 1, relatedEntityId: 1 }, { name: "ix_relatedCollectionName_relatedEntityId" });
db.getCollection("u_mes_sys_erpMessage").createIndex({ siteId: 1, createdInSourceAt: -1 }, { name: "ix_siteId_createdInSourceAt" });
db.getCollection("u_mes_sys_erpMessage").createIndex({ idempotencyKey: 1 }, { name: "ux_idempotencyKey", unique: true });
