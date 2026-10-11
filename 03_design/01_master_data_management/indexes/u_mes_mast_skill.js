// Indexes for u_mes_mast_skill
db.getCollection("u_mes_mast_skill").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mast_skill").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mast_skill").createIndex({ skillCategoryId: 1 }, { name: "ix_skillCategoryId" });
db.getCollection("u_mes_mast_skill").createIndex({ trainingControlledDocumentId: 1 }, { name: "ix_trainingControlledDocumentId" });
