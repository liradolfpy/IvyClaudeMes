// Sample document for u_mes_mast_siteCertificate (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_siteCertificate").insertOne({
  _id: "SITE-PN1-C001",
  recordNo: "PN1-C001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  sequenceNo: NumberInt(1),
  standard: "IATF 16949:2016",
  certificateNo: "IATF-0412877",
  issuedById: "USR-10045",
  issuedBy: "Rajesh Patil",
  validFrom: ISODate("2026-03-31T18:30:00.000+0000"),
  validTo: ISODate("2027-03-31T18:29:59.000+0000"),
  schemaVersion: NumberInt(1)
});
