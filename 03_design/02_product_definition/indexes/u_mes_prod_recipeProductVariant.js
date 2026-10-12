// Indexes for u_mes_prod_recipeProductVariant
db.getCollection("u_mes_prod_recipeProductVariant").createIndex({ recipeId: 1, productVariantId: 1 }, { name: "ux_recipeId_productVariantId", unique: true });
db.getCollection("u_mes_prod_recipeProductVariant").createIndex({ productVariantId: 1, recipeId: 1 }, { name: "ix_productVariantId_recipeId" });
