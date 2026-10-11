// Indexes for u_mes_qlt_samplingPlanSizeRow
db.getCollection("u_mes_qlt_samplingPlanSizeRow").createIndex({ samplingPlanId: 1, lotSizeFrom: 1 }, { name: "ux_samplingPlanId_lotSizeFrom", unique: true });
