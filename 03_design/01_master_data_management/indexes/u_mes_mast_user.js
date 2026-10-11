// Indexes for u_mes_mast_user
db.getCollection("u_mes_mast_user").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mast_user").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mast_user").createIndex({ departmentId: 1 }, { name: "ix_departmentId" });
db.getCollection("u_mes_mast_user").createIndex({ designationId: 1 }, { name: "ix_designationId" });
db.getCollection("u_mes_mast_user").createIndex({ defaultShiftId: 1 }, { name: "ix_defaultShiftId" });
db.getCollection("u_mes_mast_user").createIndex({ homeWorkCenterId: 1 }, { name: "ix_homeWorkCenterId" });
db.getCollection("u_mes_mast_user").createIndex({ reportsToUserId: 1 }, { name: "ix_reportsToUserId" });
db.getCollection("u_mes_mast_user").createIndex({ userName: 1 }, { name: "ux_userName", unique: true });
db.getCollection("u_mes_mast_user").createIndex({ badgeNo: 1 }, { name: "ux_badgeNo", unique: true });
