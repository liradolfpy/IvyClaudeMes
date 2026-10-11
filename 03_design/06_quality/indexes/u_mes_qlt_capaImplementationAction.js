// Indexes for u_mes_qlt_capaImplementationAction
db.getCollection("u_mes_qlt_capaImplementationAction").createIndex({ capaId: 1, sequenceNo: 1 }, { name: "ux_capaId_sequenceNo", unique: true });
