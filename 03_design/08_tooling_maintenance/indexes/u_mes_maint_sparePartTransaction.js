// Indexes for u_mes_maint_sparePartTransaction
db.getCollection("u_mes_maint_sparePartTransaction").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_maint_sparePartTransaction").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_maint_sparePartTransaction").createIndex({ sparePartId: 1 }, { name: "ix_sparePartId" });
db.getCollection("u_mes_maint_sparePartTransaction").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_maint_sparePartTransaction").createIndex({ maintenanceWorkOrderId: 1 }, { name: "ix_maintenanceWorkOrderId" });
db.getCollection("u_mes_maint_sparePartTransaction").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_maint_sparePartTransaction").createIndex({ storageLocationId: 1 }, { name: "ix_storageLocationId" });
db.getCollection("u_mes_maint_sparePartTransaction").createIndex({ siteId: 1, transactedAt: -1 }, { name: "ix_siteId_transactedAt" });
