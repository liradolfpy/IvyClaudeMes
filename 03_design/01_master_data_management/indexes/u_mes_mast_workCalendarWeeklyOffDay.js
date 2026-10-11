// Indexes for u_mes_mast_workCalendarWeeklyOffDay
db.getCollection("u_mes_mast_workCalendarWeeklyOffDay").createIndex({ workCalendarId: 1, sequenceNo: 1 }, { name: "ux_workCalendarId_sequenceNo", unique: true });
