// Sample document for u_mes_qlt_msaStudyTrial (illustrative; seed data is generated separately)
db.getCollection("u_mes_qlt_msaStudyTrial").insertOne({
  _id: "MSA-2026-0009-T001",
  recordNo: "2026-0009-T001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  msaStudyId: "MSA-2026-0009",
  msaStudyName: "2026-0009",
  appraiserUserId: "USR-10087",
  appraiserUserName: "Anita Kulkarni",
  partNo: NumberInt(4),
  trialNo: NumberInt(2),
  measuredValue: NumberDecimal("54.018"),
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
