// Indexes for u_mes_qual_measurementCurve
db.getCollection("u_mes_qual_measurementCurve").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_measurementCurve").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_measurementCurve").createIndex({ curveEnvelopeId: 1 }, { name: "ix_curveEnvelopeId" });
db.getCollection("u_mes_qual_measurementCurve").createIndex({ characteristicId: 1 }, { name: "ix_characteristicId" });
db.getCollection("u_mes_qual_measurementCurve").createIndex({ wipUnitId: 1 }, { name: "ix_wipUnitId" });
db.getCollection("u_mes_qual_measurementCurve").createIndex({ serialNumberId: 1 }, { name: "ix_serialNumberId" });
db.getCollection("u_mes_qual_measurementCurve").createIndex({ operationExecutionId: 1 }, { name: "ix_operationExecutionId" });
db.getCollection("u_mes_qual_measurementCurve").createIndex({ siteId: 1, capturedAt: -1 }, { name: "ix_siteId_capturedAt" });
