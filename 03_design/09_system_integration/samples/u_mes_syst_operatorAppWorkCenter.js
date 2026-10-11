// Sample document for u_mes_syst_operatorAppWorkCenter (illustrative; seed data is generated separately)
db.getCollection("u_mes_syst_operatorAppWorkCenter").insertOne({
  _id: "APP-APP-TRQ-01-WC001",
  recordNo: "APP-TRQ-01-WC001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  operatorAppId: "APP-APP-TRQ-01",
  operatorAppName: "Torque station operator app",
  sequenceNo: NumberInt(1),
  workCenterId: "WC-TRQ-01",
  workCenterName: "Bleed Screw Torque Station",
  schemaVersion: NumberInt(1)
});
