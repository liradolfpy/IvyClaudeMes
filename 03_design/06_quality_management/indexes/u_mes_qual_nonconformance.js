// Indexes for u_mes_qual_nonconformance
db.getCollection("u_mes_qual_nonconformance").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_nonconformance").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_nonconformance").createIndex({ detectedAtOperationId: 1 }, { name: "ix_detectedAtOperationId" });
db.getCollection("u_mes_qual_nonconformance").createIndex({ detectedAtWorkCenterId: 1 }, { name: "ix_detectedAtWorkCenterId" });
db.getCollection("u_mes_qual_nonconformance").createIndex({ originOperationId: 1 }, { name: "ix_originOperationId" });
db.getCollection("u_mes_qual_nonconformance").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qual_nonconformance").createIndex({ defectCodeId: 1 }, { name: "ix_defectCodeId" });
db.getCollection("u_mes_qual_nonconformance").createIndex({ siteId: 1, detectedAt: -1 }, { name: "ix_siteId_detectedAt" });
