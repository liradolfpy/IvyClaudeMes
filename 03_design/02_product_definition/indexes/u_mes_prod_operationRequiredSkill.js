// Indexes for u_mes_prod_operationRequiredSkill
db.getCollection("u_mes_prod_operationRequiredSkill").createIndex({ operationId: 1, requiredSkillId: 1 }, { name: "ux_operationId_requiredSkillId", unique: true });
db.getCollection("u_mes_prod_operationRequiredSkill").createIndex({ requiredSkillId: 1, operationId: 1 }, { name: "ix_requiredSkillId_operationId" });
