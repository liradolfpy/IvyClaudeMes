// Indexes for u_mes_prod_billOfProcessStep
db.getCollection("u_mes_prod_billOfProcessStep").createIndex({ billOfProcessId: 1, stepNo: 1 }, { name: "ux_billOfProcessId_stepNo", unique: true });
db.getCollection("u_mes_prod_billOfProcessStep").createIndex({ operationId: 1 }, { name: "ix_operationId" });
db.getCollection("u_mes_prod_billOfProcessStep").createIndex({ recipeId: 1 }, { name: "ix_recipeId" });
db.getCollection("u_mes_prod_billOfProcessStep").createIndex({ workInstructionId: 1 }, { name: "ix_workInstructionId" });
