// Indexes for u_mes_syst_operatorApp
db.getCollection("u_mes_syst_operatorApp").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_operatorApp").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_operatorApp").createIndex({ previousVersionOperatorAppId: 1 }, { name: "ix_previousVersionOperatorAppId" });
