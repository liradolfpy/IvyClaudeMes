// Sample document for u_mes_mast_transporter (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_transporter").insertOne({
  _id: "TRP-DRC",
  recordNo: "DRC",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Deccan Road Carriers",
  gstin: "27AAACV4521K1Z6",
  phone: "+91-2135-555-0142",
  email: "sunil.jadhav@varunabrakes.example",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
