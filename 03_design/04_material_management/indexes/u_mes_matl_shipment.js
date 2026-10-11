// Indexes for u_mes_matl_shipment
db.getCollection("u_mes_matl_shipment").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_matl_shipment").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_matl_shipment").createIndex({ customerId: 1 }, { name: "ix_customerId" });
db.getCollection("u_mes_matl_shipment").createIndex({ customerScheduleId: 1 }, { name: "ix_customerScheduleId" });
db.getCollection("u_mes_matl_shipment").createIndex({ transporterId: 1 }, { name: "ix_transporterId" });
db.getCollection("u_mes_matl_shipment").createIndex({ dockLocationId: 1 }, { name: "ix_dockLocationId" });
db.getCollection("u_mes_matl_shipment").createIndex({ siteId: 1, invoiceDate: -1 }, { name: "ix_siteId_invoiceDate" });
