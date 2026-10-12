// Indexes for u_mes_maint_equipmentLifecycleEvent
db.getCollection("u_mes_maint_equipmentLifecycleEvent").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_maint_equipmentLifecycleEvent").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_maint_equipmentLifecycleEvent").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_maint_equipmentLifecycleEvent").createIndex({ maintenanceWorkOrderId: 1 }, { name: "ix_maintenanceWorkOrderId" });
db.getCollection("u_mes_maint_equipmentLifecycleEvent").createIndex({ engineeringChangeId: 1 }, { name: "ix_engineeringChangeId" });
db.getCollection("u_mes_maint_equipmentLifecycleEvent").createIndex({ modelPredictionId: 1 }, { name: "ix_modelPredictionId" });
db.getCollection("u_mes_maint_equipmentLifecycleEvent").createIndex({ siteId: 1, eventAt: -1 }, { name: "ix_siteId_eventAt" });
