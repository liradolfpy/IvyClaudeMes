// Indexes for u_mes_prod_recipeStage
db.getCollection("u_mes_prod_recipeStage").createIndex({ recipeId: 1, stageNo: 1 }, { name: "ux_recipeId_stageNo", unique: true });
