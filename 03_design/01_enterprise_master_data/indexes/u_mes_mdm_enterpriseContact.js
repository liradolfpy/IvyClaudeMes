// Indexes for u_mes_mdm_enterpriseContact
db.getCollection("u_mes_mdm_enterpriseContact").createIndex({ enterpriseId: 1, sequenceNo: 1 }, { name: "ux_enterpriseId_sequenceNo", unique: true });
