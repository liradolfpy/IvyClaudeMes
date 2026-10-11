// Indexes for u_mes_plan_productionSchedule
db.getCollection("u_mes_plan_productionSchedule").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_plan_productionSchedule").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_plan_productionSchedule").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_plan_productionSchedule").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_plan_productionSchedule").createIndex({ workCalendarId: 1 }, { name: "ix_workCalendarId" });
db.getCollection("u_mes_plan_productionSchedule").createIndex({ siteId: 1, productionDate: -1 }, { name: "ix_siteId_productionDate" });
