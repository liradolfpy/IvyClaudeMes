// Indexes for u_mes_qual_productRecallLot
db.getCollection("u_mes_qual_productRecallLot").createIndex({ productRecallId: 1, lineNo: 1 }, { name: "ux_productRecallId_lineNo", unique: true });
db.getCollection("u_mes_qual_productRecallLot").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_qual_productRecallLot").createIndex({ shipmentId: 1 }, { name: "ix_shipmentId" });
