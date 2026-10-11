// Sample document for u_mes_qual_spcChartControlLimit (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_spcChartControlLimit").insertOne({
  _id: "SPC-C012-CNC-01-CL001",
  recordNo: "C012-CNC-01-CL001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  spcChartId: "SPC-C012-CNC-01",
  spcChartName: "Piston bore diameter, X-bar R, CNC-01",
  revisionNo: NumberInt(2),
  effectiveFrom: ISODate("2026-03-31T18:30:00.000+0000"),
  ucl: NumberDecimal("54.031"),
  centerLine: NumberDecimal("54.021"),
  lcl: NumberDecimal("54.011"),
  uclRange: NumberDecimal("0.036"),
  centerLineRange: NumberDecimal("0.017"),
  lclRange: NumberDecimal("0.000"),
  basedOnSubgroups: NumberInt(25),
  schemaVersion: NumberInt(1)
});
