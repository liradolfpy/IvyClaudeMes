// Sample document for u_mes_mast_unitOfMeasure (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_unitOfMeasure").insertOne({
  _id: "UOM-EA",
  recordNo: "EA",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Each",
  scope: "Enterprise",
  symbol: "N.m",
  dimension: "Torque",
  baseUnitOfMeasureId: null,
  baseUnitOfMeasureName: null,
  factorToBase: NumberDecimal("1.000000"),
  offsetToBase: NumberDecimal("0.000000"),
  decimalPlaces: NumberInt(1),
  isoCode: "NU",
  isBaseUnit: false,
  status: "Active",
  schemaVersion: NumberInt(1)
});
