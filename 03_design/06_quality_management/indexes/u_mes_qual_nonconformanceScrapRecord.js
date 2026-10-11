// Indexes for u_mes_qual_nonconformanceScrapRecord
db.getCollection("u_mes_qual_nonconformanceScrapRecord").createIndex({ nonconformanceId: 1, scrapRecordId: 1 }, { name: "ux_nonconformanceId_scrapRecordId", unique: true });
db.getCollection("u_mes_qual_nonconformanceScrapRecord").createIndex({ scrapRecordId: 1, nonconformanceId: 1 }, { name: "ix_scrapRecordId_nonconformanceId" });
