// Indexes for u_mes_qlt_auditFinding
db.getCollection("u_mes_qlt_auditFinding").createIndex({ auditId: 1, findingNo: 1 }, { name: "ux_auditId_findingNo", unique: true });
db.getCollection("u_mes_qlt_auditFinding").createIndex({ ownerUserId: 1 }, { name: "ix_ownerUserId" });
db.getCollection("u_mes_qlt_auditFinding").createIndex({ capaId: 1 }, { name: "ix_capaId" });
