// Indexes for u_mes_qlt_characteristic
db.getCollection("u_mes_qlt_characteristic").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qlt_characteristic").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qlt_characteristic").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qlt_characteristic").createIndex({ operationId: 1 }, { name: "ix_operationId" });
db.getCollection("u_mes_qlt_characteristic").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_qlt_characteristic").createIndex({ gaugeId: 1 }, { name: "ix_gaugeId" });
db.getCollection("u_mes_qlt_characteristic").createIndex({ gaugeTypeId: 1 }, { name: "ix_gaugeTypeId" });
