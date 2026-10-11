// Indexes for u_mes_mast_lineIdealRate
db.getCollection("u_mes_mast_lineIdealRate").createIndex({ lineId: 1, sequenceNo: 1 }, { name: "ux_lineId_sequenceNo", unique: true });
db.getCollection("u_mes_mast_lineIdealRate").createIndex({ itemId: 1 }, { name: "ix_itemId" });
