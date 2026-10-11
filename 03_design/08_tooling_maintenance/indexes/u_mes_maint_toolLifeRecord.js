// Indexes for u_mes_maint_toolLifeRecord
db.getCollection("u_mes_maint_toolLifeRecord").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_maint_toolLifeRecord").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_maint_toolLifeRecord").createIndex({ toolId: 1 }, { name: "ix_toolId" });
db.getCollection("u_mes_maint_toolLifeRecord").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_maint_toolLifeRecord").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_maint_toolLifeRecord").createIndex({ maintenanceWorkOrderId: 1 }, { name: "ix_maintenanceWorkOrderId" });
db.getCollection("u_mes_maint_toolLifeRecord").createIndex({ siteId: 1, eventAt: -1 }, { name: "ix_siteId_eventAt" });
