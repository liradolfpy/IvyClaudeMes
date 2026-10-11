// Sample document for u_mes_mast_userRole (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_userRole").insertOne({
  _id: "USR-10231-R001",
  recordNo: "10231-R001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  userId: "USR-10231",
  userName: "Sunil Jadhav",
  sequenceNo: NumberInt(1),
  roleId: "ROLE-OPERATOR",
  roleName: "Production Operator",
  schemaVersion: NumberInt(1)
});
