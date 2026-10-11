// Indexes for u_mes_qual_qualityHoldHeldObject
db.getCollection("u_mes_qual_qualityHoldHeldObject").createIndex({ qualityHoldId: 1, sequenceNo: 1 }, { name: "ux_qualityHoldId_sequenceNo", unique: true });
