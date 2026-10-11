// Sample document for u_mes_qual_nonconformanceContainmentAction (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_nonconformanceContainmentAction").insertOne({
  _id: "NCR-2026-000118-CA001",
  recordNo: "2026-000118-CA001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  nonconformanceId: "NCR-2026-000118",
  nonconformanceName: "Leak test failures on caliper LH",
  actionNo: NumberInt(1),
  description: "Hold all units assembled with seal lot S260921-SEL-004 and retest 100 percent",
  ownerUserId: "USR-10087",
  ownerUserName: "Anita Kulkarni",
  completedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
