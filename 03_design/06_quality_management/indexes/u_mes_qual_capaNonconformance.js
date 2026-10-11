// Indexes for u_mes_qual_capaNonconformance
db.getCollection("u_mes_qual_capaNonconformance").createIndex({ capaId: 1, nonconformanceId: 1 }, { name: "ux_capaId_nonconformanceId", unique: true });
db.getCollection("u_mes_qual_capaNonconformance").createIndex({ nonconformanceId: 1, capaId: 1 }, { name: "ix_nonconformanceId_capaId" });
