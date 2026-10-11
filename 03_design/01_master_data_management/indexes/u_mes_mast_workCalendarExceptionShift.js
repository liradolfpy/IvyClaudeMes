// Indexes for u_mes_mast_workCalendarExceptionShift
db.getCollection("u_mes_mast_workCalendarExceptionShift").createIndex({ workCalendarExceptionId: 1, shiftId: 1 }, { name: "ux_workCalendarExceptionId_shiftId", unique: true });
db.getCollection("u_mes_mast_workCalendarExceptionShift").createIndex({ shiftId: 1, workCalendarExceptionId: 1 }, { name: "ix_shiftId_workCalendarExceptionId" });
