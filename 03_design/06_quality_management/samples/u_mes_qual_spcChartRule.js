// Sample document for u_mes_qual_spcChartRule (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_spcChartRule").insertOne({
  _id: "SPC-C012-CNC-01-R001",
  recordNo: "C012-CNC-01-R001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  spcChartId: "SPC-C012-CNC-01",
  spcChartName: "Piston bore diameter, X-bar R, CNC-01",
  sequenceNo: NumberInt(1),
  rule: "Earliest Due Date",
  schemaVersion: NumberInt(1)
});
