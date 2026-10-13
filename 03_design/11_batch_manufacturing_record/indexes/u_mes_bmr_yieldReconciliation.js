// Indexes for u_mes_bmr_yieldReconciliation
db.getCollection("u_mes_bmr_yieldReconciliation").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_bmr_yieldReconciliation").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_bmr_yieldReconciliation").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_bmr_yieldReconciliation").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_bmr_yieldReconciliation").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_bmr_yieldReconciliation").createIndex({ nonconformanceId: 1 }, { name: "ix_nonconformanceId" });
db.getCollection("u_mes_bmr_yieldReconciliation").createIndex({ siteId: 1, calculatedAt: -1 }, { name: "ix_siteId_calculatedAt" });
