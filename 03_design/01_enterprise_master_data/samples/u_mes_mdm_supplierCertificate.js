// Sample document for u_mes_mdm_supplierCertificate (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_supplierCertificate").insertOne({
  _id: "SUP-S1042-C2001",
  recordNo: "S1042-C2001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  supplierId: "SUP-S1042",
  supplierName: "Konkan Precision Pistons Pvt. Ltd.",
  sequenceNo: NumberInt(1),
  standard: "IATF 16949:2016",
  certificateNo: "IATF-0412877",
  validTo: ISODate("2027-03-31T18:29:59.000+0000"),
  schemaVersion: NumberInt(1)
});
