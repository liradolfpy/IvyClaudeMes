// Indexes for u_mes_mdm_workCalendarLine
db.getCollection("u_mes_mdm_workCalendarLine").createIndex({ workCalendarId: 1, lineId: 1 }, { name: "ux_workCalendarId_lineId", unique: true });
db.getCollection("u_mes_mdm_workCalendarLine").createIndex({ lineId: 1, workCalendarId: 1 }, { name: "ix_lineId_workCalendarId" });
