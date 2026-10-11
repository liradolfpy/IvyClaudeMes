// Sample document for u_mes_mdm_role (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_role").insertOne({
  _id: "ROLE-OPERATOR",
  recordNo: "OPERATOR",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Production Operator",
  scope: "Enterprise",
  description: "Runs operations at an assigned station and records results",
  canSign: true,
  approvalLimitInr: NumberDecimal("0.00"),
  isSystemRole: false,
  status: "Active",
  schemaVersion: NumberInt(1)
});
