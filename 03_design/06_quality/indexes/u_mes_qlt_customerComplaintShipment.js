// Indexes for u_mes_qlt_customerComplaintShipment
db.getCollection("u_mes_qlt_customerComplaintShipment").createIndex({ customerComplaintId: 1, shipmentId: 1 }, { name: "ux_customerComplaintId_shipmentId", unique: true });
db.getCollection("u_mes_qlt_customerComplaintShipment").createIndex({ shipmentId: 1, customerComplaintId: 1 }, { name: "ix_shipmentId_customerComplaintId" });
