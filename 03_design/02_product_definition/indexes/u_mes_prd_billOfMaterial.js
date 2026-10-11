// Indexes for u_mes_prd_billOfMaterial
db.getCollection("u_mes_prd_billOfMaterial").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_prd_billOfMaterial").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_prd_billOfMaterial").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_prd_billOfMaterial").createIndex({ baseUnitOfMeasureId: 1 }, { name: "ix_baseUnitOfMeasureId" });
db.getCollection("u_mes_prd_billOfMaterial").createIndex({ engineeringChangeId: 1 }, { name: "ix_engineeringChangeId" });
