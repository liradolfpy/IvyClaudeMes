// Indexes for u_mes_qual_nonconformanceMrbUser
db.getCollection("u_mes_qual_nonconformanceMrbUser").createIndex({ nonconformanceId: 1, mrbUserId: 1 }, { name: "ux_nonconformanceId_mrbUserId", unique: true });
db.getCollection("u_mes_qual_nonconformanceMrbUser").createIndex({ mrbUserId: 1, nonconformanceId: 1 }, { name: "ix_mrbUserId_nonconformanceId" });
