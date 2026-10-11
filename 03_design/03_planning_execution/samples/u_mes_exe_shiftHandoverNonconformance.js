// Sample document for u_mes_exe_shiftHandoverNonconformance (illustrative; seed data is generated separately)
db.getCollection("u_mes_exe_shiftHandoverNonconformance").insertOne({
  _id: "SHO-20260929-ASY-01-A-N001",
  recordNo: "20260929-ASY-01-A-N001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  shiftHandoverId: "SHO-20260929-ASY-01-A",
  shiftHandoverName: "20260929-ASY-01-A",
  sequenceNo: NumberInt(1),
  nonconformanceId: "NCR-2026-000118",
  nonconformanceName: "Leak test failures on caliper LH",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
