// Indexes for u_mes_plan_lot
db.getCollection("u_mes_plan_lot").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_plan_lot").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_plan_lot").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_plan_lot").createIndex({ supplierId: 1 }, { name: "ix_supplierId" });
db.getCollection("u_mes_plan_lot").createIndex({ goodsReceiptId: 1 }, { name: "ix_goodsReceiptId" });
db.getCollection("u_mes_plan_lot").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_plan_lot").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_plan_lot").createIndex({ siteId: 1, manufacturedAt: -1 }, { name: "ix_siteId_manufacturedAt" });
