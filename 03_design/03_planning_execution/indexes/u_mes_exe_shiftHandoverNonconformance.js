// Indexes for u_mes_exe_shiftHandoverNonconformance
db.getCollection("u_mes_exe_shiftHandoverNonconformance").createIndex({ shiftHandoverId: 1, nonconformanceId: 1 }, { name: "ux_shiftHandoverId_nonconformanceId", unique: true });
db.getCollection("u_mes_exe_shiftHandoverNonconformance").createIndex({ nonconformanceId: 1, shiftHandoverId: 1 }, { name: "ix_nonconformanceId_shiftHandoverId" });
