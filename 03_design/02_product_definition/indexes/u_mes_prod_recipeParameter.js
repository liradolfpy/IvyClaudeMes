// Indexes for u_mes_prod_recipeParameter
db.getCollection("u_mes_prod_recipeParameter").createIndex({ recipeId: 1, sequenceNo: 1 }, { name: "ux_recipeId_sequenceNo", unique: true });
db.getCollection("u_mes_prod_recipeParameter").createIndex({ processTagId: 1 }, { name: "ix_processTagId" });
db.getCollection("u_mes_prod_recipeParameter").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
