// Indexes for u_mes_qlt_nonconformanceReworkOrder
db.getCollection("u_mes_qlt_nonconformanceReworkOrder").createIndex({ nonconformanceId: 1, reworkOrderId: 1 }, { name: "ux_nonconformanceId_reworkOrderId", unique: true });
db.getCollection("u_mes_qlt_nonconformanceReworkOrder").createIndex({ reworkOrderId: 1, nonconformanceId: 1 }, { name: "ix_reworkOrderId_nonconformanceId" });
