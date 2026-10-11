// Indexes for u_mes_matl_shipmentLineContainer
db.getCollection("u_mes_matl_shipmentLineContainer").createIndex({ shipmentLineId: 1, containerId: 1 }, { name: "ux_shipmentLineId_containerId", unique: true });
db.getCollection("u_mes_matl_shipmentLineContainer").createIndex({ containerId: 1, shipmentLineId: 1 }, { name: "ix_containerId_shipmentLineId" });
