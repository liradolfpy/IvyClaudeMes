// Indexes for u_mes_matl_goodsReceiptLineInspectionResult
db.getCollection("u_mes_matl_goodsReceiptLineInspectionResult").createIndex({ goodsReceiptLineId: 1, inspectionResultId: 1 }, { name: "ux_goodsReceiptLineId_inspectionResultId", unique: true });
db.getCollection("u_mes_matl_goodsReceiptLineInspectionResult").createIndex({ inspectionResultId: 1, goodsReceiptLineId: 1 }, { name: "ix_inspectionResultId_goodsReceiptLineId" });
