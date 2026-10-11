// Indexes for u_mes_qlt_pfmea
db.getCollection("u_mes_qlt_pfmea").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qlt_pfmea").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qlt_pfmea").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qlt_pfmea").createIndex({ controlPlanId: 1 }, { name: "ix_controlPlanId" });
