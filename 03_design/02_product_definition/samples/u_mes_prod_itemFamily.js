// Sample document for u_mes_prod_itemFamily (illustrative; seed data is generated separately)
db.getCollection("u_mes_prod_itemFamily").insertOne({
  _id: "IFM-FRONT-CALIPER",
  recordNo: "FRONT-CALIPER",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Front Caliper",
  description: "Front Caliper",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
