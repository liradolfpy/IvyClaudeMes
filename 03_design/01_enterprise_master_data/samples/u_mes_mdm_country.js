// Sample document for u_mes_mdm_country (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_country").insertOne({
  _id: "CTY-IN",
  recordNo: "IN",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "India",
  isoAlpha3Code: "IND",
  dialCode: "+91",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
