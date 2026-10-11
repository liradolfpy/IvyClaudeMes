// Indexes for u_mes_prd_billOfMaterialComponentAlternateItem
db.getCollection("u_mes_prd_billOfMaterialComponentAlternateItem").createIndex({ billOfMaterialComponentId: 1, alternateItemId: 1 }, { name: "ux_billOfMaterialComponentId_alternateItemId", unique: true });
db.getCollection("u_mes_prd_billOfMaterialComponentAlternateItem").createIndex({ alternateItemId: 1, billOfMaterialComponentId: 1 }, { name: "ix_alternateItemId_billOfMaterialComponentId" });
