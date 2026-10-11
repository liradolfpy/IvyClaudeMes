// Sample document for u_mes_mast_shift (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_shift").insertOne({
  _id: "SH-A",
  recordNo: "A",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Shift A",
  startTimeLocal: "06:00",
  endTimeLocal: "14:00",
  crossesMidnight: false,
  durationMinutes: NumberInt(480),
  plannedProductionMinutes: NumberInt(430),
  shiftAllowancePerDay: NumberDecimal("0.00"),
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
