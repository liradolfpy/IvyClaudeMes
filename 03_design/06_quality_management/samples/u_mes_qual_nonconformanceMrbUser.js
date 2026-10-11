// Sample document for u_mes_qual_nonconformanceMrbUser (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_nonconformanceMrbUser").insertOne({
  _id: "NCR-2026-000118-MU001",
  recordNo: "2026-000118-MU001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  nonconformanceId: "NCR-2026-000118",
  nonconformanceName: "Leak test failures on caliper LH",
  sequenceNo: NumberInt(1),
  mrbUserId: "USR-10019",
  mrbUserName: "Meera Deshpande",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
