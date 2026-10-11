// Indexes for u_mes_mat_goodsReceiptLine
db.getCollection("u_mes_mat_goodsReceiptLine").createIndex({ goodsReceiptId: 1, lineNo: 1 }, { name: "ux_goodsReceiptId_lineNo", unique: true });
db.getCollection("u_mes_mat_goodsReceiptLine").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_mat_goodsReceiptLine").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_mat_goodsReceiptLine").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
