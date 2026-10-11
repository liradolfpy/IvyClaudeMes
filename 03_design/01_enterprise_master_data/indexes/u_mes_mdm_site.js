// Indexes for u_mes_mdm_site
db.getCollection("u_mes_mdm_site").createIndex({ recordNo: 1 }, { name: "ux_recordNo", unique: true });
db.getCollection("u_mes_mdm_site").createIndex({ status: 1 }, { name: "ix_status" });
db.getCollection("u_mes_mdm_site").createIndex({ enterpriseId: 1 }, { name: "ix_enterpriseId" });
db.getCollection("u_mes_mdm_site").createIndex({ addressCountryId: 1 }, { name: "ix_addressCountryId" });
db.getCollection("u_mes_mdm_site").createIndex({ defaultWorkCalendarId: 1 }, { name: "ix_defaultWorkCalendarId" });
db.getCollection("u_mes_mdm_site").createIndex({ currencyId: 1 }, { name: "ix_currencyId" });
db.getCollection("u_mes_mdm_site").createIndex({ languageId: 1 }, { name: "ix_languageId" });
