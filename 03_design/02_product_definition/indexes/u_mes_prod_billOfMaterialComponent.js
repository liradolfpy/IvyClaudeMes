// Indexes for u_mes_prod_billOfMaterialComponent
db.getCollection("u_mes_prod_billOfMaterialComponent").createIndex({ billOfMaterialId: 1, lineNo: 1 }, { name: "ux_billOfMaterialId_lineNo", unique: true });
db.getCollection("u_mes_prod_billOfMaterialComponent").createIndex({ componentItemId: 1 }, { name: "ix_componentItemId" });
db.getCollection("u_mes_prod_billOfMaterialComponent").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_prod_billOfMaterialComponent").createIndex({ operationId: 1 }, { name: "ix_operationId" });
