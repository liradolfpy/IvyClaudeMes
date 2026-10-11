// Indexes for u_mes_eqp_equipmentState
db.getCollection("u_mes_eqp_equipmentState").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_eqp_equipmentState").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_eqp_equipmentState").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_eqp_equipmentState").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_eqp_equipmentState").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_eqp_equipmentState").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_eqp_equipmentState").createIndex({ downtimeEventId: 1 }, { name: "ix_downtimeEventId" });
db.getCollection("u_mes_eqp_equipmentState").createIndex({ siteId: 1, startedAt: -1 }, { name: "ix_siteId_startedAt" });
db.getCollection("u_mes_eqp_equipmentState").createIndex({ equipmentId: 1, startedAt: -1 }, { name: "ix_equipmentId_startedAt" });
