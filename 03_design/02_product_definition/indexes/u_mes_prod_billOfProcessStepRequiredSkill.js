// Indexes for u_mes_prod_billOfProcessStepRequiredSkill
db.getCollection("u_mes_prod_billOfProcessStepRequiredSkill").createIndex({ billOfProcessStepId: 1, requiredSkillId: 1 }, { name: "ux_billOfProcessStepId_requiredSkillId", unique: true });
db.getCollection("u_mes_prod_billOfProcessStepRequiredSkill").createIndex({ requiredSkillId: 1, billOfProcessStepId: 1 }, { name: "ix_requiredSkillId_billOfProcessStepId" });
