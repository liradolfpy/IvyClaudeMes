// Indexes for u_mes_mdm_designation
db.getCollection("u_mes_mdm_designation").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mdm_designation").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mdm_designation").createIndex({ departmentId: 1 }, { name: "ix_departmentId" });
