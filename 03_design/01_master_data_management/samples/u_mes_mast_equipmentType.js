// Sample document for u_mes_mast_equipmentType (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_equipmentType").insertOne({
  _id: "EQT-DC-NUTRUNNER",
  recordNo: "DC-NUTRUNNER",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "DC Nutrunner",
  description: "Electric tightening spindle with torque and angle control",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
