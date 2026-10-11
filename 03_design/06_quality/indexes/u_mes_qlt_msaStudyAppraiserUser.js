// Indexes for u_mes_qlt_msaStudyAppraiserUser
db.getCollection("u_mes_qlt_msaStudyAppraiserUser").createIndex({ msaStudyId: 1, appraiserUserId: 1 }, { name: "ux_msaStudyId_appraiserUserId", unique: true });
db.getCollection("u_mes_qlt_msaStudyAppraiserUser").createIndex({ appraiserUserId: 1, msaStudyId: 1 }, { name: "ix_appraiserUserId_msaStudyId" });
