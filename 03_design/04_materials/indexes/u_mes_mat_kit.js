// Indexes for u_mes_mat_kit
db.getCollection("u_mes_mat_kit").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mat_kit").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mat_kit").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_mat_kit").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_mat_kit").createIndex({ toLocationId: 1 }, { name: "ix_toLocationId" });
db.getCollection("u_mes_mat_kit").createIndex({ siteId: 1, requiredAt: -1 }, { name: "ix_siteId_requiredAt" });
