// Sample document for u_mes_mdm_rolePermission (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_rolePermission").insertOne({
  _id: "ROLE-OPERATOR-P001",
  recordNo: "OPERATOR-P001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  roleId: "ROLE-OPERATOR",
  roleName: "Production Operator",
  sequenceNo: NumberInt(1),
  permissionId: "PRM-operationExecution.complete",
  permissionName: "Complete an operation",
  schemaVersion: NumberInt(1)
});
