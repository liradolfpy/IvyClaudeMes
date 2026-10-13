// Indexes for u_mes_bmr_batchRelease
db.getCollection("u_mes_bmr_batchRelease").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_bmr_batchRelease").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_bmr_batchRelease").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_bmr_batchRelease").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_bmr_batchRelease").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_bmr_batchRelease").createIndex({ batchRecordReviewId: 1 }, { name: "ix_batchRecordReviewId" });
db.getCollection("u_mes_bmr_batchRelease").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_bmr_batchRelease").createIndex({ siteId: 1, releasedAt: -1 }, { name: "ix_siteId_releasedAt" });
