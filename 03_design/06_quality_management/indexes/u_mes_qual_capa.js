// Indexes for u_mes_qual_capa
db.getCollection("u_mes_qual_capa").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_capa").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_capa").createIndex({ customerComplaintId: 1 }, { name: "ix_customerComplaintId" });
db.getCollection("u_mes_qual_capa").createIndex({ auditId: 1 }, { name: "ix_auditId" });
db.getCollection("u_mes_qual_capa").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qual_capa").createIndex({ customerId: 1 }, { name: "ix_customerId" });
db.getCollection("u_mes_qual_capa").createIndex({ d7PreventionPfmeaId: 1 }, { name: "ix_d7PreventionPfmeaId" });
db.getCollection("u_mes_qual_capa").createIndex({ siteId: 1, openedAt: -1 }, { name: "ix_siteId_openedAt" });
