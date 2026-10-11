// Sample document for u_mes_syst_operatorAppDeviceBinding (illustrative; seed data is generated separately)
db.getCollection("u_mes_syst_operatorAppDeviceBinding").insertOne({
  _id: "APP-APP-TRQ-01-DB001",
  recordNo: "APP-TRQ-01-DB001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  operatorAppId: "APP-APP-TRQ-01",
  operatorAppName: "Torque station operator app",
  sequenceNo: NumberInt(1),
  iotDeviceId: "IOT-NR-CTRL-01",
  iotDeviceName: "Nutrunner controller, torque station 1",
  purpose: "Tightening result",
  schemaVersion: NumberInt(1)
});
