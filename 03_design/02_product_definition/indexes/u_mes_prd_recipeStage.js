// Indexes for u_mes_prd_recipeStage
db.getCollection("u_mes_prd_recipeStage").createIndex({ recipeId: 1, stageNo: 1 }, { name: "ux_recipeId_stageNo", unique: true });
