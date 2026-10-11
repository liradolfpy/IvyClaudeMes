// Sample document for u_mes_mast_equipmentIotDevice (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_equipmentIotDevice").insertOne({
  _id: "EQ-TRQ-01-NR1-ID001",
  recordNo: "TRQ-01-NR1-ID001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  equipmentId: "EQ-TRQ-01-NR1",
  equipmentName: "DC Nutrunner Station 1",
  sequenceNo: NumberInt(1),
  iotDeviceId: "IOT-NR-CTRL-01",
  iotDeviceName: "Nutrunner controller, torque station 1",
  schemaVersion: NumberInt(1)
});
