// Indexes for u_mes_qual_samplingPlanSizeRow
db.getCollection("u_mes_qual_samplingPlanSizeRow").createIndex({ samplingPlanId: 1, lotSizeFrom: 1 }, { name: "ux_samplingPlanId_lotSizeFrom", unique: true });
