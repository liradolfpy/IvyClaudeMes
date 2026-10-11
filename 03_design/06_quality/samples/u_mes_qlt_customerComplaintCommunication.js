// Sample document for u_mes_qlt_customerComplaintCommunication (illustrative; seed data is generated separately)
db.getCollection("u_mes_qlt_customerComplaintCommunication").insertOne({
  _id: "CMP-2026-0004-C001",
  recordNo: "2026-0004-C001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  customerComplaintId: "CMP-2026-0004",
  customerComplaintName: "Bleed screw cap missing on three calipers at customer line",
  sequenceNo: NumberInt(1),
  communicatedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  direction: "Inbound",
  communicationSummary: "Containment report with sorting result sent to customer SQA",
  authorUserId: "USR-10087",
  authorUserName: "Anita Kulkarni",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
