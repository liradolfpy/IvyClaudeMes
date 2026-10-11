// Sample document for u_mes_mdm_permission (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_permission").insertOne({
  _id: "PRM-operationExecution.complete",
  recordNo: "operationExecution.complete",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Complete an operation",
  description: "Complete an operation",
  resourceName: "operationExecution",
  actionName: "complete",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
