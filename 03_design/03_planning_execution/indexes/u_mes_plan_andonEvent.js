// Indexes for u_mes_plan_andonEvent
db.getCollection("u_mes_plan_andonEvent").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_plan_andonEvent").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_plan_andonEvent").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_plan_andonEvent").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_plan_andonEvent").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_plan_andonEvent").createIndex({ andonTypeId: 1 }, { name: "ix_andonTypeId" });
db.getCollection("u_mes_plan_andonEvent").createIndex({ reasonCodeId: 1 }, { name: "ix_reasonCodeId" });
db.getCollection("u_mes_plan_andonEvent").createIndex({ siteId: 1, raisedAt: -1 }, { name: "ix_siteId_raisedAt" });
