// Sample document for u_mes_prod_ppeItem (illustrative; seed data is generated separately)
db.getCollection("u_mes_prod_ppeItem").insertOne({
  _id: "PPE-SAFETY-GLASSES",
  recordNo: "SAFETY-GLASSES",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Safety Glasses",
  description: "Safety Glasses",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
