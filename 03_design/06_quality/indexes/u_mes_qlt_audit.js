// Indexes for u_mes_qlt_audit
db.getCollection("u_mes_qlt_audit").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qlt_audit").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qlt_audit").createIndex({ areaId: 1 }, { name: "ix_areaId" });
db.getCollection("u_mes_qlt_audit").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_qlt_audit").createIndex({ customerId: 1 }, { name: "ix_customerId" });
db.getCollection("u_mes_qlt_audit").createIndex({ leadAuditorUserId: 1 }, { name: "ix_leadAuditorUserId" });
db.getCollection("u_mes_qlt_audit").createIndex({ auditeeUserId: 1 }, { name: "ix_auditeeUserId" });
db.getCollection("u_mes_qlt_audit").createIndex({ siteId: 1, plannedDate: -1 }, { name: "ix_siteId_plannedDate" });
