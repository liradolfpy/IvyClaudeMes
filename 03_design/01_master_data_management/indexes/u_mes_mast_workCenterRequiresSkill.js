// Indexes for u_mes_mast_workCenterRequiresSkill
db.getCollection("u_mes_mast_workCenterRequiresSkill").createIndex({ workCenterId: 1, requiresSkillId: 1 }, { name: "ux_workCenterId_requiresSkillId", unique: true });
db.getCollection("u_mes_mast_workCenterRequiresSkill").createIndex({ requiresSkillId: 1, workCenterId: 1 }, { name: "ix_requiresSkillId_workCenterId" });
