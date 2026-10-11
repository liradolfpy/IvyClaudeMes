// Indexes for u_mes_trac_asBuiltRecordOperation
db.getCollection("u_mes_trac_asBuiltRecordOperation").createIndex({ asBuiltRecordId: 1, stepNo: 1 }, { name: "ux_asBuiltRecordId_stepNo", unique: true });
db.getCollection("u_mes_trac_asBuiltRecordOperation").createIndex({ operationId: 1 }, { name: "ix_operationId" });
db.getCollection("u_mes_trac_asBuiltRecordOperation").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_trac_asBuiltRecordOperation").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
