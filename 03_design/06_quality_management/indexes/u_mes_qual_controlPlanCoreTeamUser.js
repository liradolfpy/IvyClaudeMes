// Indexes for u_mes_qual_controlPlanCoreTeamUser
db.getCollection("u_mes_qual_controlPlanCoreTeamUser").createIndex({ controlPlanId: 1, coreTeamUserId: 1 }, { name: "ux_controlPlanId_coreTeamUserId", unique: true });
db.getCollection("u_mes_qual_controlPlanCoreTeamUser").createIndex({ coreTeamUserId: 1, controlPlanId: 1 }, { name: "ix_coreTeamUserId_controlPlanId" });
