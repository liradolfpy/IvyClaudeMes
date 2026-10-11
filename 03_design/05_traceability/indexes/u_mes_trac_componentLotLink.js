// Indexes for u_mes_trac_componentLotLink
db.getCollection("u_mes_trac_componentLotLink").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_trac_componentLotLink").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_trac_componentLotLink").createIndex({ parentLotId: 1 }, { name: "ix_parentLotId" });
db.getCollection("u_mes_trac_componentLotLink").createIndex({ childLotId: 1 }, { name: "ix_childLotId" });
db.getCollection("u_mes_trac_componentLotLink").createIndex({ parentItemId: 1 }, { name: "ix_parentItemId" });
db.getCollection("u_mes_trac_componentLotLink").createIndex({ childItemId: 1 }, { name: "ix_childItemId" });
db.getCollection("u_mes_trac_componentLotLink").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_trac_componentLotLink").createIndex({ siteId: 1, linkedAt: -1 }, { name: "ix_siteId_linkedAt" });
