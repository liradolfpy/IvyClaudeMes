// Sample document for u_mes_plan_indirectActivity (illustrative; seed data is generated separately)
db.getCollection("u_mes_plan_indirectActivity").insertOne({
  _id: "IND-WAIT-MAT",
  recordNo: "WAIT-MAT",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Waiting For Material",
  description: "Waiting For Material",
  isPaid: true,
  costCenterId: "CC-5120",
  costCenterName: "Assembly Line 1",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
