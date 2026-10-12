// Indexes for u_mes_syst_escalationRuleLevel
db.getCollection("u_mes_syst_escalationRuleLevel").createIndex({ escalationRuleId: 1, level: 1 }, { name: "ux_escalationRuleId_level", unique: true });
db.getCollection("u_mes_syst_escalationRuleLevel").createIndex({ roleId: 1 }, { name: "ix_roleId" });
db.getCollection("u_mes_syst_escalationRuleLevel").createIndex({ notificationTypeId: 1 }, { name: "ix_notificationTypeId" });
