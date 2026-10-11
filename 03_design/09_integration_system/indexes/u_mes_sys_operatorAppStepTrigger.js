// Indexes for u_mes_sys_operatorAppStepTrigger
db.getCollection("u_mes_sys_operatorAppStepTrigger").createIndex({ operatorAppStepId: 1, sequenceNo: 1 }, { name: "ux_operatorAppStepId_sequenceNo", unique: true });
