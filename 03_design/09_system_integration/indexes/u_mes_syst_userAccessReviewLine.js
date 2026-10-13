// Indexes for u_mes_syst_userAccessReviewLine
db.getCollection("u_mes_syst_userAccessReviewLine").createIndex({ userAccessReviewId: 1, lineNo: 1 }, { name: "ux_userAccessReviewId_lineNo", unique: true });
db.getCollection("u_mes_syst_userAccessReviewLine").createIndex({ userId: 1 }, { name: "ix_userId" });
db.getCollection("u_mes_syst_userAccessReviewLine").createIndex({ roleId: 1 }, { name: "ix_roleId" });
