// Indexes for u_mes_syst_operatorAppStep
db.getCollection("u_mes_syst_operatorAppStep").createIndex({ operatorAppId: 1, stepNo: 1 }, { name: "ux_operatorAppId_stepNo", unique: true });
db.getCollection("u_mes_syst_operatorAppStep").createIndex({ workInstructionId: 1 }, { name: "ix_workInstructionId" });
db.getCollection("u_mes_syst_operatorAppStep").createIndex({ inspectionPlanId: 1 }, { name: "ix_inspectionPlanId" });
