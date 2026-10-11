// Sample document for u_mes_mdm_workCalendarException (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_workCalendarException").insertOne({
  _id: "CAL-PN1-2026-E001",
  recordNo: "PN1-2026-E001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  workCalendarId: "CAL-PN1-2026",
  workCalendarName: "Chakan Plant Calendar 2026",
  sequenceNo: NumberInt(1),
  exceptionDate: ISODate("2026-03-31T18:30:00.000+0000"),
  exceptionType: "Public Holiday",
  description: "Gandhi Jayanti",
  isWorking: true,
  schemaVersion: NumberInt(1)
});
