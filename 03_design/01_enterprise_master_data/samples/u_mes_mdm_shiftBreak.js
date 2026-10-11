// Sample document for u_mes_mdm_shiftBreak (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_shiftBreak").insertOne({
  _id: "SH-A-B001",
  recordNo: "A-B001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  shiftId: "SH-A",
  shiftName: "Shift A",
  sequenceNo: NumberInt(1),
  name: "Lunch break",
  startTimeLocal: "06:00",
  durationMinutes: NumberInt(480),
  paid: true,
  schemaVersion: NumberInt(1)
});
