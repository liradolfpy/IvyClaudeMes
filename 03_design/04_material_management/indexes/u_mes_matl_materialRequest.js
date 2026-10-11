// Indexes for u_mes_matl_materialRequest
db.getCollection("u_mes_matl_materialRequest").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_matl_materialRequest").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_matl_materialRequest").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_matl_materialRequest").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_matl_materialRequest").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_matl_materialRequest").createIndex({ fromLocationId: 1 }, { name: "ix_fromLocationId" });
db.getCollection("u_mes_matl_materialRequest").createIndex({ toLocationId: 1 }, { name: "ix_toLocationId" });
db.getCollection("u_mes_matl_materialRequest").createIndex({ siteId: 1, requestedAt: -1 }, { name: "ix_siteId_requestedAt" });
