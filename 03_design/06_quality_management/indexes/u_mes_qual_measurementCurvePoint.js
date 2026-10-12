// Indexes for u_mes_qual_measurementCurvePoint
db.getCollection("u_mes_qual_measurementCurvePoint").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_measurementCurvePoint").createIndex({ measurementCurveId: 1 }, { name: "ix_measurementCurveId" });
db.getCollection("u_mes_qual_measurementCurvePoint").createIndex({ siteId: 1, sampledAt: -1 }, { name: "ix_siteId_sampledAt" });
