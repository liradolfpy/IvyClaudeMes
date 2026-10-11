// Indexes for u_mes_mdm_supplier
db.getCollection("u_mes_mdm_supplier").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mdm_supplier").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mdm_supplier").createIndex({ commodityId: 1 }, { name: "ix_commodityId" });
db.getCollection("u_mes_mdm_supplier").createIndex({ addressCountryId: 1 }, { name: "ix_addressCountryId" });
db.getCollection("u_mes_mdm_supplier").createIndex({ currencyId: 1 }, { name: "ix_currencyId" });
