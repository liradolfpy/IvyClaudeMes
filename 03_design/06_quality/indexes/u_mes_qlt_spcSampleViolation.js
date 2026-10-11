// Indexes for u_mes_qlt_spcSampleViolation
db.getCollection("u_mes_qlt_spcSampleViolation").createIndex({ spcSampleId: 1, sequenceNo: 1 }, { name: "ux_spcSampleId_sequenceNo", unique: true });
