// Indexes for u_mes_mdm_workCalendarException
db.getCollection("u_mes_mdm_workCalendarException").createIndex({ workCalendarId: 1, sequenceNo: 1 }, { name: "ux_workCalendarId_sequenceNo", unique: true });
