// Indexes for u_mes_prod_routingStepNextStep
db.getCollection("u_mes_prod_routingStepNextStep").createIndex({ routingStepId: 1, stepNo: 1 }, { name: "ux_routingStepId_stepNo", unique: true });
