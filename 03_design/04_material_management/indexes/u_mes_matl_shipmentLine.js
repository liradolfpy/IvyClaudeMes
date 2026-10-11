// Indexes for u_mes_matl_shipmentLine
db.getCollection("u_mes_matl_shipmentLine").createIndex({ shipmentId: 1, lineNo: 1 }, { name: "ux_shipmentId_lineNo", unique: true });
db.getCollection("u_mes_matl_shipmentLine").createIndex({ itemId: 1 }, { name: "ix_itemId" });
