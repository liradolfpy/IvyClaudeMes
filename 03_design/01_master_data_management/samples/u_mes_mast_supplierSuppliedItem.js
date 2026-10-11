// Sample document for u_mes_mast_supplierSuppliedItem (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_supplierSuppliedItem").insertOne({
  _id: "SUP-S1042-SI001",
  recordNo: "S1042-SI001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  supplierId: "SUP-S1042",
  supplierName: "Konkan Precision Pistons Pvt. Ltd.",
  sequenceNo: NumberInt(1),
  suppliedItemId: "ITM-5110-10-0100",
  suppliedItemName: "Front Brake Caliper Assembly, LH",
  schemaVersion: NumberInt(1)
});
