// Indexes for u_mes_prod_routing
db.getCollection("u_mes_prod_routing").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_prod_routing").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_prod_routing").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_prod_routing").createIndex({ engineeringChangeId: 1 }, { name: "ix_engineeringChangeId" });
db.getCollection("u_mes_prod_routing").createIndex({ parentRoutingId: 1 }, { name: "ix_parentRoutingId" });
