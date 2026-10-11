// Indexes for u_mes_mdm_supplierCertificate
db.getCollection("u_mes_mdm_supplierCertificate").createIndex({ supplierId: 1, sequenceNo: 1 }, { name: "ux_supplierId_sequenceNo", unique: true });
