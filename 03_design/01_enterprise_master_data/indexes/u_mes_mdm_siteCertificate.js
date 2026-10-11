// Indexes for u_mes_mdm_siteCertificate
db.getCollection("u_mes_mdm_siteCertificate").createIndex({ siteId: 1, sequenceNo: 1 }, { name: "ux_siteId_sequenceNo", unique: true });
