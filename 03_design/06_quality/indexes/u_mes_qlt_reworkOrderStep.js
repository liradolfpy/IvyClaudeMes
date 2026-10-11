// Indexes for u_mes_qlt_reworkOrderStep
db.getCollection("u_mes_qlt_reworkOrderStep").createIndex({ reworkOrderId: 1, stepNo: 1 }, { name: "ux_reworkOrderId_stepNo", unique: true });
db.getCollection("u_mes_qlt_reworkOrderStep").createIndex({ operationId: 1 }, { name: "ix_operationId" });
