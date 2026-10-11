// Indexes for u_mes_prod_recipe
db.getCollection("u_mes_prod_recipe").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_prod_recipe").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_prod_recipe").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_prod_recipe").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_prod_recipe").createIndex({ operationId: 1 }, { name: "ix_operationId" });
db.getCollection("u_mes_prod_recipe").createIndex({ engineeringChangeId: 1 }, { name: "ix_engineeringChangeId" });
