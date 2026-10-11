// Indexes for u_mes_qual_capaTeamMember
db.getCollection("u_mes_qual_capaTeamMember").createIndex({ capaId: 1, sequenceNo: 1 }, { name: "ux_capaId_sequenceNo", unique: true });
db.getCollection("u_mes_qual_capaTeamMember").createIndex({ userId: 1 }, { name: "ix_userId" });
