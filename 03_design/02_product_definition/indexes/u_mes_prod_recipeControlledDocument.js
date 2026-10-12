// Indexes for u_mes_prod_recipeControlledDocument
db.getCollection("u_mes_prod_recipeControlledDocument").createIndex({ recipeId: 1, controlledDocumentId: 1 }, { name: "ux_recipeId_controlledDocumentId", unique: true });
db.getCollection("u_mes_prod_recipeControlledDocument").createIndex({ controlledDocumentId: 1, recipeId: 1 }, { name: "ix_controlledDocumentId_recipeId" });
