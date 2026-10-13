// Indexes for u_mes_maint_logbookEntry
db.getCollection("u_mes_maint_logbookEntry").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_maint_logbookEntry").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_maint_logbookEntry").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_maint_logbookEntry").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_maint_logbookEntry").createIndex({ cleaningRecordId: 1 }, { name: "ix_cleaningRecordId" });
db.getCollection("u_mes_maint_logbookEntry").createIndex({ maintenanceWorkOrderId: 1 }, { name: "ix_maintenanceWorkOrderId" });
db.getCollection("u_mes_maint_logbookEntry").createIndex({ lineClearanceId: 1 }, { name: "ix_lineClearanceId" });
db.getCollection("u_mes_maint_logbookEntry").createIndex({ relatedCollectionName: 1, relatedEntityId: 1 }, { name: "ix_relatedCollectionName_relatedEntityId" });
db.getCollection("u_mes_maint_logbookEntry").createIndex({ siteId: 1, startedAt: -1 }, { name: "ix_siteId_startedAt" });
