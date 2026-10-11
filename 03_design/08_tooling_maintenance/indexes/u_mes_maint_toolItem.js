// Indexes for u_mes_maint_toolItem
db.getCollection("u_mes_maint_toolItem").createIndex({ toolId: 1, itemId: 1 }, { name: "ux_toolId_itemId", unique: true });
db.getCollection("u_mes_maint_toolItem").createIndex({ itemId: 1, toolId: 1 }, { name: "ix_itemId_toolId" });
