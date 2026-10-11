// Indexes for u_mes_matl_shipmentLineLot
db.getCollection("u_mes_matl_shipmentLineLot").createIndex({ shipmentLineId: 1, lotId: 1 }, { name: "ux_shipmentLineId_lotId", unique: true });
db.getCollection("u_mes_matl_shipmentLineLot").createIndex({ lotId: 1, shipmentLineId: 1 }, { name: "ix_lotId_shipmentLineId" });
