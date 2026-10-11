// Indexes for u_mes_qlt_ppapSubmissionMsaStudy
db.getCollection("u_mes_qlt_ppapSubmissionMsaStudy").createIndex({ ppapSubmissionId: 1, msaStudyId: 1 }, { name: "ux_ppapSubmissionId_msaStudyId", unique: true });
db.getCollection("u_mes_qlt_ppapSubmissionMsaStudy").createIndex({ msaStudyId: 1, ppapSubmissionId: 1 }, { name: "ix_msaStudyId_ppapSubmissionId" });
