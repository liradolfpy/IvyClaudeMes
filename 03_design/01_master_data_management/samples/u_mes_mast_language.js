// Sample document for u_mes_mast_language (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_language").insertOne({
  _id: "LNG-en",
  recordNo: "en",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "English",
  nativeName: "English",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
