// Indexes for u_mes_qlt_pfmeaCoreTeamUser
db.getCollection("u_mes_qlt_pfmeaCoreTeamUser").createIndex({ pfmeaId: 1, coreTeamUserId: 1 }, { name: "ux_pfmeaId_coreTeamUserId", unique: true });
db.getCollection("u_mes_qlt_pfmeaCoreTeamUser").createIndex({ coreTeamUserId: 1, pfmeaId: 1 }, { name: "ix_coreTeamUserId_pfmeaId" });
