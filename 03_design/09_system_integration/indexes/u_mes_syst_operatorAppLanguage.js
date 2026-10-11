// Indexes for u_mes_syst_operatorAppLanguage
db.getCollection("u_mes_syst_operatorAppLanguage").createIndex({ operatorAppId: 1, languageId: 1 }, { name: "ux_operatorAppId_languageId", unique: true });
db.getCollection("u_mes_syst_operatorAppLanguage").createIndex({ languageId: 1, operatorAppId: 1 }, { name: "ix_languageId_operatorAppId" });
