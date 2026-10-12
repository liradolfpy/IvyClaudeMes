// Indexes for u_mes_maint_reliabilitySummary
db.getCollection("u_mes_maint_reliabilitySummary").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_maint_reliabilitySummary").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_maint_reliabilitySummary").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_maint_reliabilitySummary").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_maint_reliabilitySummary").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_maint_reliabilitySummary").createIndex({ siteId: 1, periodStartAt: -1 }, { name: "ix_siteId_periodStartAt" });
