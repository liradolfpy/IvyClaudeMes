// Indexes for u_mes_qual_scrapRecord
db.getCollection("u_mes_qual_scrapRecord").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_scrapRecord").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_scrapRecord").createIndex({ nonconformanceId: 1 }, { name: "ix_nonconformanceId" });
db.getCollection("u_mes_qual_scrapRecord").createIndex({ defectCodeId: 1 }, { name: "ix_defectCodeId" });
db.getCollection("u_mes_qual_scrapRecord").createIndex({ wipUnitId: 1 }, { name: "ix_wipUnitId" });
db.getCollection("u_mes_qual_scrapRecord").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_qual_scrapRecord").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qual_scrapRecord").createIndex({ siteId: 1, declaredAt: -1 }, { name: "ix_siteId_declaredAt" });
