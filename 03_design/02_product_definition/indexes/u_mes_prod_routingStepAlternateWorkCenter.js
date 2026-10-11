// Indexes for u_mes_prod_routingStepAlternateWorkCenter
db.getCollection("u_mes_prod_routingStepAlternateWorkCenter").createIndex({ routingStepId: 1, alternateWorkCenterId: 1 }, { name: "ux_routingStepId_alternateWorkCenterId", unique: true });
db.getCollection("u_mes_prod_routingStepAlternateWorkCenter").createIndex({ alternateWorkCenterId: 1, routingStepId: 1 }, { name: "ix_alternateWorkCenterId_routingStepId" });
