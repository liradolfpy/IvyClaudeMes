// Indexes for u_mes_mast_enterprise
db.getCollection("u_mes_mast_enterprise").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mast_enterprise").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mast_enterprise").createIndex({ parentEnterpriseId: 1 }, { name: "ix_parentEnterpriseId" });
db.getCollection("u_mes_mast_enterprise").createIndex({ registeredAddressCountryId: 1 }, { name: "ix_registeredAddressCountryId" });
db.getCollection("u_mes_mast_enterprise").createIndex({ baseCurrencyId: 1 }, { name: "ix_baseCurrencyId" });
