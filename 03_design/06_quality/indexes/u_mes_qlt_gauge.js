// Indexes for u_mes_qlt_gauge
db.getCollection("u_mes_qlt_gauge").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qlt_gauge").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qlt_gauge").createIndex({ gaugeTypeId: 1 }, { name: "ix_gaugeTypeId" });
db.getCollection("u_mes_qlt_gauge").createIndex({ manufacturerId: 1 }, { name: "ix_manufacturerId" });
db.getCollection("u_mes_qlt_gauge").createIndex({ rangeUnitOfMeasureId: 1 }, { name: "ix_rangeUnitOfMeasureId" });
db.getCollection("u_mes_qlt_gauge").createIndex({ storageLocationId: 1 }, { name: "ix_storageLocationId" });
db.getCollection("u_mes_qlt_gauge").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
