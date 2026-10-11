// Indexes for u_mes_prd_billOfMaterialComponentProductVariant
db.getCollection("u_mes_prd_billOfMaterialComponentProductVariant").createIndex({ billOfMaterialComponentId: 1, productVariantId: 1 }, { name: "ux_billOfMaterialComponentId_productVariantId", unique: true });
db.getCollection("u_mes_prd_billOfMaterialComponentProductVariant").createIndex({ productVariantId: 1, billOfMaterialComponentId: 1 }, { name: "ix_productVariantId_billOfMaterialComponentId" });
