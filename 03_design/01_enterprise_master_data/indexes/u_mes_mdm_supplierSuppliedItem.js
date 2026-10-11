// Indexes for u_mes_mdm_supplierSuppliedItem
db.getCollection("u_mes_mdm_supplierSuppliedItem").createIndex({ supplierId: 1, suppliedItemId: 1 }, { name: "ux_supplierId_suppliedItemId", unique: true });
db.getCollection("u_mes_mdm_supplierSuppliedItem").createIndex({ suppliedItemId: 1, supplierId: 1 }, { name: "ix_suppliedItemId_supplierId" });
