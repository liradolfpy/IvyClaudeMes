// Sample document for u_mes_syst_operatorAppOperation (illustrative; seed data is generated separately)
db.getCollection("u_mes_syst_operatorAppOperation").insertOne({
  _id: "APP-APP-TRQ-01-O001",
  recordNo: "APP-TRQ-01-O001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  operatorAppId: "APP-APP-TRQ-01",
  operatorAppName: "Torque station operator app",
  sequenceNo: NumberInt(1),
  operationId: "OPN-OP070",
  operationName: "Bleed screw torque",
  schemaVersion: NumberInt(1)
});
