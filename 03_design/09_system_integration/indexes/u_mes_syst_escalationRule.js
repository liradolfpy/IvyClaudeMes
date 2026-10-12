// Indexes for u_mes_syst_escalationRule
db.getCollection("u_mes_syst_escalationRule").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_escalationRule").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_escalationRule").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_syst_escalationRule").createIndex({ firstResponderRoleId: 1 }, { name: "ix_firstResponderRoleId" });
db.getCollection("u_mes_syst_escalationRule").createIndex({ requiredSkillId: 1 }, { name: "ix_requiredSkillId" });
