// Sample document for u_mes_exe_changeoverStep (illustrative; seed data is generated separately)
db.getCollection("u_mes_exe_changeoverStep").insertOne({
  _id: "CHG-20260930-ASY-01-01-S001",
  recordNo: "20260930-ASY-01-01-S001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  changeoverId: "CHG-20260930-ASY-01-01",
  changeoverName: "20260930-ASY-01-01",
  stepNo: NumberInt(70),
  description: "Replace nutrunner socket with the RH variant socket",
  internalExternal: "Internal",
  completedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  completedById: "USR-10231",
  completedBy: "Sunil Jadhav",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
