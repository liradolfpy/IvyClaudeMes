// Indexes for u_mes_qlt_qualityHoldHeldObject
db.getCollection("u_mes_qlt_qualityHoldHeldObject").createIndex({ qualityHoldId: 1, sequenceNo: 1 }, { name: "ux_qualityHoldId_sequenceNo", unique: true });
