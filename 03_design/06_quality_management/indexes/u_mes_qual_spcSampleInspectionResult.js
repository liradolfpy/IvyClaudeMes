// Indexes for u_mes_qual_spcSampleInspectionResult
db.getCollection("u_mes_qual_spcSampleInspectionResult").createIndex({ spcSampleId: 1, inspectionResultId: 1 }, { name: "ux_spcSampleId_inspectionResultId", unique: true });
db.getCollection("u_mes_qual_spcSampleInspectionResult").createIndex({ inspectionResultId: 1, spcSampleId: 1 }, { name: "ix_inspectionResultId_spcSampleId" });
