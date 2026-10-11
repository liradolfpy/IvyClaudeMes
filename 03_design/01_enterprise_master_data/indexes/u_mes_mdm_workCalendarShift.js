// Indexes for u_mes_mdm_workCalendarShift
db.getCollection("u_mes_mdm_workCalendarShift").createIndex({ workCalendarId: 1, shiftId: 1 }, { name: "ux_workCalendarId_shiftId", unique: true });
db.getCollection("u_mes_mdm_workCalendarShift").createIndex({ shiftId: 1, workCalendarId: 1 }, { name: "ix_shiftId_workCalendarId" });
