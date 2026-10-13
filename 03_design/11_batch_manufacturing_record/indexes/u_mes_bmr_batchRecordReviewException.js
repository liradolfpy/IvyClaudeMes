// Indexes for u_mes_bmr_batchRecordReviewException
db.getCollection("u_mes_bmr_batchRecordReviewException").createIndex({ batchRecordReviewId: 1, lineNo: 1 }, { name: "ux_batchRecordReviewId_lineNo", unique: true });
