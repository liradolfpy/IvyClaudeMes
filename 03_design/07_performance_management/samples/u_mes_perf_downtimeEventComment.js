// Sample document for u_mes_perf_downtimeEventComment (illustrative; seed data is generated separately)
db.getCollection("u_mes_perf_downtimeEventComment").insertOne({
  _id: "DT-20260929-0009-C001",
  recordNo: "20260929-0009-C001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  downtimeEventId: "DT-20260929-0009",
  downtimeEventName: "20260929-0009",
  sequenceNo: NumberInt(1),
  commentedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  authorUserId: "USR-10087",
  authorUserName: "Anita Kulkarni",
  commentText: "Spare socket taken from tool crib",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
