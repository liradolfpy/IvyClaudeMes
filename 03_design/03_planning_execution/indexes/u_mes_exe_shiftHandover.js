// Indexes for u_mes_exe_shiftHandover
db.getCollection("u_mes_exe_shiftHandover").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_exe_shiftHandover").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_exe_shiftHandover").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_exe_shiftHandover").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_exe_shiftHandover").createIndex({ outgoingSupervisorUserId: 1 }, { name: "ix_outgoingSupervisorUserId" });
db.getCollection("u_mes_exe_shiftHandover").createIndex({ incomingSupervisorUserId: 1 }, { name: "ix_incomingSupervisorUserId" });
db.getCollection("u_mes_exe_shiftHandover").createIndex({ siteId: 1, productionDate: -1 }, { name: "ix_siteId_productionDate" });
