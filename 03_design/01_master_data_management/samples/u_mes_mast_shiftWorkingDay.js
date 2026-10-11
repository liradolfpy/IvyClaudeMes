// Sample document for u_mes_mast_shiftWorkingDay (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_shiftWorkingDay").insertOne({
  _id: "SH-A-WD001",
  recordNo: "A-WD001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  shiftId: "SH-A",
  shiftName: "Shift A",
  sequenceNo: NumberInt(1),
  workingDay: "Monday",
  schemaVersion: NumberInt(1)
});
