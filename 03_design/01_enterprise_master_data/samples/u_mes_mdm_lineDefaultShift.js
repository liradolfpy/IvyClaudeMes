// Sample document for u_mes_mdm_lineDefaultShift (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_lineDefaultShift").insertOne({
  _id: "LN-ASY-01-DS001",
  recordNo: "ASY-01-DS001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  lineId: "LN-ASY-01",
  lineName: "Caliper Assembly Line 1",
  sequenceNo: NumberInt(1),
  defaultShiftId: "SH-A",
  defaultShiftName: "Shift A",
  schemaVersion: NumberInt(1)
});
