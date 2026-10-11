// Indexes for u_mes_exe_wipUnit
db.getCollection("u_mes_exe_wipUnit").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_exe_wipUnit").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_exe_wipUnit").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_exe_wipUnit").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_exe_wipUnit").createIndex({ productVariantId: 1 }, { name: "ix_productVariantId" });
db.getCollection("u_mes_exe_wipUnit").createIndex({ serialNumberId: 1 }, { name: "ix_serialNumberId" });
db.getCollection("u_mes_exe_wipUnit").createIndex({ bodyLotId: 1 }, { name: "ix_bodyLotId" });
db.getCollection("u_mes_exe_wipUnit").createIndex({ siteId: 1, startedAt: -1 }, { name: "ix_siteId_startedAt" });
