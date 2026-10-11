// Indexes for u_mes_qual_defectCode
db.getCollection("u_mes_qual_defectCode").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_defectCode").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_defectCode").createIndex({ defectGroupId: 1 }, { name: "ix_defectGroupId" });
db.getCollection("u_mes_qual_defectCode").createIndex({ defaultDispositionTypeId: 1 }, { name: "ix_defaultDispositionTypeId" });
db.getCollection("u_mes_qual_defectCode").createIndex({ dispositionRoutingId: 1 }, { name: "ix_dispositionRoutingId" });
