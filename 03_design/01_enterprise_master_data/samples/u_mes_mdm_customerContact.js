// Sample document for u_mes_mdm_customerContact (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_customerContact").insertOne({
  _id: "CUS-SML-C001",
  recordNo: "SML-C001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  customerId: "CUS-SML",
  customerName: "Sahyadri Motors Ltd.",
  sequenceNo: NumberInt(1),
  name: "Priya Nair",
  businessFunction: "Quality",
  email: "sunil.jadhav@varunabrakes.example",
  phone: "+91-2135-555-0142",
  schemaVersion: NumberInt(1)
});
