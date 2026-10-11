// Indexes for u_mes_syst_statusDefinition
db.getCollection("u_mes_syst_statusDefinition").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_statusDefinition").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_statusDefinition").createIndex({ collectionName: 1, statusCode: 1 }, { name: "ux_collectionName_statusCode", unique: true });
