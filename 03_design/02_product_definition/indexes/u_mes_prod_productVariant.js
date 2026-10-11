// Indexes for u_mes_prod_productVariant
db.getCollection("u_mes_prod_productVariant").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_prod_productVariant").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_prod_productVariant").createIndex({ baseItemId: 1 }, { name: "ix_baseItemId" });
db.getCollection("u_mes_prod_productVariant").createIndex({ variantItemId: 1 }, { name: "ix_variantItemId" });
db.getCollection("u_mes_prod_productVariant").createIndex({ customerId: 1 }, { name: "ix_customerId" });
db.getCollection("u_mes_prod_productVariant").createIndex({ optionsPadCompoundId: 1 }, { name: "ix_optionsPadCompoundId" });
db.getCollection("u_mes_prod_productVariant").createIndex({ optionsMarketId: 1 }, { name: "ix_optionsMarketId" });
