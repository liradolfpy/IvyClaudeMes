// Indexes for u_mes_qlt_reworkOrder
db.getCollection("u_mes_qlt_reworkOrder").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qlt_reworkOrder").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qlt_reworkOrder").createIndex({ nonconformanceId: 1 }, { name: "ix_nonconformanceId" });
db.getCollection("u_mes_qlt_reworkOrder").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_qlt_reworkOrder").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qlt_reworkOrder").createIndex({ reworkRoutingId: 1 }, { name: "ix_reworkRoutingId" });
db.getCollection("u_mes_qlt_reworkOrder").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_qlt_reworkOrder").createIndex({ siteId: 1, issuedAt: -1 }, { name: "ix_siteId_issuedAt" });
