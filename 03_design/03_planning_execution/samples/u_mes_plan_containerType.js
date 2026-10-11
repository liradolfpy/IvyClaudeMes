// Sample document for u_mes_plan_containerType (illustrative; seed data is generated separately)
db.getCollection("u_mes_plan_containerType").insertOne({
  _id: "CTT-RB-6040",
  recordNo: "RB-6040",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Returnable Bin 600 x 400",
  description: "Returnable Bin 600 x 400",
  lengthMm: NumberDecimal("600.0"),
  widthMm: NumberDecimal("400.0"),
  heightMm: NumberDecimal("280.0"),
  tareWeightKg: NumberDecimal("2.100"),
  isReturnable: false,
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
