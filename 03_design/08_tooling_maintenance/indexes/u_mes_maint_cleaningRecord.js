// Indexes for u_mes_maint_cleaningRecord
db.getCollection("u_mes_maint_cleaningRecord").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_maint_cleaningRecord").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_maint_cleaningRecord").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_maint_cleaningRecord").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_maint_cleaningRecord").createIndex({ procedureControlledDocumentId: 1 }, { name: "ix_procedureControlledDocumentId" });
db.getCollection("u_mes_maint_cleaningRecord").createIndex({ previousProductionOrderId: 1 }, { name: "ix_previousProductionOrderId" });
db.getCollection("u_mes_maint_cleaningRecord").createIndex({ previousItemId: 1 }, { name: "ix_previousItemId" });
db.getCollection("u_mes_maint_cleaningRecord").createIndex({ siteId: 1, dirtyHoldStartAt: -1 }, { name: "ix_siteId_dirtyHoldStartAt" });
