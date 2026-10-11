// Indexes for u_mes_matl_goodsReceipt
db.getCollection("u_mes_matl_goodsReceipt").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_matl_goodsReceipt").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_matl_goodsReceipt").createIndex({ supplierId: 1 }, { name: "ix_supplierId" });
db.getCollection("u_mes_matl_goodsReceipt").createIndex({ siteId: 1, supplierInvoiceDate: -1 }, { name: "ix_siteId_supplierInvoiceDate" });
