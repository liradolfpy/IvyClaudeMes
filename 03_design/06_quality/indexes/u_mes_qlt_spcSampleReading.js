// Indexes for u_mes_qlt_spcSampleReading
db.getCollection("u_mes_qlt_spcSampleReading").createIndex({ spcSampleId: 1, sequenceNo: 1 }, { name: "ux_spcSampleId_sequenceNo", unique: true });
