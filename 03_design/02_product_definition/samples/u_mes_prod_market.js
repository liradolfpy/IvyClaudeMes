// Sample document for u_mes_prod_market (illustrative; seed data is generated separately)
db.getCollection("u_mes_prod_market").insertOne({
  _id: "MKT-DOM",
  recordNo: "DOM",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Domestic",
  description: "Domestic",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
