// Indexes for u_mes_mast_customerContact
db.getCollection("u_mes_mast_customerContact").createIndex({ customerId: 1, sequenceNo: 1 }, { name: "ux_customerId_sequenceNo", unique: true });
