// Indexes for u_mes_matl_exposureTimer
db.getCollection("u_mes_matl_exposureTimer").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_matl_exposureTimer").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_matl_exposureTimer").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_matl_exposureTimer").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_matl_exposureTimer").createIndex({ containerId: 1 }, { name: "ix_containerId" });
db.getCollection("u_mes_matl_exposureTimer").createIndex({ storageLocationId: 1 }, { name: "ix_storageLocationId" });
db.getCollection("u_mes_matl_exposureTimer").createIndex({ resetReasonCodeId: 1 }, { name: "ix_resetReasonCodeId" });
db.getCollection("u_mes_matl_exposureTimer").createIndex({ siteId: 1, startedAt: -1 }, { name: "ix_siteId_startedAt" });
