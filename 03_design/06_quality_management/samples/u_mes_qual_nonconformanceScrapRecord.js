// Sample document for u_mes_qual_nonconformanceScrapRecord (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_nonconformanceScrapRecord").insertOne({
  _id: "NCR-2026-000118-SR001",
  recordNo: "2026-000118-SR001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  nonconformanceId: "NCR-2026-000118",
  nonconformanceName: "Leak test failures on caliper LH",
  sequenceNo: NumberInt(1),
  scrapRecordId: "SCR-2026-000203",
  scrapRecordName: "2026-000203",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
