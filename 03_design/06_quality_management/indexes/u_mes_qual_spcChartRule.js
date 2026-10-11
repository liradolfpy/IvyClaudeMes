// Indexes for u_mes_qual_spcChartRule
db.getCollection("u_mes_qual_spcChartRule").createIndex({ spcChartId: 1, sequenceNo: 1 }, { name: "ux_spcChartId_sequenceNo", unique: true });
