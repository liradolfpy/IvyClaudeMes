// Indexes for u_mes_maint_sparePart
db.getCollection("u_mes_maint_sparePart").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_maint_sparePart").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_maint_sparePart").createIndex({ manufacturerId: 1 }, { name: "ix_manufacturerId" });
db.getCollection("u_mes_maint_sparePart").createIndex({ supplierId: 1 }, { name: "ix_supplierId" });
db.getCollection("u_mes_maint_sparePart").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_maint_sparePart").createIndex({ storageLocationId: 1 }, { name: "ix_storageLocationId" });
