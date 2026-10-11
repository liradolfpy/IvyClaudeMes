// Indexes for u_mes_qlt_gaugeCalibration
db.getCollection("u_mes_qlt_gaugeCalibration").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qlt_gaugeCalibration").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qlt_gaugeCalibration").createIndex({ gaugeId: 1 }, { name: "ix_gaugeId" });
db.getCollection("u_mes_qlt_gaugeCalibration").createIndex({ calibrationSupplierId: 1 }, { name: "ix_calibrationSupplierId" });
db.getCollection("u_mes_qlt_gaugeCalibration").createIndex({ certificateControlledDocumentId: 1 }, { name: "ix_certificateControlledDocumentId" });
db.getCollection("u_mes_qlt_gaugeCalibration").createIndex({ siteId: 1, calibratedAt: -1 }, { name: "ix_siteId_calibratedAt" });
