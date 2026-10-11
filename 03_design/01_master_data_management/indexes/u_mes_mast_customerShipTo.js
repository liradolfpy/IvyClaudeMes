// Indexes for u_mes_mast_customerShipTo
db.getCollection("u_mes_mast_customerShipTo").createIndex({ customerId: 1, sequenceNo: 1 }, { name: "ux_customerId_sequenceNo", unique: true });
