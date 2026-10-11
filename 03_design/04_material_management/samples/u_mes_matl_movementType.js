// Sample document for u_mes_matl_movementType (illustrative; seed data is generated separately)
db.getCollection("u_mes_matl_movementType").insertOne({
  _id: "MVT-ISSUE-LINE",
  recordNo: "ISSUE-LINE",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Issue To Line",
  description: "Issue of components from stores to a line-side location",
  erpMovementType: "261",
  stockEffect: "Decrease",
  requiresReason: false,
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
