// Indexes for u_mes_syst_operatorAppStepTrigger
db.getCollection("u_mes_syst_operatorAppStepTrigger").createIndex({ operatorAppStepId: 1, sequenceNo: 1 }, { name: "ux_operatorAppStepId_sequenceNo", unique: true });
