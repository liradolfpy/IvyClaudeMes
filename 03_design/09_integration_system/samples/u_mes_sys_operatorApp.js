// Sample document for u_mes_sys_operatorApp (illustrative; seed data is generated separately)
db.getCollection("u_mes_sys_operatorApp").insertOne({
  _id: "APP-APP-TRQ-01",
  recordNo: "APP-TRQ-01",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Torque station operator app",
  appType: "Operator Station",
  version: NumberInt(3),
  publishedById: "USR-10045",
  publishedBy: "Rajesh Patil",
  publishedAt: ISODate("2026-03-31T18:30:00.000+0000"),
  approvedById: "USR-10019",
  approvedBy: "Meera Deshpande",
  approvedAt: ISODate("2026-03-31T18:30:00.000+0000"),
  previousVersionOperatorAppId: "APP-APP-TRQ-01-V2",
  previousVersionOperatorAppName: "Torque station operator app",
  status: "Released",
  schemaVersion: NumberInt(1)
});
