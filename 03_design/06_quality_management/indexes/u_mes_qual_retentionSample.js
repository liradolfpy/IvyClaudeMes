// Indexes for u_mes_qual_retentionSample
db.getCollection("u_mes_qual_retentionSample").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_retentionSample").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_retentionSample").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qual_retentionSample").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_qual_retentionSample").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_qual_retentionSample").createIndex({ serialNumberId: 1 }, { name: "ix_serialNumberId" });
db.getCollection("u_mes_qual_retentionSample").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_qual_retentionSample").createIndex({ siteId: 1, collectedAt: -1 }, { name: "ix_siteId_collectedAt" });
