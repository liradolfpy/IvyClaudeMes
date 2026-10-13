// Indexes for u_mes_mmr_masterManufacturingRecordRecipe
db.getCollection("u_mes_mmr_masterManufacturingRecordRecipe").createIndex({ masterManufacturingRecordId: 1, recipeId: 1 }, { name: "ux_masterManufacturingRecordId_recipeId", unique: true });
db.getCollection("u_mes_mmr_masterManufacturingRecordRecipe").createIndex({ recipeId: 1, masterManufacturingRecordId: 1 }, { name: "ix_recipeId_masterManufacturingRecordId" });
