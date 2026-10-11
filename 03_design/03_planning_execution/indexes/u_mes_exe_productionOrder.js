// Indexes for u_mes_exe_productionOrder
db.getCollection("u_mes_exe_productionOrder").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_exe_productionOrder").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_exe_productionOrder").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_exe_productionOrder").createIndex({ productVariantId: 1 }, { name: "ix_productVariantId" });
db.getCollection("u_mes_exe_productionOrder").createIndex({ billOfMaterialId: 1 }, { name: "ix_billOfMaterialId" });
db.getCollection("u_mes_exe_productionOrder").createIndex({ routingId: 1 }, { name: "ix_routingId" });
db.getCollection("u_mes_exe_productionOrder").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_exe_productionOrder").createIndex({ siteId: 1, plannedStartAt: -1 }, { name: "ix_siteId_plannedStartAt" });
