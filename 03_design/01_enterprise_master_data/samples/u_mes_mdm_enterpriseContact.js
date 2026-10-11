// Sample document for u_mes_mdm_enterpriseContact (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_enterpriseContact").insertOne({
  _id: "ENT-VBS-C001",
  recordNo: "VBS-C001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  enterpriseId: "ENT-VBS",
  enterpriseName: "Varuna Brake Systems Pvt. Ltd.",
  sequenceNo: NumberInt(1),
  name: "Arvind Kelkar",
  jobTitle: "Plant Head",
  email: "sunil.jadhav@varunabrakes.example",
  phone: "+91-2135-555-0142",
  schemaVersion: NumberInt(1)
});
