// Indexes for u_mes_exe_stepCompletion
db.getCollection("u_mes_exe_stepCompletion").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_exe_stepCompletion").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_exe_stepCompletion").createIndex({ operationExecutionId: 1 }, { name: "ix_operationExecutionId" });
db.getCollection("u_mes_exe_stepCompletion").createIndex({ workInstructionId: 1 }, { name: "ix_workInstructionId" });
db.getCollection("u_mes_exe_stepCompletion").createIndex({ wipUnitId: 1 }, { name: "ix_wipUnitId" });
db.getCollection("u_mes_exe_stepCompletion").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_exe_stepCompletion").createIndex({ userId: 1 }, { name: "ix_userId" });
db.getCollection("u_mes_exe_stepCompletion").createIndex({ siteId: 1, startedAt: -1 }, { name: "ix_siteId_startedAt" });
