// Indexes for u_mes_bmr_batchManufacturingRecord
db.getCollection("u_mes_bmr_batchManufacturingRecord").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_bmr_batchManufacturingRecord").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_bmr_batchManufacturingRecord").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_bmr_batchManufacturingRecord").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_bmr_batchManufacturingRecord").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_bmr_batchManufacturingRecord").createIndex({ masterManufacturingRecordId: 1 }, { name: "ix_masterManufacturingRecordId" });
db.getCollection("u_mes_bmr_batchManufacturingRecord").createIndex({ lineClearanceId: 1 }, { name: "ix_lineClearanceId" });
db.getCollection("u_mes_bmr_batchManufacturingRecord").createIndex({ siteId: 1, openedAt: -1 }, { name: "ix_siteId_openedAt" });
