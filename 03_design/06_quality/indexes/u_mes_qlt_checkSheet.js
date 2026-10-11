// Indexes for u_mes_qlt_checkSheet
db.getCollection("u_mes_qlt_checkSheet").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qlt_checkSheet").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qlt_checkSheet").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_qlt_checkSheet").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_qlt_checkSheet").createIndex({ operationId: 1 }, { name: "ix_operationId" });
db.getCollection("u_mes_qlt_checkSheet").createIndex({ itemId: 1 }, { name: "ix_itemId" });
