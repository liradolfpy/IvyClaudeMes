// Indexes for u_mes_qlt_nonconformanceContainmentAction
db.getCollection("u_mes_qlt_nonconformanceContainmentAction").createIndex({ nonconformanceId: 1, actionNo: 1 }, { name: "ux_nonconformanceId_actionNo", unique: true });
db.getCollection("u_mes_qlt_nonconformanceContainmentAction").createIndex({ ownerUserId: 1 }, { name: "ix_ownerUserId" });
