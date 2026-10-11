// Indexes for u_mes_prod_routingStep
db.getCollection("u_mes_prod_routingStep").createIndex({ routingId: 1, stepNo: 1 }, { name: "ux_routingId_stepNo", unique: true });
db.getCollection("u_mes_prod_routingStep").createIndex({ operationId: 1 }, { name: "ix_operationId" });
db.getCollection("u_mes_prod_routingStep").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
