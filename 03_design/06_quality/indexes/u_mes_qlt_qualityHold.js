// Indexes for u_mes_qlt_qualityHold
db.getCollection("u_mes_qlt_qualityHold").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qlt_qualityHold").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qlt_qualityHold").createIndex({ reasonCodeId: 1 }, { name: "ix_reasonCodeId" });
db.getCollection("u_mes_qlt_qualityHold").createIndex({ nonconformanceId: 1 }, { name: "ix_nonconformanceId" });
db.getCollection("u_mes_qlt_qualityHold").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qlt_qualityHold").createIndex({ quarantineLocationId: 1 }, { name: "ix_quarantineLocationId" });
db.getCollection("u_mes_qlt_qualityHold").createIndex({ siteId: 1, placedAt: -1 }, { name: "ix_siteId_placedAt" });
