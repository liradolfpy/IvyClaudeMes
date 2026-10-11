// Sample document for u_mes_prod_engineeringChangeApproval (illustrative; seed data is generated separately)
db.getCollection("u_mes_prod_engineeringChangeApproval").insertOne({
  _id: "ECN-2026-0031-A001",
  recordNo: "2026-0031-A001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  engineeringChangeId: "ECN-2026-0031",
  engineeringChangeName: "Bleed screw torque window revised",
  stepNo: NumberInt(70),
  businessFunction: "Quality",
  userId: "USR-10231",
  userName: "Sunil Jadhav",
  decision: "Approved",
  decidedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  comment: "Verified against customer drawing revision D",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
