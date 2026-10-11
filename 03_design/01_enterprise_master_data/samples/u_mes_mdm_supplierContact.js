// Sample document for u_mes_mdm_supplierContact (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_supplierContact").insertOne({
  _id: "SUP-S1042-C001",
  recordNo: "S1042-C001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  supplierId: "SUP-S1042",
  supplierName: "Konkan Precision Pistons Pvt. Ltd.",
  sequenceNo: NumberInt(1),
  name: "Mahesh Gawde",
  businessFunction: "Quality",
  email: "sunil.jadhav@varunabrakes.example",
  phone: "+91-2135-555-0142",
  schemaVersion: NumberInt(1)
});
