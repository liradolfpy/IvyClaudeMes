// Indexes for u_mes_mast_supplierContact
db.getCollection("u_mes_mast_supplierContact").createIndex({ supplierId: 1, sequenceNo: 1 }, { name: "ux_supplierId_sequenceNo", unique: true });
