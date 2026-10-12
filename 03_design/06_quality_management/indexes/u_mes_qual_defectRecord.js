// Indexes for u_mes_qual_defectRecord
db.getCollection("u_mes_qual_defectRecord").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_defectRecord").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_defectRecord").createIndex({ defectCodeId: 1 }, { name: "ix_defectCodeId" });
db.getCollection("u_mes_qual_defectRecord").createIndex({ wipUnitId: 1 }, { name: "ix_wipUnitId" });
db.getCollection("u_mes_qual_defectRecord").createIndex({ serialNumberId: 1 }, { name: "ix_serialNumberId" });
db.getCollection("u_mes_qual_defectRecord").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_qual_defectRecord").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qual_defectRecord").createIndex({ siteId: 1, productionDate: -1 }, { name: "ix_siteId_productionDate" });
