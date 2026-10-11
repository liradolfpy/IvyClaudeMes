// Indexes for u_mes_trac_asBuiltRecord
db.getCollection("u_mes_trac_asBuiltRecord").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_trac_asBuiltRecord").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_trac_asBuiltRecord").createIndex({ wipUnitId: 1 }, { name: "ix_wipUnitId" });
db.getCollection("u_mes_trac_asBuiltRecord").createIndex({ serialNumberId: 1 }, { name: "ix_serialNumberId" });
db.getCollection("u_mes_trac_asBuiltRecord").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_trac_asBuiltRecord").createIndex({ productVariantId: 1 }, { name: "ix_productVariantId" });
db.getCollection("u_mes_trac_asBuiltRecord").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_trac_asBuiltRecord").createIndex({ siteId: 1, builtAt: -1 }, { name: "ix_siteId_builtAt" });
