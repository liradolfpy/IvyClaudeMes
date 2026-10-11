// Indexes for u_mes_mast_supplierCertificate
db.getCollection("u_mes_mast_supplierCertificate").createIndex({ supplierId: 1, sequenceNo: 1 }, { name: "ux_supplierId_sequenceNo", unique: true });
