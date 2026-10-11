// Indexes for u_mes_prod_billOfProcessStepTool
db.getCollection("u_mes_prod_billOfProcessStepTool").createIndex({ billOfProcessStepId: 1, toolId: 1 }, { name: "ux_billOfProcessStepId_toolId", unique: true });
db.getCollection("u_mes_prod_billOfProcessStepTool").createIndex({ toolId: 1, billOfProcessStepId: 1 }, { name: "ix_toolId_billOfProcessStepId" });
