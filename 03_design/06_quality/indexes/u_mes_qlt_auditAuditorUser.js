// Indexes for u_mes_qlt_auditAuditorUser
db.getCollection("u_mes_qlt_auditAuditorUser").createIndex({ auditId: 1, auditorUserId: 1 }, { name: "ux_auditId_auditorUserId", unique: true });
db.getCollection("u_mes_qlt_auditAuditorUser").createIndex({ auditorUserId: 1, auditId: 1 }, { name: "ix_auditorUserId_auditId" });
