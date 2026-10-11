// Sample document for u_mes_mast_manufacturer (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_manufacturer").insertOne({
  _id: "MFR-ATLAS-COPCO",
  recordNo: "ATLAS-COPCO",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Atlas Copco",
  description: "Atlas Copco",
  countryId: "CTY-IN",
  countryName: "India",
  website: "https://www.varunabrakes.example",
  supportPhone: "+91-20-5550-0188",
  status: "Active",
  schemaVersion: NumberInt(1)
});
