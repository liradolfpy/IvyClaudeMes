// Indexes for u_mes_prd_item
db.getCollection("u_mes_prd_item").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_prd_item").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_prd_item").createIndex({ itemGroupId: 1 }, { name: "ix_itemGroupId" });
db.getCollection("u_mes_prd_item").createIndex({ baseUnitOfMeasureId: 1 }, { name: "ix_baseUnitOfMeasureId" });
db.getCollection("u_mes_prd_item").createIndex({ defaultSupplierId: 1 }, { name: "ix_defaultSupplierId" });
db.getCollection("u_mes_prd_item").createIndex({ serialNumberRangeId: 1 }, { name: "ix_serialNumberRangeId" });
db.getCollection("u_mes_prd_item").createIndex({ lotNumberRangeId: 1 }, { name: "ix_lotNumberRangeId" });
