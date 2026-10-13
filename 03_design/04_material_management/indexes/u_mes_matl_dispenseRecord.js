// Indexes for u_mes_matl_dispenseRecord
db.getCollection("u_mes_matl_dispenseRecord").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_matl_dispenseRecord").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_matl_dispenseRecord").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_matl_dispenseRecord").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_matl_dispenseRecord").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_matl_dispenseRecord").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_matl_dispenseRecord").createIndex({ balanceGaugeId: 1 }, { name: "ix_balanceGaugeId" });
db.getCollection("u_mes_matl_dispenseRecord").createIndex({ siteId: 1, dispensedAt: -1 }, { name: "ix_siteId_dispensedAt" });
