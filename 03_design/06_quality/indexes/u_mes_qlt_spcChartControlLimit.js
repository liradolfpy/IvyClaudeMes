// Indexes for u_mes_qlt_spcChartControlLimit
db.getCollection("u_mes_qlt_spcChartControlLimit").createIndex({ spcChartId: 1, revisionNo: 1 }, { name: "ux_spcChartId_revisionNo", unique: true });
