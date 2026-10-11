// Sample document for u_mes_qlt_dispositionType (illustrative; seed data is generated separately)
db.getCollection("u_mes_qlt_dispositionType").insertOne({
  _id: "DSP-T-REWORK",
  recordNo: "REWORK",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Rework",
  description: "Bring the part back to specification on the rework routing",
  requiresRework: true,
  requiresScrap: true,
  requiresCustomerApproval: true,
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
