// Sample document for u_mes_mdm_workCalendar (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_workCalendar").insertOne({
  _id: "CAL-PN1-2026",
  recordNo: "PN1-2026",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Chakan Plant Calendar 2026",
  year: NumberInt(2026),
  workingDaysCount: NumberInt(303),
  validFrom: ISODate("2026-03-31T18:30:00.000+0000"),
  validTo: ISODate("2027-03-31T18:29:59.000+0000"),
  status: "Active",
  schemaVersion: NumberInt(1)
});
