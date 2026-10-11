// Indexes for u_mes_mnt_toolItem
db.getCollection("u_mes_mnt_toolItem").createIndex({ toolId: 1, itemId: 1 }, { name: "ux_toolId_itemId", unique: true });
db.getCollection("u_mes_mnt_toolItem").createIndex({ itemId: 1, toolId: 1 }, { name: "ix_itemId_toolId" });
