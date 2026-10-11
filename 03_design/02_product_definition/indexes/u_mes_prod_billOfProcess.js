// Indexes for u_mes_prod_billOfProcess
db.getCollection("u_mes_prod_billOfProcess").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_prod_billOfProcess").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_prod_billOfProcess").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_prod_billOfProcess").createIndex({ routingId: 1 }, { name: "ix_routingId" });
db.getCollection("u_mes_prod_billOfProcess").createIndex({ billOfMaterialId: 1 }, { name: "ix_billOfMaterialId" });
