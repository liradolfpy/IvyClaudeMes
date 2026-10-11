// Indexes for u_mes_sys_auditTrailChange
db.getCollection("u_mes_sys_auditTrailChange").createIndex({ auditTrailId: 1, sequenceNo: 1 }, { name: "ux_auditTrailId_sequenceNo", unique: true });
