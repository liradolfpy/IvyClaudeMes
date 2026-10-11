// Indexes for u_mes_qlt_controlPlan
db.getCollection("u_mes_qlt_controlPlan").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qlt_controlPlan").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qlt_controlPlan").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qlt_controlPlan").createIndex({ routingId: 1 }, { name: "ix_routingId" });
db.getCollection("u_mes_qlt_controlPlan").createIndex({ pfmeaId: 1 }, { name: "ix_pfmeaId" });
db.getCollection("u_mes_qlt_controlPlan").createIndex({ engineeringChangeId: 1 }, { name: "ix_engineeringChangeId" });
