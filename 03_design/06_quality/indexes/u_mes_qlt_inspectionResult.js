// Indexes for u_mes_qlt_inspectionResult
db.getCollection("u_mes_qlt_inspectionResult").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qlt_inspectionResult").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qlt_inspectionResult").createIndex({ inspectionPlanId: 1 }, { name: "ix_inspectionPlanId" });
db.getCollection("u_mes_qlt_inspectionResult").createIndex({ characteristicId: 1 }, { name: "ix_characteristicId" });
db.getCollection("u_mes_qlt_inspectionResult").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qlt_inspectionResult").createIndex({ wipUnitId: 1 }, { name: "ix_wipUnitId" });
db.getCollection("u_mes_qlt_inspectionResult").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_qlt_inspectionResult").createIndex({ siteId: 1, measuredAt: -1 }, { name: "ix_siteId_measuredAt" });
