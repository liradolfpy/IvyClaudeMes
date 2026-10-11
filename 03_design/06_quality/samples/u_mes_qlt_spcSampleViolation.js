// Sample document for u_mes_qlt_spcSampleViolation (illustrative; seed data is generated separately)
db.getCollection("u_mes_qlt_spcSampleViolation").insertOne({
  _id: "SPS-C012-CNC-01-0147-V001",
  recordNo: "C012-CNC-01-0147-V001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  spcSampleId: "SPS-C012-CNC-01-0147",
  spcSampleName: "C012-CNC-01-0147",
  sequenceNo: NumberInt(1),
  rule: "Earliest Due Date",
  description: "One point beyond the upper control limit",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
