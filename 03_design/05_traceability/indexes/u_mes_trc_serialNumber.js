// Indexes for u_mes_trc_serialNumber
db.getCollection("u_mes_trc_serialNumber").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_trc_serialNumber").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_trc_serialNumber").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_trc_serialNumber").createIndex({ productVariantId: 1 }, { name: "ix_productVariantId" });
db.getCollection("u_mes_trc_serialNumber").createIndex({ wipUnitId: 1 }, { name: "ix_wipUnitId" });
db.getCollection("u_mes_trc_serialNumber").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_trc_serialNumber").createIndex({ numberRangeId: 1 }, { name: "ix_numberRangeId" });
db.getCollection("u_mes_trc_serialNumber").createIndex({ siteId: 1, issuedAt: -1 }, { name: "ix_siteId_issuedAt" });
db.getCollection("u_mes_trc_serialNumber").createIndex({ dataMatrixPayload: 1 }, { name: "ux_dataMatrixPayload", unique: true });
