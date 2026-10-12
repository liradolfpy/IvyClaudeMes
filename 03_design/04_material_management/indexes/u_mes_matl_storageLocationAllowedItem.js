// Indexes for u_mes_matl_storageLocationAllowedItem
db.getCollection("u_mes_matl_storageLocationAllowedItem").createIndex({ storageLocationId: 1, itemId: 1 }, { name: "ux_storageLocationId_itemId", unique: true });
db.getCollection("u_mes_matl_storageLocationAllowedItem").createIndex({ itemId: 1, storageLocationId: 1 }, { name: "ix_itemId_storageLocationId" });
