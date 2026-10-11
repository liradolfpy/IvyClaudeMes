// Indexes for u_mes_mast_workCalendarException
db.getCollection("u_mes_mast_workCalendarException").createIndex({ workCalendarId: 1, sequenceNo: 1 }, { name: "ux_workCalendarId_sequenceNo", unique: true });
