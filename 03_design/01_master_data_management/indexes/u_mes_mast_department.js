// Indexes for u_mes_mast_department
db.getCollection("u_mes_mast_department").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mast_department").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mast_department").createIndex({ parentDepartmentId: 1 }, { name: "ix_parentDepartmentId" });
db.getCollection("u_mes_mast_department").createIndex({ headUserId: 1 }, { name: "ix_headUserId" });
db.getCollection("u_mes_mast_department").createIndex({ costCenterId: 1 }, { name: "ix_costCenterId" });
