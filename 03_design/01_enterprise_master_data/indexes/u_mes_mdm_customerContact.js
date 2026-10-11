// Indexes for u_mes_mdm_customerContact
db.getCollection("u_mes_mdm_customerContact").createIndex({ customerId: 1, sequenceNo: 1 }, { name: "ux_customerId_sequenceNo", unique: true });
