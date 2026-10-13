// Indexes for u_mes_qual_productQualityReview
db.getCollection("u_mes_qual_productQualityReview").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_productQualityReview").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_productQualityReview").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qual_productQualityReview").createIndex({ reportControlledDocumentId: 1 }, { name: "ix_reportControlledDocumentId" });
db.getCollection("u_mes_qual_productQualityReview").createIndex({ siteId: 1, reviewPeriodFromDate: -1 }, { name: "ix_siteId_reviewPeriodFromDate" });
