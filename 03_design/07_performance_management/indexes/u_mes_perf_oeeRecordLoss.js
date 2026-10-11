// Indexes for u_mes_perf_oeeRecordLoss
db.getCollection("u_mes_perf_oeeRecordLoss").createIndex({ oeeRecordId: 1, sequenceNo: 1 }, { name: "ux_oeeRecordId_sequenceNo", unique: true });
db.getCollection("u_mes_perf_oeeRecordLoss").createIndex({ lossCategoryId: 1 }, { name: "ix_lossCategoryId" });
db.getCollection("u_mes_perf_oeeRecordLoss").createIndex({ reasonCodeId: 1 }, { name: "ix_reasonCodeId" });
