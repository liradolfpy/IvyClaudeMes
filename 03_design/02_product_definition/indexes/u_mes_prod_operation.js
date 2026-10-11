// Indexes for u_mes_prod_operation
db.getCollection("u_mes_prod_operation").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_prod_operation").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_prod_operation").createIndex({ defaultWorkCenterId: 1 }, { name: "ix_defaultWorkCenterId" });
