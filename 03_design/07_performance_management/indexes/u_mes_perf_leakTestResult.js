// Indexes for u_mes_perf_leakTestResult
db.getCollection("u_mes_perf_leakTestResult").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_perf_leakTestResult").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_perf_leakTestResult").createIndex({ wipUnitId: 1 }, { name: "ix_wipUnitId" });
db.getCollection("u_mes_perf_leakTestResult").createIndex({ operationExecutionId: 1 }, { name: "ix_operationExecutionId" });
db.getCollection("u_mes_perf_leakTestResult").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_perf_leakTestResult").createIndex({ recipeId: 1 }, { name: "ix_recipeId" });
db.getCollection("u_mes_perf_leakTestResult").createIndex({ testerIotDeviceId: 1 }, { name: "ix_testerIotDeviceId" });
db.getCollection("u_mes_perf_leakTestResult").createIndex({ siteId: 1, masterLeakVerifiedAt: -1 }, { name: "ix_siteId_masterLeakVerifiedAt" });
db.getCollection("u_mes_perf_leakTestResult").createIndex({ wipUnitId: 1, testedAt: -1 }, { name: "ix_wipUnitId_testedAt" });
db.getCollection("u_mes_perf_leakTestResult").createIndex({ siteId: 1, sourceMessageUuid: 1 }, { name: "ux_siteId_sourceMessageUuid", unique: true, partialFilterExpression: { sourceMessageUuid: { $type: "string" } } });
