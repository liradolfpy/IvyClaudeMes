// Indexes for u_mes_matl_materialMovement
db.getCollection("u_mes_matl_materialMovement").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_matl_materialMovement").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_matl_materialMovement").createIndex({ movementTypeId: 1 }, { name: "ix_movementTypeId" });
db.getCollection("u_mes_matl_materialMovement").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_matl_materialMovement").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_matl_materialMovement").createIndex({ containerId: 1 }, { name: "ix_containerId" });
db.getCollection("u_mes_matl_materialMovement").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_matl_materialMovement").createIndex({ siteId: 1, movedAt: -1 }, { name: "ix_siteId_movedAt" });
