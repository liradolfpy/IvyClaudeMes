// Indexes for u_mes_qual_deviationPermit
db.getCollection("u_mes_qual_deviationPermit").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_deviationPermit").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_deviationPermit").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qual_deviationPermit").createIndex({ characteristicId: 1 }, { name: "ix_characteristicId" });
db.getCollection("u_mes_qual_deviationPermit").createIndex({ customerId: 1 }, { name: "ix_customerId" });
db.getCollection("u_mes_qual_deviationPermit").createIndex({ nonconformanceId: 1 }, { name: "ix_nonconformanceId" });
db.getCollection("u_mes_qual_deviationPermit").createIndex({ engineeringChangeId: 1 }, { name: "ix_engineeringChangeId" });
db.getCollection("u_mes_qual_deviationPermit").createIndex({ siteId: 1, validFrom: -1 }, { name: "ix_siteId_validFrom" });
