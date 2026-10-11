// Indexes for u_mes_qlt_reworkOrderWipUnit
db.getCollection("u_mes_qlt_reworkOrderWipUnit").createIndex({ reworkOrderId: 1, wipUnitId: 1 }, { name: "ux_reworkOrderId_wipUnitId", unique: true });
db.getCollection("u_mes_qlt_reworkOrderWipUnit").createIndex({ wipUnitId: 1, reworkOrderId: 1 }, { name: "ix_wipUnitId_reworkOrderId" });
