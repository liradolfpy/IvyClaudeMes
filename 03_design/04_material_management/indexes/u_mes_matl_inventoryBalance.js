// Indexes for u_mes_matl_inventoryBalance
db.getCollection("u_mes_matl_inventoryBalance").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_matl_inventoryBalance").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_matl_inventoryBalance").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_matl_inventoryBalance").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_matl_inventoryBalance").createIndex({ storageLocationId: 1 }, { name: "ix_storageLocationId" });
db.getCollection("u_mes_matl_inventoryBalance").createIndex({ containerId: 1 }, { name: "ix_containerId" });
db.getCollection("u_mes_matl_inventoryBalance").createIndex({ stockStatusId: 1 }, { name: "ix_stockStatusId" });
db.getCollection("u_mes_matl_inventoryBalance").createIndex({ siteId: 1, firstReceivedAt: -1 }, { name: "ix_siteId_firstReceivedAt" });
db.getCollection("u_mes_matl_inventoryBalance").createIndex({ itemId: 1, lotId: 1, storageLocationId: 1, stockStatus: 1 }, { name: "ux_itemId_lotId_storageLocationId_stockStatus", unique: true });
