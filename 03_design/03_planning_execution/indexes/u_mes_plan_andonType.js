// Indexes for u_mes_plan_andonType
db.getCollection("u_mes_plan_andonType").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_plan_andonType").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_plan_andonType").createIndex({ responsibleDepartmentId: 1 }, { name: "ix_responsibleDepartmentId" });
db.getCollection("u_mes_plan_andonType").createIndex({ escalationRuleId: 1 }, { name: "ix_escalationRuleId" });
