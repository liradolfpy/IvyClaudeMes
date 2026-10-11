// Sample document for u_mes_mdm_skillCategory (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_skillCategory").insertOne({
  _id: "SKC-PROCESS",
  recordNo: "PROCESS",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Process",
  description: "Process",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
