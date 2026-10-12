// Indexes for u_mes_trac_traceInvestigationResult
db.getCollection("u_mes_trac_traceInvestigationResult").createIndex({ traceInvestigationId: 1, sequenceNo: 1 }, { name: "ux_traceInvestigationId_sequenceNo", unique: true });
db.getCollection("u_mes_trac_traceInvestigationResult").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_trac_traceInvestigationResult").createIndex({ storageLocationId: 1 }, { name: "ix_storageLocationId" });
db.getCollection("u_mes_trac_traceInvestigationResult").createIndex({ shipmentId: 1 }, { name: "ix_shipmentId" });
