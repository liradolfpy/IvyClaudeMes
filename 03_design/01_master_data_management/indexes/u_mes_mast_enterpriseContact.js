// Indexes for u_mes_mast_enterpriseContact
db.getCollection("u_mes_mast_enterpriseContact").createIndex({ enterpriseId: 1, sequenceNo: 1 }, { name: "ux_enterpriseId_sequenceNo", unique: true });
