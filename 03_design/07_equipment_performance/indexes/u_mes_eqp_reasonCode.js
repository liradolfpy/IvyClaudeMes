// Indexes for u_mes_eqp_reasonCode
db.getCollection("u_mes_eqp_reasonCode").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_eqp_reasonCode").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_eqp_reasonCode").createIndex({ parentReasonCodeId: 1 }, { name: "ix_parentReasonCodeId" });
db.getCollection("u_mes_eqp_reasonCode").createIndex({ reasonCategoryId: 1 }, { name: "ix_reasonCategoryId" });
db.getCollection("u_mes_eqp_reasonCode").createIndex({ lossCategoryId: 1 }, { name: "ix_lossCategoryId" });
db.getCollection("u_mes_eqp_reasonCode").createIndex({ responsibleDepartmentId: 1 }, { name: "ix_responsibleDepartmentId" });
