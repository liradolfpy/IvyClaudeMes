// Sample document for u_mes_qual_checkSheetResultAnswer (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_checkSheetResultAnswer").insertOne({
  _id: "CKR-20260929-A-TRQ-01-A001",
  recordNo: "20260929-A-TRQ-01-A001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  checkSheetResultId: "CKR-20260929-A-TRQ-01",
  checkSheetResultName: "20260929-A-TRQ-01",
  itemNo: NumberInt(1),
  answerText: "Yes",
  answerNumber: null,
  passed: true,
  comment: "Verified against customer drawing revision D",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
