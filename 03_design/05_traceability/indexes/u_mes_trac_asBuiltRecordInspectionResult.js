// Indexes for u_mes_trac_asBuiltRecordInspectionResult
db.getCollection("u_mes_trac_asBuiltRecordInspectionResult").createIndex({ asBuiltRecordId: 1, inspectionResultId: 1 }, { name: "ux_asBuiltRecordId_inspectionResultId", unique: true });
db.getCollection("u_mes_trac_asBuiltRecordInspectionResult").createIndex({ inspectionResultId: 1, asBuiltRecordId: 1 }, { name: "ix_inspectionResultId_asBuiltRecordId" });
