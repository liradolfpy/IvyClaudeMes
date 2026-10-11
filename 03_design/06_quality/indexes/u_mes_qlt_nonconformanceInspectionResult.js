// Indexes for u_mes_qlt_nonconformanceInspectionResult
db.getCollection("u_mes_qlt_nonconformanceInspectionResult").createIndex({ nonconformanceId: 1, inspectionResultId: 1 }, { name: "ux_nonconformanceId_inspectionResultId", unique: true });
db.getCollection("u_mes_qlt_nonconformanceInspectionResult").createIndex({ inspectionResultId: 1, nonconformanceId: 1 }, { name: "ix_inspectionResultId_nonconformanceId" });
