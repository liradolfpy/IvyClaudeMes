// Indexes for u_mes_mast_customer
db.getCollection("u_mes_mast_customer").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mast_customer").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mast_customer").createIndex({ billingAddressCountryId: 1 }, { name: "ix_billingAddressCountryId" });
db.getCollection("u_mes_mast_customer").createIndex({ labelTemplateId: 1 }, { name: "ix_labelTemplateId" });
db.getCollection("u_mes_mast_customer").createIndex({ currencyId: 1 }, { name: "ix_currencyId" });
