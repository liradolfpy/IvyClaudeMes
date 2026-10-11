// Indexes for u_mes_qual_ppapSubmissionElement
db.getCollection("u_mes_qual_ppapSubmissionElement").createIndex({ ppapSubmissionId: 1, elementNo: 1 }, { name: "ux_ppapSubmissionId_elementNo", unique: true });
db.getCollection("u_mes_qual_ppapSubmissionElement").createIndex({ controlledDocumentId: 1 }, { name: "ix_controlledDocumentId" });
