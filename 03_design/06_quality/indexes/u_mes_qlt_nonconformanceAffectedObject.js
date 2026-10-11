// Indexes for u_mes_qlt_nonconformanceAffectedObject
db.getCollection("u_mes_qlt_nonconformanceAffectedObject").createIndex({ nonconformanceId: 1, sequenceNo: 1 }, { name: "ux_nonconformanceId_sequenceNo", unique: true });
db.getCollection("u_mes_qlt_nonconformanceAffectedObject").createIndex({ dispositionTypeId: 1 }, { name: "ix_dispositionTypeId" });
