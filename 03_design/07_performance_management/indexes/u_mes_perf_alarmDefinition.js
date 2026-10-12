// Indexes for u_mes_perf_alarmDefinition
db.getCollection("u_mes_perf_alarmDefinition").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_perf_alarmDefinition").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_perf_alarmDefinition").createIndex({ equipmentTypeId: 1 }, { name: "ix_equipmentTypeId" });
db.getCollection("u_mes_perf_alarmDefinition").createIndex({ authorizingRoleId: 1 }, { name: "ix_authorizingRoleId" });
db.getCollection("u_mes_perf_alarmDefinition").createIndex({ defaultReasonCodeId: 1 }, { name: "ix_defaultReasonCodeId" });
db.getCollection("u_mes_perf_alarmDefinition").createIndex({ escalationRuleId: 1 }, { name: "ix_escalationRuleId" });
