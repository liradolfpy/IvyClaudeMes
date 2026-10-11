// Indexes for u_mes_qual_deviationPermitApproval
db.getCollection("u_mes_qual_deviationPermitApproval").createIndex({ deviationPermitId: 1, sequenceNo: 1 }, { name: "ux_deviationPermitId_sequenceNo", unique: true });
db.getCollection("u_mes_qual_deviationPermitApproval").createIndex({ userId: 1 }, { name: "ix_userId" });
