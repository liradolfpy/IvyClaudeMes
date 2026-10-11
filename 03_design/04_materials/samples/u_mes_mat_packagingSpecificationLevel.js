// Sample document for u_mes_mat_packagingSpecificationLevel (illustrative; seed data is generated separately)
db.getCollection("u_mes_mat_packagingSpecificationLevel").insertOne({
  _id: "PKS-5110-10-0100-SML-01-L001",
  recordNo: "5110-10-0100-SML-01-L001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  packagingSpecificationId: "PKS-5110-10-0100-SML-01",
  packagingSpecificationName: "5110-10-0100-SML-01",
  levelNo: NumberInt(2),
  packTypeId: "PKT-BIN",
  packTypeName: "Bin",
  quantity: NumberInt(1),
  lengthMm: NumberDecimal("600.0"),
  widthMm: NumberDecimal("400.0"),
  heightMm: NumberDecimal("280.0"),
  schemaVersion: NumberInt(1)
});
