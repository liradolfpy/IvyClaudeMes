// Sample document for u_mes_sys_deviceType (illustrative; seed data is generated separately)
db.getCollection("u_mes_sys_deviceType").insertOne({
  _id: "DVT-NR-CTRL",
  recordNo: "NR-CTRL",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Nutrunner Controller",
  description: "Nutrunner Controller",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
