// Indexes for u_mes_mmr_masterManufacturingRecord
db.getCollection("u_mes_mmr_masterManufacturingRecord").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mmr_masterManufacturingRecord").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mmr_masterManufacturingRecord").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_mmr_masterManufacturingRecord").createIndex({ itemRevisionId: 1 }, { name: "ix_itemRevisionId" });
db.getCollection("u_mes_mmr_masterManufacturingRecord").createIndex({ productVariantId: 1 }, { name: "ix_productVariantId" });
db.getCollection("u_mes_mmr_masterManufacturingRecord").createIndex({ previousMasterManufacturingRecordId: 1 }, { name: "ix_previousMasterManufacturingRecordId" });
db.getCollection("u_mes_mmr_masterManufacturingRecord").createIndex({ billOfMaterialId: 1 }, { name: "ix_billOfMaterialId" });
