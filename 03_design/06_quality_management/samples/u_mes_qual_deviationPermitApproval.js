// Sample document for u_mes_qual_deviationPermitApproval (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_deviationPermitApproval").insertOne({
  _id: "DEV-2026-0006-A001",
  recordNo: "2026-0006-A001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  deviationPermitId: "DEV-2026-0006",
  deviationPermitName: "Anodising thickness upper limit deviation",
  sequenceNo: NumberInt(1),
  businessFunction: "Quality",
  userId: "USR-10087",
  userName: "Anita Kulkarni",
  decision: "Approved",
  decidedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
