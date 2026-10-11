// Indexes for u_mes_mast_unitOfMeasure
db.getCollection("u_mes_mast_unitOfMeasure").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mast_unitOfMeasure").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mast_unitOfMeasure").createIndex({ baseUnitOfMeasureId: 1 }, { name: "ix_baseUnitOfMeasureId" });
