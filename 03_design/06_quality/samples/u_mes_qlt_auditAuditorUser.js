// Sample document for u_mes_qlt_auditAuditorUser (illustrative; seed data is generated separately)
db.getCollection("u_mes_qlt_auditAuditorUser").insertOne({
  _id: "AUD-LPA-2026-0931-AU001",
  recordNo: "LPA-2026-0931-AU001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  auditId: "AUD-LPA-2026-0931",
  auditName: "Layered process audit, Assembly line 1, week 40",
  sequenceNo: NumberInt(1),
  auditorUserId: "USR-10087",
  auditorUserName: "Anita Kulkarni",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
