// Indexes for u_mes_eqp_torqueResult
db.getCollection("u_mes_eqp_torqueResult").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_eqp_torqueResult").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_eqp_torqueResult").createIndex({ wipUnitId: 1 }, { name: "ix_wipUnitId" });
db.getCollection("u_mes_eqp_torqueResult").createIndex({ operationExecutionId: 1 }, { name: "ix_operationExecutionId" });
db.getCollection("u_mes_eqp_torqueResult").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_eqp_torqueResult").createIndex({ toolId: 1 }, { name: "ix_toolId" });
db.getCollection("u_mes_eqp_torqueResult").createIndex({ recipeId: 1 }, { name: "ix_recipeId" });
db.getCollection("u_mes_eqp_torqueResult").createIndex({ siteId: 1, tightenedAt: -1 }, { name: "ix_siteId_tightenedAt" });
db.getCollection("u_mes_eqp_torqueResult").createIndex({ wipUnitId: 1, tightenedAt: -1 }, { name: "ix_wipUnitId_tightenedAt" });
