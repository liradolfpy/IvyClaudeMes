// Sample document for u_mes_eqp_lossCategory (illustrative; seed data is generated separately)
db.getCollection("u_mes_eqp_lossCategory").insertOne({
  _id: "LSC-BREAKDOWN",
  recordNo: "BREAKDOWN",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Breakdown",
  description: "Unplanned equipment failure",
  oeeImpact: "Availability",
  sixBigLossNo: NumberInt(1),
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
