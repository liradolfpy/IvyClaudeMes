// Indexes for u_mes_qual_capaCorrectiveAction
db.getCollection("u_mes_qual_capaCorrectiveAction").createIndex({ capaId: 1, sequenceNo: 1 }, { name: "ux_capaId_sequenceNo", unique: true });
db.getCollection("u_mes_qual_capaCorrectiveAction").createIndex({ ownerUserId: 1 }, { name: "ix_ownerUserId" });
