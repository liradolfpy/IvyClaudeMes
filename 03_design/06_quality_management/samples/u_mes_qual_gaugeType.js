// Sample document for u_mes_qual_gaugeType (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_gaugeType").insertOne({
  _id: "GTY-BORE-GAUGE",
  recordNo: "BORE-GAUGE",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Bore Gauge",
  description: "Bore Gauge",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
