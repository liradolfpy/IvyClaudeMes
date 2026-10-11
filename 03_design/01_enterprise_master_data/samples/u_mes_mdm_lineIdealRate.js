// Sample document for u_mes_mdm_lineIdealRate (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_lineIdealRate").insertOne({
  _id: "LN-ASY-01-IR001",
  recordNo: "ASY-01-IR001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  lineId: "LN-ASY-01",
  lineName: "Caliper Assembly Line 1",
  sequenceNo: NumberInt(1),
  itemId: "ITM-5110-10-0100",
  itemName: "Front Brake Caliper Assembly, LH",
  idealCycleTimeSec: NumberDecimal("32.0"),
  targetPerHour: NumberInt(100),
  schemaVersion: NumberInt(1)
});
