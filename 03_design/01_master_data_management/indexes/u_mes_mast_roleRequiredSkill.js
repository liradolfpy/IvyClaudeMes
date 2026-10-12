// Indexes for u_mes_mast_roleRequiredSkill
db.getCollection("u_mes_mast_roleRequiredSkill").createIndex({ roleId: 1, requiredSkillId: 1 }, { name: "ux_roleId_requiredSkillId", unique: true });
db.getCollection("u_mes_mast_roleRequiredSkill").createIndex({ requiredSkillId: 1, roleId: 1 }, { name: "ix_requiredSkillId_roleId" });
