// Indexes for u_mes_eqp_processTag
db.getCollection("u_mes_eqp_processTag").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_eqp_processTag").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_eqp_processTag").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_eqp_processTag").createIndex({ iotDeviceId: 1 }, { name: "ix_iotDeviceId" });
db.getCollection("u_mes_eqp_processTag").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
