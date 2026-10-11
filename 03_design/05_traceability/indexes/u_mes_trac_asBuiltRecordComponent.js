// Indexes for u_mes_trac_asBuiltRecordComponent
db.getCollection("u_mes_trac_asBuiltRecordComponent").createIndex({ asBuiltRecordId: 1, sequenceNo: 1 }, { name: "ux_asBuiltRecordId_sequenceNo", unique: true });
db.getCollection("u_mes_trac_asBuiltRecordComponent").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_trac_asBuiltRecordComponent").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_trac_asBuiltRecordComponent").createIndex({ genealogyLinkId: 1 }, { name: "ix_genealogyLinkId" });
