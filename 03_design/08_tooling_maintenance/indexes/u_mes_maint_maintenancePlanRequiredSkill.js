// Indexes for u_mes_maint_maintenancePlanRequiredSkill
db.getCollection("u_mes_maint_maintenancePlanRequiredSkill").createIndex({ maintenancePlanId: 1, requiredSkillId: 1 }, { name: "ux_maintenancePlanId_requiredSkillId", unique: true });
db.getCollection("u_mes_maint_maintenancePlanRequiredSkill").createIndex({ requiredSkillId: 1, maintenancePlanId: 1 }, { name: "ix_requiredSkillId_maintenancePlanId" });
