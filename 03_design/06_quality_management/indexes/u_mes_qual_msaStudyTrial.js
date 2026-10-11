// Indexes for u_mes_qual_msaStudyTrial
db.getCollection("u_mes_qual_msaStudyTrial").createIndex({ msaStudyId: 1, appraiserUserId: 1, partNo: 1, trialNo: 1 }, { name: "ux_msaStudyId_appraiserUserId_partNo_trialNo", unique: true });
db.getCollection("u_mes_qual_msaStudyTrial").createIndex({ appraiserUserId: 1 }, { name: "ix_appraiserUserId" });
