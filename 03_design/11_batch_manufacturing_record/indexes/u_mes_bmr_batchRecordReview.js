// Indexes for u_mes_bmr_batchRecordReview
db.getCollection("u_mes_bmr_batchRecordReview").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_bmr_batchRecordReview").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_bmr_batchRecordReview").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_bmr_batchRecordReview").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_bmr_batchRecordReview").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_bmr_batchRecordReview").createIndex({ yieldReconciliationId: 1 }, { name: "ix_yieldReconciliationId" });
db.getCollection("u_mes_bmr_batchRecordReview").createIndex({ auditTrailReviewId: 1 }, { name: "ix_auditTrailReviewId" });
db.getCollection("u_mes_bmr_batchRecordReview").createIndex({ siteId: 1, productionReviewedAt: -1 }, { name: "ix_siteId_productionReviewedAt" });
