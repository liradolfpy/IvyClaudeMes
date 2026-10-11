// Sample document for u_mes_mdm_commodity (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_commodity").insertOne({
  _id: "CMD-MACH-STEEL",
  recordNo: "MACH-STEEL",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Machined Steel Parts",
  description: "Machined Steel Parts",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
